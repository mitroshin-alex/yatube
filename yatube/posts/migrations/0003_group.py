# Generated by Django 2.2.19 on 2022-02-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]