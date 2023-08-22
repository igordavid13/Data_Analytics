## Execução

INGESTÃO DE DADOS POSTGRES
* Criar um banco de dados local com usuário e senha sendo postgres e porta 5432
* Executar arquivo create_db.py para ingestão dos dados

DASHBOARD
* Para executar o dashboard é necessário rodar o seguinte comando:

```{python}
streamlit run dashboard.py
```  
## Desafios

DESAFIOS ENCONTRADOS
* Procurei realizar o cálculo da aderência utilizando querys sql como é possível visualizar no arquivo query.sql porém para cada account_code não consegui incluir na conta as classes ausentes, portanto o resultado não se encontrava correto. Adaptei a solução usando pandas para os cálculos
