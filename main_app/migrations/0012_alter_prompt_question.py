# Generated by Django 4.1 on 2022-08-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_prompt_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prompt',
            name='question',
            field=models.CharField(max_length=250),
        ),
    ]