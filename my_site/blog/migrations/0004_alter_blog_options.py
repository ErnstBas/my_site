# Generated by Django 5.1.1 on 2024-09-14 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_options_alter_blog_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date']},
        ),
    ]
