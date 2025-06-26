# river-plastic-classification
Classify river plastic pollution contributors using environmental features and machine learning models (Logistic Regression, SVM, Random Forest, etc.) — with Scikit-Learn and cross-validation.
We explore multiple machine learning models to predict whether a river system is a **major plastic contributor** or not using features like:

- Area (`km²`)
- Coastline length (`km`)
- Annual rainfall (`mm/year`)
- L/A ratio (coastline length to area)

---

## 🔍 Objective

- Predict plastic contribution to oceans based on environmental factors.
- Classify rivers (via country-level data) into:
  - `1` → Low plastic contribution (≤ 6008 metric tons/year)
  - `0` → High plastic contribution (> 6008 metric tons/year)

---

## 🧠 Models Used

- Logistic Regression
- Decision Tree
- Random Forest ✅ *Best*
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gaussian Naive Bayes

> Random Forest achieved the highest average accuracy (90%) with perfect recall.

---

## 📊 Evaluation Metrics

Each model is evaluated using **5-fold stratified cross-validation** with:

- **Accuracy**
- **Precision**
- **Recall**

---

## 📁 Project Structure





---

## ✅ How to Run

1. Clone the repo:

```bash
   git clone https://github.com/yourusername/river-plastic-classification.git
   cd river-plastic-classification
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
