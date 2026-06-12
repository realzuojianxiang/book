#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate all TODOs in ch06/04-equivalence-relations.md"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = 'docs/part-ii/ch06-relations-modular-arithmetic/04-equivalence-relations.md'
with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read()

todo_marker = 'TODO: 待翻译'

translations = [
    '**等价关系（Equivalence Relations）** 等价关系是一种同时满足自反性、对称性和传递性的关系。它是数学中最基本的关系类型之一，将集合划分为不相交的等价类。',
    '**定义** 集合 $S$ 上的关系 $R$ 称为**等价关系（Equivalence Relation）**，若它满足：\n- **自反性（Reflexivity）**：$\\forall x \\in S.\\, xRx$\n- **对称性（Symmetry）**：$\\forall x, y \\in S.\\, xRy \\Rightarrow yRx$\n- **传递性（Transitivity）**：$\\forall x, y, z \\in S.\\, (xRy \\wedge yRz) \\Rightarrow xRz$',
    '**例** 相等关系 $=$ 是任何集合上的等价关系：自反（$x=x$），对称（$x=y \\Rightarrow y=x$），传递（$x=y \\wedge y=z \\Rightarrow x=z$）。',
    '**例** "同余模 $n$"关系 $\\equiv_n$ 是 $\\mathbb{Z}$ 上的等价关系：自反（$a \\equiv a \\pmod{n}$），对称（$a \\equiv b \\Rightarrow b \\equiv a \\pmod{n}$），传递（$a \\equiv b$ 且 $b \\equiv c$ $\\Rightarrow$ $a \\equiv c \\pmod{n}$）。',
    '**反例** "$\\leq$"不是等价关系——不满足对称性（$1 \\leq 2$ 但 $2 \\not\\leq 1$）。"$\\neq$"也不是——不满足自反性（$x \\neq x$ 为假）且不满足传递性（$1 \\neq 2$ 且 $2 \\neq 1$ 但 $1 \\neq 1$ 为假）。',
    '**等价类（Equivalence Class）** 设 $R$ 是 $S$ 上的等价关系，$x \\in S$。$x$ 的等价类定义为：$[x]_R = \\{y \\in S \\mid yRx\\}$。即所有与 $x$ 有关系 $R$ 的元素的集合。',
    '**例** 在 $\\equiv_3$ 下，$[1]_{\\equiv_3} = \\{\\ldots, -5, -2, 1, 4, 7, \\ldots\\}$。注意 $[1] = [4] = [7]$——同一等价类的不同代表元给出相同的等价类。',
    '**关键性质** 等价关系将集合划分为不相交的等价类：（1）$x \\in [x]$（自反性保证）；（2）$xRy \\Leftrightarrow [x] = [y]$；（3）若 $[x] \\neq [y]$，则 $[x] \\cap [y] = \\emptyset$。',
    '**证明 $xRy \\Leftrightarrow [x] = [y]$** "$\\Rightarrow$"：设 $xRy$，任取 $z \\in [x]$，则 $zRx$，由对称性 $xRy$，再由传递性 $zRy$，故 $z \\in [y]$，从而 $[x] \\subseteq [y]$。类似得 $[y] \\subseteq [x]$。"$\\Leftarrow$"：若 $[x] = [y]$，由 $y \\in [y]$（自反性）得 $y \\in [x]$，即 $yRx$，再由对称性 $xRy$。',
    '**划分与等价关系的对应** 给定等价关系 $R$，其等价类构成 $S$ 的一个划分。反之，给定 $S$ 的一个划分，由"在同一部分中"定义的关系是等价关系。这是等价关系与划分之间的一一对应。',
    '**例** 在 $\\mathbb{Z}$ 上，$\\equiv_2$ 将整数划分为两个等价类：$[0] = \\{$偶数$\\}$ 和 $[1] = \\{$奇数$\\}$。这构成 $\\mathbb{Z}$ 的一个划分。',
    '**例** 在 $\\mathbb{Z}$ 上，$\\equiv_n$ 将整数划分为 $n$ 个等价类：$[0], [1], \\ldots, [n-1]$。这就是模 $n$ 剩余类的来源。',
    '**商集（Quotient Set）** $S$ 模等价关系 $R$ 的商集定义为 $S/R = \\{[x]_R \\mid x \\in S\\}$，即所有等价类的集合。$|S/R|$ 是等价类的个数。',
    '**例** $\\mathbb{Z}/\\!\\equiv_2$ 有 2 个元素（偶数类和奇数类）。$\\mathbb{Z}/\\!\\equiv_n$ 有 $n$ 个元素。',
    '**练习** (1) 验证"在城市中住在同一条街上"是人的集合上的等价关系。(2) 证明空关系不是等价关系（除非集合为空）。(3) 设 $R = \\{(a,b) \\in \\mathbb{Z} \\times \\mathbb{Z} \\mid a - b \\text{ 是 5 的倍数}\\}$。证明 $R$ 是等价关系，并描述其等价类。',
    '(4) 设 $S = \\{1,2,3,4,5,6\\}$ 和划分 $\\{\\{1,3,5\\}, \\{2,4,6\\}\\}$。写出对应的等价关系。(5) 证明：若 $R$ 是等价关系，则 $[x] = [y]$ 或 $[x] \\cap [y] = \\emptyset$。',
    '(6) 考虑 $\\mathbb{R}$ 上的关系 $R$：$xRy$ 当且仅当 $x - y \\in \\mathbb{Z}$。证明 $R$ 是等价关系，并描述其等价类。',
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
