from django.db import models
from datetime import datetime


# Create your models here.

class TroubleOrder(models.Model):
    """故障单管理"""
    trouble_source_types = (
        ('WeChat', '微信'),
        ('Service', '客服'),
        ('FrontLineEngineer', '一线工程师'),
        ('SecondLineEngineer', '二线工程师'),
        ('CustomerDeclaration', '客户申告'),
        ('Alarm', '告警'),
        ('OtherTrouble', '其他'),
    )
    influence_types = (
        ('None', '不影响'),
        ('Single', '单个客户'),
        ('Part', '局部客户'),
        ('All', '全部客户'),
    )
    trouble_types = (
        ('Hard', '硬件'),
        ('System', '系统'),
        ('Configuration', '配置'),
        ('Line', '线路'),
        ('ISP', '运营商'),
        ('Software', '软件'),
        ('Other', '其他'),
    )
    trouble_levels = (
        ('Level1', '1级'),
        ('Level2', '2级'),
        ('Level3', '3级'),
    )

    trouble_id = models.AutoField(primary_key=True, verbose_name='ID')
    trouble_number = models.PositiveIntegerField(unique=True, verbose_name='故障单号')
    trouble_source = models.CharField(max_length=200, choices=trouble_source_types, default=None, verbose_name='来源')
    trouble_influence_degree = models.CharField(max_length=200, choices=influence_types, default=None,
                                                verbose_name='影响度')
    trouble_finder = models.CharField(max_length=50, blank=True, null=True, verbose_name='故障发现者')
    trouble_handler = models.CharField(max_length=50, blank=True, null=True, verbose_name='故障处理者')
    trouble_find_datetime = models.DateTimeField(blank=True, null=True, verbose_name='故障发现时间')
    trouble_order_ctime = models.DateTimeField(blank=True, null=True, verbose_name='故障单发起时间')
    trouble_req_ftime = models.DateTimeField(blank=True, null=True, verbose_name='故障要求完成时间')
    trouble_type = models.CharField(max_length=200, choices=trouble_types, default=None, verbose_name='故障类型')
    trouble_level = models.CharField(max_length=200, choices=trouble_levels, default=None, verbose_name='故障级别')
    trouble_desc = models.CharField(max_length=200, blank=True, null=True, verbose_name='故障描述')
    troubleshooting_steps = models.CharField(max_length=200, blank=True, null=True, verbose_name='故障解决步骤')
    trouble_reason = models.CharField(max_length=200, blank=True, null=True, verbose_name='故障原因')
    trouble_flow = models.CharField(max_length=200, blank=True, null=True, verbose_name='故障流转')
    trouble_device_ip = models.GenericIPAddressField(max_length=20, blank=True, null=True, verbose_name='故障设备IP')
    trouble_result = models.CharField(max_length=200, blank=True, null=True, verbose_name='结果')

    def __str__(self):
        return self.trouble_desc

    class Meta:
        verbose_name = '故障'
        verbose_name_plural = verbose_name
