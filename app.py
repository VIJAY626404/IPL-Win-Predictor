import pickle
import pandas as pd
import streamlit as st

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

# with st.sidebar:
#     st.header("Match Configuration")



pipe = pickle.load(open("pipe.pkl", 'rb'))
st.title("IPL Win Predictor")

col1, col2 = st.columns(2)

with col1:
     batting_team = st.selectbox("Select the batting team", sorted(teams))

with col2:
    bowling_team = st.selectbox("Select the bowling team", sorted(teams))

selected_city = st.selectbox("Select host City", sorted(cities))

target = st.number_input("Target")

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input("Score")
with col4:
    overs = st.number_input("Over completed")
with col5:
    wickets = st.number_input("Wickets out")

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10-wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                  'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],
                  'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")



st.image('vijay.jpg', use_column_width=True)
st.markdown(
    """
    <style>
    .stApp {
        # background: linear-gradient(9deg, rgba(33,36,41,1) 0%, rgba(33,128,198,1) 50%, rgba(0,212,255,1) 100%);
        background: linear-gradient(135deg, #004d00 0%, #008080 30%, #000080 60%, #ff9933 100%);

        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)



