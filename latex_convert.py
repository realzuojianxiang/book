"""
Batch LaTeX conversion for Unicode math symbols in all Markdown files.
Converts Unicode math characters to their LaTeX equivalents.
Also fixes common text patterns from PDF extraction.
"""
import re
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DOCS_DIR = "docs"

# Unicode symbol → LaTeX (single character replacements, most reliable)
UNICODE_LATEX = {
    '≠': '$\\neq$',
    '≥': '$\\geq$',
    '≤': '$\\leq$',
    '∈': '$\\in$',
    '∉': '$\\notin$',
    '⊆': '$\\subseteq$',
    '⊂': '$\\subset$',
    '⊇': '$\\supseteq$',
    '⊃': '$\\supset$',
    '∪': '$\\cup$',
    '∩': '$\\cap$',
    '∅': '$\\emptyset$',
    '∀': '$\\forall$',
    '∃': '$\\exists$',
    '→': '$\\to$',
    '↔': '$\\leftrightarrow$',
    '⇒': '$\\Rightarrow$',
    '⇔': '$\\Leftrightarrow$',
    '≈': '$\\approx$',
    '≡': '$\\equiv$',
    '∝': '$\\propto$',
    '∏': '$\\prod$',
    '∑': '$\\sum$',
    '∞': '$\\infty$',
    'ℕ': '$\\mathbb{N}$',
    'ℤ': '$\\mathbb{Z}$',
    'ℚ': '$\\mathbb{Q}$',
    'ℝ': '$\\mathbb{R}$',
    'ℂ': '$\\mathbb{C}$',
}

# Text pattern replacements (regex)
TEXT_PATTERNS = [
    # mod notation
    (re.compile(r'\(\s*mod\s+(\d+)\s*\)'), r'$\\pmod{\1}$'),
    # n-th, k-th ordinals
    (re.compile(r'\bn-th\b'), '$n$-th'),
    (re.compile(r'\bk-th\b'), '$k$-th'),
    # Prime factorization: 22·3 → $2^2 \cdot 3$ (common PDF artifact)
    (re.compile(r'(\d)(\d)\s*·\s*(\d)'), r'$\1^\2 \\cdot \3$'),
    # Multiply dot: · → $\cdot$
    (re.compile(r'\s*·\s*'), r' $\\cdot$ '),
]


def process_file(fpath):
    """Process a single Markdown file."""
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = 0

    # 1. Unicode symbol replacements
    for unicode_char, latex in UNICODE_LATEX.items():
        occurrences = content.count(unicode_char)
        if occurrences > 0:
            content = content.replace(unicode_char, latex)
            changes += occurrences

    # 2. Text pattern replacements
    for pattern, replacement in TEXT_PATTERNS:
        new_content = pattern.sub(replacement, content)
        if new_content != content:
            changes += 1
            content = new_content

    # 3. Fix double-dollar wrapping around already-LaTeX symbols
    # e.g. $$\\neq$$ → $\\neq$
    content = re.sub(r'\$\$(\\[a-zA-Z]+)\$\$', r'$\1$', content)

    # 4. Clean up: $\\neq$$\\neq$ → $\\neq$ $\\neq$ (add space between adjacent)
    content = re.sub(r'\$\$(\w)', r'$ $1', content)

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return 0


def main():
    total_files = 0
    total_changes = 0

    for root, dirs, files in os.walk(DOCS_DIR):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            fpath = os.path.join(root, fname)
            changes = process_file(fpath)
            if changes > 0:
                total_files += 1
                total_changes += changes
                relpath = os.path.relpath(fpath, DOCS_DIR)
                print(f"  +{changes}: {relpath}")

    print(f"\nDone! {total_files} files modified, {total_changes} replacements")


if __name__ == "__main__":
    main()
