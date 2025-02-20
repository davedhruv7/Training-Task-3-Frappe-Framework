import frappe
from frappe import _

@frappe.whitelist()
def lead_test(id):
    doc = frappe.get_doc("Server",id)
    return doc