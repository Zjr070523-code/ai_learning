squares = [x**2 for x in range(1 , 11)]
print("1到10的平方数:",squares)
evens = [x for x in range(1,21) if x % 2 == 0]
print("1到20的偶数:",evens)
student = {"name" :"张三", "age":"20","course":["数学","英语","信息"]}
print("学生姓名:",student.get("name"))
print("学生年龄:",student.get("age"))
print("学生选课:",student.get("course"))
score = student.get("score",0)
print("成绩:",score)
print(f"学生{student['name']}今年{student['age']}岁,选择了{len(student['course'])}门课")
score = 86
if score >= 90:
 grade = "A"
elif score >=80:
 grade = "B"
else :
 grade = "C"
print(f"成绩:{score}对应等级是{grade}")
for key,value in student .items():
    print(f"{key}:{value}")
