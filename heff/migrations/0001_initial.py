# Generated by Django 4.1 on 2024-06-23 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('jersey_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='heff.team')),
            ],
        ),
    ]
