# mini_pj_3
🧠 Disease Prediction Dashboard built with Streamlit to predict CKD, Liver Disease, and Parkinson's Disease using ML. Enter patient data and get instant predictions with a clean UI and customizable theme.


🧠 Disease Prediction Dashboard
A simple and interactive Streamlit web app to predict the likelihood of Chronic Kidney Disease, Liver Disease, and Parkinson's Disease using Machine Learning.

🔍 Features
Input patient data easily through the UI

Real-time disease prediction

Clean and responsive design

Theme customizable via config.toml

🧪 Diseases Covered
🩺 Chronic Kidney Disease (CKD)

🩸 Liver Disease

🧬 Parkinson's Disease

⚙️ Tech Stack
Python

Streamlit

Scikit-learn

Pandas

Joblib

🚀 How to Run
bash
Copy
Edit
git clone https://github.com/raguchinnaiyan/mini_pj_3.git
cd mini_pj_3
streamlit run Home_page.py
📁 Project Structure
arduino
Copy
Edit
📦mini_pj_3
 ┣ .streamlit/
 ┃ ┗ config.toml
 ┣ pages/
 ┃ ┣ 1_Kidney.py
 ┃ ┣ 2_Liver.py
 ┃ ┗ 3_Parkinson.py
 ┣ models/
 ┃ ┗ your_models.pkl
 ┣ Home_page.py
 ┗ requirements.txt
