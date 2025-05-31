Plagiarism Detector:
A lightweight Python script that detects plagiarism between two text documents by calculating their similarity ratio.

Features:
Compares two text files using sequence matching algorithm
Calculates similarity percentage between documents
Detects potential plagiarism based on customizable threshold
Simple command-line interface with immediate results

How It Works:
The script uses Python's built-in difflib.SequenceMatcher to analyze the text similarity between two files. It calculates a similarity ratio from 0.0 (completely different) to 1.0 (identical) and flags potential plagiarism when the ratio exceeds 50%.

Usage:
Place text files in the project directory
Replace default filenames (demo1.txt, demo2.txt) in code if needed
Run the script: python plagiarism_detector.py

Sample Output: The similarity ratio between the two files is: 0.78
Plagiarism detected

Customization:
Adjust detection threshold by modifying 0.5 in line 11
Change compared files by editing open() parameters
Modify output messages as needed

Requirements:
Python 3.x
Text files to compare (.txt format)
