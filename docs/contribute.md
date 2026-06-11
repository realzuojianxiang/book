---
title: 贡献指南
description: 如何参与本项目的翻译与改进
---

# 🤝 贡献指南 | Contributing Guide

感谢你对本项目的关注！以下是如何参与翻译和改进的详细说明。

---

## 翻译规范 | Translation Standards

### 格式约定

1. **中文译文紧跟英文原文**，使用 `> 🇨🇳` 引用块标记
2. **数学术语**首次出现时附英文原文，如"满射（Surjective）"
3. **公式不翻译**，保留 LaTeX 原样
4. **定理/定义环境**使用 HTML class 标记：

```markdown
<div class="def-definition" markdown>
**Definition 1.1.** A *set* is a collection of distinct objects.

> 🇨🇳 **定义 1.1.** *集合*是一组不同对象的汇集。
</div>
```

### 示例段落

```markdown
How do you know whether something is true or not? Surely, you've been told
that the angles of a triangle add to 180°, for example, but how do you know
for sure?

> 🇨🇳 你如何判断某件事是否为真？当然，你被告知过三角形内角和
> 为180°，但你如何确信呢？
```

### 未翻译内容

暂时无法翻译的段落请标记为：

```markdown
> 🇨🇳 TODO: 待翻译
```

---

## 工作流程 | Workflow

1. **Fork** 本仓库到你的 GitHub 账户
2. **Clone** 到本地并创建分支：`git checkout -b translate/ch01`
3. **编辑** `docs/` 下对应章节的 Markdown 文件
4. **本地预览**：
   ```bash
   pip install -r requirements.txt
   mkdocs serve
   # 浏览器打开 http://localhost:8000
   ```
5. **提交** 并推送：`git push origin translate/ch01`
6. **创建 Pull Request**，标题格式：`翻译: 第X章 YYY`

---

## 术语表 | Glossary

| English | 中文 | 备注 |
|---------|------|------|
| Proof | 证明 | |
| Theorem | 定理 | |
| Lemma | 引理 | |
| Corollary | 推论 | |
| Definition | 定义 | |
| Proposition | 命题 | |
| Conjecture | 猜想 | |
| Axiom | 公理 | |
| Surjective (Onto) | 满射 | 首次出现附英文 |
| Injective (1-to-1) | 单射 | 首次出现附英文 |
| Bijective | 双射 | |
| Set | 集合 | |
| Subset | 子集 | |
| Union | 并集 | |
| Intersection | 交集 | |
| Cardinality | 基数 | |
| Equivalence Relation | 等价关系 | |
| Modular Arithmetic | 模运算/同余算术 | |
| Mathematical Induction | 数学归纳法 | |
| Strong Induction | 强归纳法 | |
| Well-Ordering Principle | 良序原理 | |
| Pigeonhole Principle | 鸽巢原理 | |
| Inclusion-Exclusion | 容斥原理 | |
