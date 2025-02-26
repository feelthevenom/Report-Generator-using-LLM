import streamlit as st
from datetime import datetime

def render_sidebar():
    """
    Render the sidebar UI with settings for work hours and holidays
    """
    with st.sidebar:
        st.header("Settings")
        
        # Work hours settings
        render_work_hours_section()
        
        # Holiday management
        render_holiday_section()

def render_work_hours_section():
    """
    Render the work hours configuration section in the sidebar
    """
    st.subheader("Work Hours")
    work_start = st.text_input("Start Time", value=st.session_state.work_hours['start'])
    work_end = st.text_input("End Time", value=st.session_state.work_hours['end'])
    work_duration = st.text_input("Duration (hours)", value=st.session_state.work_hours['duration'])
    
    # Update work hours in session state
    st.session_state.work_hours = {
        'start': work_start,
        'end': work_end,
        'duration': work_duration
    }

def render_holiday_section():
    """
    Render the holiday management section in the sidebar
    """
    st.subheader("Holiday Management")
    holiday_date = st.date_input("Holiday Date", value=None)
    holiday_name = st.text_input("Holiday Name")
    
    if st.button("Add Holiday"):
        if holiday_date and holiday_name:
            new_holiday = {
                'date': holiday_date.strftime('%Y-%m-%d'),
                'name': holiday_name
            }
            if new_holiday not in st.session_state.holidays:
                st.session_state.holidays.append(new_holiday)
                st.success(f"Added holiday: {holiday_name} on {holiday_date}")
    
    # Display current holidays
    if st.session_state.holidays:
        st.subheader("Defined Holidays")
        for i, holiday in enumerate(st.session_state.holidays):
            st.write(f"{i+1}. {holiday['name']} ({holiday['date']})")
            
        if st.button("Clear All Holidays"):
            st.session_state.holidays = []
            st.success("All holidays cleared")