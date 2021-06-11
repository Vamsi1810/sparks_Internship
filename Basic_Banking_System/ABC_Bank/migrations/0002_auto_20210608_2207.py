# Generated by Django 3.2.4 on 2021-06-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABC_Bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdata',
            name='account_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customerdata',
            name='mobile',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='amount',
            field=models.IntegerField(verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='fromaccount',
            field=models.IntegerField(verbose_name='From Account'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='toaccount',
            field=models.IntegerField(verbose_name='To Account'),
        ),
    ]