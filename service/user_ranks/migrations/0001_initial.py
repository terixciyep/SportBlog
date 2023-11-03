# Generated by Django 4.2.6 on 2023-11-03 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sport_categories', '0002_alter_exercise_sport_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verify', models.BooleanField(default=False)),
                ('verification_file', models.FileField(upload_to='media/user_ranks_verify_media/')),
                ('ranks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_categories.rankforexercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
