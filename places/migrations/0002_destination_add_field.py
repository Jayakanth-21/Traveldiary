# Generated by Django 4.0 on 2021-12-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='add_field',
            field=models.CharField(default='and', max_length=10),
        ),
    ]
