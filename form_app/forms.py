from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    # Meta takes in the attributes of the model
    class Meta:
        model = Customer
        fields = '__all__'