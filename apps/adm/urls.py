# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/8

from django.conf.urls import url

from adm import views_bsm

urlpatterns = [

    # 基础管理：供应商管理，品牌管理，资产类型管理
    url(r'^supplier/$', views_bsm.SupplierView.as_view(), name="supplier"),
    url(r'^supplier/list', views_bsm.SupplierListView.as_view(), name="supplier-list"),
    url(r'^supplier/detail', views_bsm.SupplierDetailView.as_view(), name="supplier-detail"),
    url(r'^supplier/delete', views_bsm.SupplierDeleteView.as_view(), name='supplier-delete'),

    url(r'^assettype/$', views_bsm.AssetTypeView.as_view(), name='assettype'),
    url(r'^assettype/list', views_bsm.AssetTypeListView.as_view(), name="assettype-list"),
    url(r'^assettype/detail', views_bsm.AssetTypeDetailView.as_view(), name="assettype-detail"),
    url(r'^assettype/delete', views_bsm.AssetTypeDeleteView.as_view(), name='assettype-delete'),

]
