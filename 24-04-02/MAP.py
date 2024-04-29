import streamlit as st
c1,c2,c3=st.columns(3)

c1.metric('Casos Confirmados',420,delta=10)
c2.metric('Casos descartados',920,delta=80)
c3.metric('Casos Confirmados',420,delta=10)
st.subheader("Mapa de focos de Dengue",divider='red')
df =   {"lat": [-27.07960799144775,-27.08113642996132, -27.08165677603751,-27.073408001343402],
        "lon": [-53.002369904752655,-53.000736850887044, -53.00408957771627, -53.005462519671624],
        "size":[20.9,0.10,0.2,0.2]}

st.map(df,
    latitude='lat',
    longitude='lon',
    size='size')

from exemplotxt import adicionar_item_arquivo, ler_itens_arquivo
st.subheader("Mapa de focos de Dengue",divider='red')
a,b,c=st.columns(3)
produto=a.text_input('Produto',key="Dengue")
quantidade=b.number_input('Quantidade',value=1, key="Qtd")
valor=c.number_input('Valor',min_value=47)
if st.button('x'):
    adicionar_item_arquivo(produto,quantidade,valor)
    st.success('OK')

if st.button('y'):
    itens=ler_itens_arquivo()
    st.dataframe(itens)

