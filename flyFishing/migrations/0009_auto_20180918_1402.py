# Generated by Django 2.1.1 on 2018-09-18 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flyFishing', '0008_auto_20180918_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='river',
        ),
        migrations.AddField(
            model_name='fish',
            name='relatedLeague',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flyFishing.League'),
        ),
    ]
