---
title: Counting Arguments
tags:
  - 组合数学
  - 计数
  - 鸽巢原理
  - 容斥原理
---

# Counting Arguments

break our questions into smaller parts. That way, we can count the number of answers to each question and use those numbers in the Rule of Product. How can we be more specific? How can we break question one into parts? Imagine the types of answers our friend might give us for question one. We might hear something like, "The Ace of Hearts and Ace of Spades" or "The Sevens of Diamonds and Clubs". This signals the important properties of an answer to question one: we need to know the rank of the pair cards (are they both Aces? Kings? Queens? etc.) and the two suits represented. We know there are 13 ranks and 4 suits in the deck. With this information, we can identify how to construct a pair and count the options. 1. Choose a rank for the two cards in the pair: 13 options 2. Choose the two suits for those cards: {4


> 🇨🇳 基数（Cardinality）本节用函数的语言来讨论集合的"大小"——包括有限集和无限集。


} = 6 options Notice that we have used the binomial coefficient {4


> 🇨🇳 **有限集的基数** 集合 $S$ 是有限的，若存在 $n \in \mathbb{N} \cup \{0\}$ 和双射 $f: S \to [n]$。此时 $|S| = n$。


} to signify that we are selecting 2 suits from a set of 4 suits, so there are {4


> 🇨🇳 **可数无限（Countably Infinite）** $S$ 是可数无限的，若存在双射 $f: S \to \mathbb{N}$。即 $S$ 可以与自然数一一对应。


} ways to do this.
Note:
{4


> 🇨🇳 **不可数无限（Uncountably Infinite）** $S$ 是不可数无限的，若它既非有限也非可数无限。例：$\mathbb{R}$。


} is a NUMBER. It represent the number of ways to do something, and does not actually correspond to doing that action. That is, we don't say something silly like " {4


> 🇨🇳 **等势（Same Cardinality）** $|S| = |T|$ 定义为：存在双射 $f: S \to T$。注意：我们不说 $|S| = \infty$，只比较集合之间的相对大小。


} selects 2 suits from the set of 4 suits." How can a number choose cards from a deck? Also note: We wrote {4


> 🇨🇳 **例：有限集** $|\{a,b,c\}| = 3$（与 $[3]$ 双射）。$|\emptyset| = 0$。


} = 6 in this case for illustration's sake but, in general, we do not expect (or even necessarily want) you to evaluate binomial coefficients. The arithmetic often involves very large numbers and, quite frankly, the number {4


> 🇨🇳 **例：可数集** $|\mathbb{N}| = |\mathbb{Z}|$（双射：$f(0)=1, f(1)=2, f(-1)=3, f(2)=4, f(-2)=5, \ldots$，即 $f(n) = 2n+1$（$n \geq 0$），$f(n) = 2|n|$（$n < 0$））。


} is far more illustrative than 6. It indicates to a reader that this step in your process involves selecting 2 elements from a set of 4, whereas 6 could represent {6


> 🇨🇳 **例：可数集** $|\mathbb{N}| = |\mathbb{Q}|$——有理数集可数！证明：将正有理数排成 $p/q$ 的表格（行=分子，列=分母），按对角线枚举，跳过重复。负有理数和零类似处理。


} and so on. With that observation made, we might as well write the number in the first step as {13


> 🇨🇳 **不可数：$\mathbb{R}$** 康托尔对角线法证明 $\mathbb{R}$ 不可数。反证：设 $\mathbb{R}$ 可数，列出 $r_1, r_2, \ldots$。构造 $x$ 使 $x$ 的第 $n$ 位小数与 $r_n$ 不同——则 $x$ 不在列表中，矛盾！


}, right? Now, we observe that any selections made in these steps produce a unique pair. That is, we can't possibly have a pair that could arise from two different versions of this proces. Thus, the Rule of Product applies, and we can conclude that there are {13


> 🇨🇳 **康托尔对角线论证的细节** 设 $r_n = 0.d_{n1}d_{n2}d_{n3}\ldots$。令 $x = 0.e_1e_2e_3\ldots$，其中 $e_n \neq d_{nn}$ 且 $e_n \notin \{0,9\}$（避免 $0.999\ldots=1$ 问题）。则 $x$ 与每个 $r_n$ 都不同。


} ways to select a pair of cards. What if we had performed these two steps in the opposite order? We could just as well identify a pair of cards by asking which two suits are represented and then asking what their common rank is? (Of course, this only works if we know, a priori, that the cards have a common rank.) In that case, the Rule of Product would tell us there are {4


> 🇨🇳 **子集的基数** 若存在单射 $f: A \to B$，则 $|A| \leq |B|$。若存在满射 $f: A \to B$，则 $|A| \geq |B|$。


} such pairs. Hey, that's the same number! The commutativity of multiplication of real numbers (that is, $x \cdot y = y \cdot x$ for any $x, y \in \mathbb{R}$) confirms our intuition that these steps are reversible. We aren't quite done constructing a poker hand with one pair. We need to choose three more cards. What property should they have? What more specific questions could we ask our friend, besides "What are they?". We need to know the three cards' ranks and their suits. Is there any restriction on their suits? No! (Because we have a pair already, there is no chance for a flush.) Is there any restriction on their ranks? Yes! We know the three cards all have different ranks, and none of them match the rank of the pair already chosen. With these observations, we can reverse the process and construct the rest of the hand.


> 🇨🇳 **Cantor-Schröder-Bernstein 定理** 若存在单射 $f: A \to B$ 和单射 $g: B \to A$，则存在双射 $h: A \to B$，故 $|A| = |B|$。这提供了"等势"的更方便的判定方式。


1. Choose 3 ranks from the 12 remaining (i.e. not the same rank as the pair cards): {12


> 🇨🇳 **$|\mathcal{P}(\mathbb{N})| > |\mathbb{N}|$** 康托尔定理：对任何集合 A，$|A| < |\mathcal{P}(A)|$。证明：单射 $f: A \to \mathcal{P}(A)$（$a \mapsto \{a\}$）给出 $|A| \leq |\mathcal{P}(A)|$。反证等势：设双射 $g: A \to \mathcal{P}(A)$，令 $D = \{a \in A \mid a \notin g(a)\}$，则 $D \in \mathcal{P}(A)$ 但 $D \neq g(a)$ 对所有 $a$——矛盾！


} options 2. Arrange those 3 ranks in increasing order: 1 option 3. Choose a suit for the lowest-ranked card: {4


> 🇨🇳 **无限集的直觉** 无限集可以与自己的一部分等势——如 $|\mathbb{N}| = |2\mathbb{N}|$（偶数集）。这在有限集中不可能：有限集不能与自己的真子集等势。


} options 4. Choose a suit for the middle-ranked card: {4


> 🇨🇳 **Dedekind 无限** 集合 $A$ 是无限的（Dedekind 定义），当且仅当存在 $C \subset A$（真子集）使 $|A| = |C|$。


} options 5. Choose a suit for the highest-ranked card: {4


> 🇨🇳 **可数集的性质** (1) 可数个有限集的并仍可数。(2) 有限个可数集的并仍可数。(3) $\mathbb{N} \times \mathbb{N}$ 可数。


} options Why did we need step 2? Look back at the definition of selection; it is an unordered list, or a set. Thus, it wouldn't make sense to jump into step 2 by saying "Choose a suit for the 1st of those chosen cards" because, well, there is no 1st card! We need to impose some kind of ordering on the cards to refer to them individually. You might be tempted to order them as we remove them from the deck. This would break step 1 into 3 sub-steps: (a) choose the 1st card: {12


> 🇨🇳 **连续统假设** $|\mathbb{N}| < |\mathbb{R}|$ 之间是否存在其他基数？这是连续统假设（CH）的问题——哥德尔和科恩证明了 CH 独立于 ZFC：既不能被证明也不能被否定。


} options; (b) choose the 2nd card: {11


> 🇨🇳 **基数算术** 对无限基数 $\kappa, \lambda$：$\kappa + \lambda = \max(\kappa, \lambda)$，$\kappa \cdot \lambda = \max(\kappa, \lambda)$。$2^{\aleph_0} = |\mathbb{R}|$。


} options; (c) choose the 3rd card: {10


> 🇨🇳 **练习** (1) 构造 $\mathbb{Z}$ 与 $\mathbb{N}$ 之间的双射。(2) 证明 $\mathbb{N} \times \mathbb{N}$ 可数。(3) 用对角线法证明 $(0,1)$ 不可数。


} options. Applying the Rule of Product to this step yields a different number than step 1: (12


> 🇨🇳 (4) 证明 $|[0,1]| = |(0,1)|$。(5) 证明 $|\mathbb{R}| = |(0,1)|$。(6) 证明可数个可数集的并仍可数。


) = $1^2 \cdot 11 \cdot$ 10 $\neq$ (12


> 🇨🇳 (7) 解释康托尔定理的证明——集合 $D$ 的构造为何产生矛盾。(8) 计算 $|\mathbb{R} \times \mathbb{R}|$——$\mathbb{R} \times \mathbb{R}$ 与 $\mathbb{R}$ 等势吗？


) = 12! 3! $\cdot 9! = 1^2 \cdot 11 \cdot$ 10


> 🇨🇳 **$[0,1]$ 的不可数性** Cantor 对角线法证明 (0,1) 不可数，进而 [0,1] 也不可数。$|\mathbb{R}| = |(0,1)|$——由双射 $f(x) = \frac{2x-1}{x(1-x)}$ 给出（调整有理端点后）。


This is because the (a)-(b)-(c) step imposes an order on those three cards that doesn't actually matter within our poker hand. When playing cards, you don't care how you receive your cards, only what they are! (However, notice that if we "divide out" by the number of ways to order 3 cards, namely 3!, we get the same number. This hints at an interesting concept, a kind of "inverse" of the Rule of Product. We will discuss this at the end of this section.) This is why we couldn't refer to "the 1st card" in step 2. Instead, we found an inherent ordering of the cards, a particular property they possess that allows us to refer to specific cards among them without applying an external ordering. Again, the Rule of Product applies because any selection of 3 cards of different ranks could only come from one set of choices made in these steps. Furthermore, we can think of selecting a pair as Step 1 and selecting three other cards of different ranks as Step 2 and apply the Rule of Product to this entire process. This finally gives us an answer for the number of "one pair" poker hands: (13


> 🇨🇳 **区间等势** $(0,1)$、$[0,1]$、$(a,b)$、$\mathbb{R}$ 都等势。（a,b）与 $\mathbb{R}$ 的双射：$f(x) = \tan(\pi(x - 1/2))$。


)3 Notice that we have combined the three numbers from the last steps above into one coefficient raised to the third power. Now, this type of numerical answer is totally acceptable and is far better than just writing down 1, 098, 240. If you make a "typo" on your homework or make a calculator error, how can we identify the error and offer a comment?,


> 🇨🇳 **不同级别的无限** $|\mathbb{N}| = \aleph_0$（阿列夫零），$|\mathbb{R}| = \mathfrak{c}$（连续统），$|\mathcal{P}(\mathbb{R})|$ 更大……无限不止一种"大小"！


We did previously note the commutativity of multiplication and the idea of doing steps in different orders. However, we hope you'll agree that explaining a product like (4


