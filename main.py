class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [ ]
        self.courses_in_progress = [ ]
        self.grades = {}


    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_st(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def averge(self):
        if not self.grades:
            return 0
        all_sum = 0
        all_count = 0
        for value_grades_for_one_course in self.grades.values():
            all_sum = all_sum + sum(value_grades_for_one_course)
            all_count = all_count + len(value_grades_for_one_course)
        return all_sum / all_count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n' 
                f'Средняя оценка за домашнее задание: {self.averge}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')

    def __lt__(self, other):
        return self.averge < other.averge


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [ ]


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def averge_l(self):
        if not self.lecturer_grades:
            return 0
        all_sum = 0
        all_count = 0
        for value_grades_for_one_course in self.lecturer_grades.values():
            all_sum = all_sum + sum(value_grades_for_one_course)
            all_count = all_count + len(value_grades_for_one_course)
        return all_sum / all_count

    def __lt__(self, other):
        return self.averge_l < other.averge_l


    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оцена за лекции: {self.averge_l}')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')




student_1 = Student('Басик', 'Басиков', 'кот')
student_2 = Student('Носок', 'Носочкин', 'кот')
student_1.courses_in_progress += ['Питон']
student_1.courses_in_progress += ['Джава']
student_1.finished_courses += ['Кобра']
student_2.courses_in_progress += ['Питон']
student_2.finished_courses += ['Джава']


lecturer_1 = Lecturer('Мистер', 'Фрэш')
lecturer_2 = Lecturer('Шлёпа', 'Большой')
rewiewer_1 = Reviewer('Грэмпи', 'Кэт')
rewiewer_2 = Reviewer('Кейборд', 'Кэт')
lecturer_1.courses_attached += ['Питон']
lecturer_1.courses_attached += ['Джава']
rewiewer_1.courses_attached += ['Питон']
rewiewer_1.courses_attached += ['Джава']
lecturer_2.courses_attached += ['Питон']
rewiewer_2.courses_attached += ['Джава']

rewiewer_1.rate_hw(student_1, 'Питон', 10)
rewiewer_2.rate_hw(student_1, 'Питон', 6)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# (cool_mentor.rate_hw(best_student, 'Python', 10)

print (student_1.grades)
