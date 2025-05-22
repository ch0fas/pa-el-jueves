import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random

# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Build credentials dict from st.secrets
creds_dict = {
    "type": st.secrets["gcp_service_account"]["type"],
    "project_id": st.secrets["gcp_service_account"]["project_id"],
    "private_key_id": st.secrets["gcp_service_account"]["private_key_id"],
    "private_key": st.secrets["gcp_service_account"]["private_key"],
    "client_email": st.secrets["gcp_service_account"]["client_email"],
    "client_id": st.secrets["gcp_service_account"]["client_id"],
    "auth_uri": st.secrets["gcp_service_account"]["auth_uri"],
    "token_uri": st.secrets["gcp_service_account"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["gcp_service_account"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["gcp_service_account"]["client_x509_cert_url"]
}

credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(credentials)
sheet = client.open("ThoughtCollector").sheet1

# Function to add a response
def add_response(message):
    sheet.append_row([message])

# Function to get all responses
def get_all_responses():
    return sheet.col_values(1)

# Streamlit UI
st.title("📒 Thought Collector (Google Sheets)")

st.header("Write your thoughts:")
user_input = st.text_area("What’s on your mind?", height=100)

if st.button("Submit"):
    if user_input.strip():
        add_response(user_input.strip())
        st.success("Thanks! Your response has been saved.")
    else:
        st.warning("Please write something before submitting.")

st.header("🎲 Feeling curious?")
if st.button("Give me a random thought"):
    responses = get_all_responses()
    if responses:
        st.info(random.choice(responses))
    else:
        st.warning("No responses yet. Be the first!")
