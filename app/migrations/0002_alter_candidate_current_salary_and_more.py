# Generated by Django 4.0.2 on 2022-03-28 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='current_salary',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='expected_salary',
            field=models.BigIntegerField(default=1),
        ),
    ]
