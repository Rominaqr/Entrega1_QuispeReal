# Generated by Django 4.0.4 on 2022-05-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
