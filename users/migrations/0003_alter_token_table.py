# Generated by Django 5.0.3 on 2024-03-14 03:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_managers_remove_user_date_joined_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="token",
            table=None,
        ),
    ]
