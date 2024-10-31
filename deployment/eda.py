import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():

    st.title('Model Prediksi Tipe Diabetes')

    st.subheader('EDA Distribusi Fitur dalam Dataset')

    #memasukkan gambar
    image = Image.open('diabetes.jpg')
    st.image(image, caption = f'source: https://www.halodoc.com/artikel/perlu-tahu-ini-4-gejala-diabetes-tipe-2-yang-sering-diabaikan')

    #membuat garis lurus
    st.markdown('---')

    #load and show dataframe
    df = pd.read_csv('diabetes_dataset00.csv')
    df = df.sample(n=10000, random_state=99)  
    df = df.reset_index(drop=True) 
    st.dataframe(df)

    st.markdown('---')

    # Distribusi tipe diabetes
    st.write('#### Distribusi dari Target (Tipe Diabetes)')
    fig = plt.figure(figsize=(15,10))
    plt.title('Distribution of Diabetes Types')
    sns.countplot(x=df['Target'], palette='Set2')
    plt.xticks(rotation=90)
    st.pyplot(fig)

    st.markdown('---')

    # Distribusi Family History
    st.write('#### Histogram of Rating')
    fig = plt.figure(figsize=(8, 6))
    sns.countplot(x='Family History', data=df)
    plt.title('Family History Distribution')
    st.pyplot(fig)

    st.markdown('---')

    # historgram berdasarkan input user
    st.write('#### Histogram berdasarkan input user')
    option = st.selectbox('Pilih column: ', ('Age', 'BMI', 'Insulin Levels'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[option], bins = 20, kde = True)
    st.pyplot(fig)

    st.markdown('---')

    # historgram berdasarkan input user
    st.write('#### Distribusi Umur Berdasarkan Tipe Diabetes')
    fig = plt.figure(figsize=(10, 6))
    sns.boxplot(x='Target', y='Age', data=df)
    plt.xticks(rotation=90)
    plt.title('Age Distribution by Diabetes Type')
    st.pyplot(fig)

    st.markdown('---')

    # Distribusi BMI dengan Tekanan darah pasien
    st.write('#### Distribusi BMI dengan Tekanan Darah Pasien')
    fig = plt.figure(figsize=(8, 6))
    sns.scatterplot(x='BMI', y='Blood Pressure', data=df)
    plt.title('BMI vs Blood Pressure')
    plt.xlabel('BMI')
    plt.ylabel('Blood Pressure')
    st.pyplot(fig)

    st.markdown('---')

    # melihat korelasi dari tiap kolom numeric
    st.write('#### Korelasi dari Tiap Kolom Numeric')
    df_numeric = df.select_dtypes(include='number')
    corr_matrix = df_numeric.corr()
    fig = plt.figure(figsize=(15, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of Numerical Variables')
    st.pyplot(fig)
    
    
if __name__ == '__main__':
    run()