# Generated by Django 4.2.3 on 2023-08-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_rename_likes_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commenttext',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]