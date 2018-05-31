import json
import re

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup
from .models import Asset, AssetType, AssetLog
from .forms import AssetCreateForm
from rbac.models import Role


User = get_user_model()


class AssetView(LoginRequiredMixin, View):
    """
    资产管理
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        status_list = []
        for status in Asset.asset_status:
            status_dict = dict(item=status[0], value=status[1])
            status_list.append(status_dict)
        asset_types = AssetType.objects.all()
        ret['status_list'] = status_list
        ret['asset_types'] = asset_types
        return render(request, 'adm/asset/asset.html', ret)


class AssetListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'assetNum', 'assetType__name', 'brand', 'model', 'warehouse', 'status', 'owner__name', 'operator', 'add_time']
        filters = dict()

        # if 'number' in request.GET and request.GET['number']:
        #     filters['number__icontains'] = request.GET['number']
        # if 'equipment_type' in request.GET and request.GET['equipment_type']:
        #     filters['equipment_type'] = request.GET['equipment_type']
        # if 'equipment_model' in request.GET and request.GET['equipment_model']:
        #     filters['equipment_model__icontains'] = request.GET['equipment_model']
        # if 'customer' in request.GET and request.GET['customer']:
        #     filters['customer'] = request.GET['customer']
        ret = dict(data=list(Asset.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class AssetCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        status_list = []
        for status in Asset.asset_status:
            status_dict = dict(item=status[0], value=status[1])
            status_list.append(status_dict)
        asset_type = AssetType.objects.values()
        role = get_object_or_404(Role, title="销售")
        user_info = role.userprofile_set.all()
        ret['asset_type'] = asset_type
        ret['user_info'] = user_info
        ret['status_list'] = status_list
        return render(request, 'adm/asset/asset_create.html', ret)

    def post(self, request):
        res = dict()
        asset_create_form = AssetCreateForm(request.POST)
        if asset_create_form.is_valid():
            asset_create_form.save()
            res['status'] = 'success'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(asset_create_form.errors)
            asset_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'asset_form_errors': asset_form_errors[0]
            }

        return HttpResponse(json.dumps(res), content_type='application/json')


# class EquipmentDetailView(LoginRequiredMixin, View):
#     """
#     设备管理：详情页面
#     """
#     def get(self, request):
#         ret = dict()
#         if 'id' in request.GET and request.GET['id']:
#             equipment = get_object_or_404(Equipment, pk=request.GET.get('id'))
#             ret['equipment'] = equipment
#         return render(request, 'adm/equipment/equipment_detail.html', ret)
#
#
# class EquipmentDeleteView(LoginRequiredMixin, View):
#
#     def post(self, request):
#         ret = dict(result=False)
#         if 'id' in request.POST and request.POST['id']:
#             id_list = map(int, request.POST.get('id').split(','))
#             Equipment.objects.filter(id__in=id_list).delete()
#             ret['result'] = True
#         return HttpResponse(json.dumps(ret), content_type='application/json')