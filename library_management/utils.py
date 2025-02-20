# from frappe.utils import now

# now()

import frappe

# def create_todo():
#     doc = frappe.get_doc({
#         "doctype": "ToDo",
#         "description": "Complete the Frappe Document API task"
#     })
#     doc.insert()
#     frappe.db.commit()
#     print(f"Created ToDo: {doc.name}")


# import frappe

# def test_function():
#     task_id = "TASK00002"

#     if not frappe.db.exists("Task", task_id):
#         return f"Task {task_id} does not exist"

#     doc = frappe.get_doc("Task", task_id)
#     return f"Task Found: {doc.subject}"




def fetch_server_names():
    """
    Fetches the list of employee names using frappe.db.get_list.
    This function returns a list of employee names (pluck mode).
    """
    # frappe.db.get_list is aliased as frappe.get_list as well.
    # Using pluck='name' returns just a list of names.
    server_names = frappe.db.get_list("Server", pluck="name")
    return server_names
