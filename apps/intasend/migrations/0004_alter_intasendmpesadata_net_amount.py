# Generated by Django 4.2 on 2024-09-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intasend", "0003_intasendmpesadata_amount_transacted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="intasendmpesadata",
            name="net_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
