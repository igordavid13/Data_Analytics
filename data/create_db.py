import sqlalchemy as sa
import pandas as pd


#Ingestão de dados com usuário e senha do banco de dados sendo postgres porta 5432

engine = sa.create_engine('postgresql://postgres:postgres@localhost:5432/postgres')


df = pd.read_csv('./fake_position.csv')
df.to_sql('fake_position', engine)
