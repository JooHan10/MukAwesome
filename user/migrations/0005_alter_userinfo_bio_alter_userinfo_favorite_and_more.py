# Generated by Django 4.2 on 2023-04-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userinfo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='favorite',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mbti',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tmi',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]