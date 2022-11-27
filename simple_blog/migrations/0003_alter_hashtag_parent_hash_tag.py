# Generated by Django 4.1.3 on 2022-11-27 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simple_blog', '0002_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='parent_hash_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hash_tags', to='simple_blog.hashtag'),
        ),
    ]