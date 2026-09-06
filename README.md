# 📊 BCA Attendance System

[![Python Version](https://shields.io)](https://python.org)
[![GUI Framework](https://shields.io)](https://python.org)
[![Database](https://shields.io)](https://sqlite.org)
[![License: MIT](https://shields.io)](https://opensource.org)

A modern, visually appealing desktop application featuring a dark-cyber UI theme designed for managing student registration and attendance tracking. Built entirely with **Python (Tkinter)** and **SQLite3**, it implements dynamic frame buffering and programmatic UI gradients using the **Pillow** library.

---

## 🔥 Key Features

*   **Modern Cyber Dark Theme:** Uses a polished, responsive custom color scheme (`#12121c`) optimized for desktop displays.
*   **Programmatic Background Gradients:** Implements a fast pixel-mapping utility powered by Pillow (`PIL`) to generate sleek runtime visual backdrops.
*   **Robust Database Architecture:** Leveraging SQLite3 with full constraints (`UNIQUE`, `NOT NULL`) ensuring relational integrity.
*   **Dynamic Component Lifecycle:** Uses a unified frame recycling pattern (`clear_frame`) to transition screens seamlessly inside a single monolithic window environment.
*   **Data Validation:** Features thorough form-validation and centralized error-handling alerts for database duplicate entries (`IntegrityError`).

---

## 🛠️ Architecture & Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core programming language |
| **GUI Framework** | Tkinter | Window controls and widget rendering |
| **Database** | SQLite3 | Locally embedded relational storage engine |
| **Graphics Processing** | Pillow (PIL) | Runtime computational background rendering |

---

## 📋 Database Schema Design

The application automatically provisions an internal local database named `bca_attendance.db` upon initial execution with the following structural layout:

### `students` Table
Keeps record of registered student credentials.
*   `id`: `INTEGER` (Primary Key, Autoincrement)
*   `name`: `TEXT` (Not Null)
*   `email`: `TEXT` (Unique, Not Null)
*   `password`: `TEXT` (Not Null)
*   `roll_no`: `TEXT` (Unique)

### `attendance` Table
Tracks daily login and state statuses.
*   `id`: `INTEGER` (Primary Key, Autoincrement)
*   `student_id`: `INTEGER` (Foreign Key referencing `students(id)`)
*   `date`: `TEXT` 
*   `status`: `TEXT`

---

## 🚀 Installation & Running Locally

### 1. Prerequisites
Ensure you have Python installed. Next, install the image processing layer (**Pillow**) via pip:
```bash
pip install Pillow
```

### 2. Setup the Repository
Clone the project structure down to your working directory:
```bash
# Clone the repository
git clone https://github.com

# Navigate into the project folder
cd attendbca
```

### 3. Launch Application
Kickstart the Tkinter mainloop process:
```bash
python attendbca.py
```

---

## 📅 Roadmap / Future Enhancements
- [ ] Add a secure functional Student Login verification view.
- [ ] Implement an interactive Dashboard displaying individual attendance percentages.
- [ ] Export internal database metrics directly into `.xlsx` or `.csv` spreadsheets.
- [ ] Develop an Administrator Portal overview for bulk-marking class sheets.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
