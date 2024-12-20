# To-Do List Application

This is a **To-Do List Application** built using Python and Tkinter. The app provides an intuitive graphical user interface (GUI) to manage daily tasks efficiently. It uses **file handling** for data persistence, ensuring tasks are saved even after the application is closed.

---

## Features

### 1. **Add Tasks**
- Input new tasks through an entry field and add them to the list with a single click.

### 2. **Delete Tasks**
- Select a task from the list and delete it using the `Delete Task` button.

### 3. **Clear All Tasks**
- Quickly clear the entire task list with the `Clear All` button. A confirmation prompt ensures accidental deletions are avoided.

### 4. **Persistent Storage**
- Tasks are saved in a file (`tasks.txt`) so that they persist across sessions.

### 5. **Scrollable List**
- Integrated scrollbar allows for easy navigation of long task lists.

### 6. **Modern and Clean Design**
- Styled with a minimalistic and user-friendly interface.

---

## Prerequisites

### Required Libraries
Ensure the following Python libraries are installed:
- `tkinter`
- `messagebox` (part of Tkinter, no separate installation required)

To install Python, visit the [Python website](https://www.python.org/).

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd todo-list-app
   ```

3. Run the application:
   ```bash
   python todo_list_app.py
   ```

---

## File Structure

```
.
|-- todo_list_app.py     # Main Python file for the To-Do List application
|-- tasks.txt            # Storage file for tasks (auto-generated on first run)
|-- README.md            # Documentation file
```

---

## Usage

1. **Add a Task**:
   - Enter the task in the input field.
   - Click `Add Task` to add it to the list.

2. **Delete a Task**:
   - Select a task from the list.
   - Click `Delete Task` to remove it.

3. **Clear All Tasks**:
   - Click `Clear All` to remove all tasks.
   - Confirm the action in the popup prompt.

4. **Persistent Tasks**:
   - The tasks are saved to `tasks.txt` automatically, ensuring they are loaded when the app is reopened.

---

## Customization

You can easily customize the app to meet your needs:

1. **Change Colors and Fonts**:
   - Update the `bg`, `fg`, and `font` attributes in the Tkinter widgets.

2. **Add More Features**:
   - Integrate deadlines or priority levels.
   - Use a database (e.g., SQLite) for storage.

3. **Modify Storage**:
   - Replace file handling with a database for more robust task management.

---

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---


## Acknowledgments

- Built using Python and Tkinter.
- Inspired by simple task management needs for personal use.

---

Happy Task Managing! 😊
