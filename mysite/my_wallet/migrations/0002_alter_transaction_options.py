# Generated by Django 4.2 on 2023-06-26 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['date']},
        ),
    ]
