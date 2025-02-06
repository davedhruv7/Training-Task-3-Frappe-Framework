# Copyright (c) 2025, Dhruv and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ClientSideScripting(Document):
	pass

# @frappe.whitelist()
# def frappe_call(msg):
# 	import time
# 	time.sleep(5)
# 	frappe.msgprint(msg)

# 	# return "Hi This Message from frappe call"

@frappe.whitelist()
def insert_call():
	doc = frappe.new_doc('Client Side Scripting')
	doc.enable = 1
	doc.first_name = 'Kavya'
	doc.middle_name = 'M'
	doc.last_name = 'Raval'
	doc.email = 'kavya@example.com'
	doc.mobile = 9897676514
	doc.age = 26
	doc.dob = '12-11-98'
	doc.insert()

	return "Data Added Successfully"