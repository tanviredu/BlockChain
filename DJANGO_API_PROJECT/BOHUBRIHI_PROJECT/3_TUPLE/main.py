## tuple and list are called sequence data type
## tuple is immutable
## once you declare you cant change
tp1 = ("Tanvir",40,"Engineer","Agrabad","CDA 23")
print(tp1)
tp2 = ("Ornob","Rahman",("hasnat","Rabi"),["sugar","salt"])
print(tp2)

## you cant change the tuple member 
## but you can change the list member inside a tuple
## so you cant change the whole list
## but you can change the list member
print(tp2[3][1])

## make a single value  tuple
## just add a comma after the value
tp3 = "Tanvir",
print(tp3)
print(type(tp3))