"""
PDF → Markdown REFINED extraction script
Enhanced cleanup: removes page headers/footers, fixes math formatting,
converts common patterns to LaTeX notation.
"""
import pymupdf
import re
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PDF_PATH = "Everything You Always Wanted To Know About Mathematics.pdf"
DOCS_DIR = "docs"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chapter page ranges (0-indexed for PyMuPDF)
CHAPTERS = {
    "part-i/ch01-what-is-mathematics": [
        ("01-truths-and-proofs", 12, 22),
        ("02-exposition-exhibition", 22, 41),
        ("03-review-redo-renew", 41, 61),
        ("04-quizzical-puzzicles", 61, 92),
        ("05-its-wise-to-exercise", 92, 98),
        ("06-lookahead", 98, 101),
    ],
    "part-i/ch02-mathematical-induction": [
        ("01-introduction", 100, 104),
        ("02-examples-and-discussion", 104, 119),
        ("03-defining-induction", 119, 129),
        ("04-two-more-examples", 129, 138),
        ("05-applications", 138, 148),
        ("06-summary", 144, 149),
    ],
    "part-i/ch03-sets": [
        ("01-introduction", 148, 152),
        ("02-the-idea-of-a-set", 152, 154),
        ("03-definition-and-examples", 154, 164),
        ("04-subsets", 164, 172),
        ("05-set-operations", 172, 177),
        ("06-indexed-sets", 177, 186),
        ("07-cartesian-products", 186, 190),
        ("08-defining-natural-numbers", 190, 194),
        ("09-proofs-involving-sets", 194, 214),
    ],
    "part-i/ch04-logic": [
        ("01-introduction", 214, 217),
        ("02-mathematical-statements", 217, 225),
        ("03-quantifiers", 226, 235),
        ("04-logical-negation", 235, 244),
        ("05-logical-connectives", 244, 258),
        ("06-logical-equivalence", 258, 278),
        ("07-negation-of-any-statement", 278, 284),
        ("08-truth-values-and-sets", 284, 286),
        ("09-writing-proofs", 286, 320),
    ],
    "part-i/ch05-rigorous-induction": [
        ("01-introduction", 320, 322),
        ("02-regular-induction", 322, 331),
        ("03-other-variants", 331, 342),
        ("04-strong-induction", 342, 357),
        ("05-variants-of-strong-induction", 357, 374),
    ],
    "part-ii/ch06-relations-modular-arithmetic": [
        ("01-introduction", 376, 380),
        ("02-abstract-relations", 380, 393),
        ("03-order-relations", 393, 399),
        ("04-equivalence-relations", 399, 414),
        ("05-modular-arithmetic", 414, 466),
    ],
    "part-ii/ch07-functions-cardinality": [
        ("01-introduction", 466, 470),
        ("02-definition-and-examples", 470, 482),
        ("03-images-and-preimages", 482, 497),
        ("04-properties-of-functions", 497, 522),
        ("05-compositions-and-inverses", 522, 523),
        ("06-cardinality", 523, 566),
    ],
    "part-ii/ch08-combinatorics": [
        ("01-introduction", 566, 570),
        ("02-basic-counting-principles", 570, 589),
        ("03-counting-arguments", 589, 623),
        ("04-counting-in-two-ways", 623, 643),
        ("05-selections-with-repetition", 643, 652),
        ("06-pigeonhole-principle", 652, 657),
        ("07-inclusion-exclusion", 657, 670),
    ],
    "part-ii/ch09-definitions-theorems": [
        ("01-sets", 670, 675),
        ("02-logic", 675, 680),
        ("03-induction", 680, 682),
        ("04-relations", 682, 686),
        ("05-functions", 686, 692),
        ("06-cardinality", 692, 695),
        ("07-combinatorics", 695, 698),
    ],
}

