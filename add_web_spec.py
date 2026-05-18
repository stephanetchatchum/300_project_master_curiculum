# Detailed specs for Phase 2: Web & Data — projects 51-70
NEW_SPECS = {
"51": """WHAT YOU'RE BUILDING
A responsive personal portfolio website built with plain HTML, CSS, and JavaScript — your professional home on the web and the landing page for your space-focused project portfolio.

REQUIREMENTS
- Plain HTML, CSS, JavaScript — no framework yet
- Semantic structure: header, nav, main, multiple section elements, footer
- Sections: Hero (name + one-line mission), About, Projects gallery, Skills, Contact
- Responsive layout using CSS Grid and Flexbox, mobile-first
- Sticky navigation bar with smooth scrolling to each section
- Projects gallery: cards with image, title, description, and links (live demo + code)
- At least one JS interaction: dark/light theme toggle, project filter, or animated counters
- SEO basics: descriptive title, meta description, Open Graph tags, favicon
- Deploy it live on GitHub Pages, Netlify, or Vercel

CONCEPTS TO LEARN
- Semantic HTML5 — https://developer.mozilla.org/en-US/docs/Glossary/Semantics
- CSS Grid — https://css-tricks.com/snippets/css/complete-guide-grid/
- Flexbox — https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- Media queries — https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries
- Meta tags and SEO — https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta
- GitHub Pages deployment — https://pages.github.com/

PAGE STRUCTURE
  Hero      -> name, tagline, call-to-action button
  About     -> short bio, photo, what you do
  Projects  -> responsive grid of project cards
  Skills    -> grouped skill tags or progress bars
  Contact   -> email, social links, optional form

EDGE CASES TO HANDLE
- Very small screens (320px wide) — nothing should overflow
- Very wide screens — content should not stretch endlessly (use a max-width container)
- Missing project image — show a placeholder
- Theme toggle should persist across reloads (localStorage)
- Navigation should still work if JavaScript is disabled (plain anchor links)

STRETCH GOALS (OPTIONAL)
- Projects gallery with embedded space simulations (iframes or canvas demos)
- Scroll-reveal animations using IntersectionObserver
- A custom 404 page
- Accessibility pass: keyboard navigation, focus styles, alt text, ARIA labels
- Lighthouse score above 90 in every category""",

"52": """WHAT YOU'RE BUILDING
A fully working calculator web app — buttons, a display, and live evaluation — built with the DOM and event handling.

REQUIREMENTS
- A grid of buttons: digits 0-9, decimal point, + - * /, equals, clear (C), and delete/backspace
- A display showing the current expression and/or result
- Click any button to build an expression; equals evaluates it
- Keyboard support: digits and operators, Enter = equals, Escape = clear, Backspace = delete
- Handle chained operations (e.g. 5 + 3 * 2)
- Handle decimals and negative numbers
- Clear button resets everything
- Division by zero shows "Error", not a crash or "Infinity"
- Do NOT run raw eval() on user input — write a small parser or a safe evaluation function

CONCEPTS TO LEARN
- DOM selection — https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector
- Event handling and delegation — https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener
- Keyboard events — https://developer.mozilla.org/en-US/docs/Web/API/Element/keydown_event
- Managing state in a variable — https://javascript.info/variables
- Why eval() is risky — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval

EXAMPLE INTERACTION
  Display: 0
  [click 5][click +][click 3] -> Display: 5 + 3
  [click =]                   -> Display: 8
  [type 1 2 / 4][Enter]       -> Display: 3

EDGE CASES TO HANDLE
- Multiple decimal points in one number (reject the second)
- A leading operator (e.g. starting with *)
- Two operators in a row (replace the first, or ignore the second)
- Division by zero
- Very long results (round, or use exponential notation)
- Pressing equals with an incomplete expression

STRETCH GOALS (OPTIONAL)
- Scientific functions: sin, cos, tan, log, sqrt, power — useful for your physics calculations later
- A calculation history panel (list of past results)
- Memory keys: M+, M-, MR, MC
- Parentheses support
- A degrees/radians toggle for the trig functions""",

"53": """WHAT YOU'RE BUILDING
A weather dashboard that fetches live weather data for any city and displays it cleanly, using fetch and async/await.

REQUIREMENTS
- Use a free weather API (Open-Meteo, OpenWeatherMap, or WeatherAPI)
- A search box: user types a city name and submits
- Display: city name, current temperature, conditions, humidity, wind speed, an icon
- Show a short forecast (next few hours or next few days)
- Use fetch() with async/await
- A loading state while the request is in flight
- Error handling: city not found, network error, bad API key
- Remember the last searched city (localStorage) and load it on startup

CONCEPTS TO LEARN
- The fetch() API — https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
- async/await — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
- Promises — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
- JSON parsing — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse
- HTTP status codes — https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

API NOTE
Open-Meteo needs no API key and is great for learning. OpenWeatherMap needs a free key — never commit it to a public repo.

EXAMPLE INTERACTION
  Search: Kigali
  -> Kigali, Rwanda
     22 C, Partly cloudy
     Humidity 65%, Wind 12 km/h
     Next 3 days: 23 / 21 / 24

EDGE CASES TO HANDLE
- City name not found (404)
- Empty search submission
- Network offline
- API rate limit reached
- Ambiguous city names (multiple cities with the same name)

STRETCH GOALS (OPTIONAL)
- Add space weather: solar wind speed and the geomagnetic Kp index (NOAA SWPC API)
- Geolocation: detect the user's location automatically
- A 5-day temperature chart
- A unit toggle: Celsius / Fahrenheit
- A background or icon that changes with the weather condition""",

"54": """WHAT YOU'RE BUILDING
A currency converter that uses live exchange rates to convert between any two currencies, with caching so it stays fast and respects rate limits.

REQUIREMENTS
- Use a free exchange-rate API (exchangerate.host, Frankfurter, or open.er-api.com)
- Two dropdowns: from-currency and to-currency
- An amount input and a converted result
- Convert as the user types (debounced) or on a button click
- A "swap currencies" button
- Cache the rates in localStorage with a timestamp; only refetch if the cache is older than ~1 hour
- Loading and error states

CONCEPTS TO LEARN
- REST APIs — https://developer.mozilla.org/en-US/docs/Glossary/REST
- fetch() and async/await — https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
- localStorage — https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
- Debouncing — https://www.freecodecamp.org/news/javascript-debounce-example/
- Caching with a TTL — https://web.dev/articles/cache-api-quick-guide

EXAMPLE INTERACTION
  From: USD   To: RWF   Amount: 100
  -> 100 USD = 131,200 RWF
     (rates cached 14 minutes ago)
  [Swap] -> From: RWF  To: USD

EDGE CASES TO HANDLE
- The same currency selected for both (result equals the input)
- Non-numeric or negative amount
- API down — fall back to the last cached rates and warn the user
- A currency with no available rate
- Very large amounts (format with thousands separators)

STRETCH GOALS (OPTIONAL)
- A historical rate chart for the selected pair (last 30 days)
- Show the trend (up or down) since yesterday
- A small watchlist of favourite pairs
- Offline mode: work entirely from cached rates""",

"55": """WHAT YOU'RE BUILDING
A robust, accessible signup/contact form with real-time validation and clear user feedback.

REQUIREMENTS
- A form with several field types: name, email, password, confirm password, phone, a select, a terms checkbox
- Validate each field with regex and logic rules
- Real-time feedback: validate on blur AND on input, not only on submit
- Clear inline error messages next to each field
- A visible success state for valid fields
- Disable the submit button until the whole form is valid
- A password strength meter
- Accessible: labels tied to inputs, aria-invalid, aria-describedby, errors announced to screen readers

VALIDATION RULES
  Name     -> not empty; letters, spaces, hyphens only
  Email    -> valid email pattern
  Password -> min 8 chars, at least one letter and one number
  Confirm  -> must match password
  Phone    -> valid format (support international)
  Terms    -> must be checked

CONCEPTS TO LEARN
- Regular expressions — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions
- Form events: input, blur, submit — https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/blur_event
- The Constraint Validation API — https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation
- ARIA for forms — https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-invalid
- preventDefault() — https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault

EDGE CASES TO HANDLE
- Pasting content (the input event covers this; blur alone does not)
- Whitespace-only input
- A valid but unusual email format
- The user fixes an error — the message must clear immediately
- Submitting with the keyboard (Enter)

STRETCH GOALS (OPTIONAL)
- International phone validation with country codes
- Async validation (e.g. "username already taken" — simulate with a delay)
- A multi-step form with a progress indicator
- Save draft input to localStorage so a refresh doesn't lose data
- On submit, show all errors summarised at the top with links to each field""",

"56": """WHAT YOU'RE BUILDING
A live markdown editor: type markdown on the left, see rendered HTML update instantly on the right.

REQUIREMENTS
- A split view: a textarea on the left, a rendered preview on the right
- Support core markdown: headings, bold, italic, links, images, lists, blockquotes, inline code, code blocks, horizontal rules
- Update the preview in real time as the user types
- Either write your own parser with regex OR use a library (marked.js) — try your own first for the learning
- Sanitize the output to prevent script injection (escape raw HTML or use a sanitizer)
- A toolbar with buttons that insert markdown (bold, italic, link, etc.)
- A word and character count
- Save the document to localStorage; export it as a .md or .html file

CONCEPTS TO LEARN
- Markdown syntax — https://www.markdownguide.org/basic-syntax/
- String replace with regex — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace
- innerHTML and the XSS risk — https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks
- textContent vs innerHTML — https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent
- Blob and file download — https://developer.mozilla.org/en-US/docs/Web/API/Blob

EXAMPLE
  Left (you type):
    # Orbital Mechanics
    The **Hohmann transfer** is the cheapest two-burn path.
  Right (rendered):
    Orbital Mechanics   (large heading)
    The Hohmann transfer is the cheapest two-burn path.

EDGE CASES TO HANDLE
- An empty editor (the preview is empty, not broken)
- Unclosed markdown (a single * or unbalanced backticks)
- Raw HTML or a <script> typed by the user (must be neutralised)
- Very long documents (typing must stay responsive)
- Special characters &, <, > must render as visible text

STRETCH GOALS (OPTIONAL)
- Code syntax highlighting inside code blocks
- LaTeX math rendering with KaTeX — useful for your physics notes
- Scroll-sync between the editor and the preview
- Multiple saved documents with a sidebar
- Print or export to PDF""",

"57": """WHAT YOU'RE BUILDING
A fast client-side search and filter interface over a dataset — the kind of UI behind every product list, table, or catalogue.

REQUIREMENTS
- Load a dataset (a JSON array of at least 50 items — could be your 300 projects, books, or planets)
- A search box that filters items by text as the user types
- Debounce the search input so it doesn't filter on every keystroke
- Multiple filters: at least one dropdown (category) and one checkbox/toggle group
- Combine filters: search AND category AND toggles all apply together
- Highlight the matching text in the results
- A result count and a clear "no results" state
- A "clear all filters" button
- Sort options (by name, by date, etc.)

CONCEPTS TO LEARN
- Array filter, map, sort — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
- Debouncing — https://www.freecodecamp.org/news/javascript-debounce-example/
- String.includes and case-insensitive matching — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes
- Rendering lists efficiently — https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement

EXAMPLE INTERACTION
  Search: "orbit"   Category: Physics   Sort: A-Z
  -> 6 results, "orbit" highlighted in each
  Clear filters -> all 50 items return

EDGE CASES TO HANDLE
- No results match (show a friendly message)
- A search term with regex-special characters (escape them before matching)
- Empty search (show everything)
- Case and accent differences
- A very large dataset (filtering must stay snappy)

STRETCH GOALS (OPTIONAL)
- Multi-field search with AND/OR logic
- Fuzzy search that tolerates typos
- URL state: filters reflected in the query string so a search is shareable
- Pagination or infinite scroll
- Result counts shown next to each category""",

"58": """WHAT YOU'RE BUILDING
A multi-section responsive web page built mobile-first — the curriculum suggests a science publication / article template — that adapts gracefully from phone to desktop.

REQUIREMENTS
- Design for the smallest screen FIRST, then add complexity with min-width media queries
- A responsive layout: single column on mobile, multi-column on larger screens
- A responsive navigation: a hamburger menu on mobile, a full nav bar on desktop
- Responsive typography using rem/em and fluid sizing (clamp())
- Responsive images that scale and never overflow
- A content-rich page: article header, body text, figures with captions, a sidebar, footer
- Touch-friendly tap targets on mobile (minimum 44x44px)
- Test at 320px, 768px, and 1200px widths

CONCEPTS TO LEARN
- Mobile-first design — https://www.lukew.com/ff/entry.asp?933
- Media queries — https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries
- rem, em, and clamp() — https://developer.mozilla.org/en-US/docs/Web/CSS/clamp
- Responsive images (srcset, sizes) — https://developer.mozilla.org/en-US/docs/Web/HTML/Responsive_images
- The viewport meta tag — https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag

BREAKPOINT PLAN
  Base (mobile)     -> single column, hamburger nav, stacked figures
  >= 768px tablet   -> two columns, inline nav, side-by-side figures
  >= 1200px desktop -> article + sidebar, wider margins

EDGE CASES TO HANDLE
- Very small screens (320px) — no horizontal scroll
- Landscape phone orientation
- Long words or URLs breaking the layout (use word-wrap / overflow-wrap)
- Images of different aspect ratios
- The hamburger menu must be keyboard accessible

STRETCH GOALS (OPTIONAL)
- A dark mode that follows prefers-color-scheme
- A reading-progress bar at the top
- Container queries for true component-level responsiveness
- A print stylesheet
- Reduced-motion support (prefers-reduced-motion)""",

"59": """WHAT YOU'RE BUILDING
Your first backend API with Flask — a small web server that responds to HTTP requests with JSON.

REQUIREMENTS
- Install Flask and create a basic app
- At least 4 routes:
  - GET  /                  -> a welcome message
  - GET  /api/time          -> the current server time as JSON
  - GET  /api/greet/<name>  -> a personalised greeting using a URL parameter
  - POST /api/echo          -> returns the JSON body that was sent
- Return proper JSON with jsonify()
- Return correct HTTP status codes (200, 201, 400, 404)
- A custom 404 handler that returns JSON, not an HTML error page
- Request logging middleware: log method, path, and status for every request
- Test every route with curl or a tool like Postman / Thunder Client

CONCEPTS TO LEARN
- Flask quickstart — https://flask.palletsprojects.com/en/latest/quickstart/
- Routes and @app.route — https://flask.palletsprojects.com/en/latest/quickstart/#routing
- The request object — https://flask.palletsprojects.com/en/latest/api/#flask.request
- jsonify — https://flask.palletsprojects.com/en/latest/api/#flask.json.jsonify
- HTTP methods — https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- HTTP status codes — https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

INSTALLATION REQUIRED
  pip install flask

EXAMPLE INTERACTION
  $ curl http://localhost:5000/api/greet/Stephane
  {"message": "Hello, Stephane!"}

  $ curl -X POST http://localhost:5000/api/echo -H "Content-Type: application/json" -d '{"x": 1}'
  {"you_sent": {"x": 1}}

EDGE CASES TO HANDLE
- POST /api/echo with no body or invalid JSON
- A route that doesn't exist (404 as JSON)
- The wrong HTTP method on a route (405)
- A missing Content-Type header on POST
- An empty name in the greet route

STRETCH GOALS (OPTIONAL)
- Add CORS support (flask-cors) so a browser front-end can call it
- Add a /health endpoint for monitoring
- Environment-based config (debug vs production)
- Rate-limiting middleware
- Serve API docs at /docs""",

"60": """WHAT YOU'RE BUILDING
A complete REST API with full Create, Read, Update, Delete operations and a real database — the curriculum twist is an API serving NASA exoplanet data.

REQUIREMENTS
- Use Flask with SQLAlchemy and an SQLite database (Postgres comes in project 61)
- A resource model — e.g. Exoplanet (name, host_star, mass, radius, discovery_year, distance_ly)
- Full REST endpoints:
  - GET    /api/planets       -> list all (with pagination)
  - GET    /api/planets/<id>  -> get one
  - POST   /api/planets       -> create (201 on success)
  - PUT    /api/planets/<id>  -> update
  - DELETE /api/planets/<id>  -> delete (204 on success)
- Request body validation: reject missing or invalid fields with 400
- Proper status codes and JSON error messages everywhere
- Query parameters: filter (e.g. ?min_mass=1) and sort
- Seed the database with some real exoplanet data

CONCEPTS TO LEARN
- REST principles — https://developer.mozilla.org/en-US/docs/Glossary/REST
- Flask-SQLAlchemy — https://flask-sqlalchemy.palletsprojects.com/
- ORM models and queries — https://docs.sqlalchemy.org/en/20/orm/quickstart.html
- HTTP status codes for CRUD — https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Input validation patterns — https://flask.palletsprojects.com/en/latest/patterns/

INSTALLATION REQUIRED
  pip install flask flask-sqlalchemy

EXAMPLE INTERACTION
  $ curl http://localhost:5000/api/planets?min_mass=1
  [{"id": 1, "name": "Kepler-22b", "mass": 2.4, ...}]

  $ curl -X POST .../api/planets -d '{"name": "Proxima b", ...}'
  201 Created -> {"id": 9, "name": "Proxima b", ...}

EDGE CASES TO HANDLE
- GET / PUT / DELETE on an id that doesn't exist (404)
- POST with missing required fields (400)
- POST with wrong data types (mass sent as text)
- Duplicate names (decide: allow or reject)
- An empty database (GET returns [])
- Invalid query-parameter values

STRETCH GOALS (OPTIONAL)
- Pagination metadata (total, page, per_page, next/prev links)
- PATCH for partial updates
- Marshmallow schemas for clean serialization and validation
- Soft delete (mark as deleted instead of removing)
- Automated tests with pytest""",

"61": """WHAT YOU'RE BUILDING
A well-designed relational database schema — the curriculum twist is a satellite tracking database — applying normalization, keys, and indexes.

REQUIREMENTS
- Design a schema with at least 4 related tables, for example:
  - satellites (id, name, norad_id, launch_date, operator_id)
  - operators (id, name, country)
  - orbits (id, satellite_id, apogee_km, perigee_km, inclination, period_min)
  - ground_stations (id, name, latitude, longitude)
  - passes (id, satellite_id, ground_station_id, start_time, max_elevation)
- Apply normalization up to 3NF (no repeating groups, no partial or transitive dependencies)
- Define primary keys and foreign keys with proper constraints
- Add NOT NULL, UNIQUE, and CHECK constraints where appropriate
- Create indexes on columns used for lookups and joins
- Write the schema as a .sql file (CREATE TABLE statements)
- Write at least 8 useful queries: joins, aggregations, filtering, grouping
- Use EXPLAIN to see how an index changes a query plan

CONCEPTS TO LEARN
- Database normalization (1NF-3NF) — https://www.guru99.com/database-normalization.html
- Primary and foreign keys — https://www.postgresql.org/docs/current/ddl-constraints.html
- Indexes — https://www.postgresql.org/docs/current/indexes.html
- JOINs — https://www.postgresql.org/docs/current/tutorial-join.html
- EXPLAIN and query plans — https://www.postgresql.org/docs/current/using-explain.html

INSTALLATION REQUIRED
  PostgreSQL (local, or a free hosted instance). Use psql or a GUI like pgAdmin / DBeaver.

EXAMPLE QUERIES TO WRITE
  - All satellites launched after 2020 with their operator's country
  - Count of satellites per operator
  - Ground stations that have seen a given satellite, ordered by max elevation
  - Average orbital period grouped by inclination band

EDGE CASES TO HANDLE
- Deleting an operator that still has satellites (choose ON DELETE behaviour)
- A satellite with no recorded orbit yet
- Duplicate NORAD ids (UNIQUE constraint)
- Time zones in timestamp columns
- NULLs in optional columns

STRETCH GOALS (OPTIONAL)
- Add a VIEW for a common report
- Add a trigger (e.g. auto-update a last_modified timestamp)
- Add a composite index and measure the speedup
- Add a many-to-many relationship with a junction table
- Write a migration (schema version 2)""",

"62": """WHAT YOU'RE BUILDING
A secure authentication system for an API: users register, log in, and receive a JWT that protects private routes.

REQUIREMENTS
- Endpoints:
  - POST /register -> create a user (hash the password, never store plaintext)
  - POST /login    -> verify credentials, return a JWT
  - GET  /me       -> protected; returns the current user decoded from the token
- Hash passwords with bcrypt (with a salt)
- Issue JWTs signed with a secret key, containing the user id and an expiry
- Auth middleware: protected routes read the "Authorization: Bearer <token>" header, verify it, and reject if missing, invalid, or expired
- Proper status codes: 401 unauthorized, 403 forbidden, 400 bad input
- Never reveal whether it was the email or the password that was wrong

CONCEPTS TO LEARN
- Password hashing with bcrypt — https://en.wikipedia.org/wiki/Bcrypt
- Salting — https://en.wikipedia.org/wiki/Salt_(cryptography)
- JSON Web Tokens — https://jwt.io/introduction
- Bearer authentication — https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication
- Flask decorators for middleware — https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/

INSTALLATION REQUIRED
  pip install flask flask-bcrypt pyjwt

SECURITY NOTES
- Never store plaintext passwords. Never log them.
- Keep the JWT secret out of source code (use an environment variable).
- Use HTTPS in production — tokens in transit must be encrypted.
- Keep token lifetimes short.

EXAMPLE INTERACTION
  POST /login {"email": "...", "password": "..."}
  -> {"token": "eyJhbGc..."}
  GET /me   Authorization: Bearer eyJhbGc...
  -> {"id": 1, "email": "..."}

EDGE CASES TO HANDLE
- Registering with an email that already exists
- Login with a wrong password or an unknown email
- An expired token
- A malformed or tampered token
- A missing Authorization header
- A weak password at registration (enforce a policy)

STRETCH GOALS (OPTIONAL)
- Refresh tokens with an access/refresh split
- Token revocation (a blocklist or a token version field)
- Roles and permissions (admin vs user)
- An email-verification flow
- Account lockout after repeated failed logins""",

"63": """WHAT YOU'RE BUILDING
A real-time chat server using WebSockets — the curriculum twist is a mission control chat with a live telemetry feed.

REQUIREMENTS
- Use Flask-SocketIO (or plain websockets)
- Clients connect, join named rooms, and send messages
- Broadcast each message to everyone in the same room
- Events: connect, disconnect, join_room, leave_room, send_message
- Show "user joined" and "user left" notifications
- Keep recent message history per room (in memory or a database) and send it to a user when they join
- Track and broadcast the list of online users per room
- A simple test client (an HTML page) to exercise it

CONCEPTS TO LEARN
- WebSockets — https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
- Flask-SocketIO — https://flask-socketio.readthedocs.io/
- Rooms and namespaces — https://flask-socketio.readthedocs.io/en/latest/getting_started.html
- Event-driven programming — https://en.wikipedia.org/wiki/Event-driven_programming
- The publish/subscribe pattern — https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern

INSTALLATION REQUIRED
  pip install flask flask-socketio

EXAMPLE FLOW
  Client A joins room "mission-control" -> sees the history
  Client B joins                       -> both see "B joined"
  A sends "Telemetry nominal"           -> B receives it instantly
  A telemetry generator emits a reading every 2s -> all clients see it

EDGE CASES TO HANDLE
- A client disconnects abruptly (clean up their presence)
- Sending a message to a room with no one in it
- Empty or very long messages
- The same user open in multiple tabs
- Reconnecting after a dropped connection

STRETCH GOALS (OPTIONAL)
- A live telemetry feed: the server pushes simulated satellite data into the room
- Typing indicators ("X is typing...")
- Message persistence in a database
- Private one-to-one messaging
- Basic auth so only named users can join""",

"64": """WHAT YOU'RE BUILDING
A background task system: slow jobs are pushed to a queue and processed by workers instead of blocking the web request — the curriculum twist is scheduling periodic orbital propagation jobs.

REQUIREMENTS
- Use Celery with Redis as the broker (or RQ, which is simpler)
- A Flask API that accepts a job and returns immediately with a job id
- A worker process that picks up jobs and runs them
- At least 3 task types, e.g. a slow computation, sending a (fake) email, generating a report
- An endpoint to check a job's status (pending / running / done / failed) and get its result
- Retry logic: a failed task retries a few times with backoff
- A periodic/scheduled task (Celery beat) — e.g. recompute orbits every N minutes

CONCEPTS TO LEARN
- Why background jobs — https://realpython.com/asynchronous-tasks-with-django-and-celery/
- Celery — https://docs.celeryq.dev/en/stable/getting-started/introduction.html
- Redis as a broker — https://redis.io/docs/latest/
- Task retries and backoff — https://docs.celeryq.dev/en/stable/userguide/tasks.html
- Periodic tasks (Celery beat) — https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html

INSTALLATION REQUIRED
  pip install celery redis flask
  (and a running Redis server)

EXAMPLE FLOW
  POST /jobs/report -> {"job_id": "abc123", "status": "pending"}
  ... a worker runs it ...
  GET /jobs/abc123  -> {"status": "done", "result": {...}}

EDGE CASES TO HANDLE
- The worker is not running (jobs pile up — detect and warn)
- A task that throws an exception (mark it failed, capture the error)
- Checking the status of an unknown job id
- The Redis connection is lost
- A task that runs longer than expected (set time limits)
- Duplicate job submissions

STRETCH GOALS (OPTIONAL)
- A dashboard (Flower) to watch the queue
- Task priorities (an urgent queue and a normal queue)
- Chained tasks (the output of one feeds the next)
- Progress reporting from inside a long task
- Schedule periodic orbital propagation and store the results""",

"65": """WHAT YOU'RE BUILDING
Your first React app — a dashboard built from components and state — the curriculum twist is a science instrument readout dashboard.

REQUIREMENTS
- Set up a React project (Vite is recommended)
- Break the UI into components: Dashboard, Header, Card, ReadoutPanel, etc.
- Use useState to hold state (e.g. the selected instrument, its values)
- Use useEffect for side effects (a timer that updates readings, or a fetch on mount)
- Pass data down via props
- Lift state up so sibling components can share it
- Render lists with .map() and proper keys
- Conditional rendering (a loading state, an empty state)
- At least one interactive control (button, slider, or select) that changes state

CONCEPTS TO LEARN
- React components and JSX — https://react.dev/learn/your-first-component
- useState — https://react.dev/reference/react/useState
- useEffect — https://react.dev/reference/react/useEffect
- Props — https://react.dev/learn/passing-props-to-a-component
- Lifting state up — https://react.dev/learn/sharing-state-between-components
- Rendering lists and keys — https://react.dev/learn/rendering-lists

INSTALLATION REQUIRED
  npm create vite@latest my-dashboard -- --template react

COMPONENT SKETCH
  <Dashboard>
    <Header />
    <InstrumentSelect />      // changes shared state
    <ReadoutPanel>
      <Card /> <Card /> ...    // one per reading
    </ReadoutPanel>
  </Dashboard>

EDGE CASES TO HANDLE
- Empty data (no instrument selected yet)
- A useEffect timer MUST be cleaned up on unmount (return a cleanup function)
- Missing keys in a mapped list (React will warn)
- State updates that depend on previous state (use the updater function form)
- A loading state before data arrives

STRETCH GOALS (OPTIONAL)
- A custom hook (e.g. useInterval or useInstrumentData)
- useReducer instead of several useState calls
- Persist the selected instrument to localStorage
- A dark/light theme with useContext
- Animated value changes""",

"66": """WHAT YOU'RE BUILDING
A data dashboard in React that fetches real data and visualizes it with charts — the curriculum twist is visualizing SpaceX launch statistics.

REQUIREMENTS
- Fetch real data from a public API (the SpaceX API is free and needs no key)
- Display it with charts using a library (Recharts is the curriculum's pick)
- At least 3 chart types, e.g. a line chart, a bar chart, a pie/donut chart
- Summary stat cards (total launches, success rate, etc.)
- A data table with the underlying records
- Filters that update all charts together (e.g. by year or by rocket)
- Loading and error states
- A responsive layout that works on mobile

CONCEPTS TO LEARN
- Data fetching in React (useEffect + fetch) — https://react.dev/learn/synchronizing-with-effects
- Recharts — https://recharts.org/en-US/guide
- Derived state (compute, don't store) — https://react.dev/learn/you-might-not-need-an-effect
- Responsive CSS grid layouts — https://css-tricks.com/snippets/css/complete-guide-grid/
- The SpaceX API — https://github.com/r-spacex/SpaceX-API

INSTALLATION REQUIRED
  npm create vite@latest -- --template react
  npm install recharts

DASHBOARD SECTIONS
  Stat cards  -> total launches, successes, failures, success rate
  Line chart  -> launches per year
  Bar chart   -> launches per rocket
  Pie chart   -> success vs failure
  Table       -> recent launches with details

EDGE CASES TO HANDLE
- The API is slow or down (loading and error states)
- An empty filtered result (charts must not crash on empty data)
- Very large datasets (aggregate before charting)
- Missing fields in some records
- Charts resizing on window resize and on mobile

STRETCH GOALS (OPTIONAL)
- A date-range filter
- Click a chart segment to drill down
- Export the current view as PNG or CSV
- Compare two rockets side by side
- A live "next launch" countdown""",

"67": """WHAT YOU'RE BUILDING
A complete full-stack application: a React front-end talking to your own Flask API, with authentication — the curriculum twist is a personal science notebook with images and equations.

REQUIREMENTS
- Backend: a Flask API (reuse what you built in projects 60 and 62) — CRUD plus JWT auth
- Frontend: a React app that consumes the API
- Auth flow: register and login screens, store the JWT, attach it to requests
- Protected routes in React (redirect to login if not authenticated)
- Use axios (or fetch) for API calls
- Handle CORS correctly between the two origins
- Full CRUD from the UI: create, list, edit, delete notebook entries
- Loading, error, and empty states throughout
- A logout that clears the token

CONCEPTS TO LEARN
- Client-server architecture — https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview
- axios — https://axios-http.com/docs/intro
- CORS — https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
- React Router and protected routes — https://reactrouter.com/en/main/start/tutorial
- React Context for auth state — https://react.dev/learn/passing-data-deeply-with-context

INSTALLATION REQUIRED
  Backend:  pip install flask flask-sqlalchemy flask-bcrypt pyjwt flask-cors
  Frontend: npm create vite@latest -- --template react ; npm install axios react-router-dom

ARCHITECTURE
  React (localhost:5173)  --HTTP + JWT-->  Flask API (localhost:5000)  -->  SQLite DB

EDGE CASES TO HANDLE
- The token expires mid-session (catch the 401, redirect to login)
- A CORS misconfiguration (a very common first bug)
- Refreshing the page — the user should stay logged in
- The API is down — the UI should fail gracefully
- A protected route accessed directly by its URL
- Form validation on both the client and the server

STRETCH GOALS (OPTIONAL)
- Image upload for notebook entries
- LaTeX equation rendering with KaTeX
- Search and tags
- Optimistic UI updates
- Deploy both halves (frontend on Netlify, backend on a host) and connect them""",

"68": """WHAT YOU'RE BUILDING
A scientific web app built rapidly in pure Python with Streamlit — the curriculum twist is an interactive orbit explorer.

REQUIREMENTS
- Build a Streamlit app (no HTML or JS — all Python)
- Interactive widgets: sliders, number inputs, select boxes, buttons
- The app computes something from the inputs and shows the result live
- For the orbit explorer: sliders for semi-major axis, eccentricity, inclination; plot the resulting orbit
- At least 2 plots (Matplotlib or Plotly) that update with the inputs
- Display computed values (period, apogee, perigee) in metric widgets
- Use st.cache_data to cache expensive computations
- Organise the layout with columns, tabs, or a sidebar

CONCEPTS TO LEARN
- Streamlit basics — https://docs.streamlit.io/get-started
- Streamlit widgets — https://docs.streamlit.io/library/api-reference/widgets
- Caching — https://docs.streamlit.io/library/advanced-features/caching
- Layout: columns, sidebar, tabs — https://docs.streamlit.io/library/api-reference/layout
- Plotly in Streamlit — https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart

INSTALLATION REQUIRED
  pip install streamlit matplotlib plotly numpy
  Run with:  streamlit run app.py

EXAMPLE LAYOUT
  Sidebar -> sliders for a, e, i
  Main    -> tab 1: a 2D orbit plot + metrics (period, apogee, perigee)
             tab 2: a 3D orbit plot

EDGE CASES TO HANDLE
- An eccentricity of exactly 1 (parabolic — handle it or restrict the slider)
- The whole script re-runs on every interaction — keep heavy work cached
- Invalid input combinations
- Very fine slider steps causing lag
- Empty or degenerate orbits

STRETCH GOALS (OPTIONAL)
- Upload a CSV of real orbital elements and visualise them
- Animate the orbit over time
- Compare two orbits on the same plot
- A download button for the generated plot or data
- Deploy free on Streamlit Community Cloud""",

"69": """WHAT YOU'RE BUILDING
A web client that receives a live data stream over WebSockets and displays it on continuously updating charts — the curriculum twist is streaming simulated satellite telemetry to a dashboard.

REQUIREMENTS
- A server that emits telemetry readings on a WebSocket several times per second (reuse the chat backend from project 63, or a small Flask-SocketIO server)
- A front-end that connects with socket.io-client and listens for the stream
- Live-updating charts: values scroll across the screen as new data arrives
- Display at least 4 telemetry channels (e.g. altitude, velocity, battery, temperature)
- Current-value readouts alongside the charts
- A connection status indicator (connected / reconnecting / disconnected)
- Keep only a rolling window of recent points (don't grow memory forever)
- Pause and resume the stream

CONCEPTS TO LEARN
- WebSocket clients — https://developer.mozilla.org/en-US/docs/Web/API/WebSocket
- socket.io-client — https://socket.io/docs/v4/client-api/
- Live/streaming charts — https://www.chartjs.org/docs/latest/
- Rolling buffers / circular buffers — https://en.wikipedia.org/wiki/Circular_buffer
- requestAnimationFrame for smooth updates — https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame

INSTALLATION REQUIRED
  Server:  pip install flask flask-socketio   (or Node + socket.io)
  Client:  the socket.io-client library

EXAMPLE FLOW
  The server emits {altitude, velocity, battery, temp} every 200ms
  The client charts scroll left as new points arrive
  Disconnect the server -> the status shows "reconnecting..."

EDGE CASES TO HANDLE
- The connection drops — show the status and auto-reconnect
- Data arriving faster than the screen can render (throttle the redraw)
- Memory growth (cap the buffer length)
- Out-of-order or missing readings
- The tab being backgrounded (browsers throttle timers)

STRETCH GOALS (OPTIONAL)
- Threshold alerts (highlight a channel in red when out of range)
- Record the session and replay it
- An adjustable time window
- Export the buffered data as CSV
- Multiple satellites on one dashboard""",

"70": """WHAT YOU'RE BUILDING
An app that logs users in with their GitHub account using the OAuth 2.0 flow, then uses the GitHub API on their behalf — the curriculum twist is auto-publishing your space simulations to GitHub Pages.

REQUIREMENTS
- Register an OAuth App on GitHub (get a client id and a client secret)
- Implement the OAuth 2.0 authorization code flow:
  1. Redirect the user to GitHub to authorize
  2. GitHub redirects back to your app with a code
  3. Your backend exchanges the code for an access token
  4. Store the token server-side (never expose the client secret to the browser)
- Use the token to call the GitHub API: fetch the user's profile and repositories
- Display the logged-in user (avatar, name, repo list)
- A logout that clears the session
- Handle the user denying access

CONCEPTS TO LEARN
- The OAuth 2.0 authorization code flow — https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps
- Why the secret stays on the server — https://oauth.net/2/
- The GitHub REST API — https://docs.github.com/en/rest
- Sessions and cookies — https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
- The state parameter (CSRF protection) — https://auth0.com/docs/secure/attack-protection/state-parameters

INSTALLATION REQUIRED
  pip install flask requests   (the backend handles the token exchange)

SECURITY NOTES
- The client secret must NEVER reach the browser — keep it on the backend.
- Always send and verify the "state" parameter to prevent CSRF.
- Store tokens securely; treat them like passwords.

EXAMPLE FLOW
  The user clicks "Login with GitHub"
  -> redirected to github.com/login/oauth/authorize
  -> approves, redirected back to /callback?code=...&state=...
  -> the backend swaps the code for a token
  -> the app shows the user's profile and repos

EDGE CASES TO HANDLE
- The user denies authorization
- The state parameter doesn't match (possible CSRF — reject the request)
- The code is expired or already used
- The access token is revoked by the user
- GitHub API rate limits
- A network failure during the token exchange

STRETCH GOALS (OPTIONAL)
- Create a repository from the app
- Push a project and enable GitHub Pages via the API
- Show the user's contribution stats
- Support other providers (Google, GitLab)
- Refresh-token handling where the provider supports it"""
}


