# Generated by Django 4.1.1 on 2022-10-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='type',
            field=models.CharField(choices=[('QR', 'Qualifier Round'), ('QF', 'Quarter Final'), ('SF', 'Semi Final'), ('F', 'Final')], max_length=2),
        ),
    ]