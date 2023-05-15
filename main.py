from datetime import datetime, timedelta
import os
import shutil

def create_new_log(new_log_path):
    with open(new_log_path, "w") as f:
        f.write("## TODO List")
        f.write("\n")
        f.write("- [ ] 出勤打刻 & slack通知")
        f.write("\n")
        f.write("- [ ] 日報投稿")
        f.write("\n")
        f.write("- [ ] 退勤打刻 & slack通知")
        f.write("\n")
        f.write("\n")
        f.write("## 反省")
        f.write("\n")
        f.write("\n")
        f.write("## +αで達成できたら良いこと")
        f.write("\n")
        f.write("\n")
        f.write("## 宿題")
        f.write("\n")

def copy_latest_log(src_log_path, dest_log_path):
    shutil.copy(src_log_path, dest_log_path)

def check_log_exists(file_path):
    return os.path.exists(file_path)

def get_latest_log_path(searchDirPath):
    latest_log_path = None
    for filename in os.listdir(searchDirPath):
        filepath = os.path.join(searchDirPath, filename)
        if os.path.isfile(filepath):
            if latest_log_path is None or os.path.getctime(filepath) > os.path.getctime(latest_log_path):
                latest_log_path = filepath
    return latest_log_path

current_dir = os.getcwd()
now = datetime.now()
yesterday = now - timedelta(1)

new_log_name = now.strftime("%m_%d_%Y_log.md")
latest_log_path = get_latest_log_path(current_dir)
new_log_path = os.path.join(current_dir, new_log_name)

if latest_log_path is None:
    create_new_log(new_log_path=new_log_path)
else:
    copy_latest_log(src_log_path=latest_log_path, dest_log_path=new_log_path)