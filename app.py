import streamlit as st
import pandas as pd
import joblib

# Sayfa Ayarları
st.set_page_config(page_title="HorizonPredict", page_icon="🇪🇺")
st.title("Horizon Europe Hibe Tahmin Modeli")

# Modeli Yükle
model = joblib.load('models/horizon_model.pkl')

# Kullanıcı Girişleri
st.subheader("Proje Bilgilerini Giriniz")
col1, col2 = st.columns(2)

with col1:
    country = st.selectbox("Ülke", ["TR", "DE", "FR", "ES", "IT", "BE"])
    activity = st.selectbox("Kuruluş Türü", ["PRC", "HES", "REC", "PUB"])

with col2:
    budget = st.number_input("Toplam Proje Bütçesi (€)", value=1000000)

# Tahmin
if st.button("Başarı Olasılığını Hesapla"):
    input_df = pd.DataFrame([[country, activity, budget]], columns=['country', 'activityType', 'totalCost'])
    prob = model.predict_proba(input_df)[0][1]
    
    st.metric("Hibe Başarı Olasılığı", f"%{prob*100:.2f}")
    
    if prob > 0.6:
        st.success("Bu konfigürasyon güçlü bir potansiyele sahip!")
    else:
        st.info("Konsorsiyum yapısı güçlendirilerek olasılık artırılabilir.")