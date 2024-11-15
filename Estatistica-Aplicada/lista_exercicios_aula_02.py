# Importando as bibliotecas necessárias
import numpy as np
from scipy.stats import norm
import pandas as pd

# Organizando o código em funções

def probabilidade_inferior(taxa_conversao, media, desvio_padrao):
    probabilidade = norm.cdf(taxa_conversao, loc=media, scale=desvio_padrao)
    return probabilidade

def probabilidade_intervalo(taxa_conversao_inferior, taxa_conversao_superior, media, desvio_padrao):
    probabilidade = norm.cdf(taxa_conversao_superior, loc=media, scale=desvio_padrao) - norm.cdf(taxa_conversao_inferior, loc=media, scale=desvio_padrao)
    return probabilidade


'''Exercício 1: Taxa de conversão em campanhas de e-mail marketing
   Uma empresa de marketing digital realiza campanhas de e-mail marketing para diferentes setores. Após a análise de campanhas anteriores, foi constatado que a taxa de conversão de cliques em compras possui uma distribuição normal com média de 12% e desvio-padrão de 4%.
    A empresa deseja calcular:
        1.	A probabilidade de uma campanha apresentar uma taxa de conversão inferior a 10%.
        2.	A probabilidade de a taxa de conversão estar entre 8% e 15%.
'''

# Definindo a média e o desvio padrão
media = 12
desvio_padrao = 4

# Calculando a probabilidade de uma campanha apresentar uma taxa de conversão inferior a 10%
probabilidade1_1 = probabilidade_inferior(10, media, desvio_padrao)

# Calculando a probabilidade de uma campanha apresentar uma taxa de conversão entre 8% e 15%
probabilidade1_2 = probabilidade_intervalo(8, 15, media, desvio_padrao)


'''Exercício 2: Tempo de resposta em plataformas de atendimento digital
   Uma empresa de tecnologia focada em transformação digital oferece um sistema automatizado de atendimento para clientes via chatbot. Dados históricos indicam que o tempo de resposta dos chatbots segue uma distribuição normal com média de 3,2 segundos e desvio-padrão de 0,8 segundos.
    A empresa busca identificar:
        1.	A probabilidade de o tempo de resposta ser inferior a 2 segundos.
        2.	A probabilidade de o tempo de resposta estar entre 2,5 e 4 segundos.
'''

# Definindo a média e o desvio padrão
media = 3.2
desvio_padrao = 0.8

# Calculando a probabilidade de o tempo de resposta ser inferior a 2 segundos
probabilidade2_1 = probabilidade_inferior(2, media, desvio_padrao)

# Calculando a probabilidade de o tempo de resposta estar entre 2,5 e 4 segundos
probabilidade2_2 = probabilidade_intervalo(2.5, 4, media, desvio_padrao)


'''Exercício 3: Receita diária de uma plataforma de e-commerce
   Uma empresa de e-commerce que utiliza soluções avançadas de transformação digital verificou que a receita diária gerada em seu site segue uma distribuição normal com média de R$ 50.000,00 e desvio-padrão de R$ 10.000,00.
    A empresa deseja:
        1.	Determinar a probabilidade de a receita diária ser inferior a R$ 40.000,00.
        2.	Determinar a probabilidade de a receita diária estar entre R$ 45.000,00 e R$ 60.000,00.
'''

# Definindo a média e o desvio padrão
media = 50000
desvio_padrao = 10000

# Calculando a probabilidade de a receita diária ser inferior a R$ 40.000,00
probabilidade3_1 = probabilidade_inferior(40000, media, desvio_padrao)

# Calculando a probabilidade de a receita diária estar entre R$ 45.000,00 e R$ 60.000,00
probabilidade3_2 = probabilidade_intervalo(45000, 60000, media, desvio_padrao)

# Imprimir os resultados em formato de tabela

# Definindo um dicionário com os resultados
resultados = {
    'Exercício': ['1.1', '1.2', '2.1', '2.2', '3.1', '3.2'],
    'Descrição': ['Probabilidade de taxa de conversão inferior a 10%',
                  'Probabilidade de taxa de conversão entre 8% e 15%',
                  'Probablidade de tempo de resposta inferior a 2 segundos',
                  'Probabilidade de tempo de resposta entre 2,5 e 4 segundos',
                  'Probabilidade de receita diária inferior a R$ 40.000,00',
                  'Probabilidade de receita diária entre R$ 45.000,00 e R$ 60.000,00'
    ],
    'Probabilidade': [
        probabilidade1_1, probabilidade1_2, probabilidade2_1, probabilidade2_2, probabilidade3_1, probabilidade3_2
    ]
}

# Criando um DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)

# Formatando as probabilidades como percentuais
df_resultados['Probabilidade'] = df_resultados['Probabilidade'].apply(lambda x: f'{x * 100:.2f}%')

print(df_resultados)

