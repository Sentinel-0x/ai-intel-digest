import sys
import os

# 引擎在相邻目录里，不是已安装的包：两个仓库必须并排放置
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "sentinel-react-engine"))
from sandbox_executor import run_code_in_sandbox


class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name: str, func):
        self.tools[name] = func

    def execute_dynamic_tool(self, code_str: str, caller_id: str = "ai-intel-digest") -> dict:
        """
        在引擎沙箱里执行动态生成的工具代码，原样返回引擎的结果字典
        (execution_id / caller_id / status / output / timestamp)。
        AST 检查只在引擎里做一次，这样所有拦截都会进入引擎的审计记录和告警；
        在这里先拦截的话，引擎的监控层看不到这些试探。
        """
        return run_code_in_sandbox(code_str, caller_id=caller_id)


registry = ToolRegistry()
