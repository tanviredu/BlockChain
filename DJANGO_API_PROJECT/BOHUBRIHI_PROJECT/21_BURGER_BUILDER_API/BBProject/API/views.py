from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from API.models import UserProfile,Order
from API.serializers import UserProfileSerializer,OrderSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


##  REMEMBER THE MOMENT YOU WILL OVERWRITE THE 
## BUILT IN METHOD INSIDE A CLASS
## THE CLASS WILL USE THE NEW METHOD NOT THE OLD ONE
#  
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    ##queryset = Order.objects.all()
    permission_classes=[
        IsAuthenticated,
    ]

    def get_queryset(self):
        queryset = Order.objects.all()
        ## FROM THE URL PARAMETER IT WILL TAKE
        ## THE ID AND ID THERE IS NO ID IT WILL
        ## RETURN THE NONE

        ## GETTING THE USERNAME FROM THE JWT TOKEN
        print("[*] User Email : {}".format(self.request.user)) ## user is now the email
        user_id = self.request.query_params.get("user_id",None)
        if user_id is not None:
            ## The double underscore __ in user__id is used in Django's query
            ## lookups to navigate relationships between models and perform 
            ## lookups on related fields. In this case, it's used to filter 
            ## orders based on the user_id associated with each order's user.
            ## it will autometically search from the user field in the Ordertale
            ## and then find the id of that user
            ## it is a look up on related field and navigated through the relation
            ## and the query will be http://localhost:8000/api/order/?user_id=1
            queryset = queryset.filter(user__id = user_id)
        return queryset
