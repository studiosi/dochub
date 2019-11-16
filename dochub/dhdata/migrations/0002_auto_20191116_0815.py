# Generated by Django 2.2.7 on 2019-11-16 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dhdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorreview',
            name='chosen_plan_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctorreview',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhdata.Doctor'),
        ),
        migrations.AlterField(
            model_name='doctorreview',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhdata.Review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='final_chosen_plan',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]