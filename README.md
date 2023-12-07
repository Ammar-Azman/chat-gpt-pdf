# ChatGPT-PDF
- Application to read and reason any PDF files by using LLM model.

# Getting Started

## Run Apps Locally
1. To run apps locally, first create virtual environment and activate it. 
```
python3.9 -m venv venv
source venv/bin/activate
```
2. Install all requirements with the following command
```
pip install -r requirements.txt
```
3. Initialize Streamlit 
```
python -m streamlit run frontend/main.py

```
4. Insert your OpenAI api key within Secret Page in the app. 
5. Upload files, and ask the AI about your file!

## LLM Model Alternatives

1. If you are using model from OpenAI (OpenAI required some billing for you to use), please ensure to provide the `OPENAI_APIKEY`:
    - Within `./streamlit/secrets.toml` for **local**. (Note: please ensure to ignore toml file to avoid pushing the secret key!); or
    - Streamlit Secrets on **remote**. 
    ```toml
    # Example
    OPENAI_APIKEY="your-openai-api-key-bro"
    ```
    

2. If you are using model from HunggingFace, please provide Huggingface ID and Huggingface Token within the apps (see on sidebar). Most model from HF is free to use! Try `google/flan-t5-xxl` with your Huggingface Token. [create Hunggingface Token](https://huggingface.co/docs/hub/security-tokens)

# Prompt Engineering

### What can you do with this apps?

I will suggest several examples on how you can utilize the model with particular objective. 

**Resume/CV files**

- Prompt 1
    ```
    Please create an excellent cover letter for the resume with maximum 300 words.
    ```

- Prompt 2
    ```
    I want to apply for <job> position. Please suggest words improvement for my resume according to the position.
    ```

- Prompt 3
    ```
    List me out all job that is suitable for me according to my resume. 
    ```

**Research Paper**

- Prompt 1
    ```
    Please write an extensive summary based on this research paper.
    ```

- Prompt 2 (upload multiple research papers)
    ```
    Based on all of the research papers, which paper has the most correlation. State also which part that has highest correlation. 
    ```

- Prompt 3
    ```
    Based on my research paper, suggest me any improvement that I should do to improve the quality of my research.
    ```

**Invoice**

- Prompt 1
    ```
    Summarize the invoice so I can understand it better.
    ```
- Prompt 2
    ```
    Which invoice has the highest expenditure in 2021?
    ```

### And the rest is based on your creativity!