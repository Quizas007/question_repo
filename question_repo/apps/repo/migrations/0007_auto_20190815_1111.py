# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-15 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0006_userlog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'permissions': (('can_change_question', '可以修改题目信息'), ('can_add_question', '可以添加题目信息'), ('can_change_question_status', '可以修改题目状态')), 'verbose_name': '题库', 'verbose_name_plural': '题库'},
        ),
    ]
