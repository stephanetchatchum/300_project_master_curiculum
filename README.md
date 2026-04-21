# 300-Project Master Curriculum

> *"Participate in new discoveries, and develop my continent."*

**CLI -> Web -> Physics -> Games -> AI/ML -> African Impact -> Capstones**

---

## The Learning Protocol (Every Project)

| Step | Name | Time |
|------|------|------|
| 1 | Concept | 5 min |
| 2 | Plan | 10-20 min |
| 3 | Build | 60+ min |
| 4 | Understand | 20 min |
| 5 | Rest | 1+ day |
| 6 | Exercise | 30-60 min |
| 7 | Reflect | 10 min |

---

## Phase 1: Foundations (50 projects)

### CLI & Python Core (Math: Logic & Algorithms)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 1 | Hello World CLI | Input/output, print formatting, user interaction | print(), input(), f-strings, type conversion | Build a multilingual greeter (English, French, Kinyarwanda) |
| 2 | Temperature Converter | Functions, type conversion, formula application | def, return, float(), round() | Add Kelvin and Rankine, plus unit auto-detection |
| 3 | Number Guessing Game | Loops, conditionals, random generation | while, if/elif/else, random.randint(), break | AI guesses YOUR number using binary search |
| 4 | Calculator with History | Lists, user input parsing, operation dispatch | lists, append(), split(), eval safety | Add parentheses support and undo functionality |
| 5 | File Word Counter | File I/O, string methods, text analysis | open(), read(), split(), Counter | Count word frequency across multiple files, output CSV |
| 6 | Contact Book (CLI) | Dictionaries, CRUD operations, search | dict, keys(), values(), json.dump() | Add groups, favorites, and export to vCard format |
| 7 | Todo List (CLI) | Lists, file persistence, status management | list operations, JSON persistence, datetime | Add priorities, due dates, and overdue alerts |
| 8 | Password Generator | Random selection, string manipulation, security | random.choice(), string module, secrets | Add passphrase mode and password strength meter |
| 9 | Expense Tracker (CLI) | Data aggregation, categories, monthly reports | dictionaries, sum(), groupby logic | Add budget limits and overspend warnings per category |
| 10 | Quiz Game | Data structures, scoring, question randomization | lists of dicts, random.shuffle(), score tracking | Add timed questions and difficulty scaling |
| 11 | Hangman Game | Game loop, string manipulation, ASCII art | sets, string indexing, game state | Add word categories and hint system |
| 12 | Rock Paper Scissors (with AI) | Conditionals, simple strategy, win tracking | if/else chains, random.choice(), statistics | AI learns your patterns using frequency analysis |
| 13 | Student Grade Manager | Classes, methods, data organization | class, __init__, methods, __str__ | Add GPA calculation and grade distribution chart (text-based) |
| 14 | Library Book System | OOP, inheritance, polymorphism | inheritance, super(), isinstance() | Add different media types (DVD, magazine) with shared interface |
| 15 | Personal Diary (CLI) | File I/O, datetime, search functionality | datetime, os.path, text search | Add mood tracking and monthly mood summary |
| 16 | CSV Data Analyzer | CSV parsing, statistics, data cleaning | csv module, statistics module, data validation | Handle malformed CSV files gracefully with error reporting |
| 17 | Markdown Note-Taking App | File parsing, search/filter, organization | regex basics, os.walk(), file organization | Add tags, cross-references between notes |
| 18 | Password Manager (encrypted) | Security basics, hashing, encrypted storage | hashlib, base64, getpass, file encryption | Add master password with salt + key derivation |
| 19 | Stock Price Fetcher (API) | HTTP requests, JSON parsing, API keys | requests, json, API authentication | Add price alerts and historical comparison |
| 20 | Web Scraper (basic) | HTML parsing, data extraction, automation | BeautifulSoup, requests, CSS selectors | Scrape multiple pages with pagination handling |
| 21 | Unit Converter Suite | Modular design, dictionaries, extensibility | function dispatch, conversion tables, modules | Add custom unit definitions loaded from config file |
| 22 | Flashcard Study App | Spaced repetition logic, learning science | datetime intervals, scoring algorithms, JSON | Implement Leitner box system with stats dashboard |
| 23 | Pomodoro Timer (CLI) | Time management, threading basics, signals | time.sleep(), threading, signal handling | Add session logging and daily productivity report |
| 24 | Personal Budget Tracker | Data aggregation, reports, projections | monthly grouping, averages, trend analysis | Add savings goals and projected timeline to reach them |
| 25 | Bash Script Collection | Shell scripting, automation, system tools | bash syntax, pipes, grep, awk, cron | Create an installer script that sets up your dev environment |

