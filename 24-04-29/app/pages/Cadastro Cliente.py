import streamlit as st
import sqlite3
import pandas as pd


def cadastroPessoa(nome,data_nascimento,sexo,contato,cidade):
    conexao = sqlite3.connect('capirotinho.db') 
    c = conexao.cursor()
    c.execute("INSERT INTO pessoas (nome,data_nascimento,sexo,contato,cidade) VALUES (?,?,?,?,?)",(nome,data_nascimento,sexo,contato,cidade))
    print('inserido')
    conexao.commit()

consulta_cliente =  """
SELECT 
p.nome,
p.contato,
p.cidade,
p.sexo,
p.data_nascimento
from pessoas p 
"""
def mostrar_cliente():
    with sqlite3.connect('capirotinho.db') as conexao:
        return pd.read_sql_query(consulta_cliente, conexao)

col1,col2,col3,col4,col5=st.columns(5)

a=col1.text_input('Nome do(a) Cliente')
b=col2.text_input('data de nascimento')
c=col3.radio('Sexo',['Mas','Fem'])
st.write(c)
d=col4.number_input('Contato do(a) Cliente',min_value=0)
e=col5.text_input('Cidade')

if st.button('Cadastrar'):

    cadastroPessoa(a,b,c,d,e)
    st.success(f'Cliente {a} cadastrado(a)!')