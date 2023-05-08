from datetime import datetime, timedelta
import os
import shutil

current_dir = os.getcwd()
now = datetime.now()
yesterday = now - timedelta(1)

yesterday_report_name = yesterday.strftime("%m_%d_%Y_report.md")
new_report_name = now.strftime("%m_%d_%Y_report.md")
yesterday_report_path = os.path.join(current_dir, yesterday_report_name)
new_report_path = os.path.join(current_dir, new_report_name)

def create_new_report():
    with open(new_report_path, "w") as f:
        f.write(now.strftime("# %Y/%m/%d Daily Report"))
        f.write("\n")
        f.write("\n")
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

def copy_yesterdays_report(src_file_path, dest_file_path):
    shutil.copy(src_file_path, dest_file_path)

def check_file_exists(file_path):
    return os.path.exists(file_path)

if check_file_exists(yesterday_report_path):
    copy_yesterdays_report(yesterday_report_path, new_report_path)
else:
    create_new_report()