# Generated by Django 2.0.6 on 2018-12-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0005_user_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
