# Generated by Django 4.1.3 on 2024-02-19 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("publications", "0002_rename_description_publication_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="publication",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]