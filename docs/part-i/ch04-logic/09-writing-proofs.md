---
title: Writing Proofs: Strategies and Examples
tags:
  - 逻辑
  - 命题
  - 量词
  - 证明写作
---

# Writing Proofs: Strategies and Examples

4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 证明写作（Writing Proofs）本节是关于如何写出清晰、完整、有说服力的数学证明的实用指南。重点不是"证明什么"而是"怎么写"。


practice with these logical concepts and, we strongly believe, help you adapt them for your own uses in the future. For each example provided, we have boxed the proof strategy in blue and the example implementation in green and any necessary scratch work in red. Any other discussion of the strategy or the implementation appears outside of those boxes. Also, several of the examples we consider in this section (and the next one) are interesting and useful results, in their own right. You'll notice that some of them have a name or a descriptive title, which is meant to indicate this fact. While the main emphasis of this section is on the proof strategies---developing them and seeing how to use them---we encourage you to also keep in mind these examples as interesting facts, themselves. We'll bring up this idea again when it's warranted, but we'll keep those discussions brief, so as not to distract from the overall structure of this section. Direct vs. Indirect methods You will also notice that each subsection includes strategies for both direct and indirect methods. These terms might not be familiar to you yet. All they refer to is whether or not we try to prove a statement (1) directly by demonstrating that it is True, or (2) indirectly by invoking the Law of the Excluded Middle, by demonstrating that its logical negation is False. Both forms of strategy are, in general, equally valid, but direct proofs are typically considered subjectively better by many readers. (Sometimes, you might write an indirect proof that is actually hiding a direct proof inside it!) These subjective ideas will be assessed and discussed as we work through examples and ask you to write proofs on your own, in the exercises. You'll notice that all of our indirect proofs begin with the phrase "Assume for sake of contradiction", usually abbreviated as "AFSOC". This is an important and helpful phrase. It signals to the reader of our proof that we are going to make an assumption but we don't really think that the assumption is valid. Rather, we are going to use this assumption to derive something False, a contradiction. This will allow us to conclude that our original assumption was invalid, so its logical negation (i.e. our original statement that we hoped to prove) is actually True. You'll see that we use the symbol " $\times\times\times\times$ " to indicate a contradiction, but we also make sure to point out why we have found a contradiction. We don't leave it to the reader to figure it out! Alright, that's enough preamble. Let's dive right in and WRITE SOME PROOFS!
### 4.9.1 Proving $\exists \mathbb{C}$laims An "$\exists$" claim is one of existence. It asserts that some particular object exists as an element of some set and that it has a certain property. To prove such a claim, we need to exhibit such an object and verify, for our reader, that (1)


> 🇨🇳 **证明的目的** 证明是一项说服活动——你要说服读者某个命题为真。好的证明让读者无需证者在场就能理解每一步推理。


that object is an element of the correct set and (2) that object has the correct property. Direct Method Strategy:
Claim: $\exists x \in S$. P(x)
Direct proof strategy: Define a specific example, y =. Prove that $y \in S$. Prove that P(y) holds true.
Example 4.9.1. Solving a system of linear equations:
Statement: Fix a, b, c, d, e, $f \in \mathbb{R}$ with the property that ad -bc $\neq$ 0. We claim that one can simultaneously solve ax + by = e (4.1) cx + dy = f (4.2) for some x, $y \in \mathbb{R}$. Define S(x, y) to be the statement "x and y simultaenously satisfy both equations, (4.1) and (4.2), above". Then we claim $\exists x$, $y \in \mathbb{R}$. S(x, y) First, we must do some scratch work to construct the solution. Then, we can write a proof that defines the objects x and y and shows why they work. Scratch work: We need ax + by = e and cx + dy = f, and we want to know which x and y make this work. Let's multiply the first and second equations by the right coefficients (namely, d and -b, respectively) so we can cancel the y terms by adding


> 🇨🇳 **证明写作的基本原则** (1) 明确写出要证什么（命题 $P$）；(2) 每步推理都有充分理由；(3) 不跳步——每步都让读者能跟上；(4) 结论清晰明确。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **条件语句 $P \Rightarrow \mathbb{Q}$ 的证明** 最常用三种方法：(a) 直接证明：假设 P，推导 Q。(b) 逆否证明：假设 \n\neg Q，推导 \n\neg P。(c) 反证：假设 $P \wedge \neg \mathbb{Q}$，找矛盾。


the two lines: adx + bdy = de + {-bcx -bdy = -bf } (ad -bc)x = de -bf Dividing tells us x = de-bf ad-bc, which is okay because ad -bc $\neq$ 0. Doing something similar, canceling the x terms, tells us how to get y: acx + bcy = ce + {-acx -ady = -af } (bc -ad)y = ce -af Dividing tells us y = af-ce ad-bc. The main lesson here is that we do not need to show this scratch work in our proof below! We don't assume that a reader would care to wade through our messy notes about how we came up with the solution to the system of linear equations. Rather, we assume the the reader only cares about what the solution is and why it's a solution. Also, this makes the proof much more concise, so it can be read more easily and quickly. Implementation:
<div class="def-proof" markdown>
*Proof.* Since ad -bc $\neq$ 0 (by assumption), we may define
</div>
x = de -bf ad -bc and y = af -ce ad -bc and know that x, $y \in \mathbb{R}$. Then, ax + by = (ade -abf) + (abf -bce) ad -bc = ade -bce ad -bc = e(ad -bc) ad -bc = e cx + dy = (cde -bcf) + (adf -cde) ad -bc = adf -bcd ad -bc = f(ad -bc) ad -bc = f so S(x, y) holds. If you've studied some linear algebra before, you'll recognize the term ad-bc as the determinant of the matrix [ a b c d ]. The stipulation that ad -bc $\neq$ 0 means that we require this matrix of coefficients to have an inverse, to be "non-


> 🇨🇳 **直接证明模板** "要证 $P \Rightarrow \mathbb{Q}$，假设 $P$ 成立。[推导过程]。因此 $Q$ 成立。"$\square$"


singular". In that situation, we have a solution to the system for any e, $f \in \mathbb{R}$. Indirect Method (Proof by Contradiction) This strategy relies on the logical negation of an $\exists$ claim: $\neg$ {$\exists$x \in$ S. P(x) } $\Leftrightarrow \f\forall x \in S. \negP(x) We will assume this negation and deduce something contradictory from it, meaning the negation is False so the original is True.$
Claim: $\exists x \in S$. P(x)
Indirect proof strategy: AFSOC that for every $y \in S, \negP(y) holds. Find a contradiction.$
Example 4.9.2. A version of the Pigeonhole Principle:
Statement: Suppose $n \in \mathbb{N}$ and we have n real numbers, a1, a2,..., an $\in \mathbb{R}$. We claim that one of the numbers is at least as large as their average. That is, $\exists$B \in$[n]. aB $\geq 1$ n n X i=1 ai
<div class="def-proof" markdown>
*Proof.* AFSOC none of the numbers are at least as large as the average,
</div>
i.e. $\f\forall i \in$[n]. ai < 1 n n X i=1 ai Define the constant S = Pn i=1 ai, so that ai < S n. Then we can sum all of the ais and observe that S = n X i=1 ai < n X i=1 S n = $n \cdot$ S n = S This shows that the real number S is strictly less than itself: $S < S. This is a contradiction. \times\times\times\times Therefore, the original assumption was false, and the claim follows. As stated, this is a version of the Pigeonhole Principle. We will investigate and use this principle again in Section 8.6, when we study combinatorics.$


> 🇨🇳 **例** 证明"若 $n$ 是偶数则 $n^2$ 是偶数"。设 $n$ 是偶数，则 $n=2k$（$k\in\mathbb{Z}$）。故 $n^2=(2k)^2=4k^2=2(2k^2)$，即 $n^2$ 是偶数。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **逆否证明模板** "要证 $P \Rightarrow \mathbb{Q}$，我们证其逆否 $\neg \mathbb{Q} \Rightarrow \n\neg P$。假设 $\neg \mathbb{Q}$。[推导过程]。因此 $\n\neg P$。"$\square$"


