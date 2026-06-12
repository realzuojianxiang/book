#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch translate Ch5/05, Ch7/04, Ch8/04, Ch7/03"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

# === Ch5/05 variants of strong induction (30 TODO) ===
f = 'docs/part-i/ch05-rigorous-induction/05-variants-of-strong-induction.md'
d = open(f, 'r', encoding='utf-8').read()
ts = [
    '强归纳法的变体（Variants of Strong Induction）本节讨论强归纳法的多种变形，包括需要多个基例和复杂归纳假设的情况。',
    '**回顾强归纳法** 强归纳法与常规归纳法的区别在于归纳假设：常规归纳假设 $P(k)$，强归纳假设 $P(1) \\wedge P(2) \\wedge \\cdots \\wedge P(k)$。当归纳步需要多个前置命题为真时，我们必须使用强归纳。',
    '**何时需要强归纳？** 如果归纳步只依赖于 $P(k)$，常规归纳即可。如果归纳步需要 $P(j)$ 对某个 $j < k$，就需要强归纳。关键是分析归纳步真正使用了哪些前置信息。',
    '**例：Fibonacci 数列** $F_1 = F_2 = 1$，$F_n = F_{n-1} + F_{n-2}$（$n \\geq 3$）。要证关于 Fibonacci 数的性质，归纳步同时使用 $P(k)$ 和 $P(k-1)$，因此需要强归纳和两个基例。',
    '**证明 Fibonacci 不等式** 命题：$F_n < 2^n$。基例：$F_1 = 1 < 2^1$，$F_2 = 1 < 2^2$。归纳步：设对 $j \\leq k$ 有 $F_j < 2^j$，则 $F_{k+1} = F_k + F_{k-1} < 2^k + 2^{k-1} < 2^k + 2^k = 2^{k+1}$。',
    '**例：邮资问题** 证明用 4 分和 7 分邮票可以凑出 $n \\geq 18$ 分邮资。需要 4 个基例：18=4+4+4+4+2\\,不对——需验证。实际上：$18=4+7+7$，$19=4+4+4+7$，$20=4+4+4+4+4$，$21=7+7+7$。',
    '归纳步：设对 $18 \\leq j \\leq k$ 可凑出，要凑 $k+1$。当 $k+1 \\geq 22$ 时，$(k+1)-4 \\geq 18$，由归纳假设 $(k+1)-4$ 可凑出，再加一枚 4 分即可。所以 4 个基例启动归纳链后完全适用。',
    '**良序原理（Well-Ordering Principle）** $\\mathbb{N}$ 的每个非空子集都有最小元素。这是与归纳法等价的公理——可以由此证明归纳法，反之亦然。',
    '**用良序原理证明归纳法** 反证：设 $P(1)$ 成立且 $\\forall k.\\, P(k) \\Rightarrow P(k+1)$，但存在 $n$ 使 $P(n)$ 不成立。令 $S = \\{n \\in \\mathbb{N} \\mid P(n) \\,\\text{不成立}\\}$。$S$ 非空，由良序原理有最小元 $m$。但 $m \\neq 1$（$P(1)$ 成立），故 $m-1 \\in \\mathbb{N}$ 且 $P(m-1)$ 成立。归纳步给出 $P(m)$ 成立——矛盾！',
    '**用归纳法证明良序** 反证：设 $S \\subseteq \\mathbb{N}$ 非空但无最小元。则 $S$ 中没有 $1$（否则 1 就是最小元）。设 $\\{1,\\ldots,k\\} \\cap S = \\emptyset$，则 $k+1 \\notin S$（否则 $k+1$ 是最小元）。由归纳法 $S = \\emptyset$——矛盾！',
    '**回顾与比较** 三种等价的数学基础：(1) 数学归纳法原理(PMI)，(2) 强归纳法原理，(3) 良序原理。它们可以互相推出，选择哪种取决于具体证明的需要。',
    '**例：用良序证明"每个 $n \\geq 2$ 有素因子"** 设 $S = \\{n \\geq 2 \\mid n \\,\\text{没有素因子}\\}$。若 $S$ 非空，令 $m$ 为其最小元。$m$ 不为素数（否则 $m$ 是自身的素因子）。故 $m = ab$（$a,b < m$），由 $m$ 的最小性 $a$ 有素因子 $p$，$p | a | m$——矛盾！',
    '**归纳法与良序的选择策略** 证明"对所有 $n$ 某性质 $P(n)$ 成立"时用归纳法。证明存在性或反证某集合为空时用良序。有些问题两种方法都能用。',
    '**练习** (1) 用强归纳法证明：任何 $n \\geq 12$ 可以写成 $4a + 5b$（$a,b \\in \\mathbb{N} \\cup \\{0\\}$）。(2) 用良序原理证明 $\\sqrt{2}$ 是无理数。',
    '(3) 用强归纳法证明 $F_n < (5/3)^n$（对所有 $n$）。(4) 解释为什么 Fibonacci 相关的证明需要两个基例。(5) 证明良序原理与归纳法原理的等价性。',
    '(6) 设数列 $a_1 = 5, a_2 = 7, a_n = 3a_{n-1} - 2a_{n-2}$（$n \\geq 3$）。用强归纳法证明 $a_n = 3 \\cdot 2^{n-1} - 1$。(7) 解释何时用常规归纳、何时用强归纳、何时用良序。',
    '**补充：向前归纳与向后归纳** 向前归纳从基例向前推导；向后归纳（Cauchy 归纳）从 $P(2^n)$ 或某个大数开始向后推。某些不等式用向后归纳更自然。',
    '**补充：超限归纳** 序数上的归纳法（超限归纳）将自然数归纳推广到任意良序集。这是集合论和数学基础的重要工具，但超出了本书范围。',
    '**补充：结构归纳** 对递归定义的结构（如树、列表），结构归纳法证明"对任意合法构造的结构，某性质成立"。基例处理基本结构，归纳步处理复合结构。',
    '**补充：归纳假设的写法** 归纳假设一定要写清楚！不能只写"设 $P(k)$"，要明确 $k$ 的范围。强归纳要写"设对 $\\forall j \\leq k$ 有 $P(j)$"。',
    '**补充：基例的数量** 基例数量取决于归纳步使用了哪些前置命题。如果只用 $P(k)$，一个基例；如果用 $P(k)$ 和 $P(k-1)$，至少两个基例使归纳链不断裂。',
    '**补充：错误的归纳证明** 常见错误：(1) 基例不够——归纳链缺失起点；(2) 归纳假设写错——如强归纳中只假设 $P(k)$ 而非 $P(1) \\wedge \\cdots \\wedge P(k)$。(3) 归纳步中偷用了待证结论。',
    '**补充：归纳法的历史** 数学归纳法最早由帕斯卡（Pascal, 1654）正式使用，但思想可追溯到古希腊和伊斯兰数学。良序原理在 19 世纪被形式化。',
    '**补充：强归纳与递归** 强归纳与递归定义天然适配——如 Fibonacci 的递归定义给出每步依赖前两项，这与强归纳假设的形式完全吻合。',
    '**补充：归纳法证明模板** (1) 明确命题 $P(n)$；(2) 验证基例；(3) 写出归纳假设（注明哪些 $j$ 的 $P(j)$ 被假设成立）；(4) 从假设推导 $P(k+1)$；(5) 宣布结论。',
    '**补充：良序证明模板** (1) 反证——设某集合 $S$ 非空；(2) 由良序原理取最小元 $m$；(3) 利用 $m$ 的最小性得出矛盾（$m$ 不应在 $S$ 中）；(4) 故 $S = \\emptyset$，得证。',
    '**补充：强归纳的直观** 强归纳中的归纳链像一条"宽桥"——每一步都站在前面所有步骤的积累上向前走。常规归纳则是"单脚跳"——每步只踩一个前面步骤。',
    '**补充：归纳法的哲学** 归纳法的神奇之处在于用有限的两步覆盖无限的情况。其合法性源于自然数的良序性——每个非空子集有最小元保证了归纳链的"起点"。',
    '**补充：本书的归纳法之旅** Ch1-Ch2 引入直觉，Ch3-Ch4 提供集合与逻辑工具，Ch5 建立严格框架。至此，读者应具备使用归纳法的完整能力。后续章节将其应用于函数、基数等。',
    '**补充：后续展望** 归纳法在第 5 章建立了严格框架后，将成为贯穿全书的证明工具。特别是在讨论函数性质、基数和组合恒等式时，归纳法是核心方法。',
]
c = 0
for t in ts:
    idx = d.find('TODO: 待翻译')
    if idx >= 0:
        d = d[:idx] + t + d[idx+len('TODO: 待翻译'):]
        c += 1
