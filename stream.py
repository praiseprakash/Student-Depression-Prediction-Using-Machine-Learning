

# import streamlit as st
# import pandas as pd
# import pickle
# import mysql.connector
# import matplotlib.pyplot as plt
# import plotly.express as px


# conn = mysql.connector.connect(

#     host='localhost',

#     user='root',

#     password='praise@36',

#     database='student_depression'
# )
# cursor = conn.cursor()

# query = "SELECT * FROM predictions"

# df_db = pd.read_sql(query, conn)


# st.set_page_config(
#     page_title="Student Depression Prediction",
#     page_icon="🧠",
#     layout="wide"
# )


# st.markdown("""
# <style>

# /* MAIN BACKGROUND */

# .stApp {

#     background: linear-gradient(
#         135deg,
#         #0f172a,
#         #1e293b,
#         #020617
#     );

#     color: white;
# }


# /* TITLE */

# .main-title {

#     font-size: 50px;

#     font-weight: bold;

#     text-align: center;

#     color: #38bdf8;

#     margin-top: 10px;

#     margin-bottom: 10px;

#     letter-spacing: 2px;
# }


# /* SUBTITLE */

# .sub-title {

#     text-align: center;

#     font-size: 20px;

#     color: #cbd5e1;

#     margin-bottom: 40px;
# }


# /* INPUT LABELS */

# label {

#     font-size: 18px !important;

#     font-weight: 600 !important;

#     color: #f8fafc !important;
# }


# /* SELECT BOX */

# .stSelectbox div[data-baseweb="select"] {

#     background-color: #1e293b;

#     border-radius: 10px;

#     color: white;
# }


# /* NUMBER INPUT */

# .stNumberInput input {

#     background-color: #1e293b !important;

#     color: white !important;

#     border-radius: 10px !important;
# }


# /* SLIDER */

# .stSlider {

#     color: #38bdf8;
# }


# /* BUTTON */

# .stButton button {

#     width: 100%;

#     background: linear-gradient(
#         90deg,
#         #0ea5e9,
#         #2563eb
#     );

#     color: white;

#     font-size: 20px;

#     font-weight: bold;

#     border-radius: 15px;

#     padding: 15px;

#     border: none;

#     transition: 0.3s;
# }


# .stButton button:hover {

#     transform: scale(1.03);

#     background: linear-gradient(
#         90deg,
#         #2563eb,
#         #0ea5e9
#     );
# }


# /* RESULT BOX */

# .result-box {

#     padding: 20px;

#     border-radius: 15px;

#     text-align: center;

#     font-size: 30px;

#     font-weight: bold;

#     margin-top: 30px;
# }


# /* FOOTER */

# .footer {

#     text-align: center;

#     margin-top: 50px;

#     color: #94a3b8;

#     font-size: 15px;
# }

# </style>
# """, unsafe_allow_html=True)



# with open('model.pkl', 'rb') as file:

#     model = pickle.load(file)



# with open('preprocessor.pkl', 'rb') as file:

#     preprocessor = pickle.load(file)



# st.markdown(
#     '<div class="main-title">🧠 STUDENT DEPRESSION PREDICTION SYSTEM</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="sub-title">AI Powered Mental Health Analysis Platform</div>',
#     unsafe_allow_html=True
# )

# # =========================================
# # TWO COLUMNS
# # =========================================

# col1, col2 = st.columns(2)

# # =========================================
# # LEFT COLUMN
# # =========================================

# with col1:

#     gender = st.selectbox(
#         'Gender',
#         ['Male', 'Female']
#     )

#     age = st.number_input(
#         'Age',
#         min_value=10,
#         max_value=100
#     )

#     academic_pressure = st.slider(
#         'Academic Pressure',
#         0,
#         5
#     )

#     study_satisfaction = st.slider(
#         'Study Satisfaction',
#         0,
#         5
#     )

#     work_study_hours = st.slider(
#         'Work/Study Hours',
#         0,
#         12
#     )

# # =========================================
# # RIGHT COLUMN
# # =========================================

