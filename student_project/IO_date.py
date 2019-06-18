'''数据读入读写模块'''
from student_project.Studentmodel import StudentModel

def studentMsgRead():
    """获取学生读取文件后的列表"""
    s = open('student_msg', 'r', encoding='utf-8')
    student_list = []
    with s:
        for i in s:
            stu_list = i.strip().split(',')
            student_list.append(StudentModel(stu_list[1],int(stu_list[2]),int(stu_list[3]),int(stu_list[0])))
    return student_list


def get_student_id():
    offs = -1
    '''获取文件中最后一行的id信息 若无返回1000'''
    with open('student_msg', 'rb') as s:
        if not s.read(1):
            print('空')
            return 1000

        if len(s.readlines()) == 1:
            print('ss')
            s.seek(0,0)
            line = s.readline()
        else:
            while True:
                s.seek(offs,2)
                line = s.readlines()
                print(line)
                if len(line)>1:
                    line = line[-1]
                    break
                else:
                    offs *= 2
        print(line)
        s = line.decode('utf-8')
        lastID = s.split(',')[0]
    return int(lastID)

def studentMsgWrite(stu_info):

    s = open('student_msg','a',encoding='utf-8')
    with s:
        string = ','.join([str(i) for i in stu_info.__dict__.values()])
        string += '\n'
        s.write(string)

l = studentMsgRead()
print(l)
