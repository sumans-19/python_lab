import numpy as np
#dir(np)

data_type = [('name' , 'S15'),('class' , int) ,('height' , int)]
# column name followed by ots data types and s15 stands for string with 15 characters , float can be used , long can be used too.

print(type(data_type))

# creating a stryctured array 'student' using the def

students = np.zeros(4,dtype=data_type)
students['name'] = ['luffy' ,'zoro' ,'sanji' , 'nami']
students['class'] = [10,11,12,13]
students['height'] = [105,102,109,103]

#display the details:
print("original array :")
print(students)



print("sorted array is : ")
print(np.sort(students, order='height'))
