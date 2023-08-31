from django.db import models
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category ,self).save(*args, **kwargs)


    def __str__(self) -> str:
        return str(self.name)


class Brand(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to="brands/")

    def __str__(self) -> str:
        return str(self.name)


class Color(models.Model):
    name = models.CharField(max_length=128, unique=True)
    color_code = models.CharField(max_length=16, unique=True)

    def __str__(self) -> str:
        return str(self.name)


class Size(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    detail = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    size_variant = models.ManyToManyField(Size)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product ,self).save(*args, **kwargs)


    def __str__(self) -> str:
        return str(self.name)


'''class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.product.name)'''
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= "product_images")
    image = models.ImageField(upload_to="products/")
