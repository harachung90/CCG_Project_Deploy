# Generated by Django 4.0.4 on 2022-06-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0012_alter_quiz_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='This is a test quiz.', max_length=9999),
        ),
    ]
