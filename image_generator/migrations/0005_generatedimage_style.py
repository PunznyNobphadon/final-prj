# Generated by Django 4.2.7 on 2024-05-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("image_generator", "0004_generatedimage_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="generatedimage",
            name="style",
            field=models.CharField(default="Digital Art", max_length=255),
        ),
    ]
