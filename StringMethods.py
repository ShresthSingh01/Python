#Capitalize 
text="hello  and welcome to my space"
print(text.capitalize())
#casefold
txt="Hello And Welcome To My Space"
print(txt.casefold())
#center
txt2="Python"
print(txt2.center(5,'$'))
#Count
txt3="Surprise surprise mf the king is back"
x=txt3.count("surprise",0,29)
print(x)
#Join method to join tuple elements and all items in dictionary into a string
myTuple=("John","Peter","Vicky")
x="@".join(myTuple)
print(x)