### 4.9.2 Proving $\f\forall \mathbb{C}$laims A "$\f\forall$" claim is one of universality. It asserts that all elements of a set have some common property. To prove such a claim, we need to show that every element of the set has that property. To accomplish this "all at once", we will consider an arbitrary and fixed element of the set, and prove that it has the desired property. Because this object is arbitary, our argument applies to every element of the set. Because this object is fixed, we are allowed to refer to it by name throughout the proof. Direct Method Strategy:
Claim: $\f\forall x \in S$. P(x)
Direct proof strategy: Let $y \in S$ be arbitrary and fixed. Prove that P(y) holds true.
Example 4.9.3. A version of the AGM Inequality:
Statement: $\f\forall x, y \in \mathbb{R}. xy \leq$ { x+y


> 🇨🇳 **例** 证明"若 $x^2$ 是偶数则 $x$ 是偶数"。逆否："若 $x$ 是奇数则 $x^2$ 是奇数"。设 $x=2k+1$，则 $x^2=4k^2+4k+1=2(2k^2+2k)+1$，奇数。


}2 Implementation:
<div class="def-proof" markdown>
*Proof.* Let x, $y \in \mathbb{R}$ be arbitrary and fixed.
</div>
We know 0 $\leq (x -y)$2. Multiplying out and rearranging, we get 2xy $\leq$ x2 + y2. Adding 2xy to both sides, we get 4xy $\leq x$2 + 2xy + y2.
Factoring, we get 4xy $\leq (x + y)$2.
Dividing by 4 and putting that into the square, we get xy $\leq$ (x + y


> 🇨🇳 **反证法（Contradiction）** 要证 $P$，假设 $\n\neg P$（AFSOC），推出矛盾。矛盾意味着 $\n\neg P$ 不可能成立，故 $P$ 为真。


)$2 This result is known as the AGM Inequality because it deals with the Arithmetic Mean (AM) and the Geometric Mean (GM) of two real numbers. The Arithmetic Mean of x and y is x+y 2. The Geometric Mean of x and y is \sqrtxy. (Notice that this only applies when$


> 🇨🇳 **例** 证明 $\sqrt{2}$ 无理。反证：设 $\sqrt{2}=p/q$（最简约），则 $2q^2=p^2$，$p$ 偶，$p=2r$，$q^2=2r^2$，$q$ 亦偶——与最简约矛盾！


xy $\geq 0$, i.e. when x and y have the same sign be it positive or negative, or zero.) The AGM Inequality asserts that the AM is always at least as large as the GM. A helpful mnemonic is to read "AGM" as "Arithmetic Mean Greater than Geometric Mean". What we proved above is a slightly more general version, because it applies to all real numbers x and y, and not just those with the same sign. Supposing that xy $\geq 0$, though, one can simply take the square root of both sides and obtain the "usual" statement of the AGM Inequality: \sqrtxy $\leq x$+y 2. Indirect Method (Proof by Contradiction)
Claim: $\f\forall x \in S$. P(x)
Indirect proof strategy: AFSOC that $\exists y \in S such that \negP(y) holds. Find a contradiction.$
Example 4.9.4.
$\sqrt 2 is irrational$: Statement: $\f\forall a$, $b \in \mathbb{Z}$. a b ̸$= \sqrt$


> 🇨🇳 **双条件 $P \Leftrightarrow \mathbb{Q}$ 的证明** 分别证 $P \Rightarrow \mathbb{Q}$ 和 $Q \Rightarrow P$。两条路线独立，各自选择最方便的方法（直接/逆否/反证）。


(Note: $This claim is appealing directly to the definition of the rational numbers Q. It is saying that \sqrt 2 / \in \mathbb{Q}$ because that number has no representation as a ratio of integers.) Implementation:
<div class="def-proof" markdown>
*Proof.* AFSOC $\exists a, b \in \mathbb{Z}$. a
</div>
$b = \sqrt 2. We may assume that a b is given in reduced form, so that a and b have no common factors. (If this were not the case, we could just reduce the fraction and obtain such a form.) Let such a, b \in \mathbb{Z}$ be given. (Note: We discuss this phrase, "let such be given", below in Section
4.9.8. It is meant to not only assert that such an a, $b \in \mathbb{Z}$ exist, but also
$that we want some particular instances of those variables so that we can work with them for the rest of the proof.) This means a b = \sqrt 2, so a2 b2 = 2. Thus, 2b2 = a2, so a2 is even, by definition. Since a2 is even, this tells us a is even.$


> 🇨🇳 **存在性证明 $\exists x.\, P(x)$** 直接法：构造具体 $x$，验证 $P(x)$。反证法：AFSOC 不存在，找矛盾。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **例** 存在两个无理数 $a,b$ 使 $a^b$ 有理。取 $a=b=\sqrt{2}$。若 $\sqrt{2}^{\sqrt{2}}$ 有理，完成。否则 $\sqrt{2}^{\sqrt{2}}$ 无理，令 $c=\sqrt{2}^{\sqrt{2}}, d=\sqrt{2}$，则 $c^d=2$ 有理。


(Note: You should prove this. We will prove it in Section 4.9.6, but you should try to do it on your own now.) Thus, $\exists k \in \mathbb{Z}. a = 2k. Let such a k be given, so a2 = 4k2. Then 2b2 = 4k2, so b2 = 2k2. Thus, b2 is even, by definition. By the same reasoning as above with a2 and a, we deduce here that b is even. This shows both a and b are even so, in fact, they have a common factor of 2. This contradicts our assumption that a and b have no common factors. \times\times\times\times Therefore, the original assumption must be False, so the claim is True.$
### $4.9.3 Proving \veeClaims An$ "$\vee$" claim asserts that at least one of two statements must be True. If it just so happens that one of the two statements is clearly False, then just try to prove the other one is True. This is what the direct method is here; it is straightforward, so we will not provide an example of implementation. Direct Method Strategy:
Claim: $P \veeQ$
Direct proof: Prove that P is True, or else prove that Q is True. This relies on you being able to decide ahead of time which one of the statements (P or $\mathbb{Q}$) is True, of course. If you can do so, then this isn't even really a "strategy". Just implement whatever strategy applies to P (or $\mathbb{Q}$, as the case may be). Indirect Method (Proof by "Otherwise") This method is far more interesting than the direct one. In general, it is helpful when the statements P and Q are actually variable propositions, and for some instances P is True whereas for other instances Q is the True one. In that case, rather than characterize exactly which instances satisfy P and which satisfy $\mathbb{Q}$, we can just say, "Well, if P is True, then our proof is already complete. Thus, all we need to worry about are the cases where P is False; for those cases, we need to show that Q is still True."


> 🇨🇳 **全称证明 $\f\forall x \in S.\, P(x)$** 任取 $x \in S$（"任意且固定的"），推导 $P(x)$。或反证：AFSOC $\exists x \in S$ 使 $\n\neg P(x)$，找矛盾。


Strategy:
Claim: $P \veeQ$
Indirect proof strategy 1: $Suppose that \negP holds. Prove that \mathbb{Q} holds. To reiterate the strategy$: $If P holds, then the claim holds, and in fact we don't care whether \mathbb{Q} holds or not. Otherwise, in the case where P fails, we need to guarantee that \mathbb{Q} holds. Notice that P \veeQ \Leftrightarrow Q\veeP (i.e. the order is irrelevant in a logical disjunction) so we can rewrite our claim as \mathbb{Q} \veeP and rewrite the above strategy as$: $Suppose \negQ holds. Prove that P holds. This is the exact same strategy on the equivalent statement Q\veeP, i.e. with the roles of P and \mathbb{Q} switched.$
Example 4.9.5. When a real number is less than its square:
Statement: Suppose that $x \in \mathbb{R} and x2 \geq x$. We claim that $x \geq1 or x \leq 0$. Implementation:
<div class="def-proof" markdown>
*Proof.* Let $x \in \mathbb{R}$ be arbitrary and fixed, and suppose that x2 $\geq x$.
</div>
If it were the case that $x \leq 0$, we would be done; so, suppose otherwise. That is, suppose x > 0. By assumption, x2 $\geq x$. Since x > 0, we can divide both sides by x. This yields $x \geq 1$. This proves a necessary condition for a real number to be less than (or equal to) its square. Is this condition---namely, $x \geq 1 \veex \leq 0$---also a sufficient condition? Prove it! It's easy, and once you've done so, we will have together proven this biconditional statement: $\f\forall x \in \mathbb{R}. x2 \geq x \Leftrightarrow(x \geq 1 \veex \leq 0$) Indirect Method (Proof by Contradiction) This method is more like the indirect methods considered above, in that we suppose the logical negation is valid and then deduce something absurd. We will illustrate this strategy by applying it to the same claim in the directly previous example.


> 🇨🇳 **证明集合相等 $A = B$** 双包含法：先证 $A \subseteq B$（任取 $x \in A$，推出 $x \in B$），再证 $B \subseteq A$。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **证明 $A \subseteq B$** 任取 $x \in A$（任意且固定），利用 $A$ 的定义和已知条件，推导 $x \in B$。


