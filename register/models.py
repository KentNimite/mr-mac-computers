from django.db import models
from django.forms import ModelForm
from django.urls import reverse
# Used to generate URLs by reversing the URL patterns



class HomePage(models.Model):
    page_title = models.CharField(max_length=160)
    page_heading = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    page_paragraph = models.CharField(max_length=200)
    page_about_us = models.CharField(max_length=200)
    page_display_heading1 = models.CharField(max_length=200)
    page_display_heading2 = models.CharField(max_length=200)
    page_display_paragraph = models.CharField(max_length=200)
    page_display_image = models.ImageField(upload_to='images/')
    page_footer_paragraph = models.CharField(max_length=200)
    page_footer_location_paragraph = models.CharField(max_length=200)
    page_footer_phonemumber_paragraph = models.CharField(max_length=200)

    def __str__(self):
        return self.page_title




class Gallery(models.Model):
    date_added = models.DateTimeField('Last Updated')
    photo = models.ImageField(upload_to='images/')
    name_of_item = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name_of_item


class ShoppingItem(models.Model):
    photo = models.ImageField(upload_to='images/')
    paystack_url = models.URLField(max_length=200, unique=True)
    item_name = models.CharField(max_length=100, unique=True)
    item_description = models.TextField('Page Content', blank=True)
    priority_level = models.IntegerField(default=1)

    class Meta:
        ordering = ['priority_level']

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('shoppingitem_detail', args = [str(self.id)])        
