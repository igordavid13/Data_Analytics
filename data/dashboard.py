import streamlit as st
import pandas as pd


df = pd.read_csv('/home/uiot/Área de Trabalho/teste/fake_position.csv')
df = df.groupby(['account_code', 'account_suitability','class_name'])['position_value'].sum().reset_index().rename(columns={'position_value' : 'Soma'})
st.set_page_config(page_title="Dashboard Clients",layout='wide')
st.header(":bar_chart: Igão")
st.data_editor(
  df, 
  column_config={
    "account_code": st.column_config.NumberColumn(format="%d")
  }
)




client = st.sidebar.multiselect(
    key = 1,
    label = 'client',
    options = df['account_code'].unique()

)