# with col2:

#     financial_stress = st.slider(
#         'Financial Stress',
#         0,
#         5
#     )

#     sleep_duration = st.selectbox(
#         'Sleep Duration',
#         [
#             'Less than 5 hours',
#             '5-6 hours',
#             '7-8 hours',
#             'More than 8 hours'
#         ]
#     )

#     dietary_habits = st.selectbox(
#         'Dietary Habits',
#         [
#             'Unhealthy',
#             'Moderate',
#             'Healthy'
#         ]
#     )
#     degree = st.selectbox(
#     'Degree',
#     [
#         'B.Tech',
#         'BSc',
#         'M.Tech',
#         'MCA'
#     ]
# )

#     suicidal_thoughts = st.selectbox(
#         'Suicidal Thoughts',
#         ['Yes', 'No']
#     )

#     family_history = st.selectbox(
#         'Family History of Mental Illness',
#         ['Yes', 'No']
#     )



# original_gender = gender

# original_degree = degree

# original_suicidal = suicidal_thoughts

# original_family = family_history



# gender = 1 if gender == 'Male' else 0

# suicidal_thoughts = 1 if suicidal_thoughts == 'Yes' else 0

# family_history = 1 if family_history == 'Yes' else 0


# degree_mapping = {

#     'B.Tech':0,
#     'BSc':1,
#     'M.Tech':2,
#     'MCA':3
# }

# degree = degree_mapping[degree]


# if st.button('PREDICT DEPRESSION'):

#     input_data = pd.DataFrame({

#         'Gender':[gender],

#         'Age':[age],

#         'Academic Pressure':[academic_pressure],

#         'Study Satisfaction':[study_satisfaction],

#         'Sleep Duration':[sleep_duration],

#         'Dietary Habits':[dietary_habits],

#         'Degree':[degree],

#         'Have you ever had suicidal thoughts ?':[suicidal_thoughts],

#         'Work/Study Hours':[work_study_hours],

#         'Financial Stress':[financial_stress],

#         'Family History of Mental Illness':[family_history]
#     })

#     # =====================================
#     # PREPROCESS
#     # =====================================

#     input_transformed = preprocessor.transform(
#         input_data
#     )

#     # =====================================
#     # PREDICT
#     # =====================================

#     prediction = model.predict(
#         input_transformed
#     )

#     # =====================================
#     # SHOW RESULT
#     # =====================================

#     if prediction[0] == 1:

#         st.markdown(
#             '''
#             <div class="result-box"
#             style="
#             background:#7f1d1d;
#             color:#fecaca;
#             ">
#             ⚠️ HIGH RISK OF DEPRESSION DETECTED
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )

#     else:

#         st.markdown(
#             '''
#             <div class="result-box"
#             style="
#             background:#052e16;
#             color:#bbf7d0;
#             ">
#             ✅ NO DEPRESSION DETECTED
#             </div>
#             ''',
#             unsafe_allow_html=True
#         )
#     query = """

#     INSERT INTO predictions (

#     gender,

#     age,

#     academic_pressure,

#     study_satisfaction,

#     sleep_duration,

#     dietary_habits,

#     degree,

#     work_study_hours,

#     financial_stress,

#     suicidal_thoughts,

#     family_history,

#     prediction)

#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

#     """
#     values = (

#     original_gender,

#     age,

#     academic_pressure,

#     study_satisfaction,

#     sleep_duration,

#     dietary_habits,

#     original_degree,

#     work_study_hours,

#     financial_stress,

#     original_suicidal,

#     original_family,

#     'Depression Detected'

#     if prediction[0] == 1

#     else

#     'No Depression')

#     cursor.execute(query,values)

#     conn.commit()

#     st.subheader('Entered Student Details')

# # =====================================
# # SHOW ENTERED DATA
# # =====================================

#     with st.expander('📋 View Entered Student Details'):

#         show_data = pd.DataFrame({



#             'Gender':[original_gender],

#             'Age':[age],

#             'Academic Pressure':[academic_pressure],

