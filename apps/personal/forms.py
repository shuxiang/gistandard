# @Time   : 2018/5/6 17:22
# @Author : RobbieHan
# @File   : forms.py


from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'gender', 'birthday']