# Timesheet Generator

A streamlined Streamlit application for generating professional timesheets with customizable work hours, holiday management, and task summarization.

## Features

- **Intuitive UI**: User-friendly interface for effortless timesheet creation
- **Date Range Selection**: Generate timesheets for any period
- **Holiday Management**: Define and manage holidays
- **Work Hours Configuration**: Customize start/end times and duration
- **Task Summarization**: AI-powered summarization of daily tasks using LLM
- **Excel Export**: Generate professional Excel timesheets with proper formatting
- **Preview Functionality**: See a summary of your timesheet before downloading

## Installation

### Prerequisites

- Python 3.8 or higher
- Ollama (for LLM capabilities)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/timesheet-generator.git
   cd timesheet-generator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up Ollama (for task summarization):
   - Install Ollama following instructions at [https://ollama.ai/](https://ollama.ai/)
   - Pull the required model: `ollama pull llama3.2`

## Usage

1. Start the application:
   ```
   streamlit run app.py
   ```

2. Navigate to the application in your browser (typically http://localhost:8501)

3. Configure your settings in the sidebar:
   - Set your daily work hours
   - Add any holidays

4. Fill in your information:
   - Enter employee details
   - Select date range for the timesheet
   - Add daily task descriptions

5. Generate and download your timesheet!

## Project Structure

```
timesheet-generator/
├── app.py                 # Main application entry point
├── config/
│   └── settings.py        # Application settings and defaults
├── models/
│   └── timesheet.py       # Data models for timesheet components
├── prompts/
│   └── task_summarization.py  # LLM prompt templates
├── services/
│   ├── excel_service.py   # Excel generation functionality
│   └── llm_service.py     # LLM integration for task summarization
├── ui/
│   ├── main_ui.py         # Main interface components
│   └── sidebar.py         # Sidebar interface components
└── utils/
    └── helpers.py         # Utility functions
```

## Daily Descriptions Format

Enter descriptions in the format: `day: description`

Examples:
```
1: Implemented user authentication feature using JWT tokens, tested in development environment
2: Fixed bugs in reporting module and added data validation
3: Leave - Personal
4: Weekend
5: Holiday - Labor Day
```

Special prefixes:
- `Leave`: Marks the day as leave (highlighted in yellow)
- `Holiday`: Marks the day as holiday (highlighted in orange)
- `Weekend`: Marks the day as weekend (highlighted in gray)

Weekends are automatically detected based on the day of the week.

## Customization

### Default Settings

You can modify default settings in `config/settings.py`:
- Default work hours
- Employee information
- Excel styling options
- LLM model name

### Task Summarization

The task summarization prompt can be customized in `prompts/task_summarization.py` to change how your task descriptions are processed.

## Requirements

```
streamlit
openpyxl
pandas
langchain
ollama
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

⚠️ **Warning:** Don't forget to run the ollama service in the background