#             'Study Satisfaction':[study_satisfaction],

#             'Sleep Duration':[sleep_duration],

#             'Dietary Habits':[dietary_habits],

#             'Degree':[original_degree],

#             'Work/Study Hours':[work_study_hours],

#             'Financial Stress':[financial_stress],

#             'Suicidal Thoughts':[original_suicidal],

#             'Family History':[original_family],

#             'Prediction':[
                
#                 'Depression Detected'
                
#                 if prediction[0] == 1
                
#                 else
                
#                 'No Depression']
#             })

#         st.dataframe(
#             show_data,
#             use_container_width=True
#         )
# # =========================================
# # FOOTER
# # =========================================



# # # =========================================
# # # LIVE ANALYTICS DASHBOARD
# # # =========================================

# st.markdown('---')

# st.header('📊 Live Analytics Dashboard')

# query = "SELECT * FROM predictions"

# df_db = pd.read_sql(query, conn)

# # TOTAL PREDICTIONS

# st.subheader('Total Predictions')

# st.write(len(df_db))


# # PREDICTION DISTRIBUTION

# prediction_count = df_db['prediction'].value_counts()

# st.subheader('Prediction Distribution')

# # st.bar_chart(prediction_count)
# fig1 = px.pie(

#     names=prediction_count.index,

#     values=prediction_count.values,

#     hole=0.5,

#     title='Prediction Distribution'
# )

# st.plotly_chart(
#     fig1,
#     use_container_width=True
# )

# # GENDER DISTRIBUTION

# gender_count = df_db['gender'].value_counts()

# st.subheader('Gender Distribution')

# # st.bar_chart(gender_count)
# fig2 = px.bar(

#     x=gender_count.index,

#     y=gender_count.values,

#     title='Gender Distribution'
# )

# st.plotly_chart(
#     fig2,
#     use_container_width=True
# )



# # FINANCIAL STRESS

# stress_count = df_db['financial_stress'].value_counts()

# st.subheader('Financial Stress Levels')

# # st.bar_chart(stress_count)
# fig3 = px.bar(

#     x=stress_count.index,

#     y=stress_count.values,

#     title='Financial Stress Levels'
# )

# st.plotly_chart(
#     fig3,
#     use_container_width=True
# )



# # HISTORY TABLE

# st.subheader('📋 Prediction History')

# st.dataframe(df_db)



# st.markdown(
#     '''
#     <div class="footer">
#     Developed using Machine Learning & Streamlit
#     </div>
#     ''',
#     unsafe_allow_html=True
# )






# _______________________________________________________________________________________



import streamlit as st
import pandas as pd
import pickle
import mysql.connector
import plotly.express as px



st.set_page_config(
    page_title="Student Depression Prediction",
    page_icon="🧠",
    layout="wide"
)



conn = mysql.connector.connect(

    host='localhost',

    user='root',

    password='praise@36',

    database='student_depression'
)

cursor = conn.cursor()



with open('model.pkl', 'rb') as file:

    model = pickle.load(file)

with open('preprocessor.pkl', 'rb') as file:

    preprocessor = pickle.load(file)



st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {

    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #1e293b
    );

    color: white;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: #020617;
}


/* TITLE */

.main-title {

    text-align: center;

    font-size: 48px;

    font-weight: bold;

    color: #38bdf8;

    margin-top: 10px;

    letter-spacing: 2px;
}


/* SUBTITLE */

.sub-title {

    text-align: center;

    font-size: 18px;

    color: #cbd5e1;

    margin-bottom: 35px;
}


/* METRIC CARDS */

[data-testid="metric-container"] {

    background: linear-gradient(
        135deg,
        #1e293b,
        #0f172a
    );

    border: 1px solid #334155;

    padding: 20px;

    border-radius: 20px;

    text-align: center;

    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
}


/* INPUT LABELS */

label {

    font-size: 17px !important;

    font-weight: 600 !important;

    color: white !important;
}


/* SELECT BOX */

