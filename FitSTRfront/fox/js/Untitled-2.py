def carregaMat(nomeArquivo):
    matriz = []
    with open(nomeArquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            valores = linha.strip().split(",")
            valores_float = [float(valor) for valor in valores]
            matriz.append(valores_float)
    return matriz

def calcular_quantidade_por_armazem(matriz_estoque):
    quantidade_por_armazem = []
    for coluna in range(len(matriz_estoque[0])):  
        quantidade = sum([linha[coluna] for linha in matriz_estoque])
        quantidade_por_armazem.append(quantidade)
    return quantidade_por_armazem

def calcular_quantidade_total(matriz_estoque):
    quantidade_total = 0
    for linha in matriz_estoque:
        quantidade_total += sum(linha)
    return quantidade_total

def calcular_preco_maximo_por_armazem(matriz_estoque, vetor_precos):
    precos_maximos = []
    for coluna in range(len(matriz_estoque[0])):
        estoques_armazem = [linha[coluna] for linha in matriz_estoque]
        indice_maximo = estoques_armazem.index(max(estoques_armazem))
        preco_maximo = vetor_precos[indice_maximo]
        precos_maximos.append(preco_maximo)
    return precos_maximos

def calcular_menor_estoque(matriz_estoque):
    menor_estoque = min([min(linha) for linha in matriz_estoque])
    return menor_estoque

def calcular_custo_por_armazem(vetor_precos, quantidade_por_armazem):
    custo_por_armazem = [preco * quantidade for preco, quantidade in zip(vetor_precos, quantidade_por_armazem)]
    return custo_por_armazem


arquivo_precos = 'precos.txt'
with open(arquivo_precos, 'r') as arquivo:
    precos = [float(linha.strip()) for linha in arquivo.readlines()]


arquivo_estoque = 'estoque.txt'
estoque = carregaMat(arquivo_estoque)


quantidade_por_armazem = calcular_quantidade_por_armazem(estoque)
quantidade_total = calcular_quantidade_total(estoque)
precos_maximos = calcular_preco_maximo_por_armazem(estoque, precos)
menor_estoque = calcular_menor_estoque(estoque)
custo_por_armazem = calcular_custo_por_armazem(precos, quantidade_por_armazem)

print("Quantidade de produtos estocados em cada armazém:")
for i, quantidade in enumerate(quantidade_por_armazem):
    print(f"Armazém {i+1}: {quantidade}")

print("Quantidade de cada produto estocado em todos os armazéns juntos:")
print(quantidade_total)

print("Preço do produto com maior estoque em um único armazém:")
for i, preco in enumerate(precos_maximos):
    print(f"Armazém {i+1}: R${preco:.2f}")

print("Menor estoque armazenado:")
print(menor_estoque)

print("Custo de cada armazém:")
for i, custo in enumerate(custo_por_armazem):
    print(f"Armazém {i+1}: R${custo:.2f}")
