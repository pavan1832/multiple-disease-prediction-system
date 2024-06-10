import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Function to show main page header
def show_main_page():
    st.subheader('We Care Hospitals')
    st.title('Successfully Logged in')
    
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open("parkinsons_model.sav", "rb"))

# Display main page header
show_main_page()

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

def show_main_page():
    st.title('Successfully logged in')

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    gender = st.selectbox('Gender', ['Female', 'Male'])
    
    if gender == 'Female':
        with st.form(key='diabetes_form_female'):
            pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
            glucose = st.number_input('Glucose Level',min_value=0.0)
            blood_pressure = st.number_input('Blood Pressure value',min_value=0.0)
            skin_thickness = st.number_input('Skin Thickness value',min_value=0.0)
            insulin = st.number_input('Insulin Level',min_value=0.0)
            bmi = st.number_input('BMI value',min_value=0.0)
            diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value',min_value=0.0)
            age = st.number_input('Age of the Person', min_value=0, step=1)

            submitted = st.form_submit_button('Diabetes Test Result')

        if submitted:
            if any([age == 0]):
                st.warning('Please fill in all details to get the Diabetes test result.')
            else:
                user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
                diab_prediction = diabetes_model.predict([user_input])
                if diab_prediction[0] == 1:
                    st.success('The person is diabetic')
                else:
                    st.success('The person is not diabetic')

    elif gender == 'Male':
       
        pregnancies = 0
        with st.form(key='diabetes_form_male'):
            glucose = st.number_input('Glucose Level',min_value=0.0)
            blood_pressure = st.number_input('Blood Pressure value',min_value=0.0)
            skin_thickness = st.number_input('Skin Thickness value',min_value=0.0)
            insulin = st.number_input('Insulin Level',min_value=0.0)
            bmi = st.number_input('BMI value',min_value=0.0)
            diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value',min_value=0.0)
            age = st.number_input('Age of the Person', min_value=0, step=1)

            submitted = st.form_submit_button('Diabetes Test Result')

        if submitted:
            if any([age == 0]):
                st.warning('Please fill in all details to get the Diabetes test result.')
            else:
                user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
                diab_prediction = diabetes_model.predict([user_input])
                if diab_prediction[0] == 1:
                    st.success('The person is diabetic')
                else:
                    st.success('The person is not diabetic')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    with st.form(key='heart_disease_form'):
        age = st.number_input('Age', min_value=0, step=1)
        sex = st.selectbox('Sex', ['Male', 'Female'])
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0)
        chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=0)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', ['No', 'Yes'])
        restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0)
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0)
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy (0-3)', min_value=0, max_value=3, step=1)
        thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

        submitted = st.form_submit_button('Heart Disease Test Result')

    if submitted:
        if any([age == 0]):
            st.warning('Please fill in all required details to get the Heart Disease test result.')
        else:
            sex_encoded = 1 if sex == 'Male' else 0
            cp_encoded = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'].index(cp)
            fbs_encoded = 1 if fbs == 'Yes' else 0
            restecg_encoded = ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'].index(restecg)
            exang_encoded = 1 if exang == 'Yes' else 0
            slope_encoded = ['Upsloping', 'Flat', 'Downsloping'].index(slope)
            thal_encoded = ['Normal', 'Fixed Defect', 'Reversible Defect'].index(thal)

            user_input = [age, sex_encoded, cp_encoded, trestbps, chol, fbs_encoded, restecg_encoded, thalach, exang_encoded, oldpeak, slope_encoded, ca, thal_encoded]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                st.success('The person is diagnosed with heart disease.')
            else:
                st.success('The person does not have heart disease.')

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Prediction using ML")

    with st.form(key='parkinsons_form'):
        jil = st.number_input('Jitter (local)', format="%.2f")
        jia = st.number_input('Jitter (local, absolute)', format="%.2f")
        ji_rap = st.number_input('Jitter (rap)', format="%.5f")
        ji_ppq = st.number_input('Jitter (ppq5)', format="%.2f")
        ddp = st.number_input('Jitter (ddp)', format="%.2f")
        shi_loc = st.number_input('Shimmer (local)', format="%.2f")
        shi_db = st.number_input('Shimmer (local, dB)', format="%.2f")
        shi_apq3 = st.number_input('Shimmer (apq3)', format="%.2f")
        shi_apq5 = st.number_input('Shimmer (apq5)', format="%.2f")
        shi_apq11 = st.number_input('Shimmer (apq11)', format="%.2f")
        shi_dda = st.number_input('Shimmer (dda)', format="%.2f")
        ac = st.number_input('AC', format="%.2f")
        nth = st.number_input('NTH', format="%.2f")
        htn = st.number_input('HTN', format="%.2f")
        med = st.number_input('Median pitch', format="%.2f")
        men = st.number_input('Mean pitch', format="%.2f")
        sta_dev = st.number_input('Standard Deviation', format="%.2f")
        min_pit = st.number_input('Minimum Pitch', format="%.2f")
        max_pit = st.number_input('Maximum Pitch', format="%.2f")
        no = st.number_input('Number of Pulses', format="%.2f")
        no_per = st.number_input('Number of Periods', format="%.2f")
        me_per = st.number_input('Mean Periods', format="%.2f")
        sta = st.number_input('Standard deviation of period', format="%.6f")
        fra = st.number_input('Fraction of locally unvoiced frames', format="%.6f")
        no_vb = st.number_input('Number of voice breaks', format="%.2f")
        deg = st.number_input('Degree of voice breaks', format="%.2f")
        updrs = st.number_input('UPDRS column', format="%.2f")
        class_info = st.number_input('Class information', format="%.2f")

        submitted = st.form_submit_button("Click here to view results")

    parkinsons_diagnosis = ''
    if submitted:
        user_input = [jil, jia, ji_rap, ji_ppq, ddp, shi_loc, shi_db, shi_apq3, shi_apq5, shi_apq11, shi_dda, ac, nth, htn, med, men, sta_dev, min_pit, max_pit, no, no_per, me_per, sta, fra, no_vb, deg, updrs, class_info]
        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