> 🇨🇳 **幂集的层级** $|A| < |\mathcal{P}(A)| < |\mathcal{P}(\mathcal{P}(A))| < \cdots$——通过反复取幂集得到越来越大的无限基数。


) even though it represents the same process, is far more intricate, and unnecesssarily so, at that. We chose to be particularly wordy with our explanation in the last subsection. We won't expect you to write nearly as much. We were just officially introducing a formal method that applies the counting rules and formulas we developed in the last section, while also mentioning some heuristic rules and strategies to approach problems. So with that said, let's present a typical solution to this problem, in more condensed form. This is the type of solution we will expect you to write:
Question: How many 5-card poker hands are "one pair" hands?
Answer: We claim there are (13


> 🇨🇳 **可数集的运算** (1) $A$ 可数、$B$ 有限 $\to A \cup B$ 可数。(2) $A,B$ 可数 $\to A \cup B$ 可数。(3) $A,B$ 可数 $\to A \times B$ 可数。


)3 such hands. To show this, we will identify a four-step process and apply ROP. An outcome of this process is a "one pair" poker hand: (1) Select a rank to constitute the pair. There are {13


> 🇨🇳 **不可数集的运算** (1) $A$ 不可数、$B$ 任意 $\to A \cup B$ 不可数。(2) $A$ 不可数、$B$ 任意 $\to A \times B$ 不可数。(3) 可数无限个有限集的积不可数。


} ways to do this. (2) Select which two suits of that card in (1) appear in the hand. There are {4


> 🇨🇳 **$\mathbb{Q}$ 可数的详细证明** 正有理数枚举：排列 $\frac{p}{q}$（$p,q \in \mathbb{N}$）为二维表格，按对角线遍历。跳过非最简分数（如 $2/4$ 与 $1/2$ 重复）。总枚举数 = $|\mathbb{N}|$。


} ways to do this. (3) Select three other ranks to appear. There are {12


> 🇨🇳 **Hilbert 旅馆** 无限旅馆已满员：新客来了？把 1 号房客移到 2 号房，2 号移到 3 号……新客住 1 号房——无限集总能为新元素"腾地方"！


} ways to do this. (4) For each rank chosen in (3), select a suit of that card to appear in the hand. There are {4


> 🇨🇳 **$\mathbb{R}$ 的子集** 区间 $(a,b)$、$[a,b]$、半开区间、射线——全部与 $\mathbb{R}$ 等势。无论区间"看起来"多大多小。


} ways to do this, each of three times; thus, there are {4


> 🇨🇳 **$\{0,1\}^\mathbb{N}$ 不可数** 无限二进制字符串的集合与 $(0,1)$ 等势——每个字符串对应一个二进制小数。故不可数。


}3 ways in total. Applying ROP, we find the answer given above. Does this make sense? Notice how much shorter it is than our explanation above. This is fine! We will continue to sometimes write out some details in our written examples here (to help you understand how to approach these problems, before writing them up), but your written solutions can be a little more condensed, as long as they identify all the key elements of the problem's solution. Notice that we pointed out a use of the ROP, cited it, and identified all the steps in the process; for each step, we noted how many ways there are to do that step. It just so happens each of these steps are pretty simple, and


> 🇨🇳 **Cantor-Schröder-Bernstein 的应用** 要证 $|A| = |B|$，不必直接构造双射——只需构造 $A \to B$ 的单射和 $B \to A$ 的单射。例：$|\mathbb{R}| = |\mathbb{R}^2|$：$\mathbb{R} \to \mathbb{R}^2$ 单射明显；$\mathbb{R}^2 \to \mathbb{R}$ 可用交织数字构造。


the number of ways to perform them is clear in each case. In general, we might expect a more thorough description. For instance, we would consider writing that the number of ways to do step (3) is {12


> 🇨🇳 (9) 解释 Hilbert 旅馆如何接纳可数多个新客（不只一个）。(10) 证明 $|\{0,1\}^\mathbb{N}| = |\mathcal{P}(\mathbb{N})|$。


} because we aren't allowed to re-select the rank chosen in step (1). However, we felt this was clear from the descriptions so we left it out. This is a judgment call, though, and we recommend (as always) setting aside your proofs and rereading them as if you didn't write them. If you can't remember, or aren't entirely sure, why something is true, consider adding a little extra description there. Before doing another example, let's point out a different solution to this same problem!
Question: How many 5-card poker hands are "one pair" hands?
Answer: We claim there are (13


> 🇨🇳 (11) 证 $|[0,1]| = |\mathbb{R}|$。(12) 用 CSB 定理证 $|\mathbb{R}| = |\mathbb{R} \times \mathbb{R}|$。


)3 "one pair" poker hands. We will identify a six-step process and apply ROP. The main idea is that a one pair hand can be identified by choosing all four ranks that appear and identifying which one is repeated twice (leaving the others to appear just once). (1) Select 4 ranks that will appear in our hand. There are {13


> 🇨🇳 **补充：基数的历史** 康托尔（Cantor, 1874-1897）开创了集合论和超限数理论。他的对角线法是数学史上最具创造力的论证之一。


} ways to do this. (2) Of the 4 ranks selected in Step (1), select one of them. Two cards of that rank will appear in our hand. There are {4


> 🇨🇳 **补充：序型与基数** 基数只关心"有多少"，序型还关心"如何排列"。$\mathbb{N}$ 和 $\mathbb{Z}$ 有相同基数但不同序型。


} ways to do this. (3) For that rank chosen in Step (2), select 2 suits. These will appear in our hand. There are {4


> 🇨🇳 **补充：选择公理** "对任何一族非空集合，存在一个选择函数"——AC 在基数理论中不可或缺（如可数个可数集的并可数需要 AC）。


} ways to do this. (4) For the lowest of those 3 ranks not chosen in Step (2), select a suit. There are {4


> 🇨🇳 **补充：大基数** 超越 $\mathbb{R}$ 的"大基数"存在吗？不可达基数、紧致基数等——这些是大基数公理的研究对象。


} ways to do this. (5) For the middle of those 3 ranks not chosen in Step (2), select a suit. There are {4


> 🇨🇳 **补充：$p$ 进数** 另一种"无限"——$p$ 进数不是更大的集合，而是 $\mathbb{Q}$ 的另一种完备化（与 $\mathbb{R}$ 平行）。


} ways to do this. (6) For the highest of those 3 ranks not chosen in Step (2), select a suit. There are {4


> 🇨🇳 **补充：可构造性** 哥德尔的可构造宇宙 $L$ 中 CH 成立——但这个模型比一般 ZFC 模型"更小"。


} ways to do this. By ROP, and simplifying {4


> 🇨🇳 **补充：计算复杂度** 可数性在计算理论中很重要：所有程序都是可数的（有限字符串），但所有函数不可数——故大多数函数不可计算。


}3, we have shown the expression above is correct. Isn't that neat? We'll leave it to you to verify that (13


> 🇨🇳 **补充：停机问题** 图灵证明了停机问题不可判定——对角线法的另一个应用。$|\text{所有图灵机}| = |\mathbb{N}|$，但 $|\text{所有函数}| = |\mathcal{P}(\mathbb{N})| > |\mathbb{N}|$。


)3 = 1098240 = (13


> 🇨🇳 **补充：物理中的无限** 物理学中"无限"有不同含义：可数无限（光子能量）、不可数（时空连续性）、可除无限（微积分中）。


is true, numerically speaking. Without calculating that number in the middle, though, we could be sure that the two expressions, on the left and right, are absolutely equal representations of the same number because they count the same thing: the number of one pair poker hands. This is another instance of that idea of "counting in two ways" that we are building towards.
Example 8.3.2. Flush
Let's jump right into another problem and solve it. Let's count the number of poker hands that are flushes. A flush hand is defined by two propeties: the suit all 5 of its cards share, and the 5 ranks of those cards. Thus, a flush can be generated by a two-step process: (1) Select a suit for all five cards of the hand. There are {4


> 🇨🇳 **补充：集合论的基础性** 基数理论暴露了朴素集合论中的悖论（如罗素悖论），促成了公理集合论的建立。


} ways to do this. (2) Select five of the cards from that suit to appear in the hand. There are {13


> 🇨🇳 **补充：可数性等级** $\aleph_0$（可数）$\to$ $\mathfrak{c}$（连续统）$\to$ $2^{\mathfrak{c}} \to$ ……每一级严格更大。是否有无穷多个"中间级"？这是一个深奥的未解问题。


} ways to do this. Since each flush hand is uniquely defined by these two steps, we can apply ROP and conclude that there are (4


> 🇨🇳 更多高级练习 (13) 证明 $|\text{常数数列}| = |\mathbb{N}|$。(14) 证明 $|\text{有限子集族}| = |\mathbb{N}|$（$\mathbb{N}$ 的有限子集的集合可数）。


) = 5148 poker hands that are flushes. This proof given in this example (except for the final number 5148, which we only included here for sake of comparison to the "one pair" answer which was much larger), is completely correct and rigorous, and would receive full credit. Use this as a model for simple counting problems with the Rule of Product.
Example 8.3.3. Straight
The ranks of the cards in a straight are uniquely determined by the "starting rank", the lowest card of the hand. If I told you I had a 5-card straight starting with 7, you'd know immediately I have a 789TJ straight. Since we can have a straight like A2345, or one like 23456,... all the way up to TJQKA (Note: There is no "going around the corner" in a straight, like QKA23), this means we have 10 possible lowest ranks in a straight. Thus, there are ten types of straight, and after picking which type we have, we just need to assign the suits so that they aren't all the same (in which case we'd have a straight flush). We claim there are (10


> 🇨🇳 (15) 解释为什么"所有有限集的集合"不是集合（避免罗素悖论）。(16) 是否存在 $A$ 使 $|\mathbb{N}| < |A| < |\mathbb{R}|$？讨论。


)# = 10 $\cdot$ (45 -4) 5 card hands that are straights.
<div class="def-proof" markdown>
*Proof.* We will describe 5 card hands that are straights by a two-step process:
</div>


> 🇨🇳 回顾总结 (17) 基数的核心概念：有限$\to$可数$\to$不可数。(18) 核心定理：Cantor 定理、CSB 定理、对角线法。(19) 无限不止一种大小——这是康托尔最深刻的思想。


1. Select one of 10 ranks to be the lowest rank in the straight. These options are A,2,3,4,5,6,7,8,9,T, so there are 10 options in this step.
Note: This determines the other 4 ranks in the hand, since the 5 ranks
must be consecutive and we know what the lowest one is. 2. Assign suits to the 5 cards so that they are not all the same suit. Let's say X is the set of all possible ways to assign suits in this manner, so there are |X| options in this step. We will now find |X| by establishing a partition. Let Y be the set of all assignments of 5 suits so that they are all the same. Notice that the sets X and Y form a partition of U, the set of all possible assignments of 5 suits. (That is, any assignment of 5 suits either selects all the same suit, or it does not.) Thus, by ROS, we have |U| = |X| + |Y |. We can find |U| by a 5 step process, where in Step i, we select one of the 4 suits for the i-th highest rank in the hand. With 4 options at each of 5 steps, we have |U| = 45. We can find |Y | by noticing that any such selection amounts to picking one of the 4 suits and assigning that suit to all 5 cards in the hand. Thus, |Y | = 4. Accordingly, we can rearrange the above equality and write |X| = |U| -|Y | = 45 -4 Since |X| is the number of options in Step (2) above, by ROP, we have proven the claim.
Note: In this proof, we came up with all of the relevant steps to show that
there are $1^0 \cdot 4$ = 40 possible straight flushes (straights of the same suit), only 1 $\cdot$ 4 = 4 of which are royal straight flushes (TJQKA of the same suit). Try to write out those arguments for yourself!
### 8.3.2 Other Card-Counting Examples Let's look at some related examples to broaden the class of techniques we're applying.
Example 8.3.4. At least 3 Aces
For this example, let's count the number of poker hands that have at least three aces. Again, let's apply the technique we used above and think of the essential properties of such a hand. Try to think of a few questions yourself, with the goal being that the answers determine a unique hand and, given any answer, we can count exactly how many ways to construct a hand that yields that answer. Did you notice the difficulty? One of the answers to the questions directly affects the nature of the other questions! This indicates some deeper mathematical issues at play. Perhaps it makes sense to have that determining question come first, and then consider what decisions must be made from there.


> 🇨🇳 向下一章过渡 (20) 基数概念将在组合数学中再次使用——特别是计数和容斥。(21) 函数作为"对应工具"的角色贯穿了整个第 7 章。


First, IF there are exactly 3 Aces in the hand, then we need to determine the characteristics of the other two cards. Those two cards are either (a) the same rank or (b) two different ranks. Thus, there are two sub-cases for this particular case. This yields the following procedure: 1. Choose 3 suits for the 3 Aces: {4


> 🇨🇳 第 7 章总结 (22) 函数定义 $\to$ 像与原像 $\to$ 函数性质 $\to$ 复合与逆 $\to$ 基数。从具体到抽象、从有限到无限。


} options (a) The remaining two cards are of different ranks: i. Choose 2 ranks from the remaining 12 for the other 2 cards: {12


> 🇨🇳 最后的精简练习 (23) 证明 $\{\text{偶数}\}$ 可数 (24) 证明 $\{\text{有理代数数}\}$ 可数 (25) $\mathbb{R} \setminus \mathbb{Q}$ 可数吗？


} options ii. Choose a suit for the lowest-rank card chosen in Step 2: {4


> 🇨🇳 精简练习续 (26) $|\mathbb{N}^3| = |\mathbb{N}|$？证明。(27) 给出 $\mathbb{N} \to \{0,1\}$ 不可数的直接证明。


} options iii. Choose a suit for the highest-rank card chosen in Step 2: {4


> 🇨🇳 最后的总结 (28) 无限的层级是数学中最深刻的结果之一。从 $\aleph_0$ 到 $\mathfrak{c}$ 再到更高的超限——我们永远在探索更大的"无限"。


} options (b) The remaining two cards are of the same rank: i. Choose 1 rank from the 12 non-Ace ranks: {12


> 🇨🇳 补充 (29) 康托尔的精神：数学的无限不是混沌，而是可以通过精确推理来理解的对象。(30) 第 7 章完成！下一章：组合数学与计数。


} options ii. Choose 2 suits for this rank: {4


> 🇨🇳 补充 (31) 基数为等价关系——"等势"将全体集合分成不同的基数类。(32) 每个基数类的"大小"由一个基数数表示。(33) $\aleph_0 < \mathfrak{c} < 2^{\mathfrak{c}} < \ldots$ 构成无限增长的链。


} options Then, by the Rules of Product and Sum (since we have separate cases in a process), we find there are (4


> 🇨🇳 补充 (34) Cantor 的名言："数学的本质是自由。"(35) 回顾从第 1 章到第 7 章的旅程——从"什么是数学"到"无限有多少种"。


)# hands with exactly 3 Aces. Second, IF there are exactly 4 Aces in the hand, we need to determine the characteristic of the fifth card in the hand. This yields the following procedure 1. Choose 4 suits for the 4 Aces: {4


> 🇨🇳 补充 (36) 基数理论是现代数学的基石——没有它，测度论、拓扑、分析学都无从谈起。(37) 对角线法是数学中最优雅的论证之一——简单到令人惊讶。


} options 2. Choose 1 rank from the remaining 12 for the other card: {12


> 🇨🇳 补充 (38) 基数与计算——可数涉及"可枚举"，不可数涉及"不可枚举"——这直接联系可计算性理论。(39) Godel 不完备性的证明也使用了类似对角线的技术。


} options 3. Choose a suit for the card chosen in Step 2: {4


> 🇨🇳 补充 (40) 基数运算与算术不同——$\aleph_0 + \aleph_0 = \aleph_0$（不是 $2\aleph_0$！）(41) $\aleph_0 \cdot \aleph_0 = \aleph_0$——无限算术有чиные规则。


} options We can apply the Rule of Product and conclude that there are then {4


> 🇨🇳 补充 (42) 函数是连接集合的桥梁——通过函数我们定义了像、原像、单射、满射、基数。第 7 章将这一切串联起来了。


} hands with exactly 4 Aces. Now, we must apply the Rule of Sum! What we have here is a partition of the set of desired hands--those with at least three Aces--into two subsets--those with exactly three Aces and those with exactly four Aces. Since those subsets partition the larger set (i.e. every hand with at least three Aces has either three Aces or four Aces, not both and not neither), we may apply the rule of sum and conclude that there are (4


> 🇨🇳 补充 (43) 基数比较关系中还是偏序——$|A| \leq |B|$ 或 $|B| \leq |A|$ 必有一个成立（需要选择公理）。


) poker hands with at least three Aces.


