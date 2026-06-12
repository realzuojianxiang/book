#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate all TODOs in ch04/05-logical-connectives.md"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = 'docs/part-i/ch04-logic/05-logical-connectives.md'
with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read()

todo_marker = 'TODO: 待翻译'

translations = [
    # 1: Intro to connectives
    '**逻辑联结词（Logical Connectives）** 联结词将简单命题组合成复合命题，是逻辑推理的基本工具。本节介绍四种主要联结词及其含义。',
    # 2: Conjunction (AND)
    '**合取（Conjunction，$\\wedge$）** "$P$ 且 $Q$"写作 $P \\wedge Q$。当且仅当 $P$ 和 $Q$ 同时为真时，$P \\wedge Q$ 为真。例：设 $P$ 为"今天是周一"，$Q$ 为"在下雨"，则 $P \\wedge Q$ 要求两个条件同时满足。',
    # 3: Disjunction (OR)
    '**析取（Disjunction，$\\vee$）** "$P$ 或 $Q$"写作 $P \\vee Q$。当至少一个为真时为真（**兼或**，inclusive or）。例："$x > 0$ 或 $x = 0$"包括了 $x=0$ 的情况。注意这与日常语言中的"排他或"不同。',
    # 4: Conditional (IF...THEN)
    '**条件语句（Conditional，$\\Rightarrow$）** "若 $P$ 则 $Q$"写作 $P \\Rightarrow Q$。$P$ 称为假设（Hypothesis），$Q$ 称为结论（Conclusion）。关键观察：当 $P$ 为假时，$P \\Rightarrow Q$ 自动为真——因为条件语句对 $P$ 为假的情况不做任何断言，不能宣称其为假，故由排中律知其为真。',
    # 5: Vacuous truth
    '**空虚真（Vacuous Truth）** 条件语句在假设为假时为真，这称为"空虚真"。虽然反直觉，但这是逻辑系统的必要约定。例："若 $1 > 2$，则月亮是奶酪做的"——这是一个真命题，因为假设为假。',
    # 6: Biconditional (IFF)
    '**双条件语句（Biconditional，$\\Leftrightarrow$）** "$P$ 当且仅当 $Q$"写作 $P \\Leftrightarrow Q$，即 $(P \\Rightarrow Q) \\wedge (Q \\Rightarrow P)$。当且仅当 $P$ 和 $Q$ 具有相同真值时为真。',
    # 7: Truth table summary
    '**真值表汇总**\n\n| $P$ | $Q$ | $P \\wedge Q$ | $P \\vee Q$ | $P \\Rightarrow Q$ | $P \\Leftrightarrow Q$ |\n|-----|-----|---------|---------|------------|-------------|\n| T | T | T | T | T | T |\n| T | F | F | T | F | F |\n| F | T | F | T | T | F |\n| F | F | F | F | T | T |',
    # 8: Contrapositive, converse, inverse
    '**相关条件语句** 条件语句 $P \\Rightarrow Q$ 有三种相关形式：\n- **逆否命题（Contrapositive）**：$\\neg Q \\Rightarrow \\neg P$——与原命题同真值\n- **逆命题（Converse）**：$Q \\Rightarrow P$——不一定与原命题同真值\n- **否命题（Inverse）**：$\\neg P \\Rightarrow \\neg Q$——与逆命题同真值\n\n重要：条件语句与其逆否命题逻辑等价，但与逆命题不等价！',
    # 9: Examples of conditional statements
    '**示例** 设 $P$ 为"$n$ 是偶数"，$Q$ 为"$n^2$ 是偶数"。\n- 命题 $P \\Rightarrow Q$："若 $n$ 是偶数，则 $n^2$ 是偶数"——真\n- 逆命题 $Q \\Rightarrow P$："若 $n^2$ 是偶数，则 $n$ 是偶数"——真（此例中恰好也为真，但不总是如此）\n- 逆否命题 $\\neg Q \\Rightarrow \\neg P$："若 $n^2$ 不是偶数，则 $n$ 不是偶数"——真（与原命题逻辑等价）',
    # 10: Necessary and sufficient
    '**必要与充分条件** "若 $P$ 则 $Q$"中：\n- $P$ 是 $Q$ 的**充分条件（Sufficient Condition）**：$P$ 成立足以保证 $Q$ 成立\n- $Q$ 是 $P$ 的**必要条件（Necessary Condition）**：$Q$ 必须成立才能使 $P$ 成立\n\n例："$n$ 是偶数"是"$n^2$ 是偶数"的充分条件；"$n^2$ 是偶数"是"$n$ 是偶数"的必要条件。',
    # 11: Only if
    '**"Only if"** "$P$ only if $Q$"意思是 $P \\Rightarrow Q$，即"只有在 $Q$ 成立时 $P$ 才成立"。注意："$P$ if $Q$"是 $Q \\Rightarrow P$，而"$P$ only if $Q$"是 $P \\Rightarrow Q$——方向相反！\n\n例："$n$ 是偶数 only if $n^2$ 是偶数"等价于"若 $n$ 是偶数，则 $n^2$ 是偶数"。',
    # 12: Combining connectives
    '**组合联结词** 联结词可以组合使用。例：$P \\wedge (Q \\vee R)$ 表示"$P$ 且（$Q$ 或 $R$）"。括号决定了运算顺序。没有括号时，否定 $\\neg$ 优先级最高，然后是 $\\wedge$，再 $\\vee$，最后 $\\Rightarrow$ 和 $\\Leftrightarrow$。',
    # 13: Exercises
    '**练习** (1) 对命题 $P$："$x > 3$"和 $Q$："$x > 5$"（$x \\in \\mathbb{R}$），判断 $P \\Rightarrow Q$、$Q \\Rightarrow P$、$P \\Leftrightarrow Q$ 的真值。(2) 写出 $P \\Rightarrow Q$ 的逆否命题、逆命题和否命题。',
    # 14: More exercises
    '(3) 找一个使 $P \\Rightarrow Q$ 为真但 $Q \\Rightarrow P$ 为假的例子。(4) 用真值表验证 $P \\Rightarrow Q$ 和 $\\neg Q \\Rightarrow \\neg P$ 逻辑等价。(5) 解释"空虚真"为何是逻辑系统的必要约定，给出一个说明性例子。',
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
