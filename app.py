import streamlit as st
import pickle

# Load the gestation model
with open("knn.pkl", "rb") as pickle_in_gestation:
    knn_gest = pickle.load(pickle_in_gestation)

# Load the heart disease model
with open('rf_model.pkl', 'rb') as model_file:
    loaded_rf_model = pickle.load(model_file)

# Load the diabetic kidney disease model
with open('rfdkd_model1.pkl', 'rb') as model_file:
    dkd = pickle.load(model_file)
    
with open('Diabetes_model.pkl', 'rb') as model_file:
    diabetes = pickle.load(model_file)

# Set page configurations
st.set_page_config(
    page_title="Arogya Vicharana",
    page_icon=":clipboard:",
    layout="wide",
)

def predict_gestation_diabetes(age, pregnancies, gestation_previous, bmi, hdl, family_history, unexplained_prenatal_loss, large_child_birth_default, pcos, sys_bp, dia_bp, ogtt, hemoglobin, sedentary_lifestyle, prediabetes):
    try:
        # Convert input values to appropriate types
        age = int(age)
        pregnancies = int(pregnancies)
        gestation_previous = int(gestation_previous)
        bmi = float(bmi)
        hdl = int(hdl)
        family_history = int(family_history)
        unexplained_prenatal_loss = int(unexplained_prenatal_loss)
        large_child_birth_default = int(large_child_birth_default)
        pcos = int(pcos)
        sys_bp = float(sys_bp)
        dia_bp = float(dia_bp)
        ogtt = int(ogtt)
        hemoglobin = float(hemoglobin)
        sedentary_lifestyle = int(sedentary_lifestyle)
        prediabetes = int(prediabetes)

        # Use numpy array for prediction
        input_values = [age, pregnancies, gestation_previous, bmi, hdl, family_history, unexplained_prenatal_loss, large_child_birth_default, pcos, sys_bp, dia_bp, ogtt, hemoglobin, sedentary_lifestyle, prediabetes]
        prediction = knn_gest.predict([input_values])

        return prediction[0]  # Return the first element as a scalar
    except ValueError as e:
        return "Invalid input. Please provide valid numeric values for all input fields."

def predict_heart_disease(gender, age, hypertension, smoking_history, bmi, hba1c_level, blood_glucose_level, diabetes):
    try:
        # Convert input values to appropriate types
        gender = int(gender)
        age = int(age)
        hypertension = int(hypertension)
        smoking_history = int(smoking_history)
        bmi = float(bmi)
        hba1c_level = float(hba1c_level)
        blood_glucose_level = int(blood_glucose_level)
        diabetes = int(diabetes)

        # Use numpy array for prediction
        input_values = [gender, age, hypertension, smoking_history, bmi, hba1c_level, blood_glucose_level, diabetes]
        prediction = loaded_rf_model.predict([input_values])

        return prediction[0]  # Return the first element as a scalar
    except ValueError as e:
        return "Invalid input. Please provide valid numeric values for all input fields."

def predict_dkd_risk(sex, age, diabetes_duration, diabetic_retinopathy, smoking, drinking, bmi, sbp, dbp, hba1c, fbG, c_peptide, hdLc, ldLc, insulin):
    try:
        # Convert input values to appropriate types
        sex = int(sex)
        age = int(age)
        diabetes_duration = int(diabetes_duration)
        diabetic_retinopathy = int(diabetic_retinopathy)
        smoking = float(smoking)
        drinking = float(drinking)
        # weight = float(weight)
        bmi = float(bmi)
        sbp = float(sbp)
        dbp = float(dbp)
        hba1c = float(hba1c)
        fbG = float(fbG)
        c_peptide = float(c_peptide)
        hdLc = int(hdLc)
        ldLc = int(ldLc)
        insulin = int(insulin)

        input_values2 = [sex, age, diabetes_duration, diabetic_retinopathy, smoking, drinking, bmi, sbp, dbp, hba1c, fbG, c_peptide, hdLc, ldLc, insulin]
        prediction = dkd.predict([input_values2])

        return prediction[0]  # Return the first element as a scalar
    except ValueError as e:
        return "Invalid input. Please provide valid numeric values for all input fields."

