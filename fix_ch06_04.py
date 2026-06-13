"""
Fix math formula issues in ch06/04-equivalence-relations.md and ch06/05-modular-arithmetic.md
Known patterns:
1. $\mathbb{R}$ used where plain R (the relation) is meant
2. Math content straddling $ boundaries (part inside, part outside)
3. Bare subscripts/superscripts outside $...$
4. Unicode math symbols outside $...$
"""
import re

BASE = r"D:\BaiduSyncdisk\ai-agent\my-books\Everything You Always Wanted To Know About Mathematics"

def fix_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {filepath}: {len(replacements)} replacements")

# 04-equivalence-relations.md fixes
fix_04 = [
    # L36: ⌊x⌋= ⌊y⌋  -> proper floor notation
    ("(x, y) $\\in \\mathbb{R} \\Leftrightarrow$⌊x⌋= ⌊y⌋", "$(x, y) \\in R \\Leftrightarrow \\lfloor x \\rfloor = \\lfloor y \\rfloor$"),
    # L36 fix various bare formulas
    ("$y \\in \\mathbb{R}$ | (0, y) $\\in \\mathbb{R}$} = {y $\\in \\mathbb{R}$ | ⌊0⌋= ⌊y⌋} = {y $\\in \\mathbb{R}$ | ⌊y⌋= 0} = {y $\\in \\mathbb{R}$ | 0 $\\leq y$ < 1}",
     "$y \\in \\mathbb{R} \\mid (0, y) \\in R\\} = \\{y \\in \\mathbb{R} \\mid \\lfloor 0 \\rfloor = \\lfloor y \\rfloor\\} = \\{y \\in \\mathbb{R} \\mid \\lfloor y \\rfloor = 0\\} = \\{y \\in \\mathbb{R} \\mid 0 \\leq y < 1\\}$"),
    # Fix [1]R equivalence class
    ("$y \\in \\mathbb{R}$ | (1, y) $\\in \\mathbb{R}$} = {y $\\in \\mathbb{R}$ | 1 $\\leq y$ < 2}",
     "$y \\in \\mathbb{R} \\mid (1, y) \\in R\\} = \\{y \\in \\mathbb{R} \\mid 1 \\leq y < 2\\}$"),
    # L48: bare math in prose
    ("π $\\in[3]R, e \\in$[2]R, -1.5 $\\in$[-2]R, 1 2 $\\in$[0]R",
     "$\\pi \\in [3]_R$, $e \\in [2]_R$, $-1.5 \\in [-2]_R$, $\\frac{1}{2} \\in [0]_R$"),
    # L48: [0]R = [1 broken across lines
    ("[0]R = [1", "$[0]_R = [\\frac{1}{2}]_R$"),
    # L51: Chinese translation bare math
    ("1 \\leq 2 但 2 \\not\\leq 1", "$1 \\leq 2$ 但 $2 \\not\\leq 1$"),
    # L58: A/R definition
    ("A/R = {[x]R | x $\\in A$} Equivalently, A/R = {X \\subseteq A | \\exists x $\\in A$. X = [x]R}",
     "$A/R = \\{[x]_R \\mid x \\in A\\}$. Equivalently, $A/R = \\{X \\subseteq A \\mid \\exists x \\in A.\\, X = [x]_R\\}$"),
    # L65-66: R definition
    ("(x, y) $\\in \\mathbb{R} \\Leftrightarrow$\n⌊x⌋= ⌊y⌋",
     "$(x, y) \\in R \\Leftrightarrow \\lfloor x \\rfloor = \\lfloor y \\rfloor$"),
    # L66: various bare [x]R formulas
    ("[0]R = [0.5]R = [0.999]R", "$[0]_R = [0.5]_R = [0.999]_R$"),
    ("[3.5]R = [3.75]R", "$[3.5]_R = [3.75]_R$"),
    ("[-π]R = [-4]R", "$[-\\pi]_R = [-4]_R$"),
    ("[π]R \\neq [4]R", "$[\\pi]_R \\neq [4]_R$"),
    # L66: x ∈ R bare
    ("x $\\in \\mathbb{R}$ has an associated equivalence class, [x]R",
     "$x \\in \\mathbb{R}$ has an associated equivalence class, $[x]_R$"),
    # L66: R/R
    ("R/R = {..., [-2]R, [-1]R, [0]R, [1]R, [2]R,... }",
     "$\\mathbb{R}/R = \\{\\ldots, [-2]_R, [-1]_R, [0]_R, [1]_R, [2]_R, \\ldots\\}$"),
    # L66: z ≤ y < z+1
    ("[z]R = {y $\\in \\mathbb{R}$ | z $\\leq$ y < z + 1}",
     "$[z]_R = \\{y \\in \\mathbb{R} \\mid z \\leq y < z + 1\\}$"),
    # L67-68: B relation
    ("(x, y) $\\in$\n$B \\Leftrightarrow x$ and y were born in the same month",
     "$(x, y) \\in B \\Leftrightarrow x$ and $y$ were born in the same month"),
    # L75-76: example 6.4.9 with broken $ boundaries
    ("$Example 6.4.9. Consider the set \\mathbb{R} \\times \\mathbb{R} of all ordered-pairs of real numbers. We$\n$define a relation \\mathbb{R} on R\\timesR by declaring when two pairs are related. Specifically, let's say that ((x, y), (u, v)) \\in \\mathbb{R} \\Leftrightarrow x$ = u",
     "Example 6.4.9. Consider the set $\\mathbb{R} \\times \\mathbb{R}$ of all ordered-pairs of real numbers. We define a relation $R$ on $\\mathbb{R} \\times \\mathbb{R}$ by declaring when two pairs are related. Specifically, let's say that $((x, y), (u, v)) \\in R \\Leftrightarrow x = u$"),
    # L76: bare formulas
    ("(1, 3) \\in[(1, 0)]R", "$(1, 3) \\in [(1, 0)]_R$"),
    ("[(x, 0)]R, for some x $\\in \\mathbb{R}$", "$[(x, 0)]_R$, for some $x \\in \\mathbb{R}$"),
    # L82: p x2 + y2 pattern (= sqrt(x^2+y^2))
    ("p x2 + y2 = p u2 + v2", "$\\sqrt{x^2 + y^2} = \\sqrt{u^2 + v^2}$"),
    ("p x2 + y2 describes the distance", "$\\sqrt{x^2 + y^2}$ describes the distance"),
    # L82: R×R/S
    ("(R\\timesR)/R, is$ \"identical\" $to the real number line",
     "$(\\mathbb{R} \\times \\mathbb{R})/R$, is \"identical\" to the real number line $\\mathbb{R}$"),
    ("((x, y), (u, v)) \\in S \\Leftrightarrow p x2 + y2 = p u2 + v2",
     "$((x, y), (u, v)) \\in S \\Leftrightarrow \\sqrt{x^2 + y^2} = \\sqrt{u^2 + v^2}$"),
    # L82: radius description
    ("some real number r $\\geq$0", "some real number $r \\geq 0$"),
    ("(R \\times \\mathbb{R})/S", "$(\\mathbb{R} \\times \\mathbb{R})/S$"),
    # L88: same as question
    ("$as (R \\times \\mathbb{R})/S$", "as $(\\mathbb{R} \\times \\mathbb{R})/S$"),
    # L112: partition relation
    ("F = {Si | i $\\in I$} where the sets Si satisfy Si \\subseteq S and Si \\neq \\emptyset and [ i\\in I Si = S and \\forall i, j \\in I. i \\neq j =$\\Rightarrow Si \\cap Sj = \\emptyset",
     "$F = \\{S_i \\mid i \\in I\\}$ where the sets $S_i$ satisfy $S_i \\subseteq S$ and $S_i \\neq \\emptyset$ and $\\bigcup_{i \\in I} S_i = S$ and $\\forall i, j \\in I.\\, i \\neq j \\Rightarrow S_i \\cap S_j = \\emptyset$"),
    # L118: partition relation formal
    ("(x, y) $\\in \\mathbb{R} \\Leftrightarrow \\exists i \\in I$. {x $\\in Si \\wedgey \\in S$i }",
     "$(x, y) \\in R \\Leftrightarrow \\exists i \\in I.\\, \\{x \\in S_i \\wedge y \\in S_i\\}$"),
    ("(x, x) $\\in \\mathbb{R}$", "$(x, x) \\in R$"),
    # L118: reflexivity/symmetry/transitivity
    ("(x, y) $\\in \\mathbb{R}$", "$(x, y) \\in R$"),
    ("(y, x) $\\in \\mathbb{R}$", "$(y, x) \\in R$"),
    ("(x, y) $\\in \\mathbb{R}$ and $(y, z) \\in R$", "$(x, y) \\in R$ and $(y, z) \\in R$"),
    ("$\\exists j \\in I$. {y $\\in Sj \\wedgez \\in S$j }", "$\\exists j \\in I.\\, \\{y \\in S_j \\wedge z \\in S_j\\}$"),
    ("y $\\in Si \\wedgey \\in Sj.", "$y \\in S_i \\wedge y \\in S_j$."),
    ("Si \\cap Sj = \\emptyset f$or any distinct i, j", "$S_i \\cap S_j = \\emptyset$ for any distinct $i, j$"),
    ("y $\\in \\emptyset$", "$y \\in \\emptyset$"),
    ("x \\in Si and y \\in Si and z \\in Si", "$x \\in S_i$ and $y \\in S_i$ and $z \\in S_i$"),
    ("(x, z) $\\in \\mathbb{R}$", "$(x, z) \\in R$"),
    # L133: parity relation
    ("(a, b) $\\in \\mathbb{R}$ because a has the same parity as itself. Thus, R is reflexive.",
     "$(a, b) \\in R$ because $a$ has the same parity as itself. Thus, $R$ is reflexive."),
]

fix_file(f"{BASE}\\docs\\part-ii\\ch06-relations-modular-arithmetic\\04-equivalence-relations.md", fix_04)