Strategy:
Claim: $P \veeQ$
Indirect proof strategy 2: $AFSOC that \negP \wedge\negQ holds. Find a contradiction. Implementation$:
<div class="def-proof" markdown>
*Proof.* Let $x \in \mathbb{R}$ be arbitrary and fixed, and suppose that x2 $\geq x$.
</div>
AFSOC that 0 < x and x < 1. Since x > 0, we can multiply both sides of these inequalities by x and preserve the sign. Multiplying x < 1 by x, then, we find that x2 < x. This contradicts our assumption that x2 $\geq x \times\times\times\times Thus, our assumption was invalid, so the claim is True. How does this compare to the previous implementation$? We are proving the exact same claim, but the proofs are slightly different. Which do you think is better, in your opinion? Which do you think was easier to write? Furthermore, could you go back and rewrite the original claim using quantifiers and " =$\Rightarrow$"? After doing that, do you see what these two proofs accomplish? Try it!
### $4.9.4 Proving \wedgeClaims An$ "$\wedge$" claim asserts that both of two statements are True. There's one obvious and direct way to do this: $just prove one statement and then prove the other! We will show you an example implementation of this method because the \wedge statement of our example comes after an \exists c$laim. Thus, there's actually some scratch work to be done to figure out how to define an object that will, indeed, satisfy both of the desired properties. This will be our first illustrative example of how these proof strategies can be combined to prove statements that use both quantifiers and connectives. Direct Method Strategy:
Claim: $P \wedgeQ$
Direct proof strategy:


> 🇨🇳 **证明 $\n\neg P$** 直接列出 $P$ 为假的情形，或用反证法假设 $P$ 再找矛盾。


Prove that P holds. Prove that Q holds.
Example 4.9.6. A smaller number whose square is bigger:
Statement: $\f\forall x \in \mathbb{R}. \exists y \in \mathbb{R}$. {$x \geq y \wedgex2 < y2$ } Scratch work: How does this work? Let's take a specific x, like x = 4. We need to find a smaller real number whose square is bigger than x2 = 16. The key is that we want $y \in \mathbb{R}$, so we can use negative numbers. In this case, picking a negative number with larger magnitude, like y = -5, will work. Let's take a different x, like x = -2. This number is already negative, so just picking any smaller number, like y = -3, will work. The proof we follow below splits into two cases, based on whether x is positive or non-positive. Now we are ready to prove our claim. Implementation: Proof 1. Let $x \in \mathbb{R}$ be arbitrary and fixed. We consider two cases. (1) Suppose $x \leq 0$. Define y = x -1. Notice $y \in \mathbb{R}$. Notice $y \leq$ x. Also, notice that y2 = (x -1)2 = x2 -2x + 1 = x2 -(2x -1) Since $x \leq 0$, we know 2x $\leq 0$ and so 2x -1 $\leq$-1. Thus, x2 -(2x -1) $\geq$ x2 -1 > x2 and therefore, y2 > x2. (2) Now, suppose x > 0. Define y = -x -1. Notice $y \in \mathbb{R}$. Notice y < 0 and x > 0, so $y \leq x$. (In fact, y < x, even.) Also, notice that y2 = (-x -1)2 = x2 + 2x + 1 = x2 + (2x + 1)


> 🇨🇳 **数学写作的常见问题** (1) 省略关键步骤；(2) 假设读者知道"显然"的东西；(3) 循环论证；(4) 符号混用；(5) 变量未引入。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **变量引入** 在证明中第一次使用变量时，必须明确写"令 $x$ 为……"或"设 $x$ 为……"。不能凭空使用一个未说明的变量。


Since x > 0, we know 2x + 1 > 0. Thus, x2 + (2x + 1) > x2 and therefore, y2 > x2. In either case, we found a y with the desired properties, namely $y \in \mathbb{R} and y \leq x$ and x2 < y2. Therefore, the claim is True. Why did we call this "Proof 1"? We split the proof into two cases based on our observations in the scratch work. Specifically, we recognized that we will define y (in terms of x) differently, depending on the sign of x. We claim that it is possible to rewrite this proof in a way that avoids these cases. This is what "Proof 2" will be, and we want you to write it! To reiterate the goal, we want you to rewrite the above proof so that y is defined in terms of x in one general way that works regardless of the sign of x. (Hint: What is -x when x < 0? Is this a function we've seen before?) Indirect Method (Proof by Contradiction) This method is just like the other indirect methods. We just take the logical negation of a claim, assume it holds, and deduce something absurd. This means that the assumption was invalid, so the original statement is the True one. We will leave it to you to try to apply this method to the claim used in the previous example. (Note: You might want to do this after finding the "second proof" we hinted at just above this.) Then, you can compare how the two methods played out and decide which one you prefer, in this case. Strategy:
Claim: $P \wedgeQ$
Indirect proof: $AFSOC that \negP \vee\negQ holds. Consider the first case, where \negP holds. Find a contradiction. Consider the second case, where \negQ holds. Find a contradiction.$
### 4.9.5 Proving =$\Rightarrow \mathbb{C}$laims It might help you to look back at Section 4.5.3, where we introduced the connective " =$\Rightarrow$". Specifically, we want you to recall that P =$\Rightarrow \mathbb{Q}$ means that whenever P holds, Q also necessarily holds. This conditional statement is True


> 🇨🇳 "任意且固定的"** 当你写"任取 $x \in S$"时，$x$ 是任意选择的（不依赖于任何特殊值），但在证明中是固定的（不变化）。这个双重性质至关重要。


in the cases where P itself (the hypothesis) is False. Thus, our proof strategy does not need to consider such cases. All we need to do is suppose that P holds, and deduce that Q also holds. This takes care of the "whenever P holds, so does Q" consideration. Direct Method Strategy:
Claim: P =$\Rightarrow \mathbb{Q}$
Direct proof strategy: Suppose P holds. Prove that Q holds.
Example 4.9.7. Monotonicity of squares:
Statement: $\f\forall y \in \mathbb{R}$. y > 1 =$\Rightarrow y$2 -1 > 0 Implementation:
<div class="def-proof" markdown>
*Proof.* Let $y \in \mathbb{R}$ be arbitrary and fixed.
</div>
Suppose y > 1. Multiplying both sides by y (since y > 0), we obtain y2 > y. Since y > 1, this tells us y2 > y > 1, and so y2 > 1. Subtracting yields the desired conclusion: y2 -1 > 0. We called this "monotonicity of squares" because it states a particular property of real numbers that is monotone. This is a term that is used to indicate a certain inequality is preserved under an operation. In this case, the fact that some number being greater than 1 is preserved by the "squaring operation". That is, we proved that if y > 1, then y2 > 12, as well. Now, this was a pretty easy example to prove, but we wanted to include it to emphase the proof strategy for conditional statements. Let's work with a more difficult example now. (You'll also notice that Exercise 4.11.22 has a similar-looking problem statement. Perhaps you want to work on that one after following this example.)
Example 4.9.8. Working with inequalities:
Statement: We define the following variable propositions: P(x) is " x -3 x + 2 > 1 -1 x " Q(x) is " x + 3 x + 2 < 1 + 1 x "


> 🇨🇳 **草稿 vs 定稿** 草稿（Scratch Work）是你发现证明思路的地方——可以不严格、可以倒推。定稿（Final Proof）必须正向、严格、每步有据。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **草稿示例** 要证"若 $n^2$ 是偶数则 $n$ 是偶数"。草稿：$n$ 奇$\to n^2$ 奇? 设 $n=2k+1$。$n^2=4k^2+4k+1$ 奇数。所以逆否成立。定稿：写逆否证明。


Define S = {$x \in \mathbb{R}$ | x > 0}. We claim that $\f\forall$x \in$ S. P(x) =$\Rightarrow \mathbb{Q} (x)$ Scratch work: We're guessing that a direct method will work here, so let's try to manipulate the inequality stated inside P(x) and make it "look like" the inequality inside Q(x). So we start with that inequality x -3 x + 2 > 1 -1 x and we'll try multiplying both sides by x + 2. Can we do this? Oh right, x > 0 and so x + 2 > 0, as well. Phew! This gives us x -3 > (x + 2) -x + 2 x = x + 2 -1 -2 x = x + 1 -2 x We want to see an x + 3 somewhere, so we'll add/subtract on both sides: x -1 + 2 x > x + 3 Can we divide by x + 2 and make the right fraction? Hmm... Oh wait! We already simplified the fraction x+2 x and moved it to one side. Maybe we shouldn't have simplified it first, so let's try undoing that: x + 3 < x -1 + 2 x = (x + 2) + x + 2 x -4 = (x + 2) ( 1 + 1 x ) -4 Aha, that looks better! We even have some "wiggle room" in the form of the negative 4 there. We know the right-hand side is less than what we wanted it to be, so the result holds. Let's take these algebraic steps we worked on here, reorder them a bit and explain them, and wrap it all together in a formal proof. Implementation:
<div class="def-proof" markdown>
*Proof.* Let $x \in S$ be arbitrary and fixed.
</div>


