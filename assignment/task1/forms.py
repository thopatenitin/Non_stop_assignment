from django.forms import ModelForm
from .models import post

class post_form(ModelForm):
    class Meta:
        model = post
        exclude=["id","published_date","published","author"]

class post_update_form(ModelForm):
    class Meta:
        model = post
        exclude=["id","published_date","author"]
        
        # fields='__all__'