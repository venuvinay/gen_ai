import streamlit as st
import requests

def e_request(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={"input": {"topic": input_text}}
        )
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("output", "No output key in the response")
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except ValueError:
        return "Invalid JSON response"

def p_request(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={"input": {"topic": input_text}}
        )
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json().get("output", "No output key in the response")
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except ValueError:
        return "Invalid JSON response"

st.title("Vinay API Client")

e_input = st.text_input("Enter topic for essay")
e_button = st.button("Click for essay")

p_input = st.text_input("Enter topic for poem")
p_button = st.button("Click for poem")

if e_button and e_input:
    output = e_request(e_input)
    st.write(output)

if p_button and p_input:
    output1 = p_request(p_input)
    st.write(output1)
