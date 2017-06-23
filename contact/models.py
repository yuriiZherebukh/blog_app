from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    @staticmethod
    def get_by_id(id):
        try:
            return Contact.objects.get(id=id)
        except Exception as error:
            return None

    @staticmethod
    def get_all():
        return Contact.objects.all()

    def to_dict(self):
        return {
                'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'phone': self.phone,
                'email': self.email
                }

    def update(self,first_name=None, last_name=None, phone=None, email=None):
        if first_name:
           self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone:
            self.phone = phone
        if email:
            self.email = email

        self.save()