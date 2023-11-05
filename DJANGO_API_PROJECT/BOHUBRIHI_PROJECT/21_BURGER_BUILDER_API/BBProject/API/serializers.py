from rest_framework.serializers import ModelSerializer
from API.models import UserProfile,Order,Ingredient,CustomerDetail

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
    ## then you call the function the by default function
    ## wont work, new function work
    def create(self,validated_data):
        user = UserProfile.objects.create_user(
            email    = validated_data["email"],
            password = validated_data["password"] 
        )
        return user

class CustomerDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomerDetail
        #fields = "__all__"
        exclude = ["id"]
class IngredientSerializer(ModelSerializer):
    class Meta:
        model  = Ingredient
        ##fields = "__all__"
        exclude = ["id"]


class OrderSerializer(ModelSerializer):
    ingredients = IngredientSerializer()
    customer_detail    = CustomerDetailSerializer()
    
    class Meta:
        model = Order
        fields = "__all__"

    def create(self,validated_data):
        ingredient_data = validated_data.pop("ingredients")
        customer_detail_data = validated_data.pop("customer_detail")

        ## why the same serializer class inside the create method again
        ## remmber create is a class method
        ## this static class method is a helper function that
        ## take the a serializer class and the serialized data 
        ## to store that in the database
        ingri = IngredientSerializer.create(IngredientSerializer(),validated_data=ingredient_data)
        customer_d = CustomerDetailSerializer.create(CustomerDetailSerializer(),validated_data=customer_detail_data)
        order,is_created = Order.objects.update_or_create(
            ingredients = ingri,
            customer_detail = customer_d,
            price = validated_data.pop("price"),
            user  = validated_data.pop("user"),
            orderTime = validated_data.pop("orderTime"),


        )
        return order



