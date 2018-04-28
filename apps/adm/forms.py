# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/20

from django import forms
from .models import Supplier, AssetType


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class AssetTypeForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = '__all__'

