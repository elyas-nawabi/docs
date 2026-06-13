"""Generate ERP-aligned sidebar menu JSON from docs folder structure.

Run:
  python tools/generate_sidebar_menu_json.py

Writes:
  assets/menu.json
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from erp_menu_structure import LABEL_OVERRIDES, MENU_TREE

ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "assets" / "doc" / "umbrella"
OUT_FILES = [
    ROOT / "assets" / "menu.json",
    ROOT / "static" / "assets" / "menu.json",
]

# ERP-aligned labels for health/* submodules (avoids duplicate "Health > Health").
HEALTH_SUBMODULE_LABELS: dict[str, str] = {
    "health": "Clinical",
    "health_archives": "Archives",
    "health_caldav": "CalDAV",
    "health_contact_tracing": "Contact Tracing",
    "health_dentistry": "Dentistry",
    "health_disability": "Functioning and Disability",
    "health_ems": "Ambulances",
    "health_federation": "Federation",
    "health_genetics": "Genetics",
    "health_gyneco": "Obstetrics",
    "health_icu": "Intensive Care",
    "health_imaging": "Medical Imaging",
    "health_inpatient": "Hospitalizations",
    "health_insurance": "Insurances",
    "health_iss": "Injury Surveillance",
    "health_lab": "Laboratory",
    "health_lifestyle": "Misc",
    "health_nursing": "Nursing",
    "health_ophthalmology": "Ophthalmology",
    "health_orthanc": "Orthanc",
    "health_pediatrics": "Pediatrics",
    "health_pediatrics_growth_charts_who": "Pediatrics Growth Charts WHO",
    "health_reporting": "Reporting",
    "health_services": "Health Services",
    "health_socieconomics": "Demographics",
    "health_surgery": "Surgeries",
}


@dataclass
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
    tokens = [t for t in re.split(r"\s+", name) if t]
    acronyms = {"hr": "HR", "api": "API", "ui": "UI", "id": "ID", "icu": "ICU", "ems": "EMS"}
    out = []
    for t in tokens:
        low = t.lower()
        out.append(acronyms.get(low, t[:1].upper() + t[1:]))
    return " ".join(out)


def module_label(module_dir_name: str) -> str:
    if module_dir_name == "health":
        return "Health"
    if module_dir_name == "umbrella":
        return "Umbrella (Core)"
    if module_dir_name.startswith("umbrella_"):
        return titleize(module_dir_name[len("umbrella_") :])
    return titleize(module_dir_name)


def module_icon(module_dir_name: str) -> str:
    if module_dir_name == "umbrella":
        return "icon-shield-check"
    if module_dir_name == "health" or module_dir_name.startswith("health_"):
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
            head = yml.read_text(encoding="utf-8-sig").lstrip()[:32]
        except OSError:
            continue
        if head.lower().startswith("openapi:"):
            return yml
    return None


def scan_doc_index() -> dict[str, str]:
    """Map doc_key (posix path under umbrella/) -> assets-relative yaml path."""
    index: dict[str, str] = {}
    for d in sorted(p for p in DOCS_ROOT.rglob("*") if p.is_dir()):
        if " copy" in d.as_posix().lower():
            continue
        entry = find_openapi_entrypoint_yaml(d)
        if entry is None:
            continue
        key = d.relative_to(DOCS_ROOT).as_posix()
        rel = entry.relative_to(ROOT).as_posix()
        index[key] = rel
    return index


def leaf_label(doc_key: str) -> str:
    if doc_key in LABEL_OVERRIDES:
        return LABEL_OVERRIDES[doc_key]
    leaf = doc_key.rsplit("/", 1)[-1]
    return titleize(leaf)


def make_leaf(doc_key: str, doc_index: dict[str, str], used: set[str]) -> Node | None:
    path = doc_index.get(doc_key)
    if not path:
        return None
    used.add(doc_key)
    return Node(label=leaf_label(doc_key), icon="icon-list", path=path)


def health_submodule_label(name: str) -> str:
    if name in HEALTH_SUBMODULE_LABELS:
        return HEALTH_SUBMODULE_LABELS[name]
    if name.startswith("health_"):
        return titleize(name[len("health_") :])
    return module_label(name)


def build_health_group(doc_index: dict[str, str], used: set[str]) -> Node:
    health_root = DOCS_ROOT / "health"
    children: list[Node] = []
    if health_root.is_dir():
        for sub in sorted(p for p in health_root.iterdir() if p.is_dir()):
            if " copy" in sub.name.lower():
                continue
            leaves: list[Node] = []
            sub_key = sub.relative_to(DOCS_ROOT).as_posix()
            if sub_key in doc_index and sub_key not in used:
                leaf = make_leaf(sub_key, doc_index, used)
                if leaf:
                    leaves.append(leaf)
            for d in sorted(p for p in sub.rglob("*") if p.is_dir()):
                key = d.relative_to(DOCS_ROOT).as_posix()
                if key not in doc_index or key in used:
                    continue
                leaf = make_leaf(key, doc_index, used)
                if leaf:
                    leaves.append(leaf)
            if leaves:
                leaves.sort(key=lambda n: n.label.lower())
                children.append(
                    Node(
                        label=health_submodule_label(sub.name),
                        icon=module_icon(sub.name),
                        children=leaves,
                    )
                )
    return Node(label="Health", icon="icon-heart-pulse", children=children)


def build_from_spec(
    spec: dict,
    doc_index: dict[str, str],
    used: set[str],
    default_icon: str = "icon-folder",
) -> Node | None:
    if "module_group" in spec:
        if spec["module_group"] == "health":
            return build_health_group(doc_index, used)
        return None

    if "doc" in spec:
        leaf = make_leaf(spec["doc"], doc_index, used)
        if leaf and "label" in spec:
            return Node(label=spec["label"], icon="icon-list", path=leaf.path)
        return leaf

    children_specs = spec.get("children", [])
    children: list[Node] = []
    icon = spec.get("icon", default_icon)
    for child_spec in children_specs:
        child = build_from_spec(child_spec, doc_index, used, icon)
        if child:
            children.append(child)

    if not children:
        return None

    return Node(label=spec["label"], icon=icon, children=children)


def build_fallback_group(
    doc_index: dict[str, str], used: set[str]
) -> Node | None:
    remaining = sorted(k for k in doc_index if k not in used)
    if not remaining:
        return None

    by_module: dict[str, list[str]] = {}
    for key in remaining:
        module = key.split("/", 1)[0]
        by_module.setdefault(module, []).append(key)

    children: list[Node] = []
    for module in sorted(by_module):
        leaves = [
            make_leaf(k, doc_index, used)
            for k in sorted(by_module[module])
        ]
        leaves = [l for l in leaves if l]
        if leaves:
            children.append(
                Node(
                    label=module_label(module),
                    icon=module_icon(module),
                    children=leaves,
                )
            )

    if not children:
        return None

    return Node(label="Other APIs", icon="icon-folder", children=children)


def main() -> None:
    if not DOCS_ROOT.exists():
        raise SystemExit(f"Docs root not found: {DOCS_ROOT}")

    doc_index = scan_doc_index()
    used: set[str] = set()
    menu: list[Node] = []
    missing: list[str] = []

    def collect_missing(spec: dict) -> None:
        if "doc" in spec and spec["doc"] not in doc_index:
            missing.append(spec["doc"])
        for child in spec.get("children", []):
            collect_missing(child)

    for top_spec in MENU_TREE:
        collect_missing(top_spec)
        node = build_from_spec(top_spec, doc_index, used)
        if node:
            menu.append(node)

    fallback = build_fallback_group(doc_index, used)
    if fallback:
        menu.append(fallback)

    payload = json.dumps([n.to_dict() for n in menu], indent=2)
    for out_file in OUT_FILES:
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(payload, encoding="utf-8")
        print(f"Wrote {out_file}")

    print(f"Menu has {len(menu)} top-level items")
    print(f"Indexed {len(doc_index)} API docs, placed {len(used)} in menu tree")
    if missing:
        print(f"Warning: {len(missing)} ERP menu doc keys not found:", file=sys.stderr)
        for m in missing[:20]:
            print(f"  - {m}", file=sys.stderr)
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more", file=sys.stderr)


if __name__ == "__main__":
    main()
