# Generated by Django 4.2.2 on 2023-07-15 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_fastfood_yangsig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='menu/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Chinese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='menu/%Y/%m/%d')),
            ],
        ),
    ]