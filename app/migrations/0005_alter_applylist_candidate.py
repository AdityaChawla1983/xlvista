# Generated by Django 4.0.2 on 2022-04-13 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_applylist_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applylist',
            name='Candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usermaster'),
        ),
    ]