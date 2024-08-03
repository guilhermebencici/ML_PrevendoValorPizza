## Biblioteca para criação de app web, sem utilizar HTML, CSS e JS. Apenas py
import streamlit as st

## Biblioteca para tratamento de dados
import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

## criando o modelo
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

## treinando o modelo
modelo.fit(x,y)

## criando a interface
##usando o streamlit (biblioteca de interface)

st.title("Prevendo o valor de uma Pizza")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da pizza: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com o diâmetro {diametro:.2f} é de R$: {preco_previsto:.2f}.")
    st.balloons()
