from django.db import models

# Create your models here.
class Record(models.Model):
    # Automatically added timestamp for new record 
    created_at = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone =  models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        # Return some data from the record 
        return(f"{self.first_name}{self.last_name}")
