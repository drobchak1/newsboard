# Generated by Django 3.2.5 on 2021-07-16 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="amount_of_upvotes",
            field=models.IntegerField(default=2),
        ),
    ]
