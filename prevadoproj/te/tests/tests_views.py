from django.test import TestCase,Client
from django.urls import reverse
import pymongo

mongoclient = pymongo.MongoClient("mongodb://mongodb:27017")



class TestViews(TestCase):

    def setUp(self):
        self.testinput = {"type": "customer", "entity": "entity", "customerId": 999, "law": "base", "fields": [{"field": "name", "label": "Name", "data_type": "short-text", "default": "Type name here..", "field_type": "basic_details", "field_type_label": "Basic Details", "is_removable": False, "mandatory": True}, {"field": "description", "label": "Description", "data_type": "long-text", "default": "Type description here..", "field_type": "basic_details", "field_type_label": "Basic Details", "is_removable": False, "mandatory": False}, {"field": "entity_type", "label": "Entity Type", "data_type": "options", "default": "", "field_type": "basic_details", "field_type_label": "Basic Details", "is_removable": False, "mandatory": False, "options_list": ["Affiliate", "Client", "Holding Company", "Regulatory Body", "Subsidiary"]}, {"field": "location", "label": "Location", "data_type": "options", "default": "", "field_type": "basic_details", "field_type_label": "Basic Details", "is_removable": False, "mandatory": False, "options_url": {"url": "dm/geos", "request_type": "GET"}}, {"field": "address", "label": "Address", "data_type": "long-text", "default": "Type address here..", "field_type": "contact_details", "field_type_label": "Contact Details", "is_removable": False, "mandatory": False}, {"field": "representative", "label": "Representative", "data_type": "options", "default": "Type the representative name here..", "field_type": "contact_details", "field_type_label": "Contact Details", "is_removable": False, "mandatory": False, "options_url": {"url": "dm/customer/999/users", "request_type": "GET"}}, {"field": "representative_contact_details", "label": "Representative Contact Details", "data_type": "long-text", "default": "Type contact details here..", "field_type": "contact_details", "field_type_label": "Contact Details", "is_removable": False, "mandatory": False}, {"field": "data_protection_officer", "label": "Data Protection Officer", "data_type": "options", "default": "Type the data protection officer name here..", "field_type": "contact_details", "field_type_label": "Contact Details", "is_removable": False, "mandatory": False, "options_url": {"url": "dm/customer/999/users", "request_type": "GET"}}, {"field": "dpo_contact_details", "label": "Data Protection Officer Contact Details", "data_type": "long-text", "default": "Type contact details here..", "field_type": "contact_details", "field_type_label": "Contact Details", "is_removable": False, "mandatory": False}]}

        self.client = Client()
        mongoclient.te.templates.insert(self.testinput)
        self.customer_url = reverse("customer",args=[999])
        self.customer_url_post = reverse("customer",args=[111])
        #mongoclient.te.templates.insert_one(TEST_INPUT)

    def test_customer_GET(self):
        response = self.client.get(self.customer_url)
        self.assertEquals(response.status_code,200)
        print("Successfully tested customer GET request")
    
    def test_customer_POST(self):
        response = self.client.post(self.customer_url_post)
        self.assertEquals(response.status_code,200)
        self.assertIsNotNone(mongoclient.te.templates.find_one({"customerId":111}))
        print("Successfully tested customer POST request")

