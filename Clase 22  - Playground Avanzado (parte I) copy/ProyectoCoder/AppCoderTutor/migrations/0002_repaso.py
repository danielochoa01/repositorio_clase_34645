# Generated by Django 4.1.3 on 2022-11-21 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoderTutor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repaso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.IntegerField()),
                ('tema_a_repasar', models.CharField(max_length=40)),
                ('fecha_repaso', models.DateField(default=datetime.datetime(2022, 11, 21, 23, 21, 40, 429976, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
