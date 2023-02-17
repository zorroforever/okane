from tortoise import fields
from tortoise.models import Model


class MyAbstractBaseModel(Model):
    id = fields.IntField(pk=True, generated=True)
    d_create = fields.DatetimeField(null=True, auto_now_add=True)
    d_update = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        abstract = True


class OkaneUser(MyAbstractBaseModel):
    c_name = fields.CharField(128)

    class Meta:
        table = "OkaneUser"
        table_description = "用户表"

    def __str__(self):
        return self.name


class OkaneApply(MyAbstractBaseModel):
    c_order_no = fields.CharField(50)
    n_uid = fields.IntField
    c_pdt_name = fields.CharField(128)
    n_pdt_id = fields.IntField

    class Meta:
        table = "OkaneApply"
        table_description = "资产申请表"

    def __str__(self):
        return self.name


class OkaneProduct(MyAbstractBaseModel):
    c_pdt_name = fields.CharField(128)
    c_pdt_desc = fields.CharField(512)

    class Meta:
        table = "OkaneProduct"
        table_description = "资产产品表"

    def __str__(self):
        return self.name
