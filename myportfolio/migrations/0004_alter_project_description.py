# Generated by Django 4.0.4 on 2022-05-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_editor_pro_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