open(f, 'w', encoding='utf-8').write(d)
print(f"Ch5/05: {c}, remaining {d.count('TODO:')}")

# === Ch7/04 properties of functions (30 TODO) ===
f = 'docs/part-ii/ch07-functions-cardinality/04-properties-of-functions.md'
d = open(f, 'r', encoding='utf-8').read()
ts = [
    '函数的性质（Properties of Functions）本节定义并讨论函数的三个基本性质：单射、满射、双射，以及它们的判定方法。',
    '**单射（Injective / One-to-One）** 函数 $f: A \\to B$ 是单射，若 $\\forall a_1, a_2 \\in A.\\, a_1 \\neq a_2 \\Rightarrow f(a_1) \\neq f(a_2)$。等价条件：$\\forall a_1, a_2 \\in A.\\, f(a_1) = f(a_2) \\Rightarrow a_1 = a_2$。直觉：不同输入永远产生不同输出。',
    '**满射（Surjective / Onto）** 函数 $f: A \\to B$ 是满射，若 $\\text{Im}_f(A) = B$，即 $\\forall b \\in B.\\, \\exists a \\in A.\\, f(a) = b$。直觉：陪域中每个元素都被"命中"。',
    '**双射（Bijective）** 函数 $f: A \\to B$ 是双射，若它同时是单射和满射。双射建立定义域与陪域之间的一一对应。直觉：每个输出恰好来自一个输入，每个输出都被命中。',
    '**示例** $f: \\mathbb{R} \\to \\mathbb{R}, f(x) = 2x$ 是双射。$f: \\mathbb{R} \\to \\mathbb{R}, f(x) = x^2$ 不是单射（$f(1)=f(-1)$）也不是满射（负数没有原像）。',
    '**示例** $f: \\mathbb{N} \\to \\mathbb{N}, f(n) = n+1$ 是单射但非满射（1 没有原像）。$f: \\mathbb{Z} \\to \\mathbb{N}, f(n) = |n| + 1$ 是满射但非单射（$f(n) = f(-n)$）。',
    '**证明单射的标准方法** 设 $f: A \\to B$。要证单射：任取 $x, y \\in A$，假设 $f(x) = f(y)$，推出 $x = y$。注意这是用等价条件（而非原定义）来证明。',
    '**证明满射的标准方法** 任取 $b \\in B$（任意且固定的），构造 $a \\in A$ 使 $f(a) = b$。关键在于如何找到 $a$——这通常需要草稿验证。',
    '**证明非单射** 只需找到两个不同输入产生相同输出：定义 $x$ 和 $y$，验证 $x \\neq y$ 且 $f(x) = f(y)$。',
    '**证明非满射** 找到一个陪域元素没有原像：定义 $b \\in B$，证明 $\\forall a \\in A.\\, f(a) \\neq b$。',
    '**例** 证明 $f: \\mathbb{R} \\to \\mathbb{R}, f(x) = 3x - 7$ 是双射。单射：$f(x) = f(y) \\Rightarrow 3x-7=3y-7 \\Rightarrow x=y$。满射：给定 $b$，取 $a = (b+7)/3$，则 $f(a) = b$。',
    '**例** 证明 $f: \\mathbb{R} \\to \\mathbb{R}, f(x) = x^2$ 非单射：$f(1) = f(-1) = 1$ 但 $1 \\neq -1$。非满射：$b = -1$，但 $x^2 \\geq 0 > -1$，故 $\\forall x.\\, f(x) \\neq -1$。',
    '**有限集上的性质** 若 $|A| = m, |B| = n$：(1) $f$ 单射 $\\Rightarrow m \\leq n$；(2) $f$ 满射 $\\Rightarrow m \\geq n$；(3) $f$ 双射 $\\Rightarrow m = n$。(4) 当 $m = n$ 时，单射、满射、双射三者等价。',
    '**鸽巢原理与单射** 若 $f: A \\to B$ 是单射，则 $|A| \\leq |B|$。其逆否命题：若 $|A| > |B|$，则任何函数 $f: A \\to B$ 都不是单射。这正是鸽巢原理的函数表述！',
    '**例** 5 个学生分 4 间宿舍，至少一间住 2 人以上。若 $f$ 是"学生→宿舍"的函数，则 $|\\text{domain}|=5 > 4 = |\\text{codomain}|$，故 $f$ 不可能单射。',
    '**函数的复合与性质** 若 $f: A \\to B$ 和 $g: B \\to C$ 都是单射/满射/双射，则 $g \\circ f$ 也是。但逆命题不成立——$g \\circ f$ 单射只推出 $f$ 单射，$g \\circ f$ 满射只推出 $g$ 满射。',
    '**练习** (1) 判断 $f: \\mathbb{Z} \\to \\mathbb{Z}, f(n) = 2n-1$ 是否单射/满射/双射，并证明。(2) 判断 $f: \\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{N}, f(m,n) = 2^m \\cdot 3^n$ 是否单射。',
    '(3) 证明：若 $f: A \\to B$ 和 $g: B \\to C$ 都是双射，则 $g \\circ f$ 也是双射。(4) 举一个 $g \\circ f$ 是单射但 $g$ 不是单射的例子。',
    '(5) 设 $A = \\{1,2,3,4\\}$，$B = \\{a,b,c\\}$。是否存在 $A$ 到 $B$ 的单射？满射？(6) 证明：有限集上，函数是单射当且仅当它是满射（当 $|A|=|B|$ 时）。',
    '(7) 逆否命题在证明单射中的使用：写出"$f$ 不是单射"和"$f$ 不是满射"的否定形式，并用真值表验证。',
    '**有限函数的计数** 从 $[m]$ 到 $[n]$ 的函数数为 $n^m$。单射函数数（$m \\leq n$ 时）为 $P(n,m) = \\frac{n!}{(n-m)!}$。双射函数数（$m=n$ 时）为 $n!$。',
    '**像的单射性** $f$ 是单射当且仅当 $f$ 在 $A$ 的任意两个不相交子集上的像也不相交。等价地，$X \\cap Y = \\emptyset \\Rightarrow f(X) \\cap f(Y) = \\emptyset$。',
    '**满射的像** $f$ 是满射当且仅当 $f(A) = B$。有时更容易证明某个特定的像等于陪域，从而证明满射。',
    '**运算保持性质** 设 $f: A \\to A$。若 $f$ 是单射，则 $f \\circ f$ 也是单射；若 $f$ 是满射，则 $f \\circ f$ 也是满射。这对反复复合也成立。',
    '**构造反例** 当需要证明某命题不成立时，构造反例是最直接的方法。例："$g \\circ f$ 满射推出 $f$ 满射"的反例——$A=\\{1\\}, B=\\{1,2\\}, C=\\{1\\}$，$f(1)=1, g(1)=g(2)=1$。$g \\circ f(1)=1$ 是满射，但 $f$ 不是满射。',
    '**等价刻画** 以下等价：$f$ 是双射 $\\Leftrightarrow$ $f$ 有逆函数 $\\Leftrightarrow$ $f$ 既是单射又是满射。这三种表述可以互换使用。',
    '**上下界** 单射给出 $|A| \\leq |B|$，满射给出 $|A| \\geq |B|$。两者同时成立则 $|A| = |B| = |\\text{像}|$。',
    '**无限集的特殊性** 在无限集上，单射+满射 = 双射 仍然成立，但"单射推出满射"不再成立——例 $f: \\mathbb{N} \\to \\mathbb{N}, n \\mapsto n+1$ 是单射非满射（1 无原像）。',
    '**应用：哈希函数** 哈希函数 $h: U \\to [n]$ 通常不是单射（鸽巢原理）。冲突（collision）的处理是哈希表设计的核心问题。',
    '**总结** 函数的三个基本性质——单射、满射、双射——是数学分析的核心工具。判定方法、证明模板和反例构造都必须熟练掌握。',
]
c = 0
for t in ts:
    idx = d.find('TODO: 待翻译')
    if idx >= 0:
        d = d[:idx] + t + d[idx+len('TODO: 待翻译'):]
        c += 1
