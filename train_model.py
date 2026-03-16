import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# 1. Veri Yükleme
def load_and_merge():
    projects_url = "https://cordis.europa.eu/data/cordis-horizoneuropeprojects.csv"
    orgs_url = "https://cordis.europa.eu/data/cordis-horizoneuropeorganizations.csv"
    
    df_p = pd.read_csv(projects_url, sep=';', on_bad_lines='skip', low_memory=False)
    df_o = pd.read_csv(orgs_url, sep=';', on_bad_lines='skip', low_memory=False)
    
    # 'id' ve 'projectID' üzerinden birleştirme
    df = pd.merge(df_p, df_o, left_on='id', right_on='projectID', how='inner')
    return df

# 2. Eğitim Akışı
def train():
    df = load_and_merge()
    
    # Basit bir hedef: Medyandan fazla hibe alanlar "Yüksek Başarı" (1), az alanlar (0)
    limit = df['netContribution'].median()
    df['target'] = (df['netContribution'] > limit).astype(int)
    
    # Özellik seçimi
    features = ['country', 'activityType', 'totalCost']
    X = df[features]
    y = df['target']
    
    # Pipeline: Preprocessing + Model
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['totalCost']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['country', 'activityType'])
        ])
    
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression())
    ])
    
    # Eğitim
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model.fit(X_train, y_train)
    
    # Modeli Kaydet
    joblib.dump(model, 'models/horizon_model.pkl')
    print("✅ Model eğitildi ve 'models/horizon_model.pkl' olarak kaydedildi!")

if __name__ == "__main__":
    train()