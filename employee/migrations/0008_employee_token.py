# Generated by Django 2.0 on 2020-03-06 15:12

from django.db import migrations, models
import employee.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_response_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='token',
            field=models.CharField(default=employee.models.Employee.my_secret, editable=False, max_length=8),
        ),
    ]