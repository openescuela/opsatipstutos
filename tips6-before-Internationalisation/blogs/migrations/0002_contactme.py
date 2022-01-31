# Generated by Django 3.2.11 on 2022-01-31 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Your email address will not be published', max_length=254, verbose_name='Email')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]