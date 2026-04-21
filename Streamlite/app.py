import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# Configuração
st.set_page_config(page_title="Revenue Management System", layout="wide")

st.title("🏨 Sistema Inteligente de Revenue Management")

# Carregar os Dados
@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parent
    candidate_paths = [
        base_dir / "hotel_data_final.csv",
        base_dir.parent / "notebook" / "hotel_data_final.csv",
        Path.cwd() / "hotel_data_final.csv",
    ]

    for data_path in candidate_paths:
        if data_path.exists():
            return pd.read_csv(data_path)

    searched_paths = "\n".join(str(path) for path in candidate_paths)
    raise FileNotFoundError(
        "Arquivo 'hotel_data_final.csv' nao encontrado. Caminhos verificados:\n"
        f"{searched_paths}"
    )

df = load_data()

# Kpis
col1, col2, col3, col4 = st.columns(4)

col1.metric("Receita Total", f"{df['receita'].sum():,.0f}")
col2.metric("Receita Perdida", f"{(df['receita'] * df['is_canceled']).sum():,.0f}")
col3.metric("Ganho do Sistema", f"{df['ganho_esperado'].sum():,.0f}")
col4.metric("Cancelamentos", f"{df['prob_cancelamento'].sum():,.0f}")

st.divider()

# Risco
st.subheader("📊 Distribuição de Risco")

risk_counts = df['risk_level'].value_counts().reset_index()
risk_counts.columns = ['Risco', 'Quantidade']

fig1 = px.bar(risk_counts, x='Risco', y='Quantidade', color='Risco')
st.plotly_chart(fig1, use_container_width=True)

# Impacto Financeiro
st.subheader("💰 Impacto Financeiro por Risco")

impact = df.groupby('risk_level')['ganho_esperado'].sum().reset_index()

fig2 = px.bar(impact, x='risk_level', y='ganho_esperado', color='risk_level')
st.plotly_chart(fig2, use_container_width=True)

# Top Riscos
st.subheader("⚠️ Reservas de Alto Risco")

top_risk = df.sort_values('prob_cancelamento', ascending=False).head(20)

st.dataframe(
    top_risk[['hotel', 'lead_time', 'adr', 'prob_cancelamento', 'risk_level', 'acao']],
    use_container_width=True
)

# Insights finais
st.divider()

st.subheader("🧠 Insight do Sistema")

st.info("""
Este sistema combina Machine Learning + regras de decisão para prever cancelamentos e estimar impacto financeiro.
Ele permite que a operação hoteleira atue preventivamente em reservas de alto risco, reduzindo perdas de receita.
""")
