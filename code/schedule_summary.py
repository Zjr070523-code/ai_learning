schedule = [
    {"day":"MONDAY","course":"math","teacher":"JEFF"},
    {"day":"TUESDAY","course":"english","teacher":"MARY"},
    {"day":"WEDNESDAY","course":"computer","teacher":"JACK"},
    {"day":"THURSDAY","course":"math","teacher":"JEFF"},
    {"day":"FRIDAY","course":"english","teacher":"MARY"},
]
monday_courses = [item for item in schedule if item["day"] == "MONDAY"]
if monday_courses:
    coures_name = [course["course"] for course in monday_courses]
    teacher_nme = [course["teacher"] for course in monday_courses]
    course_str = ",".join(coures_name)
    teacher_str = ",".join(teacher_nme)
    summary = f"星期一的课程有:{course_str},授课老师有:{teacher_str}"
else :
    summary = "星期一没有课"
print(summary)
output_path = "./summary.txt"
try:
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(summary)
    print(f"将课程总结写入:{output_path}成功")
except Exception as e:
    print(f"写入文件失败:{e}")
