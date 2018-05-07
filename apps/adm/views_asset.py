import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup
from .models import Equipment, EquipmentType, Customer


User = get_user_model()


class AssetView(LoginRequiredMixin, View):
    """
    资产管理
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'page404.html', ret)


# class EquipmentListView(LoginRequiredMixin, View):
#     """
#     设备管理：设备列表
#     """
#     def get(self, request):
#         fields = ['id', 'number', 'equipment_type__name', 'equipment_model', 'buy_date', 'warranty_date', 'customer__unit']
#         filters = dict()
#         ret = dict(data=list(Equipment.objects.values(*fields)))
#         return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')
#
#
# class EquipmentCreateView(LoginRequiredMixin, View):
#     """
#     设备管理：新建和修改资产数据
#     """
#     def get(self, request):
#         ret = dict()
#         if 'id' in request.GET and request.GET['id']:
#             equipment = get_object_or_404(Equipment, pk=request.GET.get('id'))
#             ret['equipment'] = equipment
#         equipment_type = EquipmentType.objects.values()
#         customer = Customer.objects.values()
#         ret['equipment_type'] = equipment_type
#         ret['customer'] = customer
#         return render(request, 'adm/equipment/equipment_create.html', ret)
#
#     def post(self, request):
#         res = dict(result=False)
#         if 'id' in request.POST and request.POST['id']:
#             equipment = get_object_or_404(Equipment, pk=request.POST.get('id'))
#         else:
#             equipment = Equipment()
#         equipment_form = EquipmentForm(request.POST, instance=equipment)
#         if equipment_form.is_valid():
#             equipment_form.save()
#             res['result'] = True
#         return HttpResponse(json.dumps(res), content_type='application/json')
#
#
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