def predict_diabetes_risk(age, BMI, FPG, FFPG, SBP, DBP, family_history, smoking, drinking, ALT):
    try:
        # Convert input values to appropriate types
        age = int(age)
        BMI = float(BMI)
        FPG = float(FPG)
        FFPG = float(FFPG)
        SBP = float(SBP)
        DBP = float(DBP)
        family_history = int(family_history)
        smoking = float(smoking)
        drinking = float(drinking)
        ALT = int(ALT)

        input_values = [age, BMI, FPG, FFPG, SBP, DBP, family_history, smoking, drinking, ALT]
        # Replace the next line with your prediction function/method
        prediction = diabetes.predict([input_values])

        return prediction[0]  # Return the first element as a scalar
    except ValueError as e:
        return "Invalid input. Please provide valid numeric values for all input fields."



def main():
    st.title("Arogya Vicharana")

    # Sidebar for navigation
    selected = st.sidebar.selectbox(
        "AROGYA VICHARANA",
        ['Diabetes Prediction', 'Diabetes Cardiomyopathy Prediction', 'Gestational Diabetes Prediction', 'Diabetic Nephropathy Prediction'],
    )

    if selected == "Gestational Diabetes Prediction":
        st.header("Gestational Diabetes Prediction")
        
        # Create three columns
        col1, col2, col3 = st.columns(3)

        # Input elements for col1
        age = col1.number_input("Age", min_value=0, max_value=100, help="Enter 1 if male, 0 if female",key="age")
        No_of_Pregnancy = col1.number_input("No_of_Pregnancy", min_value=0, max_value=10, key="No_of_Pregnancy", placeholder="Type Here")
        Gestation_in_previous_Pregnancy = col1.number_input("Gestation_in_previous_Pregnancy", min_value=0, max_value=100, key="Gestation_in_previous_Pregnancy", placeholder="Type Here")
        BMI = col1.number_input("BMI", min_value=10.0, max_value=40.0, key="BMI", placeholder="Type Here")
        HDL = col1.number_input("HDL", min_value=20, max_value=100, key="HDL", placeholder="Type Here")

        # Input elements for col2
        Family_History = col2.number_input("Family_History", min_value=0, max_value=1, key="Family_History", placeholder="Type Here")
        unexplained_prenatal_loss = col2.number_input("unexplained_prenatal_loss", min_value=0, max_value=10, key="unexplained_prenatal_loss", placeholder="Type Here")
        Large_Child_or_Birth_Default = col2.number_input("Large_Child_or_Birth_Default", min_value=0, max_value=1, key="Large_Child_or_Birth_Default", placeholder="Type Here")
        PCOS = col2.number_input("PCOS", min_value=0, max_value=1, key="PCOS", placeholder="Type Here")
        Sys_BP = col2.number_input("Sys_BP", min_value=80, max_value=180, key="Sys_BP", placeholder="Type Here")

        # Input elements for col3
        Dia_BP = col3.number_input("Dia_BP", min_value=50, max_value=120, key="Dia_BP", placeholder="Type Here")
        OGTT = col3.number_input("OGTT", min_value=50, max_value=300, key="OGTT", placeholder="Type Here",help="Oral Glucose Tolerance Test")
        Hemoglobin = col3.number_input("Hemoglobin", min_value=10.0, max_value=20.0, key="Hemoglobin", placeholder="Type Here")
        Sedentary_Lifestyle = col3.number_input("Sedentary_Lifestyle", min_value=0, max_value=1, key="Sedentary_Lifestyle", placeholder="Type Here")
        Prediabetes = col3.number_input("Prediabetes", min_value=0, max_value=1, key="Prediabetes", placeholder="Type Here")

        result = ""
        if st.button("Predict"):
            result = predict_gestation_diabetes(age, No_of_Pregnancy, Gestation_in_previous_Pregnancy, BMI, HDL, Family_History, unexplained_prenatal_loss, Large_Child_or_Birth_Default, PCOS, Sys_BP, Dia_BP, OGTT, Hemoglobin, Sedentary_Lifestyle, Prediabetes)

        if result == 0:
            st.success('No Gestation diabetes, you are safe')
        elif result == 1:
            st.error('Yes, you have Gestation diabetes. Please consult a doctor')
        else:
            st.warning('Enter valid input values')
    
    elif selected == "Diabetes Cardiomyopathy Prediction":
        st.header("Diabetes Cardiomyopathy Prediction")

        # Create three columns
        col1, col2, col3 = st.columns(3)

        # Input elements for col1
        gender = col1.number_input("Gender", min_value=0, max_value=100, help="Enter 1 if male, 0 if female",key="gender")
        age1 = col1.number_input("Age", min_value=0, max_value=100, key="age")
        hypertension = col1.number_input("Hypertension", min_value=0, max_value=1, key="hypertension")

        # Input elements for col2
        smoking_history = col2.number_input("Smoking History", min_value=0, max_value=4, key="smoking_history",
                                            help="never=4, no_info=0, current=1, former=3")
        bmi = col2.number_input("BMI", min_value=10.0, max_value=40.0, key="bmi")
        HbA1c_level = col2.number_input("HbA1c Level", min_value=4.0, max_value=10.0, key="HbA1c_level",help="Hemoglobin A1c is a measure of average blood glucose over the past 2-3 months.")

        # Remaining input elements for col3
        blood_glucose_level = col3.number_input("Blood Glucose Level", min_value=50, max_value=300, key="blood_glucose_level")
        diabetes = col3.number_input("Diabetes", min_value=0, max_value=1, key="diabetes")

        result = ""
        if st.button("Predict", key="predict_button"):
            result = predict_heart_disease(gender, age1, hypertension, smoking_history, bmi, HbA1c_level,
                                            blood_glucose_level, diabetes)
        if result == 0:
            st.success('No Heart Disease, you are safe')
        elif result == 1:
            st.error('Yes, you have Heart Disease. Please consult a doctor')
        else:
            st.warning('Enter valid input values')

    elif selected == "Diabetic Nephropathy Prediction":
        st.header("Diabetic Nephropathy Prediction")

        col1, col2, col3, col4 = st.columns(4)  # Use beta_columns for Streamlit version 1.0.0 and later

    # Get input from the user
        with col1:
         sex = st.number_input("Sex", min_value=0, max_value=1, help="Enter 1 if male, 0 if female", value=1)
         age = st.number_input("Age", min_value=24, max_value=88, value=57)
         diabetes_duration = st.number_input("Diabetes duration (y)", min_value=0, max_value=32, key="diabetes_duration", help="Enter diabetes duration", value=10)
         diabetic_retinopathy = st.number_input("Diabetic Retinopathy", min_value=0, max_value=1, value=1)

        with col2:
         smoking = st.number_input("Smoking", min_value=0, max_value=1, value=1)
         drinking = st.number_input("Drinking", min_value=0, max_value=1, value=0)
        #  weight = st.number_input("Weight (kg)", min_value=42.0, max_value=122.0, value=60.0)
         bmi = st.number_input("BMI (kg/m2)", min_value=16.0, max_value=63.0, value=18.94,help="Body Mass Index")
         sbp = st.number_input("SBP (mmHg)", min_value=92.0, max_value=218.0, value=101.0,help="Systolic Blood Pressure is the higher of the two numbers measured when blood pressure is taken.")

        with col3:    
         dbp = st.number_input("DBP (mmHg)", min_value=50.0, max_value=210.0, value=69.0,help="Diastolic Blood Pressure is the lower of the two numbers measured.")
         hba1c = st.number_input("HbA1c (%)", min_value=1.0, max_value=15.0, value=14.10,help="Hemoglobin A1c is a measure of average blood glucose over the past 2-3 months.")
         fbG = st.number_input("FBG (mmol/L)", min_value=1.0, max_value=22.0, value=17.42,help="Fasting Blood Glucose is the concentration of glucose in the blood after an overnight fast.")
         c_peptide = st.number_input("C-peptide (ng/ml)", min_value=0.0, max_value=9.0, value=0.98,help="C-peptide is a substance formed when insulin is produced in the pancreas.")
         
        with col4:   
         hdLc = st.number_input("HDLC (mmol/L)", min_value=1.0, max_value=3.0, value=1.08,help="High-Density Lipoprotein Cholesterol is often referred to as 'good' cholesterol.")
         ldLc = st.number_input("LDLC (mmol/L)", min_value=0.0, max_value=195.0, value=3.71, help="Low-Density Lipoprotein Cholesterol is often referred to as 'bad' cholesterol.")
         insulin = st.number_input("Insulin", min_value=0, max_value=1, value=1,help="Insulin status (0 for non-insulin, 1 for insulin)")

        result = ""
        predict_button = st.button("Predict")
        if predict_button:
           result = predict_dkd_risk(sex, age, diabetes_duration, diabetic_retinopathy, smoking, drinking, bmi, sbp, dbp, hba1c, fbG, c_peptide, hdLc, ldLc, insulin)

        if result == 0:
           st.success('No Kidney Disease, you are safe')
        elif result == 1:
           st.error('Yes, you have Kidney disease. Please consult a doctor')
        else:
           st.warning('Enter valid input values')


    if selected == "Diabetes Prediction":
        st.header("Diabetes Prediction")
        
        # Create three columns
        col1, col2, col3 = st.columns(3)

        # Input elements for col1
        age = col1.number_input("Age", min_value=0, max_value=100, key="age")
        BMI = col1.number_input("BMI", min_value=10.0, max_value=40.0, key="BMI", placeholder="Type Here",help="Body Mass Index")
        FPG = col1.number_input("FPG", min_value=0.0, max_value=200.0, key="FPG", placeholder="Type Here",help="Fasting Plasma Glucose")
        FFPG = col2.number_input("FFPG", min_value=0.0, max_value=200.0, key="FFPG", placeholder="Type Here",help="Fasting and Postprandial Plasma Glucose")
        SBP = col2.number_input("SBP", min_value=80, max_value=180, key="SBP", placeholder="Type Here",help="Systolic Blood Pressure",)
        DBP = col2.number_input("DBP", min_value=50, max_value=120, key="DBP", placeholder="Type Here",help="Diastolic Blood Pressure")

        # Input elements for col2
        family_history = col2.number_input("Family History", min_value=0.0, max_value=5.0, key="family_history", placeholder="Type Here")
        smoking = col3.number_input("Smoking", min_value=0.0, max_value=7.0, key="smoking", placeholder="Type Here")
        drinking = col3.number_input("Drinking", min_value=0.0, max_value=7.0, key="drinking", placeholder="Type Here")
        ALT = col3.number_input("ALT", min_value=0.0, max_value=100.0, key="ALT", placeholder="Type Here",help="Alanine Transaminase")


        result = ""
        if st.button("Predict"):
            result = predict_diabetes_risk(age, BMI, FPG, FFPG, SBP, DBP, family_history, smoking, drinking, ALT)

        if result == 0:
            st.success('No Diabetes, you are safe')
        elif result == 1:
            st.error('Yes, you have Diabetes. Please consult a doctor')
        else:
            st.warning('Enter valid input values')

if __name__ == '__main__':
    main()
