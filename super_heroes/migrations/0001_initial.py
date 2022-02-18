# Generated by Django 4.0.2 on 2022-02-18 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supers_types', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alter_ego', models.CharField(max_length=255)),
                ('primary_ability', models.CharField(max_length=255)),
                ('secondary_ability', models.CharField(max_length=255)),
                ('catch_phrase', models.CharField(max_length=255)),
                ('super_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supers_types.supertype')),
            ],
        ),
    ]