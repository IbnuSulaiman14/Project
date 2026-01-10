import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

data_produksi = {
    'Suhu_Mesin':   [80, 95, 70, 105, 85, 60, 110, 75, 90, 100], # Derajat Celcius
    'Tekanan':      [10, 15, 8, 20, 12, 5, 25, 9, 14, 18],       # Bar (Satuan tekanan)
    'Waktu_Proses': [30, 45, 25, 60, 35, 20, 70, 28, 40, 55],    # Detik
    'Hasil_QC':     ['Lolos', 'Cacat', 'Lolos', 'Cacat', 'Lolos', 'Lolos', 'Cacat', 'Lolos', 'Cacat', 'Cacat']
}

df = pd.DataFrame(data_produksi)

map_hasil_qc = {'Cacat':0, 'Lolos' : 1}
df['Kode_Hasil_QC'] = df['Hasil_QC'].map(map_hasil_qc)

x = df[["Suhu_Mesin", "Tekanan", "Waktu_Proses"]]
y = df["Kode_Hasil_QC"]

model = LogisticRegression()
model.fit(x,y)

joblib.dump(model, "model_qc.pkl")