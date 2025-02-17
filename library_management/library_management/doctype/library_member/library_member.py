# Copyright (c) 2025, Dhruv and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class LibraryMember(Document):
	
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'

		if not self.route:
			self.route = f"{self.name.lower().replace(' ', '-')}"
