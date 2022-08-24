from django.db import models as m

import datetime
from django.utils import timezone

class Categories(m.Model):
    name = m.CharField(max_length=255)
    pub_date = m.DateTimeField('date published')
    
    def __str__(self):
        return self.name
    
    def was_published_recently(x):
        return x.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Products(m.Model):
    category = m.ForeignKey(Categories, on_delete=m.CASCADE)
    name = m.CharField(max_length=255)
    price = m.IntegerField(default=0)

    def __str__(self):
        return self.name


    
