# Generated by Django 3.0.9 on 2020-09-04 01:18

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('is_chef', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='admin', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='chef', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'chef',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id_recipe', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='recipe_img/')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes_category', to='database.Category')),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('recipe_published', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Recipe')),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='ComentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_coments', to='database.Post')),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Chef')),
            ],
            options={
                'db_table': 'coment_post',
            },
        ),
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_coments', to='database.Recipe')),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Chef')),
            ],
            options={
                'db_table': 'coment',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='coments',
            field=models.ManyToManyField(related_name='recipes_coments', through='database.Coment', to='database.Chef'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(related_name='recipe_likes', to='database.Chef'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Chef'),
        ),
        migrations.AddField(
            model_name='post',
            name='coments',
            field=models.ManyToManyField(related_name='post_coments', through='database.ComentPost', to='database.Chef'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to='database.Chef'),
        ),
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Chef'),
        ),
        migrations.AddField(
            model_name='post',
            name='sharer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_shared', to='database.Chef'),
        ),
        migrations.AddField(
            model_name='post',
            name='sharers',
            field=models.ManyToManyField(related_name='shared_post', to='database.Chef'),
        ),
        migrations.CreateModel(
            name='IngredientsRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=20)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='database.Recipe')),
            ],
            options={
                'db_table': 'ingredients_recipe',
                'unique_together': {('recipe', 'ingredient')},
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_chef', to='database.Chef')),
                ('to_chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_chef', to='database.Chef')),
            ],
            options={
                'db_table': 'follow',
                'unique_together': {('to_chef', 'from_chef')},
            },
        ),
        migrations.AddField(
            model_name='chef',
            name='followers',
            field=models.ManyToManyField(related_name='followees', through='database.Follow', to='database.Chef'),
        ),
    ]
