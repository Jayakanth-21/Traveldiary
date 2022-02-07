# Generated by Django 4.0 on 2022-02-01 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('places', '0003_destination_traveller'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristplaces',
            name='traveller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]