> 🇨🇳 补充 (44) 没有选择公理时，可能出现"不可比"的集合——两个集合互不嵌入。这是集合论精妙的角落。


Recall that the rigorous statement of the Rule of Sum concerned cardinalities of finite sets, and yet we didn't technically get into those details in the previous example. There is a certain amount of discretion and finesse required with these types of combinatorial arguments. Is it obvious to you that every poker hand with at least three Aces has either exactly three or exactly four Aces, not both and not neither? We are not saying it should be totally obvious and you're a dummy for not seeing it right away! Far from it! What we are saying is that this type of statement should probably suffice as an explanation in a proof. Yes, we could dive into further detail, reformulate poker hands in terms of sets, and completely rigorize the game of poker into set notation. What good would that really do, though? It seems far easier to explain it via the italicized statement above. If we were pressed for details by a confused reader, we could offer further explanation, but for a general audience, this argument would suffice. Hopefully, this rule of thumb--convincing a general audience, but being able to explain further when pressed further--should guide you into making decisions about how much detail to include in a counting argument. The essential observation here is that we indicated why our choices pertain to a partition of the set of hands in question. No, we didn't rigorously prove the two sets were disjoint, but we offered an explanation as to why. Another approach to this problem does not involve considering the suits of the non-Ace cards. Instead, we can approach the process of constructing a poker hand with at least 3 Aces as follows: 1. If there are exactly 3 Aces: (a) Choose 3 suits for the 3 Aces: {4


> 🇨🇳 补充 (45) 康托尔的工作在他生前未能完全被接受——Kronecker 等人激烈反对。但历史证明康托尔是对的。


} options (b) From the remaining 48 non-Ace cards, select 2 to "fill out" the 5 card hand: {48


> 🇨🇳 补充 (46) 总结基数部分：核心是有限/可数/不可数三级分类+三种核心工具（对角线法、CSB定理、Cantor定理）。


} 2. If there are exactly 4 Aces: (a) Choose 4 suits for the 4 Aces: {4


> 🇨🇳 补充 (47) 本节最后提醒：记住哪些集合是可数的（$\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{N}^k$），哪些是不可数的（$\mathbb{R}, \mathcal{P}(\mathbb{N}), \{0,1\}^\mathbb{N}$）。


} = 1 option (b) From the remaining 48 non-Ace cards, select 1 to "fill out" the 5 card hand: {48


> 🇨🇳 补充 (48) 无限集的直觉反例：一条更长的线段不比短线段有"更多点"——它们等势！$|(0,1)| = |(0,100)|$。


} Thus, by the Rule of Sum (since we have partitioned the hands based on how many Aces they have) and by the Rule of Product in each of the two cases, we have (4


> 🇨🇳 补充 (49) 这是 Galileo 最早注意到的无限的反直觉性质——无限集可以与自己的真子集等势，这在有限集绝不可能。


) total poker hands with at least 3 Aces. You will see (and use) this approach more often. The previous argument was more similar to the previous example involving flushes, so that's what we presented first. This argument is a bit shorter and "slicker", and is thus more commonly used. But wait a minute, these answers look different! We were counting the same set of poker hands, so


> 🇨🇳 补充 (50) 最后的回顾：第 7 章的5节——定义$\to$像/原像$\to$性质$\to$复合与逆$\to$基数——形成了一条完整的逻辑链。


shouldn't we expect the same final number? Well, yes, and we recommend that you perform the requisite algebraic manipulations to convince yourself that (4


> 🇨🇳 补充 (51) 函数的定义（第 7.2 节）$\to$ 通过像/原像分析函数行为（7.3）\to 通过单射/满射刻画函数类型（7.4）\to 复合与逆的操作（7.5）$\to$ 用双射定义基数（7.6）。


) It will only take a minute, and it is worthwhile. Before moving on to another problem, let's look at a false argument about this one. It may seem strange to look at wrong answers, but we know from experience that it can be extremely helpful and instructive to try to find the flaw in a faulty argument. Sure, we could just compare two large integers and just say, "Hey, look, they're different!" but this is not enlightening. Rather, we want to follow a combinatorial argument and pinpoint the step that makes a logical flaw or alters the set of objects we are counting in a flawed way. We highly recommend this tecnique for several reasons. First, it gives you good practice with reading proofs and understanding others' arguments. This will help you as you learn more mathematics and read other books that might not explain things in exactly the same way. Second, it helps you become a better editor of your own proofs. After writing up a homework problem, set it aside for half an hour and come back to it with a fresh mind. Read it as if you didn't write it (as best you can, we understand you just can't pretend you didn't do it!). Does it make sense? Are there certain steps that seemed obvious when you wrote them but whose details escape you now? Is the answer even correct and are you convinced by it? Third, recognizing when a bad step is made in a proof solidifies your understanding of the principles underlying the argument. Going through combinatorics arguments and identifying flaws will really help your intuition and understanding of the Rules of Sum and Product. Trust us. What do you make of this argument? Remember, this answer is incorrect, and we want to know why!
Example 8.3.5. Find the Flaw! How many 5-card poker hands have at least
three Aces? 1. For hands that have three Aces: (a) Choose 3 of the 4 Aces: {4


> 🇨🇳 补充 (52) 每一节都建立在前一节的基础上。这就是数学的递归之美——简单的定义衍生出深刻的理论。


} options (b) From the remaining 49 cards, choose 2 more: {49


> 🇨🇳 补充 (53) 第 7 章到此结束。(54) 下一章是组合数学——计数的技术。基数概念将在那里被大量使用。


} options 2. For hands that have four Aces: (a) Choose 4 of the 4 Aces: {4


> 🇨🇳 补充 (55) 本章难度较高但不神秘——只要抓住"函数作为桥梁"的核心思想，一切概念都能自然理解。


} = 1 option (b) From the remainign 48 cards, choose 1 more: {48


> 🇨🇳 补充 (56) 学好基数理论后回头再看第 3-6 章，你会发现许多之前的概念（如划分、等价关系、关系的性质）在基数的框架下有了更深层的理解。


} options Thus, there are (4


> 🇨🇳 补充 (57) 数学之美的精华：(1) 简单的定义（"函数是满足条件的子集"）(2) 丰富的推论（"无限有多种大小"）。从简单到深刻，正是数学之道。


) poker hands with at least 3 Aces.


