# دوال النصوص — الجزء 3

## Video Number
#13

## What I Learned
-:split وظيفة
[]تقوم بتحويل العناصر من طباعتها في سطر واحدإلى طباعتها في قائمه بين
-rsplitوظيفة 

## Important Notes
--:تضع هكذا split
print(اسم المتغير.split())
عندما يكون القوس فارغ يعتبر ان المسافه بين العناصر هي الفواصل ويكون كل عنصر منفرد
عندما نضع _ بدلا من المسافه بين العناصر فإنه لا يعتبر ان كل عنصر منصل ويقوم بطباعة السطر كامل متصل 
 :لطباعة كل عنصر منفصل في حالة وجود _ بينهما نكتب
 print(اسم المتغير.split("_"))
 -:لطباعة عدد من العناصر كل واحد لوحده والباقي يتم تجميعه في واحده فقط
 print(اسم المتغير.split("_",عدد العناصر المراد فصلها)) للبداية من اليسار
 print(اسم المتغير.rsplit("_",عدد العناصر المراد فصلها)) للبداية من اليمين

## Code Explanation
-program_lan = "html css javascript php python"
print(program_lan)
program_lan = "html css javascript php python"
print(program_lan.split())

program_lan2 = "html_css_javascript_php_python"
print(program_lan2.split())

program_lan2 = "html_css_javascript_php_python"
print(program_lan2.split("_"))
print(program_lan2.split("_",3))
print(program_lan2.split("_",2))
print(program_lan2.rsplit("_",2))

## Challenges I Solved
-لا يوجد

## Questions I Still Have
-لا يوجد