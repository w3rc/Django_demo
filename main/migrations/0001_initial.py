# Generated by Django 2.2.3 on 2019-07-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abcd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song1_name', models.CharField(max_length=100)),
                ('song1_description', models.TextField()),
                ('song1_uploaddate', models.DateField()),
            ],
        ),
    ]