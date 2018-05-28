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
            email_body = """
            {0} 提交了一个新的工单申请， 工单编号 ：{1}， 申请时间：{2}， 安排时间：{3}， 请审批！
            -----------------------------------------------------
            联系人：{4}
            电话 ： {5}
            单位 ： {6}
            地址 ： {7}
            内容 ： {8}
            -----------------------------------------------------
            本邮件为系统通知请务回复，工单详细内容请查询工单系统(QQ手机邮箱客户端收取本内容显示格式会乱掉)
            """.format(work_order.proposer.name, work_order.number, work_order.add_time.strftime("%Y-%m-%d %H:%I:%S"), work_order.do_time,
                       work_order.customer.name, work_order.customer.phone, work_order.customer.unit,
                       work_order.customer.address, work_order.content)
            email = [work_order.approver.email, work_order.proposer.email]

        elif work_order.status == "3":
            record = work_order.workorderrecord_set.get(record_type="1").content
            email_title = "工单派发通知：{0}".format(work_order.title)
            email_body = """
            编号为：{0} 的工单已经派发，申请人：{1}， 申请时间{2}，安排时间{3}，接单人：{4}
            -----------------------------------------------------
            联系人：{5}
            电话 ： {6}
            单位 ： {7}
            地址 ： {8}
            内容 ： {9}
            派发记录：{10}
            -----------------------------------------------------
            本邮件为系统通知请务回复，工单详细内容请查询工单系统(QQ手机邮箱客户端收取本内容显示格式会乱掉)
            """.format(work_order.number, work_order.proposer, work_order.add_time, work_order.do_time, work_order.receiver,
                       work_order.customer.name, work_order.customer.phone, work_order.customer.unit, work_order.customer.address,
                       work_order.content, record)
            email = [work_order.approver.email, work_order.proposer.email, work_order.receiver.email]

        elif work_order.status == "4":
            record = work_order.workorderrecord_set.get(record_type="2").content
            email_title = "工单执行通知：{0}".format(work_order.title)
            email_body = """
            编号为：{0} 的工单已经执行，执行人：{1}
            执行记录：{2}
            """.format(work_order.number, work_order.receiver.name, record)
            email = [work_order.approver.email, work_order.proposer.email, work_order.receiver.email]

        elif work_order.status == "5":
            record = work_order.workorderrecord_set.get(record_type="3").content
            email_title = "工单确认通知：{0}".format(work_order.title)
            email_body = """
            编号为：{0} 的工单已经确认完成，确认人：{1}
            确认记录：{2}
            """.format(work_order.number, work_order.proposer.name, record)
            email = [work_order.approver.email, work_order.proposer.email, work_order.receiver.email]

        send_status = send_mail(email_title, email_body, EMAIL_FROM, email)
        if send_status:
            pass

