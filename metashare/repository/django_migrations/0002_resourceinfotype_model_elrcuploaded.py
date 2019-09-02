# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceinfotype_model',
            name='ELRCUploaded',
            field=models.NullBooleanField(verbose_name='Uploaded to ELRC'),
            preserve_default=True,
        ),
    ]