# ============================================================
#  PATCHER  —  injects the web-dev specs (projects 51-70) into
#  your "300-Project Master Curriculum" HTML file.
#
#  USAGE:
#     python add_web_specs.py  your_curriculum.html
#  or just (auto-finds a single .html in the folder):
#     python add_web_specs.py
#
#  It writes a NEW file ("<name>_updated.html") and never
#  touches or overwrites your original.
# ============================================================
import json, os, sys


def find_html_file():
    if len(sys.argv) > 1:
        return sys.argv[1]
    here = [f for f in os.listdir('.') if f.lower().endswith('.html')]
    if len(here) == 1:
        return here[0]
    if not here:
        sys.exit("No .html file found. Run:  python add_web_specs.py your_file.html")
    sys.exit("Several .html files found. Run:  python add_web_specs.py "
             + here[0] + "   (pick yours)")


def main():
    path = find_html_file()
    if not os.path.exists(path):
        sys.exit("File not found: " + path)

    with open(path, encoding='utf-8') as f:
        html = f.read()

    marker = 'const PROJECT_DETAILS = '
    if marker not in html:
        sys.exit("Could not find PROJECT_DETAILS in that file — is it the right HTML?")

    start = html.index(marker) + len(marker)
    end = html.index('const PHASES', start)          # PROJECT_DETAILS sits just before PHASES

    literal = html[start:end].rstrip()                # "{...};"
    if not literal.endswith(';'):
        sys.exit("Unexpected file format near PROJECT_DETAILS.")
    literal = literal[:-1].rstrip()                   # drop the trailing ;

    try:
        details = json.loads(literal)
    except json.JSONDecodeError as e:
        sys.exit("Could not parse PROJECT_DETAILS as JSON: " + str(e))

    before = sum(1 for k in NEW_SPECS
                 if details.get(k, '').startswith('Detailed spec will be provided'))
    for key, spec in NEW_SPECS.items():
        details[key] = spec

    new_literal = json.dumps(details, ensure_ascii=False)
    new_html = html[:start] + new_literal + ';\n\n' + html[end:]

    base, ext = os.path.splitext(path)
    out = base + '_updated' + ext
    with open(out, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print("Done.")
    print("  Updated projects : 51-70 (Phase 2 - Web & Data)")
    print("  Placeholders replaced with full specs: %d" % before)
    print("  Total projects in file: %d" % len(details))
    print("  Written to: %s" % out)
    print("Open that file in your browser - click 'Full Spec' on any web project.")


if __name__ == "__main__":
    main()