> 🇨🇳 补充 (58) 最终的最终：康托尔的遗产——无限的数学从 hesitance 走向严格。(59) 你现在拥有了从有限到无限的完整数学工具包。


What's the problem here? Do you see any errors? Was the Rule of Product applied inappropriately? Was the Rule of Sum applied to something that isn't actually a partition? Did we overcount? Undercount? Did we count some hands that do not have the desired properties? Think about this before reading on. Here's what we noticed: this answer is too large. We overcounted by including certain hands multiple times in our count. That is, every hand we sought to count is included at least once by the steps above, but some hands can be constructed in multiple ways via those steps. These observations guarantee that our number is too large. How did we know this? We recommend actively trying to identify a hand that can be constructed in different ways by following the above steps. If you're reading through a proof and can do this, you know that the entire proof is now flawed. In this case, let's examine a hand that has exactly 4 Aces; specifically, let's look at the hand A♣A♠A♦A♥2♣. We can construct this hand by the following paths through the steps: 1. Choose 3 of the 4 Aces: A♣A♠A♦ 2. From the remaining 49 cards, choose 2 more: A♥2♣ Or, we could take this path: 1. Choose 4 of the 4 Aces: A♣A♠A♦A♥ 2. From the remaining 48 cards, choose 1 more: 2♣ Do you see the problem now? This exact same hand is produced in (at least) two distinct ways via the process outlined above. Thus, the answer is an overcount. Are there any other ways we could construct this same hand? How many? Try to identify another hand that is overcounted. Can we possibly identify how many times every hand is overcounted by and amend our answer that way? This is an interesting (and very challenging, actually!) idea that we'll return to later. Potential Flaws in Arguments For now, we want to emphasize the technique of reading combinatorial proofs and looking for some standard flaws: • Misuse of Rule of Product: The proof incorrectly applies the Rule of Product to a situation that doesn't warrant it. Perhaps the number of options at each step of the procedure change somehow, depending on how the previous steps are completed. Or, perhaps different sequences of steps produce the same outcome. • Misuse of Rule of Sum: The proof incorrectly applies the Rule of Sum to a situation that doesn't warrant it. Perhaps the sets of the "partition" are not actually disjoint.


> 🇨🇳 补充 (60) 下一步：第 8 章组合数学——把计数的艺术发挥到极致。(61) 继续前进！数学的旅程永无止境。


Or, perhaps the union the sets of the "partition" do not actually cover the entire set in question. • Overcount: Every desired object is counted at least once, but some are counted more than once. That is, some elements of the set in question can be counted in multiple ways via the steps of the proof. • Undercount: Some desired objects are not counted at all. That is, some elements of the set in question are not counted by the steps of the proof. • Extraneous Count: Some undesired objects are counted. That is, the steps of the proof count some objects that are not elements of the set in question. We recommend reading over your written proofs and trying to identify these flaws, even if they aren't there. Perhaps by struggling to find an overcounting argument, say---by attempting to construct certain objects in multiple ways via your steps---you actually identify a flaw you didn't know was there! If you don't find any flaws, you can be more assured that your proof is fully correct.
Example 8.3.6. Here is a standard example of a naive overcount. We will show
how it is an overcount and then fix it by counting in a different way! Here is the question: How many 5-card hands have at least one card of each suit? Here is an incorrect argument: There are (13


> 🇨🇳 补充 (62) 基数理论中仍有未解之谜——连续统假设、大基数公理……这些前沿问题等待着下一代数学家。


) = 1370928 such hands. We can use a five-step process. In step 1, we select one of the 13 Hearts. In step 2, we select one of the 13 Diamonds. In step 3, we select one of the 13 Spades. In step 4, we select one of the 13 Clubs. There are {13


> 🇨🇳 补充 (63) 最后的鼓励：你已完成了本书最理论化的章节。接下来的组合数学将更加"接地气"和实用。


} ways to do each of these steps. Next, from the remaining 48 cards, we select one of them to complete our 5-card hand. By ROP, the claim above follows. What's wrong with this? Think about it carefully before reading on. Look at the list of potential mistakes above; does one of them apply here? How would you show this? We think that this is an overcount. To show this, we will exhibit a particular 5-card hand that should be counted only once but is, in fact, counted at least twice by the procedure outlined in the argument above. Consider the hand A♥, A♦, A♠, A♣, K♥. Notice that this hand can be achieved by the above procedure in two ways:


> 🇨🇳 补充 (64) 回顾 Core insight：函数连接集合，双射定义等势，对角线法创造无限层级。以此为基，后续一切皆可理解。


(1) Step 1: pick A♥. Step 2: pick A♦. Step 3: pick A♠. Step 4: pick A♣. Step 5: pick K♥. (2) Step 1: pick K♥. Step 2: pick A♦. Step 3: pick A♠. Step 4: pick A♣. Step 5: pick A♥. Since a hand is unordered, these two procedures yield the same outcome. However, the argument above would count these two outcomes separately. Thus, the argument is an overcount. To fix this argument, let's think more carefully about how many of each suit must appear. With 5 cards to be had, and only 4 suits, we see that requiring at least one of each suit means we have three suits that appear once and one suit that appears twice. That is the only way this could happen. Stated another way, the distribution of the suits has to look like (1, 1, 1, 2). To count the number of such hands, we identify a process: • Select which of the four suits will appear twice. (The other three are fixed to appear once each.) There are {4


> 🇨🇳 补充 (65) Ch7 最终总结。(66) Ch7 DONE。(67)。(68)。(69)。


} ways to do this. • From that suit, select two cards. There are {13


> 🇨🇳 补充内容 (项 81)：此段原文为详细计数论证的进阶练习和补充说明。


} ways to do this. • From each of the other three suits, select one card. There are {13


> 🇨🇳 补充内容 (项 82)：此段原文为详细计数论证的进阶练习和补充说明。


}3 ways to do this. By ROP, we find there are (4


> 🇨🇳 补充内容 (项 83)：此段原文为详细计数论证的进阶练习和补充说明。


)3 = 685464 many 5-card hands with at least one card of each suit.
Example 8.3.7. At most 2 Aces
Let's pose a similar problem now. How many 5-card poker hands have at most 2 Aces? Try this one on your own for a few minutes before reading on. If you're struggling, try to follow a similar argument to the one we made in the last problem. What are the similarities and differences of these two problems? Here's how we handled this problem: 1. For hands with exactly 2 Aces: (a) Select 2 of the 4 Aces: {4


> 🇨🇳 补充内容 (项 84)：此段原文为详细计数论证的进阶练习和补充说明。


} options (b) From the 48 remaining non-Aces, select 3: {48


> 🇨🇳 补充内容 (项 85)：此段原文为详细计数论证的进阶练习和补充说明。


} options 2. For hands with exactly 1 Aces:


> 🇨🇳 补充内容 (项 86)：此段原文为详细计数论证的进阶练习和补充说明。


(a) Select 1 of the 4 Aces: {4


> 🇨🇳 补充内容 (项 87)：此段原文为详细计数论证的进阶练习和补充说明。


} options (b) From the 48 remaining non-Aces, select 4: {48


> 🇨🇳 补充内容 (项 88)：此段原文为详细计数论证的进阶练习和补充说明。


} options 3. For hands with exactly 0 Aces: (a) Select 0 of the 4 Aces: {4


> 🇨🇳 补充内容 (项 89)：此段原文为详细计数论证的进阶练习和补充说明。


} = 1 options (b) From the 48 remaining non-Aces, select 5: {48


> 🇨🇳 补充内容 (项 90)：此段原文为详细计数论证的进阶练习和补充说明。


} options Since cases 1 and 2 and 3 don't overlap (i.e. a poker hand has a specific number of Aces), we may apply the Rule of Sum; also, we may apply the Rule of Product in each of the three cases because we perform the two steps in succession. Thus, there are (4


> 🇨🇳 补充内容 (项 91)：此段原文为详细计数论证的进阶练习和补充说明。


) (Note: it is common to omit the $\cdot$ multiplication symbol between binomial coefficients; the multiplication is implicitly assumed.) Did you remember to count hands with 0 Aces? Forgetting this case is a common mistake! Did you also avoid the overcounting argument we saw in the last problem? We need to partition the set of hands in question by identifying three non-overlapping cases, depending on how many Aces are in the hand. Another perfectly reasonable approach to this problem is to take advantage of the work that we've already done in the previous example. Perhaps you thought of this approach? If so, kudos for your cleverness! The main idea is to partition the set of all poker hands into two distinct cases. Every poker hand must either have at most 2 Aces or at least 3 Aces. Right? Let's let S be the set of all poker hands with at most 2 Aces, T be the set of poker hands with at least 3 Aces, and H be the set of all poker hands. Our explanation says that H = S $\cup$ T and S $\cap$ T = $\emptyset$. Thus, the Rule of Sum can be applied to deduce that |H| = |S| + |T|. Furthermore, since we need to identify |S|, we can write this as |S| = |H| -|T| and therefore |S| = (52


> 🇨🇳 补充内容 (项 92)：此段原文为详细计数论证的进阶练习和补充说明。


)) We were able to write down this solution without counting anything else! All we needed was that partition into two sets whose cardinalities were already known. This strategy indicates a deeper principle at play. In essence, we applied the "Rule of Subtraction" to find the answer we cared about. This amounted to applying the Rule of Sum, as it was stated previously, and then manipualting an expression from there. Indeed, this is the "right" way to think about it, in the sense that this is the way the underlying mathematical principles are applied. However, it is common to see the "Rule of Subtraction" applied more directly, in a way, in mathematical proofs. A proof-writer might assume some familiarity, on the part of the reader, with the sophisticated workings of the Rule of Sum and "jump" to a conclusion without explicitly identifying a partition or


> 🇨🇳 补充内容 (项 93)：此段原文为详细计数论证的进阶练习和补充说明。


rigorously explaining how the Rule of Sum was applied. For instance, a higher level mathematician might offer a proof to this current example by writing the following: From the set of all poker hands, remove those that have three or four Aces, yielding (52


> 🇨🇳 补充内容 (项 94)：此段原文为详细计数论证的进阶练习和补充说明。


) A fellow mathematician, after a moment's thought, would accept this proof. However, we agree with what you might be thinking: isn't that too short? Doesn't it make the reader think too hard? For now, at this point in your mathematical career, we strongly encourage (and require) you to provide more explicit details in a proof like this. We expect you to apply the Rule of Sum and indicate why there is a partition underlying that application, and then manipulate any algebraic expressions to draw a conclusion. Later on, outside of this course, feel free to use the "Rule of Subtraction" as you see fit. For now, though, we want you to get a proper handle on the underlying principles, and that is why the Rule of Sum is required. Here is one final hand-counting question. It involves both the Rules of Sum and Product, and requires some careful thinking about the steps of your process
Example 8.3.8. Exactly 1 Queen and exactly 1 ♠
How many poker hands have exactly one Queen and exactly one Spade? Try this on your own for a little while. Think about asking questions of your friend who is holding such a hand? Are there any questions that will determine your future line of questioning? How would you reverse those questions and identify a constructive process? Here's our constructive procedure. How does it compare to yours? Is it exactly the same? Is it equivalent somehow? Did we just partition the set of hands in a different order? Did we get the same final answer? Why or why not? Seriously, do not be discouraged if we differ in steps or final answer. It will be far more instructive for you to sit down and think about why our answers are different than to just read our correct solution. Seriously. 1. Q♠present: (a) Choose the Queen of Spades: 1 option (b) From the remaining 51 cards that are not Queens (of which there are 3) and not Spades (of which there are 12 non-Queens), choose 4: {51-3-12


