#!/usr/bin/env python3
"""Ch8 math fix pass 3: deeper fixes for fragmented $ and bare math."""
import re, os

BASE = os.path.join(r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics", "docs", "part-ii", "ch08-combinatorics")

def fix_file(content, fname):
    c = content
    before = c

    # ====== Fix I = \mathbb{N} (standalone N as natural numbers set) ======
    # In 02: "I = N." -> "I = $\mathbb{N}$."
    c = c.replace('I = N.', 'I = $\\mathbb{N}$.')
    c = c.replace('I = N and', 'I = $\\mathbb{N}$ and')

    # ====== Fix bare math in Definition/Proposition/Proof blocks ======
    # Pattern: bare \subseteq, \in, \cap, \cup, \emptyset, \neq outside $...$

    # In 02: "i \in I, Si \subseteq A" -> needs $ wrapping
    c = c.replace(' i \\in I, Si \\subseteq A', ' $i \\in I$, $S_i \\subseteq A$')
    c = c.replace(' i, j \\in I with i \\neq j', ' $i, j \\in I$ with $i \\neq j$')
    c = c.replace('Si \\cap Sj = \\emptyset', '$S_i \\cap S_j = \\emptyset$')
    c = c.replace('S1 \\cap S2 = \\emptyset', '$S_1 \\cap S_2 = \\emptyset$')
    c = c.replace('S1 \\cup S2 = A', '$S_1 \\cup S_2 = A$')
    c = c.replace('x \\notin S1 and x $\\notin S$', '$x \\notin S_1$ and $x \\notin S$')
    c = c.replace('2i -1, 2i \\in Si', '$2i-1, 2i \\in S_i$')

    # In 02 proof: "i, j $\\in \\mathbb{N}$ with i \\neq j such that Si \\cap Sj \\neq \\emptyset"
    c = c.replace('with i \\neq j such that Si \\cap Sj \\neq \\emptyset',
                   'with $i \\neq j$ such that $S_i \\cap S_j \\neq \\emptyset$')

    # ====== Fix 02 summation/product notation ======
    # "n = 2k" type bare math
    c = c.replace('that n = 2k.', 'that $n = 2k$.')
    c = c.replace('such that n = 2ℓ-1.', 'such that $n = 2\\ell-1$.')
    c = c.replace('n \\in [ i$\\in I$ Si', '$n \\in \\bigcup_{i \\in I} S_i$')

    # ====== Fix 04 proof blocks ======
    # Multiple bare references: |A|, |B|, |S| etc. in proof context
    # "A \\cap B = \\emptyset since" -> "$A \\cap B = \\emptyset$ since"

    # ====== Fix 05 bare math ======
    # Many bare math expressions in this file

    # ====== Fix 06 broken math ======
    # Line 14: "⌈n/k⌉" in English text - already unicode
    c = c.replace('\\leq\\sqrt$', '\\leq \\sqrt{2}/2$ km')

    # ====== Fix 07 broken summation (X) ======
    # "X S$\\subseteq [n]$" -> this is the summation over subsets
    c = c.replace('X S$\\subseteq [n]$', '$\\sum_{S \\subseteq [n]}$')
    c = c.replace('X S\\subseteq [n]$', '$\\sum_{S \\subseteq [n]}$')

    # "n X k=0" -> "$\\sum_{k=0}^{n}$"
    c = c.replace(' n X k=0 ', ' $\\sum_{k=0}^{n}$ ')
    c = c.replace('n X k=0 ', '$\\sum_{k=0}^{n}$ ')
    c = c.replace(' n X i=0 ', ' $\\sum_{i=0}^{n}$ ')
    c = c.replace('n X i=0 ', '$\\sum_{i=0}^{n}$ ')
    c = c.replace(' n X i=1 ', ' $\\sum_{i=1}^{n}$ ')
    c = c.replace('n X i=1 ', '$\\sum_{i=1}^{n}$ ')
    c = c.replace(' k X i=1 ', ' $\\sum_{i=1}^{k}$ ')
    c = c.replace('k X i=1 ', '$\\sum_{i=1}^{k}$ ')
    c = c.replace(' n+1 X j=1 ', ' $\\sum_{j=1}^{n+1}$ ')
    c = c.replace('n+1 X j=1 ', '$\\sum_{j=1}^{n+1}$ ')
    c = c.replace(' n X ℓ=3 ', ' $\\sum_{\\ell=3}^{n}$ ')
    c = c.replace('n X ℓ=3 ', '$\\sum_{\\ell=3}^{n}$ ')
    c = c.replace(' Pn i=k ', ' $\\sum_{i=k}^{n}$ ')
    c = c.replace('Pn i=k ', '$\\sum_{i=k}^{n}$ ')

    # Fix: "⌊n/2⌋ X k=0" -> "$\sum_{k=0}^{\lfloor n/2 \rfloor}$"
    c = c.replace('⌊n/2⌋ X k=0 ', '$\\sum_{k=0}^{\\lfloor n/2 \\rfloor}$ ')
    c = c.replace('⌈n/2⌉-1 X k=0 ', '$\\sum_{k=0}^{\\lceil n/2 \\rceil - 1}$ ')

    # ====== Fix Chinese blocks: \in N -> \in \mathbb{N} ======
    # This pattern appears in Chinese blocks where N should be \mathbb{N}
    c = c.replace('从 $[n]$ 中选', '从 $[n]$ 中选')  # ok already

    # Fix: $x_i \in N$ -> $x_i \in \mathbb{N}$
    # Already fixed in pass 1 but let me check for remaining
    c = c.replace('\\in N \\cup', '\\in \\mathbb{N} \\cup')
    c = c.replace('\\in N, ', '\\in \\mathbb{N}, ')
    c = c.replace('\\in N.', '\\in \\mathbb{N}.')

    # ====== Fix: C \subset A in Chinese -> $C \subset A$ ======
    # Done in pass 1, check for any remaining

    # ====== Fix bare \mathbb references in Chinese ======
    c = c.replace('\\mathbb{R} 不可数', '$\\mathbb{R}$ 不可数')

    # ====== Fix: \frac{p}{q} bare -> wrapped ======
    # These are in Chinese blocks
    c = c.replace('排列 \\frac{p}{q}', '排列 $\\frac{p}{q}$')

    # Fix: dedekind definition bare C \subset A
    c = c.replace('$C \\subset A$', '$C \\subset A$')  # already ok from pass 1
    c = c.replace('C \\subset A（真子集）', '$C \\subset A$（真子集）')

    return c

changed = 0
for fname in ["index.md", "01-introduction.md", "02-basic-counting-principles.md",
              "03-counting-arguments.md", "04-counting-in-two-ways.md",
              "05-selections-with-repetition.md", "06-pigeonhole-principle.md",
              "07-inclusion-exclusion.md"]:
    fp = os.path.join(BASE, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    new = fix_file(content, fname)
    if new != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f"FIXED: {fname}")
        changed += 1
    else:
        print(f"OK: {fname}")
print(f"\nFiles changed: {changed}")
