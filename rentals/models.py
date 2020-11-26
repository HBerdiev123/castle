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
# from sorl.thumbnail import ImageField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import random
import os
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f"media/{final_filename}"


class Feature(models.Model):
	title           =models.CharField(max_length=255)
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

MESSAGE_STATUS = (
    ("0", "Not Replayed"),
    ("1", "Replayed")
)



class PropertyManager(models.Manager):
	def active_status(self):
		return self.filter(status="1").order_by('-id')

	def featured(self):
		return self.filter(featured=True).order_by('-id')

	def all(self):
		return self.filter(status="1").order_by('-id')

	def allproperties(self):
		return self.filter().order_by('-id')
	# def delete(self):
	# 	for obj in self.get_queryset():
	# 		obj.delete()
	

	# def count(self):
	# 	return self.count()
	# def none(self):
	# 	return self().filter()

	def min_price(self):
		max_min_price=self.filter(status="1").annotate(Min('price'), Max('price'))
		try:
			min_price=max_min_price[0].get().price__min
		except IndexError:
		    min_price=0
		except Exception as exception:
			min_price=0
		return min_price

	
	def max_price(self):
		max_min_price=self.filter(status="1").annotate(Min('price'), Max('price'))
		try:
		    max_price=max_min_price[1].price__max
		except IndexError:
		    max_price=Properties.objects.min_price()
		except Exception as exception:
			max_price=0

		return max_price
    

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
		    max_rental_price=Properties.objects.min_rent_price()
		except Exception as exception:
			max_rental_price=0

		return max_rental_price
    
	def min_sale_price(self):
		max_min_sale_price=self.filter(status="1", purpose="1").annotate(Min('price'), Max('price'))
		try:
			min_sale_price=max_min_sale_price[0].price__min
		except IndexError:
		    min_sale_price=0
		except Exception as exception:
			min_sale_price=0
		return min_sale_price

	def max_sale_price(self):
		max_min_sale_price=self.filter(status="1", purpose="1").annotate(Min('price'), Max('price'))
		try:
		    max_sale_price=max_min_sale_price[1].price__max

		except IndexError:
		    max_sale_price=Properties.objects.min_sale_price()
		except Exception as exception:
			max_sale_price=0

		return max_sale_price


	def get_by_id(self, id):
		qs = self.filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None




class Properties(models.Model):
	# address          =models.ForeignKey(Address, on_delete=models*.CASCADE)
	title			 =models.CharField(max_length=150)
	size             =models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
	price			 =models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
	bedroom			 =models.PositiveIntegerField(default=1)
	bathroom		 =models.PositiveIntegerField(null=True, blank=True)
	available_from   =models.DateField()
	status           =models.CharField(max_length=25, choices=PROPERTY_STATUS, default="1")
	purpose          =models.CharField(max_length=25, choices=PROPERTY_PURPOSE, default="1")
	category         =models.ForeignKey(PropertyCategory, on_delete=models.DO_NOTHING)
	year_built       =models.PositiveIntegerField()
	garage			 =models.PositiveIntegerField(default=0, blank=True)
	floor            =models.PositiveIntegerField()
	total_floor      =models.PositiveIntegerField(default=1)
	internet         =models.CharField(max_length=50, blank=True)
	description      =RichTextField()
	feature          =models.ManyToManyField(Feature, blank=True)
	pet_policy		 =models.CharField(max_length=50, choices=PET_POLICY, default="0")
	created     	 =models.DateTimeField(auto_now=True)
	featured 		 =models.BooleanField(default=False)

	house_number	=models.CharField(max_length=255, blank=True)
	street          =models.CharField(max_length=255)
	city			=models.CharField(max_length=255, blank=True)
	region			=models.CharField(max_length=255, blank=True)
	postal_Code		=models.CharField(max_length=255, blank=True)
	country			=models.CharField(max_length=255)
	latitude        =models.DecimalField(max_digits=22, decimal_places=16)
	longitude       =models.DecimalField(max_digits=22, decimal_places=16)
	# address_description     =RichTextField(blank=True)
	# created    		=models.DateTimeField(auto_now=True)


	slug 			 =models.SlugField(blank=True, unique=True)

	objects          =PropertyManager()        

	def get_absolute_url(self):
		return reverse("rentals:detail", kwargs={"id": self.id})



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



def property_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(property_pre_save_receiver, sender=Properties)


def validate_file_extension(value):
	ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
	valid_extensions = ['.jpg', '.png', '.jpeg', '.tif', ' .tiff']
	if not ext.lower() in valid_extensions:
		raise ValidationError('Unsupported file extension.')


