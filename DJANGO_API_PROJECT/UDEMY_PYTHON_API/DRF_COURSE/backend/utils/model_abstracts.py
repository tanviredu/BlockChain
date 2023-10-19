import uuid
from django.db import models



## this is a base Model what will
## be imported already an id is given
class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True