import streamlit as st
import sqlite3
import random

conn = sqlite3.connect('respuestas.db')
c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXISTS responses (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          message TEXT NOT NULL
          )
          """)

conn.commit()

def add_response(message):
    c.execute('INSERT INTO responses (message) VALUES (?)', (message,))

def get_all_responses():
    c.execute("SELECT message FROM responses")
    return [row[0] for row in c.fetchall()]

st.title('Para Asincerarnos, Pues')

st.header('Escribe Aquí: ')
user_input = st.text_area('Escribe', height=100)

if st.button('submit'):
    if user_input.strip():
        add_response(user_input.strip())
        st.success('Listo! Ahora puedes mandar otra!')
    else:
        st.warning('Hubo un error, pendeja la que hizo este programa')

st.header('Respuesta Random')

if st.button('Pon una respuesta: '):
    responses = get_all_responses()
    if responses:
        st.info(random.choice(responses))
    else:
        st.warning('No hay respuestas todavía!')