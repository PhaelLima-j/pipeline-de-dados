import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

df = pd.read_csv('IOT-TEMP.csv', sep=',')

engine = create_engine('postgresql://postgres:RaphaelLim4@localhost:5432/postgres-iot')

df.to_sql("temperature_reading", con=engine, if_exists='replace', index=False)

print("Dados Inseridos")