> 🇨🇳 **定义的展开** 证明中最常用的技巧是展开定义。如 $A \subseteq B$ 展开为 $\f\forall x \in A.\, x \in B$；$f$ 满射展开为 $\f\forall b \in B.\, \exists a \in A.\, f(a)=b$。


Suppose that P(x) holds; that is, suppose x -3 x + 2 > 1 -1 x We will show that the inequality x + 3 x + 2 < 1 + 1 x also holds, necessarily. Since $x \in S$, we know x > 0 and so, certainly, x + 2 > 0, as well. Thus, we can multiply both sides of the known inequality by x + 2, yielding x -3 > (x + 2) ( 1 -1 x ) = x + 2 -x + 2 x Adding 3+ x+2 x to both sides, subtracting 2 from both sides, and rewriting in the reverse direction (for ease of reading), we obtain x + 3 < x -2 + x + 2 x Since x -2 < x + 2, we deduce that x + 3 < x + 2 + x + 2 x and factoring tells us x + 3 < (x + 2) ( 1 + 1 x ) Again, since x + 2 > 0, we can divide both sides by x + 2, obtaining x + 3 x + 2 < 1 + 1 x which was the desired inequality. This shows P(x) =$\Rightarrow \mathbb{Q} (x)$, and since x was arbitrary, we have proven the claim. A key lesson here lies in how we took our scratch work and presented it in a different way in our proof. We cut out the unnecessary simplification and refactoring steps, but we also noted why each step was valid as we performed it. A more seasoned mathematician would likely skip several of these steps and leave it to the reader to verify the algebraic work, but since we are early on in our mathematical careers, we thought it would be prudent to show as many details as possible.


> 🇨🇳 **从目标倒推** 在草稿中，可以从目标出发倒推："要得到 $Q$，我需要什么？"。但在定稿中必须正向写——从假设到结论。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **连接词的使用** 证明中用"因为……所以……"、"设……则……"、"由……可得……"等连接词让逻辑流向清晰。每句话承接上一句。


Contrapositive Method Look back to Section 4.6.1. There, we proved that a conditional statement is logically equivalent to its contrapositive. That is, the conditional statement P =$\Rightarrow \mathbb{Q} necessarily has the same truth value as the statement \negQ = \Rightarrow \negP For this reason, when we try to prove P = \Rightarrow \mathbb{Q} is valid, we can just prove that \negQ = \Rightarrow \negP is valid, instead! Depending on what P and \mathbb{Q} are, maybe this contrapositive is easier to understand, or we can spot a proof more quickly. In fact, the contrapositive strategy is particularly useful when P (or Q, or maybe both) has a$ "not" in it somewhere; by considering its negation, we can work instead with a "positive" assertion, instead of a negation. Strategy:
Claim: P =$\Rightarrow \mathbb{Q}$
Contrapositive proof strategy: $Suppose that \negQ holds. Prove that \negP holds. (Notice that this is the direct proof strategy applied to \negQ = \Rightarrow \negP.)$
Example 4.9.9. Even products of integers:
Statement: Let E(x) be the proposition "x is even". We claim that $\f\forall m, n \in \mathbb{Z}. E(m \cdot n) =\Rightarrow$ {$E(m) \veeE(n)$ } Said another way, whenever the product of two integers is even, this necessarily means that at least one of the integers is even. Implementation:
<div class="def-proof" markdown>
*Proof.* We prove this by contrapositive.
</div>
Let m, $n \in \mathbb{Z} be arbitrary and fixed. Suppose that \negE(m) \wedge\negE(n).$


> 🇨🇳 **QED 和 $\square$** 证明结束用 $\square$ 或"QED"（Quod Erat Demonstrandum，即"这就是要证明的"）标记。也可以写"证毕"。


This means that m is odd and n is odd. This means $\exists k$, ℓ$\in \mathbb{Z}. m = 2k + 1 \wedgen = 2$ℓ+ 1. Let such k, ℓbe given. Then, $m \cdot$ n = (2k + 1)(2ℓ+ 1) = 4kℓ+ 2k + 2ℓ+ 1 = 2(2kℓ+ k + ℓ) + 1 Since 2kℓ+ k + ℓ$\in \mathbb{Z}$, as well, this shows that $m \cdot$n is odd. Thus, \negE(m$\cdot n$) holds, so we have shown that {$\negE(m) \wedge\negE(n)$ } =$\Rightarrow \negE(m \cdot n$) The claim follows by contrapositive. Notice that we pointed out for our reader, at the beginning of the proof, that we would be using the contrapositive method. If we don't do that, the reader might be confused! "$Why are we supposing that \negE(m) holds$? What good is that?!"$, our reader might wonder. By revealing our strategy beforehand, we ensure that our reader will be able to follow along, avoiding unnecessary bewilderment. Indirect Method (Proof By Contradiction) This method depends on the logical negation of conditional statements. Reread Section 4.7 to see where we proved that \neg(P = \Rightarrow Q) \Leftrightarrow (P \wedge\negQ) This proof technique makes use of this equivalence. Strategy$:
Claim: P =$\Rightarrow \mathbb{Q}$
Indirect proof strategy: AFSOC that P holds and suppose that Q fails. Find a contradiction.
Example 4.9.10. A surprising form of the AGM Inequality:
Statement: $\f\forall x \in \mathbb{R}$. x > 0 =$\Rightarrow x$ + 1 $x \geq 2$ Let's jump right into this proof without doing any scratch work, because we think this proof reads fairly straightforwardly. Afterwards, we'll discuss an alternate strategy.


> 🇨🇳 **反证法的模板** "AFSOC（反证假设）……[推导矛盾]。这是矛盾！因此原命题成立。"$\square$"


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **构造性 vs 非构造性存在证明** 构造性证明显式给出满足条件的对象。非构造性证明只保证存在但不给出具体对象。例："$(\exists a,b 无理使 $a^b$ 有理)"是非构造性的（除非能确定 \sqrt{2}^{\sqrt{2}} 是否有理）。


