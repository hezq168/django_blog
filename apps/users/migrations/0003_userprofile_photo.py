# Generated by Django 2.0.3 on 2018-08-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180816_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='photo/default.jpg', upload_to='photo/%Y/%m/%d', verbose_name='头像'),
        ),
    ]