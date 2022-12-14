# Generated by Django 3.2 on 2022-08-21 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tweets', '0002_auto_20220812_1926'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField(blank=True, null=True)),
                ('byuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useraction', to=settings.AUTH_USER_MODEL)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweetaction', to='tweets.tweet')),
            ],
        ),
    ]
