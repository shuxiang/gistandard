import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup
from .models import Supplier, AssetType
from .forms import SupplierForm, AssetTypeForm

class SupplierView(LoginRequiredMixin, View):
    """
    供应商管理
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/supplier.html', ret)


class SupplierListView(LoginRequiredMixin, View):
    """
    获取供应商列表
    """
    def get(self, request):
        ret = dict(data=list(Supplier.objects.values()))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class SupplierDetailView(LoginRequiredMixin, View):
    """
    供应商详情页：查看、修改、新建数据
    """
    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            supplier = get_object_or_404(Supplier, pk=request.GET.get('id'))
            ret['supplier'] = supplier
        return render(request, 'adm/bsm/supplier_detail.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            supplier = get_object_or_404(Supplier, pk=request.POST.get('id'))
        else:
            supplier = Supplier()
        supplier_form = SupplierForm(request.POST, instance=supplier)
        if supplier_form.is_valid():
            supplier_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class SupplierDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            Supplier.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class AssetTypeView(LoginRequiredMixin, View):
    """
    资产类型
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/assettype.html', ret)


class AssetTypeListView(LoginRequiredMixin, View):
    """
    资产类型列表
    """
    def get(self, request):
        fields = ['id', 'name', 'parent__name', 'level', 'status', 'desc']
        ret = dict(data=list(AssetType.objects.values(*fields)))
        return HttpResponse(json.dumps(ret), content_type='application/json')


class AssetTypeDetailView(LoginRequiredMixin, View):
    """
    资产类型：查看、修改、新建数据
    """
    def get(self, request):
        ret = dict(assettypes=AssetType.objects.filter(level=1))
        if 'id' in request.GET and request.GET['id']:
            assettype = get_object_or_404(AssetType, pk=request.GET.get('id'))
            ret['assettype'] = assettype
        return render(request, 'adm/bsm/assettype_detail.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            assettype = get_object_or_404(AssetType, pk=request.POST.get('id'))
        else:
            assettype = AssetType()
        assettype_form = AssetTypeForm(request.POST, instance=assettype)
        if assettype_form.is_valid():
            assettype_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class AssetTypeDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            AssetType.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')