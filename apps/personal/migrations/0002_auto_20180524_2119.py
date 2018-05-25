# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-24 21:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approver', to=settings.AUTH_USER_MODEL, verbose_name='审批人'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='file_content',
            field=models.FileField(blank=True, null=True, upload_to='file_folder/%Y/%m', verbose_name='项目资料'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='proposer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposer', to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='接单人'),
        ),
    ]
