from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    minimum_age_appropriate = models.IntegerField(default=0, blank=False)
    maximum_age_appropriate = models.IntegerField(default=-1, blank=False)

    def __str__(self):
        return f"{self.name}, price {self.price:.02f}"

    def age_range(self):
        if self.maximum_age_appropriate == -1:
            return f"Ages {self.minimum_age_appropriate} and up"
        elif self.maximum_age_appropriate == self.minimum_age_appropriate:
            return f"Age {self.minimum_age_appropriate}"
        else:
            return f"Ages {self.minimum_age_appropriate} to {self.maximum_age_appropriate}"

    def random_image(self):
      products = self.productimage_set.all()
      if not products.exists():
        return
      else:
        products = products.order_by('?')
        return products[0]

class ProductImage(models.Model):
  image = models.ImageField(upload_to='product_images/', blank=False)
  caption = models.CharField(max_length=255, blank=True)
  product = models.ForeignKey(Product, on_delete = models.CASCADE, blank=False)

  def __str__(self):
    if (self.caption == None):
      return  self.product
    else:
      return f"{self.product}: {self.caption}"