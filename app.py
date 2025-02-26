"""
Author Name : Rahul R
Date : 26/02/2025
Version : 1.0

Features to be implemented :
1. User can upload the work done in the day.
2. User can mail directly to the manager.

"""

import streamlit as st
from ui.sidebar import render_sidebar
from ui.main_ui import render_main_ui, render_preview
from models.timesheet import initialize_session_state
from services.excel_service import generate_excel_timesheet
import pandas as pd
import io

# App configuration
st.set_page_config(page_title="Timesheet Generator", layout="wide")
st.title("Timesheet Generator")

# Initialize session state
initialize_session_state()

# Render sidebar (settings)
render_sidebar()

# Render main UI (employee info, date selection, daily descriptions)
employee_info, date_range, descriptions_text, dates = render_main_ui()

# Generate timesheet when button is clicked
if st.button("Generate Timesheet", type="primary"):
    # Show progress
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Generate Excel file and preview data
    output, preview_data = generate_excel_timesheet(
        employee_info, 
        date_range, 
        descriptions_text, 
        dates, 
        progress_bar,
        status_text
    )
    
    # Update preview
    preview_df = pd.DataFrame(preview_data)
    
    # Display success message and download button
    st.success("Timesheet generated successfully!")
    st.download_button(
        label="Download Timesheet Excel",
        data=output,
        file_name=f"timesheet_{employee_info['name'].replace(' ', '_')}_{date_range[0].strftime('%Y%m%d')}-{date_range[1].strftime('%Y%m%d')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    
    # Show preview
    render_preview(preview_df)
else:
    # Display empty preview if not generated
    render_preview(pd.DataFrame())

# Add footer with version information
st.markdown("---")
st.markdown("Timesheet Generator v2.0 | © 2025")