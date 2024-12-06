class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        if self.grades:
            total_grades = sum([sum(grades) for grades in self.grades.values()])
            total_courses = sum([len(grades) for grades in self.grades.values()])
            return total_grades / total_courses
        return 0

    def __str__(self):
        avg_grade = self.get_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() < other.get_avg_grade()
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() <= other.get_avg_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() > other.get_avg_grade()
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() >= other.get_avg_grade()
        return False

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() == other.get_avg_grade()
        return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        if self.grades:
            total_grades = sum([sum(grades) for grades in self.grades.values()])
            total_courses = sum([len(grades) for grades in self.grades.values()])
            return total_grades / total_courses
        return 0

    def __str__(self):
        avg_grade = self.get_avg_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() < other.get_avg_grade()
        return False

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() <= other.get_avg_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() > other.get_avg_grade()
        return False

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() >= other.get_avg_grade()
        return False

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() == other.get_avg_grade()
        return False


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def review_hw(self, student, course, grade):
        self.rate_hw(student, course, grade)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках курса
def average_homework_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    if total_students > 0:
        return total_grades / total_students
    return 0


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecture_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    if total_lecturers > 0:
        return total_grades / total_lecturers
    return 0


# Пример создания экземпляров
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Anna', 'Smith', 'female')
student2.courses_in_progress = ['Python']
student2.finished_courses = ['Введение в программирование']

lecturer1 = Lecturer('John', 'Doe')
lecturer1.courses_attached = ['Python']
lecturer1.grades = {'Python': [9, 10, 8]}

lecturer2 = Lecturer('Jane', 'Doe')
lecturer2.courses_attached = ['Python']
lecturer2.grades = {'Python': [10, 9, 9]}

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached = ['Python']

reviewer2 = Reviewer('Mike', 'Johnson')
reviewer2.courses_attached = ['Python']

# Пример выставления оценок
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Python', 9)

student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 9)

# Вывод информации о студентах, лекторах и проверяющих
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Пример подсчета средней оценки за домашние задания всех студентов по курсу
students = [student1, student2]
course_name = 'Python'
avg_homework = average_homework_grade(students, course_name)
print(f"Средняя оценка за домашние задания по курсу {course_name}: {avg_homework:.1f}")

# Пример подсчета средней оценки за лекции всех лекторов по курсу
lecturers = [lecturer1, lecturer2]
avg_lecture = average_lecture_grade(lecturers, course_name)
print(f"Средняя оценка за лекции по курсу {course_name}: {avg_lecture:.1f}")
