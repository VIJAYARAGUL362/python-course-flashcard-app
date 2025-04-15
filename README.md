# Flashcard Language Learning App

Overview
This is a Tkinter-based flashcard application created as part of the "100 Days of Python" course by Dr. Angela Yu on Udemy. The app helps users learn German-English word pairs by displaying a German word on a flashcard, flipping to its English translation after 3 seconds, and allowing users to mark words as known or move to the next word.

Features
- Displays German words on a flashcard with a front and back design.
- Automatically flips to the English translation after 3 seconds.
- Right Button (Green Check): Marks a word as known, removes it from the learning list, and saves the updated list to words_to_learn.csv.
- Wrong Button (Red Cross): Moves to the next word without removing it.
- Loads word data from a CSV file (words_to_learn.csv or PYTHON_CAPSTONE_PROJECT_DATA.csv as a fallback).
- Clean and simple UI with a canvas-based flashcard and image buttons.

Requirements
- Python 3.x
- Required libraries:
  - tkinter (usually included with Python)
  - pandas
- Image files (located in the ./images/ directory):
  - card_front.png
  - card_back.png
  - right.png
  - wrong.png

Installation
1. Ensure Python 3.x is installed.
2. Install the required library:
   pip install pandas
3. Place the image files in an ./images/ directory relative to the script.
4. Prepare a CSV file (PYTHON_CAPSTONE_PROJECT_DATA.csv) with two columns: "German" and "English". Example:
   German,English
   Haus,House
   Baum,Tree

Usage
1. Run the script:
   python flashcard_app.py
2. The app will load words from words_to_learn.csv if it exists, or from PYTHON_CAPSTONE_PROJECT_DATA.csv otherwise.
3. A flashcard will display a German word. After 3 seconds, it flips to show the English translation.
4. Use the buttons:
   - Green Check (Right): Mark the word as known and remove it from the list.
   - Red Cross (Wrong): Move to the next word.
5. Known words are removed from words_to_learn.csv, which is updated each time you mark a word as known.

File Structure
- flashcard_app.py: The main Python script for the application.
- ./images/:
  - card_front.png: Front side of the flashcard.
  - card_back.png: Back side of the flashcard.
  - right.png: Green check button image.
  - wrong.png: Red cross button image.
- PYTHON_CAPSTONE_PROJECT_DATA.csv: Initial word list (fallback).
- words_to_learn.csv: Dynamically updated word list (created after marking words as known).

Notes
- Ensure the CSV files have the correct format (two columns: "German" and "English").
- The app assumes the image files are present in the ./images/ directory. Missing images will cause an error.
- If all words are marked as known, the app will continue to show the last word. Consider adding a "Done" message for this case (see Future Improvements).

Future Improvements
- Add a "Done" message when all words are learned.
- Validate CSV files before loading to ensure correct format.
- Add error handling for missing image files.
- Allow users to reset the word list or import new CSV files through the UI.
- Add a feature to track learning progress (e.g., number of words learned).

License
This project is a personal exercise from the "100 Days of Python" course by Dr. Angela Yu on Udemy. It is intended for educational purposes only and is not licensed for distribution or commercial use. All rights to the course content and design inspiration belong to Dr. Angela Yu and Udemy.
