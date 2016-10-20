# -*- encoding: utf-8 -*-
'''
Created on 2016年10月15日

@author: LuoPei
'''

import operator
from operator import itemgetter, attrgetter,methodcaller


# sorting dictionary

classCount={"1":2,"2":1,"3":2}
sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True) #按照字典的第二个元素进行排序,得到一个list
print sortedClassCount,sortedClassCount[0],sortedClassCount[0][0]


d = {1: 'z', 2:'y', 3: 'x'}
print sorted(d.items(), key=lambda x: x[1])#按照字典的键值进行排序,得到一个list

#我甚至可以得到一个根据value排序的字典，只需要用 collections.OrderedDict 即可：
from collections import OrderedDict
sorted_d = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
print sorted_d

 
# sorting list
l = [43, 12, 4, 6]
l.sort()
print l



#the list.sort() method is only defined for lists. In contrast, the sorted() function accepts any iterable.

print sorted([5, 2, 3, 1, 4])
print  sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})


#题目
# 给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
# 
# 所有的小写字母在大写字母前面
# 所有的字母在数字前面
# 所有的奇数在偶数前面

#通俗讲，key 用来决定在排序算法中 cmp 比较的内容，key 可以是任何可被比较的内容，比如元组（python 中元组是可被比较的）。所以上面的排序问题可以用下面的代码来解决：
s = "Sorting1234"
sorted_s="".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)))
print sorted_s



#KEY FUNCTIONS

print sorted("This is a test string from Andrew".split(), key=str.lower)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print sorted(student_tuples, key=lambda student: student[2])   # sort by age
print sorted(student_tuples, key=itemgetter(2))
print  sorted(student_tuples, key=itemgetter(2), reverse=True) #Ascending and Descending



#The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:
print sorted(student_tuples, key=itemgetter(1,2))




class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print sorted(student_objects, key=lambda student: student.age)   # sort by age
print  sorted(student_objects, key=attrgetter('age'))
print sorted(student_objects, key=attrgetter('grade', 'age')) #sort by grade then by age:

#operator.methodcaller() 

messages = ['critical!!!', 'hurry!', 'standby', 'immediate!!']
print  sorted(messages, key=methodcaller('count', '!'))



 

# if __name__=="__main__":
#     pass