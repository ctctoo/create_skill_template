#!/usr/bin/env python3
"""
自动生成Agent Skill目录结构和SKILL.md模板

用法:
    python create_skill_template.py [skill_name]

参数:
    skill_name: 技能名称，默认为 "my-skill"
"""

import os
import sys
from datetime import datetime


def create_skill_template(skill_name: str = "my-skill"):
    """创建Agent Skill目录结构和SKILL.md模板"""

    # 定义目录结构
    directories = [
        skill_name,
        os.path.join(skill_name, "scripts"),
        os.path.join(skill_name, "references"),
        os.path.join(skill_name, "assets"),
    ]

    # 创建目录
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"[创建目录] {directory}/")

    # 生成SKILL.md内容
    skill_md_content = f"""---
name: {skill_name}
description: 描述此技能的功能和用途。说明在什么场景下应该使用此技能，例如：处理特定类型的文件、执行特定的工作流程等。
---

# {skill_name}

## 概述

简要描述此技能的目的和主要功能。

## 使用场景

- 场景1：描述何时使用此技能
- 场景2：另一个使用场景
- 场景3：更多使用场景

## 使用说明

### 步骤1：准备工作

描述开始前的准备工作。

### 步骤2：执行操作

描述具体的操作步骤。

### 步骤3：验证结果

描述如何验证操作是否成功。

## 示例

### 示例1：基本用法

```
输入示例
```

预期输出：

```
输出示例
```

### 示例2：高级用法

```
高级输入示例
```

预期输出：

```
高级输出示例
```

## 注意事项

- 重要提示1
- 重要提示2
- 重要提示3

## 相关资源

- [references/](references/) - 参考文档和资料
- [scripts/](scripts/) - 可执行脚本
- [assets/](assets/) - 模板和资源文件

---

*生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""

    # 写入SKILL.md
    skill_md_path = os.path.join(skill_name, "SKILL.md")
    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(skill_md_content)
    print(f"[创建文件] {skill_md_path}")

    # 创建.gitkeep文件（保持空目录在git中）
    for subdir in ["scripts", "references", "assets"]:
        gitkeep_path = os.path.join(skill_name, subdir, ".gitkeep")
        with open(gitkeep_path, "w", encoding="utf-8") as f:
            f.write("")
        print(f"[创建文件] {gitkeep_path}")

    print(f"\n[成功] Skill模板 '{skill_name}' 创建成功！")
    print(f"\n目录结构：")
    print(f"{skill_name}/")
    print(f"├── SKILL.md          # 技能说明和元数据")
    print(f"├── scripts/          # 可执行代码")
    print(f"├── references/       # 文档参考资料")
    print(f"└── assets/           # 模板、资源文件")


def main():
    # 获取技能名称参数
    skill_name = sys.argv[1] if len(sys.argv) > 1 else "my-skill"

    # 验证名称格式
    if not all(c.isalnum() or c in "-_" for c in skill_name):
        print("错误：技能名称只能包含字母、数字、连字符(-)和下划线(_)")
        sys.exit(1)

    # 检查目录是否已存在
    if os.path.exists(skill_name):
        print(f"警告：目录 '{skill_name}' 已存在")
        response = input("是否覆盖？ (y/N): ").strip().lower()
        if response != "y":
            print("操作已取消")
            sys.exit(0)

    # 创建模板
    create_skill_template(skill_name)


if __name__ == "__main__":
    main()
