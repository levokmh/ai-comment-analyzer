\# 🤖 AI Comment Analyzer



Modern AI-powered sentiment analysis dashboard built with Streamlit, Transformers, and Plotly.



Analyze comments from CSV files using a real NLP model based on Hugging Face Transformers.



\---



\# ✨ Features



\* ✅ AI-powered sentiment analysis

\* ✅ Modern interactive dashboard

\* ✅ Upload your own CSV files

\* ✅ Real NLP model using Transformers

\* ✅ Positive / Neutral / Negative detection

\* ✅ Search comments instantly

\* ✅ Filter comments by sentiment

\* ✅ Export analyzed results to CSV

\* ✅ Interactive Plotly charts

\* ✅ Responsive modern UI

\* ✅ Pagination system



\---



\# 🧠 AI Model



This project uses the following Hugging Face model:



```txt

nlptown/bert-base-multilingual-uncased-sentiment

```



The model predicts sentiment scores from 1 to 5 stars.



The application converts them into:



| Stars | Sentiment |

| ----- | --------- |

| 1-2   | Negative  |

| 3     | Neutral   |

| 4-5   | Positive  |



\---



\# 📸 Dashboard Overview



The dashboard includes:



\* sentiment overview metrics

\* AI sentiment distribution chart

\* searchable comment list

\* CSV export system

\* modern dark UI



\---



\# 🛠️ Tech Stack



| Technology   | Usage              |

| ------------ | ------------------ |

| Python       | Backend            |

| Streamlit    | Web app            |

| Transformers | NLP model          |

| PyTorch      | Deep learning      |

| Plotly       | Interactive charts |

| Pandas       | Data processing    |



\---



\# 📂 Project Structure



```txt

AI-Comment-Analyzer/

│

├── app.py

├── requirements.txt

├── README.md

│

├── data/

│   └── comments\_sample.csv

│

├── src/

│   ├── data\_loader.py

│   ├── metrics.py

│   └── sentiment.py

│

└── assets/

```



\---



\# 🚀 Installation



\## 1. Clone the repository



```bash

git clone https://github.com/your-username/AI-Comment-Analyzer.git

cd AI-Comment-Analyzer

```



\---



\## 2. Create a virtual environment



\### Windows



```bash

python -m venv venv

venv\\Scripts\\activate

```



\### Linux / macOS



```bash

python3 -m venv venv

source venv/bin/activate

```



\---



\## 3. Install dependencies



```bash

pip install -r requirements.txt

```



\---



\## 4. Run the application



```bash

streamlit run app.py

```



\---



\# 📄 CSV Format



The uploaded CSV file must contain a column named:



```txt

comment

```



Example:



```csv

comment

"This video is amazing!"

"I did not enjoy this tutorial."

"Very useful content."

```



\---



\# ⚡ Performance Optimizations



The project includes:



\* Streamlit cache system

\* Batch sentiment analysis

\* Cached Transformer model loading



This significantly improves performance compared to single-comment analysis.



\---



\# 🎯 Future Improvements



Planned features:



\* toxicity detection

\* emotion analysis

\* keyword extraction

\* multilingual UI

\* authentication system

\* database integration

\* live YouTube/Twitch comment analysis

\* Docker deployment

\* cloud hosting



\---



\# 📦 Requirements



Main dependencies:



```txt

streamlit

transformers

torch

torchvision

plotly

pandas

```



\---



\# 👨‍💻 Author



Developed by \*\*LevoKMH\*\*



\---



\# ⭐ GitHub



If you like this project, consider giving it a star.



