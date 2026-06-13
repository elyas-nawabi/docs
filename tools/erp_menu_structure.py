"""ERP-aligned sidebar menu tree for umbrella-api-docs.

Leaf nodes reference doc folder keys relative to assets/doc/umbrella/, e.g.
  "umbrella_party/address" -> assets/doc/umbrella/umbrella_party/address/*.yaml

Display labels on leaves default from ERP menu names via LABEL_OVERRIDES.
"""

from __future__ import annotations

# doc_key -> sidebar label (ERP menu name)
LABEL_OVERRIDES: dict[str, str] = {
    "umbrella/fields_structure": "Fields Structure",
    "umbrella/get_access": "Get Access by Models",
    "umbrella/get_menu": "Get User Menu",
    "umbrella/models_list": "Models List",
    "umbrella/smart_enum": "Smart Enum",
    "umbrella/user_warning": "User Warning",
    "umbrella_party/address": "Address Formats",
    "umbrella_party/party": "People",
    "umbrella_party/contact_mechanism": "Contact Mechanisms",
    "umbrella_party/category": "Categories",
    "umbrella_party/party_tax_identifier": "Party Tax Identifier",
    "umbrella_product/configuration": "Configuration",
    "umbrella_product/product": "Products",
    "umbrella_product/variant": "Variants",
    "umbrella_product/product_line": "Suppliers",
    "umbrella_product/product_category": "Categories",
    "umbrella_product/unit_of_measure": "Units of Measure",
    "umbrella_product/uom_category": "UOM Categories",
    "umbrella_product/reporting": "Margins",
    "umbrella_financial_accounting/configuration": "Configuration",
    "umbrella_financial_accounting/account_type_template": "Account Types",
    "umbrella_financial_accounting/move_template": "Moves",
    "umbrella_financial_accounting/account_template": "Accounts",
    "umbrella_financial_accounting/tax_code_template": "Tax Codes",
    "umbrella_financial_accounting/tax_template": "Taxes",
    "umbrella_financial_accounting/tax_rule_template": "Tax Rules",
    "umbrella_financial_accounting/account_type": "Account Types",
    "umbrella_financial_accounting/account": "Accounts",
    "umbrella_financial_accounting/cashflow": "Account Tags",
    "umbrella_financial_accounting/fiscal_year": "Fiscal Years",
    "umbrella_financial_accounting/journal": "Journals",
    "umbrella_financial_accounting/tax": "Taxes",
    "umbrella_financial_accounting/tax_group": "Groups",
    "umbrella_financial_accounting/tax_code": "Codes",
    "umbrella_financial_accounting/tax_rule": "Rules",
    "umbrella_financial_accounting/account_invoice/payment_term": "Payment Terms",
    "umbrella_financial_accounting/account_statement/statement_journal": "Statement Journals",
    "umbrella_financial_accounting/account_payment/payment_journal": "Payment Journals",
    "umbrella_financial_accounting/account_invoice/invoice": "Invoices",
    "umbrella_financial_accounting/account_payment/payment": "Payments",
    "umbrella_financial_accounting/journal_period": "Journals - Periods",
    "umbrella_financial_accounting/account_move": "Account Moves",
    "umbrella_financial_accounting/account_statement/statement": "Statements",
    "umbrella_financial_accounting/account_statement/line_group": "Line Groups",
    "umbrella_financial_accounting/reconcile": "Reconcile Accounts",
    "umbrella_financial_accounting/fiscal_period": "Close Periods",
    "umbrella_financial_accounting/balance_non_deferral": "Balance Non-Deferral",
    "umbrella_financial_accounting/reports": "General Ledger",
    "umbrella_stock/configuration": "Configuration",
    "umbrella_stock/location": "Locations",
    "umbrella_stock/period": "Periods",
    "umbrella_stock/location_lead_time": "Location Lead Times",
    "umbrella_stock/shipment_in": "Supplier Shipments",
    "umbrella_stock/shipment_in_return": "Supplier Returns",
    "umbrella_stock/shipment_out": "Customer Shipments",
    "umbrella_stock/shipment_out_return": "Customer Returns",
    "umbrella_stock/shipment_internal": "Internal Shipments",
    "umbrella_stock/inventory": "Inventories",
    "umbrella_stock/move": "Moves",
    "umbrella_stock/lot": "Lots",
    "umbrella_company/company": "Companies",
    "umbrella_company/employee": "Employees",
    "umbrella_banking/bank": "Banks",
    "umbrella_banking/account": "Accounts",
    "umbrella_currency/currency": "Currencies",
    "umbrella_currency/scheduled_rate_update": "Scheduled Rate Updates",
    "umbrella_hr/department": "Departments",
    "umbrella_hr/departure_reason": "Departure Reasons",
    "umbrella_hr/employee_category": "Employee Tags",
    "umbrella_hr/work_location": "Work Locations",
    "umbrella_hr/job": "Job Positions",
    "umbrella_hr/contract_type": "Employment Types",
    "umbrella_hr_contract/contract": "Contracts",
    "umbrella_hr_contract/payroll_structure_type": "Salary Structure Types",
    "umbrella_hr_recruitment/applications": "Applications",
    "umbrella_hr_recruitment/candidates": "Candidates",
    "umbrella_hr_recruitment/stages": "Stages",
    "umbrella_hr_recruitment/degrees": "Applicant Degrees",
    "umbrella_hr_recruitment/tags": "Tags",
    "umbrella_hr_recruitment/refuse_reasons": "Refuse Reasons",
    "umbrella_hr_recruitment/emails": "Emails",
    "umbrella_hr_attendance/attendance": "Attendances",
    "umbrella_hr_attendance/attendance_overtime": "Extra Hours",
    "umbrella_hr_skills/resume_line_types": "Resume Line Types",
    "umbrella_hr_skills/skill_types": "Skill Types",
    "umbrella_hr_skills/skill_levels": "Skill Levels",
    "umbrella_hr_skills/skills": "Skills",
    "umbrella_hr_work_entry/work_entries": "Work Entries",
    "umbrella_hr_work_entry/work_entry_types": "Work Entry Types",
    "umbrella_hr_payroll/headcount": "Headcount",
    "umbrella_hr_payroll/headcount_working_rates": "Headcount Working Rate",
    "umbrella_hr_payroll/payroll_dashboard_warnings": "Payroll Dashboard Warnings",
    "umbrella_hr_payroll/payslips": "Payslips",
    "umbrella_hr_payroll/payslip_batches": "Payslip Batches",
    "umbrella_hr_payroll/salary_attachments": "Salary Attachments",
    "umbrella_hr_payroll/payroll_notes": "Payroll Notes",
    "umbrella_hr_payroll/salary_structures": "Salary Structures",
    "umbrella_hr_payroll/salary_rules": "Salary Rules",
    "umbrella_hr_payroll/salary_rule_categories": "Salary Rule Categories",
    "umbrella_hr_payroll/payslip_input_types": "Payslip Input Types",
    "umbrella_hr_payroll/rule_parameters": "Rule Parameters",
    "umbrella_hr_holidays/leave_type": "Time Off Types",
    "umbrella_hr_holidays/leave": "Time Off",
    "umbrella_hr_holidays/leave_allocation": "Allocations",
    "umbrella_hr_holidays/leave_accrual_plan": "Accrual Plans",
    "umbrella_hr_holidays/leave_accrual_plan_level": "Accrual Levels",
    "umbrella_hr_holidays/leave_mandatory_day": "Mandatory Days",
    "umbrella_hr_expense/expense_sheet": "Employee Expenses",
    "umbrella_hr_appraisal/appraisals": "Appraisals",
    "umbrella_hr_appraisal/appraisal_notes": "Appraisal Ratings",
    "umbrella_hr_appraisal_contract": "Appraisal Contract",
    "umbrella_planning": "Planning",
    "umbrella_planning_holidays": "Planning Holidays",
    "umbrella_planning_hr_skills": "Planning HR Skills",
    "umbrella_mail/activity_type": "Activity Types",
    "umbrella_mail/activity_plan": "Activity Plans",
    "umbrella_mail/activity": "Activity Overview",
    "umbrella_administration/users/user": "Users",
    "umbrella_administration/users/group": "Groups",
    "umbrella_administration/sequences/sequence": "Sequences",
    "umbrella_administration/sequences/sequence_strict": "Sequences Strict",
    "umbrella_administration/sequences/sequence_type": "Types",
    "umbrella_administration/modules/module": "Modules",
    "umbrella_administration/localization/lang": "Languages",
    "umbrella_administration/localization/translation": "Translations",
    "umbrella_administration/localization/message": "Messages",
    "umbrella_country/country": "Countries",
    "umbrella_country/organization": "Organizations",
    "umbrella_country/region": "Regions",
    "umbrella_resource/working_schedules": "Working Schedules",
    "umbrella_resource/resources": "Resources",
}

