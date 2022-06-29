from django.db import models


class List(models.Model):
    '''list on page'''
    pass


class Item(models.Model):
    '''element of list'''
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

