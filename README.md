# mini_pj_3
🧠 Disease Prediction Dashboard built with Streamlit to predict CKD, Liver Disease, and Parkinson's Disease using ML. Enter patient data and get instant predictions with a clean UI and customizable theme.

🔍 Features Input patient data easily through the UI Real-time disease prediction Clean and responsive design Theme customizable via config.toml

🧪 Diseases Covered 🩺 Chronic Kidney Disease (CKD) 🩸 Liver Disease 🧬 Parkinson's Disease

⚙️ Tech Stack Python Streamlit Scikit-learn Pandas Joblib

🚀 How to Run

git clone https://github.com/raguchinnaiyan/mini_pj_3.git cd mini_pj_3 streamlit run Home_page.py

📁 Project Structure 

```
📦 mini_pj_3
├── 📁 .streamlit
│   └── config.toml                 # Streamlit configuration settings
├── 📁 pages
│   ├── 1_Kidney.py                 # Kidney disease prediction page
│   ├── 2_Liver.py                  # Liver disease prediction page
│   └── 3_Parkinson.py              # Parkinson's disease prediction page
├── 📁 models
│   └── your_models.pkl             # Trained ML model(s)
├── Home_page.py                    # Main landing page for Streamlit app
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation

## ⚙️ Installation

Clone the repository and install dependencies.

```bash
git clone https://github.com/your-username/mini_pj_3.git
cd mini_pj_3
pip install -r requirements.txt
