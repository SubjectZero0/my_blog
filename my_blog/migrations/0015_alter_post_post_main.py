# Generated by Django 4.1 on 2022-09-04 15:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0014_alter_post_post_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_main',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name=''),
        ),
    ]
