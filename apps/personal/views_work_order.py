import json
import re

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from .models import WorkOrder
from .forms import WorkOrderCreateForm, WorkOrderUpdateForm
from adm.models import Customer
from rbac.models import Role

from utils.toolkit import ToolKit, SendMessage
User = get_user_model()


class WorkOrderICreatedView(LoginRequiredMixin, View):
    """
    工单创建人视图
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        return render(request, 'personal/workorder/workorder.html', ret)


class WorkOrderListView(LoginRequiredMixin, View):
    def get(self, request):
        fields = ['id', 'number', 'title', 'type', 'status', 'do_time', 'customer__unit', 'proposer__name']
        filters = dict()
        # filters['proposer_id'] = request.user.id
        if 'number' in request.GET and request.GET['number']:
            filters['number__icontains'] = request.GET['number']

        ret = dict(data=list(WorkOrder.objects.filter(**filters).values(*fields)))

        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class WorkOrderCreateView(LoginRequiredMixin, View):

    def get(self, request):
        type_list = []
        filters = dict()
        for work_order_type in WorkOrder.type_choices:
            type_dict = dict(item=work_order_type[0], value=work_order_type[1])
            type_list.append(type_dict)
        if request.user.department_id == 9:  # 新建工单时销售部门只能选择自己的用户信息
            filters['belongs_to_id'] = request.user.id
        customer = Customer.objects.values().filter(**filters)
        role = get_object_or_404(Role, title='审批')
        approver = role.userprofile_set.all()
        try:
            number = WorkOrder.objects.latest('number').number
        except WorkOrder.DoesNotExist:
            number = ""
        new_number = ToolKit.bulidNumber('SX', 9, number)
        ret = {
            'type_list': type_list,
            'customer': customer,
            'approver': approver,
            'new_number': new_number
        }
        return render(request, 'personal/workorder/workorder_create.html', ret)

    def post(self, request):
        res = dict()
        work_order = WorkOrder()
        work_order_form = WorkOrderCreateForm(request.POST, instance=work_order)
        if work_order_form.is_valid():
            work_order_form.save()
            res['status'] = 'success'
            number = request.POST.get('number')
            if work_order.status == "2":
                SendMessage.send_workorder_email(number)
                res['status'] = 'submit'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(work_order_form.errors)
            work_order_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'work_order_form_errors': work_order_form_errors[0]
            }
        return HttpResponse(json.dumps(res), content_type='application/json')


class WorkOrderDetailView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
            ret['work_order'] = work_order
        return render(request, 'personal/workorder/workorder_detail.html', ret)


class WorkOrderDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            status = get_object_or_404(WorkOrder, pk=request.POST['id']).status
            if int(status) <= 1:
                id_list = map(int, request.POST.get('id').split(','))
                WorkOrder.objects.filter(id__in=id_list).delete()
                ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class WorkOrderUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        type_list = []
        filters = dict()
        if 'id' in request.GET and request.GET['id']:
            work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        for work_order_type in WorkOrder.type_choices:
            type_dict = dict(item=work_order_type[0], value=work_order_type[1])
            type_list.append(type_dict)
        if request.user.department_id == 9:
            filters['belongs_to_id'] = request.user.id
        customer = Customer.objects.values().filter(**filters)
        role = get_object_or_404(Role, title='审批')
        approver = role.userprofile_set.all()
        ret = {
            'work_order': work_order,
            'type_list': type_list,
            'customer': customer,
            'approver': approver,
        }
        return render(request, 'personal/workorder/workorder_update.html', ret)

    def post(self, request):
        res = dict()
        work_order = get_object_or_404(WorkOrder, pk=request.POST['id'])
        work_order_form = WorkOrderUpdateForm(request.POST, instance=work_order)
        if int(work_order.status) <= 1:
            if work_order_form.is_valid():
                work_order_form.save()
                res['status'] = 'success'
                number = request.POST.get('number')
                if work_order.status == "2":
                    SendMessage.send_workorder_email(number)
                    res['status'] = 'submit'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(work_order_form.errors)
                work_order_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'work_order_form_errors': work_order_form_errors[0]
                }
        else:
            res['status'] = 'ban'
        return HttpResponse(json.dumps(res), content_type='application/json')

