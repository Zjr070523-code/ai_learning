students = [
    {"name": "张三", "score": 85, "class": "A"},
    {"name": "李四", "score": 92, "class": "B"},
    {"name": "王五", "score": 78, "class": "A"},
    {"name": "赵六", "score": 88, "class": "B"},
    {"name": "孙七", "score": 95, "class": "A"},
]
high_scorers = [student for student in students if student["score"] > 90]
print("成绩大于90的学生有:",[student["name"] for student in high_scorers])
squares = [ (student["name"],student["score"] ** 2 )for student in students]
print("学生成绩的平方分别为:", squares)
for student in students:
    if student["score"] >=90:
        grade = "A"
    elif student["score"] >=80:
        grade = "B"
    else:
        grade = "C"
    print(f"学生{student["name"]}的成绩是{student["score"]},对应的等级是{grade}")

    