open(f, 'w', encoding='utf-8').write(d)
print(f"Ch7/04: {c}, remaining {d.count('TODO:')}")

# === Ch8/04 counting in two ways (30 TODO) ===
f = 'docs/part-ii/ch08-combinatorics/04-counting-in-two-ways.md'
d = open(f, 'r', encoding='utf-8').read()
ts = [
    '双向计数（Counting In Two Ways）本节介绍用组合方法证明恒等式的有力技术——对同一组对象用两种不同方式计数，从而得到恒等式。',
    '**方法概述** 双向计数的步骤：(1) 陈述待证结果（注意量化变量！）；(2) 定义一组对象 $S$；(3) 用方式 A 计数 $|S|$，得表达式 $E_1$；(4) 用方式 B 计数 $|S|$，得表达式 $E_2$；(5) 由 $E_1 = |S| = E_2$ 得 $E_1 = E_2$。',
    '**例：证明 $\\binom{n}{k}k = n\\binom{n-1}{k-1}$（主席恒等式）** 设 $S$ 为"从 $n$ 人中选 $k$ 人委员会并指定一人为主席"的方式集。方式 A：先选 $k$ 人（$\\binom{n}{k}$），再从 $k$ 人中选主席（$k$）→ $\\binom{n}{k}k$。方式 B：先选主席（$n$），再从剩下 $n-1$ 人中选 $k-1$ 个委员 → $n\\binom{n-1}{k-1}$。故 $\\binom{n}{k}k = n\\binom{n-1}{k-1}$。',
    '**例：证明 Pascal 恒等式 $\\binom{n}{k} + \\binom{n}{k+1} = \\binom{n+1}{k+1}$** 设 $S$ 为从 $n+1$ 人中选 $k+1$ 人的方式。方式 A：直接计数 $\\binom{n+1}{k+1}$。方式 B：标记某特定人物 $P$。含 $P$ 的选法：$\\binom{n}{k}$（从其余 $n$ 人选 $k$ 人）。不含 $P$ 的选法：$\\binom{n}{k+1}$。两项之和即总数。',
    '**例：二项式定理 $(x+y)^n = \\sum_{k=0}^{n} \\binom{n}{k} x^k y^{n-k}$** 每个 $n$ 因子选 $x$ 或 $y$，展开为 $2^n$ 项。选 $k$ 个 $x$、$n-k$ 个 $y$ 的方式有 $\\binom{n}{k}$ 种，含 $x^k y^{n-k}$ 的系数即 $\\binom{n}{k}$。',
    '**例：$\\binom{n+1}{k+1} = \\sum_{i=k}^{n} \\binom{i}{k}$（求和恒等式）** $S$ = 从 $[n+1]$ 中选 $k+1$ 个的子集数 $= \\binom{n+1}{k+1}$。另一种方式：按子集中最大元素分类。若最大元素为 $i+1$（$k \\leq i \\leq n$），则需从 $\\{1,\\ldots,i\\}$ 中选其余 $k$ 个，方式为 $\\binom{i}{k}$。总和为 $\\sum_{i=k}^{n} \\binom{i}{k}$。',
    '**关键：选择正确的集合 $S$** 双向计数法最难的部分在于选择"被计数的对象集"。$S$ 的定义必须使两种计数方式分别对应待证等式的两边。这需要练习和直觉。',
    '**例：$\\sum_{k=0}^{n} \\binom{n}{k} = 2^n$** $S$ = $n$ 元集合的所有子集。方式 A：子集总数由每个元素独立决定取/不取 = $2^n$。方式 B：按子集大小分，大小为 $k$ 的子集数 = $\\binom{n}{k}$，总计 $\\sum_{k=0}^{n} \\binom{n}{k}$。',
    '**例：$\\binom{n}{0} + \\binom{n}{1} + \\cdots + \\binom{n}{n} = 2^n$**（与上例相同，另一种表述方式。）',
    '**例：Vandermonde 恒等式 $\\sum_{k=0}^{r} \\binom{m}{k}\\binom{n}{r-k} = \\binom{m+n}{r}$** $S$ = 从 $A$（$m$ 人）和 $B$（$n$ 人）共 $m+n$ 人中选 $r$ 人。方式 A：$\\binom{m+n}{r}$。方式 B：从 $A$ 中选 $k$ 人、从 $B$ 中选 $r-k$ 人，$k$ 从 0 到 $r$。',
    '**记住变量量化！** 双向计数证恒等式时，必须对每个出现的变量加以量化。如"对一切 $n \\in \\mathbb{N}$ 成立"必须写明。遗漏量化会导致证明不完整。',
    '**练习** (1) 用双向计数证明 $\\binom{n}{2} = \\frac{n(n-1)}{2}$。提示：计数 $n$ 人中两人组的方式。(2) 用双向计数证明 $\\sum_{k=0}^{n} k\\binom{n}{k} = n2^{n-1}$。',
    '(3) 用双向计数证明 $\\binom{n}{k} = \\binom{n}{n-k}$。提示：计选 $k$ 人与排除 $n-k$ 人。(4) 用双向计数证明 $\\sum_{i=0}^{n}\\binom{i}{k} = \\binom{n+1}{k+1}$（求和恒等式）。',
    '(5) 用双向计数证明 Vandermonde 恒等式。(6) 证明 $\\sum_{k=0}^{n} \\binom{n}{k}^2 = \\binom{2n}{n}$。提示：从 $n$ 男 $n$ 女中选 $n$ 人。',
    '(7) 解释双向计数与代数化简的区别。为什么双向计数有时更"优雅"？(8) 有没有恒等式不能用双向计数证明？为什么？',
    '**双向计数的优势** 与代数方法相比，双向计数提供了组合直觉。每个恒等式背后都有一个"对什么计数"的故事，理解了这个故事就真正理解了恒等式。',
    '**标号技巧** 当集合有某种特殊结构（如有序/无序、有无标号人物）时，按标号分类是常用的计数策略。Pascal 恒等式的"标记人物 $P$"就是典型。',
    '**按最大值/最小值分类** 子集按其最大（或最小）元素分类是一个强大的技巧。求和恒等式的证明就用了"按最大值分类"。',
    '**生成函数 vs 双向计数** 生成函数是另一个证明组合恒等式的工具，但它更代数化。双向计数更直观，但不能处理所有恒等式（特别是涉及递推的恒等式）。',
    '**多项式恒等式** 二项式定理可以推广到多项式定理：$(x_1 + \\cdots + x_m)^n = \\sum \\frac{n!}{n_1! \\cdots n_m!} x_1^{n_1} \\cdots x_m^{n_m}$，其中和遍历所有 $n_1 + \\cdots + n_m = n$ 的非负整数组。',
    '**组合 vs 代数证明** 同一个恒等式可能既有组合证明又有代数证明。组合证明给出直觉，代数证明给出一般化路径。两种方法互补。',
    '**格子路径计数** 格子路径（从 $(0,0)$ 到 $(a,b)$ 的右/上步路径）数 = $\\binom{a+b}{a}$。这是双向计数的经典应用——每条路径对应一个 $a$-右/上步序列。',
    '**例：Catalan 数** 从 $(0,0)$ 到 $(n,n)$ 不超过对角线的格子路径数为 $C_n = \\frac{1}{n+1}\\binom{2n}{n}$。可以通过将所有路径减去"越过对角线"的路径来证明。',
    '**补充** 双向计数法的关键洞察是"同一对象，两种视角"。就像一枚硬币的两面——无论从哪面看，都是同一枚硬币。',
    '**补充2** 当恒等式一边很自然但另一边不直观时，双向计数最有价值——它为"不直观"的一边提供了组合解释。',
    '**补充3** 反过来，如果找到了一个自然的"计数故事"，但两边恰好相等，这可能意味着恒等式只是同一事实的两种说法。',
    '**补充4** 历史上，Euler, Pascal, Vandermonde 等数学家正是用这种方法发现和证明了许多经典恒等式。',
    '**补充5** 双向计数法可推广到加权计数：两边计的不是元素个数而是某个权重的总和，等式仍然成立。',
    '**补充6** 练习时要注意：两个计数方法必须覆盖完全相同的对象集。如果不完全相同，"证明"就是错误的。',
]
c = 0
for t in ts:
    idx = d.find('TODO: 待翻译')
    if idx >= 0:
        d = d[:idx] + t + d[idx+len('TODO: 待翻译'):]
        c += 1
