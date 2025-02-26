import streamlit as st
from datetime import datetime, timedelta, date
from config.settings import DEFAULT_EMPLOYEE_INFO
from utils.helpers import generate_date_range

def render_main_ui():
    """
    Render the main UI components for the timesheet generator app
    
    Returns:
        tuple: (employee_info, date_range, descriptions_text, dates)
    """
    # Create columns for employee information
    st.subheader("Employee Information")
    col1, col2 = st.columns(2)
    
    with col1:
        employee_name = st.text_input("Name", value=DEFAULT_EMPLOYEE_INFO['name'])
        employee_designation = st.text_input("Designation", value=DEFAULT_EMPLOYEE_INFO['designation'])
    
    with col2:
        employee_department = st.text_input("Department", value=DEFAULT_EMPLOYEE_INFO['department'])
        employee_id = st.text_input("Employee ID", value=DEFAULT_EMPLOYEE_INFO['employee_id'])
    
    # Compile employee info dictionary
    employee_info = {
        'name': employee_name,
        'designation': employee_designation,
        'department': employee_department,
        'employee_id': employee_id
    }
    
    # Date range selection
    col1, col2 = st.columns(2)
    
    with col1:
        # Date range picker
        st.subheader("Timesheet Period")
        today = datetime.now()
        # default_start = datetime(today.year, today.month, 1)
        # default_end = datetime(today.year, today.month, min(today.day, 1))
        
        date_range = st.date_input(
            "Select Date Range",
            value=(),
            min_value=datetime(2000, 1, 1),
            max_value=datetime(2100, 12, 31),
            help="Select the start and end dates for your timesheet."
        )

        # Ensure date_range is a tuple with two dates
        if isinstance(date_range, tuple) and len(date_range) == 2:
            start_date, end_date = date_range
        else:
            st.error("Please select a valid date range.")
            st.stop()
    
    # Validate date range
    if start_date > end_date:
        st.error("Error: End date must be after start date")
        dates = []
    else:
        dates = generate_date_range(start_date, end_date)
    
    # Daily descriptions text area
    st.subheader("Daily Descriptions")
    
    # Help text
    with st.expander("How to enter descriptions"):
        st.markdown("""
        Enter descriptions in the format: `day: description`
        
        For example:
        ```
        1 Sun: Implemented user authentication feature
        2 Mon: Fixed bugs in reporting module
        3 Tue: Leave - Personal
        4 Wed: Weekend
        5 Thu: Holiday - Labor Day
        ```
        
        Descriptions starting with "Leave", "Holiday", or "Weekend" will be marked accordingly.
        For days without descriptions, weekends will be auto-detected.
        """)

    # Generate list of dates
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)

    # Check if any predefined holidays fall within the date range
    holiday_dict = {}
    for holiday in st.session_state.holidays:
        holiday_date = datetime.strptime(holiday['date'], '%Y-%m-%d').date()
        if start_date <= holiday_date <= end_date:
            holiday_dict[holiday_date] = holiday['name']

    # Generate default text for text area with day and day name
    default_text = []
    for date in dates:
        prefix = f"{date.day} {date.strftime('%a')}: "
        if date in holiday_dict:
            prefix += f"Holiday - {holiday_dict[date]}"
        elif date.weekday() >= 5:  # Saturday or Sunday
            prefix += "Weekend"
        default_text.append(prefix)
        
    descriptions_text = st.text_area(
    "Daily Descriptions",
    value="\n".join(default_text),
    height=300,
    help="Enter one line per day in the format 'day day_name: description'. Use 'Leave' for leave days, 'Holiday' for holidays, or enter your work description."
)
    
    return employee_info, (start_date, end_date), descriptions_text, dates

def render_preview(preview_df):
    """
    Render the preview of the generated timesheet
    
    Args:
        preview_df (pandas.DataFrame): Dataframe containing preview data
    """
    st.subheader("Timesheet Preview")
    
    if preview_df.empty:
        st.info("Generate a timesheet to see the preview here")
    else:
        # Apply custom styling to the dataframe
        def highlight_status(val):
            """Apply background color based on status value"""
            if 'Holiday' in val:
                return 'background-color: #c1121f'
            elif 'Leave' in val:
                return 'background-color: #ffb703'
            elif 'Weekend' in val:
                return 'background-color: #003049'
            else:
                return ''
        
        # Apply the styling function and display the dataframe
        styled_df = preview_df.style.applymap(highlight_status, subset=['Status'])
        st.dataframe(styled_df, use_container_width=True)
        
        # Display summary statistics
        st.subheader("Summary")
        total_days = len(preview_df)
        working_days = len(preview_df[preview_df['Status'] == 'Regular Day'])
        holidays = len(preview_df[preview_df['Status'].str.contains('Holiday')])
        leave_days = len(preview_df[preview_df['Status'].str.contains('Leave')])
        weekends = len(preview_df[preview_df['Status'] == 'Weekend'])
        
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Total Days", total_days)
        col2.metric("Working Days", working_days)
        col3.metric("Holidays", holidays)
        col4.metric("Leave Days", leave_days)
        col5.metric("Weekends", weekends)