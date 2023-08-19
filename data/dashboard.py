import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_data() -> pd.DataFrame:
  df = pd.read_csv('./fake_position.csv')
  #Limpeza dos dados
  #Elimina colunas onde o account_suitability é inexistente
  df.dropna(subset = 'account_suitability', inplace = True)
  #Elimina colunas onde a classe do investimento é inexistente
  df.dropna(subset = 'class_name', inplace = True)
  #Substitui os valores ausentes de asset_cnpj por 0
  df['asset_cnpj'].fillna(value = 0, inplace = True)
  

  return df

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

def build_visualizations(dataframe: pd.DataFrame, client):
    st.header(":bar_chart: Sales Dashboard")
    st.markdown("#")
    df = dataframe.groupby(['account_code', 'account_suitability','class_name'])['position_value'].sum().reset_index().rename(columns={'position_value' : 'Soma'})
    total = df['Soma'].sum()
    df['Soma'] = df['Soma'].div(total)
    fig_sales_by_deal_size = px.pie(
        df,
        title="<b>Porcentagem de Investimentos</b>",
        names='class_name',
        values="Soma",
        width=450,
    )
    chart_column2_left,chart_column2_right = st.columns(2)
    chart_column2_left.dataframe(df.style.format({'Soma': '{:.5}'.format}))
    chart_column2_right.plotly_chart(fig_sales_by_deal_size)
def hide_syle():
    style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def main(dataframe):
    
    client = set_sidebar(dataframe=dataframe)
    print(client)
    filtered = dataframe[dataframe['account_code'] == client]
    build_visualizations(dataframe = filtered, client = client)
    hide_syle()



if __name__ == "__main__":
    st.set_page_config(
        page_title="Sales Dashboard", 
        page_icon=":bar_chart:",
        initial_sidebar_state="collapsed",
        layout="wide"
    )

    dataframe = load_data()
    main(dataframe=dataframe)

