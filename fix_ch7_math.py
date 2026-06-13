#!/usr/bin/env python3
"""Fix common math formula issues in Ch7 markdown files."""
import re
import os

DIR = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics\docs\part-ii\ch07-functions-cardinality"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    original = text

    # 1. Fix "f : R $-> \mathbb{R}$" → proper formatting
    text = re.sub(r': R\s+\$\\to\s+\\mathbb\{R\}\$', r': $\\mathbb{R} \\to \\mathbb{R}$', text)
    text = re.sub(r': R\s+\$\\to\s+\\mathbb\{C\}\$', r': $\\mathbb{R} \\to \\mathbb{C}$', text)
    text = re.sub(r': Z\s+\$\\to\s+\\mathbb\{R\}\$', r': $\\mathbb{Z} \\to \\mathbb{R}$', text)
    text = re.sub(r': N\s+\$\\to\s+\\mathbb\{N\}\$', r': $\\mathbb{N} \\to \\mathbb{N}$', text)
    text = re.sub(r': N\s+\$\\to\s+S\$', r': $\\mathbb{N} \\to S$', text)

    # 2. Fix "from R to R" → "from $\mathbb{R}$ to $\mathbb{R}$"
    text = text.replace('from R to R', r'from $\mathbb{R}$ to $\mathbb{R}$')
    text = text.replace('from R to', r'from $\mathbb{R}$ to')

    # 3. Fix " on R" meaning real numbers (not relation R)
    text = re.sub(r' on R([ ,;.])', r' on $\\mathbb{R}$\1', text)
    text = re.sub(r' on N([ ,;.])', r' on $\\mathbb{N}$\1', text)

    # 4. Fix "$N \times \mathbb{N}$" → "$\mathbb{N} \times \mathbb{N}$"
    text = re.sub(r'\$N\\s*\\times\\s*\\mathbb\{N\}\$', r'$\\mathbb{N} \\times \\mathbb{N}$', text)
    text = re.sub(r'\$N\\s*\\times\\s*\\mathbb\{N\}\\s*\\to\\s*\\mathbb\{Z\}\$', r'$\\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{Z}$', text)
    text = re.sub(r'\$N\\s*\\times\\s*\\mathbb\{N\}\\s*\\to\\s*\\mathbb\{N\}\$', r'$\\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{N}$', text)

    # 5. Fix N\timesN (no space) → proper format
    text = text.replace(r'N\timesN', r'\mathbb{N}\times\mathbb{N}')
    text = text.replace(r'N\\timesN', r'\\mathbb{N}\\times\\mathbb{N}')

    # 6. Fix specific "d : $N" patterns
    text = re.sub(r'd : \$N\\times', r'd : $\\mathbb{N} \\times', text)
    text = re.sub(r'p : \$N\\times', r'p : $\\mathbb{N} \\times', text)
    text = re.sub(r'F : \$N\\times', r'F : $\\mathbb{N} \\times', text)
    text = re.sub(r'g : \$N\\times', r'g : $\\mathbb{N} \\times', text)
    text = re.sub(r'f : \$N\\times', r'f : $\\mathbb{N} \\times', text)

    # 7. Fix f $\subseteq g$ → $f \subseteq g$ (fragmented formulas)
    text = re.sub(r'f\s+\$\\subseteq\s+g\$', r'$f \\subseteq g$', text)
    text = re.sub(r'g\s+\$\\subseteq\s+f\$', r'$g \\subseteq f$', text)

    # 8. Fix A $\cap B$ → $A \cap B$ etc.
    text = re.sub(r'\bA\s+\$\\cap\s+B\$', r'$A \\cap B$', text)
    text = re.sub(r'\bA\s+\$\\cup\s+B\$', r'$A \\cup B$', text)

    # 9. Fix "$\geq$0" → "$\geq 0$" etc. (number stuck outside $)
    text = re.sub(r'\$\\geq\$0\b', r'$\\geq 0$', text)
    text = re.sub(r'\$\\geq\$1\b', r'$\\geq 1$', text)
    text = re.sub(r'\$\\geq\$2\b', r'$\\geq 2$', text)
    text = re.sub(r'\$\\leq\$-1\b', r'$\\leq -1$', text)
    text = re.sub(r'\$\\leq\$0\b', r'$\\leq 0$', text)
    text = re.sub(r'\$\\leq\$1\b', r'$\\leq 1$', text)

    # 10. Fix "\mathbb{Z} - N" → "\mathbb{Z} - \mathbb{N}"
    text = re.sub(r'\\mathbb\{Z\}\s*-\s*N\b', r'\\mathbb{Z} - \\mathbb{N}', text)

    # 11. Fix R2, the real plane → $\mathbb{R}^2$
    text = text.replace('be R2, the real plane', r'be $\mathbb{R}^2$, the real plane')
    text = re.sub(r'\bR2\b', r'$\\mathbb{R}^2$', text)
    # Fix double-wrapped cases
    text = text.replace(r'$\mathbb{R}^2$$', r'$\mathbb{R}^2$')

    # 12. Fix bare f1/f2/g1/g2 etc as function names in math context
    # These are complex and need manual fix - skip auto

    # 13. Fix "IdS" → "$\mathrm{Id}_S$"
    text = text.replace('IdS to mean', r'$\mathrm{Id}_S$ to mean')

    # 14. Fix P(N) → \mathcal{P}(\mathbb{N}) - skip (too risky without context)
    # Just leaving P(N) as is for now

    # 15. Fix Z -{0} (bare) - carried by surrounding context
    # Already partially handled

    # 16. Fix commonly fragmented formulas
    # "f $\in A$" → "$f \in A$"
    text = re.sub(r'\bx\s+\$\\in\s+\\mathbb\{R\}\$', r'$x \\in \\mathbb{R}$', text)
    text = re.sub(r'\by\s+\$\\in\s+\\mathbb\{R\}\$', r'$y \\in \\mathbb{R}$', text)
    text = re.sub(r'\bn\s+\$\\in\s+\\mathbb\{N\}\$', r'$n \\in \\mathbb{N}$', text)
    text = re.sub(r'\bz\s+\$\\in\s+\\mathbb\{Z\}\$', r'$z \\in \\mathbb{Z}$', text)

    # 17. Fix "(also R," → "(also $\mathbb{R}$,"
    text = text.replace('(also R,', r'(also $\mathbb{R}$,')

    # 18. Fix bare "\mathbb{R}" not in $ in Chinese blocks
    text = re.sub(r'(?<!\$)\\mathbb\{R\}(?!\$)', r'$\\mathbb{R}$', text)
    text = re.sub(r'(?<!\$)\\mathbb\{N\}(?!\$)', r'$\\mathbb{N}$', text)
    text = re.sub(r'(?<!\$)\\mathbb\{Z\}(?!\$)', r'$\\mathbb{Z}$', text)
    text = re.sub(r'(?<!\$)\\mathbb\{Q\}(?!\$)', r'$\\mathbb{Q}$', text)
    # Fix double-wrapped cases $$..$$
    text = re.sub(r'\$\$\\mathbb\{([RNZQ])\}\$\$', r'$\\mathbb{\1}$', text)

    # Save if changed
    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    return False

files = [
    '01-introduction.md',
    '02-definition-and-examples.md',
    '03-images-and-preimages.md',
    '04-properties-of-functions.md',
    '05-compositions-and-inverses.md',
    '06-cardinality.md',
]

for fname in files:
    fpath = os.path.join(DIR, fname)
    if os.path.exists(fpath):
        changed = fix_file(fpath)
        print(f"{fname}: {'CHANGED' if changed else 'no changes'}")
    else:
        print(f"{fname}: NOT FOUND")
