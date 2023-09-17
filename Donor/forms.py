from django import forms
from .models import UserProfile, UserModel

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fullname', 'age', 'gender', 'height', 'weight', 'blood_group', 'organ', 'status', 'health_history', 'email', 'pincode', 'image']

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['Username', 'Password']
