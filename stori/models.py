from django.db import models

# Create your models here.


STATUS_CHOICES = {
    "d": "Draft",
    "p": "Published",
    "w": "Withdrawn",
}


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="d")    
    Category=models.ForeignKey('Category',null=True, blank=True,on_delete=models.CASCADE)
       
    class Meta:
        verbose_name_plural = ("Blogs")
        ordering = ('-title',)
        indexes = [models.Index(fields=['title']),]

    def __str__(self) -> str:
        return self.title
   
class Category(models.Model):
    name = models.CharField(max_length=255) 