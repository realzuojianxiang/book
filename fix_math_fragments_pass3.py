#!/usr/bin/env python3
"""Third pass: fix remaining fragmented patterns.

Focus on:
1. $N \times $\mathbb{N}$ \to $\mathbb{N}$ → $N \times \mathbb{N} \to \mathbb{N}$
2. Imp(N \times $\mathbb{N}$) → $\text{Im}\, p(N \times \mathbb{N})$
3. $\forall x \in $\mathbb{R}$ → $\forall x \in \mathbb{R}$
4. Set builder splits: {$x \in $\mathbb{R}$ | ...} → $\{x \in \mathbb{R} | ...\}$
5. Example headings with stray $
6. $First, we prove ...$ stray $ at paragraph start
7. Like so$ → like so:
8. countably infinite$ → countably infinite:
"""
import re
import os
import sys
import io
import glob

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DOCS_DIR = os.path.join(os.path.dirname(__file__), 'docs')

def fix_content_pass3(content, filepath):
    """Third pass fix for remaining broken $ boundaries."""
    original = content
    changes = 0

    # ==========================================
    # PATTERN: $N \times $\mathbb{N}$ \to $\mathbb{N}$
    # This is a common pattern: N (literal N) × ℕ → ℕ
    # But the $ boundaries are misaligned
    # Should be: either $N \times \mathbb{N} \to \mathbb{N}$ or
    #             $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$
    # Looking at context, these are function definitions like:
    # p : N × ℕ → ℕ where N should actually be ℕ
    # ==========================================

    # Fix: p : $N \times $\mathbb{N}$ \to $\mathbb{N}$ → $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$
    # These are all function defs where the first N should be \mathbb{N}
    content, n = re.subn(
        r'\$N\s*\\times\s+\$\\mathbb\{N\}\$\s*\\to\s+\$\\mathbb\{N\}\$',
        r'$\\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{N}$',
        content)
    changes += n

    # Fix: p : $N \times $\mathbb{N}$ \to $\mathbb{Z}$
    content, n = re.subn(
        r'\$N\s*\\times\s+\$\\mathbb\{N\}\$\s*\\to\s+\$\\mathbb\{Z\}\$',
        r'$\\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{Z}$',
        content)
    changes += n

    # Fix: $N \times $\mathbb{N}$ → $racht{N} \times \mathbb{N}$
    content, n = re.subn(
        r'\$N\s*\\times\s+\$\\mathbb\{N\}\$',
        r'$\\mathbb{N} \\times \\mathbb{N}$',
        content)
    changes += n

    # Fix: |$N \times \mathbb{N}$| → |$\mathbb{N} \times \mathbb{N}$|
    content, n = re.subn(
        r'\|\$N\s*\\times\s+\\mathbb\{N\}\$\|',
        r'|$\\mathbb{N} \\times \\mathbb{N}$|',
        content)
    changes += n

    # Fix: |$N \times \mathbb{N}$| = |N|$ → |$\mathbb{N} \times \mathbb{N}$| = |$\mathbb{N}$|
    content, n = re.subn(
        r'\|\$N\s*\\times\s+\\mathbb\{N\}\$\|\s*=\s*\|N\|\$',
        r'|$\\mathbb{N} \\times \\mathbb{N}$| = |$\\mathbb{N}$|',
        content)
    changes += n

    # Fix: $\mathbb{N} \times \mathbb{N}$ is countably infinite$:
    # → $\mathbb{N} \times \mathbb{N}$ is countably infinite:
    content, n = re.subn(
        r'\\mathbb\{N\}\s*\\times\s+\\mathbb\{N\}\$\s+is\s+countably\s+infinite\$\:',
        r'\\mathbb{N} \\times \\mathbb{N}$ is countably infinite:',
        content)
    changes += n

    # Fix: like so$ → like so:
    content, n = re.subn(r'like so\$\:', r'like so:', content)
    changes += n
    content, n = re.subn(r'like so\$\b', r'like so:', content)
    changes += n

    # ==========================================
    # PATTERN: $\forall x \in $\mathbb{R}$
    # ==========================================
    content, n = re.subn(
        r'\$\\forall\s+(\w+)\s+\\in\s+\$\\mathbb\{(\w+)\}\$',
        r'$\\forall \1 \\in \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $\forall(a, b) \in $\mathbb{N}$ → $\forall(a, b) \in \mathbb{N}$
    content, n = re.subn(
        r'\$\\forall\s*\(([^)]+)\)\s*\\in\s+\$\\mathbb\{(\w+)\}\$',
        r'$\\forall(\1) \\in \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $\forall x \in $\mathbb{R}$.\  → $\forall x \in \mathbb{R}$.
    # This merges the expression when followed by a period and backslash-space
    content, n = re.subn(
        r'\$\\forall\s+(\w+)\s+\\in\s+\$\\mathbb\{(\w+)\}\$\.\\',
        r'$\\forall \1 \\in \\mathbb{\2}$.\\',
        content)
    changes += n

    # Fix: $\forall x \in \mathbb{R}$.\ f(x) = ... (already correct if inside one $)

    # ==========================================
    # PATTERN: $\{(x, x^2) \mid x \in $\mathbb{R}$\}$
    # → $\{(x, x^2) \mid x \in \mathbb{R}\}$
    # ==========================================
    content, n = re.subn(
        r'\$\\in\s+\$\\mathbb\{(\w+)\}\$\\}\$',
        r'\\in \\mathbb{\1}\\}$',
        content)
    changes += n

    # Fix: {$x \in $\mathbb{R}$ | 0 < x < 100} → $\\{x \in \mathbb{R} \\mid 0 < x < 100\\}$
    # Or just: $\{x \in \mathbb{R} | 0 < x < 100\}$
    # The set notation in non-math blocks needs different handling
    # Let me check the context for this one

    # ==========================================
    # PATTERN: $First, we prove ...$ stray $ at start
    # From broken fix, some paragraphs start with $
    # ==========================================
    content, n = re.subn(r'^\$First,\s+we\s+prove', r'First, we prove', content, flags=re.MULTILINE)
    changes += n

    content, n = re.subn(r'^\$First,\s+', r'First, ', content, flags=re.MULTILINE)
    changes += n

    # Fix: stray $ after N - at start
    # *Proof.* Let V = N -${1}
    content, n = re.subn(r'N\s*-\s*\$\{1\}', r'N - {1}', content)
    changes += n

    # Fix: Imp(N \times $\mathbb{N}$)
    # These are image/preimage notation that got split
    content, n = re.subn(
        r'Imp\(N\s*\\times\s+\$\\mathbb\{N\}\$\)',
        r'Imp($\\mathbb{N} \\times \\mathbb{N}$)',
        content)
    changes += n

    # Fix: Imp(N \times $\mathbb{N}$).$
    content, n = re.subn(
        r'Imp\(N\s*\\times\s+\$\\mathbb\{N\}\$\)\.\$',
        r'Imp($\\mathbb{N} \\times \\mathbb{N}$).',
        content)
    changes += n

    # Fix: \in Imp(N \times $\mathbb{N}$)
    content, n = re.subn(
        r'\\in\s+Imp\(N\s*\\times\s+\$\\mathbb\{N\}\$\)',
        r'\\in Imp($\\mathbb{N} \\times \\mathbb{N}$)',
        content)
    changes += n

    # Fix: n \in $\mathbb{N}$ and \exists(a, b) \in $\mathbb{N} \times \mathbb{N}$
    # Already correct? Let me check — if the \in and \exists are each in their own $..$ that's wrong too

    # ==========================================
    # PATTERN: $A \to B$ or $A $\to$ B$ splits in function defs
    # ==========================================

    # Fix: $f : $\mathbb{R}$ → really $f : \mathbb{R} \to \mathbb{R}$
    # Already handled in pass2 but let's check for remaining cases where colon is before the first $

    # Fix: Let $f : $\mathbb{R}$ \to $\mathbb{R}$ be the function
    # → Let $f : \mathbb{R} \to \mathbb{R}$ be the function
    content, n = re.subn(
        r'Let\s+\$(\\?\w+)\s*:\s+\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$\s+be',
        r'Let $\1: \\mathbb{\2} \\to \\mathbb{\3}$ be',
        content)
    changes += n

    # Fix: Let $a : $\mathbb{R}$ \to $\mathbb{R}$
    content, n = re.subn(
        r'Let\s+\$(\w+)\s*:\s+\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'Let $\1: \\mathbb{\2} \\to \\mathbb{\3}$',
        content)
    changes += n

    # ==========================================
    # PATTERN: $f: $\mathbb{R}$ \to $\mathbb{R}$ (without "Let")
    # ==========================================
    content, n = re.subn(
        r'\$f:\s+\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$f: \\mathbb{\1} \\to \\mathbb{\2}$',
        content)
    changes += n

    # Fix: Consider $d : $\mathbb{N}$... etc
    # General: $name : $\mathbb{X}$ ...
    content, n = re.subn(
        r'\$(\w+)\s*:\s+\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1: \\mathbb{\2} \\to \\mathbb{\3}$',
        content)
    changes += n

    # ==========================================
    # PATTERN: $A \to B and g : B $\to \mathbb{C}$
    # ==========================================

    # Fix: $\to B$ and g : B $\to \mathbb{C}$
    # These are in proof text where function composition is described

    # Fix: $f : A $\to B$ and g : B $\to \mathbb{C}$
    content, n = re.subn(
        r'\$f\s*:\s+A\s+\\to\s+B\$\s+and\s+g\s*:\s+B\s+\$\\to\s+\\mathbb\{(\w+)\}\$',
        r'$f : A \\to B$ and $g : B \\to \\mathbb{\1}$',
        content)
    changes += n

    # ==========================================
    # PATTERN: stray $ at end of example headings
    # Example 7.6.13. $\mathbb{N} \times \mathbb{N}$ is countably infinite$:
    # ==========================================
    content, n = re.subn(
        r'infinite\$\:', r'infinite:', content)
    changes += n

    content, n = re.subn(
        r'lattice\$\:', r'lattice:', content)
    changes += n

    # Fix: $Example 7.6.14. heading patterns
    content, n = re.subn(
        r'\$Example\s+(\d+\.\d+\.\d+)\.\s+',
        r'Example \1. ',
        content)
    changes += n

    # Fix: Example 7.6.14. $\mathbb{N} \times \mathbb{N}$ as a lattice$:
    # → Example 7.6.14. $\mathbb{N} \times \mathbb{N}$ as a lattice:
    content, n = re.subn(
        r'as a lattice\$\:',
        r'as a lattice:',
        content)
    changes += n

    # ==========================================
    # PATTERN: $text$ where $ at start is stray
    # Some paragraphs were prefixed with $ from the broken fix
    # e.g., $Now we know..., $infinite., $Morally...
    # ==========================================

    # Fix: $With the Hilbert Hotel → With the Hilbert Hotel  (already in pass2)
    # Fix: $Now we know → Now we know  (already in pass2)
    # Fix: $infinite. → infinite.  (already in pass2)
    # Fix: $Morally → Morally  (already in pass2)

    # Check for $First → First
    content, n = re.subn(r'\$First,', r'First,', content)
    changes += n

    # ==========================================
    # PATTERN: $|2z + 1|$ Wait... type fragments
    # $|2z + 1|$ Wait at end of $, then "how can" continues
    # ==========================================
    # These are likely correct (the $|expr|$ is a valid math block)
    # The "Wait" is literally part of the text, not math

    # ==========================================
    # PATTERN: specific remaining `\mathbb` splits
    # ==========================================

    # Fix: $\mathbb{R}$ be the function
    # → probably correct, $\mathbb{R}$ is a standalone reference

    # Fix: $\forall n \in \mathbb{N}$. $ → the . before $ is fine
    # These are correct

    # Fix: n \in $\mathbb{N}$ and \exists
    # → If n is not in a $..$ block, this might render as plain n
    # but that's a different issue

    # ==========================================
    # PATTERN: $\mathbb{C}$ (referencing the set C, not complex numbers)
    # In some contexts, \mathbb{C} is used as a set name, not complex numbers
    # Need to be careful here
    # ==========================================

    # Fix: $g : B \to \mathbb{C}$ → This is likely meant to be \mathcal{C} or just C
    # But we shouldn't change this without understanding context. Skip.

    # ==========================================
    # PATTERN: $(\mathbb{N} \cup \{0\})^2$ — already fixed in pass1
    # But check: $\in (\mathbb{N} \cup \{0\})^2$ missing opening $
    # ==========================================
    # Pattern from 03-counting-arguments.md:
    # $\in (\mathbb{N} \cup \{0\})^2 → needs opening $ before \in?
    # Actually this is: (x, y) $\in (\mathbb{N} \cup \{0\})^2.
    # The $ starts at \in. This should probably be one math block:
    # $(x, y) \in (\mathbb{N} \cup \{0\})^2$.
    # But that would require restructuring the theorem header

    # Fix: (x, y) $\in (\mathbb{N} \cup \{0\})^2. → $(x,y) \in (\mathbb{N} \cup \{0\})^2$.
    content, n = re.subn(
        r'\((x,\s*y|a,\s*b)\)\s+\$\\in\s+\(\\mathbb\{N\}\\cup\\{0\\}\)\^2',
        r'$(\1) \\in (\\mathbb{N} \\cup \\{0\\})^2$',
        content)
    changes += n

    # Fix: (x, y) $\in (\mathbb{N} \cup \{0\})^2, → same pattern with comma
    content, n = re.subn(
        r'\((x,\s*y|a,\s*b)\)\s+\$\\in\s+\(\\mathbb\{N\}\\cup\\{0\\}\)\^2,',
        r'$(\1) \\in (\\mathbb{N} \\cup \\{0\\})^2$,',
        content)
    changes += n

    # ==========================================
    # PATTERN: \that ... $ from pass2 changes
    # Also clean up \{0\}$$ double-dollar artifacts
    # ==========================================
    content, n = re.subn(r'\\{0\\}\$\$', r'\\{0\\}$', content)
    changes += n

    # ==========================================
    # PATTERN: (x, y) \in $\mathbb{N} \times \mathbb{N}$.
    # Where the first part is not in math but should be
    # ==========================================

    # Fix: (a, b) \in $\mathbb{N} \times \mathbb{N}$
    # → $(a, b) \in \mathbb{N} \times \mathbb{N}$
    content, n = re.subn(
        r'\(([^)]+)\)\s+\\in\s+\$\\mathbb\{N\}\s*\\times\s*\\mathbb\{N\}\$',
        r'$(\1) \\in \\mathbb{N} \\times \\mathbb{N}$',
        content)
    changes += n

    # ==========================================
    # PATTERN: $\mathbb{R}$: $\mathbb{R}$ where there's a colon split
    # Fix: $\mathbb{R}$ $\to$ $\mathbb{R}$ (this is already handled)
    # ==========================================

    # Fix: Let $G : $N \times ...
    # This is a function def with G as name
    content, n = re.subn(
        r'\$G\s*:\s+\$N\s*\\times\s+\$\\mathbb\{N\}\$\s*\\to\s+\$\\mathbb\{N\}\$',
        r'$G: \\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{N}$',
        content)
    changes += n

    # Fix: Let F : C $\to$ $\mathbb{R}$
    content, n = re.subn(
        r'F\s*:\s+C\s+\\to\s+\$\\mathbb\{R\}\$',
        r'$F: C \\to \\mathbb{R}$',
        content)
    changes += n

    # Fix: $C(x) = x -273.15 (with or without $around it)
    # Already correct in most cases

    # Fix: Let F : R $\to$ $\mathbb{R}$
    content, n = re.subn(
        r'F\s*:\s+R\s+\$\\to\$\s+\$\\mathbb\{R\}\$',
        r'$F: R \\to \\mathbb{R}$',
        content)
    changes += n

    # Fix: $n \in \mathbb{N}$. h(n) = 2n -1 patterns
    # These have their own $ blocks which is correct

    # Fix: Let $F : C $\to \mathbb{R}$
    content, n = re.subn(
        r'Let\s+\$F\s*:\s+C\s+\\to\s+\$\\mathbb\{R\}\$',
        r'Let $F: C \\to \\mathbb{R}$',
        content)
    changes += n

    return content, changes


def main():
    md_files = glob.glob(os.path.join(DOCS_DIR, '**/*.md'), recursive=True)
    total_changes = 0
    fixed_files = []

    for filepath in sorted(md_files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = fix_content_pass3(content, filepath)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_files.append((filepath, changes))
            total_changes += changes

    print(f"Pass 3 - Files fixed: {len(fixed_files)}")
    print(f"Total pattern replacements: {total_changes}")
    for fp, n in fixed_files:
        rel = os.path.relpath(fp, os.path.dirname(__file__))
        print(f"  {rel}: {n} fixes")


if __name__ == '__main__':
    main()
