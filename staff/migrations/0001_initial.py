# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, verbose_name='\u6280\u5e08\u59d3\u540d')),
                ('available_time', models.TimeField(null=True, verbose_name='\u53ef\u4ee5\u9884\u7ea6\u65f6\u95f4')),
                ('statu', models.CharField(max_length=20, null=True, verbose_name='\u6280\u5e08\u72b6\u6001', choices=[('\u6392\u949f', '\u6392\u949f'), ('\u4e0a\u949f', '\u4e0a\u949f'), ('\u4f11\u606f', '\u4f11\u606f')])),
                ('staffstatu', models.CharField(max_length=20, null=True, verbose_name='\u6280\u5e08\u73ed\u51b5', choices=[('\u4e0a\u73ed', '\u4e0a\u73ed'), ('\u4f11\u606f', '\u4f11\u606f')])),
            ],
            options={
                'db_table': 'staff',
                'verbose_name': '\u6280\u5e08\u5728\u5c97',
                'verbose_name_plural': '\u6280\u5e08\u5728\u5c97',
            },
            bases=(models.Model,),
        ),
    ]
