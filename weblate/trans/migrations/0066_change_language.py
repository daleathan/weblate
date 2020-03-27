# Generated by Django 3.0.4 on 2020-03-16 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lang", "0006_auto_20200309_1436"),
        ("trans", "0065_string_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="change",
            name="language",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="lang.Language",
            ),
        ),
    ]