# Build Log: ai-intelligence-agent

## Log 001: 架构污染与模块边界混淆
- **什么坏了 (What broke)**: 
  在初始化底层底座项目 `ai-intelligence-agent` 并运行 `pytest tests/` 时，测试套件抛出 `ImportError: cannot import name 'quick_filter' from 'job_agent'`，导致底层底座无法独立测试。
- **为什么坏 (Why it broke)**: 
  早期单体原型中，求职过滤逻辑（`job_agent.py`）与底层 ReAct 核心引擎紧密耦合。在拆分项目时，业务逻辑代码被错误地残留或交叉引用在底座目录中，破坏了底座的纯净性。
- **怎么修的 (How it was fixed)**: 
  严格执行架构解耦原则：将所有与特定业务（求职、简历优化）相关的模块从底座 `ai-intelligence-agent` 中剥离，移入上层业务专属项目 `job-hunter-agent` 中。同时清理底座测试文件，确保底座专注于安全沙箱与通用 ReAct 循环，实现单一职责。
