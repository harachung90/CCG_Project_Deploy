# Generated by Django 4.0.4 on 2022-08-03 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0014_alter_quiz_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]
