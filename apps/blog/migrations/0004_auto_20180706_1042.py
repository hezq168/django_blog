# Generated by Django 2.0.3 on 2018-07-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180706_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='cover/default.jpg', upload_to='cover/%Y/%m/%d', verbose_name='封面'),
        ),
    ]
