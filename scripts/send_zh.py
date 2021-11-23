import shutil
from rich.console import Console


new_trans_dir = "zh"
target_dir = "/Users/qinyu/Documents/rotp/rotp_095/lang"
old_trans_dir = target_dir + "/" + "zh"

# delete lang/zh
try:
    shutil.rmtree(old_trans_dir)
except Exception:
    print(Exception)

# copy new
shutil.copytree(new_trans_dir, old_trans_dir)

console = Console()
console.print("\n完成\n", style="bold green")
