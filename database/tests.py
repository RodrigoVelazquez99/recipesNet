from django.test import TestCase
from django.contrib.auth import get_user_model
from database.models import *

# Test for models
class ModelsTest(TestCase):

    # Init the objects for the test
    def setUp(self):
        User = get_user_model()
        user1 = User.objects.create_user(email="user1@gmail.com", username="user1", password="qwasasasqwqw1223232")
        Admin.objects.create(user=user1)
        user2 = User.objects.create_user(email="user2@gmail.com", username="user2", password="qwasasasqwqw1223233")
        chef = Chef.objects.create(user=user2, description="I like to cook bakes")
        user3 = User.objects.create_user(email="user3@gmail.com", username="user3", password="qwasasasqwqw1223234")
        Chef.objects.create(user=user3, description="I like to cook salads")
        ct = Category.objects.create(name="salsa verde")
        Recipe.objects.create(name="Enchiladas suizas", description="Unas enchiladas suizas con bajas calorias", category=ct, owner=chef)

    # Create user
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="user@gmail.com", username="user", password="foo_bar_zoo")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # Create superuser
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(email="superuser@gmail.com", username="superuser", password="foo_bar_zoo")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    # Find user saved
    def test_user(self):
        u = User.objects.get(username="user1")
        self.assertEqual(u.username, "user1")

    # Find only user with Admin role
    def test_admin(self):
        user = User.objects.get(email="user1@gmail.com")
        a = Admin.objects.get(user=user)
        self.assertEqual(a.user, user)

    # Find only user with Chef role
    def test_chef(self):
        user = User.objects.get(email="user2@gmail.com")
        c = Chef.objects.get(user=user)
        self.assertEqual(c.user, user)

    # Chef following another chef and unfollow
    def test_follow(self):
        user = User.objects.get(email="user2@gmail.com")
        user1 = User.objects.get(email="user3@gmail.com")
        chef = Chef.objects.get(user=user)
        chef1 = Chef.objects.get(user=user1)

        # chef follow chef1
        flag = chef.follow_chef(chef1)
        self.assertTrue(flag)
        # chef1 only has a follower
        self.assertEqual(chef1.followers.count(), 1)
        # chef only follow a chef
        self.assertEqual(chef.followees.count(), 1)
        # chef1 follows nobody
        self.assertEqual(chef1.followees.count(), 0)
        # chef has no followers
        self.assertEqual(chef.followers.count(), 0)

        # chef unfollow chef1
        flag = chef.follow_chef(chef1)
        self.assertFalse(flag)
        # chef1 has no followers
        self.assertEqual(chef1.followers.count(), 0)
        # chef not follow chef1
        self.assertEqual(chef.followees.count(), 0)
        # chef1 follows nobody
        self.assertEqual(chef1.followees.count(), 0)
        # chef has no followers
        self.assertEqual(chef.followers.count(), 0)

    # Set like to recipe or unlike if has like
    def test_recipe_like(self):
        user = User.objects.get(email="user2@gmail.com")
        user1 = User.objects.get(email="user3@gmail.com")
        chef = Chef.objects.get(user=user)
        chef1 = Chef.objects.get(user=user1)
        recipe = Recipe.objects.get(name="Enchiladas suizas")
        # Like to recipe
        flag = recipe.add_like(chef1)
        self.assertTrue(flag)
        # Unlike to recipe
        flag = recipe.add_like(chef1)
        self.assertFalse(flag)

    # Coment a recipe
    def test_recipe_coment(self):
        user = User.objects.get(email="user2@gmail.com")
        chef = Chef.objects.get(user=user)
        recipe = Recipe.objects.get(name="Enchiladas suizas")
        msg = "Excelente platillo !!!"
        self.assertEqual(recipe.coments.count(), 0)
        recipe.add_coment(chef, msg)
        self.assertEqual(recipe.coments.count(), 1)

    # Multiple coment to recipe
    def test_recipe_coment_multiple(self):
        user = User.objects.get(email="user2@gmail.com")
        chef = Chef.objects.get(user=user)
        recipe = Recipe.objects.get(name="Enchiladas suizas")
        msg = "Increible idea"
        msgc = "Increible idea"
        msg1 = "Buen platillo :)"
        self.assertEqual(recipe.coments.count(), 0)
        recipe.add_coment(chef, msg)
        self.assertEqual(recipe.coments.count(), 1)
        recipe.add_coment(chef, msgc)
        self.assertEqual(recipe.coments.count(), 2)
        recipe.add_coment(chef, msg1)
        self.assertEqual(recipe.coments.count(), 3)


    # Adding ingredients to recipe
    def test_recipe_add_ingredient(self):
        user = User.objects.get(email="user2@gmail.com")
        chef = Chef.objects.get(user=user)
        recipe = Recipe.objects.get(name="Enchiladas suizas")
        recipe.add_ingredient("Salsa de tomate")
        recipe.add_ingredient("Queso panela")
        ingredients = IngredientsRecipe.objects.filter(recipe=recipe)
        self.assertEqual(len(ingredients), 2)


    # Publish a post and followers will see it
    def test_post_publish(self):
        user = User.objects.get(email="user2@gmail.com")
        user1 = User.objects.get(email="user3@gmail.com")
        chef = Chef.objects.get(user=user)
        chef1 = Chef.objects.get(user=user1)
        recipe = Recipe.objects.get(name="Enchiladas suizas")
        chef.follow_chef(chef1)
        chef1.create_post(description="Una nueva presentación de mis enchiladas", recipe_published=recipe)
        post = Post.objects.filter(publisher=chef1)
        self.assertEqual(len(post), 1)
        # chef only see the post that chef1 created
        list_post = chef.refresh_post()
        self.assertEqual(len(list_post), 1)
        chef1.create_post(description="Ahora si la version final de las enchiladas", recipe_published=recipe)
        # chef see two post
        list_post = chef.refresh_post()
        self.assertEqual(len(list_post), 2)

    # Share a post to followers
    def test_post_share(self):
        user = User.objects.get(email="user2@gmail.com")
        user1 = User.objects.get(email="user3@gmail.com")
        user2 = User.objects.create(email="user4@gmail.com", username="user4", password="qwasasasqwqw1223235")
        chef = Chef.objects.get(user=user)
        chef1 = Chef.objects.get(user=user1)
        chef2 = Chef.objects.create(user=user2, description="I like to cook bakes")
        recipe = Recipe.objects.get(name="Enchiladas suizas")
        # chef follows chef1 who shares a post of chef2
        chef.follow_chef(chef1)
        chef2.create_post(description="Una nueva presentación de mis enchiladas", recipe_published=recipe)
        post = Post.objects.get(publisher=chef2)
        chef1.share_post(post)
        list_post = chef.refresh_post()
        # chef only see the post that shared chef1
        self.assertEqual(len(list_post), 1)
        list_post = chef1.refresh_post()
        # chef1 only see the original post of chef2
        self.assertEqual(len(list_post), 1)
        list_post = chef2.refresh_post()
        # chef2 only see his original post
        self.assertEqual(len(list_post), 1)
        chef.follow_chef(chef2)
        list_post = chef.refresh_post()
        # chef see the post that shared chef1 and the same post that published chef2
        self.assertEqual(len(list_post), 2)
