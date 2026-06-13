"""Generate OpenAPI documentation for umbrella_hr_payroll REST resources.

Run from repo root:
  python tools/generate_payroll_api_docs.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "assets" / "doc" / "umbrella" / "umbrella_hr_payroll"
API_DOC_REF = "../../../api_doc.yaml#/components/schemas"

MODULE_PREFIX = "/hr-payroll"


def _auth401() -> str:
    return f"""    '401':
      description: Unauthorized.
      content:
        application/json:
          schema:
            $ref: '{API_DOC_REF}/HTTP401'
"""


def _auth404() -> str:
    return f"""    '404':
      description: Not Found.
      content:
        application/json:
          schema:
            $ref: '{API_DOC_REF}/HTTP404'
"""


def _get_search(tag: str, resource: str, op_id: str) -> str:
    return f"""post:
  tags:
    - {tag}
  summary: Search {resource}.
  description: Search {resource}.
  operationId: {op_id}
  requestBody:
    description: Optional filter criteria; send an empty JSON object for all records.
    content:
      application/json:
        schema:
          $ref: '{API_DOC_REF}/Filter'
  responses:
    '200':
      description: OK
      content:
        application/json:
          schema:
            $ref: 'schema.yaml'
{_auth401()}
"""


def _post_create(tag: str, resource: str, op_id: str, schema_name: str) -> str:
    return f"""post:
  tags:
    - {tag}
  summary: Create {resource}.
  description: Create {resource}.
  operationId: {op_id}
  requestBody:
    required: true
    content:
      application/json:
        schema:
          $ref: 'schemas/{schema_name}.yaml'
  responses:
    '201':
      description: Created
      content:
        application/json:
          schema:
            $ref: 'schema.yaml'
{_auth401()}
"""


def _delete_bulk(tag: str, resource: str, op_id: str) -> str:
    return f"""delete:
  tags:
    - {tag}
  summary: Delete {resource}.
  description: Delete one or more {resource} by id.
  operationId: {op_id}
  requestBody:
    required: true
    content:
      application/json:
        schema:
          type: object
          properties:
            ids:
              type: array
              items:
                type: integer
  responses:
    '200':
      description: OK
      content:
        application/json:
          schema:
            $ref: '{API_DOC_REF}/HTTP200'
{_auth401()}
"""


def _get_by_id(tag: str, resource: str, op_id: str) -> str:
    return f"""get:
  tags:
    - {tag}
  summary: Get {resource} by id.
  description: Get {resource} by id.
  operationId: {op_id}
  parameters:
    - name: obj_id
      in: path
      required: true
      schema:
        type: integer
  responses:
    '200':
      description: OK
      content:
        application/json:
          schema:
            $ref: 'schema.yaml'
{_auth401()}
{_auth404()}
"""


def _put_by_id(tag: str, resource: str, op_id: str, schema_name: str) -> str:
    return f"""put:
  tags:
    - {tag}
  summary: Update {resource}.
  description: Update {resource}.
  operationId: {op_id}
  parameters:
    - name: obj_id
      in: path
      required: true
      schema:
        type: integer
  requestBody:
    required: true
    content:
      application/json:
        schema:
          $ref: 'schemas/{schema_name}.yaml'
  responses:
    '200':
      description: OK
      content:
        application/json:
          schema:
            $ref: 'schema.yaml'
{_auth401()}
{_auth404()}
"""


def _action_get(tag: str, summary: str, op_id: str, path_suffix: str) -> str:
    fname = f"get_{path_suffix.replace('-', '_')}_by_id.yaml"
    content = f"""get:
  tags:
    - {tag}
  summary: {summary}.
  description: {summary}.
  operationId: {op_id}
  parameters:
    - name: obj_id
      in: path
      required: true
      schema:
        type: integer
  responses:
    '200':
      description: OK
      content:
        application/json:
          schema:
            $ref: '{API_DOC_REF}/HTTP200'
{_auth401()}
{_auth404()}
"""
    return fname, content


def _action_post(tag: str, summary: str, op_id: str, path_suffix: str) -> str:
    fname = f"post_{path_suffix.replace('-', '_')}.yaml"
    content = f"""post:
  tags:
    - {tag}
  summary: {summary}.
  description: {summary}.
  operationId: {op_id}
  parameters:
    - name: obj_id
      in: path
      required: true
      schema:
        type: integer
  responses:
    '200':
      description: OK
      content:
        application/json:
          schema:
            $ref: '{API_DOC_REF}/HTTP200'
{_auth401()}
{_auth404()}
"""
    return fname, content


RESOURCES = [
    {
        "folder": "payslips",
        "route": "payslips",
        "tag": "payslips",
        "label": "Payslips",
        "actions": [
            ("compute-sheet", "GET", "Compute payslip sheet", "computeSheet"),
            ("confirm", "GET", "Confirm payslip", "confirmPayslip"),
            ("mark-as-paid", "GET", "Mark payslip as paid", "markPayslipPaid"),
            ("cancel", "GET", "Cancel payslip", "cancelPayslip"),
            ("draft", "GET", "Reset payslip to draft", "draftPayslip"),
            ("print", "GET", "Print payslip", "printPayslip"),
        ],
    },
    {
        "folder": "payslip_batches",
        "route": "payslip-batches",
        "tag": "payslip_batches",
        "label": "Payslip Batches",
        "actions": [
            ("reset-to-draft", "GET", "Reset batch to draft", "resetPayslipBatchDraft"),
            ("confirm", "GET", "Confirm payslip batch", "confirmPayslipBatch"),
            ("validate", "GET", "Validate payslip batch", "validatePayslipBatch"),
            ("mark-as-paid", "GET", "Mark payslip batch as paid", "markPayslipBatchPaid"),
            ("generate-payslips", "POST", "Generate payslips for batch", "generatePayslips"),
        ],
    },
    {
        "folder": "salary_attachments",
        "route": "salary-attachments",
        "tag": "salary_attachments",
        "label": "Salary Attachments",
        "actions": [
            ("running", "GET", "Set salary attachment running", "runningSalaryAttachment"),
            ("mark-as-completed", "GET", "Mark salary attachment completed", "completeSalaryAttachment"),
            ("cancel", "GET", "Cancel salary attachment", "cancelSalaryAttachment"),
            ("draft", "GET", "Reset salary attachment to draft", "draftSalaryAttachment"),
            ("payslip-lines", "GET", "Get salary attachment payslip lines", "salaryAttachmentPayslipLines"),
        ],
    },
    {
        "folder": "salary_structures",
        "route": "salary-structures",
        "tag": "salary_structures",
        "label": "Salary Structures",
        "actions": [],
    },
    {
        "folder": "salary_rule_categories",
        "route": "salary-rule-categories",
        "tag": "salary_rule_categories",
        "label": "Salary Rule Categories",
        "actions": [],
    },
    {
        "folder": "salary_rules",
        "route": "salary-rules",
        "tag": "salary_rules",
        "label": "Salary Rules",
        "actions": [],
    },
    {
        "folder": "rule_parameters",
        "route": "rule-parameters",
        "tag": "rule_parameters",
        "label": "Rule Parameters",
        "actions": [],
    },
    {
        "folder": "payslip_input_types",
        "route": "payslip-input-types",
        "tag": "payslip_input_types",
        "label": "Payslip Input Types",
        "actions": [],
    },
    {
        "folder": "payroll_notes",
        "route": "payroll-notes",
        "tag": "payroll_notes",
        "label": "Payroll Notes",
        "actions": [],
    },
    {
        "folder": "headcount",
        "route": "headcount",
        "tag": "headcount",
        "label": "Headcount",
        "actions": [
            ("populate", "GET", "Populate headcount", "populateHeadcount"),
        ],
    },
    {
        "folder": "headcount_working_rates",
        "route": "headcount-working-rates",
        "tag": "headcount_working_rates",
        "label": "Headcount Working Rate",
        "actions": [],
    },
    {
        "folder": "payroll_dashboard_warnings",
        "route": "payroll-dashboard-warnings",
        "tag": "payroll_dashboard_warnings",
        "label": "Payroll Dashboard Warnings",
        "actions": [],
    },
]


def camel_case(name: str) -> str:
    parts = name.replace("-", "_").split("_")
    return parts[0] + "".join(p.title() for p in parts[1:])


def write_resource(res: dict) -> None:
    folder = res["folder"]
    route = res["route"]
    tag = res["tag"]
    label = res["label"]
    base = DOCS / folder
    base.mkdir(parents=True, exist_ok=True)
    schemas_dir = base / "schemas"
    schemas_dir.mkdir(exist_ok=True)

    schema_name = f"create-{route}"
    camel = camel_case(folder)

    (base / f"get_{folder}.yaml").write_text(
        _get_search(tag, label, f"search{camel.title()}"), encoding="utf-8"
    )
    post_del = _post_create(tag, label, f"create{camel.title()}", schema_name)
    post_del += "\n" + _delete_bulk(tag, label, f"delete{camel.title()}")
    (base / f"post_delete_{folder}.yaml").write_text(post_del, encoding="utf-8")
    get_put = _get_by_id(tag, label, f"get{camel.title()}ById")
    get_put += "\n" + _put_by_id(tag, label, f"update{camel.title()}", schema_name)
    (base / f"get_put_{folder}_by_id.yaml").write_text(get_put, encoding="utf-8")

    (base / "schema.yaml").write_text(
        """type: object
