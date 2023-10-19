from django.db.models.signals        import post_save,post_delete
from django.dispatch                 import receiver
from django.contrib.auth.models      import User
from rest_framework.authtoken.models import Token

@receiver(post_save,send=User)
def report_uploaded(sender,instance,created):
    if created:
        Token.objects.create(user = instance)
    

## Signals is coming from the database
## when a data stored in a database
## it  will give  a signal
## it can be pre save or post save
## it tells that in this case that 
## do that when save the user instance
#sender: This tells us what sent the signal, in this case,
#it's a User.
#
# instance: This is the actual user that was 
# just created.

#created: This is a flag that tells us if the user was just created or if they were already in the system. 
# In this case, the code checks if created is True.
## boolean filed that gives you information if the user created in this case