### Math & Logic Foundations (Math: Number Theory, Linear Algebra, Algorithms)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 26 | Prime Number Generator | Number theory, Sieve of Eratosthenes, optimization | modulo, sieve algorithm, time complexity O(n log log n) | Visualize prime spirals (Ulam spiral) |
| 27 | Matrix Calculator | 2D arrays, linear algebra operations | nested lists, dot product, transpose, determinant | Add matrix inverse and solve Ax = b |
| 28 | Fibonacci & Sequences | Recursion, dynamic programming, sequences | recursion, memoization, generators | Implement Lucas numbers and Golden Ratio convergence |
| 29 | Sorting Algorithm Visualizer | Comparison of sort algorithms, complexity | bubble, merge, quick sort, O(n) analysis | Add radix sort and compare all with timing |
| 30 | Binary Search Implementation | Divide and conquer, logarithmic time | binary search, O(log n), edge cases | Search in rotated sorted array |
| 31 | Statistics Calculator | Descriptive statistics from scratch | mean, median, mode, std dev, variance | Add confidence intervals and hypothesis testing |
| 32 | Probability Simulator | Monte Carlo methods, combinatorics | random sampling, law of large numbers | Simulate Monty Hall problem, prove the solution |
| 33 | Graph Data Structure | Nodes, edges, traversal algorithms | adjacency list, BFS, DFS, connected components | Find shortest path in a weighted graph (Dijkstra) |
| 34 | Stack & Queue from Scratch | Abstract data types, LIFO/FIFO | push, pop, enqueue, dequeue, overflow | Implement a priority queue |
| 35 | Linked List from Scratch | Node-based structures, pointer logic | Node class, insert, delete, traverse, reverse | Detect cycle in linked list (Floyd's algorithm) |
| 36 | Binary Tree Implementation | Tree structures, recursive traversal | insert, search, inorder/preorder/postorder | Implement AVL tree with self-balancing |
| 37 | Hash Table from Scratch | Hashing, collision resolution strategies | hash functions, chaining, open addressing | Benchmark your hash table vs Python's built-in dict |
| 38 | Set Operations Visualizer | Set theory, Venn diagrams (text-based) | union, intersection, difference, symmetric diff | Apply to real data (find common words in two books) |
| 39 | Complex Number Calculator | Imaginary numbers, polar form | a+bi, magnitude, phase, multiplication | Visualize complex plane transformations |
| 40 | Polynomial Solver | Roots, factoring, evaluation | Horner's method, quadratic formula, Newton's method | Plot polynomials and highlight roots |
| 41 | Linear Equation Solver | Systems of equations, Gaussian elimination | row reduction, back substitution, pivoting | Solve 4x4 and 5x5 systems, detect no-solution cases |
| 42 | Numerical Differentiation | Limits, rate of change, approximation | forward/backward/central difference, h->0 | Differentiate real functions and compare to analytical |
| 43 | Numerical Integration | Area under curves, approximation methods | Riemann sums, trapezoidal rule, Simpson's rule | Integrate sin(x) from 0 to pi, compare accuracy |
| 44 | Trigonometry Visualizer | Unit circle, sin/cos/tan relationships | radians, unit circle, identities, matplotlib | Animate a point moving around the unit circle |
| 45 | Fractal Generator (Mandelbrot) | Complex iteration, escape time algorithm | z = z^2 + c, iteration count, color mapping | Add Julia set generation and zoom functionality |
| 46 | Chaos Game (Sierpinski) | Randomness producing order, emergence | random points, midpoint rule, attractors | Generalize to n-gon chaos game |
| 47 | Random Walk Simulator | Stochastic processes, diffusion | random steps, displacement, statistics | 2D random walk with boundary absorption |
| 48 | Logic Gate Simulator | Boolean algebra, digital circuits | AND, OR, NOT, XOR, truth tables | Build a half-adder and full-adder from gates |
| 49 | Caesar & Vigenere Cipher | Modular arithmetic, cryptography basics | modulo, character shifting, key-based encryption | Implement frequency analysis to crack Caesar cipher |
| 50 | Combinatorics Calculator | Permutations, combinations, counting | nPr, nCr, factorial, Pascal's triangle | Solve real probability problems (poker hands, lottery) |

---

## Phase 2: Web & Data (40 projects)

### Web Foundations (Math: Logic, State Machines)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 51 | Personal Portfolio Website | HTML/CSS/JS, responsive design, SEO | semantic HTML, CSS Grid/Flexbox, meta tags | Add a blog section with markdown rendering |
| 52 | JavaScript Calculator | DOM manipulation, event handling, state | querySelector, addEventListener, eval alternatives | Add scientific functions (sin, cos, log) |
| 53 | Interactive Quiz App (JS) | State management, scoring, timer | DOM updates, setInterval, object arrays | Add leaderboard with localStorage |
| 54 | Weather Dashboard | API integration, fetch, async/await | fetch(), JSON, async/await, error handling | Add 5-day forecast and location auto-detect |
| 55 | Currency Converter (live API) | REST APIs, real-time data, caching | API keys, exchange rates, localStorage cache | Add historical rate chart |
| 56 | Todo App (JavaScript) | CRUD, localStorage, DOM rendering | createElement, localStorage, event delegation | Add drag-and-drop reordering |
| 57 | Countdown Timer | Time calculations, intervals, DOM updates | setInterval, Date objects, clearInterval | Add multiple named timers running simultaneously |
| 58 | Image Gallery with Lightbox | CSS Grid, modal, keyboard navigation | CSS Grid, position:fixed, keydown events | Add slideshow mode with auto-advance |
| 59 | Form Validation System | Regex, real-time feedback, UX | regex patterns, blur/input events, aria | Validate international phone numbers and emails |
| 60 | Markdown Preview Editor | Real-time parsing, split view, syntax | innerHTML, regex parsing, contenteditable | Add code syntax highlighting |
| 61 | Dark Mode Toggle | CSS variables, theme persistence | CSS custom properties, localStorage, prefers-color-scheme | Add 3+ themes (dark, light, solarized, high-contrast) |
| 62 | Search & Filter UI | Client-side filtering, debounce, UX | filter(), debounce, highlight matching text | Add multi-field search with AND/OR logic |
| 63 | Infinite Scroll Page | Lazy loading, Intersection Observer | IntersectionObserver, pagination, throttle | Add scroll position memory on back navigation |
| 64 | Drag & Drop Interface | HTML5 drag API, list reordering | dragstart, dragover, drop, dataTransfer | Build a Kanban board with drag between columns |
| 65 | Accessible Website (WCAG) | Screen readers, aria labels, keyboard nav | aria-label, role, tabindex, focus management | Audit an existing site and fix all violations |
| 66 | CSS Animation Gallery | Keyframes, transitions, transforms | @keyframes, transition, transform, will-change | Create a loading animation library (5+ spinners) |
| 67 | Mobile-First Responsive Design | Media queries, viewport, touch | min-width queries, rem/em, touch events | Build a responsive email template |
| 68 | Landing Page with Scroll Effects | Parallax, reveal on scroll | IntersectionObserver, transform, opacity | Add smooth scroll navigation with active section highlight |
| 69 | Keyboard Shortcut Handler | Key mapping, command palette | keydown, key combos, command registry | Build a VS Code-style command palette (Ctrl+Shift+P) |
| 70 | Progressive Web App (PWA) | Service workers, manifest, offline | service worker lifecycle, cache API, manifest.json | Add push notifications and background sync |

### Backend & Databases (Math: Set Theory, Relational Algebra)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 71 | Flask Hello World API | Routes, HTTP methods, JSON responses | Flask, @app.route, request, jsonify | Add request logging middleware |
| 72 | Flask Todo API (CRUD) | Full REST API, SQLAlchemy, persistence | SQLAlchemy, CRUD endpoints, status codes | Add pagination and sorting |
| 73 | PostgreSQL Schema Design | Normalization, indexing, constraints | 1NF-3NF, foreign keys, indexes, EXPLAIN | Design a social media schema (users, posts, likes, follows) |
| 74 | User Authentication (JWT) | Password hashing, tokens, sessions | bcrypt, JWT encode/decode, middleware | Add refresh tokens and token revocation |
| 75 | File Upload Service | Multipart forms, storage, validation | multipart/form-data, file validation, storage | Add image resizing and thumbnail generation |
| 76 | Django REST Notes App | DRF, serializers, viewsets | ModelSerializer, ViewSet, Router | Add shared notes with user permissions |
| 77 | Blog API with Comments | One-to-many relationships, nested data | ForeignKey, nested serializers, pagination | Add threaded/nested comments |
| 78 | Inventory Management API | Permissions, soft deletes, audit trail | role-based access, is_deleted flag, timestamps | Add stock alerts and reorder suggestions |
| 79 | Real-Time Chat Backend | WebSockets, rooms, message history | Flask-SocketIO, rooms, events, persistence | Add typing indicators and read receipts |
| 80 | Task Queue System | Async jobs, scheduling, workers | Celery, Redis, periodic tasks, retries | Add email notification worker |

### Full-Stack Integration (Math: State Machines, Graph Theory)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 81 | React Todo App | Components, state, hooks | useState, useEffect, props, lifting state | Add categories and drag-and-drop reordering |
| 82 | React E-Commerce Page | Product listing, filtering, cart state | useReducer, context, filtering logic | Add wishlist and price comparison |
| 83 | React + Flask Blog | Full-stack, auth flow, API integration | axios, CORS, JWT in React, protected routes | Add markdown editor and image upload |
| 84 | React Data Dashboard | Charts, real data, responsive layout | Recharts, data fetching, responsive grid | Add date range picker and CSV export |
| 85 | React Kanban Board | Drag and drop, column state, persistence | react-beautiful-dnd, useReducer, localStorage | Add swimlanes and WIP limits |
| 86 | React Expense Splitter | Multi-user calculations, fairness | forms, computed values, PDF export | Add recurring expenses and settlement suggestions |
| 87 | React Real-Time Chat | WebSocket client, message rendering | socket.io-client, useEffect cleanup, scrolling | Add emoji picker and message reactions |
| 88 | Admin Dashboard (React) | CRUD tables, pagination, bulk actions | table components, pagination logic, modals | Add role-based views and audit log |
| 89 | OAuth 2.0 Login Flow | Google/GitHub auth, session management | OAuth flow, redirect URI, token storage | Add multiple providers and account linking |
| 90 | GraphQL API + Client | Schema design, queries, mutations | typeDefs, resolvers, Apollo Client, useQuery | Add subscriptions for real-time updates |

---

## Phase 3: Scientific Computing (45 projects)

### Physics Foundations (Math: Calculus, Trigonometry, Linear Algebra)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 91 | Vector Math Visualizer | 2D vectors, operations, interactive matplotlib | magnitude, dot product, cross product, angle | Add vector projection and Gram-Schmidt visualization |
| 92 | Projectile Motion Simulator | Kinematics, trajectory, gravity | x(t), y(t), v0*cos/sin, parabolic arc | Add air resistance (drag force proportional to v^2) |
| 93 | Pendulum Simulator | ODE, numerical integration, animation | angular acceleration = -(g/L)sin(angle), Euler method, energy | Double pendulum (chaotic motion) |
| 94 | Particle System (n-body) | Gravitational attraction, force accumulation | F = Gm1m2/r^2, vector forces, O(n^2) | Add Barnes-Hut optimization O(n log n) |
| 95 | Wave Equation Solver (1D) | Finite differences, standing waves | PDE discretization, boundary conditions, Laplacian | 2D wave equation with interactive disturbance |
| 96 | Heat Diffusion Simulation | Thermal conduction, boundary conditions | heat equation, explicit/implicit schemes | Add heat sources and sinks, insulation boundaries |
| 97 | Orbital Mechanics (Kepler) | Elliptical orbits, energy conservation | Runge-Kutta, orbital elements, vis-viva | Hohmann transfer orbit calculator |
| 98 | Collision Detection Suite | AABB, circle, polygon, raycasting | bounding boxes, separating axis theorem | Add spatial partitioning (quadtree) |
| 99 | Fluid Dynamics (Shallow Water) | Grid-based fluid, wave propagation | conservation laws, finite volume method | Add obstacles and dam break scenario |
| 100 | Cellular Automaton | Conway's Game of Life, emergence | grid rules, neighbor counting, generations | Implement Langton's Ant and compare emergence |
| 101 | Spring & Damping System | Hooke's law, energy dissipation | F = -kx - bv, damped oscillation | Coupled springs (two masses connected) |
| 102 | Simple Harmonic Motion | Oscillation, phase, amplitude | x = A*cos(wt + phi), energy exchange | Visualize Lissajous curves (two SHM combined) |
| 103 | Friction Models | Static, kinetic, rolling friction | us, uk, normal force, friction cone | Simulate block on inclined plane with variable angle |
| 104 | Buoyancy & Fluid Resistance | Archimedes' principle, drag forces | displaced volume, drag coefficient, terminal velocity | Simulate a submarine with depth control |
| 105 | Elastic & Inelastic Collisions | Momentum conservation, energy | p = mv, coefficient of restitution | Pool/billiards table simulator |

### Physics Engines (Math: Differential Equations, Numerical Methods)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 106 | 2D Rigid Body Physics Engine | Mass, velocity, forces, integration | Euler/Verlet integration, force accumulation | Add torque and rotational dynamics |
| 107 | Constraint Solver (Verlet) | Position-based dynamics, stability | Verlet integration, distance constraints, iterations | Build a bridge stress simulator |
| 108 | Rope/Chain Simulator | Constraint chains, tension | linked particles, distance constraints | Add breakable joints (snap under tension) |
| 109 | Cloth Simulation | Mass-spring model, wind forces | structural/shear/bend springs, wind vector | Add tearing (remove springs under stress) |
| 110 | Soft Body Physics | Deformable objects, pressure | internal pressure, spring networks | Simulate a bouncing jelly cube |
| 111 | Ragdoll Physics | Joint constraints, articulated bodies | ball/hinge joints, angular limits | Add ragdoll with user-controlled limb forces |
| 112 | Impact & Impulse Resolution | Collision response, restitution | impulse = F*dt, normal/tangent decomposition | Stack of boxes with realistic settling |
| 113 | Vehicle Suspension | Springs, damping, terrain response | spring-damper system, wheel contact | Off-road vehicle on bumpy terrain |
| 114 | Procedural Terrain Generation | Noise functions, erosion | Perlin/Simplex noise, hydraulic erosion | Add biome assignment based on height/moisture |
| 115 | Ocean Waves (Gerstner) | FFT-based waves, realistic water | Gerstner wave equation, FFT, displacement | Add floating objects that bob on waves |
| 116 | Smoke & Fire Simulation | Advection, diffusion, temperature | grid-based fluid, buoyancy, dissipation | Add fuel source and flame color temperature |
| 117 | Fluid Solver (Eulerian) | Navier-Stokes basics, pressure | advection, diffusion, pressure projection | Interactive fluid with mouse forces |
| 118 | Hair/Rope Physics | Strand dynamics, follow-the-leader | chain of particles, length constraints | Add wind and collision with head/sphere |
| 119 | Bouncing Ball (Advanced) | Energy loss, spin, material properties | coefficient of restitution, spin, rolling | Pinball machine with flippers and bumpers |
| 120 | Destruction Physics | Fracture, Voronoi, breaking geometry | Voronoi decomposition, stress threshold | Destructible building with structural supports |

### Advanced Simulations (Math: PDEs, Statistics, Dynamical Systems)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 121 | Weather System Simulator | Wind, pressure, temperature coupling | pressure gradient, Coriolis effect, advection | Add cloud formation and precipitation |
| 122 | Crowd Simulation (Boids) | Steering behaviors, emergence | separation, alignment, cohesion, obstacles | Add panic mode and bottleneck evacuation |
| 123 | Traffic Flow Model | Vehicle interactions, congestion | car-following model, lane changing, throughput | Add traffic lights with optimization |
| 124 | Ecosystem Simulation | Predator/prey, population dynamics | Lotka-Volterra, carrying capacity, birth/death | Add a third species and food web |
| 125 | Pandemic Spread Simulator | SIR/SEIR model, spatial transmission | infection rate, recovery rate, R0, herd immunity | Add vaccination campaigns and quarantine zones |
| 126 | Forest Fire Spread | Cellular automaton, probability, wind | ignition probability, wind direction, firebreaks | Add firefighting units with strategy |
| 127 | River & Erosion | Hydraulic erosion, terrain deformation | water flow, sediment transport, deposition | Simulate dam construction and flood control |
| 128 | Galaxy Formation | N-body gravity at massive scale | dark matter halo, disk formation, rotation | Galaxy collision merger simulation |
| 129 | Molecular Dynamics | Particle interactions, thermodynamics | Lennard-Jones potential, temperature, phase | Simulate phase transition (solid to liquid to gas) |
| 130 | Earthquake Simulation | Stress accumulation, fault rupture | elastic rebound, wave propagation, magnitude | Add building response and damage assessment |
| 131 | Brain Neural Activity | Hodgkin-Huxley neuron model | ion channels, action potential, voltage gating | Network of neurons with synaptic connections |
| 132 | Chemical Reaction Network | Reaction-diffusion, Turing patterns | rate equations, diffusion, pattern formation | Generate animal coat patterns (leopard spots) |
| 133 | Space Debris Tracking | Orbital decay, collision probability | Keplerian elements, conjunction analysis | Propose debris removal mission trajectory |
| 134 | Monte Carlo Simulation | Random sampling, statistical estimation | random numbers, convergence, confidence intervals | Estimate pi using random points in circle |
| 135 | Chaos & Bifurcation | Lorenz attractor, logistic map | sensitivity to initial conditions, strange attractors | Build interactive bifurcation diagram with zoom |

---

## Phase 4: Mobile & Game Dev (35 projects)

### Mobile Foundations (Math: State Machines, Algorithms)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 136 | React Native Counter App | Navigation, state, basic UI | useState, TouchableOpacity, StyleSheet | Add multiple counters with reset and history |
| 137 | React Native Todo | AsyncStorage, persistence, lists | FlatList, AsyncStorage, CRUD | Add swipe-to-delete and section headers |
| 138 | React Native Movie Browser | API calls, FlatList, detail screens | fetch, navigation params, loading states | Add favorites with offline access |
| 139 | React Native Health Tracker | Device sensors, data logging | Accelerometer, step counting, charts | Add weekly goals and streak tracking |
| 140 | React Native Expense Tracker | Charts, date pickers, exports | react-native-chart-kit, DateTimePicker | Add receipt photo capture and OCR |
| 141 | React Native Offline Notes | Local-first sync, conflict resolution | WatermelonDB or Realm, sync strategies | Add markdown support and note sharing |
| 142 | React Native Authentication | JWT tokens, secure storage | SecureStore, token refresh, protected routes | Add biometric authentication (fingerprint/face) |
| 143 | React Native Weather App | Location services, API, maps | Geolocation, MapView, weather API | Add weather-based outfit suggestions |
| 144 | React Native Food Delivery PoC | Maps, real-time location, ordering | MapView, markers, real-time updates | Add driver tracking with live location |
| 145 | React Native Multi-Language | i18n, locale switching, RTL | i18next, locale detection, RTL layout | Add Kinyarwanda and dynamic font sizing |

### Game Dev Foundations (Math: Vectors, Matrices, Physics)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 146 | 2D Platformer (Unity) | Physics, collision, player input | Rigidbody2D, Collider2D, Input system | Add wall jumping and dash mechanic |
| 147 | Puzzle Game | Match-3 or Sokoban, game state, win | grid logic, pattern matching, undo | Add level editor for custom puzzles |
| 148 | Top-Down RPG Starter | Movement, basic combat, NPCs | tilemap, raycasting, state machine | Add stealth mechanics (line of sight) |
| 149 | Dialogue System for RPGs | Branching narrative, state machine | dialogue tree, conditions, consequences | Add voice line triggers and emotion system |
| 150 | Inventory & Equipment | Data-driven design, item slots | ScriptableObjects, drag-drop UI, stats | Add crafting recipes and item rarity |
| 151 | Procedural Dungeon Generator | BSP trees, room placement | Binary Space Partition, corridors, spawning | Add themed rooms and difficulty scaling |
| 152 | Turn-Based Battle System | Game loop, action queue, UI | command pattern, initiative, damage calc | Add elemental weaknesses and combo attacks |
| 153 | First-Person Controller | Camera, input, physics | CharacterController, mouse look, gravity | Add crouching, sprinting, and head bob |
| 154 | Third-Person Camera | Follow, orbit, collision avoidance | Cinemachine, raycasting, smoothing | Add lock-on targeting system |
| 155 | Particle Effects Editor | VFX, parameters, real-time preview | Particle System, emission, lifetime, color | Create spell effect library (fire, ice, lightning) |
| 156 | Audio Manager | Spatial audio, mixing, music | AudioSource, AudioMixer, 3D sound | Add adaptive music that changes with gameplay |
| 157 | UI Menus & Settings | Responsive game UI, options | Canvas, anchoring, PlayerPrefs | Add accessibility options (colorblind, text size) |
| 158 | Save/Load System | Serialization, persistence, slots | JSON serialization, file I/O, save slots | Add auto-save and cloud save simulation |
| 159 | Simple Multiplayer (LAN) | Netcode basics, sync, lobby | NetworkManager, RPC, state sync | Add chat and player ready system |
| 160 | Physics-Based Platformer | Custom physics engine + game | Your physics engine integrated with gameplay | Add physics puzzles (weight, momentum) |

### Advanced Game Systems (Math: Graph Theory, Optimization)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 161 | Vehicle Physics Game | Car simulation, traction, drift | wheel physics, engine curves, steering | Add motorcycle with lean mechanics |
| 162 | Destruction Physics Game | Fracture, debris, chain reaction | Voronoi, structural integrity, forces | Add repair mechanic (reverse destruction) |
| 163 | Dynamic Weather System | Visual + gameplay weather effects | particle systems, lighting, gameplay modifiers | Weather affects NPC behavior and quest availability |
| 164 | Shader Programming Basics | Vertex, fragment shaders, effects | HLSL/GLSL, UV mapping, normal maps | Create a toon/cel shader and water shader |
| 165 | Quest System | Objectives, tracking, branching | quest states, prerequisites, rewards | Add dynamic quests generated from world state |
| 166 | Crafting System | Recipes, resources, discovery | recipe database, ingredient matching, UI | Add experimentation (unknown recipe discovery) |
| 167 | Economy System | Supply, demand, trading, NPCs | price curves, merchant inventory, inflation | Add stock market with player manipulation |
| 168 | Faction & Reputation | Relationships, consequences, alliances | reputation values, faction reactions, diplomacy | Add faction wars triggered by player actions |
| 169 | Procedural Animation | IK, gait cycles, natural movement | inverse kinematics, foot placement, blending | Add creature animation (4+ legs, spider, horse) |
| 170 | Modding Support System | Plugin architecture, user content | asset bundles, scripting API, mod loader | Add mod workshop with sharing and ratings |

---

## Phase 5: AI & Machine Learning (40 projects)

### Classical ML (Math: Statistics, Linear Algebra, Calculus)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 171 | Linear Regression from Scratch | Gradient descent, cost function, fitting | MSE, learning rate, convergence, R^2 | Predict Kigali rental prices from real data |
| 172 | Logistic Regression | Binary classification, sigmoid, decision boundary | sigmoid, cross-entropy, threshold tuning | Classify SMS as spam/ham from African dataset |
| 173 | K-Means Clustering | Unsupervised learning, centroids | initialization, assignment, update, elbow method | Segment Rwandan census data by region |
| 174 | Decision Tree & Random Forest | Tree-based learning, ensembles | entropy, information gain, bagging, feature importance | Predict student performance from attendance data |
| 175 | Support Vector Machine | Margin maximization, kernel trick | hyperplane, support vectors, RBF kernel | Classify handwritten digits (MNIST subset) |
| 176 | PCA (Dimensionality Reduction) | Variance, eigenvectors, visualization | covariance matrix, eigendecomposition, scree plot | Reduce and visualize high-dimensional face data |
| 177 | Time Series Forecasting | ARIMA, trend, seasonality | autocorrelation, differencing, seasonal decomp | Forecast Kigali temperature or rainfall |
| 178 | Anomaly Detection | Isolation Forest, outlier scoring | isolation trees, contamination, thresholds | Detect fraudulent transactions in payment data |
| 179 | Text Classification | NLP, Naive Bayes, bag-of-words | tokenization, TF-IDF, Bayes theorem | Classify news articles by category (African news) |
| 180 | Recommender System | Collaborative filtering, similarity | user-item matrix, cosine similarity, SVD | Recommend African music based on listening history |
| 181 | NLP Pipeline | Tokenization, embeddings, sentiment | word2vec, spaCy, sentiment scoring | Sentiment analysis on Rwandan social media posts |
| 182 | Audio Feature Extraction | Spectrograms, MFCC, classification | FFT, mel scale, librosa, audio features | Classify African instruments from audio samples |
| 183 | Image Classification (CNN) | Convolutional layers, pooling, training | convolution, stride, padding, softmax | Classify African wildlife from photos |
| 184 | Object Detection | Bounding boxes, YOLO architecture | anchor boxes, non-max suppression, mAP | Detect and count vehicles in Kigali traffic footage |
| 185 | Generative Model (VAE/GAN) | Latent space, generation, training | encoder/decoder, discriminator/generator, loss | Generate African textile patterns |

### AI Agent Systems (Math: Graph Theory, Optimization, Game Theory)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 186 | Pathfinding AI (A*) | Graph search, heuristics, optimality | open/closed sets, g+h cost, admissible heuristic | Pathfind on actual Kigali road network data |
| 187 | Behavior Tree System | Hierarchical decisions, composites | selector, sequence, decorator, blackboard | Build AI guard with patrol, investigate, attack |
| 188 | Genetic Algorithm | Evolution, fitness, crossover, mutation | population, selection, crossover, elitism | Evolve optimal antenna shapes or bridge designs |
| 189 | Q-Learning (Gridworld) | Value iteration, exploration vs exploitation | Q-table, epsilon-greedy, reward shaping | Train agent to navigate maze with traps |
| 190 | Neural Network from Scratch | Backpropagation, no frameworks | forward pass, chain rule, weight updates | Train on XOR, then iris dataset |
| 191 | Evolutionary AI (NEAT) | Neuroevolution, topology mutation | genome, speciation, complexification | Evolve AI to play Flappy Bird clone |
| 192 | Swarm Intelligence | Ant Colony Optimization, pheromones | pheromone trails, evaporation, reinforcement | Solve traveling salesman for Rwandan cities |
| 193 | Particle Swarm Optimization | Collective intelligence, parameter tuning | personal/global best, velocity update | Optimize neural network hyperparameters |
| 194 | Flocking & Steering | Multi-agent coordination, emergence | Reynolds rules, obstacle avoidance, leader | Simulate bird migration patterns |
| 195 | NPC Decision Making | Utility AI, scoring, goal-driven | utility functions, action scoring, priorities | Build a Sims-like NPC with needs and personality |
| 196 | ML for Physics Prediction | Neural net learns physical systems | training on simulation data, generalization | Predict pendulum motion from initial conditions |
| 197 | Inverse Kinematics | Character animation, joint solving | CCD, FABRIK, joint limits | Robot arm reaches for moving target |
| 198 | Multi-Agent RL | Competition and cooperation | independent Q-learning, shared reward | Predator-prey training (wolves hunt deer) |
| 199 | Goal-Oriented Action Planning | Planning AI, world state, preconditions | world state, actions, planner, A* on actions | NPC plans daily routine (eat, work, sleep, socialize) |
| 200 | Influence Maps | Tactical AI, spatial reasoning | heat maps, threat assessment, territory | RTS-style AI that controls territory |

### Deep Learning (Math: Linear Algebra, Calculus, Information Theory)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 201 | CNN (PyTorch) | CIFAR-10, ResNet basics, training | DataLoader, Conv2d, BatchNorm, SGD | Train on African sign language dataset |
| 202 | RNN / LSTM | Sequence modeling, time series | hidden state, gates, vanishing gradients | Generate Kinyarwanda text character-by-character |
| 203 | Transformer Architecture | Self-attention, multi-head, position encoding | attention, Q/K/V, positional encoding | Build a mini translator (English to French) |
| 204 | Fine-Tuned LLM (Claude API) | Domain-specific knowledge, prompting | system prompts, few-shot, RAG basics | Build a Rwanda travel guide chatbot |
| 205 | Vision Transformer (ViT) | Image patches as tokens, classification | patch embedding, class token, attention maps | Classify satellite images of African terrain |
| 206 | Diffusion Model | Noise schedule, denoising, generation | forward/reverse process, U-Net, sampling | Generate African landscape art |
| 207 | Reinforcement Learning (PPO) | Policy optimization, advantage estimation | policy gradient, clipping, GAE | Train agent for African board game (Mancala) |
| 208 | Multi-Modal Model | Vision + language, image captioning | cross-attention, CLIP, contrastive learning | Caption African wildlife photos |
| 209 | Graph Neural Network | Node classification, message passing | adjacency matrix, aggregation, GCN layers | Predict protein properties from molecular graphs |
| 210 | Production ML Pipeline | Training to inference to monitoring to retrain | MLflow, model versioning, drift detection | Deploy a model with A/B testing |

---

## Phase 6: Systems & Infrastructure (25 projects)

### DevOps & Systems (Math: Queueing Theory, Optimization)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 211 | Docker-ize Existing App | Containers, multi-stage builds, compose | Dockerfile, docker-compose, volumes, networks | Multi-container app (web + db + cache + worker) |
| 212 | CI/CD Pipeline | Auto-test, build, deploy on push | GitHub Actions, workflows, artifacts, secrets | Add staging environment with approval gates |
| 213 | Load Balancer | Multiple servers, round-robin, health checks | Nginx, upstream, health_check, sticky sessions | Add blue-green deployment switching |
| 214 | Database Backup & Recovery | Automated backups, restore testing | pg_dump, cron, S3, point-in-time recovery | Add disaster recovery drill automation |
| 215 | Monitoring & Logging | Metrics, dashboards, alerting | Prometheus, Grafana, ELK, alert rules | Add custom business metrics dashboard |
| 216 | Kubernetes Deployment | Container orchestration, scaling | pods, services, deployments, ingress | Add horizontal pod autoscaler |
| 217 | Redis Caching Layer | Performance, cache strategies, invalidation | cache-aside, TTL, cache stampede prevention | Benchmark before/after with load testing |
| 218 | API Rate Limiting | Token bucket, fairness, abuse prevention | sliding window, token bucket, Redis counters | Add tiered rate limits by API key |
| 219 | CDN Integration | Edge delivery, cache headers, performance | Cache-Control, ETag, edge locations | Measure performance improvement with analytics |
| 220 | Disaster Recovery Playbook | Documentation, runbooks, testing | RTO, RPO, failover procedures, communication | Run a chaos engineering experiment |
| 221 | Terraform Infrastructure as Code | Declarative infrastructure, state management | HCL, providers, state files, plan/apply | Multi-environment setup (dev/staging/prod) |
| 222 | Secret Management (Vault) | Secure credential storage, rotation | HashiCorp Vault, encryption, access policies, audit | Auto-rotate database credentials on schedule |
| 223 | Performance Testing Suite | Load testing, bottleneck identification | Locust/k6, latency percentiles, throughput, profiling | Generate performance regression report with graphs |

### Advanced Architecture (Math: Distributed Systems Theory)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 224 | Microservices Architecture | Service decomposition, messaging | API gateway, service discovery, eventual consistency | Add circuit breaker pattern |
| 225 | Event-Driven System | Event sourcing, CQRS, audit trails | event store, projections, command/query separation | Add event replay for debugging |
| 226 | Real-Time Analytics Pipeline | Stream processing, aggregation | Kafka, windowing, exactly-once processing | Real-time dashboard of streaming data |
| 227 | Payment Integration (Pesapal) | African payments, webhooks, security | payment flow, IPN, reconciliation, PCI | Add multi-currency support (RWF, KES, USD) |
| 228 | Search Engine (Elasticsearch) | Full-text search, facets, relevance | inverted index, analyzers, boosting, aggregations | Build a product search with autocomplete |
| 229 | Video Streaming PoC | Encoding, adaptive bitrate, delivery | HLS, transcoding, CDN, buffer management | Add live streaming support |
| 230 | Geolocation & Route Optimization | Maps, shortest path, delivery | Haversine, graph algorithms, TSP approximation | Optimize delivery routes in Kigali |
| 231 | IoT Dashboard | Sensor data, real-time, alerts | MQTT, time-series DB, WebSocket updates | Add predictive maintenance alerts |
| 232 | Fraud Detection Pipeline | ML + rules, streaming, real-time | feature engineering, online learning, rules engine | Add explainable AI for flagged transactions |
| 233 | Knowledge Graph | Entity relationships, semantic search | triples, SPARQL, graph embeddings, Neo4j | Build a Rwandan cultural knowledge graph |
| 234 | Message Queue System (RabbitMQ) | Async messaging, pub/sub, reliability | exchanges, queues, routing keys, dead letter, ack | Build order processing pipeline with retry logic |
| 235 | Multi-Tenant SaaS Architecture | Tenant isolation, shared infrastructure | schema-per-tenant, row-level security, billing | Add tenant-specific customization and white-labeling |

---

## Phase 7: African Impact & Research (32 projects)

### Climate & Environment (Math: PDEs, Statistics, Optimization)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 236 | Climate Impact Simulator | Sea-level rise, storm frequency, damage prediction | GIS data, risk modeling, monte carlo | Add evacuation route optimizer |
| 237 | Drought & Crop Yield Predictor | Climate patterns, agricultural planning | time series, satellite data, regression | Add crop recommendation engine |
| 238 | Urban Heat Analyzer | Urbanization heat islands, risk zones | spatial analysis, temperature modeling, GIS | Recommend green space placement |
| 239 | Deforestation Tracker | Satellite imagery, change detection | image differencing, classification, NDVI | Predict future deforestation patterns |
| 240 | Air Quality Monitor | Sensor data, pollution modeling, alerts | AQI, interpolation, health thresholds | Add source attribution modeling |
| 241 | Water Resource Optimizer | Hydrology, allocation, sustainability | flow networks, optimization, constraints | Multi-stakeholder water sharing simulator |
| 242 | Renewable Energy Site Selector | Solar/wind potential, terrain analysis | GIS, solar irradiance, wind rose data | Add cost-benefit analysis and ROI projection |
| 243 | Carbon Footprint Calculator | Lifecycle analysis, emissions tracking | emission factors, scope 1/2/3, visualization | Add reduction strategy recommendations |
| 244 | Biodiversity Tracker | Species monitoring, habitat analysis, conservation | species classification, GIS, population modeling | Add poaching risk prediction and patrol routing |
| 245 | Soil Health Monitor | Agricultural soil analysis, nutrient tracking | sensor data, nutrient cycles, pH modeling, yield correlation | Add fertilizer recommendation engine for Rwandan crops |

### Healthcare & Education (Math: Statistics, Probability, ML)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 246 | Disease Progression Simulator | Cancer/disease stages, visual teaching | Markov chains, state transitions, visualization | Add treatment response modeling |
| 247 | Student Dropout Predictor | Attendance, grades, early warning | classification, feature engineering, intervention | Add personalized intervention suggestions |
| 248 | Education Policy Simulator | Investment outcomes, scenario modeling | agent-based modeling, policy variables, outcomes | Compare Rwanda vs Kenya education investments |
| 249 | Public Health Dashboard | Disease tracking, outbreak detection | time series, anomaly detection, geographic viz | Add contact tracing network visualization |
| 250 | Medical Image Classifier | X-ray/scan analysis, CNN application | transfer learning, data augmentation, sensitivity | Add Grad-CAM for explainable diagnoses |
| 251 | Drug Interaction Checker | Knowledge graph, safety validation | graph database, rule engine, contraindications | Add traditional medicine interactions |
| 252 | Mental Health Screening Tool | Questionnaire, scoring, referral | validated instruments, scoring algorithms, privacy | Add multilingual support (Kinyarwanda, French) |
| 253 | Nutrition Planner (Local Foods) | African foods database, diet optimization | nutritional data, linear programming, meal plans | Add budget constraints and local market prices |
| 254 | Telemedicine Platform Prototype | Remote consultation, scheduling, records | WebRTC, appointment system, medical records, HIPAA | Add AI symptom pre-screening triage |
| 255 | Epidemic Early Warning System | Outbreak detection, spatial spread tracking | anomaly detection, sentinel surveillance, R0 estimation | Add social media signal monitoring for outbreak rumors |

### Governance, Economics & Space (Math: Optimization, Game Theory, Orbital Mechanics)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 256 | Public Service Complaint Analyzer | NLP categorization, priority routing | text classification, sentiment, topic modeling | Add trend analysis and department performance scoring |
| 257 | Election Claims Fact-Triage | Speech analysis, claim extraction, flagging | NER, claim detection, source matching | Add real-time live debate analysis |
| 258 | Local Job Market Predictor | Economic analysis, trend forecasting | time series, economic indicators, sector analysis | Add skills gap analysis and training recommendations |
| 259 | Entrepreneur Opportunity Map | Business gap analysis, location intelligence | spatial analysis, demand modeling, competition | Add startup success probability scoring |
| 260 | Poverty-Reduction Simulator | Policy intervention modeling, outcomes | agent-based model, income distribution, Gini | Compare cash transfer vs education investment |
| 261 | Smart City Traffic Predictor | Road patterns, congestion, AI optimization | graph neural networks, flow optimization | Design optimal bus routes for Kigali |
| 262 | Infrastructure Failure Warning | Risk detection, predictive maintenance | sensor fusion, degradation models, alerts | Add bridge/road inspection prioritization |
| 263 | Orbital Mechanics + AI Planner | Spacecraft trajectory optimization | Hohmann transfers, delta-v, fuel optimization | Plan multi-planet mission (gravity assists) |
| 264 | Satellite Collision Prediction | Orbital simulation, conjunction analysis | TLE data, propagation, probability of collision | Propose avoidance maneuver and fuel cost |
| 265 | AI Space Weather Predictor | Solar activity, radiation forecasting | NASA data, time series, solar cycle patterns | Add satellite vulnerability assessment |
| 266 | Multi-Agent Disaster Simulator | Pre/post disaster response modeling | multi-agent systems, resource allocation, triage | Optimize evacuation for Kigali flood scenario |
| 267 | Earth Evolution Simulator | Planetary modeling, geological time | plate tectonics, climate models, extinction events | Add human civilization impact modeling |

---

## Phase 8: Advanced Math & Scientific Computing (20 projects)

### Advanced Mathematics (Math: Everything)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 268 | Finite Element Method (FEM) | Mesh generation, weak formulation, solving | triangulation, basis functions, stiffness matrix | Simulate stress in a bridge structure |
| 269 | Computational Fluid Dynamics | Navier-Stokes 2D, pressure correction | staggered grid, SIMPLE algorithm, vorticity | Simulate airflow around an airfoil |
| 270 | FFT Exploration | Frequency domain, filtering, analysis | DFT, butterfly, convolution theorem | Build an audio equalizer |
| 271 | Spectral Methods for PDEs | Fourier basis, high-order accuracy | spectral differentiation, Chebyshev polynomials | Solve Burgers equation with shock |
| 272 | Adaptive Mesh Refinement | Dynamic grid refinement, error estimation | error indicators, h-refinement, tree structures | Track shock wave with adaptive resolution |
| 273 | Particle-in-Cell Simulation | Plasma dynamics, electromagnetic fields | charge deposition, field solve, particle push | Simulate plasma wake in accelerator |
| 274 | Stochastic Differential Equations | Brownian motion, noise, financial modeling | Wiener process, Ito calculus, Euler-Maruyama | Model stock prices with geometric Brownian motion |
| 275 | Optimization Algorithms | Gradient descent, Newton, BFGS, convergence | line search, Hessian, quasi-Newton, constraints | Optimize a real engineering design problem |
| 276 | Symbolic Math Engine | Computer algebra, simplification | expression trees, differentiation rules, pattern matching | Build a step-by-step equation solver with explanations |
| 277 | Differential Geometry Viz | Curvature, geodesics, manifolds | Gaussian curvature, parallel transport, surfaces | Visualize shortest paths on a torus |
| 278 | Quantum Mechanics Simulator | Schrodinger equation, probability densities | wave function, potential wells, tunneling | Simulate quantum tunneling through a barrier |
| 279 | Graph Theory Algorithms | Advanced graph problems, network analysis | max flow, min cut, matching, centrality | Analyze a real social network dataset |
| 280 | N-Body (Barnes-Hut) | O(n log n) gravity simulation | octree, multipole expansion, approximation | Simulate galaxy cluster with 100k+ particles |
| 281 | Multigrid Solver | Hierarchical refinement, fast PDE solving | restriction, prolongation, V-cycle, smoothing | Solve Poisson equation on 1M+ grid |
| 282 | Tensor Calculus Visualizer | Tensors, contraction, transformation | index notation, metric tensor, Christoffel symbols | Visualize spacetime curvature near a mass |
| 283 | Bayesian Inference Engine | Prior, likelihood, posterior, MCMC sampling | Bayes theorem, conjugate priors, Metropolis-Hastings | Apply to real-world A/B testing with decision framework |
| 284 | Topological Data Analysis | Persistent homology, shape of data | simplicial complexes, Betti numbers, persistence diagrams | Find hidden structure in high-dimensional African census data |
| 285 | Wavelet Transform Analyzer | Time-frequency analysis, signal processing | Haar, Daubechies wavelets, multiresolution, denoising | Denoise and analyze seismic data from East African Rift |
| 286 | Numerical Relativity (Simple) | Einstein field equations, spacetime curvature | metric tensor, geodesics, Schwarzschild solution | Simulate light bending around a black hole |
| 287 | Category Theory Visualizer | Functors, morphisms, composition | objects, arrows, commutative diagrams, natural transformations | Map category theory concepts to programming patterns |

---

## Phase 9: Personal Capstones (13 projects)

### AI Me - Personal AI Avatar (Math: Deep Learning, Signal Processing)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 288 | AI Me: Voice Synthesis | Clone your voice, text-to-speech | voice cloning, TTS, audio processing | Test with 10 people, measure recognition rate |
| 289 | AI Me: Visual Avatar | Deepfake/avatar generation from photos | face generation, expression mapping, rendering | Real-time avatar that mirrors your expressions |
| 290 | AI Me: Personality Engine | Fine-tuned LLM with your personality | personal data training, style transfer, guardrails | Blind test: can friends tell AI from real you? |
| 291 | AI Me: Full Integration | Voice + visual + personality combined | multimodal integration, latency, coherence | Deploy and have it handle a real conversation |

### African Life Game - GTA/Sims Style (Math: Procedural Generation, Agent AI, Economics)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 292 | African Game: World Generation | Procedural Africa, countries, regions | PCG, terrain, population distribution, culture | Generate 5 distinct African regions with unique feel |
| 293 | African Game: Character System | Birth, status, identity, traits | character generation, social systems, randomization | Create 100 unique characters with believable backgrounds |
| 294 | African Game: Economy & Society | Jobs, money, relationships, daily life | economic simulation, social networks, time system | Simulate one game-year with emergent stories |
| 295 | African Game: Full Prototype | Playable vertical slice, 30 min gameplay | all systems integrated, polish, testing | 5 playtesters give feedback, iterate |

### Ashes of Ikarra - Ultimate Game Project (Math: Everything)

| # | Project | Description | Key Concepts | Exercise Twist |
|---|---------|-------------|--------------|----------------|
| 296 | Ashes of Ikarra: Custom Physics | Your physics engine integrated into game | rigid body, collision, particles, environment | Physics puzzle that showcases your engine |
| 297 | Ashes of Ikarra: AI Systems | NPC behavior, combat AI, world AI | behavior trees, utility AI, GOAP, faction AI | NPCs that players describe as 'alive' |
| 298 | Ashes of Ikarra: Procedural World | Terrain, dungeons, encounters, weather | noise, BSP, biomes, dynamic events | World that feels different each playthrough |
| 299 | Ashes of Ikarra: Narrative Engine | Branching story, memory mechanic, choices | story graph, consequence tracking, player agency | Story that players discuss and debate |
| 300 | Ashes of Ikarra: Playable Chapter 1 | 30-60 min gameplay, full experience | all systems, polish, audio, UI, testing | Ship it. Get real player feedback. |

---

## Summary

| Phase | Focus | Projects | Math Thread |
|-------|-------|----------|-------------|
| 1 | Foundations | 50 | Logic, Algorithms, Number Theory, Linear Algebra |
| 2 | Web & Data | 40 | State Machines, Set Theory, Graph Theory |
| 3 | Scientific Computing | 45 | Calculus, Trigonometry, PDEs, Dynamical Systems |
| 4 | Mobile & Game Dev | 35 | Vectors, Matrices, Physics, Optimization |
| 5 | AI & Machine Learning | 40 | Statistics, Linear Algebra, Calculus, Information Theory |
| 6 | Systems & Infrastructure | 25 | Queueing Theory, Distributed Systems |
| 7 | African Impact & Research | 32 | PDEs, Statistics, Optimization, Game Theory |
| 8 | Advanced Math | 20 | Everything |
| 9 | Personal Capstones | 13 | Everything |
| **Total** | | **300** | |

---

*Built for a future African tech leader. Every project counts.*