---
title: Strong Induction
---

# Strong Induction

holds for every $n \in \mathbb{N}$, we could, in the inductive step, appeal to the immediately preceding case and invoke the inductive hypothesis, like so: n+1 X k=1 k = (n + 1) + n X k=1 k = n + 1 + n(n + 1)


> 🇨🇳 强归纳法（Strong Induction）常规归纳法的归纳假设只假设 $P(k)$ 成立。但有时归纳步需要利用多个前置命题。强归纳法的归纳假设假设 $P(1) \wedge P(2) \wedge \cdots \wedge P(k)$ 全部成立。


= (n + 1)(n + 2)


> 🇨🇳 **强归纳法原理** 定理：设 $P(n)$ 是对所有 $n \in \mathbb{N}$ 定义的变量命题。若 $P(1)$ 成立且 $\forall k \in \mathbb{N}.\, [P(1) \wedge P(2) \wedge \cdots \wedge P(k)] \Rightarrow P(k+1)$，则 $\forall n \in \mathbb{N}.\, P(n)$。


Of course, we didn't refer to these parts of our argument as the "IH" or "IS" $yet, but that is what we were doing. When we considered the Domino Tilings example, though, we found that we needed to refer to two previous instances of the fact. Specifically, to find the number of tilings of a 2\timesn board, we needed to know not only how many tilings of a 2 \times (n$ -$1) board there were, but also how many tilings of a 2 \times (n$ -2) board there were. This is inherently different! What is it about an inductive argument that lets us do this? How does this follow the "domino analogy" we described? Or the "Mojo the Monkey" analogy? Does it, at all? When we considered the game of Takeaway, we had even "more" different situation, didn't we? In constructing Player 2's winning strategy, we noticed that Player 2 should just mimic whatever Player 1 does, but on the other pile. That is, if Player 1 removes, say, 3 stones from the left pile, then Player 2 should remove 3 stones from the right pile, to guarantee a win. This held true no matter how many stones Player 1 removed. In that sense, we required the fact that Player 2 had a winning strategy on any size of piles up to n (inclusive) to guarantee that Player 2 had a winning strategy on piles of size n + 1. This required a lot of assumptions to go into our inductive hypothesis. How do we know that we can do that?
### 5.4.2 Theorem Statement and Proof
Our goal now is to state and prove a modified version of the PMI that reflects these kinds of examples, the Domino Tilings and the Takeaway game. They represent inductive arguments where we might have to (1) refer to more than one previous instance to prove the subsequent instance of the claim, or (2) refer to some unknown previous instance to prove the subsequent instance. Both of those argument styles will be covered by this theorem. Let's see that statement first and then discuss what it means.
<div class="def-theorem" markdown>
**Theorem 5.4.1 (Principle of Strong Mathematical Induction (Strong PMI)).**
</div>
Let P(n) be a variable proposition. Suppose that (1) P(1) holds True, and (2) $\forall k \in \mathbb{N}$. {$\forall i \in$[k]. P(i) } =$\Rightarrow P (k + 1)$ holds True Then $\forall$n \in \mathbb{N}$. P(n) holds True. Whoa, what does this say? We're giving you some extra work by presenting it here in logical notation before discussing it in a more wordy way, but we think you can handle it. Try to parse these two conditions, although surely condition


> 🇨🇳 **与常规归纳法的关系** 常规归纳法是强归纳法的特例——当归纳步只用到 $P(k)$ 时，强归纳假设退化为常规归纳假设。能用常规归纳法的证明也能用强归纳法，但反过来不行。


(2) is the tough one. What does it say? Read it out loud, write it down in an English sentence, think about it. Compare it to the regular old PMI we stated and proved in the previous section. Why would we call this one "strong"? How are these theorems different? Are their hypotheses different? What about their conclusions? Take a few minutes' break from reading to ponder these questions. Then, read on... Okay, let's explain this theorem. Notice that the only difference between The Strong PMI (Theorem 5.4.1) and The Regular PMI (Theorem 5.2.2) lies in condition (2), which governs what we do in the induction hypothesis part of a proof. The setup (that we have a variable proposition) and condition (1) (the base case) and the conclusion (that P(n) holds for every $n \in \mathbb{N}$) are identical. Let's compare condition (2), now. The Regular PMI requires that P(k) is sufficient to allow us to deduce P(k+ 1), for every $k \in \mathbb{N}$. If we can achieve that (the domino toppling affect), and we have a Base Case, then P(n) holds for every $n \in \mathbb{N}$. This is what we do in the IH and IS of an induction proof: suppose P(k) holds and use it to deduce P(k + 1) necessarily holds, too. Let's rewrite condition (2) of The Strong PMI to see what it says: $\forall$k \in \mathbb{N}$. {$P(1) \wedgeP(2) \wedgeP(3) \wedge \cdot \cdot \cdot \wedgeP(k)$ } =$\Rightarrow P (k + 1)$ That is, Strong PMI requires that all of the previous instances of the proposition (P(1) and P(2) and P(3) and... and all the way until P(k)) are together sufficient to allow us to deduce P(k + 1). This theorem seems to say, "Hey, don't worry about using just P(k) to get to P(k +1); you can actually use all of the statements P(1) through P(k) to get there! The desired conclusion---that $\forall n \in \mathbb{N}$. P(n)---will still follow!" Isn't that nice? There are three aspects of this theorem to discuss now: (1) why this method is actually valid, (2) when we would need to use it, and (3) how to use it. We can address aspect (3) quickly right now, before showing you some examples later on. The only difference between a Strong Induction proof and a Regular Induction proof will be in the IH and the IS. When using Strong Induction, in the IH we will suppose P(1) and P(2) and... and P(k) all hold, then use them to deduce P(k + 1) necessarily holds, too. In the IS, we will just have to be careful about pointing out which of the assumptions of the IH we use. To address aspect (2)---when to use Strong Induction---we will show you several examples. In working through these examples, we will point out precisely why a regular induction proof would fail. By seeing several instances of this, we hope to develop some intuition for when to recognize these situations in the future. That is, we will learn to realize what kinds of claims require a strong IH in their proof. Let's address aspect (1) right now, because it is the most pressing. Before we race on and start using a proof technique, we want to make sure it's actually mathematically valid! If you're like us, you're wondering, "How is this theorem


