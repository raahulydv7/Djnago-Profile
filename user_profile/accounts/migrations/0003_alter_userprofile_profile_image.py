# Generated by Django 5.1.6 on 2025-03-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
    ]
