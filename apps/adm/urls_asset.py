# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/8

from django.conf.urls import url

from adm import views_asset

urlpatterns = [

    url(r'^$', views_asset.AssetView.as_view(), name='asset'),
    url(r'^list', views_asset.AssetListView.as_view(), name="list"),
    url(r'^create', views_asset.AssetCreateView.as_view(), name="create"),
    # url(r'^detail', views_equipment.EquipmentDetailView.as_view(), name="equipment-detail"),
    # url(r'^delete', views_equipment.EquipmentDeleteView.as_view(), name='delete'),
]
