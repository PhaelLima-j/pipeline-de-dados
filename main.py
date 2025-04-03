#import das minhas libs
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

#Leitura do meu arquivo csv
df = pd.read_csv('IOT-TEMP.csv', sep=',')

#engine para me conectar ao banco que está no meu docker
engine = create_engine('postgresql://postgres:RaphaelLim4@localhost:5432/postgres-iot')

#Inserindo o meu csv dentro do meu banco
df.to_sql("temperature_reading", con=engine, if_exists='replace', index=False)

print("Dados Inseridos")

# Função para carregar as minhas views
def load_data(view_name):
    try:
        df = pd.read_sql(f'SELECT * FROM {view_name}', engine)
        df.columns = df.columns.str.replace('"', '') 
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados da view {view_name}: {e}")
        return pd.DataFrame()  

#Título do dashboard
st.title('Dashboard de Temperatura IoT')

# Primeiro gráfico
st.header('Média de Temperatura por Tipo (In/Out)')
df_avg_temp = load_data('avg_temp_by_type')

if not df_avg_temp.empty:
    fig1 = px.bar(df_avg_temp, x='type', y='avg_temp', title="Média de Temperatura")
    st.plotly_chart(fig1)
else:
    st.warning("Nenhum dado disponível.")

# Segundo gráfico
st.header('Última Medição por Sala')
df_last_temp = load_data('last_temp_by_room')

if not df_last_temp.empty:
    fig2 = px.bar(df_last_temp, x='room_id', y='temp', title="Última Temperatura por Sala")
    st.plotly_chart(fig2)
else:
    st.warning("Nenhum dado disponível.")
    
# Terceiro gráfico

st.header('Contagem de Registros por Data e Tipo')
df_count_logs = load_data('count_logs_by_date')

if not df_count_logs.empty:
    fig3 = px.bar(df_count_logs, x='date', y='total_logs', color='type', title="Contagem de Registros")
    st.plotly_chart(fig3)
else:
    st.warning("Nenhum dado disponível.")