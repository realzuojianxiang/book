#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate all TODOs in ch05/03-other-variants.md"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = 'docs/part-i/ch05-rigorous-induction/03-other-variants.md'
with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read()

todo_marker = 'TODO: 待翻译'

translations = [
    '归纳法的其他变体（Other Variants of Induction）——除了常规归纳法，还有多种变形适用于不同场景。本节讨论常见的几种。',
    '**起始值不为 1** 有时命题 $P(n)$ 仅在 $n \\geq n_0$ 时有意义。此时只需将基例改为 $P(n_0)$，归纳步假设 $P(k)$ 对某个 $k \\geq n_0$ 成立，证明 $P(k+1)$。结论是 $\\forall n \\geq n_0.\\, P(n)$。',
    '**例** 设 $P(n)$ 为"$n! > 2^n$（对 $n \\geq 4$）"。基例 $P(4)$：$24 > 16$ ✓。归纳步：设 $k \\geq 4$ 且 $k! > 2^k$，则 $(k+1)! = (k+1) \\cdot k! > (k+1) \\cdot 2^k \\geq 5 \\cdot 2^k > 2 \\cdot 2^k = 2^{k+1}$。故 $\\forall n \\geq 4.\\, n! > 2^n$。',
    '**递减归纳法（Downward Induction）** 有时需要从大到小证明。设 $P(n)$ 对某个 $n_0$ 成立，且 $P(k) \\Rightarrow P(k-1)$。则 $\\forall n \\leq n_0.\\, P(n)$。',
    '**例** 用递减归纳法证明：对所有 $n \\leq 0$，$n \\leq 0$。（举例说明递减归纳法的逻辑结构。）',
    '**多重基例** 有时归纳步需要多个前置命题为真，因此需要多个基例来"启动"归纳链。',
    '**例** 设 $P(n)$ 为"用 3 分和 5 分邮票可以凑出 $n$ 分邮资（对 $n \\geq 8$）"。验证基例：$P(8)$（3+5）✓，$P(9)$（3+3+3）✓，$P(10)$（5+5）✓。归纳步：设 $k \\geq 10$，$P(k)$ 成立。由 $P(k-2)$ 成立（因为 $k-2 \\geq 8$）加一枚 3 分邮票即得 $P(k+1)$？不对——只需直接利用 $P(k-2)$ 加一个 3 分即可。所以 $\\forall n \\geq 8.\\, P(n)$。',
    '注意：此例中归纳步利用的不是 $P(k)$ 而是 $P(k-2)$，因此需要验证多个基例（8、9、10）以确保归纳链不断裂。',
    '**向后的归纳步** 有时归纳步的证明并不是从前项推后项，而是从结论反推。这在某些涉及不等式或存在性证明时很有用。',
    '**问题与练习** (1) 对以下每个命题，确定适当的起始值并用归纳法证明：(a) $2^n > n^2$（对充分大的 $n$）(b) $n^2 + n$ 是偶数（对所有 $n \\in \\mathbb{N}$）',
    '(2) 用多重基例归纳法证明：任何 $n \\geq 12$ 可以写成 $3a + 5b$（$a, b \\in \\mathbb{N} \\cup \\{0\\}$）的形式。',
    '(3) 解释为什么在常规归纳法中只需一个基例，而在某些变体中需要多个基例。给出一个具体的例子。',
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
