"""
資料夾刪除工具
使用請注意!!有一定危險性!!!
"""
import os
import shutil
import psutil

def delete_folder(folder_path):# 刪除資料夾
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"資料夾已刪除：{folder_path}")
        else:
            print("指定的資料夾不存在。")
    except Exception as e:
        print(f"刪除失敗，原因：{e}")



def check_folder_in_use(folder_path):# 找出占用原因
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for item in proc.open_files() or []:
                if folder_path in item.path:
                    print(f"程式 {proc.info['name']} (PID: {proc.info['pid']}) 正在使用 {item.path}")
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
    

# 找出占用
check_folder_in_use(r"path")

# 刪除
#delete_folder(r"D:\Danny\path")