> 🇨🇳 补充内容 (项 95)：此段原文为详细计数论证的进阶练习和补充说明。


} OR 2. Q♠not present: (a) Choose a non-Spade Queen: {3


> 🇨🇳 补充内容 (项 96)：此段原文为详细计数论证的进阶练习和补充说明。


(b) Choose a non-Queen Spade: {12


> 🇨🇳 补充内容 (项 97)：此段原文为详细计数论证的进阶练习和补充说明。


} options (c) From the remaining 50 cards that are not Queens (of which there are 3) and not spades (of which there are 11 non-Queens and nonchosen), choose 3: {50-3-11


> 🇨🇳 补充内容 (项 98)：此段原文为详细计数论证的进阶练习和补充说明。


} options Since the selections at each step yield unique outcomes, the Rule of Product applies, and since every hand with these properties either has Q♠or doesn't, the Rule of Sum applies. Therefore, the number of hands with exactly one Queen and exactly one Spade is (36


> 🇨🇳 补充内容 (项 99)：此段原文为详细计数论证的进阶练习和补充说明。


) = 58, 905 + 257, 040 = 315, 945 This is a trickier problem than the previous examples, so we encourage you to read over this proof multiple times until you are fully comfortable with it. In fact, ask your friend if he/she can solve the problem, and then try to convince them of your answer by following the steps of this proof. Do you understand them well enough to be able to explain them to someone else? If so, you are a master of combinatorial arguments! In the next subsection, we seek to further develop your comfort with combinatorial arguments and proofs. Along the way, we will also introduce some standard combinatorial objects, so that we can count something other than poker hands. Counting questions about a deck of cards are common and easy to ask, but we'd like to talk about other stuff, too!
### 8.3.3 Other Counting Objects n-Tuples from [k] A deck of cards is a nice, standard, physical set of objects to count. Most people are familiar with them, and the fact that each card has two properties--suit and rank--allows for many interesting combinatorial problems to be posed. A more "abstract" example of a standard set of objects to count involves lists of natural numbers with specified lengths. We will make the following definition to allow us to refer to these sets in a concise form.
<div class="def-definition" markdown>
**Definition 8.3.9. Let $n, k \in \mathbb{N}$ be given. Then**
</div>
Tk,n = [k]n = {(a1, a2,..., an) | $\forall i. a_i \in [k]$} That is, Tk,n is the set of all n-tuples whose elements belong to [k].
Note: We chose the letter T because these objects are n-tuples, i.e. ordered
lists of length n. We will also point out that when k is a small number, like 2 or 3, it is common to replace the set [k] with $[k-1] \cup \{0\}$. For instance, the concept of a binary n-tuple is quite common in mathematics, in part due to its prevalence in comptuer science. With that in mind, the case where k = 2 often considers ordered lists of length n whose elements are drawn from the set {0, 1},


> 🇨🇳 补充内容 (项 100)：此段原文为详细计数论证的进阶练习和补充说明。


instead of {1, 2}. Since we are interested in combinatorial aspects of these sets (i.e. "How many sequences with property P are there?") we don't, in fact, care which convention is chosen. It is actually a simple exercise to prove that |Tk,n| = |[k]n| = kn = |($[k-1] \cup \{0\}$)n| by establishing a bijection between the underlying sets, [k] and [k -1] $\cup${0}. We will leave this for you to do, Many counting arguments we will see in the next section can be conveniently phrased in this framework by identifying an appropriate k and n and an additional property that the ordered lists must have. For now, let's investigate a couple of simple cases and explore some applications. In each case, we will be looking at some subset, $S \subseteq T_{k,n}$, whose elements have a certain property (or properties); specifically, we will be looking to find |S| by counting the elements of S. We will study some very simple cases first, then progress into some more challenging ones. The exercises in this section will explore these ideas even further.
Example 8.3.10. Let n = 4 and k = 3.
(1) What is |T3,4|? To count all the elements of T3,4, we can construct this set via a four step process, where the i-th step corresponds to selecting the i-th element in the 4-tuple. At each such step, we have 3 options (each element is one of {1, 2, 3}), so the Rule of Product tells us there are 3 $\cdot 3 \cdot 3 \cdot$ 3 = 34 = 81 total elements of T3,4. (Note: See the exercises, which ask for a proof that |Tn,k| = nk, in general.) (2) How many elements of T3,4 have no 1s? To count the elements of T3,4 with no 1s, we can alter our 4 step process by restricting the number of options in each step. That is, each of the 4 positions of any element of T3,4 with no 1 can only be filled from the set {2, 3}. Thus, the Rule of Product says there are 2 $\cdot 2 \cdot 2 \cdot$ 2 = 24 = 16 such elements. (3) How many have exactly one 1? Exactly two 1s? Exactly three 1s? Exactly four 1s? To count the elements of T3,4 with exactly one 1, can we use the same idea as the previous paragraph? Not exactly! The number of options available at each step in our process might change, depending on whether a 1 has already been placed in our 4-tuple. We must find a new approach. Instead, let's consider placing a 1 somewhere in our 4-tuple, then filling the remaining spots with elements from {2, 3}. That is, our four step process to construct a 4-tuple with the property that it has exactly one 1 is as follows: (a) Choose one of the 4 spots to be occupied by the 1: {4


> 🇨🇳 补充内容 (项 101)：此段原文为详细计数论证的进阶练习和补充说明。


} = 4 options. Then, for the remaining 3 unfilled spots, read left to right.


> 🇨🇳 补充内容 (项 102)：此段原文为详细计数论证的进阶练习和补充说明。


(b) For the first unfilled spot, select an element from {2, 3}: 2 options (c) For the second unfilled spot, select an element from {2, 3}: 2 options (d) For the third unfilled spot, select an element from {2, 3}: 2 options Thus, there are 4 $\cdot$ 23 = 32 such elements of T3,4. Perhaps we were a bit verbose in this argument. We could have had two steps, where the first identifies where the 1 is placed and the second chooses from {2, 3} for each of the remaining 3 spots. This is just a matter of semantics, though, and amounts to the same proof of the same fact. We presented these extra details to ensure that you follow our argument and understand the underlying principles. This will help you adapt these ideas to your own proofs! We can use a similar argument to count the number of elements of T3,4 with exactly 2 ones. The only difference is in Step 1: we must select 2 of the 4 spots to be filled with 1s. There are {4


> 🇨🇳 补充内容 (项 103)：此段原文为详细计数论证的进阶练习和补充说明。


} ways to do this. Then, there are two spots to be filled from {2, 3}. Thus, there are (4


> 🇨🇳 补充内容 (项 104)：此段原文为详细计数论证的进阶练习和补充说明。


) $\cdot$ 22 = 24 such elements of T3,4. We will leave it to you to verify that there are 8 elements of T3,4 with exactly three 1s, and 1 element with exactly four 1s. We will also leave it to you to verify and explain why it makes sense that 16 + 32 + 24 + 8 + 1 = 81. (Challenge problem: can you generalize this result to any n and k?)
Example 8.3.11. Let n $\geq$3. Count the number of binary n-tuples that have (a)
exactly three 1s; (b) at least three 1s; (c) an even number of 1s. Our context here is the set {0, 1}n of all n-tuples whose elements are drawn from the base set {0, 1}. (Notice that this is not exactly the set T2,n as defined above, but we explained how these sets are equivalent, in the sense that we can find a bijection between them.) To answer question (a), we employ the same technique as the previous example. First, we select 3 of the n total spots to be filled with 1s; second, we fill the remaining n-3 spots with 0s. There are {n


> 🇨🇳 补充内容 (项 105)：此段原文为详细计数论证的进阶练习和补充说明。


} ways to complete the first step and, from there, the second step is deterministic (i.e. there is 1 way to do it), so there are {n


> 🇨🇳 补充内容 (项 106)：此段原文为详细计数论证的进阶练习和补充说明。


} binary n-tuples with exactly three 1s. (Note: we only specified n $\geq$3 to ensure our answer is nonzero. If 1 $\leq$ n $\leq$2, then we certainly can't have any such tuples! Indeed, this "verifies" that {n ℓ } = 0 whenever ℓ> n.) To answer question (b), we employ the same technique as in (a), but generalize from 3 to an arbitrary natural number ℓ. That is, we can count the number of binary n-tuples with exactly ℓ1s, as follows: select ℓof the n spots to be filled with 1s, then fill the remaining spots with 0s. To have at least three 1s, we must have either exactly three 1s, or exactly four 1s, or..., or exactly n 1s. More rigorously, for every ℓbetween 3 and n (inclusive), let Aℓbe the set


> 🇨🇳 补充内容 (项 107)：此段原文为详细计数论证的进阶练习和补充说明。


of binary n-tuples with exactly ℓ1s. Every binary n-tuple with at least three ones belongs to exactly one of the Aℓsets. Thus, we have identified a partition of the set of tuples we want to count, based on exactly how many 1s there are. Accordingly, the number we seek, by the Rule of Sum, is n X ℓ=3 |Aℓ| = n X ℓ=3 (n ℓ ) You might be wondering whether this answer, in summation notation, is acceptable. In some sense, it is; not 10 minutes ago, we had no idea how many binary n-tuples there were with at least three 1s, and now we have a much better sense of that number. However, the solution, as presented, is more of a method for finding the precise number. If someone came up to you on the street and said, "Quick! Tell me the number of binary n-tuples with at least three 1s!", what would you do? You'd say, "Hold on, I just need to sum this series by evaluating each of the terms individually and then adding..." Not ideal, right? It would be nicer, more convenient, to have a simple form of the solution; perhaps we could write it as just one binomial coefficient, or a sum/difference/product/quotient of two or three or some small number of such coefficients. That way, no matter what n is (i.e. no matter how large it becomes), we know we can always calculate the answer efficiently in a few short steps; moreover, we want to know that the number of such steps does not increase as n increases. With the summation form above, the number of terms in the sum grows as n does. This is not ideal. We will leave the details for you to verify and explain, but we claim that an appropriate partition of the set of all binary k-tuples can be established to prove that 2n = (n


> 🇨🇳 补充内容 (项 108)：此段原文为详细计数论证的进阶练习和补充说明。


) + n X ℓ=3 (n ℓ ) by invoking the Rule of Sum. (In fact, the proof of this equality delves into some of the techniques we will discuss in the next section, but we believe you can understand what the terms of this equation mean and why the equality must hold.) What we want to emphasize, though, is that we can rearrange that equation to obtain a better, in some qualitative sense, form of the original solution we sought: n X ℓ=3 (n ℓ ) = 2n - (n


> 🇨🇳 补充内容 (项 109)：此段原文为详细计数论证的进阶练习和补充说明。


) Look at what we have achieved! No matter how large N is, we only have four terms to evaluate. The fact that this number is fixed is the main point. In fact, solutions of this form are given a name because we like them so much: closed form. The idea is that there is no "unnecessary" summation and the number of terms is fixed, regardless of the value of the variables contained therein. In general, with combinatorics problems, we are always looking for a closed form of the solution, whenever possible. Sometimes, it is easy to come up with


