# Generated by Django 4.1.3 on 2024-02-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("publications", "0003_publication_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
    ]