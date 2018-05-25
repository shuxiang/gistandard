# @Time   : 2018/5/24 22:48
# @Author : RobbieHan
# @File   : toolkit.py

from django.core.mail import send_mail

from personal.models import WorkOrder
from gistandard.settings import EMAIL_FROM


class ToolKit(object):

    '''
    随机生成工单号
    '''
    @classmethod
    def bulidNumber(self, nstr, nlen, srcnum="0"):
        numlen = nlen - len(nstr)
        snum = "1"
        if len(srcnum) == nlen:
            snum = srcnum[len(nstr):len(srcnum)]
            nnum = int(snum)
            snum = str(nnum + 1)
        return nstr + snum.zfill(numlen)
"""
    type_choices = (('0', '初次安装'), ('1', '售后现场'), ('2', '远程支持'), ('3', '售前支持'))
    status_choices = (('0', '新建-保存'), ('1', '提交-等待审批'), ('2', '退回'), ('3', '已审批-等待执行'), ('4', '已执行-等待确认'), ('5', '完成'))
"""

class SendMessage(object):

    @classmethod
    def send_workorder_email(self, number):
        work_order = WorkOrder.objects.get(number=number)
        if work_order.status == "2":
            email_title = u"工单申请通知：{0}".format(work_order.title)
            email_body = u""" {0} 提交了一个新的工单申请， 工单编号 ：{1}， 申请时间：{2}， 安排时间：{3}， 请审批！
            -----------------------------------------------------
            联系人：{4}
            电话 ： {5}
            单位 ： {6}
            地址 ： {7}
            内容 ： {8}
            -----------------------------------------------------
            """.format(work_order.proposer.name, work_order.number, work_order.add_time.strftime("%Y-%m-%d %H:%I:%S"), work_order.do_time,
                       work_order.customer.name, work_order.customer.phone, work_order.customer.unit,
                       work_order.customer.address, work_order.content)
            email = [work_order.approver.email]

        send_status = send_mail(email_title, email_body, EMAIL_FROM, email)
        if send_status:
            pass
