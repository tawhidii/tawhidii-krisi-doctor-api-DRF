# Generated by Django 2.1.7 on 2019-03-26 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('krisi_image_problem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_image',
            name='krisi_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='krisi_user.krisi_user'),
        ),
    ]
