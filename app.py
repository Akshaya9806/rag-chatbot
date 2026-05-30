import streamlit as st
import tempfile

from utils import process_pdf, retrieve_docs

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# UI
# -------------------------

st.title("🤖 AI Knowledge Assistant")
st.write("Upload a PDF and ask questions from it.")

# -------------------------
# Upload PDF
# -------------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(uploaded_file.read())
        pdf_path = temp_file.name

    st.success("✅ PDF Uploaded Successfully")

    # -------------------------
    # Create Vector Database
    # -------------------------

    with st.spinner("Creating Knowledge Base..."):
        db = process_pdf(pdf_path)

    st.success("✅ Knowledge Base Ready")

    # -------------------------
    # Ask Question
    # -------------------------

    question = st.text_input(
        "Ask a Question"
    )

    if st.button("Get Answer"):

        if not question:
            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("Searching Documents..."):

            docs = retrieve_docs(
                db,
                question
            )

            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

        # -------------------------
        # Retrieved Context
        # -------------------------

        with st.expander("Retrieved Context"):
            st.write(context)

        # -------------------------
        # Answer
        # -------------------------

        st.subheader("📄 Answer")

        if context.strip():
            st.write(context)
        else:
            st.warning(
                "No relevant information found in the document."
            )