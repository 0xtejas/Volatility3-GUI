# Generated by Django 3.1.6 on 2021-03-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0035_auto_20210314_2224"),
    ]

    operations = [
        migrations.AddField(
            model_name="customrule",
            name="default",
            field=models.BooleanField(default=False),
        ),
    ]
