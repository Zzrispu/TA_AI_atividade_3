import streamlit as st
import pandas as pd
import psycopg2
import os
import plotly.express as px
from dotenv import load_dotenv

load_dotenv()

# Configuração do banco de dados
DB_CONFIG = {
    'dbname': 'ml_models_comparations',
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': 'localhost',
    'port': os.getenv("DB_PORT")
}

# Função para buscar dados do banco
def run_query(query):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Erro ao consultar o banco: {e}")
        return pd.DataFrame()

# Layout do Streamlit
st.title("Comparação de Modelos de Machine Learning")

# Opção para selecionar tipo de modelo
model_type = st.selectbox("Selecione o tipo de modelo:", ["Todos", "Classificação", "Regressão"])

# Consulta SQL baseada na escolha
query = """
SELECT 
    m.name AS model, 
    m.type AS type, 
    r.dataset, 
    r.train_size, 
    r.test_size, 
    p.sampling_strategy, 
    p.split_method, 
    p.normalized, 
    me.metric_name, 
    me.metric_value
FROM results r
JOIN models m ON r.model_id = m.id
JOIN preprocessing p ON r.preprocessing_id = p.id
JOIN metrics me ON r.id = me.result_id
"""

if model_type == "Classificação":
    query += " WHERE m.type = 'classification'"
elif model_type == "Regressão":
    query += " WHERE m.type = 'regression'"

query += "ORDER BY m.name, me.metric_name;"

# Obter dados
df = run_query(query)
df_pivot = df.pivot(index=["model", "type", "dataset", "train_size", "test_size", "sampling_strategy", "split_method", "normalized"], columns="metric_name", values="metric_value")
df_pivot.reset_index(inplace=True)

# Exibir tabela de resultados
st.write("### Resultados dos Modelos")
st.dataframe(df_pivot)

# Criar gráfico comparativo de acurácia
if not df.empty:
    if model_type == "Classificação":
        fig = px.bar(df_pivot, x="dataset", y="accuracy", color="normalized", title="Comparação de Acurácia", barmode="group")
        st.plotly_chart(fig, key="accuracy")
        fig = px.bar(df_pivot, x="dataset", y="precision", color="normalized", title="Comparação de Precisão", barmode="group")
        st.plotly_chart(fig, key="precision")
        fig = px.bar(df_pivot, x="dataset", y="recall", color="normalized", title="Comparação de Recall", barmode="group")
        st.plotly_chart(fig, key="recall")
        fig = px.bar(df_pivot, x="dataset", y="f1", color="normalized", title="Comparação de F1-score", barmode="group")
        st.plotly_chart(fig, key="f1")
        fig = px.bar(df_pivot, x="dataset", y="roc_auc", color="normalized", title="Comparação de ROC-AUC", barmode="group")
        st.plotly_chart(fig, key="roc_auc")

    elif model_type == "Regressão":
        fig = px.bar(df_pivot, x="dataset", y="mse", color="normalized", title="Comparação de MSE", barmode="group")
        st.plotly_chart(fig, key="mse")
        fig = px.bar(df_pivot, x="dataset", y="mape", color="normalized", title="Comparação de MAPE", barmode="group")
        st.plotly_chart(fig, key="mape")
        fig = px.bar(df_pivot, x="dataset", y="mae", color="normalized", title="Comparação de MAE", barmode="group")
        st.plotly_chart(fig, key="mae")
        fig = px.bar(df_pivot, x="dataset", y="r2", color="normalized", title="Comparação de R²", barmode="group")
        st.plotly_chart(fig, key="r2")