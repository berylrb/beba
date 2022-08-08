# Generated by Django 4.1 on 2022-08-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Used',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asked', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateField(verbose_name='Response date'),
        ),
    ]
