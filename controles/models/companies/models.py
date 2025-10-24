## controles\models\companies\models.py
#from django.db import models
#from django.contrib.auth import get_user_model
#
#User = get_user_model()
#
#class Company(models.Model):
#    name = models.CharField(max_length=255, unique=True)
#    cnpj = models.CharField(max_length=20, blank=True, null=True)
#    created_at = models.DateTimeField(auto_now_add=True)
#    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="companies_created")
#
#    def __str__(self):
#        return self.name