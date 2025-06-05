import streamlit as st

# Page configuration
st.set_page_config(page_title="Kobe Bot – Recruiting Education Coach", page_icon="📘", layout="centered")

# Branding and Header
st.image("Upgraded logo 3-13-24 black letters sports on road.png", width=200)
st.markdown("### *One Message. One Module. One Move at a Time.*")

# Custom CSS for button styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #4B0082;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("📘 Kobe Bot: The Mamba Mentor")
st.subheader("Your Recruiting Education Coach")

st.markdown("**Style of Play:** Relentless, disciplined, and detail-oriented.")

st.markdown("""
Kobe guides you through weekly training tips, email lessons, and challenge-based learning.  
This bot delivers key content from your **42-Day Challenge** or **60-Day Recruiting Plan**, always centered on **mental toughness** and **strategic preparation**.

> “The Mamba Bot sharpens your approach—one message, one module, one move at a time.”
""")

# Step 1: Select a Training Program
st.header("Step 1: Choose Your Training Program")
program = st.radio("Which plan would you like to start?", [
    "📅 42-Day Recruiting Challenge",
    "🗓️ 60-Day Recruiting Plan"
])

# Step 2: Today's Module
st.header("Step 2: Today's Lesson from Kobe")

if program == "📅 42-Day Recruiting Challenge":
    st.info("Day 1: Write your recruiting mission statement. Define your ‘Why’ before sending your ‘What’ to coaches.")
    st.caption("Tip: The best messages come from clarity, not copy-paste.")
elif program == "🗓️ 60-Day Recruiting Plan":
    st.info("Day 1: Audit your highlight video. Is your best play first? Trim down to under 3 minutes.")
    st.caption("Tip: Coaches have short attention spans. Lead with impact.")

# Step 3: Accountability Contact Info
st.header("Step 3: Stay on Track")
contact_method = st.selectbox("How should we send your daily lessons?", ["Email", "SMS", "Just on this App"])
contact_info = st.text_input(f"Enter your {contact_method}:")

# Step 4: Daily Commitment
if st.button("Lock In Today’s Lesson"):
    st.success("✅ Your training path has been updated.")
    st.markdown(f"""
    **Plan:** {program}  
    **Delivery Method:** {contact_method} → {contact_info}
    """)
    st.info("Kobe says: Stay consistent. Keep learning. Let your work speak.")
    st.balloons()
