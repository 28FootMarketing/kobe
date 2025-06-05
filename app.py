import streamlit as st

# Page configuration
st.set_page_config(page_title="Kobe Bot - Recruiting Education Coach", page_icon="📘", layout="centered")

# Header Section
st.title("📘 Kobe Bot: The Mamba Mentor")
st.subheader("Your Recruiting Education Coach")

st.markdown("**Style of Play:** Relentless, disciplined, and detail-oriented.")
st.markdown("""
Kobe Bot guides student-athletes through weekly training, email lessons, and challenge-based learning.  
Focused on mental toughness and precision, this bot sends content from the 42-Day or 60-Day Recruiting Plan to build confidence and execution.

> “The Mamba Bot sharpens your approach—one message, one module, one move at a time.”
""")

# Step 1: Choose a Training Program
st.header("Step 1: Choose Your Training Program")
program = st.radio("Which program would you like to follow?", [
    "📅 42-Day Recruiting Challenge",
    "🗓️ 60-Day Recruiting Plan"
])

# Step 2: Lesson of the Day
st.header("Step 2: Today’s Focus Lesson")
if program == "📅 42-Day Recruiting Challenge":
    st.info("Day 1: Define your recruiting identity. What position, strengths, and mindset do you want coaches to know?")
    st.caption("Tip: Your message to coaches should reflect clarity and confidence.")
elif program == "🗓️ 60-Day Recruiting Plan":
    st.info("Day 1: Review your highlight video. Open with your best play. Keep it under 3 minutes.")
    st.caption("Tip: Coaches make snap decisions—show them who you are, fast.")

# Step 3: Contact Method
st.header("Step 3: Delivery Preference")
delivery = st.selectbox("Where should Kobe send your daily lessons?", ["Email", "SMS", "Just in this App"])
contact = st.text_input(f"Enter your {delivery} contact:")

# Summary Output
if st.button("Lock In"):
    st.success("✅ You’re enrolled and locked in.")
    st.markdown(f"""
    **Selected Plan:** {program}  
    **Delivery Method:** {delivery} → {contact if contact else 'No contact provided'}
    """)
    st.info("Kobe says: Do not skip steps. Stay disciplined. Every day is a rep.")
    st.balloons()
