import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Feature Request Template - Scrum Tools",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Feature Request Template Generator")

# Create form
with st.form("feature_request_form"):
    # Basic Information
    feature_name = st.text_input("Feature Name", placeholder="Brief name of the feature")
    description = st.text_area("Description", placeholder="Detailed description of what the feature should do")
    
    # User Story
    st.subheader("User Story")
    user_type = st.text_input("As a", placeholder="Type of user")
    action = st.text_input("I want to", placeholder="Action/goal")
    benefit = st.text_input("So that", placeholder="Benefit/value")
    
    # Technical Requirements
    st.subheader("Technical Requirements")
    col1, col2 = st.columns(2)
    
    with col1:
        frontend_ui = st.text_area("Frontend UI Components", 
            placeholder="List UI components (one per line)")
        frontend_js = st.text_area("Frontend JavaScript Logic", 
            placeholder="List JS functions (one per line)")
        
    with col2:
        backend_api = st.text_area("Backend API Endpoints", 
            placeholder="List API endpoints (one per line)")
        backend_db = st.text_area("Backend Database Changes", 
            placeholder="List database changes (one per line)")
    
    # Example Usage
    example_usage = st.text_area("Example Usage", 
        placeholder="Step-by-step example of how a user would use this feature")
    
    # Acceptance Criteria
    acceptance_criteria = st.text_area("Acceptance Criteria", 
        placeholder="Enter acceptance criteria (one per line)")
    
    # Additional Notes
    additional_notes = st.text_area("Additional Notes", 
        placeholder="Any other relevant information, known limitations, future considerations")
        
    submitted = st.form_submit_button("Generate Feature Request")

# Preview section
st.divider()
st.subheader("Live Preview")

# Convert multiline text areas to bullet points
def text_to_bullets(text, indent=""):
    if not text:
        return f"{indent}[Not specified]"
    return "\n".join(f"{indent}- [ ] {line}" for line in text.split("\n") if line.strip())

preview = f"""
# Feature Request

## Feature Name
{feature_name if feature_name else '[Brief name of the feature]'}

## Description
{description if description else '[Detailed description of what the feature should do]'}

## User Story
**As a** {user_type if user_type else '[type of user]'}
**I want to** {action if action else '[action/goal]'}
**So that** {benefit if benefit else '[benefit/value]'}

## Technical Requirements
### Frontend Changes
- [ ] UI Components:
{text_to_bullets(frontend_ui, "    ")}
- [ ] JavaScript Logic:
{text_to_bullets(frontend_js, "    ")}

### Backend Changes
- [ ] API Endpoints:
{text_to_bullets(backend_api, "    ")}
- [ ] Database:
{text_to_bullets(backend_db, "    ")}

## Example Usage
{example_usage if example_usage else '[Step-by-step example of how a user would use this feature]'}

## Acceptance Criteria
{text_to_bullets(acceptance_criteria)}

## Additional Notes
{text_to_bullets(additional_notes)}

---
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

st.markdown(preview)
