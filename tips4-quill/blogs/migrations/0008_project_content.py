# Generated by Django 3.2.11 on 2022-01-29 09:49

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_remove_project_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=django_quill.fields.QuillField(default='ici'),
        ),
    ]