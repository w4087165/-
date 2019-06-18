'''显示界面'''
from Studentmodel import  StudentModel
from StudentMangerController_model import StudentManagerController

class Student_view:
    '''显示界面控制类'''
    def __init__(self):
        self.__menu = '''
        +--------------------------------+
        |   1）添加学生信息                |
        |   2）显示学生信息                |
        |   3）删除学生信息                |
        |   4）修改学生成绩                |
        |   5）按学生成绩低~高显示学生信息    |
        +--------------------------------+
        '''
        self.stuManger = StudentManagerController()

    def __display_menu(self):
        print(self.__menu)

    def __select_menu(self):
        item = input('请输入：')
        if item == '1':
            self.__input_students()
        elif item == '2':
            self.__output_students(self.stuManger.stu_list)
        elif item == '3':
            self.__delete_student()
        elif item == '4':
            self.__modify_student()
        elif item == '5':
            self.__output_student_by_score()
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        name = input('请输入学生姓名：')
        age = int(input('请输入学生年龄：'))
        score = int(input('请输入学生成绩'))
        self.stuManger.add_student(StudentModel(name,age,score))

    def __output_students(self,stulist):

        print('%s\t\t%s\t\t%s\t\t%s' % (' ID ','name', 'age', 'score'))
        for i in stulist:
            print('%s\t\t% s \t\t% s\t\t% s '%(i.id,i.name,i.age,i.score))
    def __delete_student(self):
        student_id = int(input('请输入要删除学生的id：'))
        result = self.stuManger.remove_student(student_id)
        print(result)

    def __modify_student(self):
        student_id = int(input('请输入要修改学生的id：'))
        result = self.stuManger.update_student(student_id)
        print(result)

    def __output_student_by_score(self):
        result = self.stuManger.order_by_socre()
        self.__output_students(result)