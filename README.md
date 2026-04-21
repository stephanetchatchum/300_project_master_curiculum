# 300-PROJECT MASTER CURRICULUM
## From Zero to Technical Mastery: A Student's Complete Playbook

---

## THE LEARNING PROTOCOL

For EVERY project, follow these 5 steps. No skipping.

### Step 1: CONCEPT (10 min)
Read the project description. Understand WHAT you're building and WHY.
Research any unfamiliar concepts. Watch one video or read one article max.

### Step 2: PLAN (15-30 min)
Write pseudocode on paper (not on screen).
Sketch the structure: What classes? What functions? What data flows where?
List the libraries you'll need.

### Step 3: BUILD (1-4 hours depending on project)
Code it yourself. No copy-paste. No AI writing code for you.
When stuck: Spend 15 minutes trying before asking for help.
When asking for help: "I tried X, got Y error, I think Z is wrong."

### Step 4: UNDERSTAND (20 min)
Add comments explaining EVERY section of your code.
If you can't explain a line, you don't understand it. Research it.
Write a README: What does this project do? How does it work? What did you learn?

### Step 5: EXERCISE (30-90 min)
Complete the exercise variation listed for each project.
This is a TWIST on the same concepts. Not a rebuild. A new challenge.
If you can do the exercise without help, you've mastered the project.

### RULES:
- No moving to the next project until Step 5 is done
- Push every completed project to GitHub with a README
- Every 10 projects: Write a reflection (what you learned, what was hard, what clicked)
- Math concepts are marked with [MATH] — don't skip them

---

## CURRICULUM MAP

