from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('new_arrival', 'New Arrival'),
        ('best_selling', 'Best Selling'),
        ('you_may_also_like', 'You May Also Like'),
        ('men', 'Shop for Men'),
        ('women', 'Shop for Women'),
        ('accessories', 'Shop Accessories'),
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='new_arrival')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AboutDetail(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_details/')
    content = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product') # A user can only add a product to wishlist once

    def __str__(self):
        return f"{self.product.name} in {self.user.username}'s wishlist"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product') # A user can only have one entry for a product in cart

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.user.username}'s cart"
