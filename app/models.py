from django.db import models
from django.contrib.auth.models import User
#from django.core.validators import maxValueError,MinValueValidator

# Create your models here.
STATIC_CHOICE = (
    ("jamu nd kashmir","jamu nd kashmir"),
    ("andra pradesh","andra pradesh"),
    ("uttar pradesh","uttar pradesh"),
    ("madh pradesh", "madh pradesh"),
    ('chennai', 'chennai')
)

class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices =STATIC_CHOICE,max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICE = (
    ('m','mobile'),
    ('l','laptop'),
    ('tw','top wear'),
    ('bw','bottom wear'),
)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category= models.CharField(choices =CATEGORY_CHOICE,max_length=2)
    product_imag= models.ImageField(upload_to='productingimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICE=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Deleverd','Delevered'),
    ('Cancel','Cancel')
)

class OrderPlace(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices =STATIC_CHOICE,default='PENDING')



