# Generated by Django 4.0.4 on 2022-06-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0014_alter_quiz_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='user_level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='', max_length=25),
            
        ),
    ]
