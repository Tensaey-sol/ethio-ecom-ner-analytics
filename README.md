# Ethio Ecom NER Analytics

This repository contains the setup and development for **Ethio Ecom NER Analytics**, a real-world e-commerce analytics project focused on extracting key entities from Telegram channels in Ethiopia using Named Entity Recognition (NER) and analytics to power a centralized hub and vendor insights.

The project simulates the role of a **Data Science Engineer**, leveraging data ingestion, preprocessing, NER model fine-tuning, and vendor scoring with machine learning to deliver insights for micro-lending and e-commerce optimization.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Tensaey-sol/ethio-ecom-ner-analytics.git
cd ethio-ecom-ner-analytics
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
ethio-ecom-ner-analytics/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions workflow
├── .gitignore                 # Ignore rules for Git
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── notebooks/                 # Jupyter Notebooks
│   └── README.md
├── tests/                     # Unit tests for scripts and functions
│   └── __init__.py
├── scripts/                   # Scripts for data ingestion, preprocessing, modeling
│   ├── __init__.py
│   └── README.md
├── data/                      # Raw and processed datasets
│   ├── raw/                   # Raw Telegram data
│   ├── processed/             # Preprocessed data
│   └── conll/                 # CoNLL-formatted labeled data
└── .venv/                     # Local virtual environment (ignored via .gitignore)
```

---

## ⚙️ GitHub Actions CI

This repository uses **GitHub Actions** for continuous integration. On every push:

- Python 3.13.1 is installed
- Dependencies are installed
- Tests are executed from `/tests`

See `.github/workflows/ci.yml` for workflow configuration.

---

## 🛠 Tools & Technologies

- Python **3.13.1**
- Pandas, NumPy, Hugging Face Transformers, Scikit-learn
- Matplotlib, Seaborn (for visualization)
- SHAP, LIME (for model interpretability)
- Git & GitHub for version control
- GitHub Actions for CI/CD
- Jupyter Notebooks for analysis

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Questions or Contributions?

Feel free to open an issue or submit a pull request to contribute or raise a question.
