# 设计模式与类结构知识库：Hikari Agent 项目解读

作为您的计算机老师，今天我们来剖析一下 Hikari Agent 项目中应用的一些经典编程智慧。理解这些模式，能让您的代码不仅“能跑”，而且“优雅且易于维护”。


## 1. 工厂模式 (Factory Pattern)
### 在项目中的应用
- **文件路径**: src/agents/agents.py
- **函数名称**: create_agent
- **实现细节**: 此函数根据传入的角色类型（如 coordinator, planner 等），初始化并配置相应的 Agent 实例。它通过封装 LangGraph 的 Agent 初始化过程，确保了对象创建的一致性。

<br><strong>老师点评</strong>：如果不使用工厂模式，每次创建一个新 Agent，您可能都要在代码里重复进行类似的初始化和配置步骤。有了这个“工厂”，您只需要传入参数，它就能为您吐出一个配置好的、健壮的 Agent 对象。


## 2. 数据对象模式 (Data Classes / Pydantic)
### 在项目中的应用
- **文件路径**: src/config/configuration.py, src/graph/types.py
- **类名称**: Configuration (DataClass), State (MessagesState)
- **实现细节**: 使用 @dataclass 和 Pydantic 定义了任务处理的状态空间和配置参数，确保数据在传递过程中的类型安全性与结构完整性。

<br><strong>老师点评</strong>：使用这些数据类，您不仅拥有了自动校验数据的能力（比如如果应该传数字却传了字符串，程序会立即报错，而不是运行到一半才崩溃），还拥有了像“类型提示”这样的神器。

## 3. 状态模式 (State Pattern)
### 在项目中的应用
- **文件路径**: src/graph/types.py, src/graph/nodes.py
- **类/函数名称**: State 类, coordinator_node, planner_node, coder_node 等
- **实现细节**: State 类作为全局状态，存储了任务执行过程中的所有上下文（如 current_plan, messages 等）。各 Node 函数根据 State 中的数据动态决定下一步动作，并返回新的 State。

<br><strong>老师点评</strong>：在 LangGraph 中，State 就像是一个“剧本”，每一个 Node 函数都在读取这个剧本，根据当前状态决定接下来执行哪一步，并更新剧本内容。这使得复杂的 Agent 任务流程不再是混乱的 if-else，而是条理分明的状态流转。


## 4. 策略模式 (Strategy Pattern)
### 在项目中的应用
- **文件路径**: src/llms/llm.py, src/graph/nodes.py
- **函数名称**: get_llm_by_type, planner_node
- **实现细节**:
    - get_llm_by_type: 根据配置在 OpenAI, DeepSeek 等模型间动态切换。
    - planner_node: 根据用户任务（如“行业分析”）选择不同的 prompt 模板分支。

<br><strong>老师点评</strong>：这是解耦业务决策与具体执行的最常用手段。当您需要增加一种新的分析类型时，不需要改动核心流程逻辑，只需新增一个策略分支即可。


## 5. 装饰器模式 (Decorator Pattern)
### 在项目中的应用
- **文件路径**: src/server/app.py, src/graph/nodes.py, src/tools/decorators.py
- **装饰器名称**: @app.post, @tool, @log_io
- **实现细节**:
    - @app.post: FastAPI 路由注册。
    - @tool: 将函数封装为可调用的 Agent 工具。
    - @log_io: 自定义的日志装饰器，记录输入参数与执行结果。

<br><strong>点评</strong>：这是 Python 的灵魂。它让您的主逻辑代码非常纯粹，而将像权限校验、接口注册、日志埋点这些“脏活累活”交给装饰器在幕后处理。

