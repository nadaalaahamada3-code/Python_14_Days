# دوال القوائم (List Methods)

## Video Number
#22

## What I Learned
- اضافة عنصر للقائمه
_ دمج قائمتين داخل قائمه واحده
_ترتيب القيم العشوائية داخل القائمه
_حذف عنصر داخل القائمه

## Important Notes
-:  اضافة عنصر في نهاية القائمه
اسم المتغير.append(العنصر المراد اضافته)

-:  اضافة عنصر في اي موقع داخل القائمه
اسم المتغير.insert( العنصر المراد اضافته,رقم الموقع في القائمه)

_: دمج قائمتين داخل قائمه واحده
اسم اول قائمه.extend(اسم القائمه الثانيه)
print(اسم اول قائمه)

_: ترتيب القيم العشوائية داخل القائمه تصاعدي
اسم المتغير.sort()
        او
 اسم المتغير.sort(reverse=False)
print(اسم المتغير)

_: ترتيب القيم العشوائية داخل القائمه تنازلي
اسم المتغير.sort(reverse=True)
print(اسم المتغير)

_: حذف عنصر واحد داخل القائمه
اسم المتغير.remove(العنصر المراد حذفه)
print(اسم المتغير)

_: حذف كل العناصر داخل القائمه
اسم المتغير.clear()
print(اسم المتغير)


## Code Explanation
-x = [1,2,3]
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


## Challenges I Solved
- لا يوجد

## Questions I Still Have
- لا يوجد
