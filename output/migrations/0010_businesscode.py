# Generated by Django 4.2.6 on 2023-11-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('output', '0009_districtcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('구상권코드', models.CharField(blank=True, max_length=10, null=True)),
                ('상권코드명', models.CharField(blank=True, max_length=100, null=True)),
                ('행정동코드', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
