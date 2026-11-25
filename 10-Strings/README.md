# النصوص (Strings)

## Video Number
#10

## What I Learned
-كتابة النصوص
:backslash استخدامات
دمج سطرين مع بعض + طباعتهما في سطر واحد1
2طباعة كود واحد على سطرين
3في حالة وجود علامتين تنصيص داخل بعض يتم فصلهما بها
"abdelrahman\"gamal\""
\بديل"""
## Important Notes
-'...'في هذا النوع لا يفرق اذا كان النص مكتوب بين "..."أو 
\عند كتابه كود طويل من سطرين في نهاية السطر الاول نضع
لا يجوز وضع علامتين تنصيص داخل علامتين تنصيص """"
لا يجوز وضع علامة تنصيص داخل علامة تنصيص ''''
يجوز وضع علامة تنصيص داخل علامتين تنصيص"''"
يجوز وضع علامتين تنصيص داخل علامة تنصيص'""'

## Code Explanation
-x = "abdelrahman\
aaaaaaaaaaaa"
z = 'abdelrahman'
print(x)
print(z)

x = "abdelrahma\ngamal"
z = 'abdelrahman'
print(x)
print(z)

x = "abdelrahman\"gamal\""
z = '\'abd\'elrahman'
print(x)
print(z)
x = "abdelrahman'aaa'"
print(x)

x = 'abdelrahman"aaa"'
print(x)

z = """
a
a

a
a
"""
print(z)


z = """
"a"
'a'

a
a
"""
print(z)

## Challenges I Solved
-لا يوجد

## Questions I Still Have
-لا يوجد
