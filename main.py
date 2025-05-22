import streamlit as st
import sqlite3
import random

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect("responses.db")
c = conn.cursor()

# Create table if it doesn't exist
c.execute("""
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL
    )
""")
conn.commit()

# Function to add response
def add_response(message):
    c.execute("INSERT INTO responses (message) VALUES (?)", (message,))
    conn.commit()

# Function to get all responses
def get_all_responses():
    c.execute("SELECT message FROM responses")
    return [row[0] for row in c.fetchall()]

# Streamlit App UI
st.title("Prueba Programa 1")

# Section: Submit a response
st.header("Escribe algo:")
user_input = st.text_area("Escribe", height=100)

if st.button("Submit"):
    if user_input.strip():
        add_response(user_input.strip())
        st.success("Listo")
    else:
        st.warning("Hay q escribir algo pues!!!")

# Section: Random response
st.header("✨ Ver Respuesta")
if st.button("Seleccionar"):
    responses = get_all_responses()
    if responses:
        st.info(random.choice(responses))
    else:
        st.warning("Todavía no hay respuestas")
