# Generated by Django 5.0.4 on 2024-04-30 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0006_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='book',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
