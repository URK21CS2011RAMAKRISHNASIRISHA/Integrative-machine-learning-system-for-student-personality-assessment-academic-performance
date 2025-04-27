import streamlit as st
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration
import docx2txt
import nltk
# Initialize the summarizer and question generator models
summarizer = pipeline('summarization')
tokenizer = T5Tokenizer.from_pretrained('valhalla/t5-small-qg-hl')
model = T5ForConditionalGeneration.from_pretrained('valhalla/t5-small-qg-hl')

def read_docx(uploaded_file):
    with open("temp.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
        f.close()
    with open('temp.txt', 'r') as file:
        text = file.read()
    return text

def summarize_text(text):
    return summarizer(text, max_length=100, min_length=25, do_sample=False)

def generate_questions(text):
    questions = []
    
    # Split the text into sentences
    sentences = nltk.tokenize.sent_tokenize(text)
    
    # Generate a question for each sentence
    for sentence in sentences:
        inputs = tokenizer.encode("generate question: " + sentence, return_tensors='pt')
        outputs = model.generate(inputs, max_length=200, do_sample=True, top_p=0.95, top_k=60)
        question = tokenizer.decode(outputs[0], skip_special_tokens=True)
        questions.append(question)
    
    return questions

st.title('Text Summarizer and Question Generator')

uploaded_file = st.file_uploader("Upload a .docx file", type="docx")

if uploaded_file is not None:
    text = read_docx(uploaded_file)
    st.write('Original Text:')
    st.write(text)

    if st.button('Generate Summary'):
        summary = summarize_text(text)
        st.write('Summary:')
        st.write(summary[0]['summary_text'])

    if st.button('Generate Questions'):
        questions = generate_questions(text)
        st.write('Generated Questions:')
        for i, question in enumerate(questions, start=1):
            st.write(f"Question {i}: {question}")
