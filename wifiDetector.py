import subprocess
import time
from datetime import datetime

# 定义日志文件名
LOG_FILE = "log.txt"

# 定义间隔时间（秒）
INTERVAL = 10

# 定义需要检测的目标
TARGETS = ["192.168.0.1", "192.168.1.1","www.baidu.com"]

def log_to_file(message):
    """将消息写入日志文件"""
    with open(LOG_FILE, "a") as file:
        file.write(message + "\n")

def check_network(target):
    """检查网络目标是否通畅"""
    try:
        # 执行 ping 命令
        result = subprocess.run(
            ["ping", "-n", "1", target],  # Linux/macOS 使用 "-c"，Windows 使用 "-n"
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=3  # 设置超时时间
        )
        if result.returncode == 0:
            return True
        else:
            return False
    except subprocess.TimeoutExpired:
        return False

def main():
    """主函数：不断检测网络并记录日志"""
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for target in TARGETS:
            if check_network(target):
                log_to_file(f"{now} - {target} is reachable.")
            else:
                log_to_file(f"{now} - {target} is unreachable.")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
