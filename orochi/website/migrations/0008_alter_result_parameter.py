# Generated by Django 3.2 on 2020-08-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_result_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='parameter',
            field=models.JSONField(blank=True, null=True),
        ),
    ]