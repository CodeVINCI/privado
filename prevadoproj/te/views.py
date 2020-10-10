from django.shortcuts import render
import pymongo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
client = pymongo.MongoClient("mongodb://mongodb:27017")


@csrf_exempt
def customer(request,customerid):
    if request.method == 'POST':
        try:
            template1 = client.te.templates.find_one({"name":"template1"})['template']
            template2 = client.te.templates.find_one({"name":"template2"})['template']
            template3 = client.te.templates.find_one({"name":"template3"})['template']
            template1['fields'].extend(template2['fields'])
            template1['fields'].extend(template3['fields'])
            final_template = template1
            final_template['customerId'] = customerid
            final_template['type'] = 'customer'
            final_template['entity'] = 'entity'
            final_template = json.loads(json.dumps(final_template).replace("<customer_id>",str(customerid)))
            client.te.templates.insert(final_template)
            return JsonResponse({"status_code":"200","customer":customerid,"msg":"Customer template successfully saved."})
        except Exception as e:
            print(e)
            return JsonResponse({"status_code":"500","msg":"Bad request"})
    elif request.method == 'GET':
        try:
            template = client.te.templates.find_one({"customerId":customerid},{"_id":0})
            if template is not None:
                return JsonResponse({"template":template})
            else:
                return JsonResponse({"status_code":"404","msg":"no records found for the customer"})
        except Exception as e:
            print(e)
            return JsonResponse({"status_code":"500","msg":"Error occured"})   
   
