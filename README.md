# IPL Win Predictor 🏏🔮

**A Machine Learning project that predicts the winning probability of teams in the Indian Premier League (IPL) based on various match factors such as score, overs, wickets, and more.** 

  <img src="https://github.com/VIJAY626404/IPL-Win-Predictor/blob/main/team%20logo/ipl1.png" alt="IPL Win Predictor" />
  <img src="https://github.com/VIJAY626404/IPL-Win-Predictor/blob/main/team%20logo/ipl2.png" alt="IPL Win Predictor"  />


---

## Project Overview
The **IPL Win Predictor** utilizes **Logistic Regression** for predicting the chances of a team winning a match based on in-game factors like target runs, current score, overs, and wickets remaining. The project is built with **Streamlit** for the frontend and provides an interactive user interface where users can input match details and get real-time winning probabilities.

This project is divided into several key components including data preprocessing, model building, and deployment using Streamlit.

---

## Features
- **Real-Time Predictions:** Input match details and get instant predictions on the likelihood of a team winning the game.
- **Team Logos:** Displays the winning team's logo alongside the prediction for a more visually engaging experience.
- **Interactive Interface:** The user can interact with the model via a Streamlit application, making it easy and intuitive to use.
  
---

## Tech Stack
- **Python**: Programming language used for model building and data manipulation.
- **Streamlit**: For building the web interface and interactive application.
- **Logistic Regression**: Machine learning model used for making predictions.
- **Pandas**: For data manipulation and analysis.
- **Pickle**: For loading the pre-trained model.
  
---

## File Structure
```plaintext
📦 IPL Win Predictor
 ┣ 📂.idea
 ┣ 📂team logo
 ┃ ┣ 📜(images of winning teams)
 ┣ 📜.gitignore
 ┣ 📜app.py                    # First version of Streamlit application.
 ┣ 📜main.py                   # Updated version with team logos.
 ┣ 📜IPL_Win_Predictor.ipynb    # Jupyter notebook for analysis and model training.
 ┣ 📜pipe.pkl                   # Pre-trained model file.
 ┣ 📜requirements.txt           # List of required libraries.
 ┣ 📜ipl1.png                   # Screenshot of the model interface.
 ┣ 📜ipl2.png                   # Output prediction with winning team image.

```
## Installation and Setup
1. Clone the repository:
   ```
     git clone https://github.com/VIJAY626404/IPL-Win-Predictor.git
   ```
2. Navigate to the project directory:
   ```
   cd IPL-Win-Predictor
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## How It Works
1. **Input Match Details:**
  - Select the batting and bowling teams from the dropdown.
  - Choose the host city.
  - Enter match statistics such as target score, current score, overs completed, and wickets lost.
    
2. **View Predictions:**
  - Click the "Predict Probability" button to see the chances of both teams winning.
  - The app will display the probability percentages for both teams and show the logo of the predicted winning team.

## Model Details
The model is trained using Logistic Regression with the following pipeline:
```
  pipe = Pipeline(steps=[
    ('step1', trf),
    ('step2', LogisticRegression(solver='liblinear'))
])
```
The pipeline takes the input match data, processes it, and predicts the probability of a team winning using the trained model. The model has been fine-tuned to provide accurate predictions based on historical IPL match data.

## Streamlit App (Main Features)
- **Team Selection:** Choose between popular IPL teams like Mumbai Indians, Chennai Super Kings, Kolkata Knight Riders, and more.
- **Host City Selection:** Choose the match's venue from cities like Hyderabad, Bangalore, Mumbai, and others.
- **Live Predictions:** The app predicts the chances of winning in real-time based on in-game conditions like score, wickets, and overs completed.
The app's second version (main.py) includes additional functionality, such as displaying team logos for the predicted winning team.

## Future Enhancements
- **More Detailed Analysis:** Add additional in-game factors like player performance, run rate trends, etc., to make the predictions more accurate.
- **UI/UX Improvements:** Make the app more visually appealing by adding more animations and enhanced graphics.
- **Deployment:** Plan to host the application on a cloud platform for easier access.
  
## Contribution
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