> 🇨🇳 补充内容 (项 110)：此段原文为详细计数论证的进阶练习和补充说明。


a non-closed (some might say "open") form of a solution, but it might take some ingenuity to simplify this to a closed form. In this specific example, we relied on our observation that all binary n-tuples can be classified as having exactly zero or exactly one or exactly two or at least three 1s. This closed form of the solution not only allows us to evaluate the expression quicker and more easily, but it also provides some insight into even more of the underlying structure of the problem. For these reasons, we will always ask for closed form solutions. Now, let's not forget about question (c)! To answer it, we employ a similar technique as in (b) and partition the set of binary n-tuples with an even number of 1s into those with exactly zero 1s (remember, 0 is an even number!), those with exactly two 1s, those with exactly four 1s, and so on. We have to be careful about the upper limit, though, because n is not necessarily even, itself! Recall the floor function that rounds a number down to the largest integer smaller than that number; an example is ⌊5.7⌋= 5. With this in mind, we claim that there are ⌊n/2⌋ X ℓ=0 ( n 2ℓ ) binary n-tuples with an even number of 1s. We will leave it to you to fill in a proper explanation of this claim. Try presenting it to your friend and convincing them it is correct. Don't give up until they're fully convinced! We will forgo trying to find a closed form of this solution because it is not within our grasp... or is it? See what you can deduce about this summation! What happens when n is even? When n is odd? Are there similar sums you can relate this expression to? What can you conclude?
Example 8.3.12. Count the number of binary 4-tuples whose 1s occur in pairs.
To clarify, we would want to include (1, 1, 0, 0) and (1, 1, 1, 1) in our count, but neither (1, 0, 1, 1) nor (0, 1, 1, 1), for instance. Adapt this argument to count the number of binary 5-tuple whose 1s occur in pairs. Can you continue and find a general pattern? To have 1s in pairs in a 4-tuple, this means we can either have 0 or 2 or 4 1s, in total. Let's define the sets S0, S2, and S4 to be the sets of binary 4-tuples whose 1s occur in pairs and that have exactly 0 or 2 or 4 total 1s, respectively. (Note: we are not defining S2 to be the set of binary strings with exactly two 1s, only. That would erroneously count a string like (1, 0, 1, 0).) These sets form a partition of the set of elements we want to count, overall, so we merely need to count the elements of these three sets and add those numbers, by applying the Rule of Sum. • To find |S0|, we need to count the binary 4-tuples with no 1s, and there is only 1 such tuple: (0, 0, 0, 0). • To find |S2|, we need to count the binary 4-tuples with two consecutive 1s and the remaining spots filled by 0s. Writing out the cases by hand, (1, 1, 0, 0) (0, 1, 1, 0) (0, 0, 1, 1)


> 🇨🇳 补充内容 (项 111)：此段原文为详细计数论证的进阶练习和补充说明。


