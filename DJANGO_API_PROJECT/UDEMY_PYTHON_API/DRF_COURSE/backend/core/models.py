from django.db                   import models
from utils.model_abstracts       import Model
from django_extensions.db.models import TimeStampedModel 
from django_extensions.db.models import ActivatorModel
from django_extensions.db.models import TitleDescriptionModel

## press control and click the models
# and see what properties they have
# timeStampModel will have created_at, modified_at
# ActivatorModel has active , inactive
# Title Descriptor model has title and descripton field
# and all of them ar inheritable/abstract

class Contact(TimeStampedModel,ActivatorModel,TitleDescriptionModel,Model):
    email = models.EmailField(verbose_name="Email")
    
    class Meta:
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return  self.title



# Create your models here.
