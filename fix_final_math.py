"""
Final pass: fix remaining fragmented math patterns.
Specific targets:
1. "var $\cmd$ var" → "$var \cmd var$" (e.g. "n $\in$ N" → "$n \in \mathbb{N}$")
2. "$\sum$_{k$\in$[n]}" → "$\sum_{k \in [n]}$"
3. Other known broken patterns
"""

import re
import os
import glob

TARGET_DIR = os.path.join(os.path.dirname(__file__), 'docs')

# Set name mapping
SET_NAMES = {'N': r'\mathbb{N}', 'Z': r'\mathbb{Z}', 'Q': r'\mathbb{Q}',
             'R': r'\mathbb{R}', 'C': r'\mathbb{C}'}

def fix_fragmented_in_text(line):
    """Fix 'var $\\cmd$ var' patterns by merging into one $..$ span."""

    # Pattern: single letter followed by $\cmd$ followed by a set name or variable
    # e.g. "n $\in$ N" → "$n \in \mathbb{N}$"
    # e.g. "x $\in$ A" → "$x \in A$"

    # First, identify segments that should be merged
    # A "fragmented math run" looks like:
    # $A$ text $B$ text $C$ where text is very short (1-3 chars of variables/commas)

    # Strategy: find pairs of adjacent $...$ with very short text between,
    # where the text and both $...$ are all mathematical

    result = line
    prev = None
    iterations = 0

    while prev != result and iterations < 15:
        prev = result

        # Pattern 1: "X $\\cmd$Y" where X is a single letter/digit and Y follows
        # e.g. "n $\in$ N" → "$n \in \mathbb{N}$"
        # Match: $content1$SHORTTEXT$content2$
        # where SHORTTEXT is 1-8 chars of variables, spaces, commas

        def merge_adjacent_math(m):
            c1 = m.group(1)    # content of first $..$
            mid = m.group(2)   # text between (very short)
            c2 = m.group(3)    # content of second $..$

            # Only merge if middle is math-like (no English words)
            mid_stripped = mid.strip()
            if not mid_stripped:
                # Adjacent $..$$..$ already handled
                return f'${c1} {c2}$'

            # Check middle is math-like: letters, digits, commas, spaces, parens
            if re.match(r'^[a-zA-Z0-9,.\s()\[\]{}+\-*=/\\!]+$', mid_stripped):
                # Check it's short enough
                if len(mid_stripped) <= 12:
                    return f'${c1}{mid}{c2}$'

            return m.group(0)  # keep as is

        result = re.sub(r'\$([^$]+)\$([^$]{1,12})\$([^$]+)\$', merge_adjacent_math, result)
        iterations += 1

    # Specific known fixes

    # Fix: "$\sum$_{k$\in$[n]}" patterns → "$\sum_{k \in [n]}$"
    result = result.replace('$\\sum$_{k$\\in$[n]}', '$\\sum_{k \\in [n]}$')

    # Fix: set names in math mode that should be \mathbb{}
    # Be conservative: only fix obvious ones in newly merged spans

    # Fix: "n $\in$ N" type pattern where N → \mathbb{N}
    def fix_set_names(m):
        content = m.group(0)
        # Inside $...$, replace bare set names
        for name, latex in SET_NAMES.items():
            # Only if the name is standalone (space or boundary)
            content = re.sub(rf'(?<![\\a-zA-Z]){name}(?![a-zA-Z])', latex, content)
        return content

    # Apply set name fixes within $...$
    parts = re.split(r'(\$[^$\n]+\$)', result)
    for i, part in enumerate(parts):
        if i % 2 == 1:  # math segment
            for name, latex in SET_NAMES.items():
                # Simple replacement: " N " → " \mathbb{N} " inside math
                part = part.replace(f' {name} ', f' {latex} ')
                part = part.replace(f' {name}$', f' {latex}$')
                part = part.replace(f'\\in {name}', f'\\in {latex}')
                part = part.replace(f'\\subseteq {name}', f'\\subseteq {latex}')
                part = part.replace(f'\\subset {name}', f'\\subset {latex}')
                part = part.replace(f'\\notin {name}', f'\\notin {latex}')
                part = part.replace(f'\\times {name}', f'\\times {latex}')
                part = part.replace(f'\\to {name}', f'\\to {latex}')
            parts[i] = part
    result = ''.join(parts)

    return result


def process_file(filepath):
    """Process a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    changes = 0
    new_lines = []

    for line in lines:
        new_line = fix_fragmented_in_text(line)
        if new_line != line:
            changes += 1
        new_lines.append(new_line)

    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f"  {filepath}: {changes} lines fixed")

    return changes


def main():
    total_changes = 0
    for filepath in sorted(glob.glob(os.path.join(TARGET_DIR, '**', '*.md'), recursive=True)):
        changes = process_file(filepath)
        total_changes += changes

    print(f"\nTotal: {total_changes} lines fixed")

if __name__ == '__main__':
    main()
