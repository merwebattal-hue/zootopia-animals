# Zootopia Animals

This project generates an HTML page from animal data using Python, JSON, and an HTML template.

The goal of the project is to practice:
- Reading structured data from JSON
- Generating HTML dynamically with Python
- Applying clean HTML/CSS structure
- Using Git and GitHub with meaningful commits
- Refactoring code following best practices

---

## Project Structure

- `animals_data.json`  
  Contains the animal data used as the data source.

- `animals_template.html`  
  HTML template with placeholders and CSS styling.

- `animals_web_generator.py`  
  Python script that:
  - Loads the JSON data  
  - Optionally filters the animals  
  - Serializes each animal into semantic HTML  
  - Generates the final `animals.html` file

- `animals.html`  
  The generated HTML output (created by the script).

---

## How to Run

Make sure you are in the project directory and run:

```bash
python animals_web_generator.py
