# Generated by Django 3.2.8 on 2021-10-30 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fechaIngreso',
            field=models.DateField(),
        ),
    ]