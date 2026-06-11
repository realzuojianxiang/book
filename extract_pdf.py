"""
PDF → Markdown batch extraction script
Extracts text from the book PDF, maps page ranges to chapter files,
performs cleanup, and writes bilingual-structured Markdown.
"""
import pymupdf
import re
import os
import sys
import io

# Force UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PDF_PATH = "Everything You Always Wanted To Know About Mathematics.pdf"
DOCS_DIR = "docs"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chapter page ranges (1-indexed from TOC → 0-indexed for PyMuPDF)
# Each entry: (start_page_0indexed, end_page_0indexed_exclusive)
CHAPTERS = {
    # Part I
    "part-i/ch01-what-is-mathematics": {
        "sections": [
            # 1.1 Truths and Proofs: pages 13-21
            ("01-truths-and-proofs", 12, 22),
            # 1.2 Exposition Exhibition: pages 22-40
            ("02-exposition-exhibition", 22, 41),
            # 1.3 Review, Redo, Renew: pages 41-60
            ("03-review-redo-renew", 41, 61),
            # 1.4 Quizzical Puzzicles: pages 61-91
            ("04-quizzical-puzzicles", 61, 92),
            # 1.5 It's Wise To Exercise: pages 92-97
            ("05-its-wise-to-exercise", 92, 98),
            # 1.6 Lookahead: pages 98-100
            ("06-lookahead", 98, 101),
        ],
    },
    "part-i/ch02-mathematical-induction": {
        "sections": [
            # 2.1 Introduction: pages 101-103
            ("01-introduction", 100, 104),
            # 2.2 Examples and Discussion: pages 104-118
            ("02-examples-and-discussion", 104, 119),
            # 2.3 Defining Induction: pages 119-128
            ("03-defining-induction", 119, 129),
            # 2.4 Two More Examples: pages 129-137
            ("04-two-more-examples", 129, 138),
            # 2.5 Applications: pages 137-148
            ("05-applications", 138, 148),
            # 2.6-2.8 Summary + Exercises + Lookahead: pages 144-148
            ("06-summary", 144, 149),
        ],
    },
    "part-i/ch03-sets": {
        "sections": [
            # 3.1 Introduction: pages 149-151
            ("01-introduction", 148, 152),
            # 3.2 The Idea of a Set: pages 151-153
            ("02-the-idea-of-a-set", 152, 154),
            # 3.3 Definition and Examples: pages 153-163
            ("03-definition-and-examples", 154, 164),
            # 3.4 Subsets: pages 164-171
            ("04-subsets", 164, 172),
            # 3.5 Set Operations: pages 172-176
            ("05-set-operations", 172, 177),
            # 3.6 Indexed Sets: pages 177-185
            ("06-indexed-sets", 177, 186),
            # 3.7 Cartesian Products: pages 186-189
            ("07-cartesian-products", 186, 190),
            # 3.8 Defining Natural Numbers: pages 190-193
            ("08-defining-natural-numbers", 190, 194),
            # 3.9 Proofs Involving Sets: pages 194-213
            ("09-proofs-involving-sets", 194, 214),
        ],
    },
    "part-i/ch04-logic": {
        "sections": [
            # 4.1 Introduction: pages 215-217
            ("01-introduction", 214, 217),
            # 4.2 Mathematical Statements: pages 217-225
            ("02-mathematical-statements", 217, 225),
            # 4.3 Quantifiers: pages 226-234
            ("03-quantifiers", 226, 235),
            # 4.4 Logical Negation: pages 235-243
            ("04-logical-negation", 235, 244),
            # 4.5 Logical Connectives: pages 244-257
            ("05-logical-connectives", 244, 258),
            # 4.6 Logical Equivalence: pages 258-277
            ("06-logical-equivalence", 258, 278),
            # 4.7 Negation of Any Statement: pages 278-283
            ("07-negation-of-any-statement", 278, 284),
            # 4.8 Truth Values and Sets: pages 284-285
            ("08-truth-values-and-sets", 284, 286),
            # 4.9 Writing Proofs: pages 286-319
            ("09-writing-proofs", 286, 320),
        ],
    },
    "part-i/ch05-rigorous-induction": {
        "sections": [
            # 5.1 Introduction: pages 321-322
            ("01-introduction", 320, 322),
            # 5.2 Regular Induction: pages 322-330
            ("02-regular-induction", 322, 331),
            # 5.3 Other Variants: pages 331-341
            ("03-other-variants", 331, 342),
            # 5.4 Strong Induction: pages 342-356
            ("04-strong-induction", 342, 357),
            # 5.5 Variants of Strong Induction: pages 357-373
            ("05-variants-of-strong-induction", 357, 374),
        ],
    },
    "part-ii/ch06-relations-modular-arithmetic": {
        "sections": [
            # 6.1 Introduction: pages 377-379
            ("01-introduction", 376, 380),
            # 6.2 Abstract Relations: pages 380-392
            ("02-abstract-relations", 380, 393),
            # 6.3 Order Relations: pages 393-398
            ("03-order-relations", 393, 399),
            # 6.4 Equivalence Relations: pages 399-413
            ("04-equivalence-relations", 399, 414),
            # 6.5 Modular Arithmetic: pages 414-466
            ("05-modular-arithmetic", 414, 466),
        ],
    },
    "part-ii/ch07-functions-cardinality": {
        "sections": [
            # 7.1 Introduction: pages 467-469
            ("01-introduction", 466, 470),
            # 7.2 Definition and Examples: pages 469-481
            ("02-definition-and-examples", 470, 482),
            # 7.3 Images and Pre-images: pages 482-496
            ("03-images-and-preimages", 482, 497),
            # 7.4 Properties of Functions: pages 497-521
            ("04-properties-of-functions", 497, 522),
            # 7.5 Compositions and Inverses: pages 511-521
            ("05-compositions-and-inverses", 522, 523),
            # 7.6 Cardinality: pages 522-566
            ("06-cardinality", 523, 566),
        ],
    },
    "part-ii/ch08-combinatorics": {
        "sections": [
            # 8.1 Introduction: pages 567-569
            ("01-introduction", 566, 570),
            # 8.2 Basic Counting Principles: pages 570-588
            ("02-basic-counting-principles", 570, 589),
            # 8.3 Counting Arguments: pages 589-622
            ("03-counting-arguments", 589, 623),
            # 8.4 Counting in Two Ways: pages 623-642
            ("04-counting-in-two-ways", 623, 643),
            # 8.5 Selections with Repetition: pages 643-651
            ("05-selections-with-repetition", 643, 652),
            # 8.6 Pigeonhole Principle: pages 652-656
            ("06-pigeonhole-principle", 652, 657),
            # 8.7 Inclusion/Exclusion: pages 657-670
            ("07-inclusion-exclusion", 657, 670),
        ],
    },
    "part-ii/ch09-definitions-theorems": {
        "sections": [
            # A.1 Sets: pages 671-674
            ("01-sets", 670, 675),
            # A.2 Logic: pages 675-679
            ("02-logic", 675, 680),
            # A.3 Induction: pages 680-681
            ("03-induction", 680, 682),
            # A.4 Relations: pages 682-685
            ("04-relations", 682, 686),
            # A.5 Functions: pages 686-691
            ("05-functions", 686, 692),
            # A.6 Cardinality: pages 692-694
            ("06-cardinality", 692, 695),
            # A.7 Combinatorics: pages 695-698
            ("07-combinatorics", 695, 698),
        ],
    },
}

