# Generated by Django 4.1.3 on 2022-11-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_blog', '0007_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(related_name='posts', to='simple_blog.hashtag'),
        ),
    ]
