from django.db           import models
from API.BaseModel.Base  import Model

class UrlSchema(Model):
    url_code  = models.CharField(max_length=100)
    long_url  = models.CharField(max_length=100)
    short_url = models.CharField(max_length=100)

    def __str__(self):
        return self.short_url 

