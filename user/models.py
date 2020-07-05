from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm, Select, TextInput, forms
from django.dispatch import receiver
from django.db.models.signals import post_save

TYPE = (
    ('shop', 'shop'),
    ('book', 'book'),
    ('film', 'film'),
    ('note', 'note'),
)
STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
)
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=10, choices=TYPE)
    note = models.CharField(max_length=50)
    status = models.CharField(max_length=10,choices=STATUS)
    clicked = models.BooleanField('completed', default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    complated_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.type

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['type','note','clicked']
        widgets = {
            'type': Select(attrs={'class':'input','placeholder':'Choise One...'},choices=TYPE),
            'note': TextInput(attrs={'class':'input','placeholder':'Write Todo...'}),
            'clicked': Select(attrs={'class':'checkbox'}),
        }


