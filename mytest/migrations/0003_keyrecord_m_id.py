# Generated by Django 3.0.7 on 2020-06-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0002_auto_20200627_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyrecord',
            name='m_id',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
