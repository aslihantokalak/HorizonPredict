# 🇪🇺 HorizonPredict: Horizon Europe Grant Success Predictor

Bu proje, Avrupa Birliği **Horizon Europe** programı kapsamında hibe alan projeleri ve kuruluşları analiz ederek, yeni başvuruların başarı olasılığını tahmin eden uçtan uca bir makine öğrenmesi (ML) çözümüdür.

## 🚀 Projenin Amacı
Stratejik bir karar destek mekanizması oluşturmak. "Hangi ülke, hangi kuruluş türü ve hangi bütçe ölçeğiyle daha başarılı oluyor?" sorusuna geçmiş CORDIS verilerini kullanarak yanıt vermek.

---

## 🛠️ Yazılım Mimarisi (Architecture)

Proje, modüler ve ölçeklenebilir bir yapı üzerine kurulmuştur:

1. **Data Ingestion:** CORDIS API/CSV üzerinden canlı veri çekimi.
2. **Preprocessing Pipeline:** Kategorik veriler için `One-Hot Encoding`, sayısal veriler için `StandardScaler` kullanımı.
3. **Model Engine:** Olasılıksal çıktı üretebilen **Logistic Regression** algoritması.
4. **UI/Interface:** Kullanıcı dostu veri girişi ve sonuç görselleştirme için **Streamlit**.



---

## 📊 Özellik Mühendisliği (Feature Engineering)
Modelin başarısını artıran temel metrikler:
* **Activity Type:** Kuruluşun akademik, özel sektör veya kamu olması.
* **Country Effect:** Ülkelerin tarihsel hibe alma başarı oranları.
* **Budget Scaling:** Proje bütçesinin standartlaştırılmış ağırlığı.

---

## 💻 Kurulum ve Çalıştırma

1. Projeyi klonlayın:
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/HorizonPredict.git](https://github.com/KULLANICI_ADIN/HorizonPredict.git)
Gemini şunu dedi:
Harika! Şimdi GitHub deponda dosyalar duruyor ama o sayfanın bir "vitrine" ihtiyacı var. Bir İK uzmanı veya teknik müdür sayfana girdiğinde, kodlara bakmadan önce neyi, neden ve nasıl yaptığını anlamalı.

İşte DEHB dostu, modüler ve profesyonel README.md taslağın. Bunu kopyalayıp GitHub'daki README.md dosyanın içine yapıştırabilirsin.

Markdown
# 🇪🇺 HorizonPredict: Horizon Europe Grant Success Predictor

Bu proje, Avrupa Birliği **Horizon Europe** programı kapsamında hibe alan projeleri ve kuruluşları analiz ederek, yeni başvuruların başarı olasılığını tahmin eden uçtan uca bir makine öğrenmesi (ML) çözümüdür.

## 🚀 Projenin Amacı
Stratejik bir karar destek mekanizması oluşturmak. "Hangi ülke, hangi kuruluş türü ve hangi bütçe ölçeğiyle daha başarılı oluyor?" sorusuna geçmiş CORDIS verilerini kullanarak yanıt vermek.

---

## 🛠️ Yazılım Mimarisi (Architecture)

Proje, modüler ve ölçeklenebilir bir yapı üzerine kurulmuştur:

1. **Data Ingestion:** CORDIS API/CSV üzerinden canlı veri çekimi.
2. **Preprocessing Pipeline:** Kategorik veriler için `One-Hot Encoding`, sayısal veriler için `StandardScaler` kullanımı.
3. **Model Engine:** Olasılıksal çıktı üretebilen **Logistic Regression** algoritması.
4. **UI/Interface:** Kullanıcı dostu veri girişi ve sonuç görselleştirme için **Streamlit**.



---

## 📊 Özellik Mühendisliği (Feature Engineering)
Modelin başarısını artıran temel metrikler:
* **Activity Type:** Kuruluşun akademik, özel sektör veya kamu olması.
* **Country Effect:** Ülkelerin tarihsel hibe alma başarı oranları.
* **Budget Scaling:** Proje bütçesinin standartlaştırılmış ağırlığı.

---

## 💻 Kurulum ve Çalıştırma

1. Projeyi klonlayın:
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/HorizonPredict.git](https://github.com/KULLANICI_ADIN/HorizonPredict.git)
2. Gerekli kütüphaneleri yükleyin:

Bash
pip install -r requirements.txt
3. Modeli eğitin:

Bash
python train_model.py
4. Uygulamayı başlatın:

Bash
streamlit run app.py
📈 Gelecek Planları (Roadmap)
[ ] NLP Entegrasyonu: Proje özetlerinden (abstract) anahtar kelime analizi yapılması.

[ ] XGBoost Geçişi: Daha karmaşık ilişkileri yakalamak için modelin güncellenmesi.

[ ] SHAP Explainability: Tahminlerin nedenlerini açıklayan görselleştirme paneli.

Yazar: [Aslıhan B. Tokalak]

İletişim: [https://www.linkedin.com/in/aslihanbardak/]

