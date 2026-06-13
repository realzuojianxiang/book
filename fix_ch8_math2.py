#!/usr/bin/env python3
"""Ch8 math fix pass 2: fix remaining fragmented $ and bare math."""
import re, os

BASE = os.path.join(r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics", "docs", "part-ii", "ch08-combinatorics")

def fix_file(content, fname):
    c = content
    changes = []

    # ========== 02-basic-counting-principles.md ==========
    # Fix: i $\in$[n] -> i $\in [n]$
    c = c.replace('i $\\in$[n]', '$i \\in [n]$')
    # Fix: i $\in I$ in definition text - merge with surrounding math
    c = c.replace('(defined for every i $\\in I$)', '(defined for every $i \\in I$)')
    # Fix: S = {Si | i $\in$[n]} -> $S = \{S_i \mid i \in [n]\}$
    c = c.replace('S = {Si | i $\\in$[n]}', '$S = \\{S_i \\mid i \\in [n]\\}$')

    # Fix: Let k, n $\in \mathbb{N} with n \geq k$ -> Let $k, n \in \mathbb{N}$ with $n \geq k$
    c = c.replace('k, n $\\in \\mathbb{N} with n \\geq k$', '$k, n \\in \\mathbb{N}$ with $n \\geq k$')
    # Fix: $\in \mathbb{N}$. -> standalone, but need to fix when it's part of larger expression
    c = c.replace('n $\\in \\mathbb{N}$. Suppose', '$n \\in \\mathbb{N}$. Suppose')

    # Fix: bare math conditions in definitions - "with n \geq k"
    # $(N \cup${0}) already fixed in pass 1

    # ========== 03-counting-arguments.md ==========
    # Fix: $\forall i. ai \in$[k] -> $\forall i. a_i \in [k]$
    c = c.replace('$\\forall i. ai \\in$[k]', '$\\forall i. a_i \\in [k]$')
    # Fix: [k -1] $\cup${0} -> $[k-1] \cup \{0\}$
    c = c.replace('[k -1] $\\cup${0}', '$[k-1] \\cup \\{0\\}$')
    c = c.replace('$\\cup${0}', '$\\cup \\{0\\}$')
    # Fix: $\in(\mathbb{N} \cup \{0\})2 -> $\in (\mathbb{N} \cup \{0\})^2$
    c = c.replace('$\\in(\\mathbb{N} \\cup \\{0\\})2', '$\\in (\\mathbb{N} \\cup \\{0\\})^2')
    # Fix: $\in T$k,n -> $\in T_{k,n}$
    c = c.replace('$\\subseteq T$k,n', '$\\subseteq T_{k,n}$')

    # Fix: N \cup$\\{0\\}$ patterns
    c = c.replace('\\mathbb{N} \\cup$\\{0\\}', '\\mathbb{N} \\cup \\{0\\}')

    # Fix: \forall k $\in \mathbb{N}$. -> $\\forall k \\in \\mathbb{N}$.
    c = c.replace('\\forall k $\\in \\mathbb{N}$', '$\\forall k \\in \\mathbb{N}$')

    # ========== 04-counting-in-two-ways.md ==========
    # Fix: A = {T $\subseteq$[n] -> $A = \{T \subseteq [n]$
    c = c.replace('A = {T $\\subseteq$[n]', '$A = \\{T \\subseteq [n]$')
    # Fix: B = {T $\subseteq$[n] -> $B = \{T \subseteq [n]$
    c = c.replace('B = {T $\\subseteq$[n]', '$B = \\{T \\subseteq [n]$')
    # Fix various $ \subseteq[n]$ -> $ \subseteq [n]$
    c = c.replace('$\\subseteq$[n]', '$\\subseteq [n]$')
    c = c.replace('$\\subseteq$[n + 1]', '$\\subseteq [n+1]$')
    c = c.replace('$\\subseteq$[n + 1]', '$\\subseteq [n+1]$')

    # Fix: T $\in S$ -> $T \in S$
    c = c.replace('T $\\in S$', '$T \\in S$')
    c = c.replace('T $\\in B$', '$T \\in B$')
    c = c.replace('T $\\in A$', '$T \\in A$')
    # Fix: x $\in T$ -> $x \in T$
    c = c.replace('x $\\in T$', '$x \\in T$')

    # Fix: A $\cap B = \emptyset$ -> $A \cap B = \emptyset$
    c = c.replace('A $\\cap B = \\emptyset$', '$A \\cap B = \\emptyset$')
    c = c.replace('A $\\cup B$', '$A \\cup B$')
    c = c.replace('S $= A \\cup B$', '$S = A \\cup B$')

    # Fix: $\\cap Sj = \\emptyset$ -> $\cap S_j = \emptyset$
    c = c.replace('$\\cap Sj = \\emptyset$', ' $\\cap S_j = \\emptyset$')
    c = c.replace('Si $\\cap Sj$', '$S_i \\cap S_j$')
    c = c.replace('Si $\\cap Sj$', '$S_i \\cap S_j$')

    # Fix: |A| + |B| etc without $ in proof text
    # Actually these are very contextual, skip for now

    # ========== 05-selections-with-repetition.md ==========
    # Fix $\\in$[n] -> $\in [n]$
    c = c.replace('$\\in$[n]', '$\\in [n]$')
    c = c.replace('$\\in$[k]', '$\\in [k]$')

    # Fix: $\cdot \cdot \cdot$ -> $\cdots$
    c = c.replace('$\\cdot \\cdot \\cdot$', '$\\cdots$')
    # Fix bare \cdot \cdot \cdot -> $\cdots$
    c = c.replace('\\cdot \\cdot \\cdot', '\\cdots')

    # Fix: xi $\in \mathbb{N} \cup${0} -> $x_i \in \mathbb{N} \cup \{0\}$
    c = c.replace('xi $\\in \\mathbb{N} \\cup${0}', '$x_i \\in \\mathbb{N} \\cup \\{0\\}$')
    c = c.replace('xi $\\in \\mathbb{N} \\cup$\\{0\\}', '$x_i \\in \\mathbb{N} \\cup \\{0\\}$')
    # Fix: \forall i \in[k]. xi $\in \mathbb{N} \cup${0}
    c = c.replace('xi $\\in \\mathbb{N}$\\cup$\\{0\\}$', '$x_i \\in \\mathbb{N} \\cup \\{0\\}$')

    # Fix: $\\geq$ z/n -> $\geq z/n$
    c = c.replace('$\\geq z/n$', '$\\geq z/n$')  # already ok
    c = c.replace('xi $\\geq z$/n', '$x_i \\geq z/n$')
    c = c.replace('xi $< z$/n', '$x_i < z/n$')

    # ========== 06-pigeonhole-principle.md ==========
    # Fix: S $\subseteq[2n]$ -> $S \subseteq [2n]$
    c = c.replace('S $\\subseteq[2n]$', '$S \\subseteq [2n]$')
    # Fix: x, y $\in S -> $x, y \in S$
    c = c.replace('x, y $\\in S$', '$x, y \\in S$')

    # Fix: $\\leq \\sqrt$ -> $\leq \sqrt$
    c = c.replace('d $\\leq \\sqrt$', '$d \\leq \\sqrt{2}/2$ km')

    # Fix: $\\geq 2$ -> already ok

    # ========== 07-inclusion-exclusion.md ==========
    # Fix: $\subseteq U$ -> $\subseteq U$
    c = c.replace('$\\subseteq U$', '$\\subseteq U$')  # already ok
    # Fix: $\\subseteq[n]$ -> $\subseteq [n]$
    c = c.replace('$\\subseteq$[n]', '$\\subseteq [n]$')
    # Fix: $\\subseteq[n]$ -> $\subseteq [n]$
    c = c.replace('$\\subseteq[n]$', '$\\subseteq [n]$')

    # Fix: S $\subseteq$[n] -> $S \subseteq [n]$
    c = c.replace(' S $\\subseteq$[n]', ' $S \\subseteq [n]$')

    # Fix: i $\in S$ -> $i \in S$
    c = c.replace('i $\\in S$', '$i \\in S$')

    # Fix: $\\notin Ai -> \notin A_i$
    c = c.replace('$\\notin Ai for every i $\\in$', '$\\notin A_i$ for every $i \\in$')
    # Fix: j $\\in B$ -> $j \in B$
    c = c.replace('j $\\in B$', '$j \\in B$')
    c = c.replace('j $\\notin B$', '$j \\notin B$')
    c = c.replace('j $\\in S$', '$j \\in S$')
    c = c.replace('j $\\notin S$', '$j \\notin S$')

    # Fix: $\\subseteq [n]$ (already potentially ok)

    # Fix: |U -(A1 $\cup A2 ... -> $|U - (A_1 \cup A_2 ...$
    # Already did one in pass 1, let me check for remaining
    c = c.replace('|U -(A1 $\\cup A_2', '$|U -(A_1 \\cup A_2')

    # ========== General fixes across all files ==========
    # Fix: $\\in \\mathbb{N} \\cup$\\{0\\}$ -> proper
    c = c.replace('$\\in \\mathbb{N} \\cup$\\{0\\}$', '$\\in \\mathbb{N} \\cup \\{0\\}$')
    c = c.replace('$\\in \\mathbb{N}$\\cup$\\{0\\}$', '$\\in \\mathbb{N} \\cup \\{0\\}$')

    # Fix: $\mathbb{N}$\cup$\{0\}$ -> $\mathbb{N} \cup \{0\}$
    c = c.replace('\\mathbb{N}$\\cup$\\{0\\}', '\\mathbb{N} \\cup \\{0\\}')

    # Fix common fragmented $ around operators
    # $\\cap$ -> proper - but need to check context

    # ========== Fix 01-introduction.md ==========
    # Fix: $|A$\cup B$| -> $|A \cup B|$
    c = c.replace('|A$\\cup B$|', '$|A \\cup B|$')
    # Fix: x $\cdot y = y \cdot$ x -> $x \cdot y = y \cdot x$
    c = c.replace('x $\\cdot y = y \\cdot$ x', '$x \\cdot y = y \\cdot x$')
    # Fix: $A \cap B = $\emptyset$ patterns
    c = c.replace('A\\cap B = $\\emptyset$', '$A \\cap B = \\emptyset$')

    # Fix: x, y $\\in \\mathbb{R}$ -> $x, y \in \mathbb{R}$
    c = c.replace('x, y $\\in \\mathbb{R}$', '$x, y \\in \\mathbb{R}$')

    return c, changes

total = 0
for fname in ["index.md", "01-introduction.md", "02-basic-counting-principles.md",
              "03-counting-arguments.md", "04-counting-in-two-ways.md",
              "05-selections-with-repetition.md", "06-pigeonhole-principle.md",
              "07-inclusion-exclusion.md"]:
    fp = os.path.join(BASE, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    new, changes = fix_file(content, fname)
    if new != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f"=== {fname}: changed ===")
        total += 1
    else:
        print(f"=== {fname}: no changes ===")

print(f"\nFiles changed: {total}")
