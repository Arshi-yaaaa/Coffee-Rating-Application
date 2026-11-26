# ☕ Coffee Rating Application

### A Python Flask and SQLite-Based Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Styling-blue?logo=css3)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 1. Project Overview

The **Coffee Rating Application** is a web-based application developed using Python Flask, HTML, CSS, and SQLite.

The application allows users to explore a collection of coffee items and vote for their favourite coffee using an interactive voting button.

Whenever a user clicks the voting button, the corresponding coffee's vote count increases automatically. The updated vote count is stored in an SQLite database, ensuring that the voting information remains available even after refreshing the webpage or restarting the application.

This project demonstrates the practical implementation of backend development, database connectivity, HTTP request handling, and interactive frontend design.

## 🎯 2. Project Objective

The main objective of this project is to develop a simple and interactive coffee rating system that allows users to vote for different coffee varieties.

The project focuses on:

- Developing a web application using Python Flask.
- Displaying a collection of coffee items.
- Implementing interactive voting functionality.
- Handling user interactions through HTTP POST requests.
- Connecting a Flask application with an SQLite database.
- Storing and updating vote counts.
- Retrieving database information dynamically.
- Designing an attractive and user-friendly interface.

## ✨ 3. Key Features

### 1. Coffee Listing
The application displays different coffee varieties with their names, descriptions, and visual icons.

### 2. Interactive Voting System
Users can vote for their favourite coffee by clicking the plus (+) button.

### 3. Automatic Vote Count Update
Every successful vote increases the corresponding coffee's vote count by one.

### 4. Database Integration
SQLite is used to store coffee information and voting records.

### 5. Persistent Vote Storage
Vote counts remain saved in the database even after refreshing the browser.

### 6. Total Vote Counter
The application displays the combined number of votes received by all coffee items.

### 7. Dynamic Content Rendering
Flask and Jinja2 are used to retrieve and display coffee information dynamically.

### 8. User Feedback
The application displays success messages after a vote is recorded and error messages if an invalid coffee item is requested.

### 9. Responsive User Interface
The application uses CSS Grid and responsive styling to adapt to different screen sizes.

## 🛠️ 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| SQLite | Database management |
| HTML5 | Frontend structure |
| CSS3 | Styling and layout |
| Jinja2 | Dynamic HTML rendering |
| HTTP GET | Retrieving coffee information |
| HTTP POST | Submitting votes |
| VS Code | Development environment |
| GitHub | Source code management |

## 📂 5. Project Folder Structure

