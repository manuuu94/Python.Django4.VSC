from django.db import models
#validator
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
#create the class and inherit from model.Model
#you can add columns later on but try to be as accurate as possible
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)]) 
    #adding a new value and makemigrations will required to include a default in (), or set null = True
    heartrate = models.IntegerField(default=69,validators=[MinValueValidator(1),MaxValueValidator(300)])


#string representation of the object within the class
    def __str__(self):
        return f"ID: {self.id} - {self.last_name},{self.first_name} is {self.age} years old : heartrate {self.heartrate}"


