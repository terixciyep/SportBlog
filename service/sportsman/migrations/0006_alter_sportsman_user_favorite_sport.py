# Generated by Django 4.2.6 on 2023-10-26 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsman', '0005_alter_sportsman_user_managers_sportsman_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsman_user',
            name='favorite_sport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sportsman.sport'),
        ),
    ]