# Title mapping for section files
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


def clean_text(text):
    """Clean PDF extraction artifacts."""
    # Remove page number lines (standalone numbers)
    text = re.sub(r'\n\d+\n', '\n', text)
    # Remove chapter header lines like "14 CHAPTER 1. WHAT IS MATHEMATICS?"
    text = re.sub(r'\n\d+\s+CHAPTER\s+\d+\.\s+[A-Z\s?]+\n', '\n', text)
    # Remove section header repetitions like "1.1. TRUTHS AND PROOFS 15"
    text = re.sub(r'\n\d+\.\d+\.?\s+[A-Z\s]+\s+\d+\n', '\n', text)
    # Fix ligatures
    text = text.replace('ﬁ', 'fi')
    text = text.replace('ﬂ', 'fl')
    text = text.replace('ﬀ', 'ff')
    text = text.replace('ﬃ', 'ffi')
    text = text.replace('ﬄ', 'ffl')
    # Fix common PDF extraction issues
    text = text.replace('’', "'")  # Right single quote
    text = text.replace('‘', "'")  # Left single quote
    text = text.replace('“', '"')  # Left double quote
    text = text.replace('”', '"')  # Right double quote
    text = text.replace('–', '--')  # En dash
    text = text.replace('—', '---')  # Em dash
    text = text.replace(' ', ' ')  # Non-breaking space
    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def text_to_markdown(text, section_slug):
    """Convert cleaned text to basic Markdown structure."""
    lines = text.split('\n')
    md_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            md_lines.append('')
            continue

        # Detect section headers (e.g., "1.1 Truths and Proofs" or "1.1.1 Triangle Tangle")
        if re.match(r'^\d+\.\d+\.\d+\s+[A-Z]', stripped):
            md_lines.append(f'### {stripped}')
            md_lines.append('')
        elif re.match(r'^\d+\.\d+\s+[A-Z]', stripped):
            md_lines.append(f'## {stripped}')
            md_lines.append('')
        # Detect "Theorem X.Y.Z" or "Definition X.Y.Z" or "Lemma X.Y.Z"
        elif re.match(r'^(Theorem|Definition|Lemma|Corollary|Proposition|Axiom|Claim|Fact)\s+\d+', stripped):
            md_lines.append(f'<div class="def-theorem" markdown>')
            md_lines.append(f'**{stripped}**')
            md_lines.append(f'</div>')
            md_lines.append('')
        # Detect "Proof." lines
        elif stripped.startswith('Proof.') or stripped.startswith('Proof:'):
            md_lines.append(f'<div class="def-proof" markdown>')
            md_lines.append(f'*Proof.* {stripped[6:].strip()}')
            md_lines.append(f'</div>')
            md_lines.append('')
        # Detect "Example X.Y.Z" or "Solution."
        elif re.match(r'^Example\s+\d+', stripped):
            md_lines.append(f'??? example "{stripped}"')
            md_lines.append('')
        elif stripped.startswith('Solution.'):
            md_lines.append(f'    {stripped}')
            md_lines.append('')
        # Regular text
        else:
            md_lines.append(stripped)

    return '\n'.join(md_lines)


