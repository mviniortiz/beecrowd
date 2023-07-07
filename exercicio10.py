nome_vendedor = input()
salario_fixo = float(input())
total_vendas_efetuadas = float(input())
comissao = 0.15 * total_vendas_efetuadas
salario_final = comissao + salario_fixo

print('TOTAL = R$ {:.2f}'.format(salario_final))

