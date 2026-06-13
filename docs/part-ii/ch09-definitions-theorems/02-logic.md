---
title: A.2 Logic
---

# A.2 Logic

APPENDIX A. DEFINITIONS AND THEOREMS A.2.3 Connectives Suppose P and Q are mathematical statements. They may be composed of variable propositions with quantifiers in front.

• To say "P and Q" we write $P \wedge Q$. This has the truth value True if and only if both $P$ and $Q$ are True.
• To say "P or Q" we write $P \vee Q$. This has the truth value True if and only if at least one of the statements, $P$ and $Q$, are true. (This is the inclusive or, so it's allowable that both $P$ and $Q$ are true.)
• To say "If P then Q" we write $P \Rightarrow Q$. This has the truth value True if and only if, whenever $P$ holds, $Q$ also holds. Notice that $P \Rightarrow Q$ is, itself, a logical statement. It has a truth value, True or False. It makes no claim about the truth values of the constituent statements, $P$ and $Q$. We call this a conditional statement; we say $P$ is the hypothesis and $Q$ is the conclusion. Notice that $P \Rightarrow Q$ is True when $P$ is False. This is because it is an "If... then... " statement; it makes no claim about the situations where $P$ is False, so we cannot declare the conditional statement to be False so it must be True (by the Law of the Excluded Middle).
• An equivalent way to write $P \Rightarrow Q$ is $\neg P \vee Q$.
• The contrapositive of a conditional statement $P \Rightarrow Q$ is $\neg Q \Rightarrow \neg P$. It is guaranteed to have the same truth value as $P \Rightarrow Q$. That is, $(P \Rightarrow Q) \Leftrightarrow (\neg Q \Rightarrow \neg P)$.
• The converse of a conditional statement $P \Rightarrow Q$ is $Q \Rightarrow P$.

It is not guaranteed to have the same truth value as $P \Rightarrow Q$. There are statements $P, Q$ such that $P \Rightarrow Q$ holds and the converse holds, and there are statements $P, Q$ such that $P \Rightarrow Q$ holds and the converse fails.

• To say "P and Q are logically equivalent" we write $P \Leftrightarrow Q$ and we read this aloud as "P if and only if Q". We can also write this as $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$. This means that $P$ and $Q$ have the same truth value, whatever that happens to be.

A.2.4 Logical Negation

• We use "$\neg$" to indicate the logical negation of a statement.
• The statement $\neg P$ has the opposite truth value from the statement $P$.
• Negating a $\forall$ claim: $\neg \{\forall x \in S.\, P(x)\} \Leftrightarrow \exists x \in S.\, \neg P(x)$
• Negating a $\exists$ claim: $\neg \{\exists x \in S.\, P(x)\} \Leftrightarrow \forall x \in S.\, \neg P(x)$
• Negating a $\vee$ claim: $\neg \{P \vee Q\} \Leftrightarrow \neg P \wedge \neg Q$. This is one of DeMorgan's Laws for Logic.
• Negating a $\wedge$ claim: $\neg \{P \wedge Q\} \Leftrightarrow \neg P \vee \neg Q$. This is one of DeMorgan's Laws for Logic.
• Negating a $\Rightarrow$ claim: $\neg \{P \Rightarrow Q\} \Leftrightarrow \neg (\neg P \vee Q) \Leftrightarrow P \wedge \neg Q$
• Negating a $\Leftrightarrow$ claim: $\neg \{P \Leftrightarrow Q\} \Leftrightarrow \neg [(P \Rightarrow Q) \wedge (Q \Rightarrow P)] \Leftrightarrow (P \wedge \neg Q) \vee (Q \wedge \neg P)$
• Using these facts, we can negate any mathematical statement, because a statement is just composed of quantifiers and connectives and variable propositions. We can read the statement left to right and negate each part.


> 🇨🇳 **A.2.3 联结词（Connectives）** 设 $P$、$Q$ 为数学命题。
>
> - "P 且 Q"写作 $P \wedge Q$，当且仅当 $P$、$Q$ 同为真时为真。
> - "P 或 Q"写作 $P \vee Q$，当且仅当至少一个为真时为真（兼或）。
> - "若 P 则 Q"写作 $P \Rightarrow Q$，当 $P$ 成立时 $Q$ 也成立。$P$ 为假设，$Q$ 为结论。注意 $P$ 为假时条件语句为真。
> - 等价写法：$P \Rightarrow Q$ 即 $\neg P \vee Q$。
> - **逆否命题（Contrapositive）**：$P \Rightarrow Q$ 的逆否为 $\neg Q \Rightarrow \neg P$，与原命题真值相同。
> - **逆命题（Converse）**：$P \Rightarrow Q$ 的逆为 $Q \Rightarrow P$，真值不一定相同。


> 🇨🇳 - "P 与 Q 逻辑等价"写作 $P \Leftrightarrow Q$（"P 当且仅当 Q"），即 $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$。
>
> **A.2.4 逻辑否定（Logical Negation）**
> - $\neg P$ 与 $P$ 真值相反。
> - 否定 $\forall$：$\neg(\forall x \in S.\, P(x)) \Leftrightarrow \exists x \in S.\, \neg P(x)$。
> - 否定 $\exists$：$\neg(\exists x \in S.\, P(x)) \Leftrightarrow \forall x \in S.\, \neg P(x)$。
> - 否定 $\vee$：$\neg(P \vee Q) \Leftrightarrow \neg P \wedge \neg Q$（德摩根律）。
> - 否定 $\wedge$：$\neg(P \wedge Q) \Leftrightarrow \neg P \vee \neg Q$（德摩根律）。
> - 否定 $\Rightarrow$：$\neg(P \Rightarrow Q) \Leftrightarrow P \wedge \neg Q$。
> - 否定 $\Leftrightarrow$：$\neg(P \Leftrightarrow Q) \Leftrightarrow (P \wedge \neg Q) \vee (Q \wedge \neg P)$。
> - 据此可对任何命题逐步否定。


APPENDIX A. DEFINITIONS AND THEOREMS A.2.5 Proof Strategies We use the phrase AFSOC to mean "assume for sake of contradiction".

• Proving a $\exists$ claim: $\exists x \in S.\, P(x)$
Direct proof: Define a specific example, $y = \ldots$. Prove that $y \in S$. Prove that $P(y)$ holds true.
Indirect proof: AFSOC that for every $y \in S$, $\neg P(y)$ holds. Find a contradiction.

• Proving a $\forall$ claim: $\forall x \in S.\, P(x)$
Direct proof: Let $y \in S$ be arbitrary and fixed. Prove that $P(y)$ holds true.
Indirect proof: AFSOC that $\exists y \in S$ such that $\neg P(y)$ holds. Find a contradiction.

• Proving a $\vee$ claim: $P \vee Q$
Direct proof: Prove that $P$ holds true, or else prove that $Q$ holds true.
Indirect proof 1: Suppose that $\neg P$ holds. Prove that $Q$ holds.
Indirect proof 2: AFSOC that $\neg P \wedge \neg Q$ holds. Find a contradiction.

• Proving a $\wedge$ claim: $P \wedge Q$
Direct proof: Prove that $P$ holds. Prove that $Q$ holds.
Indirect proof: AFSOC that $\neg P \vee \neg Q$ holds. Consider the first case, where $\neg P$ holds. Find a contradiction. Consider the second case, where $\neg Q$ holds. Find a contradiction.

• Proving a $\Rightarrow$ claim: $P \Rightarrow Q$
Direct proof: Suppose $P$ holds. Prove that $Q$ holds.
Contrapositive proof: Suppose that $\neg Q$ holds. Prove that $\neg P$ holds.
Indirect proof: AFSOC that $P$ holds and suppose that $Q$ fails. Find a contradiction.

• Proving a $\Leftrightarrow$ claim: $P \Leftrightarrow Q$
Direct proof: Prove that $P \Rightarrow Q$ (using one of the methods above). Prove that $Q \Rightarrow P$ (using one of the methods above).
Indirect proof: AFSOC that $\neg(P \Rightarrow Q) \vee \neg(Q \Rightarrow P)$. Consider the first case, where $P \wedge \neg Q$ holds. Find a contradiction. Consider the second case, where $Q \wedge \neg P$ holds. Find a contradiction.


> 🇨🇳 **A.2.5 证明策略（Proof Strategies）** AFSOC 表示"反证假设"。
>
> - 证 $\exists$：定义具体例子，证其属于 $S$ 且满足 $P$；或反证。
> - 证 $\forall$：任取 $y \in S$ 为任意且固定的，证 $P(y)$ 成立；或反证。
> - 证 $\vee$：证 $P$ 或证 $Q$；或设 $\neg P$ 证 $Q$；或反证 $\neg P \wedge \neg Q$。
> - 证 $\wedge$：分别证 $P$、$Q$；或反证 $\neg P \vee \neg Q$（分情形导出矛盾）。
> - 证 $\Rightarrow$：设 $P$ 成立证 $Q$；或用逆否（设 $\neg Q$ 证 $\neg P$）；或反证。
> - 证 $\Leftrightarrow$：分别证 $P \Rightarrow Q$ 和 $Q \Rightarrow P$；或反证。
>
> **A.3 归纳法（Induction）**
> **A.3.1 数学归纳法原理** 定理：设 $P(n)$ 是对所有 $n \in \mathbb{N}$ 定义的变量命题。若 $P(1)$ 成立且 $\forall k \in \mathbb{N}.\, P(k) \Rightarrow P(k+1)$，则 $\forall n \in \mathbb{N}.\, P(n)$。归纳证明步骤：基例（证 $P(1)$）— 归纳假设（设 $P(k)$）— 归纳步（证 $P(k+1)$）— 结论。
>
> **A.3.2 强归纳法原理** 定理：若 $P(1)$ 成立且 $\forall k \in \mathbb{N}.\, [P(1) \wedge \cdots \wedge P(k)] \Rightarrow P(k+1)$，则 $\forall n \in \mathbb{N}.\, P(n)$。强归纳可能需要多个基例，归纳假设设 $P(1) \wedge \cdots \wedge P(k)$ 全部成立。


APPENDIX A. DEFINITIONS AND THEOREMS A.3 Induction

A.3.1 Principle of Specific Mathematical Induction

• Theorem: Suppose that $P(n)$ is a variable proposition that is defined for all $n \in \mathbb{N}$. Suppose that $P(1)$ holds. Suppose that $\forall k \in \mathbb{N}.\, P(k) \Rightarrow P(k+1)$. Then $\forall n \in \mathbb{N}.\, P(n)$.

• Proving a claim by induction: Suppose we have a variable proposition $P(n)$ that is defined for all $n \in \mathbb{N}$, and we want to prove $P(n)$ holds for every $n \in \mathbb{N}$.
Base Case: Prove that $P(1)$ holds.
Induction Hypothesis: Suppose that $k$ is an arbitrary and fixed natural number, and suppose that $P(k)$ holds.
Induction Step: Prove that $P(k+1)$ holds.
Conclusion: By induction, $\forall n \in \mathbb{N}.\, P(n)$.

A.3.2 Principle of Strong Mathematical Induction

• Theorem: Suppose that $P(n)$ is a variable proposition that is defined for all $n \in \mathbb{N}$. Suppose that $P(1)$ holds. Suppose that $\forall k \in \mathbb{N}.\, [P(1) \wedge P(2) \wedge \cdots \wedge P(k)] \Rightarrow P(k+1)$. Then $\forall n \in \mathbb{N}.\, P(n)$.

• Proving a claim by strong induction: Suppose we have a variable proposition $P(n)$ that is defined for all $n \in \mathbb{N}$, and we want to prove $P(n)$ holds for every $n \in \mathbb{N}$.
Base Case(s): Prove that $P(1)$ holds. (Depending on what happens in the Induction Step, you might need more than one Base Case.)
Induction Hypothesis: Suppose that $k$ is an arbitrary and fixed natural number that satisfies some inequality ($k \geq \ldots$, depending on what happens in the Induction Step), and suppose that $P(1) \wedge \cdots \wedge P(k)$ holds.
Induction Step: Prove that $P(k+1)$ holds.
Conclusion: By induction, $\forall n \in \mathbb{N}.\, P(n)$.


> 🇨🇳 （归纳法内容已合并于上方翻译）

