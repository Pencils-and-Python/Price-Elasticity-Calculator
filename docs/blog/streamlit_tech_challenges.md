# 🧪 Elasticity Risk Exposure Deployment – Troubleshooting Log

This section documents the key technical challenges encountered while preparing the Streamlit app for deployment and the strategies used to address them.

---

## 🚧 1. GitHub Push Failure (Model Too Large)

**Symptom:**  
- remote: error: File data/trained_model/random_forest_model_with_features.pkl is 2924.03 MB; this exceeds GitHub's file size limit of 100.00 MB

**Diagnosis:**  
GitHub blocks any single file over 100MB. The trained model `.pkl` file was over 2.9GB.

**Fix:**  
- Removed the large model from the repo using an interactive rebase (`git rebase -i`) and `filter-branch`.
- Switched to **dynamic model downloading** from Google Drive.

---

## 📦 2. `KeyError(60)` During `joblib.load()`

**Symptom:**  
- KeyError: 60

**Diagnosis:**  
Corrupted or incompatible `.pkl` file when downloading via `urllib.request.urlretrieve()`. It was a silent corruption — the file *existed*, but couldn't be deserialized.

**Fix:**  
- Switched to using [`gdown`](https://github.com/wkentaro/gdown) to download the model.
- Gdown handles Google Drive redirection and file integrity better.
- Confirmed that downloading manually with gdown resolved the issue.

---

## 🤯 3. `AttributeError: 'tuple' object has no attribute 'predict'`

**Symptom:**  
- AttributeError: 'tuple' object has no attribute 'predict'

**Diagnosis:**  
The model loading code returned `(model, feature_names)` as a tuple, but later assumed it was a model object.

**Fix:**  
- Ensured correct unpacking:
  ```python
  model, feature_names = load_model(...)
    ```

## ⚠️ 4. Streamlit Cloud: Model Loads Locally But Crashes on Cloud

**Symptom:** 
- KeyError: 60

*again on Streamlit Cloud, even though it worked locally.*

**Diagnosis:**
Streamlit Cloud likely hitting memory or compatibility issues:
- .pkl file is 3.07 GB
- Streamlit Cloud has ~1GB RAM per app
- Model was trained in scikit-learn==1.6.1, Cloud used 1.7.0

**Fix Options (Planned):**
- Re-train a slim version of the model with lower complexity:
    - *RandomForestRegressor(n_estimators=10, max_depth=5, n_jobs=1)*
- Reduce .pkl size dramatically (from 3GB → ~50–100MB)
- Re-upload smaller model and update download URL
- Consider hosting on Hugging Face or S3 for better pickle support

## 🧱 5. Streamlit Crash: OSError: [Errno 28] inotify watch limit reached

**Symptom:** 
- OSError: [Errno 28] inotify watch limit reached

**Diagnosis:**
Streamlit tried to watch too many files during startup, crashing the app. Common in containerized or low-resource environments.

**Fix:**
- Suppressed file-watching where possible (pending)
- A non-critical issue, overshadowed by memory crash from large .pkl

## 🧩 Key Takeaways
✅ Always remove models from Git history if over 100MB — they will block pushes to GitHub.  
✅ Use gdown instead of urllib.request for downloading Google Drive files.  
✅ Avoid pickling models over 1GB if deploying to Streamlit Cloud — it will crash.  
✅ Re-train a tiny model for deployment demos, and keep your full model for local analysis.  
✅ Use joblib and Python version consistency across environments (local vs cloud).  

### 🧠 This journey revealed how data science deployment isn’t just about ML — it’s about debugging environments, dependency hell, file size limits, and cloud resource constraints.