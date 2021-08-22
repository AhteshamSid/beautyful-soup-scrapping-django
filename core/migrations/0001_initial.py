# Generated by Django 3.2.3 on 2021-08-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portal', models.CharField(choices=[('ndtv.com', 'ndtv.com'), ('soundcloud.com', 'soundcloud.com')], max_length=100)),
                ('title', models.CharField(max_length=256)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField()),
            ],
        ),
    ]