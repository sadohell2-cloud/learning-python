# генератор пароля
s1 = input()
s2 = input()
s3 = input()
sss = [s1, s2, s3]
per_buc= []
num = []
#print( sss[0:1], sss[1:1], sss[2:1], len(sss[0]), len(sss[1]), len(sss[2]))
# загуглил как прекратить выполнение цикла
for i in sss:
    lol = i[0]
    per_buc.append(lol)
for u in range(len(sss)):
    uwu = len(sss[u])
    num.append(uwu)

# раз по услвоиям только 3 слова, то можно сделать приметивную неудобную конструкцию
password = f'{per_buc[0]}-{per_buc[1]}-{per_buc[2]}-{num[0]}-{num[1]}-{num[2]}'

#password = password[1], password[0]
print(password)

r'''

sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$  source /c/dev/learning-python/.venv/Scripts/activate
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
(((None, 0), 0), 0)
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
(((None, 'д'), 'с'), 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
((('', 'д'), 'с'), 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 8, in <module>
    hey = hey, i[k]
          ^^^
NameError: name 'hey' is not defined. Did you mean: 'hex'?
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
('л', 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 9, in <module>
    hey = hey, i[k]
          ^^^
NameError: name 'hey' is not defined. Did you mean: 'hex'?
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
(((None, 'д'), 'с'), 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
л л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 10, in <module>
    password = hey, pas
                    ^^^
NameError: name 'pas' is not defined
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 8, in <module>
    pas = i[k]
            ^
NameError: name 'k' is not defined
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
дом
строить
любовь
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
д
с
л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
д
с
л
л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
д
с
л
('л', 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
('', 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
((('', 'д'), 'с'), 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
(((None, 'д'), 'с'), 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
('л', (('None', 'д'), 'с'))
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
None д с л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
 д с л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
None д с л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
None-д--с--л-
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
None-д-с-л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
-д-с-л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
////д//с//л/
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
////д/с/л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
///None/д/с/л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
None/д/с/л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 10, in <module>
    password = f'{password}/{i[0]}'
                  ^^^^^^^^
NameError: name 'password' is not defined
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 14, in <module>
    hey = ps(i[0])
          ^^^^^^^^
  File "c:\dev\learning-python\day01\task03.py", line 7, in ps
    ps(password)
  File "c:\dev\learning-python\day01\task03.py", line 7, in ps
    ps(password)
  File "c:\dev\learning-python\day01\task03.py", line 7, in ps
    ps(password)
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
('л', 'л')
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 14, in <module>
    hey = ps(i[0])
          ^^^^^^^^
  File "c:\dev\learning-python\day01\task03.py", line 7, in ps
    password = ps(lo), lo
               ^^^^^^
  File "c:\dev\learning-python\day01\task03.py", line 7, in ps
    password = ps(lo), lo
               ^^^^^^
  File "c:\dev\learning-python\day01\task03.py", line 7, in ps
    password = ps(lo), lo
               ^^^^^^
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 10, in <module>
    password = f'{password}/{i[0]}'
                  ^^^^^^^^
NameError: name 'password' is not defined
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
lol/д/с/л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
-д-с-л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 10, in <module>
    password = f'{password}-{i[0]}'
                  ^^^^^^^^
NameError: name 'password' is not defined
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
1-л
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
['д', 'с', 'л']
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
Traceback (most recent call last):
  File "c:\dev\learning-python\day01\task03.py", line 23, in <module>
    parol()
  File "c:\dev\learning-python\day01\task03.py", line 2, in parol
    s1 = input()
         ^^^^^^^
KeyboardInterrupt

(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:\dev\learning-python\.venv\Scripts\python.exe c:/dev/learning-python/day01/task03.py
bash: c:devlearning-python.venvScriptspython.exe: command not found
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
дом
кухня
любовь
д-к-л-0-1-2
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$ c:/dev/learning-python/.venv/Scripts/python.exe c:/dev/learning-python/day01/task03.py
ljv
re[yz
k.,jdm
l-r-k-3-5-6
(.venv)
sadoh@DESKTOP-N0JQNO2 MINGW64 /c/dev
$

'''
