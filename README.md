# 🏨 Revenue Intelligence System para Hotelaria

## 📌 Visão Geral

Este projeto implementa um sistema completo de **Revenue Management para hotelaria**, utilizando Machine Learning para prever cancelamentos de reservas e simular impacto financeiro em decisões operacionais.

O sistema vai além da previsão estatística: ele atua como um **motor de decisão orientado a receita**, permitindo que hotéis antecipem riscos e otimizem sua estratégia de ocupação.

---

## 🎯 Problema de Negócio

O setor hoteleiro enfrenta um problema recorrente de cancelamentos de reservas, impactando diretamente:

- Receita total
- Taxa de ocupação
- Planejamento operacional
- Estratégias de precificação

No conjunto de dados analisado:

- Aproximadamente **33% da receita potencial é perdida devido a cancelamentos**
- Mais de **29 mil cancelamentos são esperados no período analisado**

---

## 💡 Objetivo do Projeto

Construir um sistema capaz de:

- Prever probabilidade de cancelamento de reservas
- Classificar reservas por nível de risco
- Estimar impacto financeiro por reserva
- Simular cenários de mitigação de cancelamento
- Apoiar decisões estratégicas de revenue management

---

## 🧠 Pipeline da Solução

### 1. Engenharia de Dados
- Remoção de duplicatas (~27% da base)
- Tratamento de valores ausentes
- Padronização de variáveis categóricas
- Criação de variáveis derivadas (ex: total_stay)

---

### 2. Análise Exploratória (EDA)
- Taxa geral de cancelamento (~27,5%)
- Relação entre lead time e cancelamento
- Impacto de preço (ADR)
- Sazonalidade de cancelamentos
- Segmentação por canal e tipo de cliente

---

### 3. Preparação para Machine Learning
- One-Hot Encoding de variáveis categóricas
- Normalização de variáveis numéricas
- Separação treino/teste estratificada
- Remoção de variáveis com data leakage

---

### 4. Modelagem Preditiva

Modelos testados:

- Regressão Logística (baseline)
- Regressão Logística com balanceamento de classes
- Random Forest (modelo final)

---

### 📊 Performance do Modelo Final

| Métrica        | Resultado |
|----------------|----------|
| Acurácia       | ~85%     |
| ROC-AUC        | ~0.91    |
| Recall (cancelamentos) | ~63% |

O modelo final apresentou melhor equilíbrio entre precisão e capacidade de detecção de cancelamentos.

---

## ⚙️ Motor de Decisão (Sistema de Risco)

O modelo foi integrado a um sistema de decisão baseado em probabilidade:

### 🔴 Alto risco (> 0.70)
- Ações de retenção ativa
- Estratégias de overbooking controlado

### 🟡 Médio risco (0.40 – 0.70)
- Reconfirmação automática
- Comunicação preventiva com o cliente

### 🟢 Baixo risco (< 0.40)
- Operação padrão sem intervenção

---

## 💰 Impacto Financeiro Simulado

O sistema foi avaliado com base em impacto econômico:

- 💰 Receita total potencial: **34,46 milhões**
- ❌ Receita perdida por cancelamentos: **11,48 milhões**
- 📉 Impacto atual: **33% de perda de receita**
- 📈 Ganho estimado com o sistema: **1,74 milhões**
- 📊 Cancelamentos previstos: **29.461 reservas**

👉 O sistema demonstra potencial de **recuperação de aproximadamente 15% das perdas financeiras**.

---

## 📊 Dashboard Interativo (Streamlit)

O projeto inclui um dashboard para análise operacional contendo:

- KPIs financeiros (receita, perda, ganho)
- Distribuição de risco de cancelamento
- Impacto financeiro por nível de risco
- Lista de reservas críticas (alto risco)

---

## 🧱 Estrutura do Projeto
Rede_Hotelaria/
├── data/
│ └── hotel_bookings.csv # Dataset inicial
│
├── notebook/
│ └── hotel_data_final.csv # Dataset tratado
│ └── hotel_project.ipynb # notebook do projeto
│
├── Streamlite/
│ └── app.py # Dashboard Streamlit
│
│── requirements.txt # Dependências do projeto
├── README.md # Documentação


---

## 🚀 Como Executar o Projeto

### 1. Instalar dependências

```bash
pip install -r requirements.txt

### 2. Rodar o dashboard

```bash
streamlit run app.py
