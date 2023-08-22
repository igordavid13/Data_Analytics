import streamlit as st
import pandas as pd
import plotly.express as px
import math
import sqlalchemy as sa

#Conexão com o banco de dados
engine = sa.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
dbConnection    = engine.connect()

@st.cache_data
def load_data() -> pd.DataFrame:
  df = pd.read_sql("select * from \"fake_position\"", dbConnection)
  al = pd.read_excel('./fake_allocation_policies.xlsx')
  #Limpeza dos dados
  #Elimina colunas onde o account_suitability é inexistente
  df.dropna(subset = 'account_suitability', inplace = True)
  #Elimina colunas onde a classe do investimento é inexistente
  df.dropna(subset = 'class_name', inplace = True)
  #Substitui os valores ausentes de asset_cnpj por 0
  df['asset_cnpj'].fillna(value = 'Não especificado', inplace = True)
  df['asset_cnpj'] = df['asset_cnpj'].astype(str)
  
  

  return df, al

def set_sidebar(
    dataframe: pd.DataFrame = None ) -> dict:
    df = dataframe
    
    client =st.sidebar.selectbox(
        key=0,
        label="account_code",
        options=df["account_code"].unique(),
        help="Select a client"
    )

    return client

def build_visualizations(dataframe: pd.DataFrame):
    st.header(":bar_chart: Sales Dashboard")
    st.markdown("#")
    account_code = dataframe['account_code'].iloc[0]
    account_suitability = dataframe['account_suitability'].iloc[0]
    df = dataframe.groupby(['class_name'])['position_value'].sum().reset_index().rename(columns={'position_value' : 'Total'})
    df1=df.copy()
    total = df['Total'].sum()
    df['Total'] = df['Total'].div(total)
    adherence= adherence_calculation(df,account_suitability)
    
   


    fig_sales_by_deal_size = px.pie(
        df,
        title="<b>Investiments Pie</b>",
        color_discrete_map = ["#54A28C"],
        names='class_name',
        values="Total",
        width=500,
    )
    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        st.markdown('> **Account_Code:**')
        st.subheader(f":orange[{account_code}]")

    with middle_column:
        st.markdown("> **Account_Suitability:**")
        st.subheader(f":orange[{account_suitability}]")
    with right_column:
        st.markdown("> **Adherence:**")
        st.subheader(f":orange[{adherence:3f}]")    

    st.markdown("---")
    
    chart_column2_left,chart_column2_right = st.columns(2)
    chart_column2_left.dataframe(df1, use_container_width=True, height=400)
    chart_column2_right.plotly_chart(fig_sales_by_deal_size, use_container_width=True, height=400)
    st.dataframe((dataframe[['asset_cnpj','asset_name','class_name','position_value']]).reset_index())
def hide_syle():
    style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


#Criação de dicionário com as alocações baseada no perfil do cliente
def adherence_calculation(individual_df,account_suitability):
    distance = 0
    class_allocation = pd.Series(al.classe.values, index=al[account_suitability].values).to_dict() # dicionário com as alocações do respectivo cliente
    class_allocation = {v: k for k, v in class_allocation.items()} # inverte as chaves e os valores do dicionário
    client = dict(zip(individual_df['class_name'], individual_df['Total'])) # cria um dicionário com as classes e porcentagem das classes   
    for asset_class, allocation_percentage in class_allocation.items(): # itera sobre o dicionário de alocações do cliente
        client_allocation = client.get(asset_class, 0)
        distance += (allocation_percentage - client_allocation) ** 2

    euclidean_distance = math.sqrt(distance)
    return euclidean_distance


def main(dataframe):
    client = set_sidebar(dataframe=dataframe)
    filtered = dataframe[dataframe['account_code'] == client]
    build_visualizations(dataframe = filtered)
    hide_syle()

if __name__ == "__main__":
    st.set_page_config(
        page_title="Sales Dashboard", 
        page_icon=":bar_chart:",
        initial_sidebar_state="collapsed",
        layout="wide"
    )

    dataframe,al = load_data()
    main(dataframe=dataframe)


