# Generated by Django 4.0.4 on 2022-12-05 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime_mgmt', '0006_remove_police_id_alter_police_mobile_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='police',
            old_name='poice_id',
            new_name='police_id',
        ),
    ]