.stSelectbox div[data-baseweb="select"] {

    background-color: #1e293b;

    border-radius: 12px;

    color: white;
}


/* NUMBER INPUT */

.stNumberInput input {

    background-color: #1e293b !important;

    color: white !important;

    border-radius: 12px !important;
}


/* BUTTON */

.stButton button {

    width: 100%;

    background: linear-gradient(
        90deg,
        #0ea5e9,
        #2563eb
    );

    color: white;

    font-size: 20px;

    font-weight: bold;

    border-radius: 15px;

    padding: 14px;

    border: none;

    transition: 0.3s;
}


.stButton button:hover {

    transform: scale(1.02);
}


/* RESULT BOX */

.result-box {

    padding: 20px;

    border-radius: 18px;

    text-align: center;

    font-size: 28px;

    font-weight: bold;

    margin-top: 25px;

    margin-bottom: 20px;
}


/* FOOTER */

.footer {

    text-align: center;

    margin-top: 40px;

    color: #94a3b8;

    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)



st.sidebar.title("🧠 Dashboard")

page = st.sidebar.radio(

    "Navigation",

    [

        "Prediction System",

        "Analytics Dashboard"
    ]
)



st.markdown(
    '<div class="main-title">🧠 STUDENT DEPRESSION PREDICTION SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI Powered Mental Health Analysis Platform</div>',
    unsafe_allow_html=True
)



if page == "Prediction System":

    col1, col2 = st.columns(2)

  

    with col1:

        gender = st.selectbox(

            'Gender',

            ['Male', 'Female']
        )

        age = st.number_input(

            'Age',

            min_value=10,

            max_value=100
        )

        academic_pressure = st.slider(

            'Academic Pressure',

            0,

            5
        )

        study_satisfaction = st.slider(

            'Study Satisfaction',

            0,

            5
        )

        work_study_hours = st.slider(

            'Work/Study Hours',

            0,

            12
        )


    with col2:

        financial_stress = st.slider(

            'Financial Stress',

            0,

            5
        )

        sleep_duration = st.selectbox(

            'Sleep Duration',

            [

                'Less than 5 hours',

                '5-6 hours',

                '7-8 hours',

                'More than 8 hours'
            ]
        )

        dietary_habits = st.selectbox(

            'Dietary Habits',

            [

                'Unhealthy',

                'Moderate',

                'Healthy'
            ]
        )

        degree = st.selectbox(

            'Degree',

            [

                'B.Tech',

                'BSc',

                'M.Tech',

                'MCA'
            ]
        )

        suicidal_thoughts = st.selectbox(

            'Suicidal Thoughts',

            ['Yes', 'No']
        )

        family_history = st.selectbox(

            'Family History of Mental Illness',

            ['Yes', 'No']
        )

  

    original_gender = gender

    original_degree = degree

    original_suicidal = suicidal_thoughts

    original_family = family_history

    

    gender = 1 if gender == 'Male' else 0

    suicidal_thoughts = 1 if suicidal_thoughts == 'Yes' else 0

    family_history = 1 if family_history == 'Yes' else 0

    degree_mapping = {

        'B.Tech':0,

        'BSc':1,

        'M.Tech':2,

        'MCA':3
    }

    degree = degree_mapping[degree]

    

    if st.button('PREDICT DEPRESSION'):

        input_data = pd.DataFrame({

            'Gender':[gender],

            'Age':[age],

            'Academic Pressure':[academic_pressure],

            'Study Satisfaction':[study_satisfaction],

            'Sleep Duration':[sleep_duration],

            'Dietary Habits':[dietary_habits],

            'Degree':[degree],

            'Have you ever had suicidal thoughts ?':[suicidal_thoughts],

            'Work/Study Hours':[work_study_hours],

            'Financial Stress':[financial_stress],

            'Family History of Mental Illness':[family_history]
        })

        

        input_transformed = preprocessor.transform(

            input_data
        )

     

        prediction = model.predict(

            input_transformed
        )




        probability = model.predict_proba(

        input_transformed)

        risk_percentage = probability[0][1] * 100

      

        if prediction[0] == 1:

            result_text = "Depression Detected"

            st.markdown(

                '''
                <div class="result-box"
                style="
                background:#7f1d1d;
                color:#fecaca;
                ">
                ⚠️ HIGH RISK OF DEPRESSION DETECTED
                </div>
                ''',

                unsafe_allow_html=True
            )

        else:

            result_text = "No Depression"

            st.markdown(

                '''
                <div class="result-box"
                style="
                background:#052e16;
                color:#bbf7d0;
                ">
                ✅ NO DEPRESSION DETECTED
                </div>
                ''',

                unsafe_allow_html=True
            )
        st.markdown("### Depression Risk Percentage")

        st.progress(
        int(risk_percentage))

        st.metric("Depression Risk",
        f"{risk_percentage:.2f}%"
)

      

        query = """

        INSERT INTO predictions (

        gender,

        age,

        academic_pressure,

        study_satisfaction,

        sleep_duration,

        dietary_habits,

        degree,

        work_study_hours,

        financial_stress,

        suicidal_thoughts,

        family_history,

        prediction

        )

        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

        """

        values = (

            original_gender,

            age,

            academic_pressure,

            study_satisfaction,

            sleep_duration,

            dietary_habits,

            original_degree,

            work_study_hours,

            financial_stress,

            original_suicidal,

            original_family,

            result_text
        )

        cursor.execute(query, values)

        conn.commit()

       

        with st.expander('📋 View Entered Student Details'):

            show_data = pd.DataFrame({

                'Gender':[original_gender],

                'Age':[age],

                'Academic Pressure':[academic_pressure],

                'Study Satisfaction':[study_satisfaction],

                'Sleep Duration':[sleep_duration],

                'Dietary Habits':[dietary_habits],

                'Degree':[original_degree],

                'Work/Study Hours':[work_study_hours],

                'Financial Stress':[financial_stress],

                'Suicidal Thoughts':[original_suicidal],

                'Family History':[original_family],

                'Prediction':[result_text]
            })

            st.dataframe(

                show_data,

                use_container_width=True
            )



