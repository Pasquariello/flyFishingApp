# Generated by Django 2.1.1 on 2018-09-27 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flyFishing', '0020_auto_20180927_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='relatedRiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fish', to='flyFishing.River'),
        ),
    ]