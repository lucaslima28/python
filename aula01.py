# name = "Lucas Lima"

# print(name[0:10])
# print(len (name))
# print(name.find('i'))
# print(name.replace('Lima', 'Alves'))
# #print(name.upper())

# course = 'Estação Hack do Facebook'

# print('Hack' in course)

# #CONDIÇÃO
# summer = False
# winter = False

# if summer:
#     print('use oculos de sol')
#     print('use filtro')
#     print('va a praia')
# elif winter:
#     print('nao esquece o casaco filho')
# else:
#     print('nao use oculos, durma.')     
# green_bank = True
# criminal = False
# money = True


# if green_bank and  criminal and not money:
#     print('ih deu ruim')

#while

# i= 0 

# while i < 5:
#     print(i)
#     i = i+1
# print('acabou')

# secret_number = 5
# i = 0


# while i < 3:
#     chute = int(input('qual o numero secreto? '))
#     i = i + 1
#     if chute == secret_number:
#         print('voce acertou')
#         break
#     else:
#         print('errou')




# posso comprar um celular com 2000 reias?
# iphone XR Master Plus 856gb e 10 cilindradas = R$8000
# iphone XR Diamond 856gb = R$5000
# positivo azul com tela cristal e jogo da cobrinha = 450
# se não puder, o que eu faço?

# names = ['Lucas', 'Raianey', 'Ju', 'Ana']
# print(names[0:4])
# names[1] = 'Hayane'
# print(names)

# numbers = [1, 4, 6, 6, 9, 345, 101]
# numbers.append(20)
# numbers.append(21)
# numbers.insert(0, 99)
# numbers.remove(345)
# #numbers.clear() #cuidado com este método, ele apaga tudo
# numbers.pop()


# print(numbers.reverse())

# lista2 = numbers.copy()
# numbers.append(222)
# print(lista2)
# print(numbers)

# numbers = [1, 4, 6, 6, 9, 345, 23, 101]
# nova_lista = []

# for number in numbers:
#     if number not in nova_lista:
#         nova_lista.append(number)
# print(nova_lista)

# lista2 = numbers.copy()
# numbers.remove(6)
# print(lista2)
# print(numbers)

#TUPLA OU TUPLE
# cursos = ('Matematica', 'Ingles', 'Biologia')

#DICIONARIOS

# pessoa = {
#     'name' : 'Hayane' , 
#     'age': 82,
#     'address': 'area de preservacao florestal',
#     'skills': ['assembly', 'C', 'cobol', 'pascal' , 'pearl', 'birlll']
# }

# print(pessoa['name'])
# print(pessoa['address'])



listas = [1, 2, 3, 8, 10, 45, 12]
max = listas[0]

for lista in listas :
    if lista > max:
        print(max)
        max = lista
print(max)    

# media = 6
# max_faltas = 2
# media_aluno = int(input('qual o numero secreto ? '))
#faltas_aluno = int(input('quantas faltas voce tem ? '))
# if:
#     media == media_aluno:
#     print('voce foi aprovado')
# else:
#     print('voce foi reprovado')

