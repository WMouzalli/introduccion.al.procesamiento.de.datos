# Generated by Django 4.1.7 on 2023-03-06 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revistadigital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='revistadigital.category'),
        ),
    ]