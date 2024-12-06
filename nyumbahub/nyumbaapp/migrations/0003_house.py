# Generated by Django 5.1.3 on 2024-12-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nyumbaapp', '0002_rename_sellers_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('size', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('amenities', models.CharField(max_length=50)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='house_images/')),
            ],
        ),
    ]
