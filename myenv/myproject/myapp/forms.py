from django import forms
from.models import Register,Login
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
        widgets ={

        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
        widgets = {
            
        }