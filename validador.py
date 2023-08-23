__version__ = "0.0.1"
__author__ = "GustavoOfSmach"
__license__ = "Unlicense"

print('Já estamos quase finalizando sua compra! Complete os dados abaixo:')
salario = float(input('Informe seu salario:'))
idade = int(input('Informe sua idade: '))

if salario >= 1000 and idade >= 18:

  print('Compra aprovada')
  print('Parabens sua compra foi realizada com sucesso')

else:
  print('Compra negada')
  print('Pedimos desculpas mais não foi possivel aprovar sua compra')
