## key value pair
## python dictionary
my_dict = {
    "Fname":"Tanvir",
    "Lname": "Rahman",
    "Age" : "29",
    "School": "CUET",
    "City": "Chittagong"
}
print(my_dict)
## adding new value
## Remember dictionary is mutable
## you can change things
my_dict["POST_CODE"] = "4204"
my_dict["LOCALTION"] = "AGRABAD"
print(my_dict)
## delete a key value from the dictionary
del(my_dict["POST_CODE"])
print(my_dict)
a = dict(Name="Tanvir",address="Agrabad",city="Chittagong")
print(a)
b = dict(zip(['Name','address','city'],['Tanvir','Agrabad','Chittagong']))
print(b)
b.pop("Name") ## inside the pop instead of index ## you have t provide value
print(b)
x = list(b) ## it will return the keys of the dict
print(x)