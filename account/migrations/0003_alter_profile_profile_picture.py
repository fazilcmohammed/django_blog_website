# Generated by Django 5.1.4 on 2024-12-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]