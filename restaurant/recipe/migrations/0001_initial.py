# Generated by Django 5.0.1 on 2024-01-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_desc', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipe')),
            ],
        ),
    ]
