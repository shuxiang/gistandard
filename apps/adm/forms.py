# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/20

from django import forms
from .models import Supplier, AssetType, Customer, EquipmentType, Equipment, ServiceInfo


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class AssetTypeForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['unit', 'address', 'name', 'phone', 'status', 'belongs_to']


class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentCreateForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'
        error_messages = {
            "number": {"required": "设备编号不能为空"},
            "equipment_model": {"required": "请输入设备型号"},
            "buy_date": {"required": "请输入购买日期"},
            "warranty_date": {"required": "请输入质保日期"},
            "supplier": {"required": "请选择分销商"}
        }

    def clean(self):
        cleaned_data = super(EquipmentCreateForm, self).clean()
        number = cleaned_data.get("number")
        if Equipment.objects.filter(number=number).count():
            raise forms.ValidationError('设备编号：{}已存在'.format(number))


class EquipmentUpdateForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'
        error_messages = {
            "number": {"required": "设备编号不能为空"},
            "equipment_model": {"required": "请输入设备型号"},
            "buy_date": {"required": "请输入购买日期"},
            "warranty_date": {"required": "请输入质保日期"},
            "supplier": {"required": "请选择分销商"}
        }