> 🇨🇳 **何时需要强归纳？** 判断标准：分析归纳步真正使用了哪些前置信息。如果只用到 $P(k)$，用常规归纳；如果需要 $P(j)$ 对某个 $j < k$，用强归纳。


even True? It says that we need to know a whole lot more about how the instances of P(n) relate to each other. Why should we be allowed to make so many assumptions in the IH and be able to use them later?" A Modified Domino Analogy and a Heuristic Diagram We'll start with a modification of the Domino Analogy from Chapter 2, and then show you a heuristic diagram for how Strong Induction works, to satisfy our intuitions. After that, we'll formally prove the theorem above. Think about how Regular Induction followed the Domino Analogy. We only needed to know that Domino n will fall into Domino n + 1 to guarantee the whole line will fall. Here, with Strong Induction, we actually need to know that all of the dominoes up to (and including) Domino n have fallen and knocked into Domino n + 1, toppling it, to guarantee the whole line will fall. It's as if the dominoes are getting "heavier and heavier" as the line goes on, so we need a whole bunch of them falling into each other to generate enough momentum to topple the next, much heavier one. Let's put this another way. Think about the chain of implications connecting all of our propositions. Our BC will tell us P(1) is True. Great. This will imply that P(2) holds. (Use n = 1 in condition (2) of SPMI.) Knowing these two will together imply that P(3) holds. (Use n = 2 in condition (2) of SPMI.) Knowing all three of those will collectively imply P(4) holds. And so and so on: T by BC z }| { { P(1) } Use IS z }| { =$\Rightarrow$ Get T z }| { { P(2) } | ${z } Know P (1)\wedgeP (2) = \Rightarrow$ | {z } Use IS { P(3) } | {z } Get T | ${z } Know P (1)\wedgeP (2)\wedgeP (3) = \Rightarrow$ { P(4) } =$\Rightarrow$ { P(5) } =$\Rightarrow$ In some sense, this points to why the method works, overall. We prove P(1) holds, just like with Regular Induction. But then, to "get to" the truth of P(2), that first step---P(1) =$\Rightarrow P (2)$---is the same in Strong Induction as it is in Regular Induction. (Use n = 1 in condition (2) of SPMI and PMI. It's the same condition.) From there on out, when we use Strong Induction, we're just making use of the fact that all of the previous instances of the proposition have held True; we might as well use them to keep traveling through and deducing the truths of the next propositions! Regular Induction doesn't bother with this. It says, "Okay, great, all of the previous instances have held. We don't actually need them to prove the next instance; we only need the immediately preceding one." Here's one more slightly different way of interpreting this "chain of implications". This will actually directly hint at the proof we will see very shortly, as well! Pretend we're moving along with a Strong Induction process, and we've proven everything up until P(n); that is, P(1) and P(2) and... and P(n) are all


> 🇨🇳 **例：用强归纳证明每个 $n \geq 2$ 有素因子分解** 设 $P(n)$ 为"$n \geq 2$ 有素因子"。基例 $P(2)$：2 本身是素数。归纳步：设对所有 $2 \leq j \leq k$ 有 $P(j)$。对 $k+1$：(a) 若 $k+1$ 是素数，则 $P(k+1)$ 成立；(b) 否则 $k+1 = ab$（$a,b \geq 2$），由归纳假设 $a$ 有素因子 $p$，$p|a|k+1$。


