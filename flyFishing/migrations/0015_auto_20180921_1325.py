# Generated by Django 2.1.1 on 2018-09-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyFishing', '0014_auto_20180921_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='river',
            name='active_fish',
        ),
        migrations.AddField(
            model_name='river',
            name='active_fish',
            field=models.ManyToManyField(to='flyFishing.Fish'),
        ),
    ]
