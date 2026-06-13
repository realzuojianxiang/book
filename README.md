# Everything You Always Wanted To Know About Mathematics

> *But didn't even know to ask*

📖 **双语对照阅读** | 🌐 [在线阅读](https://realzuojianxiang.github.io/book/)

---

## 🎯 项目简介

本书是 Brendan W. Sullivan 的数学入门经典，涵盖抽象数学思维与证明写作的核心内容。本项目将其构建为**中英双语对照**的在线阅读站点，方便中文读者学习。

### 核心特性

| 特性 | 实现 |
|------|------|
| 🔤 双语对照 | 英文原文 + 中文译文段落级穿插，一键切换显示模式 |
| 🔍 全文搜索 | 支持中英文混合搜索 |
| 🌙 深色模式 | 跟随系统偏好，手动切换 |
| 📊 阅读进度 | 自动跟踪滚动位置，恢复上次阅读 |
| 📐 数学公式 | MathJax 渲染 LaTeX 公式 |
| 📱 移动适配 | 完整响应式设计 |
| 🏷️ 标签系统 | 按主题标签浏览内容 |
| ⚡ SPA 导航 | 页面切换无需刷新 |

---

## 📚 内容结构

### Part I — 学会数学思考 | Learning to Think Mathematically

1. **What Is Mathematics?** — 真理与证明、符号与逻辑基础
2. **Mathematical Induction** — 归纳原理、多米诺类比、汉诺塔
3. **Sets** — 集合定义、运算、子集、笛卡尔积、证明策略
4. **Logic** — 命题、量词、联结词、等价、证明写作
5. **Rigorous Mathematical Induction** — 强归纳法、良序原理

### Part II — 学习数学主题 | Learning Mathematical Topics

6. **Relations and Modular Arithmetic** — 等价关系、序关系、模运算
7. **Functions and Cardinality** — 满射/单射/双射、可数性
8. **Combinatorics** — 计数原理、鸽巢原理、容斥原理
A. **Definitions and Theorems** — 全书定义定理速查

---

## 🚀 快速开始

### 前置要求

- Python 3.10+
- pip

### 本地预览

```bash
# 1. 克隆仓库
git clone https://github.com/realzuojianxiang/book.git
cd book

# 2. 安装依赖
pip install -r requirements.txt

# 3. 本地预览（热重载）
mkdocs serve

# 4. 浏览器打开 http://localhost:8000
```

### 构建静态站点

```bash
mkdocs build --strict
# 输出目录：site/
```

---

## 🤝 贡献指南

我们欢迎任何形式的贡献，特别是**中文翻译**！

### 翻译流程

1. 🍴 Fork 本仓库
2. 🌿 创建分支：`git checkout -b translate/ch01`
3. ✏️ 编辑 `docs/` 下对应章节的 Markdown 文件
4. 🧪 本地预览确认效果：`mkdocs serve`
5. 🔀 提交 Pull Request

### 翻译格式

```markdown
How do you know whether something is true or not?

> 🇨🇳 你如何判断某件事是否为真？
```

- 中文译文使用 `> 🇨🇳` 引用块紧跟英文原文
- 术语首次出现附英文：如"满射（Surjective）"
- 数学公式不翻译，保留 LaTeX
- 未翻译内容标记为 `> 🇨🇳 TODO: 待翻译`

详见 [贡献指南](docs/contribute.md)。

---

## 🛠️ 技术栈

| 组件 | 选型 | 理由 |
|------|------|------|
| 站点生成 | MkDocs Material 9.5+ | 搜索/深色模式/导航/插件生态 |
| 数学渲染 | MathJax 3 | LaTeX 公式支持 |
| 双语切换 | 自定义 JS | localStorage 持久化 |
| 阅读进度 | 自定义 JS | 客户端滚动追踪 |
| 部署 | GitHub Pages | 免费、CI/CD 自动化 |
| CI/CD | GitHub Actions | push to main → 自动构建部署 |

---

## 📁 项目结构

```
├── .github/workflows/deploy.yml   # GitHub Actions 自动部署
├── docs/
│   ├── index.md                    # 首页
│   ├── contribute.md               # 贡献指南
│   ├── tags.md                     # 标签索引
│   ├── assets/
│   │   ├── css/
│   │   │   ├── bilingual.css       # 双语样式 + 定义/定理环境
│   │   │   └── math.css            # 数学公式增强
│   │   ├── js/
│   │   │   ├── bilingual-toggle.js # 双语显示切换
│   │   │   └── reading-progress.js # 阅读进度跟踪
│   │   └── images/                 # 图片资源
│   ├── overrides/                  # MkDocs 模板覆盖
│   ├── part-i/                     # Part I 章节
│   │   ├── index.md
│   │   ├── ch01-what-is-mathematics/
│   │   │   ├── index.md            # ✅ 完整双语示例
│   │   │   ├── 01-truths-and-proofs.md  # ✅ 完整双语示例
│   │   │   └── ...
│   │   ├── ch02-mathematical-induction/
│   │   ├── ch03-sets/
│   │   ├── ch04-logic/
│   │   └── ch05-rigorous-induction/
│   └── part-ii/                    # Part II 章节
│       ├── index.md
│       ├── ch06-relations-modular-arithmetic/
│       ├── ch07-functions-cardinality/
│       ├── ch08-combinatorics/
│       └── ch09-definitions-theorems/
├── mkdocs.yml                      # MkDocs 配置（导航/插件/主题）
├── requirements.txt                # Python 依赖
├── .gitignore
└── README.md                       # 本文件
```

---

## 📄 许可证

- **原文**：Copyright © 2013 Brendan W. Sullivan. 本项目仅用于学习目的。
- **译文**：社区贡献，采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可。
- **项目代码**：[MIT License](LICENSE).
