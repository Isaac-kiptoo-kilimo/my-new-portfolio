# Generated by Django 4.0.4 on 2022-05-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0005_alter_project_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editor',
            name='pro_image',
            field=models.ImageField(default='index/Isaac.jpg', null=True, upload_to='index/'),
        ),
    ]