| Phase     | Projects | Focus                                    | Duration         |
|-----------|----------|------------------------------------------|------------------|
| 0         | 1-25     | Python & CLI Mastery                     | 3-4 weeks        |
| 1         | 26-45    | Data Structures & Algorithms             | 3-4 weeks        |
| 2         | 46-65    | Math Foundations                         | 3-4 weeks        |
| 3         | 66-85    | Web Foundations                          | 2-3 weeks        |
| 4         | 86-110   | Backend & Databases                      | 3-4 weeks        |
| 5         | 111-130  | Frontend Frameworks (React)              | 3 weeks          |
| 6         | 131-170  | Physics & Simulations                    | 6-8 weeks        |
| 7         | 171-185  | Mobile Development                       | 2-3 weeks        |
| 8         | 186-210  | Game Development (Unity/C#)              | 4-5 weeks        |
| 9         | 211-240  | AI & Machine Learning                    | 5-6 weeks        |
| 10        | 241-255  | Scientific Computing                     | 3 weeks          |
| 11        | 256-265  | Systems & Infrastructure                 | 2 weeks          |
| 12        | 266-280  | Space & Earth Science                    | 3 weeks          |
| 13        | 281-295  | African Impact & Research                | 3-4 weeks        |
| 14        | 296-300  | Personal Capstones                       | 8-12 weeks       |
| **TOTAL** | **300**  | **Complete Technical Mastery**           | **12-18 months** |

---

# PHASE 0: PYTHON & CLI MASTERY (Projects 1-25)
*Master the language. Build confidence. Ship fast.*

### 1. Hello World Extended
**Build:** A CLI app that greets the user by name, tells the current time, and gives a random motivational quote.
**Learn:** Input/output, string formatting, importing modules (datetime, random).
**Exercise:** Add a feature that remembers the user's name using a text file, so it greets them by name next time.

### 2. Calculator CLI
**Build:** A calculator that handles +, -, *, /, power, square root, and remembers history of calculations.
**Learn:** Functions, conditionals, loops, error handling (division by zero).
**Math:** [MATH] Order of operations, floating point precision.
**Exercise:** Add parentheses support and operator precedence parsing.

### 3. Unit Converter
**Build:** Convert between units: temperature (C/F/K), distance (km/mi/m/ft), weight (kg/lb), time (hrs/min/sec).
**Learn:** Dictionaries, functions, modular design.
**Math:** [MATH] Linear transformations, conversion factors.
**Exercise:** Add currency conversion using a live API (requests library).

### 4. Number Guessing Game
**Build:** Computer picks a random number 1-100. User guesses. App says "higher" or "lower." Track attempts.
**Learn:** While loops, conditionals, random module, input validation.
**Math:** [MATH] Binary search intuition (optimal strategy halves the range).
**Exercise:** Reverse it: User picks a number, computer guesses using binary search. Show the algorithm thinking.

### 5. Hangman
**Build:** Classic word guessing game with ASCII art for the hangman figure. Word list from a file.
**Learn:** String manipulation, file I/O, lists, sets (tracking guessed letters).
**Exercise:** Add difficulty levels (easy: common words, hard: rare words) and a scoring system.

### 6. Rock Paper Scissors (Extended)
**Build:** Play against the computer. Track win/loss/draw over multiple rounds. Show statistics.
**Learn:** Random choice, game loops, dictionaries for scoring.
**Math:** [MATH] Probability: What's the expected win rate? Track actual vs expected.
**Exercise:** Add Rock Paper Scissors Lizard Spock. Then add an AI that learns your patterns (tracks your last 5 moves and exploits tendencies).

### 7. Todo List (Text File)
**Build:** Add, view, complete, and delete tasks. Save to a text file so tasks persist between runs.
**Learn:** File I/O (read/write), CRUD operations, list management.
**Exercise:** Add priorities (high/medium/low), due dates, and sorting by priority or date.

### 8. Todo List (SQLite)
**Build:** Same as Project 7, but store tasks in an SQLite database instead of a text file.
**Learn:** SQL basics (CREATE, INSERT, SELECT, UPDATE, DELETE), sqlite3 module.
**Exercise:** Add categories/tags, search by keyword, and export to CSV.

### 9. Contact Book
**Build:** Store contacts (name, phone, email, address). Add, search, edit, delete. Save to JSON file.
**Learn:** JSON serialization, dictionaries, search algorithms.
**Exercise:** Add import/export to CSV, and a "birthday reminder" feature that checks dates.

### 10. Personal Budget Tracker
**Build:** Track income and expenses by category. Show monthly summary, total balance, spending by category.
**Learn:** Data aggregation, date handling, formatted output (tables).
**Math:** [MATH] Percentage calculations, running totals, averages.
**Exercise:** Add budget limits per category and alerts when approaching the limit. Generate a monthly report.

### 11. Password Generator
**Build:** Generate passwords with customizable length, uppercase, lowercase, digits, symbols. Rate password strength.
**Learn:** String module, random.choice, command-line arguments (argparse).
**Math:** [MATH] Combinatorics: Calculate total possible passwords given constraints. Entropy calculation.
**Exercise:** Add a passphrase generator (random words from a dictionary file). Compare entropy of passwords vs passphrases.

### 12. Password Manager
**Build:** Store encrypted passwords for different services. Master password to unlock. Add, view, search, delete entries.
**Learn:** Encryption basics (hashlib, base64), secure input (getpass), file encryption.
**Exercise:** Add password expiry warnings, auto-generate passwords, and clipboard copy functionality.

### 13. File Organizer Script
**Build:** Scan a folder (e.g., Downloads) and auto-sort files into subfolders by type (images, documents, videos, code).
**Learn:** os module, pathlib, file extensions, shutil for moving files.
**Exercise:** Add a "watch mode" that monitors the folder continuously and organizes new files as they appear.

### 14. CSV Data Processor
**Build:** Read a CSV file, clean data (remove duplicates, handle missing values), compute statistics, export results.
**Learn:** csv module, data cleaning patterns, basic statistics.
**Math:** [MATH] Mean, median, mode, standard deviation, data distribution.
**Exercise:** Process a real dataset (find one on Kaggle). Generate a summary report with insights.

### 15. Markdown Note-Taking App
**Build:** Create, edit, search, and delete notes stored as .md files. Full-text search across all notes.
**Learn:** File I/O, string searching, regex basics, directory management.
**Exercise:** Add tags/categories, linking between notes (wiki-style [[note_name]]), and a "recent notes" feature.

### 16. Journal/Diary CLI
**Build:** Write daily entries with timestamps. Browse by date. Search entries. Mood tracking (rate your day 1-10).
**Learn:** Datetime module, file organization by date, data persistence.
**Math:** [MATH] Track mood over time. Calculate rolling averages. Simple trend analysis.
**Exercise:** Add mood visualization using matplotlib (line chart of mood over 30 days).

### 17. Quiz Game Engine
**Build:** Load questions from a JSON file. Multiple choice. Score tracking. Timer per question. High scores.
**Learn:** JSON parsing, timer (time module), data structures for questions.
**Exercise:** Add different question types (true/false, fill-in-blank), difficulty scaling, and categories.

### 18. Flashcard Study App
**Build:** Create decks of flashcards. Study mode with flip. Track which cards you got right/wrong. Spaced repetition.
**Learn:** Classes (Deck, Card), spaced repetition algorithm (SM-2), JSON persistence.
**Math:** [MATH] Spaced repetition intervals (exponential growth of review intervals).
**Exercise:** Implement the full SM-2 algorithm. Add statistics: mastery percentage per deck, time spent studying.

### 19. Pomodoro Timer (CLI)
**Build:** 25 min work / 5 min break cycle. Sound notification. Track completed pomodoros per day. Daily/weekly stats.
**Learn:** Time module, threading (for timer), signal handling (Ctrl+C graceful exit).
**Exercise:** Add customizable durations, long break after 4 pomodoros, and export daily stats to CSV.

### 20. Habit Tracker
**Build:** Define habits. Mark them complete each day. Streak tracking. Weekly/monthly reports.
**Learn:** Date manipulation, data persistence (JSON/SQLite), streak algorithms.
**Math:** [MATH] Streak probability: If you succeed 80% of days, what's the probability of a 7-day streak?
**Exercise:** Add habit categories, "best streak" records, and a heatmap-style calendar view (like GitHub contributions).

### 21. Stock Price Fetcher
**Build:** Fetch stock prices from a free API (yfinance or Alpha Vantage). Display current price, daily change, 52-week high/low.
**Learn:** HTTP requests, API consumption, JSON parsing, error handling for network issues.
**Math:** [MATH] Percentage change, moving averages, basic financial metrics.
**Exercise:** Add portfolio tracking (user owns X shares of Y). Calculate total portfolio value, daily gain/loss.

### 22. Weather CLI
**Build:** Fetch weather for any city using OpenWeatherMap API. Show temperature, humidity, wind, forecast.
**Learn:** API keys, query parameters, response parsing, unit conversion.
**Exercise:** Add 5-day forecast, "should I bring an umbrella?" logic, and save favorite cities.

### 23. Web Scraper
**Build:** Scrape a website (e.g., news headlines, product prices). Parse HTML. Save results to CSV.
**Learn:** requests, BeautifulSoup, HTML structure, CSS selectors.
**Exercise:** Scrape multiple pages (pagination). Add scheduling (run every hour). Detect price changes and alert.

### 24. Bash Script Collection
**Build:** Write 10+ useful bash scripts: backup files, system info, disk usage, process monitor, bulk rename, log cleaner, etc.
**Learn:** Bash syntax, pipes, grep, awk, sed, cron jobs, chmod.
**Exercise:** Create a "setup script" that installs all your dev tools on a fresh Linux machine automatically.

### 25. Text-Based Adventure Game
**Build:** A multi-room text adventure with inventory, puzzles, and branching storylines. At least 10 rooms, 3 items, 2 puzzles.
**Learn:** State machines, game design, classes (Room, Player, Item), dictionaries for world data.
**Exercise:** Add combat system, NPC dialogue, and save/load game state to JSON.

---

# PHASE 1: DATA STRUCTURES & ALGORITHMS (Projects 26-45)
*Think like a computer scientist. Solve problems efficiently.*

### 26. Linked List Implementation
**Build:** Singly and doubly linked list from scratch. Insert, delete, search, reverse, detect cycles.
**Learn:** Pointers/references, memory concepts, node-based data structures.
**Exercise:** Implement a music playlist using your linked list (next/previous song, shuffle, repeat).

### 27. Stack & Queue
**Build:** Stack (LIFO) and Queue (FIFO) from scratch. No using Python's built-in list methods as cheats.
**Learn:** Push/pop, enqueue/dequeue, when to use each.
**Exercise:** Use your stack to build a bracket validator (checks if ({[]}) is balanced). Use your queue to simulate a print queue.

### 28. Binary Search Tree (BST)
**Build:** Insert, search, delete, in-order/pre-order/post-order traversal, find min/max, height calculation.
**Learn:** Recursive algorithms, tree traversal, balanced vs unbalanced trees.
**Math:** [MATH] Time complexity: O(log n) vs O(n). When does a BST degrade to a linked list?
**Exercise:** Build an autocomplete system using your BST (insert dictionary words, search by prefix).

### 29. Hash Table from Scratch
**Build:** Implement a hash table with collision handling (chaining or open addressing). Put, get, delete, resize.
**Learn:** Hash functions, collision resolution, load factor, amortized analysis.
**Math:** [MATH] Hash function design. Why do we use prime numbers for table sizes?
**Exercise:** Build a word frequency counter using your hash table. Process a large text file and find the top 10 most common words.

### 30. Sorting Algorithms Visualizer
**Build:** Implement bubble sort, selection sort, insertion sort, merge sort, quicksort. Visualize each step with matplotlib.
**Learn:** Sorting algorithm mechanics, time/space complexity, divide and conquer.
**Math:** [MATH] Big-O analysis: O(n²) vs O(n log n). Count comparisons and swaps for each algorithm.
**Exercise:** Add heap sort and radix sort. Benchmark all algorithms on datasets of size 100, 1000, 10000. Plot performance comparison.

### 31. Graph Implementation
**Build:** Graph class supporting adjacency list and adjacency matrix. Directed and undirected. Weighted and unweighted.
**Learn:** Graph representations, when to use list vs matrix, space/time tradeoffs.
**Math:** [MATH] Graph density. When is adjacency matrix better than list? Calculate memory usage for each.
**Exercise:** Model a real network (e.g., Kigali bus routes, social network of your friends) and answer questions about it.

### 32. BFS & DFS
**Build:** Breadth-First Search and Depth-First Search on your graph. Find paths, detect cycles, find connected components.
**Learn:** Queue-based (BFS) vs stack-based (DFS) traversal, visited tracking.
**Exercise:** Build a maze solver. Generate a random maze, then solve it using BFS (shortest path) and DFS (any path). Visualize both solutions.

### 33. Dijkstra's Shortest Path
**Build:** Implement Dijkstra's algorithm with a priority queue. Find shortest path between any two nodes in a weighted graph.
**Learn:** Greedy algorithms, priority queues (heapq), shortest path trees.
**Math:** [MATH] Why doesn't Dijkstra work with negative weights? Prove the greedy choice property.
**Exercise:** Build a "cheapest flight finder" using Dijkstra. Input: cities + flight costs. Output: cheapest route between any two cities.

### 34. Dynamic Programming Collection
**Build:** Solve 10 classic DP problems: Fibonacci, climbing stairs, coin change, longest common subsequence, knapsack, edit distance, longest increasing subsequence, matrix chain multiplication, rod cutting, subset sum.
**Learn:** Memoization vs tabulation, state definition, recurrence relations.
**Math:** [MATH] Recurrence relations. Prove correctness of each DP solution.
**Exercise:** Solve 5 new DP problems from LeetCode (medium difficulty) using the patterns you learned.

### 35. Recursion Deep Dive
**Build:** Solve 10 recursive problems: factorial, power, Fibonacci, tower of Hanoi, permutations, combinations, flood fill, tree traversals, binary search, merge sort.
**Learn:** Base cases, recursive calls, call stack, tail recursion.
**Math:** [MATH] Prove correctness by induction. Draw recursion trees. Calculate stack depth.
**Exercise:** Convert 5 recursive solutions to iterative ones. Explain when recursion is better vs worse.

### 36. Binary Search Variations
**Build:** Implement 8 binary search variations: classic, first occurrence, last occurrence, ceiling, floor, rotated array search, peak finding, square root estimation.
**Learn:** Loop invariants, boundary conditions, off-by-one errors.
**Math:** [MATH] Prove O(log n) time. How many comparisons for n = 1 billion?
**Exercise:** Build a "guess the number" AI that uses binary search. It should guess any number 1-1,000,000 in at most 20 guesses. Prove why.

### 37. Two Pointer & Sliding Window
**Build:** Solve 10 problems using two pointer and sliding window techniques: two sum (sorted), container with most water, remove duplicates, max subarray sum (window), longest substring without repeating, minimum window substring.
**Learn:** Pointer manipulation, window expansion/contraction, when to use each technique.
**Exercise:** Solve 5 new problems from LeetCode using these techniques.

### 38. Heap / Priority Queue
**Build:** Min-heap and max-heap from scratch. Insert, extract-min/max, heapify, build-heap.
**Learn:** Complete binary tree property, heap invariant, array representation.
**Math:** [MATH] Prove O(log n) insert and extract. Prove O(n) build-heap (not O(n log n)).
**Exercise:** Build a task scheduler that processes highest-priority tasks first using your heap.

### 39. Trie (Prefix Tree)
**Build:** Insert words, search words, search prefixes, delete words, autocomplete (return all words with given prefix).
**Learn:** Tree-based string storage, character-by-character traversal, memory vs time tradeoff.
**Exercise:** Build a spell-checker that suggests corrections for misspelled words (using edit distance + trie lookup).

### 40. Union-Find (Disjoint Set)
**Build:** Make-set, find (with path compression), union (by rank). Detect connected components in a graph.
**Learn:** Near-constant time operations, inverse Ackermann function, practical applications.
**Math:** [MATH] Amortized analysis. Why is path compression + union by rank almost O(1)?
**Exercise:** Use Union-Find to detect if adding an edge creates a cycle. Build Kruskal's MST algorithm using it.

### 41. Backtracking Collection
**Build:** Solve N-Queens, Sudoku solver, generate all permutations, generate all subsets, word search in grid, combination sum.
**Learn:** Backtracking template, pruning, constraint satisfaction.
**Exercise:** Build a crossword puzzle solver. Given a grid with some letters filled in and a word list, fill the grid.

### 42. Greedy Algorithms Collection
**Build:** Activity selection, fractional knapsack, Huffman coding, job scheduling with deadlines, minimum platforms.
**Learn:** Greedy choice property, when greedy works vs when it fails.
**Math:** [MATH] Prove greedy correctness for activity selection using exchange argument.
**Exercise:** Build a file compression tool using Huffman coding. Compress and decompress a text file. Show compression ratio.

### 43. String Algorithms
**Build:** KMP pattern matching, Rabin-Karp, longest palindromic substring, string hashing, anagram detection.
**Learn:** Pattern matching, rolling hash, string manipulation at scale.
**Exercise:** Build a plagiarism detector that finds similar passages between two documents using string hashing.

### 44. Graph Algorithms Advanced
**Build:** Topological sort, strongly connected components (Tarjan's), minimum spanning tree (Prim's + Kruskal's), Floyd-Warshall all-pairs shortest path.
**Learn:** Advanced graph theory, algorithm design paradigms.
**Math:** [MATH] Prove MST properties. Why does cutting any edge of an MST and taking the minimum crossing edge give the same MST?
**Exercise:** Model a real-world problem as a graph and solve it: e.g., course prerequisite ordering (topological sort), network cable cost minimization (MST).

### 45. Big-O Analysis Workbook
**Build:** Analyze 20 code snippets for time and space complexity. Write your own cheat sheet with examples for O(1), O(log n), O(n), O(n log n), O(n²), O(2^n), O(n!).
**Learn:** Asymptotic analysis, best/worst/average case, amortized analysis.
**Math:** [MATH] Formal Big-O definitions. Prove that 3n² + 5n + 2 is O(n²). Master summation formulas.
**Exercise:** Profile your sorting algorithms (Project 30) with actual timing. Compare theoretical Big-O with measured performance. Explain discrepancies.

---

# PHASE 2: MATH FOUNDATIONS (Projects 46-65)
*Build mathematical intuition through code. Every concept visualized.*

### 46. Vector Operations Library
**Build:** 2D and 3D vector class. Add, subtract, scale, magnitude, normalize, dot product, cross product, angle between vectors, projection.
**Learn:** Vector algebra, geometric interpretation, coordinate systems.
**Math:** [MATH] Prove dot product = |a||b|cos(θ). Prove cross product magnitude = area of parallelogram.
**Exercise:** Build a 2D physics vector testbed: apply forces to objects, resolve collisions using vector math.

### 47. Matrix Operations Library
**Build:** Matrix class. Add, multiply, transpose, determinant (2x2, 3x3, nxn), inverse, row reduction (Gaussian elimination).
**Learn:** Matrix algebra, linear transformations, systems of equations.
**Math:** [MATH] Prove (AB)^T = B^T A^T. When does a matrix have no inverse? What does determinant = 0 mean geometrically?
**Exercise:** Use your matrix library to solve a system of 5 equations with 5 unknowns. Visualize 2D linear transformations (rotation, scaling, shearing) using matplotlib.

### 48. Systems of Linear Equations Solver
**Build:** Solve Ax = b using Gaussian elimination with partial pivoting. Handle no solution, unique solution, infinite solutions.
**Learn:** Row echelon form, back substitution, numerical stability.
**Math:** [MATH] When does a system have 0, 1, or infinite solutions? Rank of a matrix. Null space.
**Exercise:** Model a real problem as a system of equations (e.g., circuit analysis, traffic flow, chemical balancing) and solve it.

### 49. Eigenvalue & Eigenvector Visualizer
**Build:** Compute eigenvalues and eigenvectors for 2x2 and 3x3 matrices. Visualize how eigenvectors remain on their span after transformation.
**Learn:** Characteristic polynomial, eigendecomposition, geometric meaning.
**Math:** [MATH] Solve det(A - λI) = 0 by hand for 2x2 matrices. What do eigenvalues tell you about a transformation?
**Exercise:** Use eigenvalues to analyze the stability of a dynamical system (e.g., population model).

### 50. Numerical Differentiation
**Build:** Compute derivatives numerically using forward difference, backward difference, and central difference. Compare accuracy.
**Learn:** Limits, approximation, truncation error.
**Math:** [MATH] Derive the central difference formula from Taylor series. Prove it's O(h²) accurate.
**Exercise:** Differentiate sin(x), e^x, x³ numerically. Plot numerical vs analytical derivatives. Show how error changes with step size h.

### 51. Numerical Integration
**Build:** Compute definite integrals using rectangle rule, trapezoidal rule, and Simpson's rule. Compare accuracy.
**Learn:** Area under curves, approximation methods, convergence.
**Math:** [MATH] Derive Simpson's rule. Why is it more accurate than trapezoid? Error analysis.
**Exercise:** Compute π using numerical integration of the circle equation. How many subdivisions do you need for 10 decimal places?

### 52. Gradient Descent Visualizer
**Build:** Implement gradient descent for 1D and 2D functions. Visualize the path taken to the minimum. Adjustable learning rate.
**Learn:** Optimization, partial derivatives, learning rate effects, convergence.
**Math:** [MATH] Compute gradients by hand. What happens with too large/small learning rate? Local vs global minima.
**Exercise:** Use gradient descent to fit a line to noisy data points (linear regression from scratch). Visualize the loss decreasing.

### 53. Probability Simulator
**Build:** Simulate dice rolls, coin flips, card draws. Compute empirical probabilities. Compare with theoretical. Law of large numbers demonstration.
**Learn:** Random events, probability distributions, expected value, variance.
**Math:** [MATH] Prove law of large numbers intuitively. Calculate expected value of dice games. Conditional probability (Bayes' theorem).
**Exercise:** Simulate the Monty Hall problem (1000 trials). Prove that switching wins 2/3 of the time.

### 54. Statistics Library
**Build:** Implement from scratch: mean, median, mode, variance, standard deviation, percentiles, z-score, correlation coefficient, covariance.
**Learn:** Descriptive statistics, data summarization, dispersion measures.
**Math:** [MATH] Derive variance formula. Prove that σ² = E[X²] - (E[X])². Understand correlation vs causation.
**Exercise:** Analyze a real dataset (e.g., student grades, weather data). Compute all statistics. Write a report on your findings.

### 55. Probability Distributions
**Build:** Implement and visualize: uniform, normal (Gaussian), binomial, Poisson, exponential distributions. Generate random samples. Plot PDFs and CDFs.
**Learn:** Distribution shapes, parameters, when to use each.
**Math:** [MATH] Central Limit Theorem: demonstrate by sampling from ANY distribution and showing the mean converges to normal.
**Exercise:** Model a real phenomenon with distributions: e.g., customer arrivals (Poisson), test scores (normal), coin flips (binomial).

### 56. Hypothesis Testing Tool
**Build:** Implement z-test, t-test, chi-squared test. Input data, output: test statistic, p-value, conclusion (reject/fail to reject).
**Learn:** Null hypothesis, significance level, Type I/II errors, p-values.
**Math:** [MATH] What does p = 0.03 actually mean? Why is p < 0.05 the convention? Power of a test.
**Exercise:** Design and analyze an experiment: e.g., "Do students who study with music score differently?" Generate fake data, run the test, interpret results.

### 57. Linear Regression
**Build:** Implement simple and multiple linear regression from scratch (no sklearn). Least squares, R² score, residual analysis.
**Learn:** Line of best fit, minimizing error, model evaluation.
**Math:** [MATH] Derive the normal equation (A^T A)x = A^T b. Prove least squares minimizes sum of squared errors.
**Exercise:** Predict house prices using 3+ features. Plot actual vs predicted. Analyze residuals for patterns.

### 58. Fourier Transform Visualizer
**Build:** Implement DFT (Discrete Fourier Transform) from scratch. Decompose a signal into frequency components. Visualize original signal and its spectrum.
**Learn:** Frequency domain, signal decomposition, spectral analysis.
**Math:** [MATH] Euler's formula: e^(ix) = cos(x) + i*sin(x). How does DFT decompose a signal into sines and cosines?
**Exercise:** Analyze a music clip: extract dominant frequencies. Build a simple equalizer that boosts/cuts specific frequency ranges.

### 59. Complex Numbers Library
**Build:** Complex number class. Add, subtract, multiply, divide, magnitude, argument, conjugate, polar form. Visualize on Argand diagram.
**Learn:** Complex arithmetic, polar representation, roots of unity.
**Math:** [MATH] Prove e^(iπ) + 1 = 0 (Euler's identity). Find cube roots of unity. Mandelbrot set introduction.
**Exercise:** Generate and visualize the Mandelbrot set. Color by escape iteration count.

### 60. Trigonometry Visualizer
**Build:** Interactive tool showing unit circle, sin/cos/tan graphs, and their relationships. Slider for angle. Show all trig identities.
**Learn:** Circular functions, periodicity, phase shifts, amplitude.
**Math:** [MATH] Prove sin²(x) + cos²(x) = 1 geometrically. Derive double angle formulas. Understand radians vs degrees deeply.
**Exercise:** Model a Ferris wheel ride: position as a function of time using trig functions. Plot x(t) and y(t).

### 61. Coordinate System Transformer
**Build:** Convert between Cartesian, polar, cylindrical, and spherical coordinates. Visualize points in each system.
**Learn:** Coordinate systems, when to use each, transformation formulas.
**Math:** [MATH] Derive polar-to-Cartesian conversion. Why are polar coordinates better for circular motion?
**Exercise:** Plot a spiral galaxy in polar coordinates. Convert to Cartesian for 3D visualization.

### 62. Curve Fitting Tool
**Build:** Fit curves to data: linear, quadratic, polynomial, exponential, logarithmic. Show best fit with R² score.
**Learn:** Least squares fitting, overfitting, model selection.
**Math:** [MATH] What degree polynomial fits n points exactly? Why is this usually bad (overfitting)?
**Exercise:** Fit COVID-19 case data to an exponential curve (early phase) and a logistic curve (full trajectory). Compare fits.

### 63. Interpolation Methods
**Build:** Implement Lagrange interpolation, Newton's divided differences, and cubic spline interpolation. Visualize all three.
**Learn:** Passing curves through data points, smoothness, oscillation problems.
**Math:** [MATH] Runge's phenomenon: Why do high-degree polynomial interpolations oscillate? How do splines fix this?
**Exercise:** Interpolate a terrain profile from 10 measured elevation points. Compare methods for smoothness.

### 64. Optimization Algorithms
**Build:** Implement golden section search, Newton's method, BFGS (or simplified quasi-Newton). Find minima of functions.
**Learn:** Root finding, optimization, convergence rates.
**Math:** [MATH] Derive Newton's method from Taylor series. Why is it quadratically convergent? When does it fail?
**Exercise:** Optimize a real function: e.g., minimize cost of a box with fixed volume (calculus optimization problem, solved numerically).

### 65. Number Theory Toolkit
**Build:** Implement: primality testing (trial division + Miller-Rabin), Sieve of Eratosthenes, GCD (Euclidean algorithm), modular arithmetic, modular exponentiation, RSA encryption basics.
**Learn:** Prime numbers, modular arithmetic, cryptographic foundations.
**Math:** [MATH] Prove Euclidean algorithm terminates. Explain why RSA works (Euler's theorem). Fermat's little theorem.
**Exercise:** Implement a simplified RSA encryption system. Encrypt and decrypt a message using your own prime key generation.

---

# PHASE 3: WEB FOUNDATIONS (Projects 66-85)
*Build for the browser. Understand the web platform.*

### 66. HTML/CSS: Personal Portfolio
**Build:** A responsive personal portfolio site. About, projects, skills, contact sections. Mobile-friendly.
**Learn:** HTML semantics, CSS layout (flexbox, grid), responsive design, media queries.
**Exercise:** Add a dark mode toggle using CSS variables and JavaScript.

### 67. JavaScript Fundamentals
**Build:** 10 mini-projects in vanilla JS: clock, countdown timer, color picker, typing speed test, random quote generator, tip calculator, BMI calculator, age calculator, palindrome checker, morse code translator.
**Learn:** DOM manipulation, event listeners, ES6+ syntax, template literals.
**Exercise:** Combine 3 of your mini-projects into a single "utility dashboard" page.

### 68. CSS Animations & Transitions
**Build:** 5 animated components: loading spinner, animated navbar, hover card effects, scroll reveal, animated form.
**Learn:** CSS transitions, keyframes, transform, animation timing.
**Exercise:** Build a CSS-only animated scene (e.g., day-to-night sky, bouncing ball, walking character).

### 69. Responsive Design Deep Dive
**Build:** Recreate a complex webpage (e.g., news site layout) that works perfectly on mobile, tablet, and desktop.
**Learn:** Mobile-first design, breakpoints, fluid typography, responsive images.
**Exercise:** Make your portfolio (Project 66) pass Google's mobile-friendly test with a perfect score.

### 70. Weather Dashboard
**Build:** Fetch weather data from API. Show current weather, 5-day forecast, weather icons, location search.
**Learn:** Fetch API, async/await, DOM updates, error handling for network requests.
**Exercise:** Add a "weather map" showing temperature across multiple cities. Use color coding (blue=cold, red=hot).

### 71. Todo App (Vanilla JS)
**Build:** Full CRUD todo app with categories, priorities, due dates, search, filter, local storage persistence.
**Learn:** State management without frameworks, local storage API, event delegation.
**Exercise:** Add drag-and-drop reordering, bulk actions (delete completed, mark all done), and undo/redo.

### 72. Calculator (Web)
**Build:** A calculator with standard and scientific modes. History panel. Keyboard support.
**Learn:** Event handling, complex state management, CSS grid for button layout.
**Math:** [MATH] Implement order of operations correctly (PEMDAS). Handle edge cases (division by zero, overflow).
**Exercise:** Add a graphing mode: user types f(x) = ..., calculator plots the function on a canvas.

### 73. Markdown Preview Editor
**Build:** Split-pane editor: type markdown on left, see rendered HTML on right. Real-time preview.
**Learn:** Text parsing, regex, innerHTML, split-pane layout.
**Exercise:** Add syntax highlighting for code blocks, table support, and export to HTML/PDF.

### 74. Image Gallery with Lightbox
**Build:** Responsive image grid. Click to open lightbox with full-size image. Arrow key navigation. Zoom.
**Learn:** CSS grid for layout, modal overlays, keyboard events, image lazy loading.
**Exercise:** Add categories/filters, slideshow mode with auto-advance, and swipe support for mobile.

### 75. Form Validation System
**Build:** A multi-step registration form with real-time validation: email format, password strength, phone number, date of birth, file upload size check.
**Learn:** Regex for validation, custom error messages, form UX patterns.
**Exercise:** Make it accessible: screen reader compatible, keyboard navigable, ARIA attributes.

### 76. Local Storage Projects
**Build:** 3 apps using localStorage: note-taking app, theme preferences manager, reading list tracker.
**Learn:** localStorage API, JSON serialization, storage limits, data migration.
**Exercise:** Build a "storage manager" that shows what's in localStorage, lets you edit/delete entries, and warns about storage limits.

### 77. Canvas Drawing App
**Build:** A drawing application using HTML5 Canvas. Brush sizes, colors, shapes (line, rectangle, circle), undo/redo, save as image.
**Learn:** Canvas API, mouse events, drawing primitives, state history.
**Math:** [MATH] Bresenham's line algorithm. Circle drawing. Color space (RGB, HSL).
**Exercise:** Add layers, opacity, fill tool (flood fill algorithm), and text tool.

### 78. Fetch & API Integration
**Build:** Build 3 apps consuming different APIs: GitHub user search, movie database browser (OMDB), recipe finder (TheMealDB).
**Learn:** REST API consumption, pagination, rate limiting, error handling.
**Exercise:** Build an "API explorer" tool where user enters any API endpoint and sees the formatted JSON response.

### 79. CSS Grid & Flexbox Mastery
**Build:** Recreate 5 complex layouts: Pinterest-style masonry grid, holy grail layout, dashboard with sidebar, card grid with different sizes, magazine layout.
**Learn:** Grid template areas, fr units, auto-fit/auto-fill, flexbox alignment.
**Exercise:** Build a responsive email template that looks good in all email clients.

### 80. DOM Manipulation Game
**Build:** A browser game using only DOM manipulation (no canvas): whack-a-mole, memory card matching, or Simon Says.
**Learn:** SetTimeout/setInterval, DOM element creation/removal, game loop patterns.
**Exercise:** Add difficulty scaling, high scores (localStorage), sound effects, and animations.

### 81. Drag & Drop Interface
**Build:** A Kanban-style board with drag and drop. Create columns and cards. Move cards between columns.
**Learn:** HTML5 Drag and Drop API (or build from mousedown/mousemove/mouseup), data transfer.
**Exercise:** Add card editing, column reordering, and persist state to localStorage.

### 82. Search & Filter UI
**Build:** A product listing page with: text search, multi-select category filter, price range slider, sort options, pagination.
**Learn:** Client-side filtering, debouncing search input, URL query parameters.
**Exercise:** Add "faceted search" where filter counts update based on current results (like Amazon's sidebar).

### 83. Infinite Scroll & Virtualization
**Build:** A social media-style feed with infinite scroll. Load more items as user scrolls. Handle 10,000+ items efficiently.
**Learn:** Intersection Observer API, virtual scrolling, performance optimization.
**Exercise:** Implement virtual scrolling (only render visible items in DOM). Compare performance with naive approach.

### 84. Web Accessibility (WCAG)
**Build:** Audit and fix 3 existing projects for accessibility. Screen reader testing. Keyboard navigation. Color contrast. ARIA attributes.
**Learn:** WCAG 2.1 guidelines, semantic HTML, focus management, accessibility testing tools.
**Exercise:** Build a fully accessible form wizard that can be completed entirely by keyboard and screen reader.

### 85. Progressive Web App
**Build:** Convert one of your web apps into a PWA. Service worker for offline support, manifest for installability, push notifications.
**Learn:** Service workers, cache strategies, app manifest, background sync.
**Exercise:** Make it work fully offline with data sync when connection returns.

---

# PHASE 4: BACKEND & DATABASES (Projects 86-110)
*Build real servers. Design real databases. Handle real data.*

### 86. SQL Fundamentals
**Build:** Solve 30 SQL challenges: SELECT, WHERE, JOIN (inner/left/right/full), GROUP BY, HAVING, subqueries, window functions, CTEs.
**Learn:** Relational databases, query optimization, data retrieval patterns.
**Math:** [MATH] Set theory: UNION, INTERSECT, EXCEPT. Relational algebra.
**Exercise:** Design and query a database for a university: students, courses, enrollments, grades, professors.

### 87. PostgreSQL: E-Commerce Schema
**Build:** Design a complete e-commerce database: products, categories, users, orders, order items, reviews, inventory, shipping.
**Learn:** Normalization (1NF, 2NF, 3NF), indexes, foreign keys, constraints.
**Exercise:** Write 10 complex queries: best-selling products, customer lifetime value, inventory alerts, revenue by month, etc.

### 88. Flask: Hello World API
**Build:** A simple Flask API with 5 endpoints: GET/POST/PUT/DELETE for a resource, plus health check.
**Learn:** Routes, HTTP methods, request/response, JSON serialization, status codes.
**Exercise:** Add input validation, error handling (custom error responses), and request logging.

### 89. Flask: Todo API
**Build:** Full CRUD API for todos with categories, priorities, due dates, completion status. SQLite backend.
**Learn:** Flask-SQLAlchemy, database models, query building, API design.
**Exercise:** Add pagination, sorting, filtering by status/category/date, and search.

### 90. Flask: Blog API
**Build:** Blog API with posts, comments, tags, authors. Markdown content. Published/draft status.
**Learn:** One-to-many and many-to-many relationships, nested serialization.
**Exercise:** Add full-text search, post analytics (views, read time), and related posts recommendation.

### 91. Flask: User Authentication
**Build:** Registration, login, logout, password reset. JWT tokens. Protected routes. Role-based access (admin/user).
**Learn:** Password hashing (bcrypt), JWT creation/verification, middleware, security best practices.
**Exercise:** Add email verification, refresh tokens, account lockout after failed attempts, and password strength requirements.

### 92. Flask: File Upload Service
**Build:** Upload, store, retrieve, and delete files. Image resizing. File type validation. Storage limits per user.
**Learn:** Multipart form data, file handling, image processing (Pillow), cloud storage basics.
**Exercise:** Add image thumbnails, PDF preview generation, and virus/malware scanning (basic file type checks).

### 93. Django: REST API
**Build:** Full Django REST Framework API for a notes app. CRUD, authentication, permissions, filtering, pagination.
**Learn:** DRF serializers, viewsets, routers, permissions classes, throttling.
**Exercise:** Add nested serializers (notes with tags), custom permissions, and API versioning.

### 94. Django: Blog with Admin
**Build:** Blog with Django admin interface. Posts, categories, tags, comments, media uploads. Custom admin actions.
**Learn:** Django ORM, admin customization, model managers, signals.
**Exercise:** Add scheduled post publishing, comment moderation workflow, and RSS feed generation.

### 95. Django: E-Commerce Backend
**Build:** Products, categories, cart, orders, checkout flow, inventory management. Admin dashboard for order management.
**Learn:** Complex model relationships, transaction handling, business logic layer.
**Exercise:** Add coupon/discount system, wishlist, product reviews, and order status email notifications.

### 96. Database Indexing & Optimization
**Build:** Take an existing database, add indexes strategically, optimize slow queries. Benchmark before and after.
**Learn:** B-tree indexes, composite indexes, EXPLAIN/ANALYZE, query planning.
**Math:** [MATH] B-tree depth: For n records, how deep is the index tree? How many disk reads for a lookup?
**Exercise:** Create a database with 1 million records. Find the 5 slowest queries. Optimize them to be 10x faster.

### 97. Database Migration Strategies
**Build:** Implement schema migrations: add columns, rename tables, split tables, data migration scripts. Use Alembic or Django migrations.
**Learn:** Migration planning, rollback strategies, zero-downtime migrations.
**Exercise:** Migrate a single-table design to a normalized multi-table design without data loss.

### 98. WebSocket Chat Server
**Build:** Real-time chat with rooms, user presence (online/offline), typing indicators, message history.
**Learn:** WebSocket protocol, Flask-SocketIO or Django Channels, real-time state management.
**Exercise:** Add private messaging, file sharing, message reactions, and "read" receipts.

### 99. Task Queue System
**Build:** Background task processing with Celery + Redis. Schedule emails, process uploads, generate reports asynchronously.
**Learn:** Message brokers, worker processes, task scheduling, retry logic.
**Exercise:** Build a report generation system: user requests report, system processes in background, notifies when ready.

### 100. REST API Design Patterns
**Build:** Implement a comprehensive API following best practices: HATEOAS, resource naming, versioning, pagination, filtering, error format, rate limiting, caching headers.
**Learn:** REST maturity model, API design principles, documentation.
**Exercise:** Document your API using OpenAPI/Swagger. Generate a client SDK automatically.

### 101. GraphQL API
**Build:** A GraphQL API (Django + Graphene or Flask + Ariadne) for a social media app. Queries, mutations, subscriptions.
**Learn:** Schema definition, resolvers, N+1 problem, batching (DataLoader).
**Exercise:** Build the same API in both REST and GraphQL. Compare: number of endpoints, data fetching efficiency, client complexity.

### 102. OAuth 2.0 Implementation
**Build:** "Login with Google" and "Login with GitHub" for your app. Handle tokens, user creation, session management.
**Learn:** OAuth 2.0 flow, authorization codes, access/refresh tokens, PKCE.
**Exercise:** Add "Login with Twitter" and implement account linking (merge OAuth accounts with email accounts).

### 103. Payment Integration
**Build:** Integrate Stripe (or Pesapal for African context). Handle checkout, webhooks, subscription billing, refunds.
**Learn:** Payment flow, idempotency, webhook verification, PCI compliance basics.
**Exercise:** Build a subscription system with free trial, upgrade/downgrade, usage-based billing, and invoice generation.

### 104. Email Service
**Build:** Send transactional emails (welcome, password reset, order confirmation). HTML email templates. Queue-based sending.
**Learn:** SMTP, email templates (Jinja2), email deliverability, unsubscribe handling.
**Exercise:** Build a newsletter system with subscriber management, template editor, and open/click tracking.

### 105. Unit Testing for APIs
**Build:** Write comprehensive tests for one of your APIs: unit tests, integration tests, fixture management, test database, mocking external services.
**Learn:** pytest, fixtures, mocking, test coverage, TDD workflow.
**Exercise:** Achieve 90%+ test coverage. Add property-based testing (hypothesis library) for edge cases.

### 106. Integration Testing
**Build:** End-to-end tests for your full-stack app. Test API + database + authentication together. CI integration.
**Learn:** Test isolation, database transactions in tests, API client testing.
**Exercise:** Set up a test matrix: test against SQLite (fast) and PostgreSQL (production-like). Compare results.

### 107. Load Testing
**Build:** Load test one of your APIs with Locust. Simulate 100, 500, 1000 concurrent users. Identify bottlenecks.
**Learn:** Concurrency, throughput, latency, percentile metrics (p50, p95, p99).
**Exercise:** Optimize your API to handle 2x the initial load. Document what you changed and why.

### 108. API Rate Limiting
**Build:** Implement rate limiting middleware: per-user, per-IP, sliding window. Return 429 Too Many Requests with retry-after header.
**Learn:** Token bucket algorithm, sliding window counter, distributed rate limiting.
**Math:** [MATH] Token bucket: If bucket holds 10 tokens and refills at 1/sec, what's the max burst? What's sustained throughput?
**Exercise:** Implement tiered rate limits (free: 100/hr, premium: 1000/hr) with different quotas per API key.

### 109. Database Backup & Recovery
**Build:** Automated backup system: scheduled backups, compression, remote storage, integrity verification, point-in-time recovery.
**Learn:** pg_dump, cron scheduling, backup rotation, disaster recovery planning.
**Exercise:** Simulate a database failure. Restore from backup. Document the recovery procedure step by step.

### 110. Logging & Error Tracking
**Build:** Structured logging system for your API. Log levels, request IDs, error tracking, performance metrics. Dashboard for viewing logs.
**Learn:** Python logging module, structured logging (JSON), log aggregation, alerting.
**Exercise:** Set up error alerting: when an API endpoint returns 500, send a notification with the error details.

---

# PHASE 5: FRONTEND FRAMEWORKS (Projects 111-130)
*Build modern UIs. Manage complex state. Think in components.*

### 111. React: Counter App
**Build:** Counter with increment, decrement, reset. Display count. Use functional components and hooks.
**Learn:** JSX, useState, event handlers, component structure.
**Exercise:** Add multiple counters, a global total, and undo/redo for all counter actions.

### 112. React: Todo App
**Build:** Full-featured todo with categories, priorities, due dates, search, filter. State management with useReducer.
**Learn:** useReducer, useEffect, component composition, lifting state.
**Exercise:** Add optimistic updates, undo delete (with 5-second timer), and drag-and-drop reordering.

### 113. React: E-Commerce Product Page
**Build:** Product listing, category filter, price sort, cart sidebar, quantity selector, cart total.
**Learn:** Props drilling, Context API, derived state, conditional rendering.
**Exercise:** Add wishlist, product comparison (select 2-3 products, show side-by-side), and recently viewed.

### 114. React: Blog Frontend
**Build:** Blog with post list, single post view, comment section, author profiles. Fetch from your Flask/Django API.
**Learn:** React Router, data fetching (useEffect), loading/error states, URL parameters.
**Exercise:** Add pagination, infinite scroll, search, and "reading time" estimation.

### 115. React: Data Visualization Dashboard
**Build:** Dashboard with 4-6 charts (bar, line, pie, scatter). Date range selector. Real-time data refresh.
**Learn:** Chart libraries (Recharts or Chart.js), data transformation, responsive charts.
**Math:** [MATH] Choose appropriate chart types for data. When is a pie chart misleading? When is a log scale appropriate?
**Exercise:** Build a COVID-19 dashboard showing cases by country, timeline, and comparison charts.

### 116. React: Kanban Board
**Build:** Trello-style board. Create boards, columns, cards. Drag and drop cards between columns. Card details modal.
**Learn:** Complex state management, drag-and-drop (react-dnd), modal patterns.
**Exercise:** Add card labels, due dates, assignees, activity log, and board templates.

### 117. React: Expense Splitter
**Build:** Add expenses, split between people, calculate who owes whom. Support equal, percentage, and exact splits.
**Learn:** Form handling, complex calculations, derived state, input validation.
**Math:** [MATH] Graph-based debt simplification: minimize number of transactions. This is a real graph theory problem.
**Exercise:** Add group management, currency conversion, receipt photo upload, and export to PDF.

### 118. React: Search UI with Filters
**Build:** Search interface with debounced input, faceted filters, result highlighting, sort options, URL-synchronized state.
**Learn:** Debouncing, URL search params, performance optimization (React.memo, useMemo).
**Exercise:** Add search suggestions (autocomplete), search history, and "did you mean?" fuzzy matching.

### 119. React: Real-Time Chat
**Build:** Chat app with rooms, user list, typing indicators, message timestamps, emoji picker. WebSocket connection.
**Learn:** WebSocket integration in React, real-time state updates, optimistic rendering.
**Exercise:** Add message reactions, file sharing, message threading, and unread message counts.

### 120. React: Admin Dashboard
**Build:** Admin panel with data tables (sortable, filterable, paginated), CRUD modals, bulk actions, user management.
**Learn:** Table components, modal management, form builders, role-based UI.
**Exercise:** Add export to CSV/PDF, audit log viewer, and dashboard analytics (charts on admin data).

### 121. React + Flask: Full-Stack Blog
**Build:** Complete blog: React frontend + Flask API. Authentication, CRUD, comments, image upload, Markdown support.
**Learn:** Full-stack integration, CORS, deployment, environment variables.
**Exercise:** Add server-side rendering (or static generation), SEO optimization, and deploy to a cloud provider.

### 122. React + Django: Full-Stack E-Commerce
**Build:** Complete e-commerce: React frontend + Django API. Product catalog, cart, checkout, order history, admin panel.
**Learn:** Complex full-stack workflows, payment integration, email notifications.
**Exercise:** Add product search with filters, user reviews, wishlist, and order tracking.

### 123. State Management Deep Dive
**Build:** Rebuild your Todo app using 4 different state management approaches: useState, useReducer, Context API, and Redux Toolkit. Compare.
**Learn:** When to use each approach, tradeoffs, boilerplate vs simplicity.
**Exercise:** Write a blog post comparing all 4 approaches with code examples, pros/cons, and your recommendation.

### 124. React Performance Optimization
**Build:** Take your heaviest React app. Profile it. Optimize: React.memo, useMemo, useCallback, code splitting, lazy loading, virtual lists.
**Learn:** React DevTools profiler, render cycle, memoization, bundle analysis.
**Exercise:** Reduce initial load time by 50%. Document every optimization and its measured impact.

### 125. React Custom Hooks
**Build:** Create 10 reusable custom hooks: useLocalStorage, useFetch, useDebounce, useMediaQuery, useOnClickOutside, useKeyPress, useIntersectionObserver, useToggle, usePrevious, useEventListener.
**Learn:** Hook composition, abstraction, reusability, testing hooks.
**Exercise:** Publish your hooks as an npm package. Write documentation and usage examples for each.

### 126. React Testing
**Build:** Write comprehensive tests for one of your React apps: component tests, integration tests, snapshot tests, user event tests.
**Learn:** Jest, React Testing Library, user-centric testing philosophy, mocking.
**Exercise:** Achieve 85%+ test coverage. Add visual regression testing (screenshot comparison).

### 127. React: Weather App
**Build:** Beautiful weather app with: current weather, hourly forecast, 7-day forecast, weather animations, location detection.
**Learn:** Geolocation API, complex UI state, CSS animations tied to data.
**Exercise:** Add weather alerts, "what to wear" suggestions based on weather, and historical weather comparison.

### 128. React: Portfolio Template
**Build:** A reusable portfolio template that can be configured via a JSON file. Themes, layouts, sections are all customizable.
**Learn:** Config-driven UI, theming, component abstraction.
**Exercise:** Deploy 3 different portfolios using the same template with different configs. Make it a template others can use.

### 129. React: File Manager
**Build:** A web-based file manager: folder tree, file list, preview (images, text, PDF), upload, download, rename, delete.
**Learn:** Tree data structures in UI, file type detection, preview rendering.
**Exercise:** Add drag-and-drop upload, multi-select, bulk operations, and breadcrumb navigation.

### 130. React: Music Player
**Build:** Web music player: playlist management, play/pause/next/previous, progress bar, volume control, shuffle, repeat.
**Learn:** HTML5 Audio API, media controls, playlist state management.
**Math:** [MATH] Audio visualization: FFT of audio data to create a visualizer (frequency bars).
**Exercise:** Add audio visualization (frequency bars or waveform), equalizer, and crossfade between tracks.

---

# PHASE 6: PHYSICS & SIMULATIONS (Projects 131-170)
*Simulate the real world. Master computational physics.*

### 131. Vector Math Visualizer
**Build:** Interactive 2D visualization. Two vectors with sliders. Display magnitude, dot product, angle, cross product. Real-time updates.
**Learn:** Vector operations, matplotlib interactivity, geometric interpretation.
**Math:** [MATH] All vector operations. Prove geometric meanings of dot and cross product.
**Exercise:** Add vector projection visualization. Show the projection of V1 onto V2 with a dashed line.

### 132. Projectile Motion Simulator
**Build:** Launch a projectile at an angle. Show trajectory. Sliders for angle, speed, gravity. Display stats (range, max height, time).
**Learn:** Kinematic equations, time-stepping, parametric curves.
**Math:** [MATH] Derive range formula: R = v²sin(2θ)/g. Prove 45° gives maximum range.
**Exercise:** Add air resistance (drag proportional to velocity squared). Compare trajectories with and without drag.

### 133. Pendulum Simulator
**Build:** Animated pendulum swinging. Sliders for angle, length, gravity. START/STOP buttons. Real-time animation.
**Learn:** Differential equations, Euler integration, angular motion, energy conservation.
**Math:** [MATH] Derive pendulum equation from Newton's second law. Small angle approximation: when is sin(θ) ≈ θ?
**Exercise:** Build a double pendulum (chaotic system). Show how tiny changes in initial conditions lead to wildly different trajectories.

### 134. Particle System (N-Body Gravity)
**Build:** Simulate N particles attracting each other gravitationally. Visualize orbits, collisions, clustering.
**Learn:** Newton's law of gravitation, force accumulation, O(n²) pairwise interactions.
**Math:** [MATH] Gravitational force: F = G*m1*m2/r². Energy conservation: verify total energy stays constant.
**Exercise:** Simulate the inner solar system (Sun, Mercury, Venus, Earth, Mars). Compare your orbits to real data.

### 135. Wave Equation Solver (1D)
**Build:** Simulate a vibrating string. Visualize standing waves, traveling waves, reflection at boundaries.
**Learn:** Partial differential equations, finite difference methods, boundary conditions.
**Math:** [MATH] Wave equation: ∂²u/∂t² = c²∂²u/∂x². What determines wave speed? Wavelength? Frequency?
**Exercise:** Simulate two waves colliding. Show constructive and destructive interference.

### 136. Heat Diffusion Simulation
**Build:** 2D heat equation on a plate. Set hot/cold boundaries. Watch temperature spread over time. Color map visualization.
**Learn:** Diffusion equation, explicit vs implicit methods, stability conditions (CFL).
**Math:** [MATH] Heat equation: ∂u/∂t = α∇²u. Why does explicit method require small time steps? Derive stability condition.
**Exercise:** Simulate heat flow through a wall with insulation. Compare insulated vs non-insulated heat loss.

### 137. Orbital Mechanics (Kepler)
**Build:** Simulate planetary orbits. Elliptical trajectories, orbital periods, Kepler's three laws demonstration.
**Learn:** Central force motion, conservation of angular momentum, energy orbits.
**Math:** [MATH] Kepler's laws: Prove equal areas in equal times. Derive orbital period from semi-major axis.
**Exercise:** Simulate a Hohmann transfer orbit (spacecraft transferring between two circular orbits).

### 138. Collision Detection Suite
**Build:** Implement collision detection for: point-circle, circle-circle, AABB-AABB, circle-AABB, point-polygon, polygon-polygon (SAT).
**Learn:** Geometric intersection tests, separating axis theorem, spatial partitioning.
**Math:** [MATH] SAT: Why does checking all edge normals guarantee detection? Prove it.
**Exercise:** Build a simple 2D game using your collision detection: bouncing balls in a box with obstacles.

### 139. Fluid Dynamics (Shallow Water)
**Build:** 2D shallow water equations. Simulate waves, ripples, and flow around obstacles. Color-coded height map.
**Learn:** Conservation laws, numerical flux, grid-based simulation.
**Math:** [MATH] Shallow water equations: continuity + momentum. What assumptions simplify Navier-Stokes to shallow water?
**Exercise:** Simulate a tsunami: initial displacement of water, wave propagation, interaction with coastline.

### 140. Cellular Automaton
**Build:** Conway's Game of Life with customizable rules, grid size, and speed. Pattern library (glider, spaceship, pulsar). Step and run modes.
**Learn:** Emergent behavior, rule-based systems, grid computation.
**Math:** [MATH] Turing completeness: Game of Life can compute anything. What does that mean?
**Exercise:** Implement 3 other cellular automata: Rule 110, Langton's Ant, and Brian's Brain. Compare emergent behaviors.

### 141. 2D Rigid Body Physics Engine
**Build:** Circles and rectangles with mass, velocity, forces. Gravity, collision response, friction. No external physics library.
**Learn:** Newton's laws in code, impulse-based collision, rotational dynamics.
**Math:** [MATH] Impulse: J = Δp. Coefficient of restitution. Moment of inertia.
**Exercise:** Stack boxes on top of each other. They should settle under gravity and not penetrate.

### 142. Spring & Damping System
**Build:** Mass on a spring. Oscillation, damping (underdamped, critically damped, overdamped). Energy plot.
**Learn:** Hooke's law, damping coefficient, resonance, energy dissipation.
**Math:** [MATH] Derive: F = -kx - bv. Solve analytically for underdamped case. Compare numerical vs analytical.
**Exercise:** Build a suspension bridge model: multiple masses connected by springs. Apply force and watch it oscillate.

### 143. Rope/Chain Simulator
**Build:** A rope made of connected particles with distance constraints. Grab and drag one end. Verlet integration.
**Learn:** Constraint-based dynamics, position-based physics, iterative solvers.
**Math:** [MATH] Verlet integration: Why is it more stable than Euler for constraints? Derive from Taylor series.
**Exercise:** Hang a heavy weight from the middle of the rope. Show how the rope deforms. Add wind force.

### 144. Cloth Simulation
**Build:** 2D grid of particles connected by springs. Pin corners. Apply gravity and wind. Watch it drape.
**Learn:** Mass-spring networks, structural/shear/bend springs, constraint relaxation.
**Exercise:** Tear the cloth: if a spring stretches beyond a threshold, break it. Watch the cloth rip.

### 145. Soft Body Physics
**Build:** Deformable objects (circles/blobs) that squish on impact and bounce back. Internal pressure model.
**Learn:** Pressure-based soft bodies, volume conservation, deformation.
**Math:** [MATH] Pressure: P = F/A. How does internal pressure resist deformation?
**Exercise:** Drop soft bodies of different stiffness onto a surface. Compare deformation patterns.

### 146. Buoyancy & Fluid Resistance
**Build:** Objects sinking, floating, or bobbing in water. Drag force proportional to velocity.
**Learn:** Archimedes' principle, drag coefficient, terminal velocity.
**Math:** [MATH] Buoyancy: F_b = ρ_fluid × V_submerged × g. When does an object float vs sink?
**Exercise:** Simulate a submarine: adjust ballast to control depth. Add propulsion and steering.

### 147. Friction Models
**Build:** Static, kinetic, and rolling friction. Objects on slopes. Demonstrate the difference between static and kinetic friction.
**Learn:** Friction coefficient, normal force, angle of repose.
**Math:** [MATH] At what slope angle does the object start sliding? Derive: tan(θ) = μ_s.
**Exercise:** Simulate a bowling alley: ball transitions from sliding to rolling. Show energy transfer.

### 148. Constraint Solver (Verlet Integration)
**Build:** Position-based dynamics engine. Distance constraints, angle constraints, contact constraints. Iterative solver.
**Learn:** Verlet integration, constraint projection, Jacobi vs Gauss-Seidel iteration.
**Math:** [MATH] Convergence: How many iterations are needed? How does iteration count affect accuracy?
**Exercise:** Build a ragdoll using Verlet constraints. Drop it from a height. Watch it flop realistically.

### 149. Impact & Impulse Resolution
**Build:** Collision response system: bouncing, stacking, sliding. Restitution coefficient. Momentum conservation.
**Learn:** Impulse-based resolution, coefficient of restitution, energy loss in collisions.
**Math:** [MATH] Prove momentum is conserved: m1*v1 + m2*v2 = m1*v1' + m2*v2'. Derive post-collision velocities.
**Exercise:** Simulate Newton's cradle (5 balls). Show energy transfer through the chain.

### 150. Ragdoll Physics
**Build:** Articulated body with joint constraints. Drop from height. Realistic floppy motion.
**Learn:** Joint limits, angular constraints, body part hierarchy.
**Exercise:** Add interaction: click and drag body parts. Throw the ragdoll. Apply forces.

### 151. Weather System Simulator
**Build:** Simple weather model: wind fields, pressure systems, temperature advection. Visualize with arrows and color maps.
**Learn:** Vector fields, advection, coupled systems.
**Math:** [MATH] Divergence and curl: What do they mean physically for wind fields?
**Exercise:** Add moisture and precipitation. When does it rain? (Hint: rising air cools, water condenses.)

### 152. Crowd Simulation (Boids)
**Build:** Simulate a crowd using Reynolds' boids rules: separation, alignment, cohesion. Add obstacles.
**Learn:** Emergent behavior from simple rules, spatial hashing for neighbor lookup.
**Exercise:** Add "panic mode" where agents flee from a point. Compare orderly vs chaotic evacuation.

### 153. Traffic Flow Model
**Build:** Cars on a road following distance-based rules. Simulate traffic jams from nothing (phantom jams).
**Learn:** Agent-based modeling, emergent congestion, follow-the-leader models.
**Math:** [MATH] Fundamental diagram: flow vs density. At what density does traffic jam?
**Exercise:** Add traffic lights. Optimize light timing to maximize throughput. Compare fixed vs adaptive timing.

### 154. Ecosystem Simulation
**Build:** Predator-prey model (Lotka-Volterra). Foxes and rabbits. Population oscillations. Visualize populations over time.
**Learn:** Coupled differential equations, equilibrium points, stability.
**Math:** [MATH] Lotka-Volterra equations. Find equilibrium point. Is it stable?
**Exercise:** Add a third species (grass). Create a food chain. How does it affect stability?

### 155. Pandemic Spread Simulator
**Build:** SIR/SEIR model on a spatial grid. Agents move, infect nearby agents. Visualize spread. Add interventions (quarantine, vaccination).
**Learn:** Epidemiological models, R0 (basic reproduction number), herd immunity.
**Math:** [MATH] SIR equations. Calculate R0. At what vaccination rate does epidemic stop? Derive herd immunity threshold.
**Exercise:** Compare different intervention strategies: lockdown vs mask mandate vs vaccination. Which saves more lives per dollar?

### 156. Forest Fire Spread
**Build:** Cellular automaton for fire spread. Trees, burning trees, empty cells. Wind direction affects spread probability.
**Learn:** Percolation theory, probabilistic cellular automata, spatial patterns.
**Math:** [MATH] Percolation threshold: At what tree density does fire spread across the entire grid?
**Exercise:** Add firebreaks (rows of empty cells). How wide must a firebreak be to stop fire?

### 157. River & Erosion Simulation
**Build:** Water flows downhill on a heightmap. Erodes terrain over time. Deposits sediment in valleys.
**Learn:** Hydraulic erosion, sediment transport, terrain modification.
**Exercise:** Start with a flat terrain. Run erosion for 1000 steps. Show river valleys forming from nothing.

### 158. Galaxy Formation
**Build:** N-body gravitational simulation with 1000+ particles. Dark matter halo. Star formation regions. Spiral arm emergence.
**Learn:** Large-scale N-body simulation, Barnes-Hut algorithm (O(n log n)), spatial tree structures.
**Math:** [MATH] Barnes-Hut: Why can distant particle groups be treated as single masses? Multipole expansion intuition.
**Exercise:** Simulate two galaxies colliding. Show tidal tails and merger dynamics.

### 159. Molecular Dynamics
**Build:** Simulate atoms interacting via Lennard-Jones potential. Phase transitions: solid → liquid → gas with temperature changes.
**Learn:** Interatomic potentials, thermodynamics, statistical mechanics basics.
**Math:** [MATH] Lennard-Jones potential: V(r) = 4ε[(σ/r)¹² - (σ/r)⁶]. Why the two terms? What does each represent?
**Exercise:** Compute temperature from kinetic energy. Show Maxwell-Boltzmann velocity distribution emerging from simulation.

### 160. Earthquake Simulation
**Build:** Stress accumulation on a fault line. Rupture when threshold exceeded. Wave propagation. Aftershocks.
**Learn:** Elastic rebound theory, seismic waves, Gutenberg-Richter law.
**Math:** [MATH] Magnitude scale is logarithmic: each unit = 10x amplitude. What does that mean for energy?
**Exercise:** Add building response: which buildings survive based on their resonant frequency vs earthquake frequency?

### 161. Chemical Reaction Network
**Build:** Simulate chemical reactions: A + B → C with reaction rates. Multiple coupled reactions. Equilibrium.
**Learn:** Reaction kinetics, rate equations, equilibrium constants.
**Math:** [MATH] Rate law: d[A]/dt = -k[A][B]. What determines equilibrium? Le Chatelier's principle.
**Exercise:** Simulate Belousov-Zhabotinsky reaction (oscillating chemical reaction). Show spiraling patterns.

### 162. Space Debris Tracking
**Build:** Simulate objects in Earth orbit. Different altitudes, speeds, inclinations. Detect close approaches.
**Learn:** Orbital mechanics, conjunction analysis, Keplerian elements.
**Math:** [MATH] Orbital velocity: v = √(GM/r). At what altitude is a geostationary orbit?
**Exercise:** Simulate a collision event: debris field expands. Track cascading collision risk (Kessler syndrome).

### 163. Procedural Terrain Generation
**Build:** Generate realistic terrain using noise functions. Mountains, valleys, rivers, coastlines. 3D visualization.
**Learn:** Perlin noise, fractal brownian motion, terrain features from noise octaves.
**Math:** [MATH] Fractal dimension: How does adding octaves change terrain roughness? What is self-similarity?
**Exercise:** Generate an island: terrain + erosion + water level. Add biomes based on altitude and moisture.

### 164. Perlin/Simplex Noise
**Build:** Implement Perlin noise and Simplex noise from scratch. 1D, 2D, 3D. Visualize as terrain, clouds, textures.
**Learn:** Gradient noise, interpolation, octave layering.
**Math:** [MATH] Why is Simplex noise faster than Perlin in higher dimensions? Compare computational complexity.
**Exercise:** Use your noise to generate: terrain heightmap, cave system (3D threshold), cloud texture, wood grain texture.

### 165. Fluid Solver (Eulerian)
**Build:** Grid-based 2D fluid solver. Advection, diffusion, pressure solve. Visualize velocity field and dye.
**Learn:** Navier-Stokes equations (simplified), pressure projection, stable fluids method.
**Math:** [MATH] Navier-Stokes: What does each term mean physically? Why is incompressibility important?
**Exercise:** Simulate smoke rising from a source. Add obstacles for the fluid to flow around.

### 166. Smoke & Fire Simulation
**Build:** Buoyancy-driven smoke simulation. Temperature field, density field, velocity field. Rising smoke with turbulence.
**Learn:** Buoyancy force, vorticity confinement, advection of density.
**Exercise:** Simulate a campfire: fire source at bottom, smoke rising and dissipating. Add wind.

### 167. Ocean Waves (Gerstner)
**Build:** Simulate ocean surface using Gerstner waves. Multiple wave components. Choppy vs calm seas.
**Learn:** Wave superposition, Gerstner wave equations, Fourier-based ocean.
**Math:** [MATH] Gerstner waves: Why do particle paths trace circles? How does wavelength affect wave shape?
**Exercise:** Add a floating object: it should bob up and down following the wave surface.

### 168. Vehicle Suspension Physics
**Build:** Car suspension model: springs, dampers, wheels on uneven terrain. Show chassis responding to bumps.
**Learn:** Spring-damper systems, ride comfort, resonance frequency.
**Math:** [MATH] Natural frequency: f = (1/2π)√(k/m). When does resonance occur? Why is it dangerous?
**Exercise:** Design an optimal suspension: minimize chassis acceleration while maintaining tire contact. This is a real engineering optimization.

### 169. Hair/Rope Physics
**Build:** Simulate hair strands or ropes using chain of particles with constraints. Apply gravity and wind.
**Learn:** Chain dynamics, constraint iteration, rendering curves through particles.
**Exercise:** Simulate a character's ponytail responding to head movement. Add collision with the head sphere.

### 170. Bouncing Ball Collection
**Build:** Advanced bouncing ball simulation: spin, Magnus effect, wall friction, multiple balls, different materials.
**Learn:** Rotational dynamics, spin-velocity coupling, material properties.
**Math:** [MATH] Magnus effect: spinning ball curves in flight. F_magnus = ω × v. Derive direction of curve.
**Exercise:** Simulate a ping-pong game: two paddles, ball with spin. Spin affects bounce angle and trajectory.

---

# PHASE 7: MOBILE DEVELOPMENT (Projects 171-185)
*Build for phones. Think mobile-first.*

### 171. React Native: Counter App
**Build:** Counter with increment, decrement, reset. Navigation between screens. Platform-specific styling.
**Learn:** React Native basics, Expo, navigation, native components.
**Exercise:** Add haptic feedback on button press, animated count change, and dark mode.

### 172. React Native: Todo App
**Build:** Todo list with AsyncStorage persistence. Categories, swipe-to-delete, pull-to-refresh.
**Learn:** AsyncStorage, FlatList, gesture handling, local persistence.
**Exercise:** Add notifications for due tasks, widget for home screen, and sync between devices (cloud backup).

### 173. React Native: Weather App
**Build:** Weather app with location detection, current conditions, forecast, weather animations.
**Learn:** Geolocation, API integration on mobile, animated components.
**Exercise:** Add severe weather alerts, hourly forecast slider, and weather-based wallpaper changes.

### 174. React Native: Movie Browser
**Build:** Browse movies from TMDB API. Search, categories, movie details, watchlist, ratings.
**Learn:** API pagination, image caching, navigation patterns, FlatList optimization.
**Exercise:** Add "similar movies" recommendations, trailer playback (YouTube embed), and share functionality.

### 175. React Native: Expense Tracker
**Build:** Track income and expenses. Categories, monthly reports, charts, budget limits. Camera for receipt photos.
**Learn:** Charts on mobile, camera API, date pickers, data export.
**Math:** [MATH] Budget calculations, percentage breakdown by category, trend analysis.
**Exercise:** Add recurring expenses, bill reminders, and export to CSV/PDF.

### 176. React Native: Health Tracker
**Build:** Track steps, water intake, sleep hours, weight. Daily goals. Weekly charts. Streak tracking.
**Learn:** Device sensors, health data, local notifications, charting.
**Exercise:** Add meal logging, calorie tracking, BMI calculator, and health score algorithm.

### 177. React Native: Offline-First Notes
**Build:** Notes app that works fully offline. Sync to backend when online. Conflict resolution for concurrent edits.
**Learn:** Offline-first architecture, sync strategies, WatermelonDB or Realm.
**Exercise:** Add folders, tags, markdown support, and share notes between users.

### 178. React Native: Authentication Flow
**Build:** Complete auth: login, register, forgot password, email verification, biometric login (fingerprint/face).
**Learn:** Secure storage, biometric APIs, token management, deep linking for email verification.
**Exercise:** Add social login (Google, Apple), account settings, and session management.

### 179. React Native: Map Integration
**Build:** Map with user location, markers, directions, geofencing, location search.
**Learn:** React Native Maps, geocoding, directions API, background location.
**Exercise:** Build a "nearby places" feature: show restaurants, hospitals, ATMs near user with reviews.

### 180. React Native: Camera & Image
**Build:** Camera app with photo capture, filters, crop, image gallery picker, upload to server.
**Learn:** Camera API, image manipulation, file upload from mobile, permissions handling.
**Exercise:** Add QR code scanner, document scanner (perspective correction), and OCR (text from image).

### 181. React Native: Push Notifications
**Build:** App with push notifications: schedule local notifications, receive remote push, notification actions, badge count.
**Learn:** Expo Notifications, Firebase Cloud Messaging, notification channels.
**Exercise:** Build a reminder app with recurring notifications, snooze, and notification categories.

### 182. React Native: Multi-Language App
**Build:** App supporting English, French, Kinyarwanda, Swahili. Language switcher. RTL support consideration.
**Learn:** i18n libraries (react-i18next), locale detection, language-specific formatting.
**Exercise:** Add dynamic language loading (fetch translations from server), and pluralization rules per language.

### 183. React Native: Food Delivery PoC
**Build:** Restaurant listing, menu, cart, order placement, order tracking with map, delivery status.
**Learn:** Complex navigation flows, real-time updates, map tracking.
**Exercise:** Add restaurant search with filters, driver assignment simulation, and estimated delivery time calculation.

### 184. React Native: E-Commerce App
**Build:** Product catalog, search, categories, cart, wishlist, checkout, order history. Full shopping experience.
**Learn:** Complex state management on mobile, payment integration, deep linking.
**Exercise:** Add product reviews, size/color variants, address management, and push notifications for order status.

### 185. React Native: Social Feed
**Build:** Social media feed with posts, likes, comments, user profiles, follow/unfollow, image posts.
**Learn:** Infinite scroll, optimistic updates, image upload, real-time updates.
**Exercise:** Add stories (disappearing posts), post sharing, hashtag search, and trending feed.

---

# PHASE 8: GAME DEVELOPMENT (Projects 186-210)
*Build interactive worlds. Master game systems.*

### 186. 2D Platformer (Unity)
**Build:** Side-scrolling platformer. Player movement, jump, double jump, platforms, coins, enemies, level completion.
**Learn:** Unity basics, Rigidbody2D, Collider2D, Input System, Tilemaps.
**Exercise:** Add wall jump, dash mechanic, and a boss fight with attack patterns.

### 187. Puzzle Game
**Build:** Sokoban (push boxes to targets) or Match-3 (Bejeweled-style). Level editor. Score tracking.
**Learn:** Grid-based game logic, level design, win condition checking, undo system.
**Exercise:** Add 20 hand-designed levels, difficulty progression, and a star rating system (moves vs par).

### 188. Top-Down RPG Movement
**Build:** Character moves in 4/8 directions. Animated sprite. Collision with walls. Camera follows player. NPC placement.
**Learn:** Sprite animation, tilemap collision, camera systems, layer sorting.
**Exercise:** Add different terrain types (grass slows you, ice makes you slide), footstep sounds, and day/night lighting.

### 189. Dialogue System
**Build:** Branching dialogue tree. NPC interaction. Multiple choice responses. Dialogue affects game state (relationship, quest flags).
**Learn:** Tree data structures in games, scriptable objects, UI text display with typewriter effect.
**Exercise:** Add character portraits, voice line triggers, conditional dialogue (changes based on previous choices).

### 190. Inventory & Equipment System
**Build:** Grid-based inventory. Items with stats. Equip/unequip. Item tooltips. Stack-able items. Weight limit.
**Learn:** Data-driven design, ScriptableObjects, drag-and-drop UI, stat calculation.
**Exercise:** Add crafting (combine items), item rarity tiers (common to legendary), and loot tables with weighted random.

### 191. Procedural Dungeon Generator
**Build:** Random dungeon layout: rooms, corridors, doors, spawn points. BSP tree or random walk algorithm.
**Learn:** Procedural generation algorithms, BSP trees, graph connectivity, level validation.
**Math:** [MATH] BSP tree: How does recursive subdivision create room layouts? Minimum spanning tree for corridors.
**Exercise:** Add themed rooms (treasure, boss, shop), difficulty scaling by depth, and mini-map generation.

### 192. Turn-Based Battle System
**Build:** RPG combat: player party vs enemies. Attack, defend, magic, items. Turn order based on speed. Health/mana bars.
**Learn:** Game state machine, action queue, damage formulas, UI for battle.
**Math:** [MATH] Damage formula design: How do you balance attack vs defense? Diminishing returns.
**Exercise:** Add status effects (poison, stun, buff), elemental weaknesses, and XP/leveling system.

### 193. First-Person Controller
**Build:** FPS-style movement and camera. Walk, sprint, jump, crouch, look around. Smooth mouse look.
**Learn:** CharacterController, mouse input, camera rotation, movement physics.
**Exercise:** Add head bob, footstep sounds, stamina system, and interaction (pick up objects, open doors).

### 194. Third-Person Camera System
**Build:** Camera follows player from behind. Handles wall collision (camera doesn't clip through walls). Zoom in/out. Lock-on targeting.
**Learn:** Camera rigs, raycasting for collision, smooth follow with damping.
**Exercise:** Add camera modes: exploration (wide), combat (over-shoulder), cinematic (scripted path).

### 195. Particle Effects Editor
**Build:** Visual tool to create particle effects: fire, smoke, sparks, rain, snow, magic spells. Adjustable parameters.
**Learn:** Particle systems, emission shapes, lifetime, color over time, force modules.
**Exercise:** Create 10 polished effects: explosion, healing aura, lightning, waterfall, dust cloud, etc.

### 196. Audio Manager
**Build:** Sound system: background music, SFX, 3D spatial audio, volume control, fade in/out, music transitions.
**Learn:** AudioSource, AudioMixer, spatial blend, audio pools for SFX.
**Exercise:** Add dynamic music: combat music fades in when enemies are near, exploration music returns when safe.

### 197. UI System (Menus & Settings)
**Build:** Main menu, pause menu, settings (audio, video, controls, language), loading screen, HUD.
**Learn:** UI Canvas, event system, resolution handling, save/load settings.
**Exercise:** Add key rebinding, accessibility options (colorblind mode, subtitles, text size), and tutorial tooltips.

### 198. Save/Load System
**Build:** Save game state to file (JSON or binary). Load and resume. Multiple save slots. Auto-save.
**Learn:** Serialization, file I/O in Unity, save data architecture, version compatibility.
**Exercise:** Add save file integrity check (detect corruption), cloud save sync, and screenshot preview for each save.

### 199. Environmental Storytelling Scene
**Build:** A detailed 3D scene that tells a story without dialogue. Props, lighting, notes, clues scattered around.
**Learn:** Level design, lighting for mood, prop placement, environmental narrative.
**Exercise:** Create 3 scenes that tell a connected story. Player pieces together what happened by exploring.

### 200. Quest System
**Build:** Quest log with active/completed quests. Quest objectives (kill, collect, talk, go to). Quest chains. Rewards.
**Learn:** Quest data structures, objective tracking, event systems, UI for quest log.
**Exercise:** Add side quests, daily quests, quest givers with markers above heads, and quest difficulty rating.

### 201. Physics-Based Platformer
**Build:** Platformer using physics (not kinematic): player slides, bounces, is affected by forces. Physics puzzles.
**Learn:** Rigidbody-based movement, physics materials, force application.
**Exercise:** Add grappling hook (spring joint), catapult mechanic, and wind zones.

### 202. Vehicle Physics
**Build:** Driveable car: acceleration, braking, steering, suspension, drifting. Speedometer HUD.
**Learn:** Wheel colliders, suspension setup, torque curves, drift mechanics.
**Exercise:** Add different vehicle types (truck, motorcycle, go-kart), terrain effects, and a time trial mode.

### 203. Destruction Physics
**Build:** Breakable objects: walls, crates, glass. Pre-fractured meshes that break on impact. Debris with physics.
**Learn:** Mesh fracturing, force thresholds, debris pooling, performance management.
**Exercise:** Build a demolition game: destroy a building with limited explosives. Score based on destruction percentage.

### 204. Procedural Terrain (In-Engine)
**Build:** Runtime terrain generation using noise. LOD (Level of Detail). Texture blending based on slope/height.
**Learn:** Mesh generation, noise in shaders, terrain LOD, texture splatting.
**Exercise:** Add vegetation placement, water plane, and infinite terrain streaming.

### 205. AI Pathfinding (NavMesh)
**Build:** NPCs navigate using Unity's NavMesh. Avoid obstacles. Follow waypoints. Chase player.
**Learn:** NavMesh baking, NavMeshAgent, obstacle avoidance, path smoothing.
**Exercise:** Add dynamic obstacles (moving platforms), flying enemies (3D pathfinding), and formation movement.

### 206. Behavior Trees for NPCs
**Build:** NPC AI using behavior trees: patrol, detect player, chase, attack, flee when low health, return to patrol.
**Learn:** Behavior tree nodes (sequence, selector, decorator), blackboard pattern.
**Exercise:** Add cooperative AI: NPCs communicate, flank player, call for reinforcements.

### 207. Crafting System
**Build:** Combine materials to create items. Recipe discovery. Crafting stations. Material gathering.
**Learn:** Recipe data structures, inventory integration, UI for crafting.
**Exercise:** Add recipe experimentation (combine unknown items to discover recipes), quality levels, and tool requirements.

### 208. Day/Night Cycle & Weather
**Build:** Dynamic time of day with lighting changes. Weather system: rain, snow, fog, wind. Weather affects gameplay.
**Learn:** Directional light rotation, skybox blending, particle weather, post-processing.
**Exercise:** Add seasons that change over game time. Crops grow in spring, freeze in winter. NPCs go indoors when it rains.

### 209. Open World Streaming
**Build:** Large world divided into chunks. Load/unload chunks as player moves. LOD for distant objects.
**Learn:** World chunking, async loading, object pooling, LOD groups.
**Exercise:** Create a 2km x 2km world with varied biomes. Maintain 60fps with streaming. Add fast travel.

### 210. Multiplayer Basics
**Build:** Simple multiplayer game: two players in a room, synchronized movement, basic interaction.
**Learn:** Netcode basics, client-server model, state synchronization, latency.
**Exercise:** Add a simple multiplayer minigame (race, arena combat) with lobby and matchmaking.

---

# PHASE 9: AI & MACHINE LEARNING (Projects 211-240)
*Teach machines to think. Build intelligent systems.*

### 211. Linear Regression (sklearn)
**Build:** Predict house prices, salary, or crop yield using scikit-learn. Feature selection, training, evaluation.
**Learn:** Supervised learning workflow, train/test split, model evaluation metrics (MSE, R²).
**Math:** [MATH] Compare with your from-scratch implementation (Project 57). Verify they give the same results.
**Exercise:** Try polynomial regression on the same data. When does adding more features help vs hurt (overfitting)?

### 212. Logistic Regression
**Build:** Binary classifier: spam detection, disease diagnosis, or customer churn prediction. Confusion matrix, ROC curve.
**Learn:** Classification vs regression, sigmoid function, decision boundary, threshold tuning.
**Math:** [MATH] Derive sigmoid function. Why does log-odds give a linear decision boundary?
**Exercise:** Multi-class classification using one-vs-rest. Compare with softmax approach.

### 213. K-Means Clustering
**Build:** Cluster data points automatically. Visualize clusters with colors. Elbow method for choosing K. Apply to real data.
**Learn:** Unsupervised learning, centroid initialization, convergence, cluster quality.
**Math:** [MATH] Why does K-means converge? Prove the objective function decreases each iteration.
**Exercise:** Cluster African countries by economic indicators. Interpret the clusters. What story do they tell?

### 214. Decision Tree & Random Forest
**Build:** Decision tree classifier with visualization. Then ensemble into Random Forest. Feature importance ranking.
**Learn:** Information gain, entropy, Gini impurity, ensemble methods, bagging.
**Math:** [MATH] Derive information gain formula. Why do random forests reduce overfitting?
**Exercise:** Predict student dropout risk using educational data. Which features matter most?

### 215. Support Vector Machine
**Build:** SVM classifier with linear and RBF kernels. Visualize decision boundaries. Support vector identification.
**Learn:** Margin maximization, kernel trick, soft margin, hyperparameter tuning (C, gamma).
**Math:** [MATH] What is the "kernel trick" actually doing? Why does mapping to higher dimensions help separability?
**Exercise:** Compare SVM vs Random Forest vs Logistic Regression on 3 datasets. When does each win?

### 216. Dimensionality Reduction (PCA)
**Build:** Reduce high-dimensional data to 2D/3D for visualization. Explained variance. Scree plot. Reconstruction error.
**Learn:** Eigendecomposition, variance explained, dimensionality curse, feature extraction.
**Math:** [MATH] PCA uses eigenvalues of the covariance matrix. Why do the top eigenvectors capture the most variance?
**Exercise:** Apply PCA to face images (Eigenfaces). Reconstruct faces using different numbers of components.

### 217. Time Series Forecasting
**Build:** Forecast stock prices, weather, or sales using ARIMA. Trend detection, seasonality decomposition, prediction intervals.
**Learn:** Stationarity, autocorrelation, differencing, ARIMA parameters (p,d,q).
**Math:** [MATH] What is stationarity? Why must time series be stationary for ARIMA? Augmented Dickey-Fuller test.
**Exercise:** Forecast electricity demand for a week. Compare ARIMA vs simple moving average vs exponential smoothing.

### 218. Anomaly Detection
**Build:** Detect outliers in data: fraud detection, sensor malfunction, network intrusion. Isolation Forest + statistical methods.
**Learn:** Isolation Forest, z-score method, Local Outlier Factor, evaluation without labels.
**Exercise:** Build a credit card fraud detector using real anonymized data (Kaggle). Calculate precision/recall.

### 219. Text Classification
**Build:** Classify text into categories: news topic, sentiment, spam. TF-IDF features + Naive Bayes or SVM.
**Learn:** Text preprocessing, bag of words, TF-IDF, Naive Bayes, text feature engineering.
**Math:** [MATH] Bayes' theorem in Naive Bayes: How does P(spam|words) get calculated? Why "naive"?
**Exercise:** Build a Kinyarwanda/French language detector. Train on multilingual text.

### 220. Recommender System
**Build:** "Users who liked X also liked Y." Collaborative filtering (user-based and item-based). Matrix factorization.
**Learn:** Similarity metrics (cosine, Pearson), cold start problem, evaluation (RMSE, precision@K).
**Math:** [MATH] Cosine similarity: Why does it work for comparing user preferences? SVD for matrix factorization.
**Exercise:** Build a movie recommender. Evaluate on MovieLens dataset. Compare collaborative vs content-based.

### 221. NLP Pipeline
**Build:** Complete NLP pipeline: tokenization, stemming, lemmatization, POS tagging, named entity recognition, dependency parsing.
**Learn:** spaCy or NLTK, linguistic preprocessing, pipeline architecture.
**Exercise:** Analyze a collection of African news articles. Extract key entities, topics, and sentiment trends.

### 222. Sentiment Analysis
**Build:** Analyze sentiment of product reviews, tweets, or news. Positive/negative/neutral classification. Aspect-based sentiment.
**Learn:** Sentiment lexicons, feature engineering for text, evaluation metrics.
**Exercise:** Analyze sentiment about Rwanda tourism from TripAdvisor reviews. What do tourists love vs complain about?

### 223. Audio Feature Extraction
**Build:** Extract features from audio: spectrograms, MFCCs, chromagrams. Classify music genres or detect speech.
**Learn:** Digital signal processing, FFT for audio, mel scale, audio preprocessing.
**Math:** [MATH] Mel scale: Why is human hearing logarithmic? How do MFCCs capture this?
**Exercise:** Build a "is someone speaking?" detector for audio files. Could be used for meeting transcription triggers.

### 224. Image Classification (CNN)
**Build:** Classify images using a CNN built from scratch in PyTorch. Train on CIFAR-10 or custom dataset.
**Learn:** Convolution layers, pooling, flattening, training loops, GPU acceleration.
**Math:** [MATH] What does a convolution filter detect? Why do deeper layers detect more complex features?
**Exercise:** Fine-tune a pre-trained model (ResNet) on a custom dataset of African wildlife images.

### 225. Object Detection
**Build:** Detect and locate objects in images. Bounding boxes. Use YOLO or Faster R-CNN (transfer learning).
**Learn:** Anchor boxes, IoU, non-max suppression, mAP evaluation.
**Exercise:** Build a crop disease detector from leaf images. Train on PlantVillage dataset.

### 226. Generative Model (GAN)
**Build:** Generate new images using a GAN. Start with simple (MNIST digits), then faces or patterns.
**Learn:** Generator vs discriminator, adversarial training, mode collapse, training instability.
**Math:** [MATH] GAN loss function: Why is it a minimax game? What does Nash equilibrium mean here?
**Exercise:** Generate African textile patterns using a GAN trained on fabric images.

### 227. Pathfinding AI (A*)
**Build:** A* pathfinding on a grid. Visualize exploration. Compare with Dijkstra and BFS. Different heuristics.
**Learn:** Heuristic search, admissibility, Manhattan vs Euclidean distance, weighted A*.
**Math:** [MATH] Prove A* finds optimal path when heuristic is admissible (never overestimates).
**Exercise:** Implement Jump Point Search (faster A* for uniform grids). Benchmark against standard A*.

### 228. Genetic Algorithm
**Build:** Optimize a function using genetic algorithm. Population, selection, crossover, mutation. Visualize evolution over generations.
**Learn:** Evolutionary computation, fitness landscapes, parameter tuning.
**Math:** [MATH] Schema theorem: Why do good building blocks propagate? Selection pressure vs diversity.
**Exercise:** Use GA to evolve a neural network topology (basic neuroevolution).

### 229. Q-Learning
**Build:** Agent learns to navigate a gridworld. Reward for reaching goal, penalty for walls. Q-table visualization.
**Learn:** Reinforcement learning basics, exploration vs exploitation, epsilon-greedy, discount factor.
**Math:** [MATH] Bellman equation: Q(s,a) = R + γ * max(Q(s',a')). Why does this converge?
**Exercise:** Train agent to play a simple game (Frozen Lake or custom maze). Show learning curve over episodes.

### 230. Neural Network from Scratch
**Build:** Multi-layer perceptron from scratch. Forward pass, backpropagation, gradient descent. Train on XOR and MNIST.
**Learn:** Neurons, activation functions, chain rule, weight updates, loss functions.
**Math:** [MATH] Derive backpropagation using chain rule. Why does sigmoid cause vanishing gradients? How does ReLU fix it?
**Exercise:** Add momentum, learning rate scheduling, and mini-batch gradient descent. Compare convergence speeds.

### 231. Convolutional Neural Network (PyTorch)
**Build:** CNN for image classification. Conv layers, pooling, batch norm, dropout. Train on CIFAR-10.
**Learn:** PyTorch training loop, GPU training, data augmentation, learning rate scheduling.
**Exercise:** Implement ResNet skip connections. Show how they enable training deeper networks.

### 232. Recurrent Neural Network (LSTM)
**Build:** LSTM for sequence prediction: text generation, stock prediction, or music generation.
**Learn:** Sequential data, hidden state, gates (forget, input, output), BPTT.
**Math:** [MATH] Why do vanilla RNNs have vanishing gradient? How do LSTM gates solve this?
**Exercise:** Generate text in the style of an author. Train on a book and generate new passages.

### 233. Transformer Architecture
**Build:** Implement a small transformer from scratch. Self-attention, multi-head attention, positional encoding.
**Learn:** Attention mechanism, query-key-value, parallelization advantage over RNNs.
**Math:** [MATH] Attention: softmax(QK^T/√d)V. Why divide by √d? What does each matrix represent?
**Exercise:** Train a small transformer on a translation task (English → French for simple sentences).

### 234. Fine-Tuned LLM
**Build:** Fine-tune a language model (or use Claude API) for a specific task: customer support, code review, or tutoring.
**Learn:** Prompt engineering, few-shot learning, fine-tuning strategies, evaluation.
**Exercise:** Build a Kinyarwanda language tutor using Claude API. It teaches basic phrases and corrects pronunciation descriptions.

### 235. Vision Transformer (ViT)
**Build:** Implement Vision Transformer: split image into patches, linear embedding, transformer encoder, classification head.
**Learn:** Patch embedding, position encoding for images, attention maps visualization.
**Math:** [MATH] Why does treating image patches as tokens work? What do attention maps show about what the model "looks at"?
**Exercise:** Compare ViT vs CNN on the same dataset. When does each architecture perform better?

### 236. Diffusion Model
**Build:** Implement a simple diffusion model for image generation. Forward noising, reverse denoising, U-Net architecture.
**Learn:** Score matching, noise scheduling, denoising process, sampling.
**Math:** [MATH] Forward process: q(x_t|x_{t-1}) = N(√(1-β)x_{t-1}, βI). Why does adding noise gradually work better than all at once?
**Exercise:** Generate handwritten digits (MNIST) using your diffusion model. Show the denoising process step by step.

### 237. Reinforcement Learning (PPO)
**Build:** Train an agent using PPO to play a game (CartPole, LunarLander, or custom environment).
**Learn:** Policy gradient, advantage estimation, clipping, actor-critic architecture.
**Math:** [MATH] PPO objective function: Why does clipping prevent destructively large policy updates?
**Exercise:** Train an agent to balance a double pendulum (connecting to your physics simulations!).

### 238. Multi-Modal Model
**Build:** Model that processes both images and text. Image captioning or visual question answering.
**Learn:** Multi-modal fusion, cross-attention, image-text alignment.
**Exercise:** Build a "describe this African landmark" model that takes an image and outputs a description.

### 239. Graph Neural Network
**Build:** GNN for node classification or graph classification. Apply to social network or molecular data.
**Learn:** Message passing, graph convolution, node embedding, graph pooling.
**Math:** [MATH] How does message passing aggregate neighbor information? Why do GNNs capture graph structure?
**Exercise:** Predict molecular properties (toxicity, solubility) from molecular graphs.

### 240. Production ML Pipeline
**Build:** Complete ML pipeline: data ingestion, preprocessing, feature engineering, training, validation, deployment, monitoring, retraining.
**Learn:** MLOps, model versioning, A/B testing, data drift detection, model serving.
**Exercise:** Deploy a model as an API. Monitor prediction quality. Trigger retraining when accuracy drops.

---

# PHASE 10: SCIENTIFIC COMPUTING (Projects 241-255)
*Solve hard numerical problems. Push computational boundaries.*

### 241. Finite Element Method (FEM)
**Build:** Solve a simple structural problem: beam bending, heat distribution on irregular domain. Mesh, basis functions, assembly.
**Learn:** Weak formulation, element matrices, assembly, boundary conditions.
**Math:** [MATH] Galerkin method: Why does multiplying by test functions and integrating work? Derive element stiffness matrix.
**Exercise:** Analyze stress in a bridge truss. Find which members are under most stress.

### 242. Computational Fluid Dynamics (CFD)
**Build:** 2D CFD solver: flow around a cylinder. Pressure field, velocity field, vortex shedding. Visualize streamlines.
**Learn:** Navier-Stokes discretization, SIMPLE algorithm, boundary conditions.
**Math:** [MATH] Reynolds number: Re = ρvL/μ. What determines laminar vs turbulent flow?
**Exercise:** Simulate airflow over an airfoil. Calculate lift and drag coefficients.

### 243. Fast Fourier Transform (FFT)
**Build:** Implement FFT from scratch. Compare with DFT (Project 58). Apply to signal analysis, image processing, polynomial multiplication.
**Learn:** Divide and conquer, butterfly diagram, bit-reversal, Cooley-Tukey algorithm.
**Math:** [MATH] Why is FFT O(n log n) while DFT is O(n²)? Derive the recursive structure.
**Exercise:** Use FFT for fast polynomial multiplication. Multiply two polynomials of degree 10000 instantly.

### 244. Monte Carlo Simulation
**Build:** Estimate π, compute integrals, simulate random processes. Variance reduction techniques.
**Learn:** Random sampling, law of large numbers, importance sampling, variance reduction.
**Math:** [MATH] Estimate π: Why does throwing darts at a square/circle work? Derive the relationship.
**Exercise:** Price a financial option using Monte Carlo. Compare with Black-Scholes analytical solution.

### 245. Stochastic Differential Equations
**Build:** Simulate Brownian motion, geometric Brownian motion (stock prices), Ornstein-Uhlenbeck process.
**Learn:** Wiener process, Itô's lemma, Euler-Maruyama method.
**Math:** [MATH] Why are stock prices modeled as geometric Brownian motion? What assumptions does this make?
**Exercise:** Simulate 1000 stock price paths. Compute the distribution of final prices. Compare with real stock data.

### 246. Graph Theory Algorithms
**Build:** Implement: max flow (Ford-Fulkerson), bipartite matching, graph coloring, Euler/Hamiltonian paths, network reliability.
**Learn:** Network flow, matching theory, NP-hard problems, approximation.
**Math:** [MATH] Max-flow min-cut theorem: Prove it. Why is it fundamental? Real-world applications.
**Exercise:** Model a real network (road network, communication network) and find maximum flow or minimum cut.

### 247. Optimization Algorithms Advanced
**Build:** Implement: simplex method (linear programming), branch and bound, simulated annealing, convex optimization.
**Learn:** Linear programming, integer programming, metaheuristics, convexity.
**Math:** [MATH] Simplex: Why does it move along vertices of the feasible region? Duality theorem.
**Exercise:** Optimize a real problem: school bus routing, nurse scheduling, or resource allocation for a development project.

### 248. Symbolic Math (SymPy)
**Build:** Symbolic algebra system: differentiate, integrate, simplify expressions, solve equations symbolically. LaTeX output.
**Learn:** SymPy library, symbolic vs numerical computation, computer algebra.
**Math:** [MATH] When is symbolic better than numerical? When is numerical better? Limitations of each.
**Exercise:** Symbolically derive the equations of motion for a double pendulum using Lagrangian mechanics.

### 249. Differential Geometry Visualization
**Build:** Visualize: curvature of curves, Gaussian curvature of surfaces, geodesics on sphere/torus, parallel transport.
**Learn:** Curvature, manifolds, geodesics, intrinsic vs extrinsic geometry.
**Math:** [MATH] Gauss's Theorema Egregium: Curvature is intrinsic. Why can't you flatten a sphere without distortion?
**Exercise:** Compute geodesics on Earth's surface. Verify that great circles are shortest paths between cities.

### 250. Quantum Mechanics Simulator
**Build:** Solve 1D Schrödinger equation. Particle in a box, harmonic oscillator, tunneling through a barrier. Visualize wavefunctions.
**Learn:** Wavefunctions, probability densities, energy quantization, tunneling.
**Math:** [MATH] Why are energy levels quantized? What does |ψ|² represent? Why does tunneling defy classical intuition?
**Exercise:** Simulate quantum tunneling: particle approaching a barrier. Show probability of transmission vs barrier width/height.

### 251. Chaos & Bifurcation Analysis
**Build:** Lorenz attractor, logistic map bifurcation diagram, Lyapunov exponents. Sensitivity to initial conditions.
**Learn:** Deterministic chaos, strange attractors, period doubling, sensitivity analysis.
**Math:** [MATH] Lyapunov exponent: How do you measure chaos? Positive = chaotic, negative = stable. Calculate for logistic map.
**Exercise:** Find the onset of chaos in the logistic map (r ≈ 3.57). Show the fractal structure of the bifurcation diagram.

### 252. Multigrid Solver
**Build:** Solve Poisson's equation using multigrid method. V-cycle, restriction, prolongation. Compare convergence with Jacobi/Gauss-Seidel.
**Learn:** Hierarchical solving, smoothing, coarse-grid correction.
**Math:** [MATH] Why does multigrid converge faster? High-frequency errors smoothed on fine grid, low-frequency on coarse.
**Exercise:** Solve a 1000x1000 Poisson problem. Compare multigrid vs direct solver performance.

### 253. Adaptive Mesh Refinement
**Build:** Solve a PDE with AMR: refine mesh where solution changes rapidly. Coarsen where it's smooth.
**Learn:** Error estimation, mesh refinement criteria, quad-tree data structure.
**Exercise:** Solve heat equation with a moving heat source. Show mesh adapting to follow the source.

### 254. Particle-in-Cell (PIC) Simulation
**Build:** Simulate plasma: charged particles in electromagnetic fields. Particle push, field solve, charge deposition.
**Learn:** Plasma physics, Maxwell's equations (simplified), particle-grid coupling.
**Math:** [MATH] Debye length: At what scale do plasmas behave collectively vs individually?
**Exercise:** Simulate two-stream instability. Show beams of particles destabilizing and forming vortices in phase space.

### 255. Spectral Methods
**Build:** Solve PDEs using spectral methods (Fourier or Chebyshev basis). Compare accuracy with finite differences.
**Learn:** Spectral accuracy (exponential convergence), basis functions, aliasing.
**Math:** [MATH] Why do spectral methods converge exponentially for smooth solutions? What happens with discontinuities?
**Exercise:** Solve Burgers' equation (nonlinear). Show shock formation and compare spectral vs finite difference handling.

---

# PHASE 11: SYSTEMS & INFRASTRUCTURE (Projects 256-265)
*Deploy, scale, and maintain production systems.*

### 256. Docker: Containerize App
**Build:** Dockerize one of your web apps. Dockerfile, .dockerignore, multi-stage builds, environment variables.
**Learn:** Containers, images, layers, Docker commands, container networking.
**Exercise:** Create a docker-compose setup with app + database + Redis. One command to start everything.

### 257. Docker Compose: Multi-Container
**Build:** Multi-service application: web app + API + database + cache + message queue. All orchestrated with docker-compose.
**Learn:** Service dependencies, volumes, networks, health checks.
**Exercise:** Add a monitoring service (Grafana) and a log aggregator to your compose stack.

### 258. CI/CD Pipeline
**Build:** GitHub Actions pipeline: lint, test, build, deploy. Run on every push. Deploy to staging on PR, production on merge.
**Learn:** CI/CD concepts, GitHub Actions syntax, secrets management, deployment strategies.
**Exercise:** Add code coverage reporting, security scanning, and Slack notifications for build status.

### 259. Nginx: Reverse Proxy
**Build:** Nginx configuration: reverse proxy to your app, SSL termination, load balancing, rate limiting, static file serving.
**Learn:** Web server configuration, TLS/SSL, proxy headers, upstream servers.
**Exercise:** Set up blue-green deployment: two app instances behind Nginx, switch traffic between them with zero downtime.

### 260. Kubernetes Basics
**Build:** Deploy your app to Kubernetes (Minikube or kind). Pods, Services, Deployments, ConfigMaps, Secrets.
**Learn:** Container orchestration, desired state, self-healing, scaling.
**Exercise:** Set up horizontal pod autoscaling. Load test your app and watch Kubernetes scale pods up/down.

### 261. Monitoring & Alerting
**Build:** Set up Prometheus + Grafana. Monitor: request rate, error rate, latency, CPU, memory. Dashboard + alerts.
**Learn:** Metrics collection, dashboards, alerting rules, SLOs/SLIs.
**Exercise:** Create an on-call runbook: for each alert, document what it means and how to investigate/fix.

### 262. Redis Advanced
**Build:** Use Redis for: caching, session storage, rate limiting, leaderboards, pub/sub messaging.
**Learn:** Redis data structures, TTL, eviction policies, pub/sub pattern.
**Exercise:** Build a real-time leaderboard for a game. 1 million players, top 100 query in <1ms.

### 263. Message Queue
**Build:** Implement a producer-consumer system with RabbitMQ or Redis Streams. Handle: task distribution, dead letter queues, retry logic.
**Learn:** Message brokers, at-least-once delivery, idempotency, backpressure.
**Exercise:** Build an image processing pipeline: upload → resize → thumbnail → store. Each step is a separate consumer.

### 264. Security Audit
**Build:** Audit one of your web apps: SQL injection, XSS, CSRF, authentication flaws. Fix all vulnerabilities found.
**Learn:** OWASP Top 10, security testing tools, secure coding practices.
**Exercise:** Set up automated security scanning in your CI/CD pipeline. No deployment if vulnerabilities found.

### 265. Disaster Recovery
**Build:** Document and test a complete disaster recovery plan: backup verification, failover procedure, data recovery, communication plan.
**Learn:** RTO/RPO, backup strategies, failover, incident response.
**Exercise:** Simulate a disaster (delete the database). Time yourself recovering. Target: under 30 minutes.

---

# PHASE 12: SPACE & EARTH SCIENCE (Projects 266-280)
*Simulate the universe. Predict Earth's future. Use real data.*

### 266. Orbital Mechanics + AI Trajectory Planner
**Build:** Simulate spacecraft trajectories. Add AI to find optimal routes (minimum fuel). Hohmann transfers, gravity assists.
**Learn:** Orbital mechanics, optimization, trajectory planning, delta-v budgets.
**Math:** [MATH] Tsiolkovsky rocket equation: Δv = ve * ln(m0/mf). Why is fuel efficiency exponentially expensive?
**Exercise:** Plan a mission to Mars: Earth departure, transfer orbit, Mars capture. Calculate fuel requirements.

### 267. Satellite Collision Prediction
**Build:** Simulate hundreds of satellites in orbit. Detect close approaches. Predict collision probability. Visualize orbital planes.
**Learn:** TLE data parsing, orbital propagation, conjunction analysis, probability assessment.
**Math:** [MATH] Collision probability: Given position uncertainties (Gaussian), what's the probability of overlap?
**Exercise:** Use real satellite data (CelesTrak). Find the top 10 most dangerous close approaches this week.

### 268. AI Space Weather Prediction
**Build:** Predict solar wind conditions, geomagnetic storms, aurora probability using ML on real NASA data.
**Learn:** Space weather data (DSCOVR, ACE), time series prediction, solar cycle patterns.
**Math:** [MATH] Kp index, Dst index: What do these measure? How do solar wind parameters predict geomagnetic activity?
**Exercise:** Build an aurora alert system: predict when aurora will be visible at a given latitude.

### 269. Multi-Agent Disaster Simulator
**Build:** Simulate disaster scenarios: earthquake, flood, wildfire. Agents represent: people, emergency services, infrastructure. Model response effectiveness.
**Learn:** Multi-agent systems, spatial simulation, resource allocation, emergency management.
**Exercise:** Simulate a flood in a Kigali neighborhood. Optimize evacuation routes and emergency resource placement.

### 270. Earth Evolution Simulator
**Build:** Long-term simulation of Earth: plate tectonics (simplified), climate change, sea level rise, vegetation shifts over millions of years.
**Learn:** Geological time scales, climate models (simplified), feedback loops.
**Math:** [MATH] Carbon cycle: How do feedback loops (albedo, CO2, temperature) create stability or tipping points?
**Exercise:** Simulate the next 100 years of climate change under different emission scenarios. Visualize sea level rise on a map.

### 271. Climate Impact Simulator (Coastal)
**Build:** Simulate sea-level rise impact on coastal communities. Elevation data, population data, infrastructure mapping.
**Learn:** GIS data processing, elevation models, risk assessment, visualization.
**Exercise:** Apply to a specific African coastal city (e.g., Dar es Salaam, Lagos). Identify neighborhoods at highest risk.

### 272. Drought & Crop Yield Predictor
**Build:** Predict crop yields based on weather patterns, soil data, historical yields. Alert farmers to drought risk.
**Learn:** Agricultural data, weather APIs, regression/classification for prediction.
**Exercise:** Apply to Rwandan agriculture. Predict maize yields by district. Validate against historical data.

### 273. Urban Heat Analyzer
**Build:** Predict urban heat islands using satellite data, building density, green space coverage. Identify at-risk neighborhoods.
**Learn:** Remote sensing data, heat island effect, spatial analysis.
**Exercise:** Analyze Kigali: which neighborhoods are hottest? Recommend where to add green spaces.

### 274. Smart City Traffic Predictor
**Build:** Predict traffic congestion using road network, time of day, events, weather. Suggest optimal routes.
**Learn:** Graph-based routing, temporal patterns, prediction models.
**Math:** [MATH] Braess's paradox: Adding a road can make traffic WORSE. Simulate and demonstrate this.
**Exercise:** Model Kigali's road network. Predict bottlenecks. Suggest 3 infrastructure improvements.

### 275. Infrastructure Failure Warning
**Build:** Predict infrastructure failure risk: bridges, buildings, roads. Based on age, load, weather, maintenance history.
**Learn:** Predictive maintenance, risk scoring, sensor data analysis.
**Exercise:** Create a risk dashboard for a fictional city. Color-code infrastructure by failure risk.

### 276. Student Dropout Predictor
**Build:** Analyze student data (grades, attendance, participation) to predict dropout risk. Early warning system.
**Learn:** Educational data mining, feature engineering, ethical considerations (bias in predictions).
**Exercise:** Address fairness: ensure your model doesn't discriminate by gender, income, or background.

### 277. Education Policy Simulator
**Build:** Simulate outcomes of education investments: teacher training, technology, curriculum changes. Agent-based model.
**Learn:** Policy simulation, agent-based modeling, outcome metrics.
**Exercise:** Simulate Rwanda's education system. What investment gives the best improvement per dollar?

### 278. Disease Progression Simulator
**Build:** Visualize disease progression stages. Interactive tool for medical education. Data-driven timelines.
**Learn:** Medical data visualization, stage modeling, patient pathways.
**Exercise:** Build a tool for diabetes management: predict progression based on lifestyle factors. Show intervention effects.

### 279. Public Service Complaint Analyzer
**Build:** Analyze citizen complaints: categorize, prioritize, route to departments. NLP for text classification.
**Learn:** Text classification at scale, priority scoring, dashboard for officials.
**Exercise:** Build a dashboard showing: complaint categories, resolution times, geographic distribution, trends.

### 280. Election Claims Fact-Triage
**Build:** Analyze political speeches. Categorize claims (economic, social, security). Flag claims needing fact-checking.
**Learn:** NLP for claim extraction, classification, knowledge base lookup.
**Exercise:** Process a real political debate transcript. Generate a structured fact-check priority list.

---

# PHASE 13: AFRICAN IMPACT & RESEARCH (Projects 281-295)
*Build solutions for Africa. Make real impact.*

### 281. Local Job Market Predictor
**Build:** Analyze economic data to predict job market trends by sector and region. Career guidance tool.
**Learn:** Economic data analysis, sector modeling, trend prediction.
**Exercise:** Predict the top 5 growing job sectors in Rwanda for 2028. Validate against current trends.

### 282. Entrepreneur Opportunity Map
**Build:** Identify where new businesses are needed most. Combine population data, existing businesses, income levels, infrastructure.
**Learn:** Market analysis, geographic data, gap analysis, heat mapping.
**Exercise:** Generate an opportunity report for Kigali: top 10 business opportunities by neighborhood.

### 283. Poverty Reduction Simulator
**Build:** Model poverty dynamics: income, education, health, infrastructure interactions. Test intervention strategies.
**Learn:** Systems dynamics, feedback loops, policy modeling.
**Math:** [MATH] Sensitivity analysis: Which intervention parameter has the largest effect on poverty reduction?
**Exercise:** Simulate 3 poverty reduction strategies for a Rwandan district. Compare outcomes over 10 years.

### 284. Urban Growth & Housing Simulator
**Build:** Predict urban expansion patterns. Housing demand, land use, infrastructure pressure. Agent-based growth model.
**Learn:** Urban modeling, land use change, population dynamics.
**Exercise:** Simulate Kigali's growth over the next 20 years. Identify where housing shortages will be worst.

### 285. AI Content Detector
**Build:** Detect AI-generated text, images, and eventually video. Classify content as human vs AI-generated.
**Learn:** Stylometric analysis, perplexity scoring, watermark detection.
**Exercise:** Test your detector against Claude, GPT, and other LLM outputs. Report accuracy.

### 286. Satellite Image Classifier
**Build:** Classify land use from satellite images: urban, forest, water, agriculture, barren. Using CNNs on real satellite data.
**Learn:** Remote sensing, image segmentation, transfer learning for satellite imagery.
**Exercise:** Track deforestation in a region of Congo or Rwanda using time-series satellite images.

### 287. Renewable Energy Monitor
**Build:** Dashboard for solar/wind energy: production forecasting, efficiency tracking, maintenance alerts.
**Learn:** Energy data, weather correlation, IoT sensor integration.
**Math:** [MATH] Solar panel efficiency: How does angle, latitude, and season affect output? Model it.
**Exercise:** Design an optimal solar farm layout for a location in Rwanda. Maximize annual energy production.

### 288. Water Quality Predictor
**Build:** Predict water quality from sensor data (pH, turbidity, temperature, dissolved oxygen). Alert when unsafe.
**Learn:** Sensor data processing, classification for safety thresholds, real-time monitoring.
**Exercise:** Build an alert system for Lake Kivu: predict methane-related water quality changes.

### 289. Agricultural Supply Chain Optimizer
**Build:** Optimize farm-to-market logistics. Minimize transport costs while maximizing freshness. Route optimization.
**Learn:** Supply chain modeling, vehicle routing problem, perishable goods logistics.
**Math:** [MATH] Vehicle Routing Problem: NP-hard. Use heuristics (nearest neighbor, genetic algorithm) to find good solutions.
**Exercise:** Model a coffee supply chain from Rwandan farms to Kigali processing centers. Minimize costs.

### 290. Multilingual Chatbot
**Build:** Chatbot supporting English, French, Kinyarwanda, Swahili. Context-aware responses. Domain-specific knowledge.
**Learn:** Multilingual NLP, translation, context management, intent recognition.
**Exercise:** Deploy the chatbot for a specific use case: tourist information, health advice, or agricultural tips.

### 291. Community Health Dashboard
**Build:** Aggregate health data by region. Track: disease prevalence, vaccination rates, hospital capacity, health outcomes.
**Learn:** Health informatics, data aggregation, geographic visualization, privacy considerations.
**Exercise:** Build a malaria risk map for Rwanda using climate data and historical case reports.

### 292. Financial Inclusion Tool
**Build:** Mobile-first tool for financial literacy: budgeting, savings goals, micro-lending information, mobile money integration concepts.
**Learn:** Fintech basics, mobile money ecosystems, financial modeling for low-income users.
**Math:** [MATH] Compound interest, loan amortization, savings projections at different rates.
**Exercise:** Build a loan calculator that shows true cost of borrowing from different sources (bank vs microfinance vs mobile money).

### 293. Open Data Platform
**Build:** Platform for sharing and visualizing open data about Africa: demographics, economics, health, education, infrastructure.
**Learn:** Data aggregation, API design for open data, visualization at scale.
**Exercise:** Aggregate data from 5 open data sources about Rwanda. Build an interactive dashboard.

### 294. Cross-Border Trade Analyzer
**Build:** Analyze trade flows between African countries. Identify opportunities, barriers, and trends. Visualize trade networks.
**Learn:** Trade data (UN Comtrade), network analysis, economic modeling.
**Math:** [MATH] Gravity model of trade: Trade ∝ GDP₁ × GDP₂ / Distance. Test this on African trade data.
**Exercise:** Predict which trade corridors will grow most under the AfCFTA (African Continental Free Trade Area).

### 295. Language Preservation Tool
**Build:** Record, transcribe, and archive African languages. Speech-to-text for low-resource languages. Community contributions.
**Learn:** Speech recognition, low-resource NLP, community data collection, cultural preservation.
**Exercise:** Build a basic Kinyarwanda speech-to-text model trained on community recordings.

---

# PHASE 14: PERSONAL CAPSTONES (Projects 296-300)
*Your ultimate projects. Everything you've learned, synthesized.*

### 296. AI Me (Personal AI Avatar)
**Build:** AI chatbot with your personality, appearance, and voice. Trained on your data. Video/voice output.
**Requires:** LLM fine-tuning (Project 234), voice synthesis, computer vision (for avatar), personality modeling.
**Scope:** MVP: Text chatbot with your personality. V2: Voice clone. V3: Video avatar.
**Exercise:** Have 10 friends interact with "AI You." Can they tell it's not really you?

### 297. Ashes of Ikarra: Playable Chapter 1
**Build:** 30-60 minute playable RPG chapter with: custom physics, AI NPCs, procedural elements, African-inspired world, memory-based mechanics.
**Requires:** Game dev (Phase 8), physics (Phase 6), AI (Phase 9), narrative design.
**Scope:** One region, 5 quests, 3 NPC types, combat, dialogue, environmental storytelling.
**Exercise:** Playtest with 10 people. Iterate based on feedback. Document what works and what doesn't.

### 298. African Life Game (GTA/Sims PoC)
**Build:** Proof of concept: Character creation (country, gender, economic status), daily life simulation, economic system, social interactions.
**Requires:** Game dev (Phase 8), procedural generation, agent systems, economic modeling.
**Scope:** One city, 5 activities, basic economy, day/night cycle, character progression.
**Exercise:** Simulate 100 AI lives. Analyze outcomes. Does your simulation reflect real African life experiences?

### 299. African Messenger App MVP
**Build:** End-to-end encrypted messaging with African features: mobile money integration concepts, low-bandwidth mode, local language support, data-light media sharing.
**Requires:** Mobile dev (Phase 7), backend (Phase 4), encryption, real-time messaging.
**Scope:** 1-on-1 chat, group chat, media sharing, E2E encryption, offline message queuing.
**Exercise:** Compare with WhatsApp: what does your app do better for African users? Document 5 unique advantages.

### 300. African Social Media Platform MVP
**Build:** Content sharing platform for Africa: posts, images, video, communities, content moderation, multilingual support, celebration of African culture.
**Requires:** Full-stack (Phase 4-5), mobile (Phase 7), AI for moderation (Phase 9), scalability (Phase 11).
**Scope:** User profiles, feed, posting, comments, likes, communities, basic content moderation.
**Exercise:** Launch beta with 50 users. Gather feedback. Iterate on the top 3 requested features.

---

# MATH THREAD SUMMARY

Throughout the curriculum, you'll build mathematical skills in:

| Math Area | Where It Appears | Key Projects |
|-----------|-------------------|--------------|
| Algebra & Arithmetic | Phase 0-1 | 2, 3, 10, 11 |
| Linear Algebra | Phase 2, 6 | 46-49, 131, 216 |
| Calculus | Phase 2, 6 | 50-52, 132-137 |
| Probability & Statistics | Phase 2, 9 | 53-56, 213-218 |
| Differential Equations | Phase 6, 10 | 133-136, 154-155, 245 |
| Discrete Math | Phase 1 | 28-29, 31, 40-44, 65 |
| Optimization | Phase 2, 9, 10 | 52, 64, 228, 247 |
| Number Theory | Phase 2 | 65 |
| Fourier Analysis | Phase 2, 10 | 58, 243 |
| Graph Theory | Phase 1, 10 | 31-33, 44, 246 |
| Geometry | Phase 2, 10 | 60-61, 249 |
| Chaos Theory | Phase 10 | 251 |
| Quantum Mechanics | Phase 10 | 250 |

---

# REFLECTION SCHEDULE

Write a reflection every 10 projects:

- After Project 10: "What surprised me about Python?"
- After Project 20: "What's my biggest weakness so far?"
- After Project 30: "What was the hardest algorithm to understand?"
- After Project 45: "Am I ready for math foundations?"
- After Project 65: "Which math concept clicked the most?"
- After Project 85: "Do I understand the web platform?"
- After Project 110: "Can I build a production API?"
- After Project 130: "Am I a full-stack developer now?"
- After Project 170: "What's my favorite simulation?"
- After Project 185: "Can I build a real mobile app?"
- After Project 210: "What game mechanic am I most proud of?"
- After Project 240: "Do I understand AI/ML deeply?"
- After Project 255: "What's the hardest numerical method?"
- After Project 265: "Can I deploy and maintain a production system?"
- After Project 280: "What scientific discovery excited me most?"
- After Project 295: "How has my vision for Africa's tech future evolved?"
- After Project 300: "Who am I now vs when I started?"

---

# FINAL NOTES

## This Is Your Journey
300 projects over 12-18 months. Some will take 2 hours. Some will take 2 weeks.
The point is not speed. The point is depth.

## The Protocol Matters
Concept → Plan → Build → Understand → Exercise.
Skip none of these. Especially "Understand" and "Exercise."

## Your Mission
You said it: "Participate in new discoveries and develop my continent."
This curriculum is designed to get you there. Every project builds toward that mission.

## Start Now
Project 1: Hello World Extended.
Open a blank file. Write the first line.
Go.

