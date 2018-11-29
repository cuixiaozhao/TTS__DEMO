from django.db import models
from datetime import datetime


# Create your models here.


class TaskOrderManage(models.Model):
    """任务单管理"""
    trouble_type_choices = (
        ('IterfaceTrouble', '接口故障'),
        ('NetworkTrouble', '网络故障'),
        ('CircuitTrouble', '线路故障'),
        ('OtherTrouble', '其他'),
    )
    trouble_levels = (
        ('General', '一般'),
        ('Emergency', '紧急'),
    )
    trouble_order_status = (
        ('New', '新建'),
        ('Other', '其他'),
    )
    service_obj = (
        ('Customer', '客户'),
        ('VIP', 'VIP客户'),
        ('Internal', '公司内部'),
        ('Test', '测试'),
        ('Other', '其他'),
    )
    id = models.AutoField(primary_key=True, verbose_name='ID')
    order_number = models.PositiveIntegerField( blank=True, null=True, verbose_name='单号')
    order_creater = models.CharField(max_length=20, blank=True, null=True, verbose_name='发起者')
    trouble_type = models.CharField(max_length=200,choices=trouble_type_choices, default=None)
    trouble_level = models.CharField(max_length=200,choices=trouble_levels, default=None, verbose_name='故障级别')
    trouble_status = models.CharField(max_length=200,choices=trouble_order_status, default=None, verbose_name='故障状态')
    task_desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='任务描述')
    task_influence = models.CharField(max_length=200, blank=True, null=True, verbose_name='任务影响')
    service_object = models.CharField(max_length=200,choices=service_obj, default=None, verbose_name='服务对象')
    attachment = models.CharField(max_length=200, verbose_name='附件')
    start_time = models.DateTimeField(blank=True, null=True, verbose_name='开始时间')
    end_time = models.DateTimeField(blank=True, null=True, verbose_name='完成时间')
    flow = models.CharField(max_length=200, blank=True, null=True, verbose_name='操作')

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = '任务工单管理'
        verbose_name_plural = verbose_name
