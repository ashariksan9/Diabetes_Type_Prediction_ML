# Early-Detection-Diabetes-Types-Machine-Learning

## 🎯 Project Objective

This project aims to build a machine learning model for the early detection of diabetes types based on a variety of medical, genetic, and lifestyle factors. The project utilizes supervised learning, specifically classification, to predict whether an individual has diabetes and to identify the type of diabetes they might have. The main goal is to provide a preventive solution to reduce the spread of diabetes, especially in younger individuals.

## 🧩 Problem Statement

Diabetes is a complex disease with often subtle symptoms, making early detection challenging. The prevalence of unhealthy eating habits, such as the rise of fast foods, has led to an increase in diabetes diagnoses, even among younger people. Identifying individuals at risk early can help in preventing or managing the condition more effectively.

## 🔍 Background

With the increase in diabetes cases, particularly among younger individuals, it is crucial to detect the disease early. Early detection allows for better management, prevention strategies, and lifestyle adjustments. This project focuses on predicting the likelihood of an individual having diabetes and categorizing it into different types, helping to implement timely interventions.

## 📊 Dataset

The dataset used in this project contains medical, genetic, and lifestyle information of individuals, including variables such as age, blood pressure, body mass index, and insulin levels. This dataset is available on [Kaggle](https://www.kaggle.com/datasets/ankitbatra1210/diabetes-dataset/data).

## 🚀 Output

The model predicts the likelihood of diabetes for an individual and classifies the type of diabetes. The evaluation metric used is the **F1-Score**, which balances precision and recall, as both false positives and false negatives are critical in the diagnosis of diabetes.

## 🧑‍💻 Methodology

1. **Data Preprocessing**: Handle missing data, encode categorical variables, and scale numerical features.
2. **Model Building**: Using Random Forest as the classification algorithm for prediction.
3. **Model Evaluation**: Model performance is evaluated using F1-Score.
4. **Hyperparameter Tuning**: Apply grid search for hyperparameter optimization.
5. **Model Deployment**: Deploy the final model on [Hugging Face](https://huggingface.co/spaces/ashariksan9/Model_Prediction_Diabetes_Type).

## 🔧 Tech Stack

- **Python Libraries**: Pandas, Numpy, Seaborn, Matplotlib, Pickle
- **Machine Learning Libraries**: Scikit-learn
  - **Pipeline**: For model building and deployment
- **Imbalanced-learn**: SMOTENC for handling class imbalance
- **Deployment**: Streamlit for creating a user-friendly interface
- **Model Serialization**: Pickle for saving and loading models

## 📂 File Descriptions

- `P1M2_<student-name>.ipynb`: Jupyter notebook for model development, training, and evaluation.
- `P1M2_<student-name>_inf.ipynb`: Jupyter notebook for model inference with unseen data.
- `deployment/`: Folder containing files related to model deployment.
  - `app.py`: Flask app for model inference.
  - `eda.py`: Script for exploratory data analysis.
  - `prediction.py`: Script for generating predictions using the trained model.
  - `model.pkl`: Serialized Random Forest model.
- `url.txt`: Contains URLs for the dataset and deployed model.

## ⚡ Advantages & Limitations

### Advantages:
- High accuracy with Random Forest for classification tasks.
- F1-Score metric ensures a balanced evaluation of the model’s precision and recall.
- Real-time deployment via Hugging Face enables quick predictions.

### Limitations:
- Dataset imbalance in specific diabetes types can affect model performance.
- Hyperparameter tuning could be improved for better accuracy.

## 🔗 References & Links

- [Dataset](https://www.kaggle.com/datasets/ankitbatra1210/diabetes-dataset/data)
- [Model Deployment on Hugging Face](https://huggingface.co/spaces/ashariksan9/Model_Prediction_Diabetes_Type)
- [Understanding Diabetes Types](https://www.diabetes.org.uk/diabetes-the-basics/types-of-diabetes)

## 📝 Conclusion

This project demonstrated the use of supervised learning techniques for the early detection of diabetes. By leveraging Random Forest and proper data preprocessing, the model provides reliable predictions for diabetes classification. Further improvements can be made through deeper feature engineering and additional hyperparameter tuning.

## 📫 Contact

- LinkedIn: www.linkedin.com/in/muhammadasharihsan
- Email: ashar4iksan@gmail.com
