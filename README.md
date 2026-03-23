# agent-runtime-core

`agent-runtime-core` 是一个基于 FastAPI 的 Python 服务骨架，用于承载 agent runtime 相关的 API、核心编排、工具调用、记忆管理和服务层逻辑。

当前仓库已完成最小初始化，包含基础目录结构、依赖管理、一个健康检查接口，以及对应测试。

## Requirements

- Python 3.13+

## Quick Start

1. 创建虚拟环境

```bash
python3 -m venv .venv
```

2. 激活虚拟环境

```bash
source .venv/bin/activate
```

3. 安装项目依赖

```bash
pip install -e ".[dev]"
```

4. 启动开发服务

```bash
uvicorn app.main:app --reload
```

5. 运行测试

```bash
pytest
```

## Current Project Structure

```text
.
├── app/
│   ├── agent/
│   │   └── __init__.py
│   ├── api/
│   │   └── __init__.py
│   ├── core/
│   │   └── __init__.py
│   ├── memory/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   ├── tools/
│   │   └── __init__.py
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_health.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Directory Responsibilities

### `app/main.py`

应用入口，负责创建 FastAPI 实例并注册基础路由。当前包含：

- `GET /health`

返回结果：

```json
{
  "status": "ok"
}
```

### `app/api/`

放置 API 路由定义，例如：

- HTTP 接口
- 路由注册
- 请求处理入口

### `app/core/`

放置全局基础能力，例如：

- 配置管理
- 日志封装
- 常量
- 共享基础组件

### `app/agent/`

放置 agent runtime 相关逻辑，例如：

- agent 生命周期管理
- 对话编排
- 任务执行控制

### `app/tools/`

放置外部工具或内部工具的调用封装，例如：

- 工具定义
- 工具执行器
- 工具适配层

### `app/memory/`

放置记忆系统相关模块，例如：

- 会话记忆
- 长短期记忆抽象
- 存储后端适配

### `app/schemas/`

放置 Pydantic 数据模型，例如：

- 请求体
- 响应体
- 内部领域模型

### `app/services/`

放置业务服务层，负责组合多个模块完成具体业务流程，例如：

- runtime service
- memory service
- tool orchestration service

### `tests/`

放置测试代码。当前已有：

- `test_health.py`：验证健康检查接口是否正常返回

## Installed Dependencies

当前项目已安装以下核心依赖：

- `fastapi`
- `uvicorn`
- `pydantic`
- `httpx`
- `python-dotenv`

开发依赖：

- `pytest`

## Next Suggested Steps

- 在 `app/core/` 中增加 `settings.py`，统一管理环境变量
- 在 `app/api/` 中拆分路由模块，并集中注册到 `main.py`
- 在 `app/schemas/` 中定义统一的请求与响应模型
- 在 `app/services/` 中建立首批 service 抽象
