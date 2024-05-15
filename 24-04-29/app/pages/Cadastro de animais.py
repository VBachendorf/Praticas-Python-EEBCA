import streamlit as st
import pandas as pd
import sqlite3
conn = sqlite3.connect('capirotinho.db')
def db_cadastro_especie(nome,is_mamifero,nome_familia):
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO especies
        (name, is_mamifero, familia)
        VALUES (?, ?, ?)""",
        (nome, is_mamifero, nome_familia))
        conn.commit()
        
    except Exception as e:
        st.error(f"Erro ao cadastrar a espécie: {e}")
    finally:
        conn.close()
st.title('Cadastro de Animais !')
tab1,tab2,tab3 = st.tabs(['Espécie','Raça','Animal'])
with tab1:
    col1,col2,col3=st.columns(3)
    a=col1.text_input('digite o nome da Espécie')
    b=col2.radio('o animal é mamífero',['Sim','Não'])
    c=col3.text_input('nome de familia do animal',key='ass')
    if col2.button('cadastro'):
        if b=='Não':
            b=0
        else:
            b=1
        st.write(b)
        db_cadastro_especie(a,b,c)