# Generated by Django 4.2 on 2023-05-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(help_text='insira seu email', max_length=254)),
                ('cpf', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
