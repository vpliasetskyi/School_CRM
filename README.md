# School Management System — Functionality Guide

---

## $${\color{green}Student \space Class}$$

Represents a single student with an ID, name, and grade level.

- `__init__` — creates the student object
- `display_info()` — prints ID, name, grade level
- `__str__()` — returns a readable string when printed

$${\color{blue}Screenshot \space — \space Student \space output}$$

&nbsp;

&nbsp;

&nbsp;

---

## $${\color{green}Class \space Class}$$

Represents a school course. Manages its own list of enrolled students.

- `__init__` — creates the class with ID, name, teacher, and empty student list
- `add_student(student)` — enrolls a student; warns if already enrolled
- `remove_student(student)` — removes a student; warns if not found
- `list_students()` — prints all enrolled students

$${\color{blue}Screenshot \space — \space Class \space enrollment \space output}$$

&nbsp;

&nbsp;

&nbsp;

---

## $${\color{green}Grade \space Class}$$

Links a student to a class with a numeric score and converts it to a letter grade.

- `__init__` — creates the grade record with student, class, and score
- `get_letter_grade()` — converts score to A / B / C / D / F
- `display_grade()` — prints the full grade record

| Score | Letter |
|-------|--------|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | F |

$${\color{blue}Screenshot \space — \space Grade \space output}$$

&nbsp;

&nbsp;

&nbsp;

---

## $${\color{green}School \space Class}$$

Central manager that coordinates all students, classes, and grades.

**Student management**
- `add_student()` — creates and stores a student; rejects duplicate IDs
- `find_student()` — returns a student by ID
- `list_all_students()` — prints every student in the school

**Class management**
- `add_class()` — creates and stores a class; rejects duplicate IDs
- `find_class()` — returns a class by ID
- `list_all_classes()` — prints every class with teacher and enrollment count

**Enrollment**
- `enroll_student_in_class()` — looks up student and class by ID then enrolls them

**Grades**
- `add_grade()` — creates a grade after verifying the student is enrolled
- `list_grades_for_student()` — prints all grades for a student
- `list_grades_for_class()` — prints all grades for a class
- `calculate_student_average()` — calculates and prints a student's average score

$${\color{blue}Screenshot \space — \space List \space all \space students}$$

&nbsp;

&nbsp;

&nbsp;

$${\color{blue}Screenshot \space — \space List \space all \space classes}$$

&nbsp;

&nbsp;

&nbsp;

$${\color{blue}Screenshot \space — \space Grades \space and \space average}$$

&nbsp;

&nbsp;

&nbsp;

---

## $${\color{green}main() \space Function}$$

Entry point. Seeds sample data then runs the interactive menu loop.

**Setup phase** (runs once at startup):
1. Creates the `School` object
2. Adds 5 students, 4 classes
3. Enrolls students and records grades

**Menu loop** — uses `match/case` (Python 3.10+) to route user input:

| Choice | Action |
|--------|--------|
| `1` | List all students |
| `2` | List all classes |
| `3` | Add a new student |
| `4` | Add a new class |
| `5` | Enroll student in class |
| `6` | Add a grade |
| `7` | View student grades |
| `8` | View class grades |
| `9` | Calculate student average |
| `0` | Exit |
| `_` | Invalid input warning |

$${\color{blue}Screenshot \space — \space Startup \space output}$$

&nbsp;

&nbsp;

&nbsp;

$${\color{blue}Screenshot \space — \space Main \space menu}$$

&nbsp;

&nbsp;

&nbsp;

$${\color{blue}Screenshot \space — \space Menu \space option \space in \space action}$$

&nbsp;

&nbsp;

&nbsp;