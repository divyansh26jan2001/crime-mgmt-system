# Generated by Django 4.0.4 on 2022-12-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_mgmt', '0007_rename_poice_id_police_police_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='crime_category',
            fields=[
                ('category_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category_desc', models.TextField()),
            ],
        ),
    ]
