# Generated by Django 3.0.5 on 2022-04-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(
                choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')],
                default='Beginner', max_length=25),
        ),
    ]
