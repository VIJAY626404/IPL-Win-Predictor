import pickle
import pandas as pd
import streamlit as st

# Correct paths for the team logos stored in the "team logo" folder
team_logos = {
    'Sunrisers Hyderabad': 'team logo/Sunrisers_Hyderabad.png',
    'Mumbai Indians': 'team logo/Mumbai_Indians_Logo.svg.png',
    'Royal Challengers Bangalore': 'team logo/Royal_Challengers_Bangalore_Logo.png',
    'Kolkata Knight Riders': 'team logo/Kolkata_Knight_Riders_Logo.svg.png',
    'Kings XI Punjab': 'team logo/Punjab_Kings_Logo.svg.png',
    'Chennai Super Kings': 'team logo/Chennai_Super_Kings_Logo.svg.png',
    'Rajasthan Royals': 'team logo/Rajasthan_Royals_Logo.png',
    'Delhi Capitals': 'team logo/DC.jpeg'
}

teams = list(team_logos.keys())

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

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
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left
    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team],
                             'city': [selected_city], 'runs_left': [runs_left], 'balls_left': [balls_left],
                             'wickets': [wickets], 'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    st.header(f"{batting_team} - {round(win * 100)}%")
    st.header(f"{bowling_team} - {round(loss * 100)}%")

    # Display the logo of the team with a higher win probability
    if win > loss:
        st.image(team_logos[batting_team], caption=f"Winning Team: {batting_team}", use_column_width=True)
    else:
        st.image(team_logos[bowling_team], caption=f"Winning Team: {bowling_team}", use_column_width=True)

# Optionally, you can retain the background customization
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #004d00 0%, #008080 30%, #000080 60%, #ff9933 100%);
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
