from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    
class MainSilder(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_info/')
    date = models.DateTimeField(auto_now=False)
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class StartSlider(models.Model):
    image = models.ImageField(upload_to='user_info/')
    info = models.CharField(max_length=255)

class Posts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    image = models.ImageField(upload_to='user_info/')

    def __str__(self):
        return self.title

class Featured(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user_info/')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    info = models.TextField()

    def __str__(self):
        return self.name
