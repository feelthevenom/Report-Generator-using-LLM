from datetime import datetime, timedelta

def ordinal_suffix(day):
    """
    Determine ordinal suffix for a day number (e.g., 1st, 2nd, 3rd, 4th)
    
    Args:
        day (int): The day number
        
    Returns:
        str: The appropriate suffix
    """
    if 11 <= day <= 13:
        return "th"
    elif day % 10 == 1:
        return "st"
    elif day % 10 == 2:
        return "nd"
    elif day % 10 == 3:
        return "rd"
    else:
        return "th"

def generate_date_range(start_date, end_date):
    """
    Generate a list of dates between start_date and end_date, inclusive
    
    Args:
        start_date (datetime.date): Start date
        end_date (datetime.date): End date
        
    Returns:
        list: List of datetime.date objects
    """
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    return dates

def parse_descriptions(descriptions_text, dates):
    """
    Parse text area input into a dictionary mapping dates to descriptions
    
    Args:
        descriptions_text (str): Text from the descriptions text area
        dates (list): List of dates
        
    Returns:
        dict: Dictionary mapping date objects to description strings
    """
    date_to_desc = {}
    lines = descriptions_text.split("\n")
    
    for line in lines:
        if ":" in line:
            prefix, desc = line.split(":", 1)
            parts = prefix.strip().split()
            if len(parts) >= 1:
                try:
                    day = int(parts[0])
                    # Find the corresponding date
                    for date in dates:
                        if date.day == day:
                            date_to_desc[date] = desc.strip()
                            break
                except ValueError:
                    continue  # Skip invalid lines
    
    return date_to_desc