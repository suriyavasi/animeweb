from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help ="this command catagory data"
  

    def handle(self,*args:Any, **options:Any) :
        Category.objects.all().delete()
        
        
        
        categories = ['Action','Adventure','Drama','Demons','Cars']

        for category_name in categories:            
            Category.objects.create(name = category_name )

        self.stdout.write(self.style.SUCCESS("compeleted inserting categoty data"))    
