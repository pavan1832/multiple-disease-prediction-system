import pickle
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from streamlit_option_menu import option_menu

def show_main_page():
   st.subheader('We Care Hospitals')
   st.title('Sucessfully Logged in')
    

diabetes_model = pickle.load(open("C:/Users/Pavan/OneDrive/Desktop/multiple decision system/saved models/diabetes_model.sav","rb"))
heart_disease_model = pickle.load(open("C:/Users/Pavan/OneDrive/Desktop/multiple decision system/saved models/heart_disease_model.sav","rb"))
parkinsons_model= pickle.load(open("C:/Users/Pavan/OneDrive/Desktop/multiple decision system/saved models/parkinsons_model.sav","rb"))

def generate_pdf(diagnosis):
    c = canvas.Canvas("diagnosis_result.pdf", pagesize=letter)
    c.drawString(100, 750, "Diagnosis Result:")
    c.drawString(100, 730, diagnosis)
    c.save()
#sidebar
show_main_page()
# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

 # Creating a button for printing the result
    if st.button('Print Result'):
        generate_pdf(diab_diagnosis)

    # Creating a download link for the generated PDF
    st.markdown("[Download PDF](diagnosis_result.pdf)")
 
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

   

    with col1:
        jil = st.text_input('Jitter(local)')

    with col2:
        jia = st.text_input('Jitter(local,absolute)')

    with col3:
        ji_rap = st.text_input('Jitter(rap)')

    with col4:
        ji_ppq = st.text_input('Jitter(ppq5)')

    with col5:
        ddp = st.text_input('Jitter (ddp)')

    with col1:
        shi_loc = st.text_input('Shimmer (local)')

    with col2:
        shi_db = st.text_input('Shimmer (local, dB)')

    with col3:
        Shi_apq3 = st.text_input('Shimmer (apq3)')

    with col4:
        Shi_apq5 = st.text_input('Shimmer (apq5)')

    with col5:
        shi_apq11 = st.text_input('Shimmer (apq11)')

    with col1:
        shi_dda = st.text_input('Shimmer (dda)')

    with col2:
        ac = st.text_input('AC')

    with col3:
        nth = st.text_input('NTH')

    with col4:
        htn = st.text_input('HTN')

    with col5:
        med = st.text_input('Median pitch')

    with col1:
        men = st.text_input('Mean pitch')

    with col2:
        sta_dev = st.text_input('Standard Deviation')

    with col3:
        min_pit = st.text_input('Minimum Pitch')

    with col4:
        max_pit = st.text_input('Maximum Pitch')

    with col5:
        no = st.text_input('Number of Pulses')

    with col1:
        no_per = st.text_input('Number of Periods')
        
        with col2:
            me_per= st.text_input('Mean Periods')
            
            with col3:
                sta = st.text_input('Standard deviation of period')
                
                 
            with col4:
                fra = st.text_input(' Fraction of locally unvoiced frames')
                
                 
            with col5:
                no_vb = st.text_input('Number of voice breaks')
                 
                      
            with col1:
                deg= st.text_input('degree of voice breaks')
                 
            with col2:
                updrs = st.text_input('UPDRS column')
                 
            with col3:
                class_info = st.text_input(' class information')
                


    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [jil,jia,ji_rap,ji_ppq,ddp,shi_loc,shi_db,Shi_apq3,Shi_apq5,shi_apq11,shi_dda,ac,nth,htn,med,men,sta_dev,min_pit,max_pit,no,no_per,me_per,sta,fra,no_vb,deg,updrs,class_info]

        user_input = [float(x) for x in user_input]
    
        
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
