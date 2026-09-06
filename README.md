# <p align="center">🔮 BCA ATTENDANCE SYSTEM 🔮</p>

<p align="center">
  <img src="https://githubusercontent.com" width="45" alt="Python" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://githubusercontent.com" width="45" alt="SQLite" />
</p>

<p align="center">
  <strong>An elegant, dark-cyber themed desktop portal designed for seamless classroom management.</strong>
</p>

<p align="center">
  <img src="https://shields.io" alt="Python Version" />
  <img src="https://shields.io" alt="GUI Framework" />
  <img src="https://shields.io" alt="Database" />
  <img src="https://shields.io" alt="License" />
</p>

---

## 🎨 Visual Identity

The interface is structurally generated around a high-contrast dark environment with premium accent states:

```ini
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█   ⚡ BACKGROUND: #12121c     ⚡ PRIMARY ACCENT:  #5b6cf9 (BLUE)     █
█   ⚡ PANEL BG:   #1c1c28     ⚡ SECONDARY BG:    #d946ef (PINK)     █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
```

---

## ✨ Features

*   **Computational Visual Gradients:** Generates an algorithmic dual-color backdrop on runtime memory buffers through structural **Pillow (PIL)** pixel processing.
*   **Dynamic Component Layering:** Implements an atomic `clear_frame()` pipeline layer to recycle interface screens instantly without spawning multi-window pollution.
*   **Relational Database Mapping:** Managed through safe local **SQLite3** schemas complete with input fields protection (`Unique` key filters).
*   **Input Cleansing Engine:** Built-in form validators instantly capture missing records or duplicate student identifiers (`IntegrityError`).

---

## 🛠️ System Architecture

| Component | Technical Stack | Layer Operations |
| :--- | :--- | :--- |
| **Language Core** | Python 3.x | Algorithmic logic processing |
| **Window Host** | Tkinter Toolset | Graphical window, widgets, and form bindings |
| **Graphics Node** | Pillow Imaging Engine | High-performance canvas matrix gradient processing |
| **Data Engine** | SQLite3 Instance | Local relation-mapped binary file storage |

---

## 🗃️ Database Layout Configuration

Upon activation, the runtime thread builds an internal `bca_attendance.db` layout configuration holding two relational maps:

### 1. `students` (Registration Records)
*   `id`: `INTEGER` — Primary Identification (Auto-increment)
*   `name`: `TEXT` — Student Identity Name (`NOT NULL`)
*   `email`: `TEXT` — Account Email ID (`UNIQUE`, `NOT NULL`)
*   `password`: `TEXT` — Authentication Secret String (`NOT NULL`)
*   `roll_no`: `TEXT` — Academic Registration Number (`UNIQUE`)

### 2. `attendance` (Tracking Matrix)
*   `id`: `INTEGER` — Sheet Row Pointer (Primary Key)
*   `student_id`: `INTEGER` — Relational reference key map targeting `students(id)`
*   `date`: `TEXT` — Log timestamp entry
*   `status`: `TEXT` — Attendance state indicator 

---

## 🚀 Running the Core Locally

### 1. Environment Requirements
Ensure Python is fully operational on your engine terminal. Next, bind the missing image compiler using pip:
```bash
pip install Pillow
```

### 2. File Assembly
Pull the environment down to your workspace tree layer:
```bash
# Clone the repository files
git clone https://github.com

# Step into the host directory
cd attendbca
```

### 3. Execution
Launch the primary initialization stream directly from the compiler:
```bash
python attendbca.py
```

---

## 📝 License
Distributed under the terms of the open-source **MIT License**. See `LICENSE` for structural parameters.
