import json
import asyncio
from pathlib import Path
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor

class Task:
    def __init__(self, task_id: int, title: str, description: str, keywords_required: List[str]):
        self.id = task_id
        self.title = title
        self.description = description
        self.keywords_required = keywords_required

    @classmethod
    def load_from_file(cls, path_to_json: Path) -> "Task":
        data = json.loads(path_to_json.read_text(encoding="utf-8"))
        return cls(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            keywords_required=data["keywords_required"]
        )

class Student:
    def __init__(self, student_id: str, name: str, assigned_tasks: Optional[List[int]] = None):
        self.student_id = student_id
        self.name = name
        self.assigned_tasks = assigned_tasks or []
        self.tasks_objects: List[Task] = []

    @classmethod
    def load_from_dict(cls, data: dict) -> "Student":
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            assigned_tasks=data["assigned_tasks"]
        )

    def assign_task_object(self, task: Task) -> None:
        self.tasks_objects.append(task)

class TaskCheckResult:
    def __init__(self, task_id: int, matched_keywords: List[str], missing_keywords: List[str]):
        self.task_id = task_id
        self.matched_keywords = matched_keywords
        self.missing_keywords = missing_keywords

    def to_dict(self) -> Dict:
        return {
            "task_id": self.task_id,
            "matched_keywords": self.matched_keywords,
            "missing_keywords": self.missing_keywords
        }

async def check_task_for_keywords(task: Task) -> TaskCheckResult:
    await asyncio.sleep(0.1)
    description_lower = task.description.lower()
    matched = []
    missing = []
    for kw in task.keywords_required:
        if kw.lower() in description_lower:
            matched.append(kw)
        else:
            missing.append(kw)
    return TaskCheckResult(task_id=task.id, matched_keywords=matched, missing_keywords=missing)

async def check_tasks_for_student(student_name: str, tasks: List[Task]) -> Dict:
    coroutines = [check_task_for_keywords(task) for task in tasks]
    results = await asyncio.gather(*coroutines)
    return {
        "student": student_name,
        "results": [r.to_dict() for r in results]
    }

BASE_DIR = Path(__file__).parent
TASKS_DIR = BASE_DIR / "tasks"
STUDENTS_FILE = BASE_DIR / "students.json"
REPORT_FILE = BASE_DIR / "report.json"

def create_default_jsons():
    TASKS_DIR.mkdir(exist_ok=True)
    if not any(TASKS_DIR.iterdir()):
        default_tasks = [
            {
                "id": 1,
                "title": "Аналіз даних з CSV",
                "description": "Написати скрипт, який читає CSV-файл із даними про екологічні показники та обчислює основу статистику (середнє, медіану).",
                "keywords_required": ["csv", "pandas", "statistics"]
            },
            {
                "id": 2,
                "title": "Побудова графіку",
                "description": "Створити програму, яка будує лінійний графік зміни концентрації CO₂ за даними JSON-вхідного файлу.",
                "keywords_required": ["matplotlib", "json", "plot"]
            },
            {
                "id": 3,
                "title": "Асинхронний запит API",
                "description": "Реалізувати асинхронний запит до публічного екологічного API та обробити отримані дані.",
                "keywords_required": ["asyncio", "aiohttp", "json"]
            }
        ]
        for task in default_tasks:
            path = TASKS_DIR / f"task{task['id']}.json"
            path.write_text(json.dumps(task, ensure_ascii=False, indent=4), encoding="utf-8")
    if not STUDENTS_FILE.exists():
        STUDENTS_FILE.write_text(json.dumps([], ensure_ascii=False, indent=4), encoding="utf-8")

def load_all_tasks(tasks_dir: Path) -> List[Task]:
    json_paths = list(tasks_dir.glob("*.json"))
    tasks: List[Task] = []
    def load_single(path: Path) -> Task:
        return Task.load_from_file(path)
    with ThreadPoolExecutor() as executor:
        for task_obj in executor.map(load_single, json_paths):
            tasks.append(task_obj)
    return tasks

def load_all_students(students_file: Path) -> List[Student]:
    data = json.loads(students_file.read_text(encoding="utf-8"))
    students: List[Student] = []
    for entry in data:
        students.append(Student.load_from_dict(entry))
    return students

def save_students(students: List[Student]) -> None:
    data = []
    for s in students:
        data.append({
            "student_id": s.student_id,
            "name": s.name,
            "assigned_tasks": s.assigned_tasks
        })
    STUDENTS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding="utf-8")

def assign_tasks_to_students(students: List[Student], all_tasks: List[Task]) -> None:
    task_dict = {task.id: task for task in all_tasks}
    for student in students:
        student.tasks_objects.clear()
        for task_id in student.assigned_tasks:
            if task_id in task_dict:
                student.assign_task_object(task_dict[task_id])

def save_report(report_data: List[Dict], output_path: Path) -> None:
    output_path.write_text(json.dumps(report_data, ensure_ascii=False, indent=4), encoding="utf-8")

async def run_checks_for_all_students(students: List[Student]) -> List[Dict]:
    report_data: List[Dict] = []
    coroutines = []
    for student in students:
        if not student.tasks_objects:
            report_data.append({"student": student.name, "results": []})
        else:
            coroutines.append(check_tasks_for_student(student.name, student.tasks_objects))
    if coroutines:
        results = await asyncio.gather(*coroutines)
        report_data.extend(results)
    return report_data

def input_student(students: List[Student], all_tasks: List[Task]) -> None:
    print("\nДодавання нового студента")
    student_id = input("Введіть ID студента: ").strip()
    if any(s.student_id == student_id for s in students):
        print("Студент з таким ID вже існує")
        return
    name = input("Введіть ім'я студента: ").strip()
    print("Доступні завдання:")
    for task in all_tasks:
        print(f"{task.id}: {task.title}")
    assigned = input("Введіть номери завдань для призначення (через кому): ").strip()
    try:
        assigned_tasks = [int(x) for x in assigned.split(",") if x.strip().isdigit()]
    except Exception:
        assigned_tasks = []
    new_student = Student(student_id=student_id, name=name, assigned_tasks=assigned_tasks)
    students.append(new_student)
    save_students(students)
    print(f"Студент {name} доданий")

def main():
    create_default_jsons()
    all_tasks = load_all_tasks(TASKS_DIR)
    students = load_all_students(STUDENTS_FILE)

    while True:
        print("\nМеню:")
        print("1. Додати нового студента")
        print("2. Запустити перевірку завдань та зберегти звіт")
        print("3. Вийти")
        choice = input("Оберіть дію: ").strip()
        if choice == "1":
            input_student(students, all_tasks)
            assign_tasks_to_students(students, all_tasks)
        elif choice == "2":
            assign_tasks_to_students(students, all_tasks)
            report_data = asyncio.run(run_checks_for_all_students(students))
            save_report(report_data, REPORT_FILE)
            print(f"Звіт збережено у {REPORT_FILE}")
        elif choice == "3":
            break
        else:
            print("Невірний вибір")

if __name__ == "__main__":
    main()
