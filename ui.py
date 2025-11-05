import streamlit as st
import requests
import pandas as pd


API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="FastAPI Login",layout="centered")
st.title("FastAPI Login System")

menu = ["Register","Login","Update Username","Delete User","Show Users"]
choice = st.sidebar.selectbox("select Action",menu)

# Register
if choice == 'Register':
    st.subheader("Register User")
    username = st.text_input("Username")
    password = st.text_input("password",type="password")
    if st.button("Register"):
        res = requests.post(f"{API_URL}/register",json={"username":username,"password":password})
        if res.status_code == 200:
            st.success("User Registered Successfully!")
        else:
            st.error("User Already Exists") 

 # Login
elif choice == "Login":
    st.subheader("Login User")
    username = st.text_input("Username")
    password = st.text_input("password",type="password")
    if st.button("Login"):
        res = requests.post(f"{API_URL}/login",json={"username":username,"password":password})
        if res.status_code == 200:
            st.success("Login Successfully!")
# Update
elif choice == "Update Username":
    st.subheader("Update Username")
    user_id = st.number_input("User ID",min_value=1)
    new_username = st.text_input("New Username")
    if st.button("Update"):
        res = requests.put(f"{API_URL}/update/{user_id}?username={new_username}")
        if res.status_code == 200:
            st.success("Username Updated Successfully!")
        else:
            st.error("Update Failed")
# Delete
elif choice == "Delete User":
    st.subheader("Delete User")
    user_id = st.number_input("User ID",min_value=1)
    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/delete/{user_id}")
        if res.status_code == 200:
            st.success("User Deleted Successfully!")
        else:
            st.error("Delete Failed")

# Show User
elif choice == "Show Users":
    st.subheader("User List")
    users = requests.get(f"{API_URL}/users").json()
    if users:
        df = pd.DataFrame(users,columns=["ID","Username"])
        st.dataframe(df,use_container_width=True)
        st.write("Delete User From Table")
        for idx, row in df.iterrows():
            col1,col2,col3 = st.columns([2,4,2])
            col1.write(f"ID {row["ID"]}")
            col2.write(f"{row["Username"]}")
            if col3.button(f"Delete {row["ID"]}"):
                requests.delete(f"{API_URL}/delete/{row["ID"]}")
                st.success(f"Deleted {row["Username"]}")
                st.rerun()
    else:
        st.info("No users found")
    if st.button("Refresh"):
        st.rerun()                



                 
