# Generated by Django 2.1.3 on 2018-11-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TroubleOrder',
            fields=[
                ('trouble_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('trouble_number', models.PositiveIntegerField(max_length=30, unique=True, verbose_name='故障单号')),
                ('trouble_source', models.CharField(choices=[('WeChat', '微信'), ('Service', '客服'), ('FrontLineEngineer', '一线工程师'), ('SecondLineEngineer', '二线工程师'), ('CustomerDeclaration', '客户申告'), ('Alarm', '告警'), ('OtherTrouble', '其他')], default=None, max_length=200, verbose_name='来源')),
                ('trouble_influence_degree', models.CharField(choices=[('None', '不影响'), ('Single', '单个客户'), ('Part', '局部客户'), ('All', '全部客户')], default=None, max_length=200, verbose_name='影响度')),
                ('trouble_finder', models.CharField(blank=True, max_length=50, null=True, verbose_name='故障发现者')),
                ('trouble_handler', models.CharField(blank=True, max_length=50, null=True, verbose_name='故障处理者')),
                ('trouble_find_datetime', models.DateTimeField(blank=True, null=True, verbose_name='故障发现时间')),
                ('trouble_order_ctime', models.DateTimeField(blank=True, null=True, verbose_name='故障单发起时间')),
                ('trouble_req_ftime', models.DateTimeField(blank=True, null=True, verbose_name='故障要求完成时间')),
                ('trouble_type', models.CharField(choices=[('Hard', '硬件'), ('System', '系统'), ('Configuration', '配置'), ('Line', '线路'), ('ISP', '运营商'), ('Software', '软件'), ('Other', '其他')], default=None, max_length=200, verbose_name='故障类型')),
                ('trouble_level', models.CharField(choices=[('Level1', '1级'), ('Level2', '2级'), ('Level3', '3级')], default=None, max_length=200, verbose_name='故障级别')),
                ('trouble_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='故障描述')),
                ('troubleshooting_steps', models.CharField(blank=True, max_length=200, null=True, verbose_name='故障解决步骤')),
                ('trouble_reason', models.CharField(blank=True, max_length=200, null=True, verbose_name='故障原因')),
                ('trouble_flow', models.CharField(blank=True, max_length=200, null=True, verbose_name='故障流转')),
                ('trouble_device_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='故障设备IP')),
                ('trouble_result', models.CharField(blank=True, max_length=200, null=True, verbose_name='结果')),
            ],
            options={
                'verbose_name': '故障',
                'verbose_name_plural': '故障',
            },
        ),
    ]
