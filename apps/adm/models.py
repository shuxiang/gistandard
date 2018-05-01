
from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()


class Supplier(models.Model):
    """
    供应商管理
    """
    company = models.CharField(max_length=30, verbose_name="公司名称")
    address = models.CharField(max_length=100, verbose_name="地址")
    linkname = models.CharField(max_length=20, verbose_name="联系人")
    phone = models.CharField(max_length=20, verbose_name="联系电话")
    status = models.BooleanField(default=True, verbose_name="状态")
    desc = models.TextField(blank=True, null=True, verbose_name="备注")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "供应商管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company


class Customer(models.Model):
    """
    客户信息
    """
    unit = models.CharField(max_length=30, verbose_name="客户单位")
    address = models.CharField(max_length=100, verbose_name="地址")
    name = models.CharField(max_length=20, verbose_name="联系人")
    phone = models.CharField(max_length=20, verbose_name="联系电话")
    belongs_to = models.ForeignKey(User, verbose_name="责任人")
    status = models.BooleanField(default=True, verbose_name="状态")
    desc = models.TextField(blank=True, null=True, verbose_name="备注")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "客户管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.unit


class AssetType(models.Model):
    """
    资产类型
    """
    CODE_TYPE = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
    )
    name = models.CharField(max_length=30, verbose_name="类型名称", help_text="类型名称")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="所属", help_text="所属",)
    level = models.IntegerField(choices=CODE_TYPE, verbose_name="类型级别", help_text="类型级别")
    status = models.BooleanField(default=True, verbose_name="状态", help_text="状态")
    desc = models.TextField(blank=True, null=True, verbose_name="备注")


    class Meta:
        verbose_name = "资产类型"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    """
    设备类型
    """
    name = models.CharField(max_length=30, verbose_name="类型名称", help_text="类型名称")
    desc = models.TextField(blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "设备类型"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Asset(models.Model):
    asset_status = (
        (1, "闲置"),
        (2, "在用"),
        (3, "维修"),
        (4, "报废"),
    )
    assetNum = models.CharField(max_length=128, default="", verbose_name="资产编号")
    assetType = models.ForeignKey(AssetType, verbose_name="资产类型")
    brand = models.CharField(max_length=20, blank=True, null=True, verbose_name="品牌")
    config = models.CharField(max_length=128, default="", verbose_name="配置")
    supplier = models.ForeignKey(Supplier, verbose_name="供应商")
    buyDate = models.DateField(verbose_name="购买日期")
    warrantyDate = models.DateField(verbose_name="到保日期")
    status = models.IntegerField(choices=asset_status, default=1, verbose_name="资产状态")
    owner = models.ForeignKey(User, verbose_name="使用人")
    desc = models.TextField(default="")

    class Meta:
        verbose_name = "资产管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.assetNum


class Equipment(models.Model):
    number = models.CharField(max_length=20, default="", verbose_name="设备编号")
    equipment_type = models.ForeignKey(EquipmentType, verbose_name="设备类型")
    equipment_model = models.CharField(max_length=20, default="", verbose_name="设备型号")
    buy_date = models.DateField(verbose_name="购买日期")
    warranty_date = models.DateField(verbose_name="到保日期")
    config_desc = models.TextField(default="", verbose_name="配置说明")
    customer = models.ForeignKey(Customer, verbose_name="客户信息")
