file_path = "../notes/day1.md"
try:
    with open(file_path, 'r',encoding = 'utf-8') as file:
        content = file.read()
        lines = content.splitlines()
        line_count= len(lines)
        char_count = len(content)
        word_count = len(content.split())
        print(f"文件{file_path}的行数为:{line_count}")
        print(f"文件{file_path}的字符数为:{char_count}")
        print(f"文件{file_path}的单词数为:{word_count}")
except FileNotFoundError:
    print(f"文件不存在")
except Exception as e:
    print(f"发生错误:{e}")
out_path =  "../notes/states.txt"
try:
    with open(out_path, 'w',encoding = 'utf-8') as file:
         file.write(f"文件:{file_path}\n")
         file.write(f"行数:{line_count}\n")
         file.write(f"字符数:{char_count}\n")
         file.write(f"单词数:{word_count}\n")
    print (f"将统计结果写入:{out_path}成功")
except Exception as e:
    print(f"写入文件失败:{e}")
        
