# Generated by Django 3.2.4 on 2021-06-08 16:25

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
                ('mobile', models.IntegerField(max_length=10, unique=True)),
                ('account_number', models.IntegerField(max_length=6)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromaccount', models.IntegerField(max_length=6, verbose_name='From Account')),
                ('toaccount', models.IntegerField(max_length=6, verbose_name='To Account')),
                ('amount', models.IntegerField(max_length=10, verbose_name='Amount')),
            ],
        ),
    ]