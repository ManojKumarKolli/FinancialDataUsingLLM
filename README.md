# FinancialDataUsingLLM

# AI-Driven Question Answering System

## Overview
This repository contains the implementation of an AI-driven Question Answering System that leverages state-of-the-art machine learning techniques and NLP models to efficiently retrieve accurate answers from a large corpus of documents. This system integrates FAISS for efficient similarity search in high-dimensional spaces and utilizes models like OpenAI's GPT-3 and fine-tuned transformers for generating responses.

## Project Structure
- `FAISS_INDEX.py`: Script for managing the FAISS index and saving the vector database.
- `QnA.py`: Core script containing the model logic, including functions to generate answers and find relevant document chunks.
- `evaluation.py`: Script for generating predictions on a sample set and saving the results for metric calculations.
- `extract_urls.py`: Utility for scraping URLs from the Moneycontrol website.
- `faiss_index.pkl`: Pickle file containing preprocessed document chunks stored in a vector database format.
- `file_info.json`: JSON file containing metadata about the document chunks such as file counts and URLs.
- `finetuning.ipynb`: Jupyter notebook detailing the fine-tuning process of the models used in the project.
- `load_documents.py`: Script to display the contents of the pickle file containing the document chunks.
- `main.py`: Streamlit application script for the user interface, including functionality to display metrics graphs.
- `metrics.json`: JSON file containing computed metrics from model evaluations.
- `metrics_evaluation.py`: Script that computes metrics based on model predictions and reference answers.
- `record_metrics_data_huggingface.json`: Output data containing predictions for sample questions using the Hugging Face model.
- `record_metrics_data_openai.json`: Output data containing predictions for sample questions using OpenAI's model.
- `requirements.txt`: List of Python libraries required to run the project.
- `sample.json`: Sample data file containing questions, reference answers, and contexts used for metric calculations.

## Setup and Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/question-answering-system.git
   cd question-answering-system
2. **Install Dependencies**:
Make sure Python 3.8+ is installed on your system, then run:
   ```bash
   pip install -r requirements.txt

3. **Running the Streamlit Application**:
Execute the following command to start the Streamlit interface:
   ```bash
   streamlit run main.py

## Contributions
We extend our deepest gratitude to each team member whose dedicated efforts have significantly shaped this project:

- **Manoj Kumar** ([@manojkumar](https://github.com/ManojKumarKolli)): Led the integration and optimization of the OpenAI model, managed the model fine-tuning processes, developed evaluation metrics, and contributed to human-centric metrics analysis.
- **Meghana Reddy** ([@meghanaDasireddy](https://github.com/DasireddyMeghana)): Responsible for data scraping and preprocessing, managed the FAISS indexing system, and played a key role in the evaluation of human-centric metrics.
- **Krishna Sai** ([@ananthakrishna](https://github.com/ananthakrishna4747)): Developed the Streamlit application, integrated the Hugging Face model, implemented metric plotting in the UI, and handled various evaluation processes including human-centric metrics.

## Acknowledgments
Special thanks to all mentors and advisors who provided guidance throughout the project. Their insights were invaluable in navigating the complexities of advanced NLP and system integration.