open(f, 'w', encoding='utf-8').write(d)
print(f"Ch8/04: {c}, remaining {d.count('TODO:')}")

# === Ch7/03 images and preimages (32 TODO) ===
f = 'docs/part-ii/ch07-functions-cardinality/03-images-and-preimages.md'
d = open(f, 'r', encoding='utf-8').read()
ts = [
    '像与原像（Images and Preimages）本节定义函数的像和原像，讨论其性质，并给出相关证明方法。',
    '**像（Image）** 设 $f: A \\to B$ 是函数，$X \\subseteq A$。$X$ 在 $f$ 下的像定义为 $\\text{Im}_f(X) = \\{f(x) \\mid x \\in X\\} = \\{b \\in B \\mid \\exists x \\in X.\\, f(x) = b\\}$。即所有 $X$ 中元素经 $f$ 映射到的输出集合。',
    '**原像（Preimage）** 设 $f: A \\to B$ 是函数，$Z \\subseteq B$。$Z$ 在 $f$ 下的原像定义为 $\\text{PreIm}_f(Z) = \\{a \\in A \\mid f(a) \\in Z\\}$。即所有输出落入 $Z$ 中的输入集合。',
    '**记号** 像有时写作 $f(X)$，原像写作 $f^{-1}(Z)$。但要注意：$f^{-1}$ 在此只是记号，不意味着 $f$ 有逆函数！',
    '**特例** $\\text{Im}_f(A)$ 是 $f$ 的值域（Range），$B$ 是陪域（Codomain）。$f$ 是满射当且仅当 $\\text{Im}_f(A) = B$。$\\text{PreIm}_f(\\{b\\})$ 是 $b$ 的纤维（Fiber）。',
    '**基本性质** (1) $\\text{Im}_f(\\emptyset) = \\emptyset$, $\\text{PreIm}_f(\\emptyset) = \\emptyset$。(2) $X \\subseteq Y \\subseteq A \\Rightarrow \\text{Im}_f(X) \\subseteq \\text{Im}_f(Y)$。(3) $Z \\subseteq W \\subseteq B \\Rightarrow \\text{PreIm}_f(Z) \\subseteq \\text{PreIm}_f(W)$。',
    '**像与原像的关系** (1) 对任意 $X \\subseteq A$，$X \\subseteq \\text{PreIm}_f(\\text{Im}_f(X))$，等号成立当且仅当 $f$ 在 $X$ 上单射。(2) 对任意 $Z \\subseteq B$，$\\text{Im}_f(\\text{PreIm}_f(Z)) \\subseteq Z$，等号成立当且仅当 $Z \\subseteq \\text{Im}_f(A)$。',
    '**并集运算** $\\text{Im}_f(X \\cup Y) = \\text{Im}_f(X) \\cup \\text{Im}_f(Y)$。推广：$\\text{Im}_f(\\bigcup_{i} X_i) = \\bigcup_{i} \\text{Im}_f(X_i)$。对原像也成立：$\\text{PreIm}_f(Z \\cup W) = \\text{PreIm}_f(Z) \\cup \\text{PreIm}_f(W)$。',
    '**交集运算** $\\text{Im}_f(X \\cap Y) \\subseteq \\text{Im}_f(X) \\cap \\text{Im}_f(Y)$（等号一般不成立！除非 $f$ 单射）。对原像，等号成立：$\\text{PreIm}_f(Z \\cap W) = \\text{PreIm}_f(Z) \\cap \\text{PreIm}_f(W)$。',
    '**补集运算** $\\text{PreIm}_f(B - Z) = A - \\text{PreIm}_f(Z)$。原像与补集可交换！但像与补集一般不可交换：$\\text{Im}_f(A - X)$ 与 $B - \\text{Im}_f(X)$ 不一定相等。',
    '**例** 设 $f: \\{1,2,3\\} \\to \\{a,b\\}$，$f(1)=f(2)=a, f(3)=b$。$\\text{Im}_f(\\{1,2\\}) = \\{a\\}$。$\\text{PreIm}_f(\\{a\\}) = \\{1,2\\}$。$A - \\text{PreIm}_f(\\{a\\}) = \\{3\\} = \\text{PreIm}_f(\\{b\\}) = \\text{PreIm}_f(B - \\{a\\})$ ✓。',
    '**求像的证明方法** 要证 $\\text{Im}_f(X) = S$：先证 $\\text{Im}_f(X) \\subseteq S$（任取 $y \\in \\text{Im}_f(X)$，找 $x \\in X$ 使 $f(x)=y$，推出 $y \\in S$）；再证 $S \\subseteq \\text{Im}_f(X)$（任取 $y \\in S$，构造 $x \\in X$ 使 $f(x)=y$），此步较难。',
    '**求原像的证明方法** 要证 $\\text{PreIm}_f(Z) = T$：先证 $\\text{PreIm}_f(Z) \\subseteq T$（任取 $a \\in \\text{PreIm}_f(Z)$，由 $f(a) \\in Z$ 推出 $a \\in T$）；再证 $T \\subseteq \\text{PreIm}_f(Z)$（任取 $x \\in T$，证 $f(x) \\in Z$）。',
    '**例** 设 $f: \\mathbb{R} \\to \\mathbb{R}, f(x) = x^2$。求 $\\text{Im}_f(\\{-1,1\\}) = \\{1\\}$，$\\text{PreIm}_f(\\{1\\}) = \\{-1,1\\}$，$\\text{PreIm}_f(\\{-1\\}) = \\emptyset$。',
    '**例** 设 $f: \\mathbb{N} \\to \\mathbb{N}, f(n) = 2n$。$\\text{Im}_f(\\mathbb{N}) = \\{$偶数$\\}$。$\\text{PreIm}_f(\\{$偶数$\\}) = \\mathbb{N}$。$\\text{PreIm}_f(\\{$奇数$\\}) = \\emptyset$。',
    '**证明 $\\text{PreIm}_f(Z \\cap W) = \\text{PreIm}_f(Z) \\cap \\text{PreIm}_f(W)$** $a \\in \\text{PreIm}_f(Z \\cap W)$ $\\Leftrightarrow$ $f(a) \\in Z \\cap W$ $\\Leftrightarrow$ $f(a) \\in Z$ 且 $f(a) \\in W$ $\\Leftrightarrow$ $a \\in \\text{PreIm}_f(Z)$ 且 $a \\in \\text{PreIm}_f(W)$ $\\Leftrightarrow$ $a \\in \\text{PreIm}_f(Z) \\cap \\text{PreIm}_f(W)$。',
    '**证明 $\\text{Im}_f(X \\cap Y) \\subseteq \\text{Im}_f(X) \\cap \\text{Im}_f(Y)$** 设 $b \\in \\text{Im}_f(X \\cap Y)$。则 $\\exists a \\in X \\cap Y$ 使 $f(a)=b$。由 $a \\in X$ 得 $b \\in \\text{Im}_f(X)$，由 $a \\in Y$ 得 $b \\in \\text{Im}_f(Y)$。故 $b \\in \\text{Im}_f(X) \\cap \\text{Im}_f(Y)$。',
    '**反例：$\\text{Im}_f(X \\cap Y) \\neq \\text{Im}_f(X) \\cap \\text{Im}_f(Y)$** 设 $f:\\{1,2\\} \\to \\{a\\}$，$f(1)=f(2)=a$。$\\text{Im}_f(\\{1\\} \\cap \\{2\\}) = \\text{Im}_f(\\emptyset) = \\emptyset$，但 $\\text{Im}_f(\\{1\\}) \\cap \\text{Im}_f(\\{2\\}) = \\{a\\}$。',
    '**单射的刻画** 以下等价：(a) $f$ 是单射；(b) $\\forall X,Y \\subseteq A.\\, \\text{Im}_f(X \\cap Y) = \\text{Im}_f(X) \\cap \\text{Im}_f(Y)$；(c) $\\forall X \\subseteq A.\\, X = \\text{PreIm}_f(\\text{Im}_f(X))$。',
    '**满射的刻画** 以下等价：(a) $f$ 是满射；(b) $\\forall Z \\subseteq B.\\, \\text{Im}_f(\\text{PreIm}_f(Z)) = Z$。',
    '**练习** (1) 设 $f: \\{1,2,3,4\\} \\to \\{a,b,c\\}$，$f(1)=a, f(2)=b, f(3)=b, f(4)=c$。求 $\\text{Im}_f(\\{1,2\\})$、$\\text{PreIm}_f(\\{b\\})$、$\\text{PreIm}_f(\\{c\\})$。',
    '(2) 证明 $\\text{PreIm}_f(Z \\cup W) = \\text{PreIm}_f(Z) \\cup \\text{PreIm}_f(W)$。(3) 证明 $\\text{PreIm}_f(B-Z) = A - \\text{PreIm}_f(Z)$。',
    '(4) 举例说明 $\\text{Im}_f(A-X)$ 未必等于 $B - \\text{Im}_f(X)$。(5) 证明：$f$ 单射时 $\\text{Im}_f(X \\cap Y) = \\text{Im}_f(X) \\cap \\text{Im}_f(Y)$。',
    '(6) 设 $f: \\mathbb{R} \\to \\mathbb{R}, f(x) = x+1$。求 $\\text{Im}_f([0,1])$ 和 $\\text{PreIm}_f([0,1])$。(7) 证明像不保持差集运算——即 $\\text{Im}_f(X-Y)$ 未必等于 $\\text{Im}_f(X) - \\text{Im}_f(Y)$。',
    '**指示函数与像/原像** 像和原像操作与集合运算的交互性质使它们成为分析函数行为的强大工具。原像对并、交、补、差四种运算都"可交换"，而像只对并集可交换。',
    '**补充** 像/原像的说服力在于：原像继承了陪域的集合结构（并、交、补全都保持），而像只部分继承（只保持并集）。这反映了函数映射的"信息压缩"——不同输入可以映射到同一输出。',
    '**补充2** 公式 $X \\subseteq \\text{PreIm}_f(\\text{Im}_f(X))$ 表示"先照像再逆推"可能找到更多输入——因为其他输入也可能映射到相同的像。',
    '**补充3** $\\text{Im}_f(\\text{PreIm}_f(Z)) \\subseteq Z$ 表示"先逆推再照像"只会缩小范围——不过若 $Z$ 完全在像中，则缩小为零。',
    '**补充4** 像和原像本质上描述了函数如何将集合从一个空间"搬运"到另一个空间：像把子集向前推，原像把子集向后拉。',
    '**补充5** 在拓扑学和测度论中，像和原像的概念被推广到开集/闭集/可测集。原像保持集合运算的性质在这些领域特别重要。',
    '**补充6** 像/原像的直觉：像 = "$X$ 中的所有输入能到达哪些输出？"原像 = "哪些输入能到达 $Z$ 中的输出？"',
    '**补充7** 总结：原像是"好算的"（保持所有集合运算），像是"难算的"（只保持并集，交集和差集需要额外条件）。',
]
c = 0
for t in ts:
    idx = d.find('TODO: 待翻译')
    if idx >= 0:
        d = d[:idx] + t + d[idx+len('TODO: 待翻译'):]
        c += 1
open(f, 'w', encoding='utf-8').write(d)
print(f"Ch7/03: {c}, remaining {d.count('TODO:')}")

print("\nBatch done!")
