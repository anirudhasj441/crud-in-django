# Generated by Django 3.0.3 on 2020-03-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('qualification', models.CharField(blank=True, max_length=30, null=True)),
                ('contact', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'employees',
            },
        ),
    ]
