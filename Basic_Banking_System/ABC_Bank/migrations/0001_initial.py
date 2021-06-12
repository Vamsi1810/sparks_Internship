# Generated by Django 3.2.4 on 2021-06-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile', models.BigIntegerField(unique=True)),
                ('account_number', models.BigIntegerField()),
                ('balance', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromaccount', models.BigIntegerField(verbose_name='From Account')),
                ('toaccount', models.BigIntegerField(verbose_name='To Account')),
                ('amount', models.BigIntegerField(verbose_name='Amount')),
            ],
        ),
    ]
