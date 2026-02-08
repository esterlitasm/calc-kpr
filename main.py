import streamlit as st

# ----------------------------
# Page config (must be first)
# ----------------------------
st.set_page_config(
    page_title="Streamlit App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# App constants / config
# ----------------------------
APP_TITLE = "Streamlit Base Template"
APP_DESCRIPTION = "Starting point for a Streamlit application."

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.title(APP_TITLE)
    st.caption(APP_DESCRIPTION)

    st.markdown("---")
    option = st.selectbox(
        "Select mode",
        options=["Home", "testing"],
        index=0,
    )

# ----------------------------
# Main layout
# ----------------------------
st.title(APP_TITLE)

if option == "Home":
    st.subheader("Home")
    st.write("Your main app content goes here.")

    if st.button("Click me"):
        st.success("Button clicked.")

elif option == "Settings":
    st.subheader("Settings")

    example_toggle = st.checkbox("Enable feature X", value=False)
    example_value = st.slider("Example value", 0, 100, 50)

    st.write("Feature X:", example_toggle)
    st.write("Value:", example_value)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Built with Streamlit")