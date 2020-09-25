from django.db import models

# Create your models here.

class Like(models.Model):
    user_id = models.IntegerField(null=True)
<<<<<<< HEAD
    dog_id = models.CharField(max_length=300, null=True)
=======
    dog_id = models.IntegerField(null=True)
>>>>>>> develop_ssh_data
