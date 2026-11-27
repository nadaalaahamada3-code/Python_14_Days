x = [1,2,3]
x.append(4)
print(x)

x = [1,2,3]
x.insert(1,"ahmed")
print(x)

x = [1,2,3]
z = [4,5,6]
x.extend(z)
print(x)

x = [1,2,3]
z = ["ahmed","ali","abdelrahman"]
x.extend(z)
print(x)

x = [1,10,3,9,5,0]
x.sort()
print(x)

z = ["nada","ahmed","zyad"]
z.sort()
print(z)

x = [1,10,3,9,5,0]
x.sort(reverse=False)
print(x)

x = [1,10,3,9,5,0]
x.sort(reverse=True)
print(x)

z = ["nada","ahmed","zyad"]
z.sort(reverse=False)
print(z)

z = ["nada","ahmed","zyad"]
z.sort(reverse=True)
print(z)

z = ["nada","ahmed","zyad"]
z.remove("ahmed")
print(z)

z = ["nada","ahmed","zyad"]
z.clear()
print(z)