True. Let's just package those instances all together and label them as one big proposition, Q(n). (Thinking of it another way, we'll take all of those dominoes and bind them together into one giant domino.) The next step is to use that one instance to prove the next one, which sounds a lot more like Regular Induction, which we're more comfortable with for now. This is essentially what we will do in the proof! We'll reformulate the whole process of Strong Induction to phrase it as a Regular Induction process. Formal Proof As the previous paragraph hinted, the proof below will make use of PMI. (In fact, we will even use the proof template for a proof by induction that we saw in the previous section!) In this sense, we are really proving this statement: PMI =$\Rightarrow S$PMI Let's do it!
<div class="def-proof" markdown>
*Proof.* Let P(n) be a variable proposition. Suppose that
</div>
(1) P(1) holds True, and (2) $\forall k \in \mathbb{N}$. {$\forall i \in$[k]. P(i) } =$\Rightarrow P (k + 1)$ holds True Our goal is to prove that $\forall$n \in \mathbb{N}. P(n). Define the proposition Q(n) by setting Q(n) \Leftrightarrow \forall i \in$[n]. P(i) (That is, Q(n) says "All of the propositions P(1) and P(2) and... and P(n) are True.) We will now prove $\forall n \in \mathbb{N}$. Q(n) by induction on n. BC: $By the definition of the proposition Q(1), we have Q(1) \Leftrightarrow P (1)$. Condition (1) tells us that P(1) holds, and therefore Q(1) holds, as well. IH: Let $k \in \mathbb{N}$ be arbitrary and fixed. Suppose Q(k) holds. IS: $By the definition of $\mathbb{Q}$(k), we have Q(k) \Leftrightarrow \forall i \in$[k]. P(i) (Again, that is, P(1) and... and P(k) all hold.) By condition (2), we can deduce that P(k + 1) holds. This means that $\forall i \in$[k + 1]. P(i). (That is, we already knew P(1) and... and P(k) all hold, and we just found that P(k + 1) holds, too.) By the definition of Q(k +1), this means that Q(k +1) holds. This was the goal of the IS.


> 🇨🇳 **多个基例的必要性** 有时强归纳步需要用到 $P(k)$ 和 $P(k-1)$，因此需要验证两个基例 $P(1)$ 和 $P(2)$ 来"启动"归纳链。基例数量取决于归纳步回溯多远。


Accordingly, by PMI, we deduce that $\forall n \in \mathbb{N}$. Q(n) holds. By the definition of $\mathbb{Q}$(n), we have $\forall n \in \mathbb{N}. Q(n) =\Rightarrow P (n) (That is, every instance Q(n)$ says that all of the instances P(1) and... and P(n) hold and so, at the very least, we know that P(n) itself holds.) Since we just proved that Q(n) holds for every $n \in \mathbb{N}$, we may deduce that P(n) therefore also holds for every $n \in \mathbb{N}, i.e. \forall n \in \mathbb{N}$. P(n) This was the goal, so our proof is complete. Proof Summary and a Striking Equivalence Look at what we've accomplished: we used Regular Induction to prove that Strong Induction is a valid technique. This tells us the PMI Theorem implies the SPMI Theorem, as we mentioned above: PMI =$\Rightarrow S$PMI But certainly, this works the other way around, too! If we had already somehow proven (by other means) that Strong Induction is valid, then Regular Induction would have to be valid, as well. That is, we also know that SPMI =$\Rightarrow P$MI Said another way: if we already had Strong Induction in hand as a valid proof technique, then whenever we would want to use Regular Induction to prove something, we would just use Strong Induction to accomplish our goal. In that sense, Strong Induction "subsumes" Regular Induction as a technique. Together, these two observations tell us something remarkable about the theorems PMI and SPMI as they are in the world of mathematical truths. We have now shown that they are equivalent: $PMI \Leftrightarrow S$PMI Each theorem implies the other one. Now, for the practical purpose of applying these techniques to prove facts, this equivalence might not seem to matter too much, but it really does tell us something helpful. It says this: Whenever we have to prove something by induction, we might as well always use Strong Induction. Think about this for a few minutes. Read over the theorem statements and their proofs and consider it. Have it in mind as we work through the coming examples.


> 🇨🇳 **例：邮票问题** 用 4 分和 7 分邮票凑邮资。$18=4+7+7$，$19=4\times4+7$，$20=4\times5$，$21=7\times3$。归纳步：对 $k+1 \geq 22$，$(k+1)-4 \geq 18$，由强归纳假设 $(k+1)-4$ 可凑出，加一枚 4 分邮票。


Once you've read the proof template below, go back to the examples from the previous section on Regular Induction and apply Strong Induction to them. Does it work? Does it seem different? Try it! We'll discuss this Regular/Strong comparison again after working out the examples below, so let's move on and see how to use Strong Induction.
### 5.4.3 Using Strong Induction: Proof Template This template is very similar to the one for Regular Induction, since the only difference between the two theorems (and, accordingly, their respective techniques when applied) occurs in the IH. Template for a "Proof by Strong Induction" Goal: Prove that $\forall n \in \mathbb{N}$. P(n)
<div class="def-proof" markdown>
*Proof.* Let P(n) be the proposition " ". We will prove $\forall n \in \mathbb{N}$. P(n) by induction on n. Base Case: Observe that P(1) holds because. Induction Hypothesis: Let $k \in \mathbb{N}$ be arbitrary and fixed. Suppose $\forall$i \in$[k]. P(k) holds. Induction Step: Deduce that P(k + 1) also holds. By PMI, it follows that $\forall$n \in \mathbb{N}$. P(n). All of the same important observations and recommendations that we made about Regular Induction apply here, as well. We have to be sure to define a proposition, point out that we're using (strong) induction on a specific variable, label our steps, and make a conclusion. One new recommendation we want to make is a refinement of an old one. When using Regular Induction, we had to be sure to cite the IH whenever we used it. Here, we will have many instances of the proposition in our IH, so we will actually have to be careful and cite which instance(s) of the proposition we use! You'll see this come into play in the examples below.
</div>
### 5.4.4 Examples
We will see three different "kinds" of examples here. Even though they all use the same template for Strong Induction that we just introduced, they differ in how the refer to the hypotheses in the IH. This first one is a direct application of the method, so let's work through it first, and then discuss how the other examples might be different.
Example 5.4.2. A formula for a recursively-defined sequence:


> 🇨🇳 为什么需要 4 个基例？因为归纳步用 $(k+1)-4$，必须保证 $P(k+1)$ 依赖的 $P(k-3)$ 从基例开始连续成立。18-21 四个基例恰好覆盖到归纳步能接续的最小值。


Claim: Let the sequence sn be defined by
s0 = 1 and $\forall n \in \mathbb{N}$. sn = 1 + n-1 X i=0 si Find and prove a closed formula for sn for every $n \in \mathbb{N} \cup \{0\}$.
<div class="def-proof" markdown>
*Proof.* Let P(n) be "sn = 2n". We prove $\forall n \in \mathbb{N} \cup \{0\}$. P(n) by induction on
</div>
n. BC: When n = 0, observe that s0 = 1 and 20 = 1, so s0 = 20. Thus, P(0) holds. IH: Let $k \in \mathbb{N} \cup {0} be arbitrary and fixed. Suppose P(0) \wedgeP(1) \wedge \cdot \cdot \cdot \wedgeP(k) holds. IS$: Observe that sk+1 = 1 + k X i=0 si
Definition of sk+1
= 1 + k X i=0 2i Using IHs: $P(0) \wedge \cdot \cdot \cdot \wedgeP(k) = 1 +$ {2k+1 -1 } Standard result (see Exercise 2.7.1) = 2k+1 Thus, P(k + 1) holds. Therefore, $\forall n \in \mathbb{N} \cup \{0\}$. P(n) holds, by induction. Notice that this example required us to use all of the instances in the IH. Isn't that striking? Certainly, we needed strong induction here. Without knowing all of the previous instances held, we wouldn't have any hope of deducing the next one! What distinguishes this from the next example is that here we knew exactly which instance(s) of the IH we used (namely, all of them). In the next example, we will invoke the IH, but we won't be able to say exactly which instance we use. You'll see what we mean!
Example 5.4.3. To start we need to introduce you to (or perhaps remind you
of) a couple of ideas about prime numbers and the natural numbers. Primes: A prime number is an element of the set P = {$n \in \mathbb{N}$ | $n > 1 \wedge(n = ab) = \Rightarrow (a = 1 \veea = n)} That is, the only divisors of a prime number are 1 and itself. Prime Factorization$: Given $x \in \mathbb{N}$, a prime factorization of x is a product of primes that equals x, with repeats allowed.


> 🇨🇳 **强度对比** 常规归纳法证明 $\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$ 时，归纳步只需 $P(k)$。但证明"每个 $n \geq 2$ 有素因子"时必须用强归纳，因为 k+1 的因子可能小于 $k$。


For example, a prime factorization of 6 is 2 $\cdot$ 3, and a prime factorization of 252 is 2 $\cdot$ 2 $\cdot$ 3 $\cdot$ 3 $\cdot$ 7. We will now state and prove the fact that every natural number has a prime factorization.
Claim: Let F(n) be the proposition "n has a prime factorization". Then we
claim that $\forall n \in \mathbb{N}$ -{1}. F(n).
<div class="def-proof" markdown>
*Proof.* We will prove $\forall n \in \mathbb{N}$ -{1}. F(n) by induction on n.
</div>
BC: Notice that F(2) holds because 2 = 2 is a prime factorization of 2. IH: Let $k \in \mathbb{N}$ -{1} be arbitrary and fixed. Suppose $\forall$i \in$[k] -${1}. F(i) holds. (That is, suppose F(2) \wedgeF(3) \wedge \cdot \cdot \cdot \wedgeF(k).) IS$: Consider k + 1. We want to find a prime factorization of k + 1. There are two cases, based on whether k + 1, itself, is prime: Case 1: If k + 1 itself is prime, then k + 1 is a prime factorization of k + 1, thereby showing F(k + 1) holds. Case 2: If k + 1 is not prime, there exist a, $b \in \mathbb{N}$ -{1} such that k + 1 = $a \cdot$ b. Since a, $b \neq$ 1, it must be that 1 < a < k + 1 and 1 < b < k + 1. That is, 2 $\leq$a \leq$ k and 2 $\leq$b \leq$ k. Thus, F(a) and F(b) hold, by the IH. Accordingly, there is a prime factorization of a and a prime factorization of b. Multiplying these two factorizations together yields a prime factorization of $a \cdot$ b = k + 1. This shows F(k + 1) holds. In either case, we deduce that F(k + 1) holds. By induction, we conclude that $\forall$n \in \mathbb{N}$ -{1}. F(n). Notice that we invoked the IH in this proof but we didn't know which "previous instance" of the claim we invoked. We were only able to appeal to some a and b with a certain property. This is different than the previous example, but it also clearly indicates we needed strong induction here. Nothing about a prime factorization for k could possibly help us find one for k + 1. Think about it: does knowing 14 = 2 $\cdot$ 7 help us figure out that 15 = 3 $\cdot$ 5? Does knowing 16 = 24 help us figure out that 17 is prime? This result we just proved is an important one: it says that every natural number has a prime factorization. Now, it also happens to be true that these prime factorizations are unique, in the sense that every natural number has exactly one prime factorization. Of course, this only works "up to the ordering of the factors". By this, we mean that 6 = 2 $\cdot$ 3 and 6 = 3 $\cdot$ 2 are really the same factorization of 6. Likewise, 252 = 2 $\cdot$ 2 $\cdot$ 3 $\cdot$ 3 $\cdot$ 7 is the only factorization of 252; it is no different than writing 252 = 7 $\cdot$ 32codt22. Nothing about proof above addresses this fact, though! We only used the existence of some a and b to deduce something. Who's to say that there weren't some other c and d with the same properties that we could have used? Think


> 🇨🇳 **证明模板** 强归纳证明步骤：(1) 明确 $P(n)$；(2) 验证所需基例 $P(1), P(2), \ldots, P(m)$；(3) 归纳假设：设对 $1 \leq j \leq k$ 有 $P(j)$；(4) 从假设推导 $P(k+1)$；(5) 宣布结论。


about this. Can you prove that prime factorizations are unique? What method will you use? The next example will adress the Fibonacci Sequence, a sequence of numbers we have used before. Specifically, we will state and prove a closed form for the sequence, which is typically defined recursively. By a "closed form" we mean a straight-forward expression that can be evaluated by "plugging and chugging". To find, for example, f100, with the recursive definition of the sequence, we would have to compute all of the numbers in the sequence up until that point: we need f99 and f98, which means we need f97, which means... With the closed form, though, we will be able to just "plug in n" and evaluate directly to find f100.
Example 5.4.4. A closed form for the Fibonacci Sequence:
Claim: Define the standard Fibonacci Sequence by
f0 = 0 and f1 = 1 and $\forall n \in \mathbb{N}$ -{1}. fn = fn-1 + fn-2 Define ϕ$= 1+ \sqrt$


> 🇨🇳 **例：邮资问题推广** 用 $a$ 分和 $b$ 分邮票（$\gcd(a,b)=1$），可以凑出所有 $n \geq (a-1)(b-1)$ 分邮资。证明需要强归纳和 $(a-1)(b-1)$ 以下的多个基例。


. Then the following equality holds for every $n \in \mathbb{N} \cup \{0\}$: fn =


> 🇨🇳 **强归纳的常见错误** (1) 基例不够——归纳链断裂。(2) 归纳假设写错——应写"对所有 $j \leq k$"而非只写"假设 $P(k)$"。(3) 归纳步中假设了不该假设的东西。


{ϕn -(1 -ϕ)n }
<div class="def-proof" markdown>
*Proof.* Let fn and ϕ be defined as in the claim above.
</div>
We will first prove the following equation: 1 + ϕ = ϕ2 ($\star$1) Observe that ϕ2 =


> 🇨🇳 **强归纳与递归定义** 递归定义与强归纳天然适配：$F_n = F_{n-1} + F_{n-2}$ 的定义需要两个前置值，恰好对应强归纳的两个基例。


$!2 = 1 + 2 \sqrt 5 + 5$


> 🇨🇳 **练习** (1) 用强归纳法证明：$F_n < 2^n$（$F_n$ 为 Fibonacci 数）。(2) 用强归纳法证明：$n \geq 12$ 可写成 $4a+5b$（$a,b \geq 0$）。


= 1 + ϕ Then, we can use this to prove the following equation: 2 -ϕ = (1 -ϕ)2 ($\star$2) Observe that (1 -ϕ)2 = 1 -2ϕ + ϕ2 = 1 -2ϕ + (ϕ + 1) = 2 -ϕ where we have used fact ($\star$1). We will make use of both of these facts below. Let P(n) be the proposition " fn =


> 🇨🇳 (3) 用强归纳法证明"每个 $n \geq 2$ 有素因子"。(4) 解释为什么强归纳法中等号可能需要多个基例。


{ϕn -(1 -ϕ)n } "


> 🇨🇳 (5) 数列 $a_1=1, a_2=3, a_n=a_{n-1}+2a_{n-2}$（$n\geq3$）。用强归纳法证明 $a_n = 2^n - (-1)^n$。


We will prove that $\forall n \in \mathbb{N} \cup \{0\}$. P(n) by induction on n. BC: Observe that f0 = 0 and


> 🇨🇳 (6) 证明：用 5 分和 9 分邮票可以凑出所有 $n \geq 32$ 分。(7) 对比常规归纳与强归纳：各自给出一个必须用该方法的例子。


{ϕ0 -(1 -ϕ)0 } =


> 🇨🇳 **补充：归纳法的选用** 判断方法的简单规则：若递推关系只依赖前一项 $\to$ 常规归纳；若依赖前多项 \to 强归纳；若涉及"存在最小反例" $\to$ 良序原理。


$\sqrt 5(1$ -1) = 0 Thus, P(0) holds. IH: Let $k \in \mathbb{N} \cup \{0\}$ be arbitrary and fixed. Suppose $\forall i \in[k] \cup \{0\}$. P(i) holds. IS: Our goal now is to deduce that P(k + 1) holds. Case 1: Suppose k = 0. Then we can directly observe that f1 = 1 and


> 🇨🇳 **补充：强归纳与良序** 强归纳与良序原理逻辑等价——但强归纳的证明往往更构造性（给出具体步骤），而良序证明更非构造性（只需矛盾）。


{ϕ1 -(1 -ϕ)1 } =


> 🇨🇳 **补充：Fibonacci 与黄金比例** $F_n/F_{n-1}$ 收敛于黄金比例 $\phi = (1+\sqrt{5})/2$。这可以用强归纳法证明 $F_n = (\phi^n - (1-\phi)^n)/\sqrt{5}$（Binet 公式）。


{$1 + \sqrt 5$ -1 } =


> 🇨🇳 **补充：强归纳的"宽度"** 常规归纳假设"宽度为 1"（只看 $P(k)$），强归纳假设"宽度为 $k$"（看 $P(1)$ 到 $P(k)$）。更大的宽度给归纳步更多信息可用。


} = 1 This shows that P(1) holds. Case 2: Suppose $k \geq 1$. Then, observe that fk+1 = fk + fk-1 Defn, since $k \geq 1$ =


