# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20151203_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookorder',
            name='isused',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
