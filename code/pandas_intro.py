import os
import pandas as pd
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script directory: {script_dir}")
project_dir = os.path.dirname(script_dir)
print(f"Project directory: {project_dir}")
data_dir = os.path.join(project_dir, 'data')
print(f"Data directory: {data_dir}")
os.makedirs(data_dir, exist_ok=True)
data = {
    "name": ["张三", "李四", "王五", "赵六", "孙七"],
    "score": [85, 92, 78, 88, 95],
    "class": ["A", "B", "A", "B", "A"]
}
df = pd.DataFrame(data)
sample_file_path = os.path.join(data_dir, 'sample.xlsx')
df.to_excel(sample_file_path, index=False)
print(f"Sample Excel file created at: {sample_file_path}")
df_read = pd.read_excel(sample_file_path)
print("读取的Excel文件内容为:")
print(df_read)
print("\n---数据预览(前三行)---")
print(df_read.head(3))
print("\n---数据维度---")
print(df_read.shape)
print("\n---列名列表---")
print(df_read.columns.tolist())
print("\n---分数列统计信息---")
print(df_read['score'].describe())
mean_score = df_read['score'].mean()
print(f"\n---分数列均值---\n{mean_score}")