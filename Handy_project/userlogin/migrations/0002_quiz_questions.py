# Generated by Django 2.0.6 on 2018-12-15 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('questions', models.CharField(max_length=100)),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('answers', models.CharField(max_length=50)),
            ],
        ),
    ]
