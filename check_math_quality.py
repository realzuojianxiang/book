"""
Scan markdown files for math formula quality issues:
1. Unicode math symbols outside $...$
2. Bare subscripts/superscripts outside $...$
3. Fragment formula patterns outside $...$
"""
import re
import sys
import os

# Target directories
TARGETS = [
    r"docs\part-i\ch01-what-is-mathematics",
    r"docs\part-i\ch02-mathematical-induction",
    r"docs\part-i\ch03-sets",
    r"docs\part-i\ch04-logic",
    r"docs\part-i\ch05-rigorous-induction",
]

# Ch6 specific files (02 and 03 already fixed)
CH6_FILES = [
    r"docs\part-ii\ch06-relations-modular-arithmetic\01-introduction.md",
    r"docs\part-ii\ch06-relations-modular-arithmetic\04-equivalence-relations.md",
    r"docs\part-ii\ch06-relations-modular-arithmetic\05-modular-arithmetic.md",
    r"docs\part-ii\ch06-relations-modular-arithmetic\index.md",
]

BASE = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics"

# Unicode math symbols that should not appear outside $...$
UNICODE_MATH = re.compile(r'[≤≥≠∞∑∏√⊆⊇∈∉∧∨¬⟹⟺∀∃⟶→←↔⊕⊗×·±≈≅≡≪≫⊂⊃⊄⊅∪∩∖∆∇θ]')

# Bare subscript: letter followed by _ and identifier, NOT inside $
# e.g. x_1, a_n, F_{n-1}
BARE_SUBSCRIPT = re.compile(r'[a-zA-Z]_[a-zA-Z0-9{]')

# Bare superscript: letter/digit followed by ^ and digit/{
BARE_SUPERSCRIPT = re.compile(r'[a-zA-Z0-9]\^[0-9{]')

# Fragment formulas: isolated math operators outside $...$
FRAGMENT_PATTERNS = [
    re.compile(r'(?<![a-zA-Z])\d+\s*[+\-]\s*\d+(?![a-zA-Z])'),  # bare arithmetic like "3 + 5"
    re.compile(r'\\(?:frac|sum|prod|sqrt|int|lim|log|sin|cos|tan|gcd|lcm|min|max|inf|sup)\b'),  # LaTeX outside $
]

def is_inside_math(line, pos):
    """Check if position pos in line is inside $...$ or $$...$$."""
    # Count unescaped $ signs before position
    count = 0
    i = 0
    while i < pos:
        if line[i] == '\\' and i + 1 < pos and line[i+1] == '$':
            i += 2  # skip escaped \$
            continue
        if line[i] == '$':
            count += 1
        i += 1
    # Inside math if odd number of $ before pos
    return count % 2 == 1

def check_file(filepath):
    """Check a single file for math issues."""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  ERROR reading {filepath}: {e}")
        return issues

    for lineno, line in enumerate(lines, 1):
        # Skip code blocks and front matter
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('---'):
            continue

        # Check Unicode math symbols
        for m in UNICODE_MATH.finditer(line):
            if not is_inside_math(line, m.start()):
                issues.append((lineno, 'UNICODE_MATH', m.group(), m.start()))

        # Check bare subscripts
        for m in BARE_SUBSCRIPT.finditer(line):
            if not is_inside_math(line, m.start()):
                # Extra check: make sure it's not inside a code span `...`
                # Check if inside backtick
                before = line[:m.start()]
                if before.count('`') % 2 == 1:
                    continue  # inside code span
                issues.append((lineno, 'BARE_SUBSCRIPT', m.group(), m.start()))

        # Check bare superscripts
        for m in BARE_SUPERSCRIPT.finditer(line):
            if not is_inside_math(line, m.start()):
                before = line[:m.start()]
                if before.count('`') % 2 == 1:
                    continue
                issues.append((lineno, 'BARE_SUPERSCRIPT', m.group(), m.start()))

        # Check fragment LaTeX outside $
        for pattern in FRAGMENT_PATTERNS:
            for m in pattern.finditer(line):
                if not is_inside_math(line, m.start()):
                    before = line[:m.start()]
                    if before.count('`') % 2 == 1:
                        continue
                    issues.append((lineno, 'FRAGMENT_LATEX', m.group(), m.start()))

    return issues

def main():
    all_issues = {}

    # Collect all target files
    files_to_check = []
    for target_dir in TARGETS:
        full_dir = os.path.join(BASE, target_dir)
        if os.path.isdir(full_dir):
            for fname in sorted(os.listdir(full_dir)):
                if fname.endswith('.md'):
                    files_to_check.append(os.path.join(full_dir, fname))

    for ch6_file in CH6_FILES:
        full_path = os.path.join(BASE, ch6_file)
        if os.path.isfile(full_path):
            files_to_check.append(full_path)

    print(f"Checking {len(files_to_check)} files...\n")

    for filepath in files_to_check:
        relpath = os.path.relpath(filepath, BASE)
        issues = check_file(filepath)
        if issues:
            all_issues[relpath] = issues

    if all_issues:
        print("=== ISSUES FOUND ===\n")
        for relpath, issues in sorted(all_issues.items()):
            print(f"\n{relpath}:")
            for lineno, itype, match, pos in issues:
                print(f"  L{lineno}: [{itype}] '{match}' at col {pos}")
                # Show context
                with open(os.path.join(BASE, relpath), 'r', encoding='utf-8') as f:
                    line = f.readlines()[lineno-1].rstrip()
                print(f"    {line}")
    else:
        print("No issues found!")

    # Summary
    total = sum(len(v) for v in all_issues.values())
    print(f"\n=== SUMMARY: {len(all_issues)} files, {total} issues ===")
    for itype in ['UNICODE_MATH', 'BARE_SUBSCRIPT', 'BARE_SUPERSCRIPT', 'FRAGMENT_LATEX']:
        count = sum(1 for issues in all_issues.values() for _, t, _, _ in issues if t == itype)
        if count:
            print(f"  {itype}: {count}")

if __name__ == '__main__':
    main()
