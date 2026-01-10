import streamlit as st
import main

st.set_page_config(page_title="DUKUN AI", page_icon="🤖")
st.title("Dukun AI yg akan meramal masa depan kamu bersama dia 🔮")
st.caption("Tarot | Zodiak | Curhat")

with st.sidebar:
    st.header("Follow @sulaimannibnu")
    if st.button("Chat Baru"):
        st.session_state.messages = []
        st.rerun()  

if "messages" not in st.session_state or len(st.session_state.messages) ==0:
    st.session_state.messages = []

    sapaan = "Sstt... Aku mencium bau-bau kegalauan di sini. Sini mendekat mau diramal jodohnya atau mau minta pelet online?"
    st.session_state.messages = [
        {"role" : "assistant", "content" : sapaan}
    ]

for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Tuliskan keluh kesah mu disini  "):
    st.session_state.messages.append({"role" : "user", "content" : prompt})

    with st.chat_message("assistant"):
        with st.spinner("Sedang menerawang masa depan kita..."):
            try:
                response = main.tanya_ai(prompt)
                    
                st.markdown(response)
                st.session_state.messages.append({"role" : "assistant", "content" : response})

            except Exception as e:
                st.error(f"Koneksi antara aku dan kamu terputus... : {e}")