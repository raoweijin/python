a =3 
def test():
    global a
    a= 5
    print("local a ",a)
test()
print("global a ",a)
print("end")