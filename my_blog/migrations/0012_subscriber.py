# Generated by Django 4.1 on 2022-08-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0011_alter_post_draft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('l_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
