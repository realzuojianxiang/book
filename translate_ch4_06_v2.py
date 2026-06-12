#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate all TODOs in ch04/06-logical-equivalence.md"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = 'docs/part-i/ch04-logic/06-logical-equivalence.md'
with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read()

todo_marker = 'TODO: 待翻译'

translations = [
    '逻辑等价（Logical Equivalence）两个命题 $P$ 和 $Q$ 逻辑等价，记作 $P \\Leftrightarrow Q$，意味着它们对所有可能的赋值具有相同的真值。本节讨论如何用真值表和逻辑规则来判定等价性。',
    '**用真值表验证等价** 要证 $P \\Leftrightarrow Q$，构造包含 $P$ 和 $Q$ 的真值表，验证两列完全相同。这是最直接但有时最繁琐的方法。',
    '**例** 验证 $\\neg(P \\wedge Q) \\Leftrightarrow (\\neg P \\vee \\neg Q)$（德摩根律之一）：\n\n| $P$ | $Q$ | $P \\wedge Q$ | $\\neg(P \\wedge Q)$ | $\\neg P$ | $\\neg Q$ | $\\neg P \\vee \\neg Q$ |\n|---|---|---|---|---|---|---|\n| T | T | T | F | F | F | F |\n| T | F | F | T | F | T | T |\n| F | T | F | T | T | F | T |\n| F | F | F | T | T | T | T |\n\n两侧完全相同，故等价。',
    '**重要等价律**\n\n**德摩根律（De Morgan\'s Laws）：**\n- $\\neg(P \\wedge Q) \\Leftrightarrow \\neg P \\vee \\neg Q$\n- $\\neg(P \\vee Q) \\Leftrightarrow \\neg P \\wedge \\neg Q$\n\n**条件语句等价：** $P \\Rightarrow Q \\Leftrightarrow \\neg P \\vee Q \\Leftrightarrow \\neg Q \\Rightarrow \\neg P$',
    '**分配律（Distributive Laws）：**\n- $P \\wedge (Q \\vee R) \\Leftrightarrow (P \\wedge Q) \\vee (P \\wedge R)$\n- $P \\vee (Q \\wedge R) \\Leftrightarrow (P \\vee Q) \\wedge (P \\vee R)$',
    '**结合律（Associative Laws）：**\n- $(P \\wedge Q) \\wedge R \\Leftrightarrow P \\wedge (Q \\wedge R)$\n- $(P \\vee Q) \\vee R \\Leftrightarrow P \\vee (Q \\vee R)$\n\n**交换律（Commutative Laws）：**\n- $P \\wedge Q \\Leftrightarrow Q \\wedge P$\n- $P \\vee Q \\Leftrightarrow Q \\vee P$',
    '**双重否定律（Double Negation）：** $\\neg(\\neg P) \\Leftrightarrow P$\n\n**幂等律（Idempotent Laws）：**\n- $P \\wedge P \\Leftrightarrow P$\n- $P \\vee P \\Leftrightarrow P$\n\n**恒真律与恒假律：**\n- $P \\vee \\neg P \\Leftrightarrow \\text{True}$（排中律）\n- $P \\wedge \\neg P \\Leftrightarrow \\text{False}$（矛盾律）',
    '**利用等价律化简** 等价律允许我们将复杂命题逐步化简。这比真值表更高效，尤其当变量很多时。',
    '**例** 化简 $\\neg((P \\wedge Q) \\vee (\\neg P \\wedge Q))$：\n\n$= \\neg(P \\wedge Q) \\wedge \\neg(\\neg P \\wedge Q)$（德摩根律）\n$= (\\neg P \\vee \\neg Q) \\wedge (P \\vee \\neg Q)$（德摩根律）\n$= ((\\neg P \\vee P) \\vee \\neg Q)$（分配律方向）\n$= \\text{True} \\wedge \\neg Q$（排中律）\n$= \\neg Q$\n\n结果：$\\neg Q$',
    '**用等价律证明逆否等价** 我们可以用等价律逐步变形来证明 $P \\Rightarrow Q \\Leftrightarrow \\neg Q \\Rightarrow \\neg P$：\n\n$P \\Rightarrow Q \\Leftrightarrow \\neg P \\vee Q$（条件等价）\n$\\Leftrightarrow Q \\vee \\neg P$（交换律）\n$\\Leftrightarrow \\neg(\\neg Q) \\vee \\neg P$（双重否定）\n$\\Leftrightarrow \\neg Q \\Rightarrow \\neg P$（条件等价）',
    '**条件语句的否定** 我们来推导 $\\neg(P \\Rightarrow Q)$ 的等价形式：\n\n$\\neg(P \\Rightarrow Q) \\Leftrightarrow \\neg(\\neg P \\vee Q)$（条件等价）\n$\\Leftrightarrow P \\wedge \\neg Q$（德摩根律 + 双重否定）\n\n即：否定条件语句得到"假设成立但结论不成立"。',
    '**双条件语句的否定** $\\neg(P \\Leftrightarrow Q)$：\n\n$\\Leftrightarrow \\neg((P \\Rightarrow Q) \\wedge (Q \\Rightarrow P))$\n$\\Leftrightarrow \\neg(P \\Rightarrow Q) \\vee \\neg(Q \\Rightarrow P)$（德摩根律）\n$\\Leftrightarrow (P \\wedge \\neg Q) \\vee (Q \\wedge \\neg P)$\n\n即"恰好一个成立，另一个不成立"——这正是"异或"（XOR）的定义。',
    '**量词与联结词的交互** 量词和联结词之间也有重要等价：\n\n- $\\neg(\\forall x.\\, P(x)) \\Leftrightarrow \\exists x.\\, \\neg P(x)$\n- $\\neg(\\exists x.\\, P(x)) \\Leftrightarrow \\forall x.\\, \\neg P(x)$\n\n这是前几节讨论过的量词否定规则，用等价的语言重述。',
    '**练习** (1) 用真值表验证 $P \\Rightarrow Q \\Leftrightarrow \\neg P \\vee Q$。(2) 用等价律化简 $\\neg(P \\vee (Q \\wedge \\neg P))$。',
    '(3) 证明 $(P \\Rightarrow Q) \\wedge (Q \\Rightarrow P) \\Leftrightarrow P \\Leftrightarrow Q$。(4) 写出 $\\neg(P \\Leftrightarrow Q)$ 的最简等价形式。',
    '(5) 用等价律证明 $\\neg(\\neg P \\vee Q) \\Leftrightarrow P \\wedge \\neg Q$。(6) 解释为什么 $P \\Rightarrow Q$ 与 $Q \\Rightarrow P$ 不等价，并给出一个具体例子。',
    '(7) 化简 $\\neg((P \\wedge Q) \\Rightarrow R)$。(8) 证明分配律 $P \\wedge (Q \\vee R) \\Leftrightarrow (P \\wedge Q) \\vee (P \\wedge R)$。',
    '(9) 化简 $\\neg(P \\Leftrightarrow Q)$。(10) 什么条件下 $P \\Rightarrow Q$ 与 $Q \\Rightarrow P$ 同时为真？这说明了什么？',
    '**补充等价律**\n\n**吸收律（Absorption Laws）：**\n- $P \\wedge (P \\vee Q) \\Leftrightarrow P$\n- $P \\vee (P \\wedge Q) \\Leftrightarrow P$\n\n**蕴含律：** $P \\Rightarrow Q \\Leftrightarrow \\neg Q \\Rightarrow \\neg P$\n\n**逆否等价的推论：** 条件语句的否定 $\\neg(P \\Rightarrow Q) \\Leftrightarrow P \\wedge \\neg Q$ 是证明中反证法的理论基础。',
    '总结：逻辑等价的判定有两种方法——真值表（穷举但机械）和等价律化简（快速但需要技巧）。熟练掌握两种方法对证明写作至关重要。',
    '最后的综合练习：(11) 设 $P$ 为"$n$ 是偶数"，$Q$ 为"$2n$ 是偶数"。判断 $P \\Rightarrow Q$、$Q \\Rightarrow P$、$P \\Leftrightarrow Q$ 是否为真，并解释。(12) 化简 $\\neg((\\neg P \\wedge Q) \\vee (P \\wedge \\neg Q))$。',
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