SECTION_TITLES = {
    "01-truths-and-proofs": "1.1 Truths and Proofs",
    "02-exposition-exhibition": "1.2 Exposition Exhibition",
    "03-review-redo-renew": "1.3 Review, Redo, Renew",
    "04-quizzical-puzzicles": "1.4 Quizzical Puzzicles",
    "05-its-wise-to-exercise": "1.5 It's Wise To Exercise",
    "06-lookahead": "1.6 Lookahead",
    "01-introduction": "Introduction",
    "02-examples-and-discussion": "Examples and Discussion",
    "03-defining-induction": "Defining Induction",
    "04-two-more-examples": "Two More (Different) Examples",
    "05-applications": "Applications",
    "06-summary": "Summary",
    "02-the-idea-of-a-set": "The Idea of a Set",
    "03-definition-and-examples": "Definition and Examples",
    "04-subsets": "Subsets",
    "05-set-operations": "Set Operations",
    "06-indexed-sets": "Indexed Sets",
    "07-cartesian-products": "Cartesian Products",
    "08-defining-natural-numbers": "Defining the Natural Numbers",
    "09-proofs-involving-sets": "Proofs Involving Sets",
    "02-mathematical-statements": "Mathematical Statements",
    "03-quantifiers": "Quantifiers: Existential and Universal",
    "04-logical-negation": "Logical Negation of Quantified Statements",
    "05-logical-connectives": "Logical Connectives",
    "06-logical-equivalence": "Logical Equivalence",
    "07-negation-of-any-statement": "Negation of Any Mathematical Statement",
    "08-truth-values-and-sets": "Truth Values and Sets",
    "09-writing-proofs": "Writing Proofs: Strategies and Examples",
    "02-regular-induction": "Regular Induction",
    "03-other-variants": "Other Variants of Induction",
    "04-strong-induction": "Strong Induction",
    "05-variants-of-strong-induction": "Variants of Strong Induction",
    "02-abstract-relations": "Abstract (Binary) Relations",
    "03-order-relations": "Order Relations",
    "04-equivalence-relations": "Equivalence Relations",
    "05-modular-arithmetic": "Modular Arithmetic",
    "02-definition-and-examples": "Definition and Examples",
    "03-images-and-preimages": "Images and Pre-images",
    "04-properties-of-functions": "Properties of Functions",
    "05-compositions-and-inverses": "Compositions and Inverses",
    "06-cardinality": "Cardinality",
    "02-basic-counting-principles": "Basic Counting Principles",
    "03-counting-arguments": "Counting Arguments",
    "04-counting-in-two-ways": "Counting in Two Ways",
    "05-selections-with-repetition": "Selections with Repetition",
    "06-pigeonhole-principle": "Pigeonhole Principle",
    "07-inclusion-exclusion": "Inclusion/Exclusion",
    "01-sets": "A.1 Sets",
    "02-logic": "A.2 Logic",
    "03-induction": "A.3 Induction",
    "04-relations": "A.4 Relations",
    "05-functions": "A.5 Functions",
    "06-cardinality": "A.6 Cardinality",
    "07-combinatorics": "A.7 Combinatorics",
}

# Regex patterns for page header/footer removal
# Pattern: "XX  CHAPTER Y. TITLE" at start of a line
RE_CHAPTER_HEADER = re.compile(
    r'^\d+\s+CHAPTER\s+\d+\.\s+[A-Z\s?]+$', re.MULTILINE
)
# Pattern: "X.Y.  SECTION TITLE  XX" (section header with page number)
RE_SECTION_FOOTER = re.compile(
    r'^\d+\.\d+\.\s+[A-Z\s]+\s+\d+$', re.MULTILINE
)
# Pattern: standalone page number on its own line
RE_STANDALONE_NUM = re.compile(r'^\d{1,3}$', re.MULTILINE)
# Pattern: "Part I/II" headers
RE_PART_HEADER = re.compile(
    r'^Part\s+(I{1,2}|1|2)\s+', re.MULTILINE
)


def clean_text(text):
    """Clean PDF extraction artifacts aggressively."""
    # Fix ligatures FIRST (before any regex)
    text = text.replace('ﬁ', 'fi')
    text = text.replace('ﬂ', 'fl')
    text = text.replace('ﬃ', 'ffi')
    text = text.replace('ﬄ', 'ffl')
    text = text.replace('ﬀ', 'ff')

    # Fix quotation marks
    text = text.replace('’', "'")  # Right single quote
    text = text.replace('‘', "'")  # Left single quote
    text = text.replace('“', '"')  # Left double quote
    text = text.replace('”', '"')  # Right double quote
    text = text.replace('–', '--')  # En dash
    text = text.replace('—', '---')  # Em dash
    text = text.replace(' ', ' ')  # Non-breaking space

    # Remove page headers/footers
    text = RE_CHAPTER_HEADER.sub('', text)
    text = RE_SECTION_FOOTER.sub('', text)
    text = RE_STANDALONE_NUM.sub('', text)

    # Remove "Part I/II Learning to..." standalone lines
    text = re.sub(r'^Part\s+I+\s+Learning\s+.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\s*$', '', text, flags=re.MULTILINE)  # stray numbers

    # Collapse whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+$', '', text, flags=re.MULTILINE)  # trailing spaces

    return text.strip()


