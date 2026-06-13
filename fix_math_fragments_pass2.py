#!/usr/bin/env python3
"""Second pass: fix remaining fragmented $..$ patterns.

Handles:
1. $|$ \mathbb{N} $|$ cardinality splits
2. $f: $\mathbb{R}$ \to $\mathbb{R}$ function definition splits
3. $\mathbb{N}$ \times \mathbb{N}$ Cartesian product splits
4. General $A $\mathbb{B}$ C$ merges where C continues the math expression
5. Various splits in Chinese translation blocks
"""
import re
import os
import sys
import io
import glob

# Fix encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DOCS_DIR = os.path.join(os.path.dirname(__file__), 'docs')

def fix_content_pass2(content, filepath):
    """Second pass fix for remaining broken $ boundaries."""
    original = content
    changes = 0

    # ==========================================
    # PATTERN: $|$ \mathbb{X} $|$ cardinality notation
    # Broken: $|$\mathbb{N}$|$ → $|\mathbb{N}|$
    # Broken: $|$\mathbb{N}$| = |$\mathbb{Z}$|$ → $|\mathbb{N}| = |\mathbb{Z}|$
    # ==========================================

    # Fix: $|$\mathbb{X}$|$ → $|\mathbb{X}|$
    content, n = re.subn(
        r'\$\|\$\\mathbb\{(\w+)\}\$\|\$',
        r'$|\\mathbb{\1}|$',
        content)
    changes += n

    # Fix: $|\mathbb{X}|$ is sometimes rendered correctly already, skip

    # Fix: $|$\mathbb{X}$| = |$\mathbb{Y}$|$ → $|\mathbb{X}| = |\mathbb{Y}|$
    content, n = re.subn(
        r'\$\|\$\\mathbb\{(\w+)\}\$\|\s*=\s*\|\$\\mathbb\{(\w+)\}\$\|\$',
        r'$|\\mathbb{\1}| = |\\mathbb{\2}|$',
        content)
    changes += n

    # Fix: $|$\mathbb{X}$| < |$\mathbb{Y}$|$ → $|\mathbb{X}| < |\mathbb{Y}|$
    content, n = re.subn(
        r'\$\|\$\\mathbb\{(\w+)\}\$\|\s*<\s*\|\$\\mathbb\{(\w+)\}\$\|\$',
        r'$|\\mathbb{\1}| < |\\mathbb{\2}|$',
        content)
    changes += n

    # Fix: $|$\mathbb{X}$| > |$\mathbb{Y}$|$ → $|\mathbb{X}| > |\mathbb{Y}|$
    content, n = re.subn(
        r'\$\|\$\\mathbb\{(\w+)\}\$\|\s*>\s*\|\$\\mathbb\{(\w+)\}\$\|\$',
        r'$|\\mathbb{\1}| > |\\mathbb{\2}|$',
        content)
    changes += n

    # ==========================================
    # PATTERN: $f: $\mathbb{X}$ \to $\mathbb{Y}$
    # Broken: $f: $\mathbb{R}$ \to $\mathbb{R}$ → $f: \mathbb{R} \to \mathbb{R}$
    # ==========================================

    # Fix: $VAR: $\mathbb{X}$ \to $\mathbb{Y}$
    content, n = re.subn(
        r'\$(\\?\w+)\s*:\s+\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1: \\mathbb{\2} \\to \\mathbb{\3}$',
        content)
    changes += n

    # Fix: $VAR $\to $\mathbb{X}$
    content, n = re.subn(
        r'\$(\\?\w+)\s+\$\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1 \\to \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $\mathbb{X}$ \to $\mathbb{Y}$ (no preceding var)
    content, n = re.subn(
        r'\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$\\mathbb{\1} \\to \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $\mathbb{X}$ \times \mathbb{Y}$ → $\mathbb{X} \times \mathbb{Y}$
    # When the first \mathbb{} is in its own $ block but \times continues
    content, n = re.subn(
        r'\$\\mathbb\{(\w+)\}\$\s*\\times\s+\\mathbb\{(\w+)\}\$',
        r'$\\mathbb{\1} \\times \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $A \times $\mathbb{B}$ → $A \times \mathbb{B}$
    content, n = re.subn(
        r'\$([^$]+?)\\times\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1\\times \\mathbb{\2}$',
        content)
    changes += n

    # ==========================================
    # PATTERN: General $A $\mathbb{B}$ C$ merge
    # Where A ends with an operator/in and C is clearly math continuation
    # ==========================================

    # Fix: $X \in $\mathbb{Y}$ and more → depends on context
    # Only merge when it's clearly a continuous expression
    # $VAR \in $\mathbb{Y}$ → $VAR \in \mathbb{Y}$
    content, n = re.subn(
        r'\$([^$]+?)\\in\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1\\in \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $VAR \to $\mathbb{Y}$ → $VAR \to \mathbb{Y}$
    content, n = re.subn(
        r'\$([^$]+?)\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1\\to \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $VAR \subset $\mathbb{Y}$ → $VAR \subset \mathbb{Y}$
    content, n = re.subn(
        r'\$([^$]+?)\\subset\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1\\subset \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $VAR \supseteq $\mathbb{Y}$ → $VAR \supseteq \mathbb{Y}$
    content, n = re.subn(
        r'\$([^$]+?)\\supseteq\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1\\supseteq \\mathbb{\2}$',
        content)
    changes += n

    # ==========================================
    # PATTERN: $Example N.M.N. $\mathbb{X}$ \times ...$
    # Broken: $Example 7.6.13. $\mathbb{N}$ \times \mathbb{N}$ is countably infinite$:
    # → Example 7.6.13. $\mathbb{N} \times \mathbb{N}$ is countably infinite:
    # ==========================================

    # Fix: $Example ... $\mathbb{...}$ ...$  — leading $ is wrong
    content, n = re.subn(
        r'\$Example\s+(\d+\.\d+\.\d+)\.\s+\$\\mathbb\{([^}]+)\}',
        r'Example \1. $\\mathbb{\2}',
        content)
    changes += n

    # Fix: $With ... $\mathbb{...}$ ...$ — leading $ is wrong
    content, n = re.subn(
        r'\$With\s+',
        r'With ',
        content)
    changes += n

    # Fix: $Now we know ... $\mathbb{...}$ ...$ — leading $ is wrong
    content, n = re.subn(
        r'\$Now\s+we\s+know\s+',
        r'Now we know ',
        content)
    changes += n

    # Fix: $infinite. at start of paragraph
    content, n = re.subn(
        r'\$infinite\.\s+',
        r'infinite. ',
        content)
    changes += n

    # Fix: $A \cup B$| = ...  (without leading $)
    # This is partial — need to handle based on context

    # ==========================================
    # PATTERN: Stray $ at start/end of paragraphs
    # From the broken fix, some paragraphs start or end with $
    # ==========================================

    # Fix: $Moral ... $ pattern at start
    content, n = re.subn(
        r'\$Morally\s+speaking',
        r'Morally speaking',
        content)
    changes += n

    # Fix: $infinite. This ...
    content, n = re.subn(
        r'\$infinite\.\s+This',
        r'infinite. This',
        content)
    changes += n

    # ==========================================
    # PATTERN: $ text $\mathbb{X}$ text $  (3-block merge)
    # Merge: $A $\mathbb{B}$ C$ where C is clearly continuation
    # ==========================================

    # Fix: $A $\mathbb{B}$ C$ where A ends with \in or \to etc.
    # and C is math content ending with $
    def merge_three_blocks(m):
        a, b, c = m.group(1), m.group(2), m.group(3)
        return f'${a} \\mathbb{{{b}}} {c}$'
    content, n = re.subn(
        r'\$([^$\n]+?\\in)\s+\$\\mathbb\{([^}]+)\}\$\s+([^$\n]+?)\$',
        merge_three_blocks,
        content)
    changes += n

    # Fix: $A $\mathbb{B}$ C$ where A ends with \to
    content, n = re.subn(
        r'\$([^$\n]+?\\to)\s+\$\\mathbb\{([^}]+)\}\$\s+([^$\n]+?)\$',
        merge_three_blocks,
        content)
    changes += n

    # ==========================================
    # PATTERN: $\mathbb{Z}$ mod $n$ (this is actually correct, skip)
    # But: $f : $\mathbb{R}$ \to $\mathbb{R}$  is broken
    # ==========================================

    # Fix: $f : $\mathbb{X}$ \to $\mathbb{Y}$ → $f : \mathbb{X} \to \mathbb{Y}$
    content, n = re.subn(
        r'\$\\?(\w+)\s*:\s+\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1: \\mathbb{\2} \\to \\mathbb{\3}$',
        content)
    changes += n

    # Fix: various $ expr $\mathbb{X}$ expr$ merged patterns
    # Fix: $\mathbb{X}$ \subseteq $\mathbb{Y}$ → $\mathbb{X} \subseteq \mathbb{Y}$
    content, n = re.subn(
        r'\$\\mathbb\{(\w+)\}\$\s*\\subseteq\s+\$\\mathbb\{(\w+)\}\$',
        r'$\\mathbb{\1} \\subseteq \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $A \subseteq $\mathbb{X}$ → $A \subseteq \mathbb{X}$
    content, n = re.subn(
        r'\$([^$]+?)\\subseteq\s+\$\\mathbb\{(\w+)\}\$',
        r'$\1\\subseteq \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $|$\mathbb{N}$|^k$ → $|\mathbb{N}|^k$ or similar
    # Fix: $|$\mathbb{N}$ \times \mathbb{N}$|$ → $|\mathbb{N} \times \mathbb{N}|$
    content, n = re.subn(
        r'\$\|\$\\mathbb\{(\w+)\}\$\s*\\times\s+\\mathbb\{(\w+)\}\$\|\$',
        r'$|\\mathbb{\1} \\times \\mathbb{\2}|$',
        content)
    changes += n

    # ==========================================
    # PATTERN: Chinese blocks: $f: $\mathbb{X}$ \to ...$
    # ==========================================

    # Fix: $f: $\mathbb{R}$ \to $\mathbb{R}$ in Chinese blocks
    # Already handled above but let's also catch:
    # $f: $\mathbb{N}$ \to $\mathbb{N}$
    # $f: $\mathbb{Z}$ \to $\mathbb{Q}$
    content, n = re.subn(
        r'\$f:\s+\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$f: \\mathbb{\1} \\to \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $g: $\mathbb{X}$ \to $\mathbb{Y}$
    content, n = re.subn(
        r'\$g:\s+\$\\mathbb\{(\w+)\}\$\s*\\to\s+\$\\mathbb\{(\w+)\}\$',
        r'$g: \\mathbb{\1} \\to \\mathbb{\2}$',
        content)
    changes += n

    # ==========================================
    # PATTERN: $\{X \in ...$\} — set notation with \mathbb inside
    # Fix: $\{(x, x^2) \mid x \in \mathbb{R}$\}$  →  $\{(x, x^2) \mid x \in \mathbb{R}\}$
    # ==========================================
    content, n = re.subn(
        r'\$\\mathbb\{(\w+)\}\$\\}',
        r'\\mathbb{\1}\\}$',
        content)
    changes += n

    # Fix: general pattern where $\}$ appears alone at end of set-builder
    # $\{(x, x^2) \mid x \in $\mathbb{R}$\}$
    # This is: $\{(x, x^2) \mid x \in $ + \mathbb{R}$ + \}$
    # → should be: $\{(x, x^2) \mid x \in \mathbb{R}\}$
    content, n = re.subn(
        r'\$\\in\s+\$\\mathbb\{(\w+)\}\$\\}\$',
        r'$\\in \\mathbb{\1}\\}$',
        content)
    changes += n

    # Fix: more general: $.. \mid .. \in $\mathbb{X}$\}$
    content, n = re.subn(
        r'\$([^$]+?)\\mid\s+([^$]+?)\\in\s+\$\\mathbb\{(\w+)\}\$\\}\$',
        r'$\1\\mid \2\\in \\mathbb{\3}\\}$',
        content)
    changes += n

    # Fix: $\{$ x \in $\mathbb{R}$ | ... $\}$ → $\{x \in \mathbb{R} | ...\}$
    # This is harder - the { and } are at the boundaries
    # Let's handle: $\{X \in $\mathbb{R}$ | condition $\}$
    # → should be: $\{X \in \mathbb{R} | condition\}$

    # ==========================================
    # PATTERN: $Im_f($\mathbb{N}$) = \{$ even $\}$ style
    # ==========================================

    # Fix: $\text{PreIm}_f(Z \cap W) = \text{PreIm}_f(Z) \cap \text{PreIm}_f(W)$
    # This should be one expression if it isn't already

    # ==========================================
    # PATTERN: Stray $ signs from broken merges
    # After first-pass fixes, there may be unbalanced $ due to double replacements
    # ==========================================

    # Fix: $\cup \{0\}$$ — double $$ at end from replacement
    content, n = re.subn(r'\\{0\\}\$\$', r'\\{0\\}$', content)
    changes += n

    # Fix: $$\{0\}$ — double $$ at start
    content, n = re.subn(r'\$\$\\{0\\}\$', r'$\\{0\\}$', content)
    changes += n

    # Fix: double $$ appearing
    content, n = re.subn(r'\$\$', r'', content)  # remove empty $$ pairs
    changes += n

    return content, changes


def check_line_balance(content):
    """Check each line for unbalanced $ signs (odd count)."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        # Skip lines inside code blocks
        if line.strip().startswith('```') or line.strip().startswith('```'):
            continue
        # Count $ signs (excluding $$ for display math)
        count = line.count('$')
        if count % 2 != 0:
            issues.append((i, count, line.strip()[:120]))
    return issues


def main():
    md_files = glob.glob(os.path.join(DOCS_DIR, '**/*.md'), recursive=True)
    total_changes = 0
    fixed_files = []

    for filepath in sorted(md_files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = fix_content_pass2(content, filepath)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_files.append((filepath, changes))
            total_changes += changes

    print(f"Pass 2 - Files fixed: {len(fixed_files)}")
    print(f"Total pattern replacements: {total_changes}")
    for fp, n in fixed_files:
        rel = os.path.relpath(fp, os.path.dirname(__file__))
        print(f"  {rel}: {n} fixes")

    # Now check for remaining issues
    print("\n=== Remaining unbalanced $ lines ===")
    for filepath in sorted(md_files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        issues = check_line_balance(content)
        if issues:
            rel = os.path.relpath(filepath, os.path.dirname(__file__))
            for line_num, count, line_text in issues[:10]:
                # Skip Chinese block lines as they might be intentional
                if line_text.startswith('>'):
                    continue
                print(f"  {rel}:{line_num} (${count}$): {line_text}")


if __name__ == '__main__':
    main()
