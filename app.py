import streamlit as st

# Page setup
st.set_page_config(page_title="Kobe Bot - Recruiting Education Coach", page_icon="📘", layout="centered")

# Branding and Headerimport streamlit as st

# Page setup
st.set_page_config(page_title="Kobe Bot - Recruiting Education Coach", page_icon="📘", layout="centered")

# Branding and Header
st.image("Upgraded logo 3-13-24 black letters sports on road.png", width=200)
st.markdown("### *Outwork the Noise. Learn the Game. Lead the Process.*")

# Custom styling for buttons
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

# App Title
st.title("📘 Kobe Bot: The Mamba Mentor")
st.subheader("Your Recruiting Education Coach")

st.markdown("**Style of Play:** Intense, driven, and relentless.")

st.markdown("""
Kobe Bot helps you sharpen your recruiting IQ with structured training paths and real-world education.  
This is where you master the process—not just go through it.
""")

# Step 1: Struggle Identification
st.header("Step 1: What Do You Struggle With Most?")
struggle = st.selectbox("Pick your biggest recruiting challenge:", [
    "I don't know how to reach out to coaches",
    "I’m unsure what to say in emails",
    "I don’t know what to post on social media",
    "I haven’t built my highlight video yet",
    "I don’t know what schools fit me"
])
notes = st.text_area("Add any other concerns or questions")

# Step 2: Choose a Learning Track
st.header("Step 2: Choose a Learning Track")
learning_path = st.radio("What would you like to learn about first?", [
    "🏀 Recruiting Timeline Overview",
    "✉️ Coach Communication Tips",
    "🎞️ Building a Highlight Video",
    "📅 42-Day Recruiting Challenge"
])

# Step 3: Tip of the Day
st.header("Step 3: Today's Tip from Kobe")
if learning_path == "🏀 Recruiting Timeline Overview":
    st.info("Start early. Coaches begin tracking athletes as early as 9th grade. Your timeline is your edge—track progress monthly.")
elif learning_path == "✉️ Coach Communication Tips":
    st.info("Use the 3C method: Clear, Concise, and Confident. Personalize every message to the coach.")
elif learning_path == "🎞️ Building a Highlight Video":
    st.info("Your best plays should be first. Keep it under 3 minutes. Show athleticism, IQ, and hustle plays.")
elif learning_path == "📅 42-Day Recruiting Challenge":
    st.info("Consistency beats intensity. Show up daily. Complete 1 task a day to stay recruitable and visible.")

# Step 4: Delivery Method
st.header("Step 4: How Should We Deliver Your Lessons?")
contact_method = st.selectbox("Choose where you’d like to receive daily tips:", ["Email", "Text Message (SMS)", "Just On This App"])
contact_info = st.text_input(f"Enter your {contact_method}:")

# Summary
if st.button("Submit and Start Training"):
    st.success("📬 Training Path Submitted")
    st.markdown(f"""
    **Struggle Area:** {struggle}  
    **Extra Notes:** {notes}  
    **Chosen Path:** {learning_path}  
    **Delivery:** {contact_method} → {contact_info}
    """)
    st.info("Kobe Bot says: The work starts now. Let’s get it.")
    st.balloons()

st.image("Upgraded logo 3-13-24 black letters sports on road.png", width=200)
st.markdown("### *Outwork the Noise. Learn the Game. Lead the Process.*")

# Custom styling for buttons
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

# App Title
st.title("📘 Kobe Bot: The Mamba Mentor")
st.subheader("Your Recruiting Education Coach")

st.markdown("**Style of Play:** Intense, driven, and relentless.")

st.markdown("""
Kobe Bot helps you sharpen your recruiting IQ with structured training paths and real-world education.  
This is where you master the process—not just go through it.
""")

# Step 1: Struggle Identification
st.header("Step 1: What Do You Struggle With Most?")
struggle = st.selectbox("Pick your biggest recruiting challenge:", [
    "I don't know how to reach out to coaches",
    "I’m unsure what to say in emails",
    "I don’t know what to post on social media",
    "I haven’t built my highlight video yet",
    "I don’t know what schools fit me"
])
notes = st.text_area("Add any other concerns or questions")

# Step 2: Choose a Learning Track
st.header("Step 2: Choose a Learning Track")
learning_path = st.radio("What would you like to learn about first?", [
    "🏀 Recruiting Timeline Overview",
    "✉️ Coach Communication Tips",
    "🎞️ Building a Highlight Video",
    "📅 42-Day Recruiting Challenge"
])

# Step 3: Tip of the Day
st.header("Step 3: Today's Tip from Kobe")
if learning_path == "🏀 Recruiting Timeline Overview":
    st.info("Start early. Coaches begin tracking athletes as early as 9th grade. Your timeline is your edge—track progress monthly.")
elif learning_path == "✉️ Coach Communication Tips":
    st.info("Use the 3C method: Clear, Concise, and Confident. Personalize every message to the coach.")
elif learning_path == "🎞️ Building a Highlight Video":
    st.info("Your best plays should be first. Keep it under 3 minutes. Show athleticism, IQ, and hustle plays.")
elif learning_path == "📅 42-Day Recruiting Challenge":
    st.info("Consistency beats intensity. Show up daily. Complete 1 task a day to stay recruitable and visible.")

# Step 4: Delivery Method
st.header("Step 4: How Should We Deliver Your Lessons?")
contact_method = st.selectbox("Choose where you’d like to receive daily tips:", ["Email", "Text Message (SMS)", "Just On This App"])
contact_info = st.text_input(f"Enter your {contact_method}:")

# Summary
if st.button("Submit and Start Training"):
    st.success("📬 Training Path Submitted")
    st.markdown(f"""
    **Struggle Area:** {struggle}  
    **Extra Notes:** {notes}  
    **Chosen Path:** {learning_path}  
    **Delivery:** {contact_method} → {contact_info}
    """)
    st.info("Kobe Bot says: The work starts now. Let’s get it.")
    st.balloons()