```text
Coffee-Rating-Application/
│
├── app.py
│
├── requirements.txt
│
├── coffee_votes.db
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

**Note:** The `coffee_votes.db` database file is automatically generated when the application is first executed.

### File Description

**app.py**
- Contains the main Flask application.
- Defines the application routes.
- Initializes the SQLite database.
- Creates the coffee table.
- Inserts the initial coffee items.
- Retrieves coffee details and vote counts.
- Handles voting requests.
- Updates the database whenever a user votes.

**requirements.txt**
- Contains the Python dependencies required for the application.
- Specifies Flask as the required web framework.

**coffee_votes.db**
- SQLite database used to store coffee information.
- Contains coffee names, descriptions, icons, and vote counts.
- Automatically maintains updated voting information.

**templates/index.html**
- Contains the frontend HTML structure.
- Displays the coffee menu.
- Provides voting buttons.
- Displays individual vote counts and total votes.
- Uses Jinja2 template expressions to display database information.

**static/style.css**
- Defines the application's visual appearance.
- Styles the background, coffee cards, buttons, and typography.
- Implements hover effects.
- Provides responsive layouts.

## ⚙️ 6. System Requirements

The following tools and software are required:

- Python 3.x
- Visual Studio Code
- Flask framework
- SQLite database
- Google Chrome or another modern web browser
- Internet connection for installing dependencies

## 🚀 7. Installation and Setup

Follow these steps to execute the project locally.

### Step 1: Download the Project

Download or clone the project repository from GitHub.

```bash
git clone https://github.com/Arshi-yaaaa/Coffee-Rating-Application.git
```

### Step 2: Open the Project Folder

```bash
cd Coffee-Rating-Application
```

Open the folder using Visual Studio Code.

### Step 3: Install Dependencies

Open the VS Code terminal and execute:

```bash
py -m pip install -r requirements.txt
```

This installs the Flask framework required to run the application.

### Step 4: Run the Application

Execute the following command:

```bash
py app.py
```

The Flask development server will start.

### Step 5: Open the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

The Coffee Rating Application will now be displayed.

## 🔄 8. Application Workflow

The application follows a simple frontend-backend-database workflow.

1. The user opens the Coffee Rating Application.
2. Flask retrieves coffee information from the SQLite database.
3. The retrieved coffee details and vote counts are passed to the HTML template.
4. The webpage displays the available coffee items.
5. The user selects a favourite coffee.
6. The user clicks the plus (+) voting button.
7. The browser sends an HTTP POST request to the Flask backend.
8. Flask identifies the selected coffee using its unique ID.
9. The SQLite database updates the corresponding vote count.
10. The application redirects the user to the main page.
11. The updated vote count is retrieved from the database and displayed.

## 🧠 9. Backend Implementation

The backend is developed using Python Flask.

### Flask Application
Flask is used to create and manage the web application.

### Routing
The application contains two main routes:

**Home Route (`/`)**
- Handles GET requests.
- Retrieves coffee details from the database.
- Calculates the total number of votes.
- Displays the coffee menu.

**Voting Route (`/vote/<coffee_id>`)**
- Handles POST requests.
- Identifies the selected coffee.
- Updates the corresponding vote count.
- Redirects the user to the homepage.

### Database Connection
SQLite is connected using Python's built-in `sqlite3` module.

### Database Initialization
The application creates a coffee table if it does not already exist.

The table contains:
- ID
- Coffee Name
- Description
- Icon
- Vote Count

### Vote Processing
Whenever a user clicks the voting button, the backend executes an SQL UPDATE statement to increase the selected coffee's vote count.

## 🗄️ 10. Database Implementation

SQLite is used as the database management system.

The database is automatically created using Python's SQLite module.

### Database Table: coffees

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Unique coffee identifier |
| name | TEXT | Coffee name |
| description | TEXT | Coffee description |
| icon | TEXT | Coffee visual icon |
| votes | INTEGER | Number of votes |

### SQL Operations Used

**CREATE TABLE**

Creates the coffee table if it does not already exist.

**INSERT OR IGNORE**

Inserts the initial coffee items without creating duplicate entries when the application restarts.

**SELECT**

Retrieves coffee details and vote counts.

**UPDATE**

Increases the vote count whenever a user votes.

### Vote Count Update Logic

```sql
UPDATE coffees
SET votes = votes + 1
WHERE id = ?;
```

This query updates only the selected coffee item's vote count.

## 🎨 11. Frontend Implementation

The frontend is developed using HTML5 and CSS3.

### HTML Components
- Application heading.
- Coffee menu section.
- Coffee name and description.
- Voting buttons.
- Individual vote counters.
- Total vote counter.
- Success and error messages.

### CSS Components
- Coffee-themed background.
- Dark brown gradient header.
- Individual coffee cards.
- Rounded card layouts.
- Interactive voting buttons.
- Hover animations.
- Responsive grid layout.
- Typography and spacing.

## 🧪 12. Testing and Verification

The application was tested to verify its main functionalities.

| Test Case | Expected Result |
|---|---|
| Open the application | Coffee menu displayed |
| Click a coffee voting button | Vote count increases |
| Vote for different coffees | Corresponding counts update |
| Refresh the webpage | Previous vote counts remain |
| Restart the application | Database information remains available |
| Check total votes | Displays the combined vote count |
| Submit an invalid coffee ID | Error feedback is displayed |

## 📸 13. Application Output

The application successfully displays a collection of coffee varieties with their descriptions and voting options.

Users can interact with the voting buttons to select their favourite coffee.

The application dynamically updates and displays individual vote counts and the total number of votes.

All voting information is stored in the SQLite database.

## 🔐 14. Error Handling and Data Management

Basic error handling and database management techniques are implemented.

- Invalid coffee IDs are handled without updating unrelated records.
- SQL queries use parameterized values.
- Duplicate initial coffee records are avoided using `INSERT OR IGNORE`.
- Database connections are managed using Python context managers.
- User feedback is displayed after voting.
- Existing vote counts are preserved in the database.

## 📚 15. Learning Outcomes

Through this project, I gained practical experience in:

- Developing web applications using Python Flask.
- Understanding HTTP GET and POST requests.
- Implementing interactive voting functionality.
- Connecting Python applications with SQLite.
- Creating and managing database tables.
- Performing SQL INSERT, SELECT, and UPDATE operations.
- Handling database records dynamically.
- Working with Jinja2 templates.
- Integrating frontend and backend components.
- Designing responsive web interfaces using CSS.
- Implementing persistent data storage.
- Organizing project files and managing source code using GitHub.

## 🔮 16. Future Enhancements

The application can be further improved by introducing:

- User registration and login.
- One-vote-per-user restrictions.
- Coffee rating using a five-star system.
- Coffee images and detailed descriptions.
- Graphical voting statistics.
- Displaying the most popular coffee.
- Admin dashboard for managing coffee items.
- Ability to add and remove coffee varieties.
- Database backup and export functionality.

## 🏁 17. Conclusion

The Coffee Rating Application successfully demonstrates the integration of Python Flask, SQLite, HTML, and CSS to develop an interactive web-based voting system.

The application allows users to explore different coffee varieties, vote for their favourites, and view updated voting results.

By implementing database connectivity and backend request handling, this project provides practical experience in full-stack web application development and database management.

## 👩‍💻 18. Developer Information

**Developed by:** Arshiya Thaslim K

**Domain:** Python Full Stack Development

**Project:** Coffee Rating Application

**Internship Organization:** VirtualWorks

**Project Number:** Task 3

**Task ID:** task3

**GitHub Repository:**  
https://github.com/Arshi-yaaaa/Coffee-Rating-Application

---
