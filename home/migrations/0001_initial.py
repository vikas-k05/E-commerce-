# Generated by Django 4.0.5 on 2022-10-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=20)),
                ('ram', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
