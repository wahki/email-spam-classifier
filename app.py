import streamlit as st
from predict import predict

st.title("📧 E-Posta Spam Tespiti")
text = st.text_area("E-posta Metni", height=200)

if st.button("Tahmin Et"):
    if not text.strip():
        st.warning("Lütfen önce e-posta metni girin.")
    else:
        pred = predict(text)
        if pred == 1:
            st.error("⚠️ Bu bir SPAM e-posta.")
        else:
            st.success("✅ Bu e-posta spam değil.")
