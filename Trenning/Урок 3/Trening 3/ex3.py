from student import Student
from course_group import CourseGroup

# 2. Сначала создаем студентов (сначала наполняем список сокурсников)
# Создаем список classmates (сокурсников)
classmates_list = [
    Student("Иван", "Иванов", 19, 2),
    Student("Петр", "Петров", 20, 2),
    Student("Анна", "Сидорова", 19, 2)
]

main_student = Student("Руслан", "Хатукаев", 52, 1)

# 4. Создаем экземпляр группы и передаем туда студента и список сокурсников
group = CourseGroup(main_student, classmates_list)

# 5. Формируем строку со списком сокурсников для вывода
# Соберем их полные имена в одну строку через запятую
classmates_names = ", ".join([student.get_full_name() for student in group.classmates])

# 6. Выводим информацию в требуемом формате
print(f"{group.student.get_full_name()}, {group.student.age} лет, учится на курсе {group.student.course} вместе с: {classmates_names}")
