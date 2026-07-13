# DataFilterPy

DataFilterPy is a Python application that simplifies the analysis of Excel spreadsheets through an interactive terminal interface.

The application allows users to load Excel files, apply multiple filters, remove unnecessary columns, preview the filtered data, and export the final result to a new spreadsheet.

---

## Features

- Load Excel (.xlsx) files
- Filter data by one or multiple columns
- Apply multiple filters simultaneously
- Remove unwanted columns
- Preview filtered data
- Export filtered data to Excel
- Simple terminal interface

---

## Technologies

- Python 3
- Pandas
- OpenPyXL
- Tkinter

---

## Project Structure

```
src/
├── config/
├── global_context/
├── input/
├── service/
├── utils/
├── view/
└── main.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-user/DataFilterPy.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/main.py
```

---

## Workflow

1. Select an Excel file.
2. Choose one or more columns.
3. Apply filters.
4. Preview the filtered data.
5. Remove unnecessary columns (optional).
6. Export the final spreadsheet.

---

## Future Improvements

- Graphical interface
- Support for CSV files
- Advanced filters
- Filter history
- Report generation
- Charts and statistics

---

## License

This project is licensed under the MIT License.
