import streamlit as st
from datetime import datetime
from config.settings import DEFAULT_WORK_HOURS

class Holiday:
    """Model for holiday data"""
    def __init__(self, date, name):
        self.date = date
        self.name = name
        
    def to_dict(self):
        return {
            'date': self.date.strftime('%Y-%m-%d') if isinstance(self.date, datetime) else self.date,
            'name': self.name
        }
    
    @staticmethod
    def from_dict(data):
        date = data['date']
        if isinstance(date, str):
            date = datetime.strptime(date, '%Y-%m-%d').date()
        return Holiday(date, data['name'])

class WorkHours:
    """Model for work hours data"""
    def __init__(self, start, end, duration):
        self.start = start
        self.end = end
        self.duration = duration
        
    def to_dict(self):
        return {
            'start': self.start,
            'end': self.end,
            'duration': self.duration
        }

def initialize_session_state():
    """Initialize session state with default values if not already set"""
    if 'holidays' not in st.session_state:
        st.session_state.holidays = []
    if 'work_hours' not in st.session_state:
        st.session_state.work_hours = DEFAULT_WORK_HOURS