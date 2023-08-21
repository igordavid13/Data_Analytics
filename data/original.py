import pandas as pd
import numpy as np
import math

df = pd.read_csv('/home/igor/Desafio-VLGI/Desafio-VLGI/data/fake_position.csv')
al = pd.read_excel('/home/igor/Desafio-VLGI/Desafio-VLGI/data/fake_allocation_policies.xlsx')

#Limpeza dos dados
#Elimina colunas onde o account_suitability é inexistente
df.dropna(subset = 'account_suitability', inplace = True)
#Elimina colunas onde a classe do investimento é inexistente
df.dropna(subset = 'class_name', inplace = True)
#Substitui os valores ausentes de asset_cnpj por 0
df['asset_cnpj'].fillna(value = 0, inplace = True)

df = df.groupby(['account_code', 'account_suitability','class_name'])['position_value'].sum().reset_index().sort_values(['account_code', 'class_name']).rename(columns={'position_value' : 'Soma'})
clients = df['account_code'].unique()
aderencia= dict()

#Retorna o perfil do cliente de acordo com a tabela de alocações
def perfil_client(individual_df):
    perfil = individual_df['account_suitability'].iloc[0] # perfil do cliente a partir da tabela de alocações
    class_allocation = pd.Series(al.classe.values, index=al[perfil].values).to_dict() # dicionário com as alocações do respectivo cliente
    class_allocation = {v: k for k, v in class_allocation.items()} # inverte as chaves e os valores do dicionário
    return class_allocation

def aderencia_client(client, class_allocation, account_code):
    distance = 0
    for asset_class, allocation_percentage in class_allocation.items():
        client_allocation = client.get(asset_class, 0)
        distance += (allocation_percentage - client_allocation) ** 2

    euclidean_distance = math.sqrt(distance)
    aderencia.update({f"{account_code}" : f"{euclidean_distance}"})
    
for client in clients:
    individual_df = df[df['account_code'] == client]
    class_allocation = perfil_client(individual_df)

    total = individual_df['Soma'].sum()
    individual_df['Soma'] = individual_df['Soma']/total # atualiza a Series Soma com o percentual de cada classe
    client = dict(zip(individual_df['class_name'], individual_df['Soma'])) # cria um dicionário com as classes e porcentagem das classes
    aderencia_client(client, class_allocation, individual_df['account_code'].iloc[0])

print(aderencia)