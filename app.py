import asyncio

import streamlit as st

from cover_letter_agent import generate_cover_letter_from_documents
from helpers import extract_text_from_file


def main():
    st.set_page_config(
        page_title="LetGen",
        page_icon="✉️",
        layout="wide",
    )

    st.title("✉️ LetGen")
    st.caption("Upload your CV and related docs to generate a tailored cover letter.")

    with st.sidebar:
        tone = st.selectbox("Tone", ["Professional", "Confident", "Friendly", "Enthusiastic"], index=0)
        length_choice = st.selectbox("Length", ["Short (~180–250 words)", "Medium (~250–350 words)", "Long (~350–500 words)"], index=1)

    st.markdown("---")
    st.subheader("Target Role")
    job_title = st.text_input("Job Title", placeholder="e.g., Senior Backend Engineer")
    company_name = st.text_input("Company Name", placeholder="e.g. Arasaka")

    st.markdown("### 📤 Upload your documents")
    st.write("Upload your **CV** and any **additional files** (job description, summary, notes). Supports PDF, DOCX, TXT.")
    col1, col2 = st.columns(2)

    with col1:
        cv_file = st.file_uploader("CV (PDF/DOCX preferred)", type=["pdf", "docx", "txt"], accept_multiple_files=False, key="cv")
    with col2:
        additional_docs = st.file_uploader("Additional documents (optional) – multiple allowed", type=["pdf", "docx", "txt"], accept_multiple_files=True, key="extras")

    st.markdown("---")
    col_left, col_right = st.columns([1, 1])
    with col_left:
        is_generate_disabled = cv_file is None
        generate_btn = st.button("🚀 Generate Cover Letter", type="primary", use_container_width=True, disabled=is_generate_disabled)
    with col_right:
        clear_btn = st.button("🧹 Clear All", use_container_width=True)

    if clear_btn:
        st.rerun()

    if generate_btn:
        with st.spinner("Writing Cover Letter... this may take up to a minute ⏳"):
            cv_text = extract_text_from_file(cv_file)
            additional_docs = [extract_text_from_file(doc) for doc in additional_docs] if additional_docs else None
            generated_text = asyncio.run(
                generate_cover_letter_from_documents(
                    cv_text=cv_text,
                    company_name=company_name,
                    role=job_title,
                    additional_docs=additional_docs,
                    tone=tone,
                    length=length_choice
                )
            )
            st.markdown("### ✅ Generated Cover Letter")
            st.text_area("Result", value=generated_text, height=420)

        st.download_button(
            label="⬇️ Download TXT",
            data=generated_text,
            file_name="cover_letter.txt",
            mime="application/txt"
        )


if __name__ == "__main__":
    main()
