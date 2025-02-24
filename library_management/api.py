import frappe
from frappe import _

@frappe.whitelist()  # This decorator exposes the function as an API endpoint
def get_all_server_data():
    """
    API endpoint to fetch all columns of all records from the 'Server' doctype.
    Accessible via: /api/method/library_management.api.get_all_server_data
    """
    server_data = frappe.db.get_list("Server", fields=["*"])
    return {"server_data": server_data}

@frappe.whitelist() 
def get_all_server_name():
    server_name = frappe.db.get_list("Server", plunk="name")
    return {"server_name": server_name}

@frappe.whitelist(allow_guest=True)
def get_public_tasks():
    """
    Returns a list of tasks with limited fields, accessible without authentication.
    """
    tasks = frappe.get_all("Task", fields=["name", "subject", "status"])
    return tasks

    

import frappe
import requests

@frappe.whitelist()
def fetch_users():
    base_url = frappe.utils.get_url()  # e.g., http://127.0.0.1:8000
    headers = {
        "Authorization": "token 928ac424a2324ce:c87a89cb859c0c9"
    }
    doc_type = "User"
    response = requests.get(f"{base_url}/api/resource/{doc_type}", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        frappe.throw(f"Failed to fetch data: {response.status_code} - {response.text}")

