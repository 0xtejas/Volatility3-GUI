# Generated by Django 4.2.5 on 2023-09-20 08:35

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0041_alter_dump_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dump",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FF0000", image_field=None, max_length=25, samples=None
            ),
        ),
    ]