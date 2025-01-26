
import spacy
import pytextrank
import streamlit as st

def summarize_text(input_text):
    nlp = spacy.load("en_core_web_lg")
    nlp.add_pipe("textrank")
    doc = nlp(input_text)
    summary = "\n".join([sent.text for sent in doc._.textrank.summary(limit_phrases=2, limit_sentences=2)])
    return summary

def main():
    st.title("TextRank Text Summarizer")
    st.write("This app generates a concise summary from your input text using TextRank.")

    input_text = st.text_area("Enter the text you want to summarize:", height=300)

    if st.button("Summarize"):
        if input_text.strip():
            with st.spinner("Generating summary..."):
                summary = summarize_text(input_text)
                st.subheader("Summary:")
                st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()