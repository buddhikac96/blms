# Generated by Django 4.1.1 on 2022-10-03 17:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('team', '0002_alter_team_short_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Q', 'Qualifier Round'), ('QF', 'Quarter Final'), ('SF', 'Semi Final'), ('F', 'Final')], max_length=2)),
                ('team_one_score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('team_two_score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('team_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_one', to='team.team')),
                ('team_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_two', to='team.team')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='MatchPlayerConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='league.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='user.player')),
            ],
        ),
    ]