properties:
  data:
    type: object
    additionalProperties: true
  error:
    type: object
    nullable: true
  pagination:
    type: object
    nullable: true
  status:
    type: integer
  success_message:
    type: string
    nullable: true
""",
        encoding="utf-8",
    )

    (schemas_dir / f"{schema_name}.yaml").write_text(
        "type: object\nadditionalProperties: true\n", encoding="utf-8"
    )

    paths = [
        f"  '{MODULE_PREFIX}/{route}/search':",
        f"    $ref: 'get_{folder}.yaml'",
        f"  '{MODULE_PREFIX}/{route}':",
        f"    $ref: 'post_delete_{folder}.yaml'",
        f"  '{MODULE_PREFIX}/{route}/{{obj_id}}':",
        f"    $ref: 'get_put_{folder}_by_id.yaml'",
    ]

    for action_suffix, method, summary, op_id in res.get("actions", []):
        if method == "GET":
            fname, content = _action_get(tag, summary, op_id, action_suffix)
        else:
            fname, content = _action_post(tag, summary, op_id, action_suffix)
        (base / fname).write_text(content, encoding="utf-8")
        if method == "POST":
            paths.append(f"  '{MODULE_PREFIX}/{route}/{{obj_id}}/{action_suffix}':")
        else:
            paths.append(f"  '{MODULE_PREFIX}/{route}/{{obj_id}}/{action_suffix}':")
        paths.append(f"    $ref: '{fname}'")

    entry = f"""openapi: 3.1.0
servers:
  - url: 'http://api-alpha.umbrellaerp.com'
tags:
  - name: {tag}
    description: {label} — payroll data management.
paths:
{chr(10).join(paths)}
"""
    (base / f"{folder}.yaml").write_text(entry, encoding="utf-8")


def main() -> None:
    # Remove legacy placeholder
    placeholder = DOCS / "payroll"
    if placeholder.is_dir():
        import shutil

        shutil.rmtree(placeholder)

    for res in RESOURCES:
        write_resource(res)
        print(f"Wrote {res['folder']}")

    print(f"Generated {len(RESOURCES)} payroll API doc sets under {DOCS}")


if __name__ == "__main__":
    main()
