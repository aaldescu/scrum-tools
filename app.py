import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Scrum Tools",
    page_icon="🔄",
    layout="wide"
)

st.title("🔄 Scrum Tools")
st.header("Welcome to Scrum Tools!")

st.markdown("""
This application provides various tools to help you manage your Scrum process more effectively.

### Available Tools:

1. 📝 **Feature Request Template**
   - Generate well-formatted feature requests
   - Includes sections for user stories, technical requirements, and acceptance criteria
   - Live preview as you type

### Coming Soon:
- 📋 Sprint Planning Tool
- 📊 Story Point Calculator
- ⏱️ Sprint Velocity Tracker
- 🎯 Sprint Goal Generator
""")

st.sidebar.success("Select a tool from the sidebar to get started.")

