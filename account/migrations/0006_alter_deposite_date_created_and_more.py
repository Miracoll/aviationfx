# Generated by Django 4.1.7 on 2023-03-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_withdrawal_options_alter_deposite_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposite',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='expire_time',
            field=models.DateTimeField(),
        ),
    ]