if page == "Analytics Dashboard":

    st.header("📊 Analytics Dashboard")

    query = "SELECT * FROM predictions"

    df_db = pd.read_sql(query, conn)

    

    total_predictions = len(df_db)

    depression_count = len(

        df_db[
            df_db['prediction'] == 'Depression Detected'
        ]
    )

    no_depression_count = len(

        df_db[
            df_db['prediction'] == 'No Depression'
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Total Predictions",

            total_predictions
        )

    with col2:

        st.metric(

            "Depression Cases",

            depression_count
        )

    with col3:

        st.metric(

            "Healthy Cases",

            no_depression_count
        )

    

    prediction_count = df_db['prediction'].value_counts()

    gender_count = df_db['gender'].value_counts()

    stress_count = df_db['financial_stress'].value_counts()

   

    fig1 = px.pie(

        names=prediction_count.index,

        values=prediction_count.values,

        hole=0.6,

        title='Prediction Distribution'
    )

    fig1.update_layout(height=350)

    fig2 = px.bar(

        x=gender_count.index,

        y=gender_count.values,

        title='Gender Distribution'
    )

    fig2.update_layout(height=350)

    fig3 = px.bar(

        x=stress_count.index,

        y=stress_count.values,

        title='Financial Stress Levels'
    )

    fig3.update_layout(height=350)

   

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(

            fig1,

            use_container_width=True,

            key='prediction_chart'
        )

    with col2:

        st.plotly_chart(

            fig2,

            use_container_width=True,

            key='gender_chart'
        )

   

    st.plotly_chart(

        fig3,

        use_container_width=True,

        key='stress_chart'
    )

   

    st.subheader("📋 Prediction History")

    st.dataframe(

        df_db,

        use_container_width=True,

        height=300
    )



st.markdown(

    '''
    <div class="footer">
    Developed using Machine Learning, Streamlit & MySQL
    </div>
    ''',

    unsafe_allow_html=True
)

