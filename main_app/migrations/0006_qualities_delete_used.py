# Generated by Django 4.1 on 2022-08-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_used_asked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Used',
        ),
    ]
