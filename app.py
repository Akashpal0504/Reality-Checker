import time

from pypdf import PdfReader

def extract_text_from_pdf(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


claim_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    Extract all factual claims involving numbers, dates, prices, or events.
    Return each claim as a bullet point.

    TEXT:
    {text}
    """
)

def extract_claims(text):
    response = llm.invoke(claim_prompt.format(text=text))

    return response.content.split("\n")



from tavily import TavilyClient

tavily = TavilyClient(api_key="TAVILY_API_KEY")

def verify_claim(claim):
    search_result = tavily.search(query=claim, max_results=3)

    if not search_result["results"]:
        return "❌ False", "No evidence found"

    evidence = search_result["results"][0]["content"]

    verdict_prompt = f"""
    Claim: {claim}
    Evidence: {evidence}

    Classify this claim as:
    - Verified
    - Inaccurate
    - False
    """

    time.sleep(2)  # ⏳ prevent rate limit
    verdict = llm.invoke(verdict_prompt).content
    return verdict, evidence



import streamlit as st

st.title("🕵️ REALITY CHECKER")

uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")

if uploaded_pdf:
    text = extract_text_from_pdf(uploaded_pdf)
    MAX_CHARS = 4000
    claims = extract_claims(text[:MAX_CHARS])


    for claim in claims[:5]:

        verdict, evidence = verify_claim(claim)
        st.subheader(claim)
        st.write("Status:", verdict)
        st.write("Evidence:", evidence)
