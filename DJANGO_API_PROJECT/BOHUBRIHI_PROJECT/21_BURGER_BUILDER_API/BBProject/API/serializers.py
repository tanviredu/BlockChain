from rest_framework.serializers import ModelSerializer
from API.models import UserProfile

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model  = UserProfile
        fields = ["id","email","password"]
        
        ## this code prevent the password field to show
        extra_kwargs = {
            "password":{"write_only":True,"style":{"input_type":"password"}}
        }


    ## overrite function
    ## this function is autometically called
    ## in the serializer
    ## we need to customize the data
    ## in the create method the validated_data is passed
    ## autometically and contverted to json
    ## so we can get the data from the dictionary
    def create(self,validated_data):
        user = UserProfile.objects.create_user(
            email    = validated_data["email"],
            password = validated_data["password"] 
        )
        return user
