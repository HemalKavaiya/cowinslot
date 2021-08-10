from django.db import models

# Create your models here.
class User(models.Model):
    status_choice = (
        (0,'disabled'),
        (1,'active')
    )

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    pin = models.IntegerField()
    age = models.IntegerField()
    status = models.IntegerField(choices=status_choice,default=1)

    def __str__(self):
        return self.name