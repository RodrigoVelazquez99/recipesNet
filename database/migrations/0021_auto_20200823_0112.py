# Generated by Django 3.0.9 on 2020-08-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_img/'),
        ),
    ]
