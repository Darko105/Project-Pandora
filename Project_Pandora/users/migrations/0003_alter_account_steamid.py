# Generated by Django 4.2.7 on 2023-11-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_account_steamid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='steamId',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]