# Top-level ERP menu tree. Nodes are dicts with label, optional icon, children, and/or doc.
MENU_TREE: list[dict] = [
    {
        "label": "Umbrella (Core)",
        "icon": "icon-shield-check",
        "children": [
            {"doc": "umbrella/auth"},
            {"doc": "umbrella/fields_structure"},
            {"doc": "umbrella/get_access"},
            {"doc": "umbrella/get_menu"},
            {"doc": "umbrella/models_list"},
            {"doc": "umbrella/smart_enum"},
            {"doc": "umbrella/toolbar"},
            {"doc": "umbrella/user_warning"},
            {"doc": "umbrella/wizard"},
        ],
    },
    {
        "label": "Party",
        "icon": "icon-users",
        "children": [
            {
                "label": "Configuration",
                "children": [
                    {"doc": "umbrella_party/address"},
                ],
            },
            {
                "label": "Parties",
                "children": [
                    {"doc": "umbrella_party/party"},
                ],
            },
            {"doc": "umbrella_party/contact_mechanism"},
            {
                "label": "Categories",
                "children": [
                    {"doc": "umbrella_party/category"},
                ],
            },
            {"doc": "umbrella_party/party_tax_identifier"},
        ],
    },
    {
        "label": "Product",
        "icon": "icon-layout-grid",
        "children": [
            {"doc": "umbrella_product/configuration"},
            {
                "label": "Products",
                "children": [
                    {"doc": "umbrella_product/product"},
                    {"doc": "umbrella_product/variant"},
                    {"doc": "umbrella_product/product_line"},
                ],
            },
            {
                "label": "Categories",
                "children": [
                    {"doc": "umbrella_product/product_category"},
                ],
            },
            {"doc": "umbrella_product/unit_of_measure"},
            {"doc": "umbrella_product/uom_category"},
            {
                "label": "Reporting",
                "children": [
                    {"doc": "umbrella_product/reporting"},
                ],
            },
        ],
    },
    {
        "label": "Financial",
        "icon": "icon-building",
        "children": [
            {
                "label": "Configuration",
                "children": [
                    {"doc": "umbrella_financial_accounting/configuration"},
                    {
                        "label": "Templates",
                        "children": [
                            {"doc": "umbrella_financial_accounting/account_type_template"},
                            {"doc": "umbrella_financial_accounting/move_template"},
                            {"doc": "umbrella_financial_accounting/account_template"},
                            {"doc": "umbrella_financial_accounting/tax_code_template"},
                            {"doc": "umbrella_financial_accounting/tax_template"},
                            {"doc": "umbrella_financial_accounting/tax_rule_template"},
                        ],
                    },
                ],
            },
            {
                "label": "General Account",
                "children": [
                    {"doc": "umbrella_financial_accounting/account_type"},
                    {"doc": "umbrella_financial_accounting/account"},
                    {"doc": "umbrella_financial_accounting/cashflow"},
                ],
            },
            {"doc": "umbrella_financial_accounting/fiscal_year"},
            {"doc": "umbrella_financial_accounting/journal"},
            {
                "label": "Taxes",
                "children": [
                    {"doc": "umbrella_financial_accounting/tax"},
                    {"doc": "umbrella_financial_accounting/tax_group"},
                    {"doc": "umbrella_financial_accounting/tax_code"},
                    {"doc": "umbrella_financial_accounting/tax_rule"},
                ],
            },
            {
                "label": "Payment Terms",
                "children": [
                    {"doc": "umbrella_financial_accounting/account_invoice/payment_term"},
                    {"doc": "umbrella_financial_accounting/account_invoice/payment_method"},
                ],
            },
            {
                "label": "Statements",
                "children": [
                    {"doc": "umbrella_financial_accounting/account_statement/statement_journal"},
                ],
            },
            {
                "label": "Payments",
                "children": [
                    {"doc": "umbrella_financial_accounting/account_payment/payment_journal"},
                    {"doc": "umbrella_financial_accounting/account_payment/payment"},
                    {"doc": "umbrella_financial_accounting/account_payment/payment_group"},
                    {"doc": "umbrella_financial_accounting/account_payment/line_to_pay"},
                ],
            },
            {"doc": "umbrella_financial_accounting/account_invoice/invoice"},
            {
                "label": "Entries",
                "children": [
                    {"doc": "umbrella_financial_accounting/journal_period"},
                    {"doc": "umbrella_financial_accounting/account_move"},
                    {"doc": "umbrella_financial_accounting/account_move_line"},
                ],
            },
            {
                "label": "Statements",
                "children": [
                    {"doc": "umbrella_financial_accounting/account_statement/statement"},
                    {"doc": "umbrella_financial_accounting/account_statement/line_group"},
                ],
            },
            {
                "label": "Processing",
                "children": [
                    {"doc": "umbrella_financial_accounting/reconcile"},
                    {"doc": "umbrella_financial_accounting/fiscal_period"},
                    {"doc": "umbrella_financial_accounting/balance_non_deferral"},
                    {"doc": "umbrella_financial_accounting/write_off"},
                ],
            },
            {
                "label": "Reporting",
                "children": [
                    {"doc": "umbrella_financial_accounting/reports"},
                ],
            },
        ],
    },
    {
        "label": "Currency",
        "icon": "icon-dollar-sign",
        "children": [
            {"doc": "umbrella_currency/currency"},
            {"doc": "umbrella_currency/scheduled_rate_update"},
        ],
    },
    {
        "label": "Inventory & Stock",
        "icon": "icon-warehouse",
        "children": [
            {
                "label": "Configuration",
                "children": [
                    {"doc": "umbrella_stock/configuration"},
                    {"doc": "umbrella_stock/location"},
                    {"doc": "umbrella_stock/period"},
                    {"doc": "umbrella_stock/location_lead_time"},
                ],
            },
            {
                "label": "Shipments",
                "children": [
                    {"doc": "umbrella_stock/shipment_in"},
                    {"doc": "umbrella_stock/shipment_in_return"},
                    {"doc": "umbrella_stock/shipment_out"},
                    {"doc": "umbrella_stock/shipment_out_return"},
                    {"doc": "umbrella_stock/shipment_internal"},
                ],
            },
            {"doc": "umbrella_stock/inventory"},
            {"doc": "umbrella_stock/inventory_line"},
            {"doc": "umbrella_stock/move"},
            {"doc": "umbrella_stock/lot"},
            {"doc": "umbrella_stock/lot_trace"},
            {"doc": "umbrella_stock/lots_by_locations"},
        ],
    },
    {
        "label": "Companies",
        "icon": "icon-building-2",
        "children": [
            {"doc": "umbrella_company/company"},
            {"doc": "umbrella_company/employee"},
        ],
    },
    {
        "label": "Banking",
        "icon": "icon-banknote",
        "children": [
            {"doc": "umbrella_banking/bank"},
            {"doc": "umbrella_banking/account"},
        ],
    },
    {
        "label": "Human Resource",
        "icon": "icon-users-round",
        "children": [
            {
                "label": "Employees",
                "children": [
                    {"doc": "umbrella_hr/department"},
                    {"doc": "umbrella_hr/departure_reason"},
                    {"doc": "umbrella_hr/employee_category"},
                    {"doc": "umbrella_hr/work_location"},
                    {"doc": "umbrella_hr/job"},
                    {"doc": "umbrella_hr/contract_type"},
                ],
            },
            {
                "label": "Contracts",
                "children": [
                    {"doc": "umbrella_hr_contract/contract"},
                    {"doc": "umbrella_hr_contract/payroll_structure_type"},
                ],
            },
            {
                "label": "Recruitment",
                "children": [
                    {"doc": "umbrella_hr_recruitment/applications"},
                    {"doc": "umbrella_hr_recruitment/candidates"},
                    {"doc": "umbrella_hr_recruitment/stages"},
                    {"doc": "umbrella_hr_recruitment/degrees"},
                    {"doc": "umbrella_hr_recruitment/tags"},
                    {"doc": "umbrella_hr_recruitment/refuse_reasons"},
                    {"doc": "umbrella_hr_recruitment/emails"},
                ],
            },
            {
                "label": "Attendances",
                "children": [
                    {"doc": "umbrella_hr_attendance/attendance"},
                    {"doc": "umbrella_hr_attendance/attendance_overtime"},
                    {"doc": "umbrella_hr_attendance/overtime_ruleset"},
                    {"doc": "umbrella_hr_presence/check_presence"},
                    {"doc": "umbrella_hr_presence/company"},
                    {"doc": "umbrella_hr_presence/employees"},
                ],
            },
            {
                "label": "Skills",
                "children": [
                    {"doc": "umbrella_hr_skills/resume_line_types"},
                    {"doc": "umbrella_hr_skills/skill_types"},
                    {"doc": "umbrella_hr_skills/skill_levels"},
                    {"doc": "umbrella_hr_skills/skills"},
                    {"doc": "umbrella_hr_appraisal_skills/appraisal_skills"},
                ],
            },
            {
                "label": "Payroll",
                "children": [
                    {"doc": "umbrella_hr_work_entry/work_entries"},
                    {"doc": "umbrella_hr_work_entry/work_entry_types"},
                    {"doc": "umbrella_hr_payroll/headcount"},
                    {"doc": "umbrella_hr_payroll/headcount_working_rates"},
                    {"doc": "umbrella_hr_payroll/payroll_dashboard_warnings"},
                    {"doc": "umbrella_hr_payroll/payslips"},
                    {"doc": "umbrella_hr_payroll/payslip_batches"},
                    {"doc": "umbrella_hr_payroll/salary_attachments"},
                    {"doc": "umbrella_hr_payroll/payroll_notes"},
                    {
                        "label": "Configuration",
                        "children": [
                            {"doc": "umbrella_hr_payroll/salary_structures"},
                            {"doc": "umbrella_hr_payroll/salary_rules"},
                            {"doc": "umbrella_hr_payroll/salary_rule_categories"},
                            {"doc": "umbrella_hr_payroll/payslip_input_types"},
                            {"doc": "umbrella_hr_payroll/rule_parameters"},
                        ],
                    },
                ],
            },
            {
                "label": "Time Off",
                "children": [
                    {"doc": "umbrella_hr_holidays/leave_type"},
                    {"doc": "umbrella_hr_holidays/leave"},
                    {"doc": "umbrella_hr_holidays/leave_allocation"},
                    {"doc": "umbrella_hr_holidays/leave_accrual_plan"},
                    {"doc": "umbrella_hr_holidays/leave_accrual_plan_level"},
                    {"doc": "umbrella_hr_holidays/leave_mandatory_day"},
                ],
            },
            {"doc": "umbrella_hr_expense/expense_sheet"},
            {
                "label": "Appraisals",
                "children": [
                    {"doc": "umbrella_hr_appraisal/appraisals"},
                    {"doc": "umbrella_hr_appraisal/appraisal_notes"},
                    {"doc": "umbrella_hr_appraisal_contract"},
                ],
            },
            {
                "label": "Planning",
                "children": [
                    {"doc": "umbrella_planning"},
                    {"doc": "umbrella_planning_holidays"},
                    {"doc": "umbrella_planning_hr_skills"},
                ],
            },
            {
                "label": "Activities",
                "children": [
                    {"doc": "umbrella_mail/activity_type"},
                    {"doc": "umbrella_mail/activity_plan"},
                    {"doc": "umbrella_mail/activity"},
                    {"doc": "umbrella_mail/employee"},
                ],
            },
        ],
    },
    {
        "label": "Purchases",
        "icon": "icon-shopping-cart",
        "children": [
            {
                "label": "Configuration",
                "children": [
                    {"doc": "umbrella_purchase/configuration"},
                ],
            },
            {"doc": "umbrella_purchase/purchase"},
            {"doc": "umbrella_purchase/purchase_line"},
            {"doc": "umbrella_purchase/product_supplier"},
            {
                "label": "Reporting",
                "children": [
                    {"doc": "umbrella_purchase/reporting_purchase"},
                    {"doc": "umbrella_purchase/reporting_purchase_per_product"},
                    {"doc": "umbrella_purchase/reporting_purchase_per_supplier"},
                ],
            },
        ],
    },
    {
        "label": "Sales",
        "icon": "icon-store",
        "children": [
            {
                "label": "Configuration",
                "children": [
                    {"doc": "umbrella_sale/configuration"},
                ],
            },
            {"doc": "umbrella_sale/leads_and_opportunities"},
            {"doc": "umbrella_sale/sale"},
            {"doc": "umbrella_sale/sale_line"},
            {
                "label": "Reporting",
                "children": [
                    {"doc": "umbrella_sale/reporting_sale"},
                    {"doc": "umbrella_sale/reporting_sale_per_country"},
                    {"doc": "umbrella_sale/reporting_sale_per_customer"},
                    {"doc": "umbrella_sale/reporting_sale_per_customer_category"},
                    {"doc": "umbrella_sale/reporting_sale_per_product"},
                    {"doc": "umbrella_sale/reporting_sale_per_product_category"},
                    {"doc": "umbrella_sale/reporting_sale_per_region"},
                    {"doc": "umbrella_sale/reporting_sale_per_subdivision"},
                ],
            },
        ],
    },
    {
        "label": "Administration",
        "icon": "icon-wrench",
        "children": [
            {
                "label": "Users",
                "children": [
                    {"doc": "umbrella_administration/users/user"},
                    {"doc": "umbrella_administration/users/group"},
                ],
            },
            {
                "label": "Sequences",
                "children": [
                    {"doc": "umbrella_administration/sequences/sequence"},
                    {"doc": "umbrella_administration/sequences/sequence_strict"},
                    {"doc": "umbrella_administration/sequences/sequence_type"},
                ],
            },
            {
                "label": "Modules",
                "children": [
                    {"doc": "umbrella_administration/modules/module"},
                    {"doc": "umbrella_administration/modules/module_config_wizard_item"},
                ],
            },
            {
                "label": "Localization",
                "children": [
                    {"doc": "umbrella_administration/localization/lang"},
                    {"doc": "umbrella_administration/localization/translation"},
                    {"doc": "umbrella_administration/localization/message"},
                ],
            },
            {
                "label": "Countries",
                "children": [
                    {"doc": "umbrella_country/country"},
                    {"doc": "umbrella_country/organization"},
                    {
                        "label": "Areas",
                        "children": [
                            {"doc": "umbrella_country/region"},
                            {"doc": "umbrella_country/subdivision"},
                        ],
                    },
                ],
            },
            {
                "label": "User Interface",
                "children": [
                    {"doc": "umbrella_administration/user_interface/ui_menu"},
                    {"doc": "umbrella_administration/user_interface/view"},
                    {"doc": "umbrella_administration/user_interface/view_search"},
                    {"doc": "umbrella_administration/user_interface/view_tree_optional"},
                    {"doc": "umbrella_administration/user_interface/view_tree_state"},
                    {"doc": "umbrella_administration/user_interface/view_tree_width"},
                    {"doc": "umbrella_administration/user_interface/icon"},
                    {
                        "label": "Actions",
                        "children": [
                            {"doc": "umbrella_administration/user_interface/action"},
                            {"doc": "umbrella_administration/user_interface/action_report"},
                            {"doc": "umbrella_administration/user_interface/action_act_window"},
                            {"doc": "umbrella_administration/user_interface/action_url"},
                            {"doc": "umbrella_administration/user_interface/action_wizard"},
                            {"doc": "umbrella_administration/user_interface/email_template"},
                        ],
                    },
                ],
            },
            {"doc": "umbrella_administration/models/model"},
            {"doc": "umbrella_administration/ir/export_import"},
            {
                "label": "Resource",
                "children": [
                    {"doc": "umbrella_resource/working_schedules"},
                    {"doc": "umbrella_resource/resources"},
                ],
            },
        ],
    },
    {
        "label": "Health",
        "icon": "icon-heart-pulse",
        "module_group": "health",
    },
]
