"""
A variável **i** serve como o contador sobre RANGE de [0,10), 
inclusive do limite inferior, mas exclusive do limite superior.

O limite inferior de 0 NÃO precisa ser especificado;
ele é implementado por padrão, a menos que outro limite inferior seja especificado.

Também, por padrão, se NÃO existir um terceiro parâmetro para range(), 
então **i** aumenta em 1. 
"""
#for i in range(10):
#  print(i)

"""
Estes exemplos especificam um limite inferior que difere do valor padrão de 0.

A ordem do parâmetro é SEMPRE:
 1. Posição inicial, inclusive
 2. Posição de parada, exclusive
 3. Valor incremental


Neste exemplo, x começa com o valor igual a 2 e para em 9 inclusive, ou seja, 10 exclusive, 
com x acréscimos de 1 para cada iteração.
"""

#for i in range(2, 10, 2):
#  print(i)

"""
Loop 'for-Each' sobre cada caractere em uma string.

Neste exemplo, a variável 'i' representa cada elemento/caractere de 'hello'.
"""

#for i in "hello!":
#  print(i)

"""
Poderíamos também iterar sobre a string por indexação.

Considere o seguinte exemplo de iteração sobre a string por index, 
começando no índex 0 e terminando no último elemento, com os incrementos do contador em 2, 
portanto, imprimindo APENAS todos os outros elementos da string. 
"""

string = "hello world!"
for i in range(0, len(string), 2):
  print(str(i) + "th letter is "+ string[i])