<div align="center">

# 📝 Plagiarism Detector — Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Text%20Analysis-9cf?style=for-the-badge)
![Similarity](https://img.shields.io/badge/Text-Similarity-orange?style=for-the-badge)
![Difflib](https://img.shields.io/badge/difflib-SequenceMatcher-blueviolet?style=for-the-badge)
![CLI](https://img.shields.io/badge/CLI-Tool-grey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A lightweight Python script that detects plagiarism between two text documents by calculating their similarity ratio — no external libraries needed.**

</div>

---

## 📖 About

**Plagiarism Detector** is a simple yet effective Python tool that compares two text documents and calculates how similar they are. Using Python's built-in `difflib.SequenceMatcher`, it produces a similarity ratio between `0.0` (completely different) and `1.0` (identical), then flags potential plagiarism when the ratio exceeds a configurable threshold.

Perfect for students, teachers, or developers who need a quick, dependency-free plagiarism check tool.

---

## ⚙️ How It Works

```
[File 1: demo1.txt] ──┐
                       ├──► [SequenceMatcher] ──► Similarity Ratio ──► Verdict
[File 2: demo2.txt] ──┘         (difflib)            0.0 – 1.0
```

**Step-by-step:**
1. Both text files are read and their content is extracted
2. Python's `difflib.SequenceMatcher` compares the two texts
3. A similarity ratio is calculated (0.0 = different, 1.0 = identical)
4. If ratio **> 0.5 (50%)** → **"Plagiarism Detected"**
5. If ratio **≤ 0.5** → **"No Plagiarism Found"**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Text Comparison** | Compares any two `.txt` files |
| 📊 **Similarity Score** | Returns precise ratio from 0.0 to 1.0 |
| ⚠️ **Plagiarism Flag** | Automatically detects and reports plagiarism |
| ⚙️ **Adjustable Threshold** | Easily change the detection sensitivity |
| 🪶 **Zero Dependencies** | Uses only Python's built-in `difflib` library |
| ⚡ **Fast & Lightweight** | Runs instantly on any Python 3 environment |
| 🖥️ **CLI Interface** | Simple command-line output |

---

## 🗂️ Project Structure

```
Plagiarism-Detection----Python/
│
├── plagiarism_detector.py    # Main detection script
├── demo1.txt                 # Sample text file 1
├── demo2.txt                 # Sample text file 2
└── README.md
```

---

## 🚀 Getting Started

### Requirements
- Python 3.x (no pip installs needed!)

### Installation
```bash
# Clone the repo
git clone https://github.com/naimurhamim/Plagiarism-Detection----Python.git
cd Plagiarism-Detection----Python
```

### Run
```bash
python plagiarism_detector.py
```

---

## 📤 Sample Output

```
Comparing: demo1.txt  vs  demo2.txt
---------------------------------------
Similarity Ratio : 0.78
Result           : ⚠️  Plagiarism Detected!
```

```
Comparing: file_a.txt  vs  file_b.txt
---------------------------------------
Similarity Ratio : 0.21
Result           : ✅  No Plagiarism Found.
```

---

## 🔧 Customization

### Change the Files Being Compared
Open `plagiarism_detector.py` and edit the file names:
```python
file1 = open("your_file1.txt", "r")
file2 = open("your_file2.txt", "r")
```

### Adjust the Detection Threshold
Change the threshold value (default `0.5` = 50%):
```python
if similarity > 0.5:     # Change 0.5 to whatever you prefer
    print("Plagiarism Detected")
```

| Threshold | Sensitivity |
|---|---|
| `0.3` | High sensitivity — flags even minor similarity |
| `0.5` | Default — balanced detection |
| `0.7` | Strict — only flags very high similarity |
| `0.9` | Very strict — nearly identical only |

---

## 💡 Core Code

```python
from difflib import SequenceMatcher

def check_plagiarism(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    similarity = SequenceMatcher(None, text1, text2).ratio()
    print(f"Similarity Ratio: {similarity:.2f}")

    if similarity > 0.5:
        print("⚠️  Plagiarism Detected!")
    else:
        print("✅  No Plagiarism Found.")

check_plagiarism("demo1.txt", "demo2.txt")
```

---

## 🔮 Future Improvements

- [ ] Support for `.pdf` and `.docx` file formats
- [ ] Compare multiple files at once (batch mode)
- [ ] GUI interface with drag-and-drop
- [ ] Word-level and sentence-level highlight of matched sections
- [ ] Export report as PDF
- [ ] Web-based version using Flask

---

## 👨‍💻 Author

**MD Naimur Rashid**  
Department of Internet of Things and Robotics Engineering  
University of Frontier Technology, Bangladesh (UFTB)

[![GitHub](https://img.shields.io/badge/GitHub-naimurhamim-181717?style=for-the-badge&logo=github)](https://github.com/naimurhamim)

---

<div align="center">
  <i>⭐ Star this repo if you found the plagiarism detector useful!</i>
</div>