> 🇨🇳 **补充：整数的唯一分解** 算术基本定理（每个 $n \geq 2$ 唯一分解为素数之积）可用强归纳证明存在性，唯一性则另需论证。


{ϕk -(1 -ϕ)k } $+ 1 \sqrt$


> 🇨🇳 **补充：归纳步中的回溯** 强归纳步中，实际使用的可能只是 $P(j)$ 对某些特定 $j < k+1$。关键是确保这些 $j$ 已被基例或之前的归纳涵盖。


{ϕk-1 -(1 -ϕ)k-1 } IHs P(k), P(k -1) =


> 🇨🇳 **补充：强归纳与动态规划** 强归纳的思想与动态规划完全一致——利用所有已解决的子问题（前 $k$ 个）来解决第 $k+1$ 个问题。


{ϕk + ϕk-1 -(1 -ϕ)k -(1 -ϕ)k-1 } Simplify =


> 🇨🇳 **补充：错误示范** 错误证明："假设 $P(k)$ 成立。由某种关系得到 $P(k-1)$ 和 $P(k)$ 推出 $P(k+1)$。"——问题在于只假设了 $P(k)$，但用到了 $P(k-1)$，该用强归纳！


{ϕk-1(ϕ + 1) -(1 -ϕ)k-1((1 -ϕ) + 1) }
Factor
=