class Picture(models.Model):
	title          =models.CharField(max_length=255, null=True, blank=True)
	properties     =models.ForeignKey(Properties, on_delete=models.CASCADE)
	description	   =models.TextField(null=True, blank=True)
	# picture        =models.FileField(upload_to=upload_image_path, validators=[validate_file_extension], null=True, blank=True)

	picture        =models.FileField(upload_to=upload_image_path, null=True, blank=True)
	created        =models.DateTimeField(auto_now=True)

	# def delete(self,*args,**kwargs):
	# 	if os.path.isfile(self.picture.path):
	# 		os.remove(self.picture.path)
	# 	super(Picture, self).delete(*args,**kwargs)

# 	def _delete_file(path):
# 		if os.path.isfile(path):
# 			os.remove(path)


# @receiver(pre_delete, sender=Picture)
# def delete_img_pre_delete_post(sender, instance, *args, **kwargs):
# 	if instance.picture:
# 		_delete_file(instance.picture.path)




phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")



class Message(models.Model):
	full_name	   =models.CharField(max_length=255)
	phone_number   =models.CharField(validators=[phone_regex], max_length=17, blank=True)
	email          =models.EmailField()
	message        =models.TextField()
	properties     =models.ForeignKey(Properties, on_delete=models.CASCADE)
	status         =models.CharField(max_length=50, choices=MESSAGE_STATUS, default="0")
	created        =models.DateTimeField(auto_now=True)
	






class ReplyMessage(models.Model):
	title           =models.CharField(max_length=255)
	reply_message   =models.TextField()
	message         =models.ManyToManyField(Message)
	created         =models.DateTimeField(auto_now=True)
	user            =models.ManyToManyField(User)





# class Address(models.Model):
# 	# title			=models.CharField(max_length=255)
# 	house_number	=models.CharField(max_length=255, blank=True)
# 	street          =models.CharField(max_length=255)
# 	city			=models.CharField(max_length=255, blank=True)
# 	region			=models.CharField(max_length=255, blank=True)
# 	postal_Code		=models.CharField(max_length=255, blank=True)
# 	country			=models.CharField(max_length=255)
# 	latitude        =models.DecimalField(max_digits=22, decimal_places=16)
# 	longitude       =models.DecimalField(max_digits=22, decimal_places=16)
# 	address_description     =RichTextField(blank=True)
# 	created    		=models.DateTimeField(auto_now=True)





# class Address(models.Model):
# 	title			=models.CharField(max_length=255)
# 	house_number	=models.CharField(max_length=255, blank=True)
# 	street          =models.CharField(max_length=255)
# 	city			=models.CharField(max_length=255, blank=True)
# 	region			=models.CharField(max_length=255, blank=True)
# 	postal_Code		=models.CharField(max_length=255, blank=True)
# 	country			=models.CharField(max_length=255)
# 	latitude        =models.DecimalField(max_digits=22, decimal_places=16)
# 	longitude       =models.DecimalField(max_digits=22, decimal_places=16)
# 	description     =RichTextField()
# 	created    		=models.DateTimeField(auto_now=True)

# class Property(models.Model):
# 	address          =models.ForeignKey(Address, on_delete=models.CASCADE)
# 	title			 =models.CharField(max_length=150)
# 	size             =models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
# 	price			 =models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
# 	bedroom			 =models.PositiveIntegerField(default=1)
# 	bathroom		 =models.PositiveIntegerField(blank=True)
# 	available_from   =models.DateField()
# 	status           =models.CharField(max_length=25, choices=PROPERTY_STATUS, default="1")
# 	purpose          =models.CharField(max_length=25, choices=PROPERTY_PURPOSE, default="1")
# 	category         =models.ForeignKey(PropertyCategory, on_delete=models.DO_NOTHING)
# 	year_built       =models.PositiveIntegerField()
# 	garage			 =models.PositiveIntegerField(default=0, blank=True)
# 	floor            =models.PositiveIntegerField()
# 	total_floor      =models.PositiveIntegerField(default=1)
# 	internet         =models.CharField(max_length=50, blank=True)
# 	description      =RichTextField()
# 	feature          =models.ForeignKey(Feature, on_delete=models.DO_NOTHING)
# 	pet_policy		 =models.CharField(max_length=50, choices=PET_POLICY, default="0")
# 	picture          =models.ForeignKey(Picture, on_delete=models.CASCADE)
# 	created     	 =models.DateTimeField(auto_now=True)
# 	slug 			= models.SlugField(blank=True, unique=True)


# 	def get_absolute_url(self):
# 		return reverse("rental:detail", kwargs={"slug": self.slug})



# def property_pre_save_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)


# pre_save.connect(property_pre_save_receiver, sender=Property)

