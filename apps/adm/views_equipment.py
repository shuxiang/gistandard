import json
from datetime import datetime, timedelta

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
from .forms import EquipmentForm

User = get_user_model()


class EquipmentView(LoginRequiredMixin, View):
    """
    设备管理
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        equipment_types = EquipmentType.objects.all()
        customers = Customer.objects.all()
        ret['equipment_types'] = equipment_types
        ret['customers'] = customers
        return render(request, 'adm/equipment/equipment.html', ret)


class EquipmentListView(LoginRequiredMixin, View):
    """
    设备管理：设备列表
    """

    def get(self, request):
        fields = ['id', 'number', 'equipment_type__name', 'equipment_model', 'buy_date', 'warranty_date',
                  'customer__unit', 'customer__belongs_to__name']
        filters = dict()
        if 'select' in request.GET and request.GET['select']:
            select = int(request.GET['select'])
            if select == 0:
                date_time = datetime.today()
                filters['warranty_date__lte'] = date_time
            if select == 3:
                now = datetime.today()
                date_time = now + timedelta(days=90)
                filters['warranty_date__range'] = (now, date_time)
        if 'number' in request.GET and request.GET['number']:
            filters['number__icontains'] = request.GET['number']
        if 'equipment_type' in request.GET and request.GET['equipment_type']:
            filters['equipment_type'] = request.GET['equipment_type']
        if 'equipment_model' in request.GET and request.GET['equipment_model']:
            filters['equipment_model__icontains'] = request.GET['equipment_model']
        if 'customer' in request.GET and request.GET['customer']:
            filters['customer'] = request.GET['customer']
        ret = dict(data=list(Equipment.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class EquipmentCreateView(LoginRequiredMixin, View):
    """
    设备管理：新建和修改资产数据
    """

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            equipment = get_object_or_404(Equipment, pk=request.GET.get('id'))
            ret['equipment'] = equipment
        equipment_type = EquipmentType.objects.values()
        customer = Customer.objects.values()
        ret['equipment_type'] = equipment_type
        ret['customer'] = customer
        return render(request, 'adm/equipment/equipment_create.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            equipment = get_object_or_404(Equipment, pk=request.POST.get('id'))
        else:
            equipment = Equipment()
        equipment_form = EquipmentForm(request.POST, instance=equipment)
        if equipment_form.is_valid():
            equipment_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class EquipmentDetailView(LoginRequiredMixin, View):
    """
    设备管理：详情页面
    """

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            equipment = get_object_or_404(Equipment, pk=request.GET.get('id'))
            ret['equipment'] = equipment
        return render(request, 'adm/equipment/equipment_detail.html', ret)


class EquipmentDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            Equipment.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')
