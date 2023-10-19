from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework      import status

class ContactTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data   = {
            "name":"Tanvir Rahman",
            "message":"Test Message",
            "email": "t@gmail.com"
        } 
        self.url = "/contact/"

    def test_create_contact(self):
        data = self.data
        response = self.client.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_create_contact_without_name(self):
        data = self.data 
        data.pop("name")
        response = self.client.post(self.url,self.data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
