# Generated by Django 3.0.8 on 2020-08-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeritem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='availability',
            field=models.CharField(choices=[('Available', 'Available'), ('Given', 'Given')], default='Available', max_length=20),
        ),
    ]
