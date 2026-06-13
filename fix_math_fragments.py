#!/usr/bin/env python3
"""Fix broken LaTeX math formulas in markdown files.

Fixes three types of issues caused by a previous automated "fix":
1. Fragmented \mathbb{} patterns: $n \in $\mathbb{N}$ \cup${0} → $n \in \mathbb{N} \cup \{0\}$
2. Split $ dollar signs around \cup and set notation
3. Empty $$ pairs (to check)
"""
import re
import os
import sys
import glob

DOCS_DIR = os.path.join(os.path.dirname(__file__), 'docs')

fixes_log = []

def log_fix(filepath, line_num, old_text, new_text):
    rel = os.path.relpath(filepath, os.path.dirname(__file__))
    fixes_log.append(f"  {rel}:{line_num}: {old_text!r} → {new_text!r}")

def fix_content(content, filepath):
    """Apply all fix patterns to content, return (fixed_content, change_count)."""
    original = content
    changes = 0

    # ========== PATTERN GROUP 1: \cup${0} and variants ==========
    # These patterns arise when a previous fix split math expressions at \cup boundaries
    # and un-escaped set braces {0} → \{0\}

    # Fix 1a: $X $\mathbb{Y}$ \cup${0}  →  $X \mathbb{Y} \cup \{0\}$
    # Example: $\forall n \in $\mathbb{N}$ \cup${0} → $\forall n \in \mathbb{N} \cup \{0\}$
    # Example: $\exists a, b \in $\mathbb{N}$ \cup${0} → $\exists a, b \in \mathbb{N} \cup \{0\}$
    def fix_1a(m):
        pre, bb = m.group(1), m.group(2)
        return f'${pre} \\mathbb{{{bb}}} \\cup \\{{0\\}}$'
    content, n = re.subn(
        r'\$([^$\n]+?)\s\$\\mathbb\{([^}]+)\}\$\s*\\cup\$\{0\}',
        fix_1a, content)
    changes += n

    # Fix 1b: $X $\mathbb{Y}$ \cup \{0\}$  →  $X \mathbb{Y} \cup \{0\}$
    # Example: $n \in $\mathbb{N}$ \cup \{0\}$ → $n \in \mathbb{N} \cup \{0\}$
    def fix_1b(m):
        pre, bb = m.group(1), m.group(2)
        return f'${pre} \\mathbb{{{bb}}} \\cup \\{{0\\}}$'
    content, n = re.subn(
        r'\$([^$\n]+?)\s\$\\mathbb\{([^}]+)\}\$\s*\\cup\s*\\{0\\}\$',
        fix_1b, content)
    changes += n

    # Fix 1c: $\mathbb{Y}$ \cup${0}  →  $\mathbb{Y} \cup \{0\}$
    # (no leading math fragment before $\mathbb)
    content, n = re.subn(
        r'\$\\mathbb\{([^}]+)\}\$\s*\\cup\$\{0\}',
        r'$\\mathbb{\1} \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1d: $\mathbb{Y}$ \cup \{0\}$  →  $\mathbb{Y} \cup \{0\}$
    content, n = re.subn(
        r'\$\\mathbb\{([^}]+)\}\$\s*\\cup\s*\\{0\\}\$',
        r'$\\mathbb{\1} \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1e: $\exists VAR$ $\in \mathbb{Z} \cup${0} → $\exists VAR \in \mathbb{Z} \cup \{0\}$
    content, n = re.subn(
        r'\$\\exists\s+(\w+)\$\s*\$\\in\s+\\mathbb\{(\w+)\}\s*\\cup\$\{0\}',
        r'$\\exists \1 \\in \\mathbb{\2} \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1f: $\in \mathbb{X} \cup${0}  →  $\in \mathbb{X} \cup \{0\}$
    content, n = re.subn(
        r'\$\\in\s+\\mathbb\{(\w+)\}\s*\\cup\$\{0\}',
        r'$\\in \\mathbb{\1} \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1g: $\in$[n -1] $\cup${0}  →  $\in [n-1] \cup \{0\}$
    content, n = re.subn(
        r'\$\\in\$\[n\s*-\s*1\]\s*\$\\cup\$\{0\}',
        r'$\\in [n-1] \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1h: $\in$[n -1] $\cup \{0\}$  →  $\in [n-1] \cup \{0\}$
    content, n = re.subn(
        r'\$\\in\$\[n\s*-\s*1\]\s*\$\\cup\s*\\{0\\}\$',
        r'$\\in [n-1] \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1i: $\forall i, j \in$[n -1] $\cup${0}  →  $\forall i, j \in [n-1] \cup \{0\}$
    content, n = re.subn(
        r'\$\\forall\s+([^$]+?)\\in\$\[n\s*-\s*1\]\s*\$\\cup\$\{0\}',
        r'$\\forall \1\\in [n-1] \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1j: $\to $\mathbb{N}$ \cup${0} → $\to \mathbb{N} \cup \{0\}$
    content, n = re.subn(
        r'\$\\to\s+\$\\mathbb\{(\w+)\}\$\s*\\cup\$\{0\}',
        r'$\\to \\mathbb{\1} \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1k: standalone $\cup${0} → $\cup \{0\}$
    content, n = re.subn(
        r'\$\\cup\$\{0\}',
        r'$\\cup \\{0\\}$',
        content)
    changes += n

    # Fix 1m: $\in \mathbb{N} \cup \{0\}$ is correct, but check for
    # $\exists ... $\mathbb{...}$ \cup \{0\}$
    # Pattern: $\exists n \in $\mathbb{N}$ \cup \{0\}$ → single expr
    content, n = re.subn(
        r'\$\\exists\s+([^$]+?)\s+\\in\s+\$\\mathbb\{(\w+)\}\$\s*\\cup\s*\\{0\\}\$',
        r'$\\exists \1 \\in \\mathbb{\2} \\cup \\{0\\}$',
        content)
    changes += n

    # ========== PATTERN GROUP 2: Fragmented \mathbb{} without \cup ==========
    # Fix 2a: $X $\mathbb{Y}$ Z$ → $X \mathbb{Y} Z$
    # This is a general merge for when \mathbb splits a math expression
    # Be careful: only match when the continuation looks like math content
    # Pattern: $word $\mathbb{SET}$ word$
    # where word doesn't contain $

    # Fix 2a: $text $\mathbb{X}$  → $text \mathbb{X}
    # This handles when the second $ (after \mathbb{X}) should start a new segment
    # but instead the expression should be continuous
    # Only apply when followed by something that looks like math continuation

    # Fix: "$\in $\mathbb{N}$" → "$\in \mathbb{N}$" (merge)
    content, n = re.subn(
        r'\$\\in\s+\$\\mathbb\{([^}]+)\}\$',
        r'$\\in \\mathbb{\1}$',
        content)
    changes += n

    # Fix: "$\to $\mathbb{N}$" → "$\to \mathbb{N}$"
    content, n = re.subn(
        r'\$\\to\s+\$\\mathbb\{([^}]+)\}\$',
        r'$\\to \\mathbb{\1}$',
        content)
    changes += n

    # Fix: "$\forall n \in $\mathbb{N}$\s" followed by non-math → merge up to end
    # But only if the next part is also math

    # ========== PATTERN GROUP 3: [n-1] $\cup${0} style ==========
    # These appear in proof text where the set-builder notation got split

    # Fix 3a: [n -1] $\cup \{0\}$ → $[n-1] \cup \{0\}$
    # When $\cup is a separate $ block
    content, n = re.subn(
        r'\[n\s*-\s*1\]\s*\$\\cup\s*\\{0\\}\$',
        r'$[n-1] \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 3b: [n -1] $\cup${0} → $[n-1] \cup \{0\}$
    content, n = re.subn(
        r'\[n\s*-\s*1\]\s*\$\\cup\$\{0\}',
        r'$[n-1] \\cup \\{0\\}$',
        content)
    changes += n

    # Fix 3c: $\forall VAR \in$[n -1] $\cup \{0\}$ → $\forall VAR \in [n-1] \cup \{0\}$
    content, n = re.subn(
        r'\$\\forall\s+(\w+)\s*\\in\$\[n\s*-\s*1\]\s*\$\\cup\s*\\{0\\}\$',
        r'$\\forall \1 \\in [n-1] \\cup \\{0\\}$',
        content)
    changes += n

    # ========== PATTERN GROUP 4: Chinese block specific ==========
    # $n \in $\mathbb{N}$ \cup \{0\}$ → $n \in \mathbb{N} \cup \{0\}$
    content, n = re.subn(
        r'\$([^$]+?)\s\\in\s+\$\\mathbb\{([^}]+)\}\$\s*\\cup\s*\\{0\\}\$',
        r'$\1 \\in \\mathbb{\2} \\cup \\{0\\}$',
        content)
    changes += n

    # $n, k \in \mathbb{N} \cup${0} → $n, k \in \mathbb{N} \cup \{0\}$
    content, n = re.subn(
        r'\$([^$]+?)\\in\s+\\mathbb\{(\w+)\}\s*\\cup\$\{0\}',
        r'$\1\\in \\mathbb{\2} \\cup \\{0\\}$',
        content)
    changes += n

    # ========== PATTERN GROUP 5: Other known fragmentations ==========
    # $\exists n \in $\mathbb{N}$ \cup \{0\}$ → $\exists n \in \mathbb{N} \cup \{0\}$
    content, n = re.subn(
        r'\$\\exists\s+n\s+\\in\s+\$\\mathbb\{([^}]+)\}\$\s*\\cup\s*\\{0\\}\$',
        r'$\\exists n \\in \\mathbb{\1} \\cup \\{0\\}$',
        content)
    changes += n

    # $n, k \in $\mathbb{N}$ \cup${0} (with space before \mathbb)
    content, n = re.subn(
        r'\$([^$]+?)\s+\\in\s+\$\\mathbb\{([^}]+)\}\$\s*\\cup\$\{0\}',
        r'$\1 \\in \\mathbb{\2} \\cup \\{0\\}$',
        content)
    changes += n

    # $n, k \in \mathbb{N} \cup${0} (no split before \mathbb, but split after \cup)
    content, n = re.subn(
        r'\$([^$]+?\s+\\in\s+\\mathbb\{[^}]+\})\s*\\cup\$\{0\}',
        r'\1 \\cup \\{0\\}$',
        content)
    changes += n

    # $n, k \in \mathbb{N} \cup \{0\}$ — check for already-correct versions (no change needed)

    # ========== PATTERN GROUP 6: General \cup$ at split points ==========
    # Any remaining \cup${0} that wasn't caught by above patterns
    # Context: \cup is followed by $ then {0} — always wrong
    # Replace: \cup${0} → \cup \{0\}$
    # But we need to figure out where the closing $ goes
    # Strategy: look for the nearest following $ and adjust

    # After all specific fixes, any remaining `\cup${0}` is standalone
    # Replace: \cup${0} → \cup \{0\}$
    # This moves the $ from before {0} to after 0}
    content, n = re.subn(r'\\cup\$\{0\}', r'\\cup \\{0\\}$', content)
    changes += n

    # And: \cup \{0\}$ → \cup \{0\} (if the $ was already at end)
    # Actually no, after moving $ to end, we may have $ at end followed by $ at start of next expression... skip this for now

    # ========== PATTERN GROUP 7: Empty $$ pairs ==========
    # Check for $$ with only whitespace between them on same line
    content, n = re.subn(r'\$\$\s*\$\$', '', content)
    changes += n

    # ========== PATTERN GROUP 8: Fix broken $ boundaries in general ==========
    # When we have $text $\mathbb{X}$ text$ and the split was wrong
    # This is hard to generalize, but let's handle a few more common cases

    # $\xrightarrow{}$ patterns aren't broken, skip

    # Handle: $N \times $\mathbb{N}$ → $N \times \mathbb{N}$
    content, n = re.subn(
        r'\$([^$]+?)\\times\s+\$\\mathbb\{([^}]+)\}\$',
        r'$\1\\times \\mathbb{\2}$',
        content)
    changes += n

    # Handle various $.. $\mathbb{..}$ at end of expressions
    # Pattern: $X $\mathbb{Y}$ (end of expr) → $X \mathbb{Y}$
    # Specifically: when $\mathbb{Y}$ appears to be closing a math expression
    # that was split at the \mathbb boundary
    # $to $\mathbb{N}$ → $to \mathbb{N}$
    content, n = re.subn(
        r'\$\\to\s+\$\\mathbb\{([^}]+)\}',
        r'$\\to \\mathbb{\1}',
        content)
    changes += n

    # Fix: $\exists n \in $\mathbb{N}$ → $\exists n \in \mathbb{N}$
    # This is when the expression doesn't have \cup part
    content, n = re.subn(
        r'\$\\exists\s+([^$]+?)\\in\s+\$\\mathbb\{([^}]+)\}\$',
        r'$\\exists \1\\in \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $n \in $\mathbb{N}$ → $n \in \mathbb{N}$  (simple case)
    content, n = re.subn(
        r'\$([^$]+?)\\in\s+\$\\mathbb\{([^}]+)\}\$',
        r'$\1\\in \\mathbb{\2}$',
        content)
    changes += n

    # Fix: $|$\mathbb{N}$| → $|\mathbb{N}|$
    content, n = re.subn(
        r'\$\|?\$\\mathbb\{([^}]+)\}\$\|?\$',
        r'$|\\mathbb{\1}|$',
        content)
    changes += n

    # Fix: |\mathbb{N}|  vs  $|\mathbb{N}|$ — varies by context
    # Let: $\mathbb{N}$| → $|\mathbb{N}| when | is cardinality
    # Too ambiguous, skip for now

    return content, changes


def find_remaining_issues(content, filepath):
    """Find lines that still look suspicious after fixes."""
    issues = []
    lines = content.split('\n')

    for i, line in enumerate(lines, 1):
        # Check for \cup${0} still present
        if r'\cup${' in line or r'\cup$\\{' in line:
            issues.append((i, line.strip()[:100], '\\cup${'))

        # Check for $\mathbb{}$ followed by what looks like math continuation
        # Pattern: $\mathbb{X}$ word (where word should be in math)
        # Too hard to detect generically, skip

        # Check for unpaired $ on a line (rough check)
        dollar_count = line.count('$')
        if dollar_count % 2 != 0:
            issues.append((i, line.strip()[:100], f'unpaired $ (count={dollar_count})'))

    return issues


def main():
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    md_files = glob.glob(os.path.join(DOCS_DIR, '**/*.md'), recursive=True)
    total_changes = 0
    fixed_files = []

    for filepath in sorted(md_files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = fix_content(content, filepath)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_files.append((filepath, changes))
            total_changes += changes

            # Check for remaining issues
            issues = find_remaining_issues(new_content, filepath)
            if issues:
                rel = os.path.relpath(filepath, os.path.dirname(__file__))
                print(f"\n  Remaining issues in {rel}:")
                for line_num, line_text, issue_type in issues[:5]:
                    print(f"    Line {line_num}: {issue_type}: {line_text}")

    print(f"\nFiles fixed: {len(fixed_files)}")
    print(f"Total pattern replacements: {total_changes}")
    for fp, n in fixed_files:
        rel = os.path.relpath(fp, os.path.dirname(__file__))
        print(f"  {rel}: {n} fixes")


if __name__ == '__main__':
    main()
