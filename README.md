# Gold Recovery Prediction for Industrial Process Optimization

## 📊 Project Overview
This project develops a Machine Learning regression model to predict the amount of gold recovered from ore for the industrial company Zyfra, which provides efficiency solutions for heavy industry.
Using historical data from different stages of the gold extraction and purification process, predictive models were built to estimate final gold recovery levels.
The primary evaluation metric is sMAPE (Symmetric Mean Absolute Percentage Error), which is well suited for industrial forecasting problems.
The objective is to minimize prediction error and support production optimization through data-driven decision-making.

## 📊 Dataset Description
The dataset contains technological process parameters collected from multiple stages of gold extraction, including:
- Flotation stage variables
- Primary and secondary purification process parameters
- Chemical concentrations and material characteristics
- Recovery rates at different production stages
- Final gold recovery (target variable)
The dataset reflects real industrial process conditions and is used to identify the most influential parameters affecting gold recovery.

[Data Description for Tech Process](notebooks/data_description.ipynb)

## 🔬 Gold Extraction Process Overview
<p align="center">
  <img src="assets/gold_recovery_process.png " width="500"/>
</p>

[Technological Process](notebooks/technological_process.ipynb) <br>
[Recovery Calculation](notebooks/recovery_calculation.ipynb)

## ⚙️ Methodology
The project follows a structured Machine Learning regression workflow:
1. Data Analysis & Preprocessing
  - Verified recovery calculation consistency
  - Removed features not available during model deployment
  - Handled missing values
  - Performed feature alignment between training and test datasets
  - Applied scaling when necessary
  - Implemented cross-validation for robust evaluation

2. Model Development
- Two regression algorithms were evaluated:
  - Linear Regression
  - Random Forest Regressor
- A machine learning pipeline was used to streamline preprocessing and modeling steps.

3. Model Evaluation
- Models were evaluated using:
  - sMAPE (Primary Metric)
  - Cross-validation scoring

- sMAPE was selected because:
  - It measures relative prediction error
  - It is suitable for industrial forecasting tasks
  - Lower sMAPE values indicate better predictive performance.

## 📈 Results
- Model Performance Comparison
  - Model	Final sMAPE
    - Linear Regression	11.39% 
    - Random Forest Regressor	8.99%

- Final Model Selection: <br>
  - The Random Forest Regressor achieved the lowest prediction error with a final sMAPE of 10.58%, outperforming Linear Regression.
  - This suggests that the relationship between process variables and gold recovery is non-linear and complex, which is better captured by ensemble tree-based methods.

## 💼 Business Impact
The model enables Zyfra to:
- Identify key production parameters affecting gold recovery
- Optimize technological processes
- Reduce operational inefficiencies
- Support data-driven industrial decision-making
- By integrating predictive modeling into production monitoring systems, the company can improve recovery rates and enhance overall profitability.

## ▶️ How to Run the Project
1.	Clone this repository: git clone https://github.com/alangudi417/industrial-gold-recovery-prediction.git 
2.	Navigate to the project folder: cd industrial-gold-recovery-prediction
3.	Create and activate virtual environment: python -m venv venv venv\Scripts\activate # Windows source venv/bin/activate # Mac/Linux
4.	Install dependencies: pip install -r requirements.txt
5.	Launch Jupyter Notebook: jupyter notebook
6.	Open notebooks/gold_recovery.ipynb