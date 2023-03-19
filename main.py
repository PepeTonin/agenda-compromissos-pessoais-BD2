import mysql.connector
from mysql.connector import errorcode
import streamlit as st
from querysSQL import *


senha = st.text_input('senha de acesso ao banco de dados', type='password')
acessarBanco = st.checkbox('entrar')
if not acessarBanco:
    st.stop()

#  estabelecer conexão com a database
# tenta estabelecer conexão:
try:
    # instancia um objeto mysql.connector na variavel db_connection
    db_connection = mysql.connector.connect(
        host='localhost', user='root', password=senha, database='aulaIntegracaoSQLePY')
    st.write('Conexão com o banco de dados feita!')

# em caso de algum erro, executa essa parte
except mysql.connector.Error as error:
    # trata os diferentes erros
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        st.write('Esse banco de dados não existe!')
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        st.write('Usuário ou senha inválidos!')
    else:
        st.write(error)

# se não der erro, executa essa parte
else:

    cursor = db_connection.cursor()

    tab_select, tab_insert, tab_delete = st.tabs(
        ['Visualizar', 'Inserir', 'Deletar'])

    with tab_select:
        st.header('Visualizar dados do banco')

        with st.form('pesquisar dados no banco'):

            date = st.date_input('Data inicial da busca')
            time = st.time_input('Hora inicial da busca')
            qntde = st.slider(
                'Quantidade de compromissos mostrados', 1, 20, 5, 1)

            submitted_select = st.form_submit_button('pesquisar')

            if submitted_select:

                select_script = selectQuery(date, time, qntde)

                cursor.execute(select_script)
                result = cursor.fetchall()

                for elemento in result:
                    st.write(elemento)
                    print(elemento)

    with tab_insert:
        st.header('Inserir dados no banco')

        with st.form('inserir dados no banco'):

            compromisso = st.text_input('Compromisso')
            descricao = st.text_input('Descricao do compromisso')
            data_inicio = st.date_input('Data inicio')
            hora_inicio = st.text_input(
                'Hora inicio', placeholder='08:00', help='Utilizar o formato "00:00"')
            data_fim = st.date_input('Data fim')
            hora_fim = st.text_input(
                'Hora fim', placeholder='09:00', help='Utilizar o formato "00:00"')

            submitted_insert = st.form_submit_button('enviar')

            if submitted_insert:
                insert_script = insertQuery(
                    compromisso, descricao, data_inicio, hora_inicio, data_fim, hora_fim)
                cursor.execute(insert_script)
                db_connection.commit()
                st.success('Item inserido')

    with tab_delete:
        st.header('Apagar dados do banco')

        with st.form('apagar dados no banco'):

            idItem = st.number_input('id do item que deseja deletar', step=1)

            submitted_delete = st.form_submit_button('deletar')

            if submitted_delete:
                select_before_delete_script = selectBeforeDeleteQuery(idItem)
                cursor.execute(select_before_delete_script)
                deleted_item = cursor.fetchall()
                delete_script = deleteQuery(idItem)
                cursor.execute(delete_script)
                db_connection.commit()
                st.warning('Voce excluiu o item:')
                st.text(deleted_item)
