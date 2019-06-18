'''
    学生管理系统
    项目计划
        1.完成数据模型类Studentmodel
        2.创建逻辑控制类StudentManagerController
        3.完成数据：学生列表 _stu_list
        4.行为：获取列表 stu_list
        5.添加学生方法 add_student
        -------------14:30----------
'''
from Studentmodel import  StudentModel
from StudentMangerController_model import StudentManagerController
from student_view import Student_view

student_view = Student_view()

student_view.main()




