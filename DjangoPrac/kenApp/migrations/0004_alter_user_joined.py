# Generated by Django 4.2.16 on 2024-09-24 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kenApp', '0003_user_joined_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined',
            field=models.DateField(null=True),
        ),
    ]