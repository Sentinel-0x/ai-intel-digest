#!/bin/bash
# 切换到项目绝对路径
cd /home/melody/ai-intelligence-agent

# 激活虚拟环境并执行主程序，输出同时写入标准输出和日志文件
source venv/bin/activate
python3 main.py >> /home/melody/ai-intelligence-agent/cron_job.log 2>&1
