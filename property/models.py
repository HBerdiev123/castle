from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
# from filer.fields.image import FilerImageField
from django.urls import reverse
from castle.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.db.models import Max, Min
from django.conf import settings 

# Create your models here.

class Feature(models.Model):
	title          =models.CharField(max_length=255)
	description    =models.TextField()
	created        =models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class PropertyCategory(models.Model):
	title          =models.CharField(max_length=255)
	description    =models.TextField()
	created        =models.DateTimeField(auto_now=True)



PROPERTY_STATUS = (
    ("0","Not Available"),
    ("1","Available")
)
PROPERTY_PURPOSE = (
    ("0","Rent"),
    ("1","Sale")
)


PET_POLICY= (
    ("0","Not Allowed"),
    ("1","Allowed"),
    ("2","Unknown"),
)



class Address(models.Model):
	# title			=models.CharField(max_length=255)
	house_number	=models.CharField(max_length=255, blank=True)
	street          =models.CharField(max_length=255)
	city			=models.CharField(max_length=255, blank=True)
	region			=models.CharField(max_length=255, blank=True)
	postal_Code		=models.CharField(max_length=255, blank=True)
	country			=models.CharField(max_length=255)
	latitude        =models.DecimalField(max_digits=22, decimal_places=16)
	longitude       =models.DecimalField(max_digits=22, decimal_places=16)
	address_description     =RichTextField(blank=True)
	created    		=models.DateTimeField(auto_now=True)


class PropertyManager(models.Manager):
	def active_status(self):
		return self.filter(status="1")

	def featured(self):
		return self.filter(featured=True)

	def all(self):
		return self.filter()
	# def none(self):
	# 	return self().filter()

	def min_rent_price(self):
		max_min_rental_price=self.filter(status="1", purpose="0").annotate(Min('price'), Max('price'))
		try:
			min_rent_price=max_min_rental_price[0].price__min
		except IndexError:
		    min_rent_price=0
		except Exception as exception:
			min_rent_price=0
		return min_rent_price
	
	def max_rent_price(self):
		max_min_rental_price=self.filter(status="1", purpose="0").annotate(Min('price'), Max('price'))
		try:
		    max_rental_price=max_min_rental_price[1].price__max
		except IndexError:
		    max_rental_price=Property.objects.min_rent_price()
		except Exception as exception:
			max_rental_price=0

		return max_rental_price


	def get_by_id(self, id):
		qs = self.filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None




class Property(models.Model):
	user		     = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='properties', on_delete=models.CASCADE)
	address            = models.CharField(max_length=255)
	short_description  = models.CharField(max_length=150, blank=True, null=True)
	size             = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
	price			 = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
	bedroom			 = models.PositiveIntegerField(default=1)
	bathroom		 = models.PositiveIntegerField(blank=True)
	available_from   = models.DateField()
	status           = models.CharField(max_length=25, choices=PROPERTY_STATUS, default="1")
	purpose          = models.CharField(max_length=25, choices=PROPERTY_PURPOSE, default="1")
	category         = models.ForeignKey(PropertyCategory, on_delete=models.DO_NOTHING)
	year_built       = models.PositiveIntegerField()
	garage			 = models.PositiveIntegerField(default=0, blank=True)
	floor            = models.PositiveIntegerField()
	total_floor      = models.PositiveIntegerField(default=1)
	internet         = models.CharField(max_length=50, blank=True)
	description      = RichTextField()
	feature          = models.ManyToManyField(Feature)
	pet_policy		 = models.CharField(max_length=50, choices=PET_POLICY, default="0")
	# picture          =models.ForeignKey(Picture, on_delete=models.CASCADE)
	created     	 = models.DateTimeField(auto_now=True)
	featured 		 = models.BooleanField(default=False, blank=True)
	slug 			 = models.SlugField(blank=True, unique=True)

	objects          = PropertyManager()        

	def get_absolute_url(self):
		return reverse("rentals:detail", kwargs={"id": self.id})

	class Meta:
		ordering = ['-created']
		
	def __str__(self):
		return f'Address: {self.address} status: {self.status}'

	# def save(self, *args, **kwargs):
	# 	if not self.user:
	# 		self.user = django.contrib.auth.get_user_model()
	# 		print(django.contrib.auth.get_user_model())
	# 	super().save(*args, *kwargs)	 	

def property_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(property_pre_save_receiver, sender=Property)


class Picture(models.Model):
	title          = models.CharField(max_length=255, blank=True, null=True)
	# description	   = models.TextField(blank=True, null=True)
	Property       = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images_created', blank=True, null=True)
	picture        = models.ImageField(null=True, blank=True)
	created_at     = models.DateTimeField(auto_now=True, db_index=True)
	update_at = models.DateTimeField(auto_now_add=True)

	# def __str__(self):
		# return self.title

class FeaturedProperties(models.Model):
	prop   		= models.ForeignKey(Property, on_delete=models.CASCADE, related_name='featured_prop')
	is_active 	= models.BooleanField(default=True)
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True) 