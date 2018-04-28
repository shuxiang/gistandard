# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/10/17

import xadmin
from xadmin import views

from .models import Supplier, AssetType




class SupplierAdmin(object):
    list_display = ['id', 'company', 'address', 'linkname', 'phone', 'status', 'add_time']
    list_filter = ['id', 'company', 'address', 'linkname', 'phone', 'status']
    list_editable = ['status']


class AssetTypeAdmin(object):
    list_display = ['id', 'name', 'parent', 'level', 'status', 'desc']
    list_filter = ['id', 'name', 'parent', 'level', 'status', 'desc']
    list_editable = ['status']

xadmin.site.register(Supplier, SupplierAdmin)
xadmin.site.register(AssetType, AssetTypeAdmin)
