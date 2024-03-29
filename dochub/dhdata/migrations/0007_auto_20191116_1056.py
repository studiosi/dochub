# Generated by Django 2.2.7 on 2019-11-16 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dhdata', '0006_merge_20191116_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='helper_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helper_doctor_profile', to='dhdata.Doctor'),
        ),
        migrations.AlterField(
            model_name='task',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to='dhdata.Doctor'),
        ),
    ]
