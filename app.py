import streamlit as st

st.set_page_config(
    page_title="Recruitment Matcher",
    page_icon="🌸",
    layout="wide"
)

st.title("🌸 Recruitment Matcher")

st.write(
    "A tool to help create recruitment bump schedules."
)

st.sidebar.header("Navigation")

page = st.sidebar.selectbox(
    "Go to",
    [
        "Home",
        "Members",
        "PNMs",
        "Bump Groups",
        "Generate Schedule"
    ]
)

if page == "Home":
    st.header("Welcome!")
    st.write(
        """
        This tool will eventually help you:
        
        - Manage member information
        - Upload PNM information
        - Create bump groups
        - Generate conversation assignments
        - Optimize recruitment flow
        """
    )

elif page == "Members":
    st.header("Members")
    st.info("Member database coming soon!")

elif page == "PNMs":
    st.header("PNMs")
    st.info("PNM database coming soon!")

elif page == "Bump Groups":
    st.header("Bump Groups")
    st.info("Bump group setup coming soon!")

elif page == "Generate Schedule":
    st.header("Generate Schedule")
    st.info("Optimization engine coming soon!")