> 🇨🇳 **补充：归纳法的结构** 所有归纳法都有两部分——基例（验证起点）和归纳步（保证传播）。强归纳的区别仅在于"传播"所需的信息量更大。


{ϕk-1 $\cdot$ ϕ2 -(1 -ϕ)k-1(2 -ϕ) } By ($\star$1) =


> 🇨🇳 **补充：强归纳的历史** 强归纳法的形式化比常规归纳法稍晚。它在数论中特别重要——如整数的素因子分解和丢番图方程。


{ϕk+1 -(1 -ϕ)k-1(1 -ϕ)2 } By ($\star$2) =


> 🇨🇳 **补充：数学教育中的强归纳** 强归纳法的教学难点在于"看起来与常规归纳太像"——学生容易忘记把归纳假设写成"对所有 $j \leq k$"。


{ϕk+1 -(1 -ϕ)k+1 } Thus, P(k + 1) holds. By induction, we conclude that $\forall n \in \mathbb{N} \cup \{0\}$. P(n). A Discussion about Multiple Base Cases Notice, in the previous example, that we had to establish two cases in the IS. Because the Fibonacci Sequence is defined recursively so that each term depends on two previous terms, we could not use the truth of P(0) alone to deduce P(1). We had to show P(1) held separately. (Go back and try it. You'll find yourself trying to refer to f-1, an undefined term!) After that, we can use the truth of P(0) and P(1) to deduce P(2), then we can use P(1) and P(2) to deduce P(3)... That is to say, we really needed to throw in one extra base case before the whole "and so on" of induction kicked in.


> 🇨🇳 **补充：归纳法的等价性** 四种表述等价：(1) 常规 PMI；(2) 强 PMI；(3) 良序原理；(4) 无限下降法（$P(n+1) \Rightarrow P(n)$ 导出矛盾）。选择最方便的用。


There are two legitimate ways to handle this, and we just showed you one. The alternative would be to recognize that this situation will happen ahead of time, and instead present two base cases in the BC step. For the sake of illustration, let's show you how the relevant parts of the proof would be different, had we done that instead:
<div class="def-proof" markdown>
*Proof.*...... BC: Observe that f0 = 0 and
</div>


> 🇨🇳 **补充：多个基例的直觉** 想象多米诺骨牌：常规归纳是"每块推倒下一块"——一个基例启动。强归纳是"每块需要前几块的支持"——需要多个基例启动多条传导链。


{ϕ0 -(1 -ϕ)0 } =


> 🇨🇳 **补充：递归与归纳** 每个递归定义都对应一个归纳证明，反之亦然。递归给出结构，归纳验证性质。这是计算数学与理论数学的桥梁。


$\sqrt 5(1$ -1) = 0 Thus, P(0) holds. Also, observe that f1 = 1 and


> 🇨🇳 **补充：课堂提示** 当归纳步用了 $P(k-1)$ 时，你**必须**验证 P(1) **和** P(2)。当用了 $P(k), P(k-1), P(k-2)$ 时，**必须**验证三个基例。基例数 = 归纳步回溯深度 + 1。


{ϕ1 -(1 -ϕ)1 } =


> 🇨🇳 **补充：强归纳的适用范围** 强归纳适用于：(1) 涉及因子分解的数论命题；(2) 递推依赖于多个前项的数列；(3) 图论中的路径和连通性命题；(4) 博弈论中的策略分析。


{$1 + \sqrt 5$ -1 } =


> 🇨🇳 **补充：书中的强归纳法之旅** 第 2-3 章建立了直觉，第 4 章提供了逻辑工具，第 5 章建立了严格框架。第 5.4 节是归纳法理论的顶峰——后续将应用而非扩展这些工具。


} = 1 Thus, P(1) holds. IH: Let $k \in \mathbb{N}$ be arbitrary and fixed. Suppose $\forall$i \in$[k] $\cup${0}. P(i) holds. IS: Our goal now is to deduce that P(k + 1) holds. Observe that...... We moved the special P(1) case into the BC section. Because of this, we had to also modify the quantification that happens in the IH and IS. We no longer want to use k = 0 in the ensuing argument, so in the IH we just take an arbitrary k that satisfies $k \geq 1$. However, we have already seen P(0) holds, so we can still include it in our IH. That's it! The two proofs are fundamentally identical. The only differences lie in their presentation and, even then, the differences are small. We will leave it to you to decide which style you prefer (if either) to be used in your proofs. We want to remind you, though, that these differences are small but they're also subtle and sometimes easy to forget! If you find yourself including many base cases, be sure to start your IS by seeking to prove a value above those base case values! You don't want to be inadvertently asserting some logical implication that doesn't actually hold. (For example, look back at the second proof above. If we had allowed k = 0 as a case in the IS, we would have inadvertenly been referring to f-1, which does not exist. Thus, we would have been saying something incorrect, and the proof would be flawed, albeit not totally doomed.)


