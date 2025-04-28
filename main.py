import requests
import base64
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

credentials = f"{os.getenv('ALLOY_API_TOKEN')}:{os.getenv('ALLOY_API_SECRET')}"
encoded_string = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

# get the exact format of required fields #

get_url = "https://sandbox.alloy.co/v1/parameters"
headers = {"accept": "application/json", "authorization": "Basic " + encoded_string}
response = requests.get(get_url, headers=headers)
print(response.text)


# submit an evaluation #

post_url = "https://sandbox.alloy.co/v1/evaluations"
st.title("Alloy Take Home Assignment")

with st.form("Enter your information"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    birth_date = st.text_input("Date of Birth YYYY-MM-DD")
    ssn = st.text_input("Social Security Number")
    email = st.text_input("Email")
    address_line1 = st.text_input("Address Line 1")
    address_line2 = st.text_input("Address Line 2")
    city = st.text_input("City")
    state = st.text_input("State")
    zip_code = st.text_input("Zip Code")
    country = st.text_input("Country Code")
    submit = st.form_submit_button("Submit")

    if submit:
        data = {
            "name_first": first_name,
            "name_last": last_name,
            "birth_date": birth_date,
            "document_ssn": ssn,
            "email_address": email,
            "address_line_1": address_line1,
            "address_line_2": address_line2,
            "address_city": city,
            "address_state": state,
            "address_postal_code": zip_code,
            "address_country_code": country,
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Basic " + encoded_string,
        }
        response = requests.post(post_url, json=data, headers=headers)
        results = response.json()

        if response.status_code == 200:
            st.write("Missing required fields")
        elif response.status_code == 201 or response.status_code == 206:
            if results["summary"]["outcome"] == "Approved":
                st.write("Congratulations! You are approved.")
            if results["summary"]["outcome"] == "Manual Review":
                st.write("Your application is under review. Please wait for further updates.")
            if results["summary"]["outcome"] == "Denied":
                st.write("Unfortunately, we cannot approve your application at this time.")
        elif response.status_code == 400:
            st.write(results["error"]["message"])
        else:
            st.write("Error processing your request")
            st.write(results)
