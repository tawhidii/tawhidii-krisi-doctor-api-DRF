# Generated by Django 2.1.7 on 2019-04-08 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestAppImage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test_image',
            old_name='image',
            new_name='files',
        ),
    ]
