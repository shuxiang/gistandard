import json

from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

from django.views.generic.base import View
from django.http import HttpResponse

from utils.mixin_utils import LoginRequiredMixin
from .models import Menu
from system.models import SystemSetup


class MenuView(LoginRequiredMixin, View):
    """
    菜单管理
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'system/rbac/menu-list.html', ret)


class MenuListView(LoginRequiredMixin, View):
    """
    获取菜单列表
    """

    def get(self, request):
        fields = ['id', 'title', 'code', 'url', 'parent__title']
        ret = dict(data=list(Menu.objects.values(*fields).order_by('id')))
        return HttpResponse(json.dumps(ret), content_type='application/json')
