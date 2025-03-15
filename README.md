# Diabetes Prediction using Support Vector Machine (SVM) 🏥🔬  

## Overview 📄  

This project predicts whether a **patient has diabetes** based on features such as **age, BMI, glucose levels, and blood pressure** using a **Support Vector Machine (SVM) model**. The workflow includes **data collection, preprocessing, feature engineering, scaling, model training, and evaluation** using metrics like **accuracy and F1-score**. Additionally, a **Streamlit web application** has been developed for real-time predictions.  

---

## Project Workflow 🔄  

### 1. Data Collection 📂  
- The dataset was obtained from **Kaggle**.  
- It contains **medical records** of patients, including:  
  - **Age**  
  - **BMI (Body Mass Index)**  
  - **Glucose Levels**  
  - **Blood Pressure**  
  - **Insulin Levels**  
  - **Diabetes Pedigree Function**  
  - **Pregnancies**
  - **SkinThickness**
  - **Outcome (Diabetes: 1, No Diabetes: 0)**  

### 2. Data Preprocessing 🔍  
- Checked for missing values and handled them accordingly.  
- Removed **outliers** using statistical techniques.  

### 3. Feature Engineering 🛠️  
- Created new meaningful features to improve model performance.  
- Performed **correlation analysis** to select the most relevant features.  

### 4. Feature Scaling 📊  
- Applied **StandardScaler** to normalize numerical features for better performance.  

### 5. Train-Test Split 🔢  
- Split the dataset into **80% training** and **20% testing**.  

### 6. Model Training 🤖  
- Trained a **Support Vector Machine (SVM) classifier** using **Scikit-Learn**.  
- Tuned hyperparameters to optimize performance.  

### 7. Model Evaluation 📉  
- Evaluated model performance using:  
  - **Accuracy Score**  
  - **Precision, Recall, and F1-Score**  
  - **Confusion Matrix**  

### 8. Visualization & Insights 📊  
- Plotted feature distributions and model performance metrics using **Matplotlib** and **Seaborn**.  

### 9. Real-Time Prediction 🔮  
- Developed a **Streamlit web app** where users can input their medical details to check for diabetes risk.  

---

## UI Development 🖥️  
- A **Graphical User Interface (GUI)** was built using **Streamlit**.  
- Users can enter their **age, BMI, glucose levels, and blood pressure** to get a real-time **diabetes prediction**.  

---

## Technologies Used 💻  
- **Python** (Pandas, NumPy, Scikit-Learn, joblib)  
- **Streamlit** (for UI)  
- **Matplotlib & Seaborn** (for visualization)  
- **Jupyter Notebook** (for model training & evaluation)  

---

## Installation Guide 🛠️  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/Diabetes-Prediction-SVM.git
   cd Diabetes-Prediction-SVM
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the Streamlit UI:
   ```bash
   streamlit run app.py
   ```
   
---

## User Guide 🚀
  - Open the Streamlit UI in a browser.
  - Enter age, BMI, glucose levels, blood pressure, etc.
  - Click on Predict to check for diabetes risk.
  - View Results.

---

## Results & Insights 📊
  - The SVM model effectively classifies patients as diabetic or non-diabetic.
  - The web app allows users to check their diabetes risk interactively.
  - The model helps in early diabetes detection, which can assist in preventive healthcare.

---

## Future Enhancements 🚧
  - Deploy the model on a cloud platform (e.g., AWS, Heroku).
  - Compare with other classification models (e.g., Random Forest, Neural Networks).
---

## 👥 Contact
For questions or feedback, feel free to reach out:
  - GitHub: @RimeshCdry
  - Email: rimeshcdry45@gmail.com
  - LinkedIn: https://www.linkedin.com/in/rimesh-chaudhary-09a25a30a
