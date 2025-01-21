from django.db import models

class Product(models.Model):
      id = models.IntegerField(primary_key=True)
      name = models.CharField(max_length=20)
      image = models.ImageField(upload_to='images/')
      price = models.IntegerField()
      def __str__(self):
            return f"{self.id} {self.name} {self.image} {self.price}"

