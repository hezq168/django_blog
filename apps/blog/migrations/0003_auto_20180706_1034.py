# Generated by Django 2.0.3 on 2018-07-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180706_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='显示'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='显示'),
        ),
    ]