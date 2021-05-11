# Generated by Django 3.2.1 on 2021-05-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_trigger_lang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('content', models.CharField(blank=True, max_length=100)),
                ('answer', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
