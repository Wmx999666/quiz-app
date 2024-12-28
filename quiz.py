import streamlit as st

# App Title
st.title("Welcome to Your Personalized Quiz")

# Question 1
answer1 = st.radio(
    "What is your biggest challenge?",
    ("Generating leads", "Improving conversions", "Scaling my business")
)

# Question 2
if answer1:
    answer2 = st.radio(
        "What industry are you in?",
        ("E-commerce", "Consulting", "Service-based")
    )

# Show Result
if answer1 and answer2:
    st.write("Based on your answers, here's what we recommend:")
    if answer1 == "Generating leads":
        st.write("You should focus on creating high-converting lead magnets!")
    elif answer1 == "Improving conversions":
        st.write("Consider optimizing your sales funnel with email campaigns.")
    else:
        st.write("Scaling requires better automation tools and team delegation.")
# Email Capture
email = st.text_input("Enter your email to receive your personalized report:")
if email:
    st.write(f"Thank you, {email}! Your report has been sent.")
