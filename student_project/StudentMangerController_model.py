#导入文件读写模块
from student_project.IO_date import *

class StudentManagerController:
    '''逻辑控制类StudentManagerController
        对学生类 进行逻辑处理'''
    __init_id = get_student_id()
    def __init__(self):
        self.__stu_list = studentMsgRead()

    @property
    def stu_list(self):

        return self.__stu_list

    #添加学生方法 add_student
    def add_student(self,stu_info):
        stu_info.id = self.__geterate_id()    #更新id编号
        self.__stu_list.append(stu_info)
        studentMsgWrite(stu_info)

    def __geterate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id


    # 根据id查找学生，找到后返回学生对象
    def __find_student_byid(self, id):
        for i in self.__stu_list:
            if i.id == id:
                return i

    #删除学生
    def remove_student(self,id):
        del_student = self.__find_student_byid(id)
        if del_student:

            self.__stu_list.remove(del_student)
            return '删除成功！'
        else:
            return '没有满足条件的删除对象'

    #修改学生信息
    def update_student(self,id):
        upstudent = self.__find_student_byid(id)
        print(upstudent)
        if  upstudent:
            #更新信息
            upstudent.name = input('请输入新的名字')
            upstudent.age = input('请输入年龄')
            upstudent.score = input('成绩：')
            return '修改成功'
        else:
            return '没有满足条件的对象'

    #排序学生信息从第低~高
    def order_by_socre(self):
        order_list = sorted(self.stu_list,key=self.get_socre)
        return order_list
    #获取学生成绩
    def get_socre(self,stu_info):
        return stu_info.score

#文件操作IO类：



#测试用例
import Studentmodel
if __name__ == '__main__':
    stumanger = StudentManagerController()
    stumanger.stu_list
    stumanger.add_student(Studentmodel.StudentModel('闫少甫',1,1))
    stumanger.add_student(Studentmodel.StudentModel('闫少甫',1,2))





