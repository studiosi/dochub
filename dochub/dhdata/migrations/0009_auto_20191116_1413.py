# Generated by Django 2.2.7 on 2019-11-16 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhdata', '0008_auto_20191116_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='plan_id',
            field=models.CharField(max_length=200),
        ),
    ]
