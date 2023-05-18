# Testando pesquisa binária livro Entendendo Algoritmos

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1  # Verificando o tamanho/comprimento (lenght) da lista, ou seja o número de elementos contidos nela, que possui 5 elementos mas precisa de subtrair 1 para ficar com 4

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

# Pode-se armazenar uma sequência de elementos em uma linha de buckets consecutivos que se chama Array
# Os buckets são numerados a partir do 0: o primeiro bucket está na posição #0; o segundo em #1, o terceiro em #2...
print(pesquisa_binaria(minha_lista, 3))  # => 1
print(pesquisa_binaria(minha_lista, -1))  # => None
# Ao alterar o valor de 3 na pesquisa da minha lista, o resultado será diferente pois ele irá o buscar o número em seu respectivo array
# Ou seja, como a lista se inicia em 0, o próximo endereço tem índice 1, o próximo endereço tem índice 2 etc...
