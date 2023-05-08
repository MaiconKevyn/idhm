import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("idhmT3.csv")


# Função para criar gráfico de barras com ranking dos estados por índice e ano
def criar_grafico_barras(df, indice, ano):
    dados_selecionados = df[df['ano'] == ano].groupby('sigla')[indice].mean()
    dados_selecionados.sort_values(ascending=True).plot(kind='barh', figsize=(12,8))
    #plt.xlabel(indice)
    plt.ylabel("sigla", fontdict={'fontsize': 7})
    plt.title(f"Ranking de estados brasileiros por {indice}")
    plt.legend(loc='lower right', fontsize='small')
    plt.show()

# Função para criar gráfico de linhas com IDHM e sub-índices de um estado ao longo dos anos
def criar_grafico_linhas(df, estado):
    dados_estado = df[df['sigla'] == estado].groupby(['ano']).mean()
    ax = dados_estado[['idhm_e', 'idhm_l', 'idhm_r', 'idhm']].plot(kind='line', figsize=(12, 8), color=['blue', 'orange', 'green', 'red'])
    plt.title(f"IDHM do estado {estado} ao longo dos anos")
    plt.legend(["idhm_e", "idhm_l", "idhm_r", "idhm"], loc='upper left',fontsize='small', labelspacing=0.5)
    ax.set_xticks([1991, 2000, 2010])
    ax.set_xticklabels([f"({estado}, 1991)", f"({estado}, 2000)\nsigla,ano", f"({estado}, 2010)"],fontdict={'fontsize': 7, 'ha': 'center'})
    ax.set_xlabel('')
    plt.show()

    
# Loop para escolher opções e criar gráficos
while True:
    print("Digite uma opção de gráfico:")
    print("1 - Ranking por estados.")
    print("2 - Informações de um estado ao longo dos anos.")
    opcao = int(input())

    if opcao == 1:
        print("Digite qual índice o gráfico utilizará:")
        print("1 - IDHM")
        print("2 - IDHM-L")
        print("3 - IDHM-R")
        print("4 - IDHM-E")
        opcao_indice = int(input())

        if opcao_indice not in [1, 2, 3, 4]:
            print("Opção inválida!")
            continue
            
        # Mapear opção de índice para o nome da coluna correspondente
        mapa_indice = {1: 'idhm', 2: 'idhm_l', 3: 'idhm_r', 4: 'idhm_e'}
        indice = mapa_indice[opcao_indice]

        print("Digite o ano a ser analisado [1991, 2000, 2010]:")
        ano = int(input())
        
        # Verificar se a opção de ano é válida
        if ano not in [1991, 2000, 2010]:
            print("Opção inválida!")
            continue

        criar_grafico_barras(df, indice, ano)

    elif opcao == 2:
        print("Informe o estado que deseja analisar:")
        estado = input().strip().upper()
        criar_grafico_linhas(df, estado)

    else:
        print("Opção inválida!")
        continue

    parar = input("Deseja fazer um novo gráfico? n/N para parar: ")
    if parar.lower() == 'n':
        break

