# Generated by Django 2.2.8 on 2019-12-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191217_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信用户id')),
                ('avatar', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像')),
                ('nickname', models.CharField(blank=True, max_length=255, null=True, verbose_name='昵称')),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='用户账号')),
                ('password', models.CharField(blank=True, max_length=255, null=True, verbose_name='密码')),
                ('status', models.CharField(choices=[('enabled', '启用'), ('disabled', '禁用')], default='enabled', max_length=100, verbose_name='状态')),
                ('nickname', models.CharField(blank=True, max_length=255, null=True, verbose_name='昵称')),
                ('avatar', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像')),
                ('create_time', models.DateTimeField(blank=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
