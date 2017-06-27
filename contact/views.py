from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
import json


from .models import Contact


class ContactView(View):
    """Contact view handle GET, POST, PUT, DELETE requests."""

    def get(self, request, contact_id=None):

        if not contact_id:
            contacts = Contact.get_all()
            print(contacts)
            contacts = [contact.to_dict() for contact in contacts]
            print(contacts)
            return render(request, 'contact/list.html', {'contacts': contacts})
        else:
            print(contact_id)
            contact = Contact.get_by_id(contact_id)
            print(contact)
            contact = contact.to_dict()
            return JsonResponse(contact, status=200)

    def put(self, request, contact_id):
        contact = Contact.get_by_id(contact_id)
        if not contact:
            return HttpResponse(status=404)
        update_data = json.loads(request.body)
        contact.update(**update_data)
        return JsonResponse(contact.to_dict(), status=200)

    def post(self,request):
        contact_data = json.loads(request.body.decode('utf-8'))
        print(request.body)
        contact = Contact()
        contact.create(**contact_data)
        return JsonResponse(contact.to_dict(), status=200)

    def delete(self,request,contact_id):
       print(contact_id)
       contact = Contact.get_by_id(contact_id)
       if not contact:
            return HttpResponse(status=404)
       contact.delete()
       return self.get(request)
