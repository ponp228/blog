# Generated by Django 5.0.4 on 2024-05-08 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_post_feature_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_ta',
            new_name='created_at',
        ),
    ]
