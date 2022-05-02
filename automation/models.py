from django.db import models

# Create your models here.
class Email(models.Model):
    Username = models.CharField(max_length=250)
    email = models.EmailField()
    
    def __str__(self):
        return self.email
       
class Subscription(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
      
class Subscriber(models.Model):
    email = models.ForeignKey(Email, on_delete= models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete= models.CASCADE)
    
    # def __str__(self):
    #     return self.email

# class Contact(models.Model):
    