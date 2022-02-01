# Generated by Django 4.0 on 2022-02-01 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('places', '0002_destination_add_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='traveller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
