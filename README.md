# K-Means Customer Segmentation Dashboard

Complete end-to-end machine learning project demonstrating customer segmentation using K-Means clustering.

## 📊 Project Workflow
```
1. Exploratory Data Analysis (EDA)
2. Feature Engineering & Scaling  
3. WCSS Elbow Method for K selection
4. sklearn K-Means Clustering
5. Model Persistence (pickle .pkl)
6. Streamlit Dashboard Deployment
```

## 🛠️ Key Features
- **Interactive Streamlit App** - Visualize clusters & predictions
- **Production-ready Models** - Pre-trained KMeans saved as `Kmeans.pkl`
- **Complete Pipeline** - EDA → Feature Engineering → Clustering → Deployment
- **WCSS Analysis** - Optimal cluster determination

## 🚀 Quick Start
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 File Structure
```
├── app.py              # Streamlit dashboard
├── Kmeans.pkl         # Trained K-Means model
├── data/              # Processed datasets
├── notebooks/         # EDA & model training
└── requirements.txt   # Dependencies
```

Load model instantly: `pickle.load(open('Kmeans.pkl', 'rb'))`
