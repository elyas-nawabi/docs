"""Generate a sidebar menu JSON from the docs folder structure.

This keeps index.html maintainable and ensures the menu stays in sync with
assets/doc/umbrella.

Run:
  python tools/generate_sidebar_menu_json.py

It writes:
  assets/menu.json
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "assets" / "doc" / "umbrella"
OUT_FILE = ROOT / "assets" / "menu.json"


@dataclass(frozen=True)
class Node:
    label: str
    icon: str
    path: str | None = None
    children: list["Node"] | None = None

    def to_dict(self) -> dict:
        data: dict = {"label": self.label, "icon": self.icon}
        if self.path:
            data["path"] = self.path
        if self.children:
            data["children"] = [c.to_dict() for c in self.children]
        return data


def titleize(name: str) -> str:
    name = name.replace("_", " ").replace("-", " ").strip()
    if not name:
        return name

    # Keep common acronyms.
    tokens = [t for t in re.split(r"\s+", name) if t]
    acronyms = {"hr": "HR", "api": "API", "ui": "UI", "id": "ID"}
    out = []
    for t in tokens:
        low = t.lower()
        if low in acronyms:
            out.append(acronyms[low])
        else:
            out.append(t[:1].upper() + t[1:])
    return " ".join(out)


def module_label(module_dir_name: str) -> str:
    if module_dir_name == "health":
        return "Health"
    if module_dir_name == "umbrella":
        return "Umbrella (Core)"

    if module_dir_name.startswith("umbrella_"):
        base = module_dir_name[len("umbrella_") :]
        return titleize(base)

    return titleize(module_dir_name)


def module_icon(module_dir_name: str) -> str:
    # Use lucide icons already present in index.html for safety.
    if module_dir_name == "umbrella":
        return "icon-shield-check"
    if module_dir_name == "health":
        return "icon-heart-pulse"

    if module_dir_name.startswith("umbrella_hr"):
        return "icon-users-round"

    mapping = {
        "umbrella_party": "icon-users",
        "umbrella_company": "icon-building-2",
        "umbrella_product": "icon-layout-grid",
        "umbrella_purchase": "icon-shopping-cart",
        "umbrella_sale": "icon-store",
        "umbrella_stock": "icon-warehouse",
        "umbrella_currency": "icon-dollar-sign",
        "umbrella_banking": "icon-banknote",
        "umbrella_financial_accounting": "icon-building",
        "umbrella_country": "icon-globe",
        "umbrella_mail": "icon-mail",
        "umbrella_resource": "icon-hard-drive",
        "umbrella_administration": "icon-wrench",
        "umbrella_planning": "icon-calendar-days",
        "umbrella_planning_holidays": "icon-calendar-days",
        "umbrella_planning_hr_skills": "icon-calendar-days",
    }
    return mapping.get(module_dir_name, "icon-folder")


def find_openapi_entrypoint_yaml(dir_path: Path) -> Path | None:
    if not dir_path.is_dir():
        return None

    for yml in sorted(dir_path.glob("*.yaml")):
        try:
            # Use utf-8-sig to gracefully handle UTF-8 files with BOM
            # (common on Windows when edited via PowerShell Set-Content).
            head = yml.read_text(encoding="utf-8-sig").lstrip()[:32]
        except OSError:
            continue
        if head.lower().startswith("openapi:"):
            return yml
    return None


def build_leaf_nodes(module_root: Path) -> list[Node]:
    """Find all directories containing an OpenAPI root yaml and return leaf nodes."""

    leaves: list[tuple[str, str]] = []

    # include module-level yaml if present (for modules without resources)
    entry = find_openapi_entrypoint_yaml(module_root)
    if entry is not None:
        rel = entry.relative_to(ROOT).as_posix()
        leaves.append((module_label(module_root.name), rel))

    for d in sorted(p for p in module_root.rglob("*") if p.is_dir()):
        entry = find_openapi_entrypoint_yaml(d)
        if entry is None:
            continue

        rel = entry.relative_to(ROOT).as_posix()
        # Label uses the directory name; for nested dirs, include parent group for clarity.
        parts = d.relative_to(module_root).parts
        if len(parts) == 1:
            label = titleize(parts[0])
        else:
            label = " / ".join(titleize(p) for p in parts)
        leaves.append((label, rel))

    # de-dupe by path
    seen: set[str] = set()
    out: list[Node] = []
    for label, rel in leaves:
        if rel in seen:
            continue
        seen.add(rel)
        out.append(Node(label=label, icon="icon-list", path=rel))

    # Sort leaves by label
    out.sort(key=lambda n: n.label.lower())
    return out


def group_by_prefix(modules: Iterable[Path]) -> list[Node]:
    """Create a curated top-level grouping (HR and Planning aggregated)."""

    modules = list(modules)

    def pick(name: str) -> Path | None:
        for m in modules:
            if m.name == name:
                return m
        return None

    # Aggregate HR modules.
    hr_modules = [m for m in modules if m.name.startswith("umbrella_hr")]
    planning_modules = [m for m in modules if m.name.startswith("umbrella_planning")]

    used = set(m.name for m in hr_modules + planning_modules)

    top: list[Node] = []

    if pick("umbrella"):
        m = pick("umbrella")
        top.append(
            Node(
                label=module_label(m.name),
                icon=module_icon(m.name),
                children=build_leaf_nodes(m),
            )
        )
        used.add(m.name)

    # Common business modules in a reasonable order
    ordered = [
        "umbrella_party",
        "umbrella_company",
        "umbrella_product",
        "umbrella_purchase",
        "umbrella_sale",
        "umbrella_stock",
        "umbrella_currency",
        "umbrella_banking",
        "umbrella_financial_accounting",
        "umbrella_administration",
        "umbrella_country",
        "umbrella_mail",
        "umbrella_resource",
    ]
    for name in ordered:
        m = pick(name)
        if not m:
            continue
        top.append(
            Node(
                label=module_label(m.name),
                icon=module_icon(m.name),
                children=build_leaf_nodes(m),
            )
        )
        used.add(m.name)

    # Human Resources aggregate
    if hr_modules:
        hr_children: list[Node] = []
        for m in sorted(hr_modules, key=lambda p: p.name):
            hr_children.append(
                Node(
                    label=module_label(m.name),
                    icon=module_icon(m.name),
                    children=build_leaf_nodes(m),
                )
            )
        top.append(
            Node(label="Human Resources", icon="icon-users-round", children=hr_children)
        )

    # Planning aggregate
    if planning_modules:
        plan_children: list[Node] = []
        for m in sorted(planning_modules, key=lambda p: p.name):
            plan_children.append(
                Node(
                    label=module_label(m.name),
                    icon=module_icon(m.name),
                    children=build_leaf_nodes(m),
                )
            )
        top.append(
            Node(label="Planning", icon="icon-calendar-days", children=plan_children)
        )

    # Health special-case
    health = pick("health")
    if health:
        health_children: list[Node] = []
        for sub in sorted(p for p in health.iterdir() if p.is_dir()):
            sub_label = titleize(sub.name)
            health_children.append(
                Node(
                    label=sub_label,
                    icon="icon-heart-pulse",
                    children=build_leaf_nodes(sub),
                )
            )
        top.append(
            Node(label="Health", icon="icon-heart-pulse", children=health_children)
        )
        used.add("health")

    # Any remaining modules not in curated order
    for m in sorted(modules, key=lambda p: p.name):
        if m.name in used:
            continue
        top.append(
            Node(
                label=module_label(m.name),
                icon=module_icon(m.name),
                children=build_leaf_nodes(m),
            )
        )

    return top


def main() -> None:
    if not DOCS_ROOT.exists():
        raise SystemExit(f"Docs root not found: {DOCS_ROOT}")

    modules = [p for p in DOCS_ROOT.iterdir() if p.is_dir() and p.name != "schemas"]
    menu = group_by_prefix(modules)

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(
        json.dumps([n.to_dict() for n in menu], indent=2), encoding="utf-8"
    )
    print(f"Wrote {OUT_FILE} with {len(menu)} top-level items")


if __name__ == "__main__":
    main()
