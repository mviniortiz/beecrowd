#Este exercício tem como objetivo calcular a área de diversos objetos geométricos, sendo eles círculo, triângulo, trapézio, quadrado, retângulo.


a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

r = (a * c) / 2
r2 = 3.14159 * c ** 2
r3 = ((a + b)) * c / 2
r4 = b ** 2
r5 = a * b

print('TRIANGULO: %.3f' % r)
print('CIRCULO: %.3f' % r2)
print('TRAPEZIO: %.3f' % r3)
print('QUADRADO: %.3f' % r4)
print('RETANGULO: %.3f' % r5)
