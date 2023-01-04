# Generated by Django 4.1.4 on 2023-01-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.CharField(max_length=60)),
                ('contact_number', models.CharField(max_length=60)),
                ('roll', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=30)),
            ],
        ),
    ]