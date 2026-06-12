#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate all TODOs in ch01/05-its-wise-to-exercise.md"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = 'docs/part-i/ch01-what-is-mathematics/05-its-wise-to-exercise.md'
with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read()

todo_marker = 'TODO: 待翻译'

translations = [
    # 1: Section intro - exercises overview
    '**练习的智慧** 本节提供一些练习帮助你巩固所学。数学学习需要主动练习，而非被动阅读。每个练习都是对前面概念的直接应用。',
    # 2: Section 1.5.2 Remind Yourself
    '**回顾自检** 简要回答以下问题。如果你无法回忆某个定义、概念或例子，回去重读相关部分。\n\n(1) 数学的两个主要目标是什么？\n(2) 真理和证明之间有什么关系？\n(3) 什么是归纳过程？举例说明。\n(4) 符号在数学中起什么作用？',
    # 3: Section 1.5.3 Try It
    '**动手试试** 回答以下简答题，要求写下或说出答案。目标是练习使用新概念、定义和符号。\n\n(1) 用自己的话描述"数学"和"做数学"之间的区别。\n(2) 找一个朋友，试着向他解释"数学证明"是什么。你用了什么类比？',
    # 4: More Try It questions
    '(3) 回顾本章讨论的归纳过程。举一个你自己想到的、不同于本书的归纳过程例子。\n(4) 为什么符号很重要？如果没有符号，数学会怎样？',
    # 5: Section 1.5.4 Exercises
    '**练习** 这些问题需要更多工作和思考。(1) 回顾 1.2 节中立方数的讨论。我们如何从 $n^3$ 到 $(n+1)^3$ 的关系中推导出求和公式？写下推导过程。',
    # 6: More exercises
    '(2) 回顾 1.2 节中平面直线的讨论。我们如何从 $n$ 条直线到 $n+1$ 条直线的关系中推导出公式 $R(n)$？写下推导过程。',
    # 7: More exercises
    '(3) 书中提到数学的两个主要目标是"发现真理"和"通过证明验证真理"。举例说明这两个目标的区别。',
    # 8: More exercises
    '(4) 解释"归纳推导"和"演绎证明"之间的区别。为什么我们既需要归纳推导来发现公式，又需要演绎证明来验证公式？',
    # 9: More exercises
    '(5) 符号如何帮助我们压缩信息和揭示模式？举一个具体的例子。',
    # 10: Final exercise
    '(6) 思考"省略号（$\\ldots$）"在数学推导中的问题。为什么省略号不够严谨？用本章的具体例子说明。',
]

count = 0
for t in translations:
    idx = data.find(todo_marker)
    if idx >= 0:
        data = data[:idx] + t + data[idx+len(todo_marker):]
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(data)
print(f"Replaced {count} TODOs, remaining: {data.count('TODO')}")
