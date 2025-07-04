# 🌌 Exoplanet Detection and Explainability System

This project is an end-to-end machine learning pipeline for detecting exoplanet transit events using light curve data from missions like NASA Kepler and TESS. It includes model training, inference APIs, a web dashboard, and natural language summaries and literature search to enhance explainability and accessibility.

---

## 🚀 Goals

- Detect exoplanet transit events from raw light curve data
- Deploy a CNN or Transformer model with high accuracy
- Provide natural language explanations of predictions
- Search for similar patterns in arXiv scientific literature
- (Bonus) Filter false positives and support few-shot learning

---

## 🧠 Project Architecture

```
light curves → preprocessing → CNN/Transformer → prediction → 
    → REST API + Dashboard
    → Natural language summary
    → arXiv paper search
```

---

## 📁 Project Structure

- `data/`: Raw and processed light curve data
- `src/`: All code (models, preprocessing, explainability, API)
- `notebooks/`: Exploratory analysis, modeling, and evaluation
- `dashboard/`: Streamlit or Dash frontend
- `scripts/`: CLI scripts to train, predict, summarize
- `tests/`: Unit tests for major modules

---

## ⚙️ Setup

1. Clone the repo:
    ```bash
    git clone https://github.com/your_username/exoplanet-detection.git
    cd exoplanet-detection
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run preprocessing:
    ```bash
    python scripts/run_preprocessing.py
    ```

4. Train the model:
    ```bash
    python scripts/run_training.py
    ```

5. Start the API:
    ```bash
    uvicorn src.api.main:app --reload
    ```

6. Run the dashboard:
    ```bash
    streamlit run dashboard/app.py
    ```

---

## 📝 Example Output

> 🪐 *"This light curve shows a dip consistent with a planet approximately 1.8 times the radius of Earth, orbiting every 3.2 days."*

---

## 🔍 Features

- ✅ Light curve normalization & windowing
- ✅ CNN or Transformer-based classifier
- ✅ REST API for inference
- ✅ Web dashboard for uploading/viewing light curves
- ✅ NLP-generated event summaries
- ✅ Search arXiv for similar exoplanet research

---

## 🤖 Tech Stack

- Python, NumPy, Pandas, PyTorch/TensorFlow
- FastAPI for REST API
- Streamlit/Dash for frontend
- HuggingFace Transformers for NLP
- FAISS or Sentence-BERT for paper search

---

## 📌 Future Work

- [ ] Eclipsing binary filtering
- [ ] Few-shot learning support
- [ ] Feedback loop for model retraining

---

## 🤝 Contributing

1. Fork this repo
2. Create a feature branch: `git checkout -b my-feature`
3. Commit your changes
4. Open a Pull Request 🚀

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

## 📫 Contact

Feel free to reach out if you’re interested in collaborating or using this project for research!
