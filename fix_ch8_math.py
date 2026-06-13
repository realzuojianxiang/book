#!/usr/bin/env python3
"""Fix math formula issues in Ch8 combinatorics files."""
import re, os

BASE = os.path.join(r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics", "docs", "part-ii", "ch08-combinatorics")

files = [
    "index.md", "01-introduction.md", "02-basic-counting-principles.md",
    "03-counting-arguments.md", "04-counting-in-two-ways.md",
    "05-selections-with-repetition.md", "06-pigeonhole-principle.md",
    "07-inclusion-exclusion.md",
]

def fix_file(content, fname):
    c = content
    changes = []

    # ---- Fragmented $ signs: |A$\cup B$| -> $|A \cup B|$ ----
    # Pattern: math expression split by $ around an operator
    before = c
    # Fix: x $\in U$ -> $x \in U$ (common in proof text)
    c = c.replace('x $\\in U$', '$x \\in U$')
    if c != before: changes.append('x $\\in U$ -> $x \\in U$'); before = c

    # Fix: k $\in \mathbb{N}$ -> $k \in \mathbb{N}$ (when preceded by Let/For any)
    c = c.replace('Let n $\\in \\mathbb{N}$', 'Let $n \\in \\mathbb{N}$')
    c = c.replace('Let k, n $\\in \\mathbb{N}$', 'Let $k, n \\in \\mathbb{N}$')
    c = c.replace('Let n, k $\\in \\mathbb{N}$', 'Let $n, k \\in \\mathbb{N}$')
    c = c.replace('Let k $\\in \\mathbb{N}$', 'Let $k \\in \\mathbb{N}$')
    c = c.replace('For any n, k $\\in \\mathbb{N}$', 'For any $n, k \\in \\mathbb{N}$')
    c = c.replace('For any n $\\in \\mathbb{N}$', 'For any $n \\in \\mathbb{N}$')
    c = c.replace('Let x, y $\\in \\mathbb{R}', 'Let $x, y \\in \\mathbb{R}$')
    c = c.replace('n $\\in \\mathbb{N}$ be given', '$n \\in \\mathbb{N}$ be given')
    c = c.replace('n, k $\\in \\mathbb{N}$', '$n, k \\in \\mathbb{N}$')
    c = c.replace('n, k $\\in \\mathbb{N} \\cup$', '$n, k \\in \\mathbb{N} \\cup$')
    if c != before: changes.append('Fragmented $ fixed for variable declarations'); before = c

    # Fix: $\in \mathbb{N} with n \geq$ -> $\in \mathbb{N}$ with $n \geq$
    c = c.replace('$\\in \\mathbb{N} with n \\geq$', '$\\in \\mathbb{N}$ with $n \\geq$')
    c = c.replace('$\\in \\mathbb{N} with a + b \\geq k$', '$\\in \\mathbb{N}$ with $a + b \\geq k$')
    c = c.replace('$\\in \\mathbb{N} (with n \\geq$3)', '$\\in \\mathbb{N}$ (with $n \\geq 3$)')
    if c != before: changes.append('Fixed fragmented $ in quantifier+condition'); before = c

    # ---- Set name N -> $\mathbb{N}$ when referencing natural numbers ----
    # "set A = N" -> "set A = $\mathbb{N}$"
    c = c.replace('set A = N and', 'set A = $\\mathbb{N}$ and')
    c = c.replace('partition of N.', 'partition of $\\mathbb{N}$.')
    c = c.replace('partition of N so', 'partition of $\\mathbb{N}$ so')
    c = c.replace('partition of N?', 'partition of $\\mathbb{N}$?')
    c = c.replace('element of N.', 'element of $\\mathbb{N}$.')
    c = c.replace('elements of N.', 'elements of $\\mathbb{N}$.')
    c = c.replace('of N such', 'of $\\mathbb{N}$ such')
    c = c.replace('Consider the set N', 'Consider the set $\\mathbb{N}$')
    if c != before: changes.append('Bare N -> $\\mathbb{N}$ for natural numbers set'); before = c

    # ---- Fix: $(N \cup${0}) -> $(\mathbb{N} \cup \{0\})$ ----
    c = c.replace('$(N \\cup${0})$', '$(\\mathbb{N} \\cup \\{0\\})$')
    c = c.replace('$\\in(N \\cup${0})', '$\\in(\\mathbb{N} \\cup \\{0\\})')
    c = c.replace('$(N \\cup$\\{0\\})$', '$(\\mathbb{N} \\cup \\{0\\})$')
    if c != before: changes.append('Fixed $(N \\cup${0})$ -> $(\\mathbb{N} \\cup \\{0\\})$'); before = c

    # ---- Fix: broken bigcup notation ----
    c = c.replace('[ i$\\in I$ Si = A', '$\\bigcup_{i \\in I} S_i = A$')
    c = c.replace('[ i\\in I Si = A', '$\\bigcup_{i \\in I} S_i = A$')
    c = c.replace('[ i$\\in \\mathbb{N}$ Si = N', '$\\bigcup_{i \\in \\mathbb{N}} S_i = \\mathbb{N}$')
    if c != before: changes.append('Fixed broken bigcup notation'); before = c

    # ---- Fix: more specific fragmented $ in 07-inclusion-exclusion.md ----
    c = c.replace('$\\cup A2 \\cup \\cdot \\cdot \\cdot \\cup A$n)', '$\\cup A_2 \\cup \\cdots \\cup A_n)$')
    c = c.replace('\\ i$\\in \\emptyset$ Ai = U', '$\\bigcap_{i \\in \\emptyset} A_i = U$')
    c = c.replace('x $\\notin Ai for every i \\in$', '$x \\notin A_i$ for every $i \\in$')
    c = c.replace('i $\\in S$ such that j $\\notin B$', '$i \\in S$ such that $j \\notin B$')
    c = c.replace('|AH $\\cap A$S|', '$|A_H \\cap A_S|$')
    c = c.replace('|AH $\\cap AS \\cap A$D|', '$|A_H \\cap A_S \\cap A_D|$')
    c = c.replace('$\\cap A$C', '$\\cap A_C$')
    c = c.replace('$\\cap A$D', '$\\cap A_D$')
    c = c.replace('S $\\subseteq$[n]', '$S \\subseteq [n]$')
    c = c.replace('S $\\subseteq T$k,n', '$S \\subseteq T_{k,n}$')
    c = c.replace('T $\\subseteq$[n]', '$T \\subseteq [n]$')
    c = c.replace('$\\subseteq$[n]', '$\\subseteq [n]$')
    c = c.replace('\\ i$\\in S$ Ai = S(k)', '$\\bigcap_{i \\in S} A_i = S(k)$')
    if c != before: changes.append('Fixed fragmented $ in inclusion-exclusion'); before = c

    # ---- Fix: bare math in 02-basic-counting-principles.md ----
    # Sum/product notation
    c = c.replace('X i$\\in$[n]', '$\\sum_{i \\in [n]}$')
    c = c.replace('X i$\\in [n]$', '$\\sum_{i \\in [n]}$')
    c = c.replace('Y i$\\in [n]$', '$\\prod_{i \\in [n]}$')
    c = c.replace('Y k$\\in[n] k =', '$\\prod_{k \\in [n]} k =')
    c = c.replace('X k$\\in[n] |Ti|', '$\\sum_{k \\in [n]} |T_k|$')
    c = c.replace('Y i$\\in$[n] |Ti|', '$\\prod_{i \\in [n]} |T_i|$')
    c = c.replace('Y i$\\in$[n] wi', '$\\prod_{i \\in [n]} w_i$')
    c = c.replace('X i\\in I Si', '$\\bigcup_{i \\in I} S_i$')
    if c != before: changes.append('Fixed broken sum/product notation'); before = c

    # ---- Fix: bare \subset, \subseteq etc. in English text ----
    # These are less dangerous but still odd-looking

    # ---- Fix: $\\cup A$D -> $\\cup A_D$ in 07 ----
    if c != before: changes.append('Fixed broken set name in 07'); before = c

    # ---- Fix: Chinese blocks ----
    # Fix \in N -> \in \mathbb{N} in Chinese blocks
    c = c.replace('\\in N \\cup', '\\in \\mathbb{N} \\cup')
    c = c.replace('\\in N \\times', '\\in \\mathbb{N} \\times')
    c = c.replace('\\in N,', '\\in \\mathbb{N},')
    if c != before: changes.append('Fixed \\in N -> \\in \\mathbb{N} in Chinese blocks'); before = c

    # Fix C \subset A -> C \subset A (already fine as LaTeX, but check if needs $)
    c = c.replace('C \\subset A', '$C \\subset A$')
    c = c.replace('A \\to B', '$A \\to B$')
    c = c.replace('B \\to A', '$B \\to A$')
    if c != before: changes.append('Fixed bare relations in Chinese blocks'); before = c

    # Fix \frac{p}{q} not wrapped -> already should be in $...$
    # Fix \mathbb{R} not at start of line in Chinese blocks
    c = c.replace('\\mathbb{R} 不可数', '$\\mathbb{R}$ 不可数')
    c = c.replace('\\mathbb{R} 与', '$\\mathbb{R}$ 与')
    if c != before: changes.append('Fixed bare \\mathbb{} in Chinese'); before = c

    return c, changes

total = 0
for fname in files:
    fp = os.path.join(BASE, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    new, changes = fix_file(content, fname)
    if new != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f"\n=== {fname}: {len(changes)} fixes ===")
        for ch in changes:
            print(f"  - {ch}")
        total += len(changes)
    else:
        print(f"\n=== {fname}: no changes ===")

print(f"\nTotal fixes: {total}")
