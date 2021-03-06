# Generated by Django 2.2.19 on 2021-02-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateFinder', '0007_auto_20210221_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='job',
            name='skill',
        ),
        migrations.AddField(
            model_name='candidate',
            name='skills',
            field=models.ManyToManyField(to='CandidateFinder.Skill'),
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='CandidateFinder.Skill'),
        ),
    ]
