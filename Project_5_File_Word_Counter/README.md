# Project 5: File Word Counter

## Overview
This project analyzes text files to count words and identify the most frequently used words.

## How It Works
1. User enters a filename (or multiple filenames separated by commas)
2. The program reads the file(s) and counts all words
3. Displays the total word count
4. Shows the top 5 most common words with their frequencies

## Running the Project

### Exercise Version (Single File)
```bash
python exercise.py
```

### Main Version (Multiple Files)
```bash
python main.py
```

## Example Usage

**Single file:**
```
Enter the file name: 
sample.txt
The total number of words is: 150
Most common words: 
1. the - 12 times
2. hello - 8 times
3. world - 6 times
4. python - 5 times
5. code - 4 times
```

**Multiple files (main.py only):**
```
Enter the file names(Separate with comma): 
file1.txt, file2.txt
```

## Key Concepts
- **File I/O**: Reading files using Python's `open()` function
- **String manipulation**: Splitting text into words with `.split()`
- **Counter**: Using `collections.Counter` for frequency analysis
- **Error handling**: Catching `FileNotFoundError` for missing files