> 🇨🇳 **补充：强归纳法 vs 数学归纳法** "强"不意味着更强——两种方法逻辑上等价。"强"只是指归纳假设更强（假设更多信息），使某些证明更方便。


This kind of distinction typically occurs when you are asked to prove some representation formula for a recursively-defined sequence, where each term in the sequence is defined by several previous terms. There are several examples of this phenomenon in the exercises, both for this section and at the end of the chapter. Keep this in mind as you work on them! Needing n = 2 A fairly common phenomenon that occurs in strong induction proofs is the necessity of proving both the n = 1 and n = 2 cases before jumping into the IS. In particular, this might happen when you have to prove some inequality or equality holds for n variables, where the n = 1 case is trivial and the n = 2 case is the interesting one that requires more work, and the rest of the induction follows by invoking the n = 2 case. Note that this requires taking $k \geq 2$ in the IS, of course. Let's see an example to show you what we mean. Lucky for us, we have already proven the n = 2 case for this claim; it's actually one of DeMorgan's Laws for Sets!
Example 5.4.5. A Generalized DeMorgan's Law for Sets:
Claim: Let U be a universal set. For every $i \in \mathbb{N}, let Ai \subseteq U$ be a set.
Then, the following equality holds for every $n \in \mathbb{N}$: n [ i=1 Ai = n \ i=1 Ai Written another way, this claim says that, for every $n \in \mathbb{N}$, we have A1 $\cup$ A2 $\cup$\cdot$\cdot$\cdot$\cup$ An = A1 $\cap$ A2 $\cap$\cdot$\cdot$\cdot$\cap A$n
<div class="def-proof" markdown>
*Proof.* Let U and A1, A2,... be defined as in the claim.
</div>
Let P(n) be the proposition " n [ i=1 Ai = n \ i=1 Ai " We will prove $\forall n \in \mathbb{N}$. P(n) by induction on n. BC: Certainly, A1 = A1, so P(1) holds. Also, A1 $\cup$ A2 = A1 $\cap$ A2 by DeMorgan's Law for Sets (Theorem 4.6.9), so P(2) holds. IH: Let $k \in \mathbb{N}$ -{1} be arbitrary and fixed. Suppose $\forall$i \in$[k]. P(i) holds. IS: Our goal now is to deduce that P(k + 1) holds. First, observe that k+1 [ i=1 Ai = Ak+1 $\cup k$[ i=1 Ai


> 🇨🇳 **补充：归纳法的元数学** 归纳法本身不能在皮亚诺公理内被"证明"——它是公理之一。选择归纳法还是良序原理作为公理是习惯问题，另一个可以推出。


so let's define Bk = k[ i=1 Ai Then, observe that k+1 [ i=1 Ai = Ak+1 $\cup B$k Defn of Bk = Ak+1 $\cap$ Bk By BC, P(2) (a.k.a. DeMorgan) = Ak+1 $\cap k$[ i=1 Ai Defn of Bk = Ak=1 $\cap k$\ i=1 Ai By IH, P(k) = k+1 \ i=1 Ai Simplify Thus, P(k + 1) also holds. By induction, $\forall$n \in \mathbb{N}$. P(n).
### 5.4.5 Comparing "Regular" and Strong Induction We want to reiterate something we said earlier when we introduced strong induction as a technique. It bears repeating here, because it's an important lesson: Whenever we have to prove something by induction, we might as well always use Strong Induction. The reason behind this is that regular induction and strong induction are biconditinally connected; each one implies the other. When working through an induction proof, it essentially "doesn't hurt" to make a strong induction hypothesis, because we know we can. When you're working through a proof, you might not anticipate which or how many of the hypotheses from the IH that you'll need to invoke in the IS. It would be a shame to make a weaker hypothesis and find yourself referencing "truths" that you never officially proved! Instead, you might as well make the strongest hypothesis you can, just in case you'll need it. It might end up being overkill (in the sense that you really only needed P(k) to deduce P(k + 1)), but who cares, right? The point is to prove the fact at hand, and as long as that is achieved, then you've been successful. As you move on in your mathematical careers, you'll probably get better at identifying the distinctions between regular/strong induction arguments. In particular, you'll likely notice when strong induction is truly required. Typically, this happens when we have a recursively-defined sequence, but this occurs in many other places, too. As you play around with a problem, trying to come


> 🇨🇳 **补充：归纳法的计算复杂度** 归纳证明的"长度"是常数（与 $n$ 无关）——这就是归纳法的威力：用固定的框架覆盖无限的情况。


up with an argument, look at what sorts of dependencies there are between instances of your proposition. If you notice that an instance depends on several previous ones, you will almost certainly need a strong induction argument.
### 5.4.6 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What are the differences between Strong and Regular Induction? (2) How might you identify when a Strong Induction argument is required? (3) Why is it that we might as well always use Strong Induction, instead of deciding whether to use Regular/Strong? (4) What was interesting about the use of the IH in the Prime Factorization example that we saw? How does it compare to the other examples, where we proved a formula about a recursively-defined sequence of numbers? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Define a sequence of numbers by x1 = 2 and x2 = 3 and $\forall n \in \mathbb{N}$ -{1, 2}. xn = 3xn-1 -2xn-2 Prove that $\forall n \in \mathbb{N}$. xn = 2n-1 + 1 (2) Let the sequence an be defined by a0 = 0 and a1 = 1 and $\forall n \in \mathbb{N}$ -{1}. an = 5an-1 -6an-$2 That is, \langlean\rangle= \langle0, 1, 5, 19, 65, 211,...\rangle Prove that an = 3n$ -2n for every $n \in \mathbb{N} \cup \{0\}$.


> 🇨🇳 **补充：非标准归纳** 有些变体不那么常见：(1) 向后归纳（$P(2^n)$ 再向下推）；(2) 区间归纳（$P(n) \Rightarrow P(n+1)$ 和 $P(n) \Rightarrow P(n-1)$）；(3) 超限归纳。


(3) Let a1 $\in \mathbb{Z}$ be arbitrary and fixed. Define a sequence by setting $\forall$n \in \mathbb{N}$ -{1}. an = n-1 X k=1 k2ak Prove that a1 is even =$\Rightarrow \forall n \in \mathbb{N}. an is even (4) Define a sequence \langletn\rangleby setting t1 = t2 = 2 and \forall n \in \mathbb{N}$ -{1, 2}. tn =


> 🇨🇳 **补充：良序在本书中的使用** 良序原理主要用于反证法——"设最小反例，导出矛盾"。这将在后续章节频繁使用，特别是在基数和集合论中。


2tn-2 (tn-1 -4)(tn-1 -6) Prove that $\forall n \in \mathbb{N}$. tn = 2. (5) You have likely seen the Triangle Inequality before; it states $\forall x, y \in \mathbb{R}$. |x + y| $\leq$|x| + |y| (where |x| is the absolute value of x). Prove that this inequality holds with n variables, not just 2; that is, prove that if we have a sequence of real numbers xi, where $\forall i \in \mathbb{N}. xi \in \mathbb{R}, then \forall n \in \mathbb{N}$.


> 🇨🇳 **补充：总结** 第 5 章完成了从直觉到严格框架的过渡。(1) 常规归纳法——归纳步只需 $P(k)$；(2) 强归纳法——归纳步需要 P(1) 到 $P(k)$；(3) 良序原理——每个非空子集有最小元。三种方法等价，选择取决于问题。


n X k=1 xi $\leq n X k$=1 |xi| (Note: $Prove the n = 2 case, as well. We do not want you to just assume it!) (6) Look back to Section 2.4.1 where we considered tiling 2 \times n rectangular chessboards with dominoes. Here, investigate the similar problem of tiling 3 \times n rectangular chessboards with straight triominoes (i.e. 3 \times 1 rectangular pieces). Identify an inductive relationship and define a sequence that identifies the number of ways to tile a 3 \times n board. (Note$: Don't attempt to find a closed form and/or prove it! The techniques required to do so lie outside the scope of our current discussion. If you are curious, search for recurrence relations. If you'd like, try to apply what you read about to come up with a closed form for this problem. Can you prove it by induction?)
## 5.5 Variants of Strong Induction Much like we saw a few variations on regular induction---inducting with a different base case, on a different set, backwards, etc.---we have a variation on strong induction to discuss here. As you will see, "minimal criminal" arguments are


> 🇨🇳 **补充：后续应用** 从第 6 章开始，所有章节都将使用本章建立的归纳框架。关系、函数、基数、组合数学中的许多证明都依赖归纳法——它已成为我们证明工具箱的核心。


