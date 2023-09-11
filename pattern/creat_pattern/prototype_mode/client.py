from student import Student


if __name__ == '__main__':
    student1 = Student()
    student1.name = '张三'
    student2 = student1.deep_clone()
    student2.name = '李四'
    student1.show_name()
    student2.show_name()
    print(id(student1.name))
    print(id(student2.name))
    student3 = student1.shallow_clone()
    student3.name = '王五'
    student1.show_name()
    student3.show_name()
    print(id(student1.name))
    print(id(student3.name))
