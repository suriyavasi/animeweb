from django.db import models
# from django.utils.text import slugify



# catagory
class Category(models.Model):
    name = models.CharField( max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    img_url = models.URLField(max_length=800,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
        
    
        
    
        
    def __str__(self):
        return self.title


class AboutUs(models.Model):
    content = models.TextField()


    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})




   
    
