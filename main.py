import datetime
import os

current_dir = os.getcwd()
now = datetime.datetime.now()

file_name = now.strftime("%m_%d_%Y_report.md")
file_path = os.path.join(current_dir, file_name)

with open(file_path, "w") as f:
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
    f.write("## Reflection")
    f.write("\n")
    f.write("\n")
    f.write("## Additional Notes")
    f.write("\n")