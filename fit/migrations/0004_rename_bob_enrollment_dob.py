# Generated by Django 4.2 on 2024-04-24 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0003_enrollment_duedate_enrollment_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='BOB',
            new_name='DOB',
        ),
    ]
