# Generated by Django 3.1.5 on 2021-03-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='d_name',
            new_name='d_department',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='i_description',
            new_name='u_description',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='u_phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
