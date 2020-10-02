from django.db import models
import numpy as np
import  PIL
from PIL import Image
from django.core.files.base import ContentFile
from .views import cartoonize
from io import BytesIO

# Create your models here.
class cartoonizer(models.Model):
    GRAYSCALE = 'GR'
    image_modifications= [
        (GRAYSCALE, 'grayscale'),
    ]
    action= models.CharField(
        max_length=2,
        choices=image_modifications,
        default=GRAYSCALE,
    )
    image = models.ImageField(upload_to='media/')
    
    #for naming purposes 
    
    def __str__(self):
        return str(self.id)
    
    #saving image once snding it alog with required parameters for actions to be applied onto it.
    
    def save(self,*args,**kwargs):
        pil_image=Image.open(self.image)               #to use Image we need to install pillow
        
        #convert to array 
        cv_image=np.array(pil_image)            #need to import numpy
        img=cartoonize(cv_image,self.action)         
        
        #convert back
        image_pil = Image.fromarray(img)
        buffer = BytesIO()
        image_pil.save(buffer,format='png')
        
        image_png=buffer.getvalue()
        self.image.save(str(self.image),ContentFile (image_png) , save=False)
        
        super().save(*args,**kwargs)
        
