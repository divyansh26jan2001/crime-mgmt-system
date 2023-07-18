# Generated by Django 4.2 on 2023-05-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_mgmt', '0017_alter_fir_police_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir',
            name='FIR_no',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='accused_name',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='address',
            field=models.TextField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='applicant_name',
            field=models.CharField(default=0, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='number',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='parentage',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='purpose',
            field=models.TextField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='relation_with_accussed',
            field=models.CharField(default=0, max_length=100, null=True),
        ),
    ]