def format_math_paragraphs(text):
    """
    Attempt to rejoin lines that were broken mid-sentence by PDF extraction.
    PDFs often break paragraphs at line boundaries, producing one-line-per-line.
    We want to rejoin these into proper paragraphs.
    """
    lines = text.split('\n')
    result = []
    buffer = ''

    for line in lines:
        stripped = line.strip()
        if not stripped:
            # End of paragraph - flush buffer
            if buffer:
                result.append(buffer)
                buffer = ''
            result.append('')
            continue

        # Check if this line starts a structural element
        is_structural = bool(re.match(
            r'^(#{1,6}\s|\d+\.\d+|Theorem|Definition|Lemma|Corollary|'
            r'Proposition|Axiom|Claim|Fact|Proof[.:]|Example|Solution[.:]|'
            r'Question|Exercise|Remark|Note:|WARNING|TODO|\*|>|<div|</div|---)',
            stripped
        ))

        if is_structural:
            if buffer:
                result.append(buffer)
                buffer = ''
            result.append(stripped)
        elif buffer:
            # Continuation line - join with space
            # Check if previous line ended with hyphen (word break)
            if buffer.endswith('-') and not buffer.endswith('--'):
                buffer = buffer[:-1] + stripped
            else:
                buffer = buffer + ' ' + stripped
        else:
            buffer = stripped

    if buffer:
        result.append(buffer)

    return '\n'.join(result)


def add_bilingual_markers(text):
    """Add Chinese translation TODO markers after each paragraph."""
    paragraphs = text.split('\n\n')
    result = []

    for para in paragraphs:
        stripped = para.strip()
        if not stripped:
            continue
        # Skip very short fragments
        if len(stripped) < 15:
            continue

        result.append(stripped)
        result.append('')
        result.append('> 🇨🇳 TODO: 待翻译')
        result.append('')

    return '\n\n'.join(result)


def enhance_markdown(text):
    """Convert detected patterns to Markdown elements."""
    # Theorem/Definition environments
    text = re.sub(
        r'^(Theorem \d+\.\d+\.\d+.*?)$',
        r'<div class="def-theorem" markdown>\n**\1**\n</div>',
        text, flags=re.MULTILINE
    )
    text = re.sub(
        r'^(Definition \d+\.\d+\.\d+.*?)$',
        r'<div class="def-definition" markdown>\n**\1**\n</div>',
        text, flags=re.MULTILINE
    )
    text = re.sub(
        r'^(Lemma \d+\.\d+\.\d+.*?)$',
        r'<div class="def-theorem" markdown>\n**\1**\n</div>',
        text, flags=re.MULTILINE
    )
    text = re.sub(
        r'^(Corollary \d+\.\d+\.\d+.*?)$',
        r'<div class="def-theorem" markdown>\n**\1**\n</div>',
        text, flags=re.MULTILINE
    )

    # Proof blocks
    text = re.sub(
        r'^Proof\.\s*(.*?)$',
        r'<div class="def-proof" markdown>\n*Proof.* \1\n</div>',
        text, flags=re.MULTILINE
    )

    # Section headers with number patterns
    text = re.sub(
        r'^(\d+\.\d+\.\d+)\s+(.+)$',
        r'### \1 \2',
        text, flags=re.MULTILINE
    )
    text = re.sub(
        r'^(\d+\.\d+)\s+(.+)$',
        r'## \1 \2',
        text, flags=re.MULTILINE
    )

    return text


def extract_pages(doc, start, end):
    """Extract text from page range."""
    parts = []
    for i in range(start, min(end, doc.page_count)):
        page = doc[i]
        page_text = page.get_text()
        if page_text.strip():
            parts.append(page_text)
    return '\n'.join(parts)


def main():
    pdf_path = os.path.join(BASE_DIR, PDF_PATH)
    docs_dir = os.path.join(BASE_DIR, DOCS_DIR)

    print(f"Opening PDF: {pdf_path}")
    doc = pymupdf.open(pdf_path)
    print(f"Total pages: {doc.page_count}")

    total = 0
    ok = 0
    skip = 0

    for chapter_path, sections in CHAPTERS.items():
        for slug, start_page, end_page in sections:
            total += 1
            filepath = os.path.join(docs_dir, chapter_path, f"{slug}.md")

            # Skip manually-written files with real bilingual content
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if len(content) > 2000 and '🇨🇳' in content and 'TODO' not in content:
                    print(f"  SKIP (real content): {chapter_path}/{slug}")
                    skip += 1
                    continue

            # Extract, clean, format
            raw = extract_pages(doc, start_page, end_page)
            cleaned = clean_text(raw)
            rejoined = format_math_paragraphs(cleaned)
            enhanced = enhance_markdown(rejoined)
            bilingual = add_bilingual_markers(enhanced)

            title = SECTION_TITLES.get(slug, slug.replace('-', ' ').title())

            # Build final file
            md = f"---\ntitle: {title}\n---\n\n# {title}\n\n{bilingual}\n"

            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md)

            ok += 1
            print(f"  OK: {chapter_path}/{slug}.md ({len(cleaned)} chars)")

    doc.close()
    print(f"\nDone! {ok}/{total} sections processed ({skip} skipped)")


if __name__ == "__main__":
    main()
