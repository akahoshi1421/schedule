# Generated by Django 3.1.7 on 2021-08-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('time', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('conect', models.IntegerField()),
            ],
        ),
    ]
