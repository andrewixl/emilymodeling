# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
from datetime import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class AlbumManager(models.Manager):
    def createAlbum(self, postData, user_id):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['product_name']) < 3:
			results['status'] = False
			results['errors'].append('Product Name Must be at Least 3 Characters.')
        if len(postData['price']) < 1:
			results['status'] = False
			results['errors'].append('Please Enter a Valid Price.')
        if len(postData['weight']) < 1:
			results['status'] = False
			results['errors'].append('Please Enter a Valid Weight in Pounds.')
        if len(postData['description']) < 10:
			results['status'] = False
			results['errors'].append('Description Must be at Least 10 Characters.')
        url = URLValidator()
        try:
            url(postData['image_link'])
        except:
            results['status'] = False
            results['errors'].append('Please Enter Proper Url such as http://google.com')

        if results['status'] == True:
            userInt = int(user_id)
            user = User.objects.get(id=userInt)
            results['person'] = Person.objects.create(product_name=postData['product_name'], price=postData['price'], weight=postData['weight'], image_link=postData['image_link'], description=postData['description'], views=0, seller=user)
        return results


class Album(models.Model):
    album_name = models.CharField(max_length=25)
    # album_cover = models.ManyToManyField('Photo', related_name="photo")
    album_location = models.CharField(max_length=25)
    album_description = models.CharField(max_length=50)
    shoot_date = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AlbumManager()

    def __str__(self):
        return self.album_name

class PhotoManager(models.Manager):
    def createPhoto(self, postData, user_id):
        results = {'status': True, 'errors': [], 'user': None}
        if len(postData['destination']) < 3:
			results['status'] = False
			results['errors'].append('Destination Name Must be at Least 3 Characters.')
        if len(postData['description']) < 10:
			results['status'] = False
			results['errors'].append('Description Must be at Least 10 Characters.')
        if postData['travelstartdate'] > postData['travelenddate'] or str(postData["travelstartdate"]) < str(datetime.now().date()):
			results['status'] = False
			results['errors'].append('End Date Must Be After Start Date and Future Dated.')
        # if len(postData['travelenddate']) < 1:
		# 	results['status'] = False
		# 	results['errors'].append('Description Must be at Least 10 Characters.')

        if results['status'] == True:
            userInt = int(user_id)
            user = User.objects.get(id=userInt)
            results['plan'] = Plan.objects.create(destination=postData['destination'], description=postData['description'], travelstartdate=postData['travelstartdate'], travelenddate=postData['travelenddate'], owner=user)
        return results


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'media/', default = 'media/None/no-img.jpg')
    photo_caption = models.CharField(max_length=25)
    photo_description = models.CharField(max_length=50)
    master_album = models.ManyToManyField('Album', related_name="album")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PhotoManager()

    def __str__(self):
        return self.photo_caption

class Home(models.Model):
    slide_1 = models.ManyToManyField('Photo', related_name="slide_1")
    slide_2 = models.ManyToManyField('Photo', related_name="slide_2")
    slide_3 = models.ManyToManyField('Photo', related_name="slide_3")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects = PhotoManager()
