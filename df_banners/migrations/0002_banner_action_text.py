# Generated by Django 4.2.8 on 2023-12-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("df_banners", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="banner",
            name="action_text",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
