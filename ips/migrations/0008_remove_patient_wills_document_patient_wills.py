# Generated by Django 4.2.11 on 2024-05-23 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ips', '0007_wills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='wills_document',
        ),
        migrations.AddField(
            model_name='patient',
            name='wills',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ips.wills', verbose_name='Documento de voluntad'),
            preserve_default=False,
        ),
    ]
