# Generated by Django 4.2.16 on 2024-09-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kenApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('breed', models.CharField(max_length=255)),
            ],
        ),
    ]