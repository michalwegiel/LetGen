from datetime import datetime

import streamlit as st


def main():
    st.set_page_config(
        page_title="LetGen",
        page_icon="✉️",
        layout="wide",
    )

    st.title("✉️ LetGen")
    st.caption("Upload your CV and related docs to generate a tailored cover letter.")

    with st.sidebar:
        tone = st.selectbox("Tone", ["Professional", "Confident", "Friendly", "Formal", "Enthusiastic"], index=0)
        length_choice = st.selectbox("Length", ["Short (~180–250 words)", "Medium (~250–350 words)", "Long (~350–500 words)"], index=1)

    st.markdown("---")
    st.subheader("Target Role")
    job_title = st.text_input("Job Title", placeholder="e.g., Senior Backend Engineer")
    company_name = st.text_input("Company Name", placeholder="e.g. Arasaka")
    recruiter_name = st.text_input("Recruiter / Hiring Manager (optional)")

    st.markdown("### 📤 Upload your documents")
    st.write("Upload your **CV** and any **additional files** (job description, summary, notes). Supports PDF, DOCX, TXT, MD.")
    col1, col2 = st.columns(2)

    with col1:
        cv_file = st.file_uploader("CV (PDF/DOCX preferred)", type=["pdf", "docx", "txt", "md"], accept_multiple_files=False, key="cv")
    with col2:
        other_files = st.file_uploader("Additional documents (optional) – multiple allowed", type=["pdf", "docx", "txt", "md"], accept_multiple_files=True, key="extras")

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
        generated_text = ""
        st.markdown("### ✅ Generated Cover Letter")
        st.text_area("Result", value=generated_text, height=420)


        docx_bytes = b""
        fname = f"cover_letter_{company_name or 'company'}_{datetime.now().strftime('%Y%m%d')}.docx".replace(" ", "_")
        st.download_button(
            "⬇️ Download DOCX",
            data=docx_bytes,
            file_name=fname,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
        )


if __name__ == "__main__":
    main()
