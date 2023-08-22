# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1.7 on 2023-03-14 11:28

from django.db import migrations
from django.db.models import Q


def remove_blank(apps, schema_editor):
    Memory = apps.get_model("memory", "Memory")
    Memory.objects.using(schema_editor.connection.alias).filter(
        Q(source="") | Q(target="")
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("memory", "0015_remove_blank"),
    ]

    operations = [migrations.RunPython(remove_blank, elidable=True)]
