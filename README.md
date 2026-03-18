功能说明:

自动生成Agent Skill目录结构
创建完整的SKILL.md模板文件
支持自定义技能名称（默认为my-skill）
生成的目录结构:


my-skill/
├── SKILL.md          # 技能说明和元数据（包含YAML frontmatter）
├── scripts/          # 可执行代码目录
├── references/       # 文档参考资料目录
└── assets/           # 模板、资源文件目录
使用方法:


# 使用默认名称 my-skill
python create_skill_template.py

# 使用自定义名称
python create_skill_template.py my-custom-skill
SKILL.md模板已包含完整的结构：元数据头、概述、使用场景、使用说明、示例、注意事项和相关资源链接。
