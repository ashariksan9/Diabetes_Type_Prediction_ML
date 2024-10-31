import streamlit as st
import pandas as pd
import numpy as np
import pickle


#Load All files

with open ('model_terbaik.pkl','rb') as file:
    model = pickle.load(file)


def run():
  #kita buat form untuk isi data
    with st.form('form_pasien_diabetes'):

        # select 1
        Gen_mark = st.selectbox('Genetic MArkers: ', ('Positive', 'Negative'), index=1)
        Autoantibodies = st.selectbox('Autoantibodies: ', ('Positive', 'Negative'), index=1)
        history = st.selectbox('Family History: ', ('Yes', 'No'), index=1)
        Environmental = st.selectbox('Environmental Factors: ', ('Present', 'Absent'), index=1)
        Smoking = st.selectbox('Smoking Status: ', ('Smoker', 'Non-Smoker'), index=1)
        Early = st.selectbox('Early Onset Symptoms: ', ('Yes', 'No'), index=1)


        # numeric 1
        Insulin_Levels = st.number_input('Insulin Levels: ', value = 5, min_value = 0, max_value = 50, help = 'min = 0 and max = 50')
        age = st.number_input('Age: ', value = 36, min_value = 0, max_value = 80, help = 'isi dengan usia pasien')
        Berat = st.number_input('BMI: ', value = 32, min_value = 10, max_value = 40, help = 'isi dengan BMI pasien')
        blood = st.number_input('Blood Pressure', value = 115, min_value = 60, max_value = 160, help = 'isi dengan tekanan darah pasien')


        # numeric slides 1
        kolesterol = st.slider('Cholesterol Levels', value = 221, min_value = 100, max_value = 300, help = 'isi dengan level kolesterol pasien')


        # select 2
        Activity = st.selectbox('Physical Activity: ', ('Low', 'Moderate', 'High'), index=1)
        habits = st.selectbox('Dietary Habits: ', ('Healthy', 'Unhealthy'), index=1)
        etnis = st.selectbox('Ethnicity: ', ('Low Risk', 'High Risk'), index=1)
        Socioeconomic = st.selectbox('Socioeconomic Factors: ', ('Low', 'Medium', 'High'), index=1)
        Alcohol = st.selectbox('Alcohol Consumption: ', ('Low', 'Moderate', 'High'), index=1)
       

        # numeric 2
        Waist = st.number_input('Waist Circumference: ', value = 36, help = 'isi dengan lingkar pinggang pasien')
        Blood_Glucose = st.number_input('Blood Glucose Levels: ', value = 134, min_value = 80, help = 'isi dengan level gula darah pasien')
        Gain_hamil = st.number_input('Weight Gain During Pregnancy: ', value = 18, min_value = 0, max_value = 40, help = 'isi dengan kenaikan berat saat hamil')
        Birth_Weight = st.number_input('Birth Weight: ', value = 2645, min_value = 1000, help = 'isi dengan berat janin (g) pasien saat kehamilan')
        

        # numeric slides 2
        Pancreatic = st.slider('Pancreatic Health: ', value = 73, min_value = 10, max_value = 99)
        Pulmonary = st.slider('Pulmonary Function: ', value = 78, min_value = 30, max_value = 90)
        Enzyme = st.slider('Digestive Enzyme Levels: ', value = 53, min_value = 10, max_value = 99)
        

        # select 3
        Tolerance = st.selectbox('Glucose Tolerance Test: ', ('Normal', 'Abnormal'), index=1)
        history_pcos = st.selectbox('History of PCOS: ', ('Yes', 'No'), index=1)
        Gestational = st.selectbox('Previous Gestational Diabetes: ', ('Yes', 'No'), index=1)
        Pregnancy = st.selectbox('Autoantibodies: ', ('Normal', 'Complications'), index=1)
        Cystic = st.selectbox('Cystic Fibrosis Diagnosis: ', ('Yes', 'No'), index=1)
        Steroid = st.selectbox('Steroid Use History: ', ('Yes', 'No'), index=1)
        Genetic = st.selectbox('Genetic Testing: ', ('Positive', 'Negative'), index=1)
        Neurological = st.selectbox('Neurological Assessments: ', (1, 2, 3), index=1)
        Liver = st.selectbox('Liver Function Tests: ', ('Normal', 'Abnormal'), index=1)
        urine = st.selectbox('Urine Test: ', ('Ketones Present', 'Glucose Present', 'Normal', 'Protein Present'), index=1)

        #define submit button form
        submitted = st.form_submit_button('Predict')



    data = [{
        'Genetic Markers': Gen_mark,
        'Autoantibodies': Autoantibodies,
        'Family History': history,
        'Environmental Factors': Environmental,
        'Insulin Levels': Insulin_Levels,
        'Age': age,
        'BMI': Berat,
        'Physical Activity': Activity,
        'Dietary Habits': habits,
        'Blood Pressure': blood,
        'Cholesterol Levels': kolesterol,
        'Waist Circumference': Waist,
        'Blood Glucose Levels': Blood_Glucose,
        'Ethnicity': etnis,
        'Socioeconomic Factors': Socioeconomic,
        'Smoking Status': Smoking,
        'Alcohol Consumption': Alcohol,
        'Glucose Tolerance Test': Tolerance,
        'History of PCOS': history_pcos,
        'Previous Gestational Diabetes': Gestational,
        'Pregnancy History': Pregnancy,
        'Weight Gain During Pregnancy': Gain_hamil,
        'Pancreatic Health': Pancreatic,
        'Pulmonary Function': Pulmonary,
        'Cystic Fibrosis Diagnosis': Cystic,
        'Steroid Use History': Steroid,
        'Genetic Testing': Genetic,
        'Neurological Assessments': Neurological,
        'Liver Function Tests': Liver,
        'Digestive Enzyme Levels': Enzyme,
        'Urine Test': urine,
        'Birth Weight': Birth_Weight,
        'Early Onset Symptoms': Early
    }]
    
    data_inf = pd.DataFrame(data)
    st.dataframe(data_inf)


    if submitted:
        
        #predict
        y_pred_inf = model.predict(data_inf)

        if y_pred_inf == 1:
            st.write('## Prediction Result : Diabetes Kategori 1 (Neonatal Diabetes Mellitus (NDM), Steroid-Induced Diabetes)')
        elif y_pred_inf == 2:
            st.write('## Prediction Result : Diabetes Kategori 2 (Prediabetic, Type 1 Diabetes, Wolfram Syndrome, LADA)')
        elif y_pred_inf == 3:
            st.write('## Prediction Result : Diabetes Kategori 3 (Type 2 Diabetes)')
        elif y_pred_inf == 4:
            st.write('## Prediction Result : Diabetes Kategori 4 (Wolcott-Rallison Syndrome, Secondary Diabetes)')
        else:
            st.write('## Prediction Result : Diabetes Kategori 5 (Type 3c, Gestational, CFRD, MODY)')

if __name__ == '__main__':
   run()