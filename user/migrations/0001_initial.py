# Generated by Django 4.1.1 on 2022-10-03 06:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0002_alter_team_short_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('height', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('game_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
    ]
