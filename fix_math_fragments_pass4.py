#!/usr/bin/env python3
"""Pass 4: Fix cardinality notation splits and remaining Chinese block issues."""
import re
import os
import sys
import io
import glob

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DOCS_DIR = os.path.join(os.path.dirname(__file__), 'docs')

def mb(name):
    """Shorthand for \\mathbb{name}."""
    return f'\\mathbb{{{name}}}'

def fix_content_pass4(content, filepath):
    original = content
    changes = 0

    # Fix: $|$\mathbb{X}$|$ → $|\mathbb{X}|$
    def fix_card(m):
        return f'$|{mb(m.group(1))}|$'
    content, n = re.subn(r'\$\|\$\\mathbb\{(\w+)\}\$\|\$', fix_card, content)
    changes += n

    # Fix: $|$\mathbb{X}$| (trailing | after closing $)
    def fix_card_trail(m):
        return f'$|{mb(m.group(1))}|'
    content, n = re.subn(r'\$\|\\mathbb\{(\w+)\}\$\|', fix_card_trail, content)
    changes += n

    # Fix: |\mathbb{X}$|$ → |\mathbb{X}|$
    def fix_card_open(m):
        return f'|{mb(m.group(1))}|$'
    content, n = re.subn(r'\|\\mathbb\{(\w+)\}\$\|\$', fix_card_open, content)
    changes += n

    # Fix: $|$\mathbb{X}$| = |$\mathbb{Y}$|$
    def fix_card_eq(m):
        return f'$|{mb(m.group(1))}| = |{mb(m.group(2))}|$'
    content, n = re.subn(r'\$\|\$\\mathbb\{(\w+)\}\$\|\s*=\s*\|\$\\mathbb\{(\w+)\}\$\|\$', fix_card_eq, content)
    changes += n

    # Fix: $|$\mathbb{X}$| < |$A$ < |$\mathbb{Y}$|$
    def fix_card_chain(m):
        return f'$|{mb(m.group(1))}| < |{m.group(2)}| < |{mb(m.group(3))}|$'
    content, n = re.subn(
        r'\$\|\$\\mathbb\{(\w+)\}\$\|\s*<\s*\|([^$]+?)\|\s*<\s*\|\$\\mathbb\{(\w+)\}\$\|\$',
        fix_card_chain, content)
    changes += n

    # Fix: |$\mathbb{X}$| → $|\mathbb{X}|$ (cardinality context)
    def fix_card_bare(m):
        return f'$|{mb(m.group(1))}|$'
    content, n = re.subn(r'\|\$\\mathbb\{(\w+)\}\$\|', fix_card_bare, content)
    changes += n

    # Fix double $$ from previous: $|$\mathbb{X}|$ → $|\mathbb{X}|$
    def fix_card_dollar(m):
        return f'$|{mb(m.group(1))}|$'
    content, n = re.subn(r'\$\|\$\\mathbb\{(\w+)\}\|\$', fix_card_dollar, content)
    changes += n

    # Fix: $|$\mathbb{R}$| = |(0,1)|$
    def fix_card_eq_set(m):
        return f'$|{mb(m.group(1))}| = |{m.group(2)}|$'
    content, n = re.subn(r'\$\|\$\\mathbb\{(\w+)\}\$\|\s*=\s*\|([^|]+)\|\$', fix_card_eq_set, content)
    changes += n

    # Fix: ^$\mathbb{N}$ → ^{\mathbb{N}} when exponent
    def fix_exp(m):
        return f'^{{{mb(m.group(1))}}}'
    content, n = re.subn(r'\^\$\\mathbb\{(\w+)\}\$', fix_exp, content)
    changes += n

    # Fix: $\mathbb{R} \to $\mathbb{R}$^2$
    def fix_to_sq(m):
        return f'${mb(m.group(1))} \\to {mb(m.group(2))}^2$'
    content, n = re.subn(r'\$\\mathbb\{(\w+)\}\s*\\to\s+\$\\mathbb\{(\w+)\}\$\^2\$', fix_to_sq, content)
    changes += n

    # Fix: $\mathbb{R}^2 \to $\mathbb{R}$
    def fix_sq_to(m):
        return f'${mb(m.group(1))}^2 \\to {mb(m.group(2))}$'
    content, n = re.subn(r'\$\\mathbb\{(\w+)\}\^2\s*\\to\s+\$\\mathbb\{(\w+)\}\$', fix_sq_to, content)
    changes += n

    # Fix: $\mathbb{N}$\times$\mathbb{N}$ → $\mathbb{N} \times \mathbb{N}$
    def fix_times(m):
        return f'${mb(m.group(1))} \\times {mb(m.group(2))}$'
    content, n = re.subn(r'\$\\mathbb\{(\w+)\}\$\\times\$\\mathbb\{(\w+)\}\$', fix_times, content)
    changes += n

    # Fix: $|$\mathbb{N}$^3| → $|\mathbb{N}^3|$
    def fix_card_pow(m):
        return f'$|{mb(m.group(1))}^3|'
    content, n = re.subn(r'\$\|\$\\mathbb\{(\w+)\}\$\^3\|', fix_card_pow, content)
    changes += n

    # Fix: |$N \times \mathbb{N}$| = |N|$
    def fix_ntimes(m):
        return f'|${mb("N")} \\times {mb("N")}$| = |${mb("N")}$|'
    content, n = re.subn(r'\|\$N\s*\\times\s+\\mathbb\{N\}\$\|\s*=\s*\|N\|\$', fix_ntimes, content)
    changes += n

    # Fix: $\mathbb{N} \times \mathbb{N}$ in the proof$:
    content, n = re.subn(r'in the proof\$\:', 'in the proof:', content)
    changes += n

    # Fix: ...the two sets.$ → ...the two sets.
    content, n = re.subn(r'between the two sets\.\$', 'between the two sets.', content)
    changes += n

    # Fix: $Imf($\mathbb{N} \times \mathbb{N}$) → Imf($\mathbb{N} \times \mathbb{N}$)
    def fix_imf(m):
        return f'Imf(${mb("N")} \\times {mb("N")})'
    content, n = re.subn(r'\$Imf\(\$\\mathbb\{N\}\s*\\times\s*\\mathbb\{N\}\$\)', fix_imf, content)
    changes += n

    # Fix: $|\mathcal{P}($\mathbb{X}$)|$ → $|\mathcal{P}(\mathbb{X})|$
    def fix_pwr_card(m):
        return f'$|\\mathcal{{P}}({mb(m.group(1))})|$'
    content, n = re.subn(r'\$\\mathcal\{P\}\(\$\\mathbb\{(\w+)\}\$\)\|\$', fix_pwr_card, content)
    changes += n

    # Fix: $|\mathcal{P}($\mathbb{X}$)|  (without trailing $)
    def fix_pwr_card2(m):
        return f'$|\\mathcal{{P}}({mb(m.group(1))})|'
    content, n = re.subn(r'\$\\mathcal\{P\}\(\$\\mathbb\{(\w+)\}\$\)\|', fix_pwr_card2, content)
    changes += n

    # Fix: |\text{...}| = |$\mathbb{N}$|$
    def fix_text_card(m):
        return f'|\\text{{{m.group(1)}}}| = |{mb(m.group(2))}|$'
    content, n = re.subn(r'\|\\text\{([^}]+)\}\|\s*=\s*\|\$\\mathbb\{(\w+)\}\$\|\$', fix_text_card, content)
    changes += n

    # Fix: |\text{...}| > |$\mathbb{N}$|$
    def fix_text_card_gt(m):
        return f'|\\text{{{m.group(1)}}}| > |{mb(m.group(2))}|$'
    content, n = re.subn(r'\|\\text\{([^}]+)\}\|\s*>\s*\|\$\\mathbb\{(\w+)\}\$\|\$', fix_text_card_gt, content)
    changes += n

    # Fix: common stray patterns at end of paragraphs
    content, n = re.subn(r'the proof\$\:', 'the proof:', content)
    changes += n
    content, n = re.subn(r'like so\$\:', 'like so:', content)
    changes += n
    content, n = re.subn(r'infinite\$\:', 'infinite:', content)
    changes += n
    content, n = re.subn(r'lattice\$\:', 'lattice:', content)
    changes += n

    # Clean empty $$
    content, n = re.subn(r'\$\$', '', content)
    changes += n

    return content, changes


def main():
    md_files = glob.glob(os.path.join(DOCS_DIR, '**/*.md'), recursive=True)
    total_changes = 0
    fixed_files = []

    for filepath in sorted(md_files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changes = fix_content_pass4(content, filepath)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_files.append((filepath, changes))
            total_changes += changes

    print(f"Pass 4 - Files fixed: {len(fixed_files)}")
    print(f"Total pattern replacements: {total_changes}")
    for fp, n in fixed_files:
        rel = os.path.relpath(fp, os.path.dirname(__file__))
        print(f"  {rel}: {n} fixes")


if __name__ == '__main__':
    main()
