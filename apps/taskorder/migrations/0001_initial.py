# Generated by Django 2.1.3 on 2018-11-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskOrderManage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.PositiveIntegerField(blank=True, max_length=30, null=True, verbose_name='单号')),
                ('order_creater', models.CharField(blank=True, max_length=20, null=True, verbose_name='发起者')),
                ('trouble_type', models.CharField(choices=[('IterfaceTrouble', '接口故障'), ('NetworkTrouble', '网络故障'), ('CircuitTrouble', '线路故障'), ('OtherTrouble', '其他')], default=None, max_length=200)),
                ('trouble_level', models.CharField(choices=[('General', '一般'), ('Emergency', '紧急')], default=None, max_length=200, verbose_name='故障级别')),
                ('trouble_status', models.CharField(choices=[('New', '新建'), ('Other', '其他')], default=None, max_length=200, verbose_name='故障状态')),
                ('task_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='任务描述')),
                ('task_influence', models.CharField(blank=True, max_length=200, null=True, verbose_name='任务影响')),
                ('service_object', models.CharField(choices=[('Customer', '客户'), ('VIP', 'VIP客户'), ('Internal', '公司内部'), ('Test', '测试'), ('Other', '其他')], default=None, max_length=200, verbose_name='服务对象')),
                ('attachment', models.CharField(max_length=200, verbose_name='附件')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='完成时间')),
                ('flow', models.CharField(blank=True, max_length=200, null=True, verbose_name='操作')),
            ],
            options={
                'verbose_name': '任务工单管理',
                'verbose_name_plural': '任务工单管理',
            },
        ),
    ]
