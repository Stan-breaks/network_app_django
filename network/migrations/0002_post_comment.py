# Generated by Django 4.2.3 on 2023-07-31 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('likes', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='network.post')),
                ('user', models.ManyToManyField(related_name='commentUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
