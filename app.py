import streamlit as st
import google.generativeai as genai

# ====================================
# PASTE YOUR GEMINI API KEY HERE
# ====================================

GEMINI_API_KEY = "AQ.Ab8RN6K_vrnQ_OkHCEwlSDMGLGvkkXSqGX6RyBkAtxD3Fj5hrw"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="AI Gold Market Advisor",
    page_icon="🥇",
    layout="wide"
)

st.title("🥇 AI Gold Market Advisor for India")

st.markdown(
    "Analyze gold market trends using Generative AI"
)

# ====================================
# USER INPUTS
# ====================================

current_price = st.number_input(
    "Current Gold Price (₹ per gram)",
    min_value=1000.0,
    value=9800.0,
    step=10.0
)

investment_amount = st.number_input(
    "Investment Amount (₹)",
    min_value=1000,
    value=50000
)

risk_level = st.selectbox(
    "Risk Appetite",
    ["Low", "Medium", "High"]
)

investment_period = st.selectbox(
    "Investment Period",
    [
        "1 Month",
        "3 Months",
        "6 Months",
        "1 Year",
        "3 Years"
    ]
)

# ====================================
# AI ANALYSIS
# ====================================

if st.button("Generate AI Analysis"):

    prompt = f"""
    Act as a professional Gold Market Analyst in India.

    Current Gold Price: ₹{current_price} per gram

    Investor Details:
    Investment Amount: ₹{investment_amount}
    Risk Appetite: {risk_level}
    Investment Period: {investment_period}

    Provide:

    1. Current Gold Market Analysis
    2. Gold Price Trend Prediction
    3. Buy / Hold / Sell Recommendation
    4. Risks and Opportunities
    5. Investment Advice
    6. Future Outlook for Indian Investors

    Format the response with headings and bullet points.
    """

    try:

        with st.spinner("Analyzing Gold Market..."):

            response = model.generate_content(prompt)

        st.success("Analysis Generated Successfully")

        st.markdown(response.text)

    except Exception as e:

        st.error(f"Error: {e}")

# ====================================
# FOOTER
# ====================================

st.markdown("---")
st.caption("AI Gold Market Advisor | Streamlit + Gemini AI")