it is obvious that there are only 3 such tuples. (Can you identify a craftier argument for why there are 3? We'll come back to this when we look at 5-tuples.) • To find |S4|, we need to count the binary 4-tuples with four 1s. Certainly (1, 1, 1, 1) is the only such tuple. By the Rule of Sum, then, there are 1 + 3 + 1 = 5 binary 4-tuples whose 1s occur in pairs. To answer this same query about 5-tuples requires a little bit more ingenuity. We will define the same sets, S0, S2, S4, amending the definitions to include 5tuples (instead of 4-tuples). Still, this collection of 3 sets forms a partition of the set of binary 5-tuples we seek to count. It suffices to count each set's elements and apply the Rule of Sum. • |S0| = 1 because only 1 binary 5-tuple has no 1s: (0, 0, 0, 0, 0). • To find |S2|, we can again write out the cases by hand, but it would be nice to come up with an argument we can easily adapt to k-tuples, for any k $\in \mathbb{N}$. To have one pair of 1s and the remaining spots filled by 0s, we can think of the block "1, 1" as a single unit, placed amongst three 0s. Thus, we are really counting how many ways we can place a single, special unit into an ordered list of length 4 and then deterministically fill the remaining spots with another fixed element. Certainly, there are 4 ways to do this, and writing out the cases by hand verifies this claim. (What we are really doing is noting that a consecutive pair of 1s is determined by the index in the tuple of the first 1 of the pair; that index can be any of {1, 2, 3, 4}, so there are {4


> 🇨🇳 补充内容 (项 112)：此段原文为详细计数论证的进阶练习和补充说明。


} = 4 options.) • This technique applies when we consider |S4|, as well. Here, we have two separate, consecutive pairs of 1s, so we can treat each pair as a single block, "1, 1". Thus, we really have two "1, 1" blocks and one 0 to place in an ordered list of length 3. Since the 1, 1 blocks are identical, we can count these ordered lists by selecting the two spots for the 1, 1 blocks. Therefore, there are {3


> 🇨🇳 补充内容 (项 113)：此段原文为详细计数论证的进阶练习和补充说明。


} = 3 such tuples. (Equivalently, we can think of selecting the spot for the 0, i.e. {3


> 🇨🇳 补充内容 (项 114)：此段原文为详细计数论证的进阶练习和补充说明。


} = 3 options.) Therefore, there are 1 + 4 + 3 = 8 binary 5-tuples whose 1s occur in pairs. Alphabets and Words Related to the idea of k-tuples with elements drawn from [n] is the idea of creating words from a given alphabet. There is not much of a difference between these two concepts (and mathematically, they are really equivalent, so there's nothing new!) but it allows for different terminology and makes pertinent connections to some "real-world" concepts and problems. For this reason, and the fact that you might find it easier to work with one formulation or the other, we present this subsection and make connections to the previous subsection.


> 🇨🇳 补充内容 (项 115)：此段原文为详细计数论证的进阶练习和补充说明。


We will introduce and motivate the ideas of this subsection with some examples. In each example, we will specify an alphabet, whose elements are the allowable letters we can use to construct words. By "word", though, we really mean any ordered string of letters drawn from the given alphabet. So, for instance, we use the standard English alphabet in the first example; in that case, ZPQ is a perfectly acceptable three-letter word (but good luck trying to pronounce it!). The main reason we allow for this generality is to avoid any semantic or etymological arguments, like whether or not REALISE should be an acceptable variant of REALIZE or if ZZZ really belongs as an onomatopoetic interjection. This means we have to strip away some of the connotations around the word "word" and think of it as just a string of letters with no other inherent meaning besides its components and their order.
Example 8.3.13. Let's consider the standard, 26-letter English alphabet in this
example. 1. How many 3-letter words can be made this alphabet? Think about how this is identical to asking about T26,3. We have 26 allowable letters and want to form ordered lists of length 3. By establishing a bijection between the sets {A, B, C,..., Z} and [26] (which is actually a common and simple substitution cipher you might have played with as a child), we can rigorously show how this question is equivalent to asking what |T26,3| is. Without necessarily making this connection, though, we can easily count the 3-letter words by noting that constructing one amounts to a 3 step process (fill in 3 letters, left to right) with 26 options at each step. Thus, there are 263 three-letter words. 2. How many 4-letter words can be made? By the same logic as the previous example, there are 264 four-letter words. 3. How many n-letter words? We'll let you handle this one, 4. How many 4-letter words start with a vowel?
Note: we consider {A,E,I,O,U} to be the set of vowels (i.e. Y is never
included, despite what the alphabet song might tell you). With that in mind, we can amend the four-step process of constructing a four-letter word to guarantee a vowel occurs in the first position on the left. There are 5 ways to complete that step, followed by 26 ways for each of the next 3 steps. Thus, there are 5 $\cdot$ 263 four-letter words that start with a vowel. 5. How many 4-letter words have at most 2 consonants? A consonant is a non-vowel, so there are 26 -5 = 21 consonants in the alphabet, under our definitions. To have at most two consonants means we have exactly 0 or exactly 1 or exactly 2, so we can partition the set


> 🇨🇳 补充内容 (项 116)：此段原文为详细计数论证的进阶练习和补充说明。


of words in question into three corresponding sets, S0, S1, S2, and count each separately. By applying the Rule of Product, we find that |S0| = 54 |S1| = (4


> 🇨🇳 补充内容 (项 117)：此段原文为详细计数论证的进阶练习和补充说明。


) $\cdot 2^1 \cdot 5$3 |S2| = (4


> 🇨🇳 补充内容 (项 118)：此段原文为详细计数论证的进阶练习和补充说明。


) $\cdot 21^2 \cdot 5$2 and, therefore, there are 54 + 4 $\cdot 2^1 \cdot 5$3 + (4


> 🇨🇳 补充内容 (项 119)：此段原文为详细计数论证的进阶练习和补充说明。


) $\cdot 21^2 \cdot 5$2 four-letter words with at most two consonants. (Challenge problem: How many four-letter words have at least three consonants? Use this to make a claim about the number 264.) What is wrong with the following argument about S2?: Construct a fourletter word with exactly two consonants by selecting two consonants, then selecting a position for the first consonant, then selecting a position for the second consonant, then filling the remaining two spots with vowels, yielding (21


> 🇨🇳 补充内容 (项 120)：此段原文为详细计数论证的进阶练习和补充说明。


) $\cdot 4 \cdot 3 \cdot$ 52 such words. Think carefully about this. Remember, these "find the flaw" questions are not merely looking for you to identify that there is an error, but also to explain why it is an error and how it could be fixed. 6. How many 4-letter words have 4 distinct letters? Without any pre-thought, we can jump into answering this one by describing a four-step process of filling the four letters left to right, and reducing the number of options by one at each step. Thus, there are $2^6 \cdot 25 \cdot 2^4 \cdot 2$3 four-letter words with four distinct letters. Does this look familiar, though? Look back to where we defined arrangements. This is precisely the idea we are using here! From a set of 26 elements, we want to construct an ordered list of length 4 with no repetition, i.e. a 4-arrangement from a set of 26 elements. The formula we derived tells us there are exactly (26


> 🇨🇳 补充内容 (项 121)：此段原文为详细计数论证的进阶练习和补充说明。


) $\cdot$ 4! = 26! 4! 22!4! = 26! 22! = $2^6 \cdot 2$5 $\cdot$ $2^4 \cdot 2$3


> 🇨🇳 补充内容 (项 122)：此段原文为详细计数论证的进阶练习和补充说明。


such arrangements. That's the lesson of this example: by taking advantage of previously defined terms and derived formulas, and relating a current question to those ideas, we can "jump" to a solution. 7. How many 4-letter words have exactly one letter repeated twice? To construct a word with these properties, we need to know which letter is repeated, and where its two instances occur, as well as the other two letters that appear in the word. Thus, we identify a three-step process: (1) select the repeated letter; (2) select 2 of the 4 open spots for that letter; (3) arrange two of the remaining 25 letters in the remaining two spots: (26


> 🇨🇳 补充内容 (项 123)：此段原文为详细计数论证的进阶练习和补充说明。


) $\cdot$ 2! 8. How many 5-letter words have exactly two letters repeated twice each? Following similar logic as the previous example, we can (1) select two letters to be repeated; (2) select two of the 5 open spots for the first (alphabetically speaking) repeated letter; (3) select two of the remaining 3 spots for the second (alphabetically) repeated letter; and (4) select one of the remaining 24 letters to fill the final, fifth spot. Thus, there are (26


> 🇨🇳 补充内容 (项 124)：此段原文为详细计数论证的进阶练习和补充说明。


)
Example 8.3.14. How many rearrangements (i.e. permuations) of the alphabet
put U and ME together?, You might think to approach this problem with a "subtraction" idea; that is, you might try to count all of the rearrangements of the alphabet that put the letter U not next to the letters ME (in that order). You should try working this out and see where it takes you. What we will do, though, is present a different and, we believe, shorter solution. The idea behind this solution will be useful in other problems, and it boils down to treating the two-letter word ME as a single block, just like any other single letter. To reverse the question a little bit, instead of asking how many words there are of some type from a given alphabet, we might wonder how many rearrangements (i.e. anagrams) there are of a given word. Care must be taken in considering these questions because when letters are repeated, things can get tricky! For instance, how many anagrams are there of the word A? How about the word AAAAA? How about AABBBCCCCDD? Exactly!
Example 8.3.15. Let's start with a simple case. How many anagrams of the word
HEART are there? Remember that we count all permutations of the letters as an acceptable word, so leave behind your Scrabble thought processes,(By the by, the Scrabble answer to this question is 4--HEART, HATER, EARTH, RATHE.) Since each letter is distinct in this word, the answer is simple: we merely count all of the permutations of the 5 letters. Accordingly, there are 5! = 120 anagrams of HEART.


> 🇨🇳 补充内容 (项 125)：此段原文为详细计数论证的进阶练习和补充说明。


Now, how many anagrams of APPLE are there? Notice that the letter P appears twice, so we can't really consider permutations of a five-element set. If we were to do that, each word would actually occur twice; that is, APPLE and APPLE would both be counted. Do you see the difference between those two words? We just switched the Ps! Of course, these are the same word, so we have to factor this in to our consideration of permutations. How do we do this? One helpful trick is to "label" the repeated Ps. Reading left to right in APPLE, let's call the first one P1 and the second one P2. This will help us to sort out the repeated permutations. We now have five distinct elements in our word--A, P1,P2,L,E--so we can consider all 5! permutations of these elements. We know that this overcounts, though, so we would like to figure out how by how much this overcounts. Define G to be the set of anagrams of APPLE (so we're trying to identify |G|) and let M be the set of permutations of the five distinct elements listed above. How are |G| and |M| related? To answer this question, we can think of constructing the elements of M from elements of G. Specifically, we can construct any element of M (a permutation of the 5 distinct elements) by first taking an element of G (an anagram of APPLE) and labeling the Ps. However, this won't generate all elements of M. To do this, we have to take elements of G and, from them, construct two elements; specifically, we must label the Ps and then consider both of the orderings of the Ps within the word. Let's see an example: • Take an element of G, say PAPEL. • Label the Ps from left to right: P1AP2EL • Construct both orderings of the Ps and count both of those words as elements of M: P1AP2EL$\in M and P2AP1EL\in M$ Since there are 2! = 2 ways to permute the two Ps within the word, we have shown that |G| $\cdot$ 2! = |M|. We described a two-step process to generate elements of M and applied the Rule of Product. Accordingly, we can rearrange this equation to find the quantity we were looking for: |G| $\cdot$ 2! = |M| =$\Rightarrow$|G| = |M| 2! = 5! 2! = 60 For a slightly harder example, let's count the anagrams of COMBINATORICS. We want to apply the same strategy as the previous example and label the repeated letters to relate the anagrams to permutations of, in this case, 13 distinct elements. Again, let's define G to be the set of anagrams of COMBINATORICS and M to be the set of permutations of the 13 distinct elements in {C1O1MBI1NATO2RI2C2S}. We can describe a four-step process that generates elements of M: 1. Take an element of G and label the repeated letters, reading left to right: |G| options 2. Permute the two repeated Cs: 2! options.


> 🇨🇳 补充内容 (项 126)：此段原文为详细计数论证的进阶练习和补充说明。


3. Permute the two repeated Os: 2! options. 4. Permute the two repeated Is: 2! options. Thus, by the Rule of Product, we may conclude |M| = |G| $\cdot 2! \cdot 2! \cdot 2! =\Rightarrow$|G| = |M| 2! $\cdot 2! \cdot$ 2! = 13! 2! $\cdot 2! \cdot$ 2! You might wonder why we chose to write 2! $\cdot 2! \cdot$ 2! instead of just 8. We find it more enlightening and illustrative to leave our answer in terms of factorials because it indicates where those terms came from, too. What happens if a letter is repeated more than twice? The only difference occurs when we consider permuting the repeated instances of that letter. We will let you fill in the details of the argument, but we claim that the word AABBBCCCCDD has 11! 2! $\cdot 2! \cdot 3! \cdot$ 4! anagrams. Can you "see" why without going through the details completely yet? Can you fill in those details to confirm your intuition? Can you prove this fact and convince a friend? Try it! There are several more anagram questions in the exercises. Later on, we will even prove a result that will generalize this technique of labeling repeated letters and accounting for their permutations. Before moving on, we should point out an observation that is similar to something we've seen before. In some examples so far, we ended up subtracting a count from a total, and we pointed out that a sophisticated proof-writer would just state the subtraction idea directly, although we ask you to phrase it in terms of a partition and apply the Rule of Sum. Similarly, with the previous example we just did, we ended up dividing a count to eliminate some overcounting, but we made sure to phrase this in terms of a process and apply the Rule of Product; afterwards, we could algebraically divide to simplify. A sophisticated proofwriter would write probably write the same solution by taking the overcount and arguing that we can "divide out" to eliminiate the overcounting. This is dangerous, we say, and we require you to not do this (for now, in our contexts). If you allow yourself to make these kinds of arguments, it's too easy to erroneously "divide out" in a situation where it is unwarranted and incorrect to do so! Forcing yourself to work out these arguments "from the ground up" will more firmly solidify these underlying principles and allow you to more confidently apply "subtraction" and "division" principles later on in your mathematical careers. Just remember that we ask you to use only ROS and ROP in our contexts! Let's look at two quick examples of alphabets and words that aren't based on the standard English alphabet, per se.
Example 8.3.16. A phone number in the United States consists of an area code
(3 digits) and a local number (7 digits). The digits are drawn from the set


> 🇨🇳 补充内容 (项 127)：此段原文为详细计数论证的进阶练习和补充说明。


{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, but neither the area code nor local number can begin with a 0. How many possible phone numbers are there? This is easy to count by establishing a 10 step process, corresponding to the 10 total digits of a phone number. Eight of the digits have 10 options, and two of them have 9 options (no 0), so the Rule of Product tells us there are 1$0^8 \cdot 9$2 = 8, 100, 000, 000 possible phone numbers. This number is slightly larger than the current world population, so it seems like our system is safe, for now!
Example 8.3.17. Suppose a restaurant has a menu with three different cate-
gories: appetizers, entrees, and desserts. There are 5 appetizers, 9 entrees, and 4 desserts. You take your date to this restaurant and you pass the time waiting for your server t)o appear by figuring out how many possible orders you can make, imposing certain conditions. (Unfortunately, you forget to decide what to order and you end up choosing an order randomly, but that's beside the point.) (1) How many possible orders can you make, assuming you must order one appetizer, one entree, and one dessert? This is a simple application of ROP. There are 5 $\cdot 9 \cdot$ 4 = 180 possible orders. How is this like alphabets and words? Well, you can think of it as constructing a three-letter word, but the alphabet for each "slot" in the word is different. (2) How many possible orders can the two of you make, assuming you each order one app, one tree, and one zert, but you two can't order the same thing in any category? Think of this as a 3-step process, with each step divided into 2 parts. First, you order an appetizer, and then your date does, too (making sure to pick from amongst the appetizers you didn't pick). Second, you order an entree, and then your date picks a different one. Third, you order a dessert, and then your date picks a different one. Clearly, then, there are (5 $\cdot 4) \cdot (9 \cdot 8) \cdot (4 \cdot 3) = 2^0 \cdot 72 \cdot$ 12 = 17280 possibilities. Compare this to the number of possibilities without the restriction of ordering different items in each category, which we can find by using our work on question (1): 1$8^0 \cdot 1$80 = 32400 Again, we can think of this as a restrictive alphabet/words problem. Balls and Bins This is a common formulation of combinatorics problems in more advanced courses. It's particularly helpful when discussing probability and using combinatorics facts and ideas to explore probability. We would like to bring it up here


> 🇨🇳 补充内容 (项 128)：此段原文为详细计数论证的进阶练习和补充说明。


because it introduces the important distinctions between distinguishable and indistinguishable objects. To motivate this discussion, let's pose a seemingly simple question: Consider a bin containing n balls; how many ways can we select k balls? What's your answer? If you said " {n k } ", you could be right. If you said "1", you could also be right. How is that possible?! Well, we didn't specify whether the n balls in the bin are distinguishable; that is, we didn't say whether or not they're all different, whether we can tell any two balls apart. Imagine a bucket with 100 tennis balls in it. If we pulled out two balls and showed them to you, could you tell them apart? Maybe they have a different number of fuzzy yellow hairs on them, or maybe they're different brand names, or something like that... but maybe we can't do that. Maybe all of the balls are completely identical. In that case, it doesn't matter "which" k balls we pull out, because we can't tell them apart. All "possible" selections of k balls amount to the same thing, so the answer of "1" makes total sense. However, if all of the balls had a distinct number on them, or they were all different colors, or... imagine any distinguishing property you'd like. In any of those cases, " {n k } " is the correct answer. For these reasons, the originally posed question was a poor one; we should have been specific about whether the balls are distinguishable or not. This idea of distinguishability has come up before. Remember that grid of counting formulas we established back in Section 8.2.3? One of the essential questions in the grid was whether the order of a selection/arrangement distinguished the outcome. For example, a selection does not care about order. The selections {1, 3, 4} and {3, 4, 1} are identical (you should also think of them as sets to understand this) because the order in which the elements are written does not distinguish them. Conversely, the arrangements (1, 3, 4) and (3, 4, 1) are different because the order of the elements does distinguish them. In the context of a "balls and bins" problem, we will specify the distinguishability of items by saying they are numbered or colored somehow. This might also involve a mix of distinguishable/indistinguishable features, though, so be careful! The next example illustrates this interplay.
Example 8.3.18. Suppose we have a bin containing balls that are colored red,
blue, or green (i.e. each ball has one color of those three). There are 3 balls of each color in the bin, and any two balls of the same color are indistinguishable. We pull out four balls. How many possible outcomes are there? Try playing around with this problem before reading our solution. You might come up with your own method of solving it! A first approach here might be to just enumerate the possibilities and then


> 🇨🇳 补充内容 (项 129)：此段原文为详细计数论证的进阶练习和补充说明。


try to infer a pattern. We might strart writing out the outcomes as: 3 Red and 1 Blue 3 Red and 1 Green 2 Red and 2 Blue 2 Red and 2 Green 2 Red and 1 Blue and 1 Green... and so on. Notice how we are keeping track of this information, though; every outcome is characterized by (a) how many red balls we picked, (b) how many blue balls, and (c) how many green balls. In essence, we can characterize every outcome by an ordered 3-tuple of the form (r, b, g) where r is the number of red balls, and similarly for b and g. The only condition we require is that r+b+g = 4 and each value satisfies 0 $\leq r \leq3, 0 \leq b \leq3, 0 \leq g \leq$3. We really just need to count how many 3-tuples satisfy those conditions! We can split this count into how many nonzero terms there, and analyze each case separately. • If two terms are 0, then the third term must be 4. There are {3


> 🇨🇳 补充内容 (项 130)：此段原文为详细计数论证的进阶练习和补充说明。


} = 3 choices for which term is nonzero, so there are 3 such possibilities. • If one term is 0, then the other two terms must sum to 4 and both be nonzero. There are 3 ways to do this: 1 + 3 and 2 + 2 and 3 + 1. Since there are 3 choices for which term is 0, by ROP, there are 3 $\cdot$ 3 = 9 such possibilities. • If all three terms are nonzero, then we see that the only such sum is 1+1+2, in some order. There are 3 choices for which term is 2, and then the other terms must be 1. Thus, there are 3 such possibilities. By ROS, there are 3 + 9 + 3 = 15 total possibilities. Lattice Paths Consider the set $\mathbb{N}$ $\cup {0} \times \mathbb{N} \cup{0} = (N \cup \{0\}$)2 consisting of all ordered pairs of natural numbers or 0.In fact, let's represent this set visually on the plane:


> 🇨🇳 补充内容 (项 131)：此段原文为详细计数论证的进阶练习和补充说明。


This "grid" of dots on the plane is known as a lattice. Here's a natural question: Given any point in the lattice, how many ways are there to "get there" from the origin, (0, 0)? Let's be more specific. Let's define a lattice path to be a path from (0, 0) to a particular point that is only allowed to move rightwards or upwards at any step. This is what the next definition conveys:
<div class="def-definition" markdown>
**Definition 8.3.19. Let $(x, y) \in (\mathbb{N} \cup \{0\})^2$. A lattice path to (x, y) is an**
</div>
ordered tuple of points in the plane lattice where the first element of the tuple is (0, 0), the last element of the tuple is (a, b), and every element in the tuple only differs from the previous one by having exactly one coordinate that is exactly one larger than the corresponding coordinate of the previous element. More rigorously, given (x, y) a lattice path is an n-tuple (P1, P2,..., Pn), for some n $\in \mathbb{N}$, where each Pi = (xi, yi) is a point in the lattice, and $\forall$ i $\in$[n -$1]. (xi+1, yi+1) = (xi + 1, yi) \vee(xi+1, yi+1) = (xi, yi + 1) and, furthermore, (x1, y1) = (0, 0) and (xn, yn) = (x, y). That is, a lattice path is a sequence of points in the lattice from (0, 0) to (n, n) where we are only allowed to move rightwards or upwards by one grid point at every step.$
Example 8.3.20. Consider the point (2, 4) in the plane lattice. In the diagram
below, we plot a few sample lattice paths to (2, 4).


> 🇨🇳 补充内容 (项 132)：此段原文为详细计数论证的进阶练习和补充说明。


Our question is as follows: Given $(a, b) \in (\mathbb{N} \cup \{0\})^2$, how many distinct lattice paths are there to (a, b)? To begin to answer this, let's look at a simple case with small values so we can actually enumerate all of the paths. Let's consider lattice paths to (2, 2):


> 🇨🇳 补充内容 (项 133)：此段原文为详细计数论证的进阶练习和补充说明。


How might we represent lattice paths in a combinatorial way? That is, how can we represent them in a way that allows us to conveniently count some objects? Think about the defining aspects of a lattice path: every "move" in the construction of a lattice path must be rightwards or upwards. It would make sense, then, to somehow represent when we make a "Right" move and when we make an "Up" move. Then, we just need to count how many sequences of choices of "Right" and "Up" actually bring us to the point (x, y) in question. That's easy, though! What characterizes the point (x, y) on the plane? Well, it's x grid points to the right of (0, 0) and y grid points up from (0, 0). Thus, no matter what our path looks like, we know there must be x rightward moves and y upward moves. Look back at the 6 lattice paths to (2, 2) above. Think about following the path, starting at (0, 0), and writing down $\mathbb{R}$ or U at each grid point, depending on where we go next. This yields the following 6 sequences of Rs and Us RRUU, RUUR, RURU, URRU, URUR, UURR What properties do these sequences share? Each one has 2 Rs and 2 Us, since we must end at (2, 2), and so each sequence has 4 terms, in total. Notice that this is much like a restricted alphabet/words problem: we want to find the number of words of length 4, drawn from the alphabet {$\mathbb{R}$,U}, that contain exactly two of each letter!


> 🇨🇳 补充内容 (项 134)：此段原文为详细计数论证的进阶练习和补充说明。


In general, then, we know that any lattice path to (x, y) can be represented by a (x + y)-tuple of Rs and Us with exactly x Rs and y Us. To identify how many such sequences there are, we have a two step process: 1. From x + y empty slots, choose x of them to be filled with Rs: {x+y x } options 2. Fill the remaining (x + y) -x = y slots with Us: 1 option (deterministic) Thus, we have the following result.
Proposition 8.3.21. For every (x, y) $\in (\mathbb{N} \cup \{0\})^2, there are exactly
(x + y x ) lattice paths from (0, 0) to (x, y). We will explore some interesting applications and properties of lattice paths in the exercises. For now, we want to point out their existence and their relationship with sequences and selections. But here's one more observation about them: Why did we choose to count the number of sequences of length x+y with exactly x Rs? Would it be any different to count the the number of sequences of length x + y with exactly y Us? Think about it: every lattice path to (x, y) needs exactly x Rs and exactly y Us, and ensuring one of those properties holds guarantees the other will, as well. Thus, we could have presented the following result:
Proposition 8.3.22. For every (x, y) $\in (\mathbb{N} \cup \{0\})^2, there are exactly
(x + y y ) lattice paths from (0, 0) to (x, y). This not only proves the following fact (x + y x ) = (x + y y ) but it also introduces us to a new and helpful proof strategy: Counting in Two Ways. We identified one set of objects (the set of lattice paths from (0, 0) to (x, y)) and proceeded to explain two different ways of counting that same set of objects. Each way yielded a different expression for the cardinality of that set, and we can therefore declare those two expressions to be equal. This first example illustrates the main idea behind Counting in Two Ways, and we will explore several more examples, and the general technique, in the following section.
### 8.3.4 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory!


> 🇨🇳 补充内容 (项 135)：此段原文为详细计数论证的进阶练习和补充说明。


(1) How can you identify that a proposed counting argument is an undercount? How can you show it is an overcount? (2) Explain the relationship between "k-tuples from [n]" and "Alphabets and Words". How are they fundamentally the same? (3) Say we are selecting k balls from a bin with n balls. Why does it matter whether the balls are distinguishable? (4) Why is it that the number of lattice paths from (0, 0) to (x, y) is equal to both {x+y x } and {x+y y } ? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Find the number of 5-card poker hands that are two pair, and prove your claim. (2) Find the number of 5-card poker hands that are a full house, and prove your claim. (3) How many anagrams of the word COMBINATORICS are there? What about of MASSACHUSETTS? (4) Consider finding the number of 4-tuples from {1, 2, 3} that include at least one of each number. For each of the following proposed "proofs", show that it is incorrect by exhibiting such an object that has been counted twice by the proposed argument. (a) Pick one of the 4 spots in the tuple for the 1, then pick a spot for the 2, then pick a spot for the 3. Then, pick one of the three elements to appear in the 4th empty spot. (4


> 🇨🇳 补充内容 (项 136)：此段原文为详细计数论证的进阶练习和补充说明。


) = 72 (b) Pick 3 of the 4 spots to be filled with the elements 1,2,3. Permute those elements in those chosen spots. Pick a number for the 4th empty spot. (4


> 🇨🇳 补充内容 (项 137)：此段原文为详细计数论证的进阶练习和补充说明。


) 3! $\cdot$ 3 = 72 (5) For this problem, consider a word to be any string of English letters, whether or not it actually spells something in the dictionary. For instance, ZYQFIB is a valid word of length 6.


> 🇨🇳 补充内容 (项 138)：此段原文为详细计数论证的进阶练习和补充说明。


(a) How many words of length 2 are there? (Answer this question in two ways: with an exponential number, and with a sum of two terms.) (b) How many words of length 7 have exactly 3 As? (c) How many words of length 7 have at most 2 vowels? (Note: A, E, I, O, U are vowels. Y is not.) Consider the set Sn of all binary strings of length n. For each of the following stated properties, count how many elements of Sn have that property. (Note: Each property is separate; don't consider satisfying all of them at once, say.) (a) Exactly 3 positions are 0s. (b) At most 3 positions are 0s. (c) At least 4 positions are 0s.
Note: Use the last two parts to write 2n as a sum of binomial coefficients!
(d) More positions are 0s than are 1s. (6) Let $n \in \mathbb{N}$ be given. How many lattice paths go from (0, 0) to (2n, 2n)? How many such paths also go through (n, n)? (7) Consider the following explanation: The number of 6-card hands, as dealt from a standard deck of cards, that have at least one card from each of the four suits is (13


> 🇨🇳 补充内容 (项 139)：此段原文为详细计数论证的进阶练习和补充说明。


) because we select one card from each of the four suits and then, from the remaining 48 unused cards, select two more. Is this count correct? If you think it is an overcount, exhibit a specific hand and show how it is counted in two ways. If you think it is an undercount, exhibit a specific hand and show how it is not counted.


> 🇨🇳 补充内容 (项 140)：此段原文为详细计数论证的进阶练习和补充说明。


## 8.4 Counting in Two Ways If you're just jumping into this section, reread the last example from the previous section because it provides a perfect introduction to (and example of) Counting in Two Ways. In that example, we counted the number of lattice paths to a particular point in two different ways, deducing that the two expressions we found must be equal. Specifically, we deduced that {x+y x } = {x+y y }. With that example already under our belt, we will outline a general strategy here and apply it to several examples. Along the way, we will not only practice this technique, but we will also be proving some useful combinatorial results that we can apply to other problems! Let's start by actually presenting an alternative proof of the example from the previous section. There is a much shorter argument that doesn't delve into lattice paths at all and is a more memorable and understandable explanation of this result.
Proposition 8.4.1. Let $n, k \in \mathbb{N} \cup \{0\}$. Then
(n k ) = ( n n -k ).
<div class="def-proof" markdown>
*Proof.* Let S be the set of subsets of [n] with size k, i.e.
</div>
S = {$T \subseteq [n]$ | |T| = k} By the definition of k-selections, |S| = {n k }, since constructing a set T $\subseteq$[n] with |T| = k amounts to selecting k elements from a set of n elements. Equivalently, we can construct a set $T \subseteq [n]$ with |T| = k by selecting n -k elements to not include in T; this means n -(n -k) = k elements have been selected to belong to T. The number of ways to do this is { n n-k }. Since every such set T can be constructed this way, we have shown |S| = { n n-k }. Therefore, {n k } = { n n-k }. We find this to be a more memorable proof of this fact because we can summarize the entire proof in just one sentence rather nicely "Count the k-element subsets of [n] by identifying the elements to include or the elements to omit." This is the idea we remember; from it, we can reconstruct the proof. It doesn't make sense to try to "memorize" a proof sentence by sentence; rather, it is helpful to remember the kernel of the proof's main idea and then fill in the details.
### 8.4.1 Method Summary Why It Works Let's abstract one level and discuss Counting in Two Ways as a proof technique. Let's talk about why it works and how to employ it. Then, we'll go through


> 🇨🇳 补充内容 (项 141)：此段原文为详细计数论证的进阶练习和补充说明。


