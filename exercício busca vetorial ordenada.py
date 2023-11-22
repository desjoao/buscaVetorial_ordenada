def buscaVet(vetor, tam, valor):
    k = 0
    vet = [-1]*tam
    for i in range (tam):
        if vetor[i] <= valor:
            if vetor[i] == valor:
                vet[k] = i
                k +=1
        else:
            break
    return vet

def leitura(tam):
    vetor = [0]*tam
    for i in range(tam):
        vetor[i] = int(input(f'Informe um {i +1}º valor positivo e ordenado do menor para o maior: '))
        while vetor[i] <0:
            vetor[i] = int(input(f'Informe um {i +1}º valor POSITIVO e ordenado do menor para o maior: '))
        while vetor[i]<vetor[i-1]:
            vetor[i] = int(input(f'Informe um {i +1}º valor POSITIVO E ORDENADO DO MENOR PARA O MAIOR: '))
    return vetor

info = leitura(10)
val = int(input(f'Informe o valor que gostaria de buscar: '))
busca = buscaVet(info, len(info), val)

count = 0
for i in range (10):
    if busca[i] != -1:
        count+=1

res = [0]*count
for i in range (count):
    res[i] = busca[i]

if count == 0:
    print(f'Não foi encontrado o valor buscado.')
elif count == 1:
    print(f'O valor buscado está localizado na posição {res} do vetor {info}.')
else:
    print(f'O valor buscado está localizado nas posições {res} do vetor {info}.')

