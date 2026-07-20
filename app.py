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
    st.header("👩 Members")

    if "members" not in st.session_state:
        st.session_state.members = []

    with st.form("member_form"):
        name = st.text_input("Member Name")

        group = st.selectbox(
            "Bump Group",
            ["A", "B", "C", "D"]
        )

        can_pickup = st.checkbox(
            "Can Pick Up"
        )

        can_pickup_two = st.checkbox(
            "Can Pick Up 2 PNMs"
        )

        initiator = st.checkbox(
            "Initiates Bump"
        )

        submitted = st.form_submit_button(
            "Add Member"
        )

        if submitted:
            st.session_state.members.append(
                {
                    "Name": name,
                    "Group": group,
                    "Can Pick Up": can_pickup,
                    "Can Pick Up 2": can_pickup_two,
                    "Initiator": initiator
                }
            )

            st.success(
                f"{name} added!"
            )

    st.divider()

    st.subheader("Current Members")

    if st.session_state.members:
        st.dataframe(
            st.session_state.members
        )

        if st.button("Clear All Members"):
            st.session_state.members = []
            st.success("All members removed.")
            st.rerun()

    else:
        st.info(
            "No members added yet."
        )

elif page == "PNMs":
    st.header("🎀 PNMs")

    if "pnms" not in st.session_state:
        st.session_state.pnms = []

    with st.form("pnm_form"):

        name = st.text_input("PNM Name")

        major = st.text_input("Major")

        hometown = st.text_input("Hometown")

        interests = st.text_area(
            "Activities / Interests"
        )

        notes = st.text_area(
            "Notes"
        )

        submitted = st.form_submit_button(
            "Add PNM"
        )

        if submitted:
            st.session_state.pnms.append(
                {
                    "Name": name,
                    "Major": major,
                    "Hometown": hometown,
                    "Interests": interests,
                    "Notes": notes
                }
            )

            st.success(
                f"{name} added!"
            )

    st.divider()

    st.subheader("Current PNMs")

    if st.session_state.pnms:
        st.dataframe(
            st.session_state.pnms
        )

        if st.button("Clear All PNMs"):
            st.session_state.pnms = []
            st.success("All PNMs removed.")
            st.rerun()

    else:
        st.info(
            "No PNMs added yet."
        )

elif page == "Bump Groups":
    st.header("Bump Groups")
    st.info("Bump group setup coming soon!")

elif page == "Generate Schedule":
    st.header("Generate Schedule")
    st.info("Optimization engine coming soon!")
