from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
    
class Food(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="food/")
    price = models.DecimalField(max_digits=10,decimal_places=2)
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='foods')
    
    def __str__(self) -> str:
        return self.title
    
class Order(models.Model):
    PICKUP = 'pickup'
    DELIIVERY = 'delivery'
    SHIPPING_TYPES = (
        (PICKUP,'Pick-up'),
        (DELIIVERY,'Delivery')
    )
    client = models.ForeignKey('Client',on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)
    shipping = models.CharField(max_length=10,choices=SHIPPING_TYPES,default=DELIIVERY)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.client.full_name} - Order {self.pk}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    food = models.ForeignKey(Food,on_delete=models.CASCADE,related_name='order_items')
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    
    def __str__(self) -> str:
        return self.full_name
    
