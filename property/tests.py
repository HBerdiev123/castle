from django.test import TestCase, Client
from .models import Property, PropertyCategory
import random
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import User
# Create your tests here.

user = get_user_model().objects.get(id=2)
# user= authenticate(username='khusan', password='Adgjmptw')
# user = login(User.objects.get(id=2))

cat = PropertyCategory.objects.get(id=1)
class ProfiletestCase(TestCase):
	def setUp(self):
		self.client = Client()
		login = self.client.force_login(user)
		self.property = Property.objects.create(
			user=login, address="45 Regent Street, London, UK status", short_description="Historic Town House", size=12,
			price=12, bedroom=2,bathroom=1,available_from='2020-12-12',status=1,category=cat,
			year_built=1,floor=1,internet='available',description='Best home to live',slug='sd')
		self.property.feature.add(1)

	def test_property(self):
		lion = Property.objects.get(short_description="Historic Town House")
		self.assertEqual(lion.speak(), 'Historic Town House')

