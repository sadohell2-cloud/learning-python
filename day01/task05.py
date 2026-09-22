# простой калькулятор
a = float(input())
b = float(input())
op = input()
res = {
    '+': a+b,
    '-':a-b,
    '*':a*b,
    '/':a/b if b != 0 else print('На ноль делить нельзя')
}
if b != 0 and op != '/' : print(res[op]);

