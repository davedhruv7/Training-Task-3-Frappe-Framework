# Copyright (c) 2025, Dhruv and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _  



class Server(Document):
	# def validate(self):
	# 	frappe.msgprint("Hello Frappe")

	############################################################################################################################
	# def validate(self):
	# 	self.get_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)

	# 	frappe.msgprint(_("The First name is {} and Age is {}").format(doc.first_name, doc.age))

	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(_("{}. The Family Members area1 is {} located in {}").format(row.idx, row.area_1, row.area_2))
	############################################################################################################################

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Raj'
	# 	doc.last_name = 'Nayi'
	# 	doc.age = 22

	# 	doc.append("family_members", {
	# 		"area_1":"Gandhinagar",
	# 		"area_2":"Sector-22",
	# 		"area_3":"Gujarat"
	# 	}) 

	# 	doc.insert()

	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting', 'CLT006')


	
	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting', 
	# 	filters = {'enable' : 1}, 
	# 	fields = ['first_name', 'age'])

	# 	for d in doc:
	# 		frappe.msgprint(_("The Parent First Name is {} and age is {}").format(d.first_name, d.age))

	# def validate(self):
	# 	self.sql()

	def sql(self):

		data = frappe.db.sql("""
								SELECT 
									first_name,
									age
								FROM
									`tabClient Side Scripting`
								
							""", as_dict=1)
		for d in data:
			frappe.msgprint(_("The Parent First Name is {} and age is {}").format(d.first_name, d.age))