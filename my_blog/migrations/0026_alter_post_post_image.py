# Generated by Django 4.1 on 2022-09-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0025_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='my_blog/static/my_blog/media/', verbose_name='Post Thumbnail'),
        ),
    ]
