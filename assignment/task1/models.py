from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=300)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    image=models.ImageField('images/')
    creation_date=models.DateTimeField(auto_now=True)
    published_date=models.DateField(null=True)
    published=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering=['-published_date','-creation_date']