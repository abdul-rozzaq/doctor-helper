# Generated by Django 5.1.3 on 2024-12-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Abdurazzoq', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Abdusalomov', max_length=150),
            preserve_default=False,
        ),
    ]
