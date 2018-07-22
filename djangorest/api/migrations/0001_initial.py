# Generated by Django 2.0.1 on 2018-01-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20, unique='true')),
                ('email', models.CharField(max_length=20, unique='true')),
                ('password', models.CharField(max_length=20)),
                ('hackerrank', models.CharField(max_length=20, unique='true')),
                ('codeforces', models.CharField(max_length=20, unique='true')),
                ('about', models.CharField(max_length=200)),
            ],
        ),
    ]