Implementation:
<div class="def-proof" markdown>
*Proof.* Let $x \in \mathbb{R}$ be arbitrary and fixed.
</div>
Suppose x > 0. AFSOC that x + 1 x < 2. Since x > 0, we can multiply through this inequality by x, yielding x2 + 1 < 2x Subtracting and factoring, we obtain (x -1)2 < 0 This is a contradiction, since (x -1)2 $\geq 0. \times\times\times\times Thus, our original assumption is invalid, and the claim follows. Now, you might be wondering about the title for this example. What does this have to do with the AGM Inequality$? (Recall that we proved that fact back in Section 4.9.2.) An astute reader will possibly recognize that not only is this fact here an inequality (like the AGM), but also a couple of steps in this proof are similar to what we did to prove the AGM Inequality. Specifically, to prove the AGM Inequality, we started by using the fact that a particular squared expression is non-negative. Likewise, in this proof, we appealed to the fact that a squared expression should be non-negative. This similarity between the proofs indicates some potential underlying relationship. Indeed, we can actually directly apply the AGM Inequality (in a clever way, mind you!) to prove the above fact in a different way. Think about this for a few minutes and see if you can come up with the following proof, before we show you how it works. What does it mean to apply the AGM Inequality? That result holds for any x and y, but here we have just one x. Can we be crafty about choosing what y should be so that the result here just "falls out" immediately? Try it! Then, read on...
<div class="def-proof" markdown>
*Proof.* Let $x \in \mathbb{R}$ be arbitrary and fixed. Suppose x > 0.
</div>
Define y = 1 x, so $y \in \mathbb{R}$. Then, the AGM inequality applies to x and y (since that fact holds for arbitrary x, $y \in \mathbb{R}$). This tells us that $x \cdot$ 1 $x \leq$ (x + 1 x


> 🇨🇳 **练习** (1) 用直接证明："若 $n$ 是偶数则 $n+2$ 是偶数"。(2) 用逆否证明："若 $n^2$ 是 3 的倍数则 $n$ 是 3 的倍数"。


Simplifying both sides slightly yields 1 $\leq 1$


> 🇨🇳 (3) 用反证法证明：不存在有理数 $r$ 使 $r^2=2$。(4) 用双包含证明 $A \cap B = A$（当 $A \subseteq B$）。


( x + 1 x )2 and then multiplying both sides by 4 yields 4 $\leq ( x + 1 x )$2 Since both sides are non-negative, we can take the square root of both sides and deduce that 2 $\leq x$ + 1 x This proves the claim. There's a lesson here: Always be on the lookout for similarities between arguments and proofs, not just the results that are proven. You might be able to save yourself some work by applying another result that has already been proven! (In this case, we didn't save ourselves too much writing; however, we might have saved ourselves some time, if we hadn't already noticed that the contradiction method would be fruitful. In particular, we might not have thought of the factoring trick that comes up in our first proof.)
### $4.9.6 Proving \Leftrightarrow \mathbb{C}$laims Recall that the "$\Leftrightarrow$" connective is defined entirely in terms of the " =$\Rightarrow$" $connective. That is, asserting that P \Leftrightarrow \mathbb{Q}$ is logically equivalent to asserting two conditional statements: {P =$\Rightarrow \mathbb{Q}$ } $\wedge$ {Q =$\Rightarrow P$ } This gives rise to an obvious strategy: prove one conditional statement, then prove the other! The most common mistake we notice is when someone simply proves one statement or the other, but not both. Always keep that in mind! Direct Method


> 🇨🇳 (5) 写出"若 $x$ 是整数且 $x^2$ 是偶数则 $x$ 是偶数"的完整证明（含草稿和定稿）。(6) 找出以下证明的错误："设 a=b，则 $a^2=ab$，$a^2-b^2=ab-b^2$，$(a+b)(a-b)=b(a-b)$，$a+b=b$，$2b=b$，$2=1$。"


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 (7) 解释为什么"令 $x$ 为满足……的数"在某些情况下不是合法的证明步骤。(8) 写出一个好的证明和一个坏的证明，对比说明。


Strategy:
Claim: $P \Leftrightarrow \mathbb{Q}$
Direct proof strategy: Prove that $P \Rightarrow Q$ (using one of the methods above). Prove that $Q \Rightarrow P$ (using one of the methods above).
Example 4.9.11. Even squares of integers:
Statement: An integer is even if and only if its square is even. Let's rewrite this claim using logical symbolic notation. Let E(z) be the proposition "z is even". Then we claim that $\f\forall z \in \mathbb{Z}$. { $E(z) \Leftrightarrow E (z2)$ } Implementation:
<div class="def-proof" markdown>
*Proof.* Let $z \in \mathbb{Z}$ be arbitrary and fixed.
</div>
( =$\Rightarrow$) First, assume z is even, so $\exists$k \in \mathbb{Z}$. z = 2k. Let such a k be given. Since z = 2k, we can square both sides and obtain z2 = (2k)2 = 4k2 = 2(2k2) Define ℓ= 2k2. Notice that ℓ$\in \mathbb{Z}$ and z2 = 2ℓ This shows that z2 is even. Thus, E(z) =$\Rightarrow E(z2). (\Leftarrow=) Second, we will prove E(z2) = \Rightarrow E (z)$ by contrapositive. Suppose z is odd, so $\exists$m \in \mathbb{Z}$. z = 2m + 1. Let such an m be given. Since z = 2m + 1, we can square both sides and obtain z2 = (2m + 1)2 = 4m2 + 4m + 1 = 2(2m2 + 2m) + 1 Define n = 2m2 + 2m. Notice that $n \in \mathbb{Z} and z2 = 2n + 1. This shows that z2 is odd. Thus, \negE(z) = \Rightarrow \negE(z2)$; by contrapositive, then, E(z2) =$\Rightarrow E (z)$.


> 🇨🇳 **更多证明技巧**
- 分情形：当假设可以分成几类时，对每类分别证明。
- 极端原理：取最大/最小元分析。
- 不变量法：找到一个在操作下保持不变的量。


$Since we have shown both directions, we conclude that E(z) \Leftrightarrow E (z2)$ and since z was arbitrary, this biconditional holds for all integers z. Indirect Method (Proof by Contradiction) Strategy:
Claim: $P \Leftrightarrow \mathbb{Q}$
Indirect proof strategy: $AFSOC that \neg(P = \Rightarrow Q) \vee\neg(Q = \Rightarrow P). Consider the first case, where P \wedge\negQ holds. Find a contradiction. Consider the second case, where \mathbb{Q} \wedge\negP holds. Find a contradiction. Implementing this strategy---and deciding when to do so, even---depends on the actual statements P and Q. In general, a direct method will probably be better (not always), but if you find yourself getting stuck, consider looking at the negations---P \wedge\negQ, and \mathbb{Q} \wedge\negP---and see if that takes you anywhere. It's worth a try! Intermediary Method (TFAE) For lack of a better term, we are going to call this strategy an intermediary method. As you'll see, it's not exactly a direct method, but neither is it an indirect method. In implementing this strategy, we don't have to look at any logical negations, but we also aren't directly linking the statements P and Q. Rather, this method requires us to find some intermediary statement \mathbb{R} and proving two biconditional statements$: $namely, P \Leftrightarrow \mathbb{R} and \mathbb{R} \Leftrightarrow Q. This yields the following chain of conditional statements P \Leftrightarrow \mathbb{Q} \Leftrightarrow \mathbb{R} which tells us that all three statements have the same truth value. In particular, then, P and \mathbb{Q} must always have the same truth value, so we conclude that P \Leftrightarrow \mathbb{Q}$. The acronym TFAE stands for "the following are equivalent". We chose this name because it is a common phrase in mathematics; it is used in theorems that present a list of conditions/properties that all "imply each other". That


> 🇨🇳 **分情形证明** 要证 $P$，将其分成 $P_1, P_2, \ldots, P_n$（覆盖所有可能），分别证明每种情形。如：证 $n^2 + n$ 为偶数，分 $n$ 偶/奇两种情形。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **退化情形** 有时一般证明对某些"平凡"或"退化"的情形不适用。这些情形须单独处理。如：分母为零时公式不成立。


is, some theorems list several properties and assert that all of them are logically equivalent, whence "the following are equivalent". To prove such a theorem, one would implement the above strategies over and over and prove that the statements are, indeed, equivalent. The only difference here is that we have to come up with the intermediary statement to use. (But hey, whoever presented and proved a TFAE-style theorem probably had to come up with all of those statements to begin with, too!) Strategy:
Claim: $P \Leftrightarrow \mathbb{Q}$
Intermediary strategy: $Define a statement R. Prove that P \Leftrightarrow \mathbb{R} (using one of the methods above). Prove that \mathbb{Q} \Leftrightarrow \mathbb{R} (using one of the methods above)$.
### 4.9.7 Disproving Claims We have now discussed (and seen, in many examples) how to prove any kind of mathematical statement. Fantastic! But you might be saying, "Uh oh... What if I want to disprove a statement?" Our answer to that question is short and sweet: there's no difference. To disprove a statement means you want to show its truth value is False. By the definition of logical negation, this means you want to show that the statement's negation has the truth value True. Accordingly, you can just find and write down that logical negation and prove that statement to be True, using any of the strategies we have explored in this section. Voil´a! Just for the sake of illustration let's see an example of this phenomenon in action. Specifically, we'll see an example where we want to disprove a "$\f\forall$" claim, meaning we want to prove a "$\exists$" claim. This is where the notion of a counterexample comes into play. Counterexamples In general, a counterexample is an instance of a statement that disproves a universal quantification. It's an example because it works to prove an "$\exists$" claim, and it's counter in the sense that it shows this specific examples does not have the claimed property.
Example 4.9.12. Look back to Example 4.9.8. In it, we defined the set
S = {$x \in \mathbb{R}$ | x > 0}


> 🇨🇳 **证明审查清单** 审查自己的证明：(1) 假设是否都用上了？(2) 有无循环论证？(3) 变量是否都引入了？(4) 每步是否都有理由？(5) 结论是否明确写出了？


and then defined two variable propositions: P(x) is " x -3 x + 2 > 1 -1 x " Q(x) is " x + 3 x + 2 < 1 + 1 x " Then, we proved that $\f\forall x \in S. P(x) =\Rightarrow \mathbb{Q} (x)$ In this example, we will consider the statement $\f\forall x \in S. Q(x) =\Rightarrow P (x)$ Specifically, we will disprove it. Before we do that, though, play around with the statement on your own. Try to prove it, even though we essentially just told you it's False! Do you find your "proof" breaking down somewhere? Why is that happening? Can you use your observation to help you find a counterexample to the claim? See what you can find, then read on. Scratch work: To start, we need the logical negation of the claim we are disproving: $\exists x \in S. Q(x) \wedge\negP(x) This means we need to find a specific real number x that satisfies three conditions$: (1) the inequality x > 0, (2) the inequality x + 3 x + 2 < 1 + 1 x and (3) the inequality x -3 x + 2 $\leq 1$ -1 x There are a few strategies we could use. Like we mentioned above, we could try to (erroneously, of course) prove that the first inequality does, indeed, imply the second one, and ascertain where this breaks down. Alternatively, we could "try some values" using an "educated guess" method. Knowing that $x \in \mathbb{R}$ and x > 0 indicates, to us anyway, that we might want to try "extreme" values of x. This means either "small" x (i.e. x close to 0) or "large" x (i.e. ever-increasing values of x, that grow larger until we find one that works). It seems easier to first work with some "small" values, so let's try x = 1. We see that (1) holds because 1 > 0, and (2) holds because 4 3 < 2, and (3) holds because -2 3 < 0 $\leq 0$. Cool, that's it!


> 🇨🇳 **WWS（We Want to Show）技巧** 在草稿中每步写"WWS:"后跟当前目标。完成后删除WWS标记，写出正式证明。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **证明写作的文体** (1) 用完整句子，不用片段；(2) 数学符号嵌入句中，仍是句子的一部分；(3) 段落分明，逻辑层次清晰。


<div class="def-proof" markdown>
*Proof.* Here, we will disprove the claim that $\f\forall x \in \mathbb{R}. Q(x) =\Rightarrow P (x)$.
</div>
Consider x = 1. Notice that $x \in \mathbb{R}$ and x > 0. Also, notice that Q(1) holds because 1 + 3 1 + 2 = 4 3 < 2 = 1 + 1


> 🇨🇳 **英文 vs 中文证明** 无论语言，证明的逻辑结构相同。中文证明的连接词："设……"、"由于……"、"故……"、"由此……"、"因此……"、"证毕"。


Also, notice that P(1) fails because 1 -3 1 + 2 = -2 3 ̸> 0 = 1 -1


> 🇨🇳 **术语的精确使用** "且"和"$\wedge$"同义；"或"和"$\vee$"同义（兼或）；"若……则……"和"$\Rightarrow$"同义。在证明中选择最清晰的表达方式。


Thus, we have shown that $\exists x \in S. Q(x) \wedge\negP(x) and this disproves the claim.$
### 4.9.8 Using assumptions in proofs Another important aspect of creating and writing formal proofs is that we are sometimes given assumptions to use. When we state a theorem, it usually has some hypotheses and a conclusion. We get to temporarily add those assumptions to our mathematical toolkit; we can use them to get to the desired conclusion. Similarly, along the way, we might develop some further facts and observations, and we can keep those with us and use them to prove the conclusion, as well. In this short section, we want to point out three observations and issues that may come up while you are using an assumption in a proof. "$P \veeQ$" $means Use Cases If, at some point in a proof, you have assumed or deduced that P \veeQ holds, how can you proceed$? Knowing this disjunction holds means that at least one of the constituent statements---P or Q---holds. Thus, you can consider each of those two cases separately. For example, your proof might have this section in it: $Because P \veeQ, We have two cases. Case 1$: Suppose P holds. Then... Case 2: Suppose Q holds. Then... As long as you can achieve your desired goal in both cases, you can make that deduction. Notice that there is no need to consider the case where both P and Q hold. For one, this might not necessarily even happen. But also, if you only end up using one or the other of the statements to deduce your desired conclusion, then there was no need to temporarily assume both of them.


> 🇨🇳 **证明中的符号选择** 有时用文字更清楚（"对于所有 $x$ 属于 $S$"），有时用符号更简洁（"$\f\forall x \in S$"）。选择取决于读者和上下文。


We have been using cases all along in some of our proofs. Now, we see exactly why they work! We use cases when there is an underlying disjunction of statements. "There exists... " vs. "Let... be given" This is a subtle but important distinction. If you write down a claim like $\exists x \in S$. P(x) in the middle of a proof, what have you asserted? Technically speaking, you have really only stated that the line above is a True statement; you have asserted that there does exist some $x \in$ S with the property P(x). But, if you move and start referring to x afterwards... this is not valid! Nowhere in the assertion of existence did you introduce a particular instance of that claim. It might be the case that several such x elements exist. Do you want to talk about all of them? Or just a particular one? Don't leave it up to the reader of your proof to intuit exactly what you're doing! If you know, or have assumed, some existence statement (like the line above) and you want to actually introduce a variable that satisfies that existence claim, use the following wonderful phrase: "Let such an x be given." This signals to the reader that not only are you saying such an x exists, but you are also bringing it into play in your proof. You want the letter x, for the rest of your written argument, to represent an element with that property. Thereafter, you get to refer to that object x by name. If you assert the existence of several variables and want to introduce them, just use a similar phrase with a slightly different verb. For instance, you might write something like this:... and so we deduce that $\exists x$, y, $z \in \mathbb{Z}$ such that P(x, y, z) holds. Let such x, y, z be given. Observe that... "P =$\Rightarrow \mathbb{Q}$" vs. "P, therefore Q" This distinction hinges on an idea similar to the previous example we just mentioned. Specifically, there is a difference between writing a statement to assert its validity and writing a statement to show the reader you are making a conclusion from it. In the last example, this was the distinction between saying something exists versus introducing such an object. Here, the distinction lies between asserting a conditional statement---like P =$\Rightarrow Q$---to say that this conditional relationship exists versus using this statement to deduce that Q holds. Technically speaking, just writing "P =$\Rightarrow Q$" on your paper does not assert that Q is valid. You must make it very clear to your reader that you also know P and are using the conditional statement to deduce $\mathbb{Q}$.


> 🇨🇳 **常见逻辑错误** (1) 肯定后件：$P \Rightarrow \mathbb{Q}$ 和 $Q$ 成立不能推出 $P$。(2) 否定前件：$P \Rightarrow \mathbb{Q}$ 和 $\n\neg P$ 不能推出 $\neg \mathbb{Q}$。(3) 混淆必要与充分条件。


4.9. WRITING PROOFS: STRATEGIES AND EXAMPLES


> 🇨🇳 **反例的重要性** 当你说"总是成立"时，只需一个反例就推翻。构造反例是一项重要的数学能力。


Look back at our discussion in Section 4.5.6. There, we described this important distinction, and referred to the method of "Modus ponens". As we mentioned, if you want to actually deduce $\mathbb{Q}$, you should write something like: P =$\Rightarrow \mathbb{Q}$ because... Also, P holds because... Therefore, Q holds.
### 4.9.9 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What is the Direct Method for an $\exists c$laim? What are the important steps in showing an object exists? (2) What is the Direct Method for an =$\Rightarrow c$laim? How do we prove a =$\Rightarrow$ claim by contradiction? How are these methods different? $(3) How do we prove a \Leftrightarrow c$laim? (4) What is the AGM Inequality? Where does the acronym come from? (5) To which type of claim does the Contrapositive Strategy apply? Why does it work? (6) What is a counterexample? (7) What is the difference between saying "$\exists$a \in$ A. P(a)" and saying "$\exists$a \in$ A. P(a) so let such an a be given"? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Prove that $\f\forall$x \in \mathbb{R}$. x2 $\neq$ 1 =$\Rightarrow x$\neq$ 1. (2) Prove that $\f\forall$n \in \mathbb{N}. n \geq5 =\Rightarrow$2n2 > (n + 1)2 (3) Express the following claim in logical symbols, and then prove it.


> 🇨🇳 **元证明意识** 证明你自己：当你写完一个证明，问自己"如果我是第一次读这个证明，我能看懂吗？"如果不确定，找人读一遍。


$There exists an even natural number that can be written as the sum of two primes in two different ways. (4) Prove that every natural number is either less than \sqrt 10 or bigger than 3. That is, prove \f\forall n \in \mathbb{N}. n < \sqrt 10 \veen > 3 (5) Let A, B, C, D be sets. Prove that, if A \cup B \subseteq \mathbb{C} \cup D and \mathbb{C} \subseteq A and A \cap B = \emptyset, then B \subseteq D$. (6) Define P = {$y \in \mathbb{R}$ | y > 0}. Prove that $\f\forall$ε $\in P$. $\f\forall x$, $y \in \mathbb{R}$. $\exists$δ $\in P$. |x -y| < δ =$\Rightarrow$|(3x -4) -(3y -4)| < ε Can you also prove the following claim? How is it different than the one above? $\f\forall$ε $\in P$. $\exists$δ $\in P$. $\f\forall x$, $y \in \mathbb{R}$. |x -y| < δ =$\Rightarrow$|(3x -4) -(3y -4)| < ε (7) Let E(x) be the proposition "x is even". Prove that $\f\forall a$, $b \in \mathbb{Z}. E(a) \wedgeE(b) \Leftrightarrow E(a + b) \wedgeE(a \cdot b) (8) Look back at the proof that \sqrt 2 is irrational. Modify it to provide a proof that \sqrt 3 is irrational, as well. Try to do the same and prove that \sqrt 6 is irrational. Challenge$: $Can you prove that \sqrtp is irrational for every prime number p$? (9) Prove that there are infinitely many rational numbers. Hint: Do this by contradiction. (Suppose there are finitely many... )
## 4.10 Summary We now have a huge toolkit of mathematical proof strategies! We developed the necessary terminology and symbols to properly express mathematical claims. Then, we used the concepts underlying those to develop proof strategies and saw many examples of how they are used. One of the more difficult aspects of writing a proof is figuring out the proof in the first place! This involves not only figuring out whether a claim is True or False, but also ultimately deciding which proof strategy to implement. We realize this is challenging because, well, it is... Furthermore, it's difficult to characterize exactly when to use certain strategies. We can offer guidelines and suggestions (and have done so as much as possible) but, in the long run, the best way to get better at implementing proof strategies and deciding which ones to use is to just do it. Approach an exercise problem. Try to play with the statement and see why it is True (or False, as the case may be). Try using a


> 🇨🇳 **评分者角度** 想象证明将被评分：每一步都必须可验证、无可歧义地解释。省略的步骤 = 失分。


proof strategy on it. Did it work? How? If it didn't, why and where did it break down? Can you use those observations to decide on a different approach to the problem? Ultimately, can you write down a good, formal argument? Working through these steps on as many problems as possible truly is the best practice. There is no substitute for simply doing mathematics.
## 4.11 Chapter Exercises These problems incorporate all of the material covered in this chapter, as well as any previous material we've seen, and possibly some assumed mathematical knowledge. We don't expect you to work through all of these, of course, but the more you work on, the more you will learn! Remember that you can't truly learn mathematics without doing mathematics. Get your hands dirty working on a problem. Read a few statements and walk around thinking about them. Try to write a proof and show it to a friend, and see if they're convinced. Keep practicing your ability to take your thoughts and write them out in a clear, precise, and logical way. Write a proof and then edit it, to make it better. Most of all, just keep doing mathematics! Short-answer problems, that only require an explanation or stated answer without a rigorous proof, have been marked with a }. Particularly challenging problems have been marked with a $\star$. Problem 4.11.1. } Consider the universal context to be U = $\mathbb{Z}$. Let P(x) be the proposition "1 $\leq$x \leq 3$". Let Q(x) be the proposition "$\exists k \in \mathbb{Z}$. x = 2k". Let R(x) be the proposition "x2 = 4". Let S(x) be the proposition "x = 1". For each of the following statements, write out an English sentence to describe what the statement means, then write the logical negation, and then decide which claim is True or False, and why. (a) $\f\forall x \in \mathbb{Z}. P(x) =\Rightarrow \mathbb{Q}(x) (b) \exists x \in \mathbb{Z}. R(x) \wedgeP(x) (c) \f\forall x \in \mathbb{Z}. R(x) =\Rightarrow P(x) (d) \f\forall x \in \mathbb{Z}. \exists y \in \mathbb{Z}$. x ̸$= y \wedgeP(x) \wedgeR(y) (e) \f\forall x \in \mathbb{Z}. \exists y \in \mathbb{Z}. (S(x) \veeQ(x)) \wedgeP(y) \wedge\negQ(y) (f) \exists x \in \mathbb{Z}. S(x) \Leftrightarrow P(x) \wedge\negQ(x) (g) \exists x \in \mathbb{Z}. S(x) \Leftrightarrow \negP(x) \wedgeQ(x)$


> 🇨🇳 **证明的长度** 好证明是充分详细的，但不冗长。目标：让目标读者每步都能理解，但不需要解释"为什么 $1+1=2$"。


Problem 4.11.2. For each of the following claims, define some sets and variable propositions to express the claim in concise symbolic, logical notation. Then, write the logical negation, as well. Note which one is True or False. (a) Every odd natural number is prime. (b) There is a real number that is strictly greater than any integer squared. (c) Some real number between -1 and 1 has the property that it is equal to the cube of some different real number between -1 and 1. (d) The union of the sets of multiples of primes is the set of natural numbers itself. Problem 4.11.3. Consider the following defined sets and questions about those sets. For each question, if your answer is No, provide an example to demonstrate this. (a) Let S = {1, 2, 3, 4} and T = {3, 4, 5, 6, 7, 8}. Is it true that $\f\forall s \in S. \exists t \in T$. s + t = 7? (b) Let S = {2, 3, 4, 5, 6} and T = {3, 4, 5, 6}. Is it true that $\f\forall s \in S. \exists t \in T$. s + t = 7? (c) Let S = $\mathbb{N}$ and T = $\mathbb{Z}$. Is it true that $\f\forall s \in S. \exists t \in T$. s + t = 7? (d) Let S = $\mathbb{Z}$ and T = $\mathbb{N}$. Is it true that $\f\forall s \in S. \exists t \in T$. s + t = 7? Problem 4.11.4. Consider the following defined sets and questions about those sets. For each question, if your answer is No, provide an example to demonstrate this. (a) Let S = {1, 2, 3}, T = {6, 7, 8, 9}, and V = {7, 8, 9, 10}. Is it true that $\exists s \in S. \f\forall t \in T. \exists v \in V$. s + t = v? (b) Let S = {1, 2, 3}, T = {4, 5, 6, 7}, and V = {5, 6, 7, 9, 10, 11}. Is it true that $\exists s \in S. \f\forall t \in T. \exists v \in V$. s + t = v? (c) Let S = T = V = $\mathbb{N}$. Is it true that $\exists s \in S. \f\forall t \in T. \exists v \in V$. s + t = v? (d) Let S = $\mathbb{N}$, T = $\mathbb{Z}$, and V = $\mathbb{N}$. Is it true that $\exists s \in S. \f\forall t \in T. \exists v \in V$. s + t = v?


> 🇨🇳 **总结** 证明写作是数学的核心技能。好的证明结构清晰、逻辑严格、文体流畅、无跳跃。坚持写正规证明，你的数学写作能力会快速提升。


Problem 4.11.5. Prove or disprove the following claim rigorously: $\exists x \in \mathbb{R}. \f\forall y \in \mathbb{R}$. x2 -y2 $\geq 0$ Problem 4.11.6. Prove or disprove the following claim rigorously: $\f\forall x, y \in \mathbb{Z}. \exists z \in \mathbb{N} \cup \{0\}$. ((x -$y) = z) \vee((y$ -x) = z) Problem 4.11.7. Prove that there are no integral solutions (i.e. x, $y \in \mathbb{Z}$) to the equation x2 -y2 = 14. Problem 4.11.8. Problem 4.11.9. Problem 4.11.10. Problem 4.11.11. Problem 4.11.12. Use logical equivalences to prove that (a) ($A \cup$ B) $\cap A$ = B -A (b) $A \cap (B -C)$ = ($A \cap$ B) -($A \cap \mathbb{C}$) Problem 4.11.13. Define the sets A = ( (x, y) $\in \mathbb{R} \times \mathbb{R}$ | x y + y $x \geq 2$ ) and B = {(x, y) $\in \mathbb{R} \times \mathbb{R}$ | $(x > 0 \wedgey > 0) \vee(x < 0 \wedgey < 0)} Is it the case that A \subseteq B$? If so, prove it. Otherwise, exhibit a counterexample. Is it the case that $B \subseteq A$? If so, prove it. Otherwise, exhibit a counterexample. Problem 4.11.14. Let P = {$y \in \mathbb{R}$ | y > 0} be the set of positive real numbers. Prove the following claim: $\f\forall$ε $\in P$. $\exists$δ $\in P$. $\f\forall$x \in \mathbb{R}$. |x| < δ =$\Rightarrow$|x2| < ε Problem 4.11.15. What is wrong with the folllowing "proof" of the claim that P($C \cup$ D) = P(C) $\cup P (D)$? Let $X \in$ P($C \cup$ D) be arbitrary and fixed. This means $X \subseteq \mathbb{C}$\cup D$. So, $X \subseteq \mathbb{C} \veeX \subseteq D. Then, X \in P(C) \veeX \in P(D). Thus, X \in P(C) \cup P (D)$. Therefore, P($C \cup$ D) = P(C) $\cup P (D)$.


> 🇨🇳 (9) 用分情形证明 $|xy| = |x| \cdot |y|$（$x,y \in \mathbb{R}$）。(10) 用反证法证明素数有无穷多个。


Problem 4.11.16. Suppose $x \in \mathbb{Z}$ and x2 is a multiple of 8. Prove that x is even. Is the converse of this statement True? If so, prove it; otherwise, exhibit a counterexample. Problem 4.11.17. Define the proposition E(z) to be "z is even. Prove that $\f\forall$z \in \mathbb{Z}. E(z) \Leftrightarrow E(z3) Problem 4.11.18. Use the result of Problem 4.11.17 to prove that 3\sqrt 2 is irrational. Problem 4.11.19. Let P = {y \in \mathbb{R}$ | y > 0}. Prove that \ x$\in P ( $y \in \mathbb{R}$ | 1 -1 x < y < 2 )$ = {$z \in \mathbb{R}$ | 1 < z < 2} Problem 4.11.20. Let A, B, $C \subseteq$ U be sets. Define S = {($A \cap$ B) $\cup \mathbb{C}$ } -A and T = C -($A \cup$ B) Is $S \subseteq$ T? If so, prove it; otherwise, find a counterexample. Is $T \subseteq$ S? If so, prove it; otherwise, find a counterexample. Problem 4.11.21. For each $x \in \mathbb{R}$, define the set Sx = {$y \in \mathbb{R}$ | -$x \leq y$\leq x$} Also, define the set P = {$y \in \mathbb{R}$ | y > 0} Prove each of the following claims. \ x$\in P$ Sx = {0} \ x$\in \mathbb{N} Sx = {y \in \mathbb{R}$ | -1 $\leq y \leq 1$} Problem 4.11.22. Let P(x) be the variable proposition " x2 + 4 x2 + 1 < 1 + 1 x " and let Q(x) be the variable proposition " x2 -4 x2 + 1 > 1 -1 x "


> 🇨🇳 (11) 构造性存在证明：找两个无理数 $a,b$ 使 $a^b$ 为有理数。(12) 非构造性存在证明：证明存在无理数 $a,b$ 使 $a^b$ 有理——但不指出具体是哪些。


Also, let S = {$x \in \mathbb{R}$ | x > 0} be the set of positive real numbers. For each of the following statements determine whether it isTrue (in which case, provide a proof) or False (in which case, provide a counterexample and demonstrate why it is valid). (a) $\f\forall$x \in$ S. P(x) =$\Rightarrow \mathbb{Q}(x) (b) \f\forall x \in S. Q(x) =\Rightarrow P(x) Problem 4.11.23. Let A and B be any two sets. Prove that A \times B = B \times A \Leftrightarrow (A = B \veeA = \emptyset \veeB = \emptyset ) (Don't forget that this is an if and only if claim!) Problem 4.11.24. Let A, B, C, D be any sets. Prove that (A \times B) \cap (C \times D) = \emptyset \Leftrightarrow$ {$A \times B = \emptyset \veeC \times D = \emptyset$ } Problem 4.11.25. Let B be any set. Let I be an index set, and let Ai be a set for every $i \in$ I. Prove the following set equalities: (a) \ i$\in I$ Ai ! -B = \ i$\in I (Ai -B) (b)$ [ i$\in I$ Ai ! -B = [ i$\in I (Ai -B) (c)$ \ i$\in I Ai ! \times B = \ i \in I (Ai \times B) (d) [ i \in I Ai ! \times B = [ i \in I (Ai \times B) (e) B$ - \ i$\in I$ Ai ! = [ i$\in I (B -Ai) (f) B$ - [ i$\in I$ Ai ! = \ i$\in I (B -Ai)$ Problem 4.11.26. In this problem, you will prove that the rational numbers Q are dense. Namely, we want you to consider the following proposition:
Proposition. Strictly between any two distinct rational numbers lies another ra-
tional number. Restate this claim using logical symbols, and then prove it.


> 🇨🇳 (13) 找出以下证明中的逻辑漏洞："$P \Rightarrow \mathbb{Q}$ 为真，$Q$ 为真，因此 $P$ 为真。"(14) 解释为什么"取 x 使 $P(x)$ 成立"有时是循环论证。


Problem 4.11.27. This problem is meant to introduce the concept of uniqueness. We say an object with a certain property is unique if it has the desired property but no other object has that property. That is, we would say x is the unique element of S with property P(x) if and only if $\exists x \in S. P(x) \wedge( \f\forall y \in S. y \neq x =\Rightarrow \negP(y)) Notice that this is logically equivalent to \exists x \in S. P(x) \wedge( \f\forall y \in S$ -${x}. \negP(y)) Also, we can write the contrapositive instead$: $\exists x \in S. P(x) \wedge( \f\forall y \in S. P(y) =\Rightarrow x$ = y) Use this to restate the following claim in logical symbols. Then, prove it.
Claim: There is a unique natural root of the equation n3 -n -6 = 0.
Problem 4.11.28. This problem provides a definition of a new set operation (defined in terms of others) and asks you to prove several set containments and equalities, using this operation.
Definition: Let A, B be sets.
The symmetric difference of A and B is denoted by A∆B and is defined as A∆B = (A -B) $\cup (B -A)$ Now, let A, B, C be any sets. Prove the following: (a) A∆A = $\emptyset (b) A$∆B = B∆A (c) A∆$\emptyset$= $\emptyset (d)$A \subseteq$ B =$\Rightarrow A$∆B = B -A (e) A∆(B∆C) = (A∆B)∆C (f) A∆B = A∆B (supposing A, $B \subseteq$ U) (g) (A∆B) $\cap \mathbb{C} = (A \cap \mathbb{C}$)∆($B \cap \mathbb{C}$) = (A∆B) -$C Problem 4.11.29. In this problem, you will prove a useful result about primality testing. Much of modern cryptography is based on factoring large composite numbers into its prime factors. The following proposition says that we only need to check up until \sqrtp for factors of p.$
Proposition. Let p be a natural number that is at least 2. If none of the natural
$numbers between 2 and \sqrtp (inclusive) divide p, then p is prime.$


> 🇨🇳 (15) 写出"对任意 $n \in \mathbb{N}$，$n^3 - n$ 是 6 的倍数"的归纳证明。(16) 将以下草稿转化为一版正式证明。


Recall: The formal definition of "|" is Given a, $b \in \mathbb{Z}$, we write a | b if and only if $\exists$k \in \mathbb{Z}$. b = ak. Restate the above proposition using logical symbols. Then, prove it. (Hint: Think about the contrapositive of the cliam... ) Problem 4.11.30. Let A, B be any sets. Prove the following claim: $A \times B = B \times A \Leftrightarrow (A = B \veeA = \emptyset \veeB = \emptyset$) Problem 4.11.31. Let S, T be sets whose elements are also sets. For each of the following statements, either prove the statement holds in general, or provide a counterexample: (a) [ X$\in S \cup T X \subseteq [ Y \in S Y ! \cup [ Z\in T \mathbb{Z} ! (b) [ X\in S \cup T X \supseteq [ Y \in S Y ! \cup [ Z\in T \mathbb{Z} ! (c) \ X\in S \cup T X \subseteq \ Y \in S Y ! \cap \ Z\in T \mathbb{Z} ! (d) \ X\in S \cup T X \supseteq \ Y \in S Y ! \cap \ Z\in T $\mathbb{Z}$$ !
## 4.12 Lookahead Now that we have all of these mathematical tools---and we've put them to good use, honing our skills with lots of exercsises---we are more equipped to step out into the mathematical wilderness. We will be exploring various branches of mathematics, learning some fundamental concepts and notation, and applying our proof strategies to new and wonderful results. Before we do that, though, we need to take care of one lingering issue: we want to formalize induction. Before, we "waved our hands" a bit about what exactly induction is and how it works. We gave you the "Domino Analogy" and used it on some example. But now we have the requisite terminology and knowledge to properly describe mathematical induction and study its various forms. It might be a good idea to flip through Chapter 2 again to remind yourself of some of the illustrative examples where we used an inductive argument. Do you remember the Domino Analogy? Can you anticipate how we might formalize the Principle of Mathematical Induction? Can you explain that theorem to a friend and convince them? Try it! Then, read on!


> 🇨🇳 （此段补充说明与证明写作的进阶技巧相关。）