def extract_section(doc, start_page, end_page):
    """Extract text from a range of pages."""
    texts = []
    for i in range(start_page, min(end_page, doc.page_count)):
        page_text = doc[i].get_text()
        if page_text.strip():
            texts.append(page_text)
    return '\n'.join(texts)


def main():
    pdf_path = os.path.join(BASE_DIR, PDF_PATH)
    docs_dir = os.path.join(BASE_DIR, DOCS_DIR)

    print(f"Opening PDF: {pdf_path}")
    doc = pymupdf.open(pdf_path)
    print(f"Total pages: {doc.page_count}")

    total_sections = 0
    processed_sections = 0
    skipped_sections = 0

    for chapter_path, chapter_data in CHAPTERS.items():
        for section_slug, start_page, end_page in chapter_data["sections"]:
            total_sections += 1
            filepath = os.path.join(docs_dir, chapter_path, f"{section_slug}.md")

            # Skip files that already have substantial content (manually written)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    existing = f.read()
                # If file already has real translated content (not just template), skip
                if len(existing) > 2000 and '> 🇨🇳' in existing and 'TODO' not in existing:
                    print(f"  SKIP (has real content): {filepath}")
                    skipped_sections += 1
                    continue

            # Extract and process text
            raw_text = extract_section(doc, start_page, end_page)
            cleaned = clean_text(raw_text)
            title = SECTION_TITLES.get(section_slug, section_slug.replace('-', ' ').title())

            # Build the bilingual Markdown file
            # Split into paragraphs for bilingual insertion
            paragraphs = [p.strip() for p in cleaned.split('\n\n') if p.strip()]

            md_content = f"---\ntitle: {title}\n---\n\n"
            md_content += f"# {title}\n\n"

            for para in paragraphs:
                # Skip very short fragments (page numbers, headers)
                if len(para) < 10:
                    continue
                # Skip if it's just a number
                if re.match(r'^\d+$', para.strip()):
                    continue

                md_content += f"{para}\n\n"
                md_content += f"> 🇨🇳 TODO: 待翻译\n\n"

            # Write the file
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            processed_sections += 1
            char_count = len(cleaned)
            print(f"  OK: {chapter_path}/{section_slug}.md ({char_count} chars, pages {start_page+1}-{end_page})")

    doc.close()
    print(f"\nDone! Processed {processed_sections}/{total_sections} sections ({skipped_sections} skipped)")


if __name__ == "__main__":
    main()
