# Generated by Django 4.0.5 on 2022-10-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_mobile_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pswd',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='tags',
            field=models.ManyToManyField(default=None, to='home.tag'),
        ),
    ]
