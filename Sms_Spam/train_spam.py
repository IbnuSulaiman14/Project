import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB



df = pd.read_csv("dataset_sms_spam.csv", encoding='latin-1', usecols=['Teks', 'label'])
df = df.dropna()

vectorizer = CountVectorizer()

kamus = {0:'Normal', 1:'Penipuan', 2:'Promo'}
df['Sentiment'] = df['label'].map(kamus)

x = vectorizer.fit_transform(df['Teks'])
y = df['label']

model = MultinomialNB()
model.fit(x,y)

joblib.dump(model, "model_sms.pkl")
joblib.dump(vectorizer, "vectorizer_sms.pkl")
