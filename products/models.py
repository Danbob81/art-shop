""" Products and categories models """
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    """ Category model """
    class Meta:
        """ Make category name plural """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ to return friendly name """
        return self.friendly_name


class SubCategory(models.Model):
    """ Sub-category model """
    class Meta:
        """ Make sub-category name plural """
        verbose_name_plural = 'Sub-categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """to return friendly name"""
        return self.friendly_name


class Product(models.Model):
    """ Product details """
    category = models.ForeignKey('Category', null=True, blank=False,
                                 on_delete=models.SET_NULL)
    sub_category = models.ForeignKey('SubCategory', null=True, blank=False,
                                     on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    stock_qty = models.PositiveSmallIntegerField(default=1,
                                                 validators=[
                                                     MaxValueValidator(100),
                                                     MinValueValidator(0),
                                                 ],
                                                 null=True,
                                                 blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
