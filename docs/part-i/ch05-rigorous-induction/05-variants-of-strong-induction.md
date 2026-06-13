---
title: Variants of Strong Induction
---

# Variants of Strong Induction

essentially strong induction proofs where the induction step is done using a contrapositive conditional statement. These types of arguments pop up in induction proofs now and again, and understanding how they work will be very helpful! Furthermore, we will state and prove a property of the set of natural numbers. This is known as the Well-Ordering Principle. Why is it included in this section? Well, you'll see how this principle is closely related to both induction and strong induction!
### 5.5.1 "Minimal Criminal" Arguments Using a Contrapositive Remember that a conditional statement is logically equivalent to its contrapositive. Also, remember that the theorem statements about how induction works all have conditional statements within them. They are always in condition (2), and they represent the action of the IH and IS. What happens if we consider the contrapositive of such a conditional statement? This won't change the truth of the theorem at all, but it will certainly affect how we apply induction as a proof technique. What would happen? Let's find out! Here is the conditional statement from the Strong PMI: $\forall k \in \mathbb{N}$. {$\forall i \in$[k]. P(i) } =$\Rightarrow P (k + 1)$ Negating both sides and switching the arrow, we find its contrapositive: $\forall$k \in \mathbb{N}. \negP(k + 1) = \Rightarrow$ {$\exists$i \in [k]. \negP(i)$ } When applying strong induction, we seek to prove that P(1) and... and P(k) together allow us to deduce P(k +1). This new version of the statement reflects a different approach: supposing that P(k + 1) actually fails, let's deduce that there is a previous instance that also fails. How It Works Technically speaking, there's nothing new to say here! This method works because a conditional statement and its contrapositive are logically equivalent. However, this is a little unsatisfying. It feels funny to argue "backwards" like this, pretending that our proposition fails somewhere and showing that it also fails somewhere earlier. Isn't that the opposite of what we were trying to do? The crux of this method is twofold: (1) we already established a base case, and (2) this "earlier failure" argument is made for an arbitrary k. Here's how we think of it. Say we have a proposition P(n) and we want to show $\forall$n \in \mathbb{N}$. P(n). First, we establish that P(1) holds. Good. Next, we pretend that P(k + 1) fails, for some arbitrary $k \in \mathbb{N}$. (Notice that k + 1 $\geq 2$, so we aren't pretending that P(1) fails, since we already know it holds.) We work through some argument and deduce that an earlier instance fails. Let's say P(ℓ) fails, for some ℓthat satisfies 1 $\leq$ℓ$\leq k$.


> 🇨🇳 强归纳法的变体（Variants of Strong Induction）本节讨论强归纳法的多种变形，包括需要多个基例和复杂归纳假设的情况。


Now, this argument we just made was for an arbitrary k, so the same argument applies to this new value ℓthat we've produced. This guarantees that P(m) fails, for some m that satisfies 1 $\leq m \leq$ℓ-1. Then, the same argument can be re-packaged to apply to the value of m, and then... You might see where this is going. Eventually, we "run out" of previous instances at which the proposition could fail; we have to eventually get back to P(1). But we already know P(1) holds! The main idea can be sumamrized thusly: if we have a valid base case, and there is no smallest instance that fails, then the proposition holds everywhere. This is where the phrase "Minimal Criminal" comes from. (It is chosen for both its descriptiveness and its playful slant rhyme, of course.) "Criminal" refers to an instance where the proposition fails, and proving the implication $\forall k \in \mathbb{N}. \negP(k + 1) = \Rightarrow$ {$\exists i$\in [k]. \negP(i)$ } amounts to showing that there can be no "minimal" such instance. Another phrase that encapsulates this same idea is "No Least Counterexample". You might find this phrase in other books, so be aware that it refers to the same idea. It conveys the idea that there is no counterexample to the claim such that all the previous instances are true. Also, another term for this method is "Infinite Descent". It's less immediately clear that this refers to the same concept, because it is hinting at the actual description we gave of how this method works. By proving that we can always find a smaller counterexample, we are showing that there exists a "backwards" sequence of instances where our proposition fails. However, this sequence cannot be an "infinite descent" because we'll eventually run into P(1), which we proved to be valid. Be aware that both of these terms are also used. We chose "Minimal Criminal" because it's more fun to say. Proof Template Let's briefly show you a template for how to write a proof like this, and then we'll move right into working through an example proof of an interesting fact. There isn't anything particularly new right here. We're applying the direct proof strategy to a =$\Rightarrow s$tatement; it's just that this statement is the contrapositive of a statement we've already seen before. Template for a "Proof by a Minimal Criminal Argument" Goal: Prove that $\forall$n \in \mathbb{N}$. P(n)
<div class="def-proof" markdown>
*Proof.* Let P(n) be the proposition " ". We will prove $\forall n \in \mathbb{N}$. P(n) by induction on n (a "minimal criminal"
</div>


> 🇨🇳 **回顾强归纳法** 强归纳法与常规归纳法的区别在于归纳假设：常规归纳假设 $P(k)$，强归纳假设 $P(1) \wedge P(2) \wedge \cdots \wedge P(k)$。当归纳步需要多个前置命题为真时，我们必须使用强归纳。


argument, in fact). Base Case: Observe that P(1) holds because. Induction Hypothesis: Let $k \in \mathbb{N}$ be arbitrary and fixed. Suppose P(k + 1) is False. Induction Step: Deduce that $\exists$ℓ$\in \mathbb{N}$ that satisfies 1 $\leq$ℓ$\leq k$ and such that P(ℓ) is False. It follows that $\forall$n \in \mathbb{N}$. P(n). If you're worried about forgetting the technical details of this template, just keep the main idea in your mind: A "Minimal Criminal" argument works by applying the contrapositive of the usual IH and IS steps of an induction proof.
Example
The following result is interesting in its own right. (In fact, we will use it later on in Section 7.6.3 when we talk about how "big" infinite sets are. Neat, right?) We encourage you to play around with the claim first before jumping into the proof. Try to see why it's true and how it works. Check it for small values of n. Then, as you read the proof, look at your scratch work and see how it mimics the kinds of patterns you might have observed.
Example 5.5.1. Expressing naturals uniquely as a product:
Claim: Every $n \in \mathbb{N}$ can be expressed uniquely as a power of 2 times an odd
number. That is, $\forall n \in \mathbb{N}. \exists m$, ℓ$\in \mathbb{N} \cup \{0\}$. n = 2m $\cdot (2ℓ+ 1)$ and the ℓ, m that exist are the only values that satisfy this equality.
<div class="def-proof" markdown>
*Proof.* We prove this claim by induction on n; specifically, we use a "minimal
</div>
criminal" argument. BC: Observe that n = 1 has such a representation as 1 = 20 $\cdot (2 \cdot$ 0 + 1). Furthermore, this is the only such representation because any other power of 2 will make the product at least 2, and any other odd will make the product at least 3. IH: Let $k \in \mathbb{N}$ be arbitrary and fixed. Suppose that P(k + 1) fails, i.e. that k + 1 has no such representation, or it has more than one such representation. We will have two cases based on the parity of k + 1. Case 1: Suppose k + 1 is even. This means k+1


> 🇨🇳 **何时需要强归纳？** 如果归纳步只依赖于 $P(k)$，常规归纳即可。如果归纳步需要 P(j) 对某个 $j < k$，就需要强归纳。关键是分析归纳步真正使用了哪些前置信息。


$\in \mathbb{N}$. First, suppose k + 1 has no such representation. Then, neither does k+1 2 ; for if


> 🇨🇳 **例：Fibonacci 数列** $F_1 = F_2 = 1$，$F_n = F_{n-1} + F_{n-2}$（$n \geq 3$）。要证关于 Fibonacci 数的性质，归纳步同时使用 P(k) 和 $P(k-1)$，因此需要强归纳和两个基例。


it actually did, then we could simply double it (i.e. increasing the power of 2 by 1) to find a representation of k + 1. Thus, P { k+1


> 🇨🇳 **证明 Fibonacci 不等式** 命题：$F_n < 2^n$。基例：$F_1 = 1 < 2^1$，$F_2 = 1 < 2^2$。归纳步：设对 $j \leq k$ 有 $F_j < 2^j$，则 $F_{k+1} = F_k + F_{k-1} < 2^k + 2^{k-1} < 2^k + 2^k = 2^{k+1}$。


} fails in this case (for non-existence). Next, suppose k + 1 has at least two such representations: k + 1 = 2m1(2ℓ1 + 1) and k + 1 = 2m2(2ℓ2 + 1) We are assuming they are different, i.e. (m1, ℓ1) $\neq (m2, ℓ2)$. Since k + 1 is even, we know m1, m2 $\geq 1$. By descreasing the powers of 2 by 1 each, we see that k + 1


> 🇨🇳 **例：邮资问题** 证明用 4 分和 7 分邮票可以凑出 $n \geq 18$ 分邮资。需要 4 个基例：18=4+4+4+4+2\,不对——需验证。实际上：18=4+7+7，19=4+4+4+7，20=4+4+4+4+4，$21=7+7+7$。


= 2m1-1(2ℓ1 + 1) and k + 1


> 🇨🇳 归纳步：设对 $18 \leq j \leq k$ 可凑出，要凑 $k+1$。当 $k+1 \geq 22$ 时，$(k+1)-4 \geq 18$，由归纳假设 $(k+1)-4$ 可凑出，再加一枚 4 分即可。所以 4 个基例启动归纳链后完全适用。


= 2m2-1(2ℓ2 + 1) are two representations of k+1 2. (Also note that m1 -1, m2 -1 $\geq 0$.) These are different because (m1 -1, ℓ1) $\neq (m2 -1, ℓ2)$, based on our assumption above. Thus, P { k+1


> 🇨🇳 **良序原理（Well-Ordering Principle）** $\mathbb{N}$ 的每个非空子集都有最小元素。这是与归纳法等价的公理——可以由此证明归纳法，反之亦然。


} fails in this case (for non-uniqueness). In either situation, we find that P { k+1


> 🇨🇳 **用良序原理证明归纳法** 反证：设 $P(1)$ 成立且 $\forall k.\, P(k) \Rightarrow P(k+1)$，但存在 $n$ 使 $P(n)$ 不成立。令 $S = \{n \in \mathbb{N} \mid P(n) \,\text{不成立}\}$。$S$ 非空，由良序原理有最小元 $m$。但 $m \neq 1$（$P(1)$ 成立），故 $m-1 \in \mathbb{N}$ 且 $P(m-1)$ 成立。归纳步给出 $P(m)$ 成立——矛盾！


} fails. Case 2: Suppose k + 1 is odd. This means $\exists$ℓ$\in \mathbb{N}$\cup \{0\}$. k + 1 = 2ℓ+ 1. Then certainly we can represent k + 1 as k + 1 = 20 $\cdot (2ℓ$+ 1)$ Also, there is certainly no other way to do this. Using a different power of 2 will make the product even (but k + 1 is odd), and using a different odd factor will make the product different. Thus, this case is a contradiction. \times\times\times\times By indcution, then, \forall n \in \mathbb{N}$. P(n) holds. Interesting, isn't it? There was actually a little bit more going on, logically speaking, in this proof than we led on at the beginning. Specifically, the cases based on parity make this a little trickier. One of the cases (the even one) follows the "minimal criminal" argument. The other case (the odd one) can actually truly be proven. In this proof, we assumed P(k + 1) failed, but then realized it actually couldn't when k + 1 is odd. That was the contradiction. It seems a little roundabout in retrospect, but it allows us to present the entire proof as a "minimal criminal" argument, rather than just doing two separate proofs, one for odds and one for evens. Furthermore, we had to address not only the existence but the uniqueness of these representations. This is why there were two considerations to make in the case for k + 1 being even. To show existence of these representations, we had to show it is not possible for k+1 to have zero representations; to show uniqueness, we had to show it is not possible for k + 1 to have two representations.


> 🇨🇳 **用归纳法证明良序** 反证：设 $S \subseteq \mathbb{N}$ 非空但无最小元。则 $S$ 中没有 $1$（否则 1 就是最小元）。设 $\{1,\ldots,k\} \cap S = \emptyset$，则 $k+1 \notin S$（否则 $k+1$ 是最小元）。由归纳法 $S = \emptyset$——矛盾！


### 5.5.2 The Well-Ordering Principle of $\mathbb{N}$ Motivation We are all familiar with the relationship "$\leq$" on the natural numbers $\mathbb{N}$. Given any two elements x, $y \in \mathbb{N}$, it must be that one of the two relationships holds: either $x \leq$ y or $y \leq$ x (or possibly both, but only when x = y). We also know that $\forall x$, y, $z \in \mathbb{N}$. {$x \leq y \wedgey \leq z$ } =$\Rightarrow x \leq z and that \forall x \in \mathbb{N}. x \leq x$. This makes N an ordered set; we call "$\leq$" an order relation on $\mathbb{N}$. (See Section 6.3 for more information.) Furthermore, it turns out that this relationship is a well-ordering. We won't define this term formally, but one of the key aspects of being a wellordering is not having any infinitely-descending chains. Just think about how this works in $\mathbb{N}$: Does there exist an infinite sequence of elements a1, a2, a3,... such that a1 > a2 > a3 > $\cdot$\cdot$\cdot$ ? Is that possible? (Notice these inequalities are strict). No, it's not! The idea is that, starting from some number a1 $\in \mathbb{N}$, if we "descend" we have to eventually reach 1. We can't "go lower" than that. Rather than discuss well-orderings in generality---which you can do in a class on set theory or formal logic---we will just discuss how this concept works in the context of $\mathbb{N}$. It's a useful property, and we will have occasion to cite it in the future, too! In this section, we will state the principle, get your help in proving it, and then demonstrate its relationship with induction. Statement and Proof
<div class="def-theorem" markdown>
**Theorem 5.5.2. Every non-empty subset of $\mathbb{N}$ has a least element. Stated in**
</div>
logical form, $\forall S \in P (N)$. [$S \neq$\emptyset$=$\Rightarrow(\exists$ℓ$\in S. (\forall x \in S$. ℓ$\leq x$))] Think about how this relates to our statement before that we cannot have an infinitely-descending chain of natural numbers. If we did have such a chain, we could define S to be the set of all of those elements in the chain. This set would not have a least element. Given an element of that set, we know it is one of the elements in the chain; let's say it's an. Then, an+1 is also in the set and an+1 < an. Thus, there would be no least element. We will have you prove this theorem, because we think it will be instructive to work through the details. It is outlined for you in several steps. One key observation is that the proof is by induction! That is, by proving the Well-Ordering Principle in this way, we will have shown that the Principle of Mathematical Induction implies the Well-Ordering Principle.
<div class="def-proof" markdown>
*Proof.* By induction. Left for the reader as Exercise 5.7.21
</div>
An easy extra observation to make is that the least element of any subset $S \subseteq \mathbb{N}$ must also be unique. That is, we can't have two (or more) least elements. Let's say we actually do have two least elements of a set S; call them ℓand m.


> 🇨🇳 **回顾与比较** 三种等价的数学基础：(1) 数学归纳法原理(PMI)，(2) 强归纳法原理，(3) 良序原理。它们可以互相推出，选择哪种取决于具体证明的需要。


By the definition of what it means to be the least element, we would know ℓ$\leq m and m \leq$ℓ. Of course, this tells us ℓ= m, so they're the same! Induction, Strong Induction, and The WOP As we mentioned before, because we used induction to prove the Well-Ordering Principle, this shows the Principle of Mathematical Induction implies the WellOrdering Principle. The next theorem shows that, in fact, those two theorems are logically equivalent: they imply each other. Furthermore, it says the the Principle of Strong Induction also implies the Well-Ordering Principle, and viceversa. In fact, it says that all three of these theorems are logically equivalent! Essentially, this is saying that these three theorems
<div class="def-theorem" markdown>
**Theorem 5.5.3. The following are all logically equivalent:**
</div>
• The Principle of Mathematical Induction • The Principle of Strong Induction • The Well-Ordering Principle
<div class="def-proof" markdown>
*Proof.* Let's use the following shorthand for each theorem:
</div>
• PMI: The Principle of Mathematical Induction • PSI: The Principle of Strong Induction • WOP: The Well-Ordering Principle By the way we proved PSI and WOP, we can already deduce that PMI =$\Rightarrow PSI and PMI =\Rightarrow W$OP We also described in Section 5.4.2 how PSI =$\Rightarrow PMI so now we know that PMI \Leftrightarrow PSI and PMI =\Rightarrow W$OP To complete the proof, we will show that WOP =$\Rightarrow PMI. This will show that WOP\Leftrightarrow P$MI, and the equivalence above will allow us to deduce that all three are logically equivalent. To prove this, let's assume that the WOP is valid. We will use it to prove PMI. (Look back at the statement of PMI, in Theorem 5.2.2, to remind yourself why what we're about to do accomplishes our goal.) Suppose we have a proposition P(n), defined for every $n \in \mathbb{N}$. Let's suppose that P(1) is True, and that $\forall$k \in \mathbb{N}. P(k) =\Rightarrow P (k +1)$. We need to show that $\forall$n \in \mathbb{N}$. P(n) holds.


> 🇨🇳 **例：用良序证明"每个 $n \geq 2$ 有素因子"** 设 $S = \{n \geq 2 \mid n \,\text{没有素因子}\}$。若 $S$ 非空，令 $m$ 为其最小元。$m$ 不为素数（否则 $m$ 是自身的素因子）。故 $m = ab$（$a,b < m$），由 $m$ 的最小性 $a$ 有素因子 $p$，$p | a | m$——矛盾！


Define the set F to be the set of "False instances" of P(n). That is, define F = {$n \in \mathbb{N}$ | P(n)is False} To prove that $\forall$n \in \mathbb{N}$. P(n), we will AFSOC that $F \neq$\emptyset$. Notice that $F \subseteq \mathbb{N}$, because we used set-builder notation. By our assumption in the line above, $\exists$f \in$ F. Let such an f be given. Because of these two conditions, the WOP applies to the set F, telling us that F has a least element. Let ℓbe that least element. We know that ℓ$\in F$ and, $\forall$x \in$ F. ℓ$\leq x$ Consider the case that ℓ= 1. This is not possible, because our assumption above says that P(1) holds, so 1 $\notin F$. Now, consider the case that ℓ$\geq 2$. Our assumption above said that $\forall$k \in \mathbb{N}. P(k) =\Rightarrow P (k + 1)$ which is logically equivalent to $\forall$k \in \mathbb{N}$ -${1}. \negP(k) = \Rightarrow \negP(k$ -1) by taking the contrapositive. Applying this to the element ℓ$\in \mathbb{N}$ -${1}, we deduce that \negP($ℓ-1) also holds. That is, P(ℓ-1) is False. This means that ℓ-1 $\in F$. However, this contradicts the fact that ℓis the least element of F, since ℓ-1 < ℓ$. \times\times\times\times Therefore, it must be that F = \emptyset$, which means that $\forall n \in \mathbb{N}$. P(n). This shows that the theorem PMI is valid. Look at the main part of this proof. To prove that P(n) holds for all n, we supposed it failed for a particular n, the element $f \in$ F. From there, you might be tempted to say, "Well, P(f) failing means P(f -1) fails, which then means P(f -2) also fails,... and so on, all the way down to P(1), but we know that P(1) is True." But that argument about "and so on" is precisely what PMI and WOP are all about! You can't use a hand-wavey "just keep going" argument to prove the very idea that you're allowed to make such arguments! This is why we invoked the WOP to produce the least element of F. It might have seemed odd to you that we would introduce $f \in$ F and the never use it again. We needed it to exist to guarantee $F \neq$\emptyset$, which allows us to apply WOP.
### 5.5.3 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you


> 🇨🇳 **归纳法与良序的选择策略** 证明"对所有 $n$ 某性质 $P(n)$ 成立"时用归纳法。证明存在性或反证某集合为空时用良序。有些问题两种方法都能用。


can confidently answer these before moving on will help your understanding and memory! (1) What is the difference between a "Minimal Criminal" argument and a Strong Induction proof? (2) We proved that every $n \in \mathbb{N}$ can be written as a product of a power of 2 and an odd number. What else is true about this representation? (3) We proved that N is well-ordered. Do you think Z also has the property? What about Q? What about R? (4) What does it mean that PMI and PSI and WOP are all logically equivalent? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; $making sure you can work through them will help you! (1) Prove the Well-Ordering Principle. It's Exercise 5.7.21. Seriously, do it! (2) Prove that \sqrt 3 is irrational. (Hint$: $AFSOC that \sqrt 3 = a b, where a, b$\in \mathbb{N}$ and the fraction is in reduced form. Use a descent argument to contradict this reduced form assumption.) (3) Use the Well-Ordering Principle to prove that every natural number, except 1, can be written as a sum of non-negative multiples of 2 and 3. For example, 2 = 2 and 8 = 6 + 2 and 101 = 3 $\cdot$ 33 + 2. (4) Consider the following equation: 4x4 + 2y4 = z4. In this problem, you will prove that this equation has no solution, (x, y, z) $\in \mathbb{N}$3, by an argument that appeals to the Well-Ordering Principle. (a) AFSOC (x, y, z) $\in \mathbb{N}$3 is a solution, and suppose further that this solution has the smallest value of x amongst all solutions. That is, we are defining T = {$x \in \mathbb{N}$ | $\exists y$, $z \in \mathbb{N}$. 4x4 + 2y4 = z4} and pre-supposing that this set is non-empty (i.e. the equation has solutions) so that T has a least element. (b) Deduce that z is even. Hint: In this and the next two parts, you may use the fact that a sum/difference of multiples of some natural number m is also a multiple of m.)


> 🇨🇳 **练习** (1) 用强归纳法证明：任何 $n \geq 12$ 可以写成 $4a + 5b$（$a,b \in \mathbb{N} \cup \{0\}$）。(2) 用良序原理证明 $\sqrt{2}$ 是无理数。


(c) Deduce that y is even. (d) Deduce that x is even. (e) Use this to deduce that there is another solution (a, b, c) with a smaller value of the first variable, i.e. a < x. (f) Explain why this has proven that there are no solutions.
## 5.6 Summary Now, we have finally placed induction on solid, mathematical ground! We have been building towards this for a while, so we wanted to present this fully when we finally got here. We took care to formally state and prove the Principle of Mathematical Induction, and see several examples of it in action. Then, we used PMI to prove the more general Principle of Strong Induction. In so doing, we pointed out that any induction proof might as well be a strong induction one, because one technique "subsumes" the other. Furthermore, we later proved--- in the section about the Well-Ordering Principle of $\mathbb{N}$---that the two principles of induction we introduced are logically equivalent to each other (and to the Well-Ordering Principle, as well). We saw a few variants of induction and an example or two for each one. One of the more helpful techniques we will use later on is the "minimal criminal" argument. This amounts to an induction proof where the induction step proves the contrapositive of the conditional statement required. For all of these variants of induction, we provided you with some proof templates. Consult them in the future, and use them to make your proofs wellorganized, clear, and easy to read. Not only will this make it easier for a reader to understand your written work, it will also reiterate the important concepts behind these proof techniques. These are not created by us out of pedantry, mind you: they are based firmly on the underlying principles! The exercises below will give you lots of practice in working with all kinds of inductive arguments. We have posed some problems that are significantly more challenging than the ones we saw in Chapter 2. This is because we have now thoroughly studied the principle of induction and feel confident applying it to solve problems. Furthermore, some of the results you prove in these problems are interesting and helpful facts to have at our disposal. We will have occasion to refer to some of them in our later work in this book, even!
## 5.7 Chapter Exercises These problems incorporate all of the material covered in this chapter, as well as any previous material we've seen, and possibly some assumed mathematical knowledge. We don't expect you to work through all of these, of course, but the more you work on, the more you will learn! Remember that you can't truly learn mathematics without doing mathematics. Get your hands dirty working on a problem. Read a few statements and walk around thinking about them.


> 🇨🇳 (3) 用强归纳法证明 $F_n < (5/3)^n$（对所有 $n$）。(4) 解释为什么 Fibonacci 相关的证明需要两个基例。(5) 证明良序原理与归纳法原理的等价性。


Try to write a proof and show it to a friend, and see if they're convinced. Keep practicing your ability to take your thoughts and write them out in a clear, precise, and logical way. Write a proof and then edit it, to make it better. Most of all, just keep doing mathematics! Short-answer problems, that only require an explanation or stated answer without a rigorous proof, have been marked with a }. Particularly challenging problems have been marked with a $\star$. Problem 5.7.1. Prove that $\forall n \in \mathbb{N}$. n X k=1 k3 = n X k=1 k !2 Problem 5.7.2. For each of the following inequalities, determine the set of natural numbers for which it holds. Make a claim and then prove it (by induction, if necessary). (a) 3n > n4 (b) (n -3)2 > (n -2)3 (c) 3n < n! (d) 4n > n4 Problem 5.7.3. What is wrong with the "proof" of the following claim?
Claim: Every even natural number is a power of 2.
We prove this by induction on n. Notice that 2 = 21 is a power of 2. Next, suppose $k \in \mathbb{N} and k \geq 4$ and k is even. Suppose that every even natural number up to (but not including) k is a power of 2. Since k is even, we can consider k 2. By assumption, k 2 is a power of 2, so k 2 = 2j for some j. This shows that k = 2j+1, so k is a power of 2. Problem 5.7.4. Let's say that a number $n \in \mathbb{N}$ is "Special in the Land of (x, y)" if n can be written as a sum of non-negative multiples of x and y. For example, 11 is Special in the Land of (3, 5) because 11 = 5 + 2 $\cdot$ 3. Also, 15 is Special in that Land because 15 = 3 $\cdot$ 5 + 0 $\cdot$ 3. However, 7 is not Special there. For each of the following pairs (x, y), state and prove a claim that identifies the set Sx,y of all numbers that are Special in the respective Land.


> 🇨🇳 (6) 设数列 $a_1 = 5, a_2 = 7, a_n = 3a_{n-1} - 2a_{n-2}$（$n \geq 3$）。用强归纳法证明 $a_n = 3 \cdot 2^{n-1} - 1$。(7) 解释何时用常规归纳、何时用强归纳、何时用良序。


1. (2, 3) 2. (3, 5) 3. (4, 9) 4. (7, 6) Problem 5.7.5. Prove that for any $n \in \mathbb{N}$, for any real numbers x1, x2,..., xn that satisfy $\forall$i \in$[n]. 0 $\leq$ xi $\leq 1$, the following inequality holds: n Y i=1 (1 -xi) $\geq 1$ - n X i=1 xi This is known as Bernoulli's Inequality. Problem 5.7.6. Let P(n) be a proposition that depends on the variable n, which is allowed to assume any integer value. For each of the following situations, you are given some kind of "Base Cases" and some kind of "Inductive Implication". Identify and explain which instances of the proposition you could necessarily deduce, from those assumptions. For instance, if you were given P(3) as a Base Case and $\forall$n \in \mathbb{N}. P(n) =\Rightarrow$ P(n + 1) as an Inductive Implication, a correct answer would be "We would know P(n) holds for every $n \in \mathbb{N} with n \geq 3$." 1. Base Cases: P(-3). Implication: $\forall n \in \mathbb{Z}. P(n) =\Rightarrow P (n + 1)$ 2. Base Cases: $P(1) \wedgeP(2). Implication$: $\forall n$\in \mathbb{N}. P(n) =\Rightarrow P (2n)$ 3. Base Cases: P(0). Implication: $\forall n \in \mathbb{Z}. P(n) =\Rightarrow$ {P(n-$1)\wedgeP(n+1)$ } 4. Base Cases: P(-$1) \wedgeP(0). Implication$: $\forall n$\in \mathbb{N}. P(n) =\Rightarrow P (n + 2)$. Problem 5.7.7. Prove that for any integers x, $y \in \mathbb{Z} (with $x \neq$ y)$, the number xn -yn is a multiple of x -y, for every $n \in \mathbb{N} \cup \{0\}$. Problem 5.7.8. (a) Identify the set of natural numbers n for which the inequality n! > 2n holds. (Recall: n! = $n \cdot (n -1)$\cdot$\cdot$\cdot$ 1.) (b) Identify the set of natural numbers n for which the inequality n! > 3n holds. (c) Identify the set of natural numbers n for which the inequality n! > 5n holds. Problem 5.7.9. \starProve the following generalization of the previous problem: $\forall$m \in \mathbb{N}$ -{1}. $\exists$ Bm $\in \mathbb{N}. \forall n \in \mathbb{N}$. $n \geq$ Bm =$\Rightarrow n$! > mn Problem 5.7.10. Recall that the Fibonacci Numbers are defined by setting f0 = 0 and f1 = 1 and then, for every $n \geq 2$, setting fn = fn-1 + fn-2. Prove the following hold for this sequence:


> 🇨🇳 **补充：向前归纳与向后归纳** 向前归纳从基例向前推导；向后归纳（Cauchy 归纳）从 $P(2^n)$ 或某个大数开始向后推。某些不等式用向后归纳更自然。


(a) $\forall n \in \mathbb{N} \cup \{0\}$. fn < 2n (b) $\forall n \in \mathbb{N}$. fn-1fn+1 = f 2 n + (-1)n (c) $\forall n \in \mathbb{N}. 1 \leq fn+1 fn \leq2 (d) \forall n \in \mathbb{N}$. n X k=1 f2k = f2k+1 -1 (e) $\forall n \in \mathbb{N}. n X k=1 f 2 k = fnfn+1 Problem 5.7.11. In Problem 5.7.1, you proved a formula for the sum of the first n perfect cubes. Specifically, you proved that it is the square of the sum of those base numbers. In this problem, we want you to prove the converse of this assertion, that the only sequence of numbers with this property is \langle1, 2,..., n\rangle. We will restate this claim below for you to consider, and then prove.$
Claim: $Suppose \langleai\rangleis a sequence of real numbers, i.e.$
$\forall i \in \mathbb{N}. ai \in \mathbb{R}$. Suppose this sequence has the property that $\forall n \in \mathbb{N}$. n X k=1 a3 k = n X k=1 ak !2 Prove that, necessarily, $\forall n \in \mathbb{N}$. an = n, by induction on n. Problem 5.7.12. (a) Prove that $\forall n \in \mathbb{N}$. 7n + 7 < 7n+1. (b) Prove that $\forall n \in \mathbb{N}$. 3n + 3 < 3n+1. (c) Identify the set S of real numbers r that satisfy $\forall n \in \mathbb{N}$. rn + r < rn+1. Prove your claim by induction. Problem 5.7.13. Prove that for every $n \in \mathbb{N}$, 23n + 1 is a multiple of 3n+1. Problem 5.7.14. $\star$Assume x + 1 x is an integer. Prove xn +


> 🇨🇳 **补充：超限归纳** 序数上的归纳法（超限归纳）将自然数归纳推广到任意良序集。这是集合论和数学基础的重要工具，但超出了本书范围。


xn is an integer for all $n \in \mathbb{Z} (Note: Do this for every $n \in \mathbb{Z}$, not just $n \in \mathbb{N}$!)$. Problem 5.7.15. Prove that n3 + 5n is a multiple of 6 for every $n \in \mathbb{N}$, by induction on n. Problem 5.7.16. Prove that the following summation equality holds for every $n \in \mathbb{N}$: 2n-1 X k=n 2k + 1 = 3n2


> 🇨🇳 **补充：结构归纳** 对递归定义的结构（如树、列表），结构归纳法证明"对任意合法构造的结构，某性质成立"。基例处理基本结构，归纳步处理复合结构。


Problem 5.7.17. For every $n \in \mathbb{N} \cup \{0\}$, define sn = { $3 + \sqrt$


> 🇨🇳 **补充：归纳假设的写法** 归纳假设一定要写清楚！不能只写"设 $P(k)$"，要明确 $k$ 的范围。强归纳要写"设对 $\forall j \leq k$ 有 $P(j)$"。


}n Prove that every such sn is actually an integer. Also, prove that, in fact, sn is a multiple of 2n. (!) Problem 5.7.18. } In this problem, we will prove that the familiar Harmonic Series, given by $\infty$ X k=1


> 🇨🇳 **补充：基例的数量** 基例数量取决于归纳步使用了哪些前置命题。如果只用 $P(k)$，一个基例；如果用 $P(k)$ 和 $P(k-1)$，至少两个基例使归纳链不断裂。


k = 1 + 1 2 + 1 3 + 1 4 + $\cdot \cdot \cdot$ is divergent; that is, we will prove that the sum of all the terms does not approach a finite limit. We claim that the following inequality holds for every natural number n: 2n X k = 1


> 🇨🇳 **补充：错误的归纳证明** 常见错误：(1) 基例不够——归纳链缺失起点；(2) 归纳假设写错——如强归纳中只假设 $P(k)$ 而非 $P(1) \wedge \cdots \wedge P(k)$。(3) 归纳步中偷用了待证结论。


Call this inequality $\star$. (a) Prove that \starholds true when n = 1. (b) Suppose that $m \in \mathbb{N}$ is arbitrary and fixed, and suppose that \starholds true for the value n = m. Deduce that \staralso holds for the value n = m + 1. Be sure to cite where you use the above assumption about the case where n = m. (c) Think about what you have accomplished so far. Explain how the Harmonic Series cannot converge to any finite limit. Problem 5.7.19. Prove that the following inequality holds for every $n \in \mathbb{N}$: n X k=1


> 🇨🇳 **补充：归纳法的历史** 数学归纳法最早由帕斯卡（Pascal, 1654）正式使用，但思想可追溯到古希腊和伊斯兰数学。良序原理在 19 世纪被形式化。


$\sqrt k = 1 + 1 \sqrt 2 + 1 \sqrt 3 + \cdot \cdot \cdot 1 \sqrtn \geq \sqrtn Use this to deduce that the infinite series P \infty$ k=1


> 🇨🇳 **补充：强归纳与递归** 强归纳与递归定义天然适配——如 Fibonacci 的递归定义给出每步依赖前两项，这与强归纳假设的形式完全吻合。


$\sqrt k does not converge to a finite limit. Problem 5.7.20. Prove that the following inequality holds for every n \in \mathbb{N}$: n Y i=1 ( i + 1 i2 ) = ( 1 + 1


> 🇨🇳 **补充：归纳法证明模板** (1) 明确命题 $P(n)$；(2) 验证基例；(3) 写出归纳假设（注明哪些 j 的 P(j) 被假设成立）；(4) 从假设推导 $P(k+1)$；(5) 宣布结论。


) $\cdot \cdot \cdot ( 1 + 1 n2 )$ < 4 -1 n Problem 5.7.21. In this problem, you will prove the Well-Ordering Principle of the natural numbers. This is stated in Theorem 5.5.2, but we'll restate it here: $\forall S \in P (N)$. [$S \neq$\emptyset$=$\Rightarrow ($\exists$ℓ$\in S$. ($\forall x \in S$. ℓ$\leq x$)$)]


> 🇨🇳 **补充：良序证明模板** (1) 反证——设某集合 $S$ 非空；(2) 由良序原理取最小元 m；(3) 利用 m 的最小性得出矛盾（m 不应在 S 中）；(4) 故 $S = \emptyset$，得证。


That is, every non-empty set of natural numbers has a least element. You will prove this claim by induction on whether or not a given set S contains n as an element. We will start the proof for you, and then guide you through the rest: Let $S \subseteq \mathbb{N}$ be arbitrary and fixed. For every $n \in \mathbb{N}$, define P(n) to be the proposition " $n \in$ S =$\Rightarrow$[$\exists$ℓ$\in S$. ($\forall$x \in$ S. ℓ$\leq x$)] " (a) Prove that P(1) holds. (Hint: What's the smallest natural number?) (b) Let $k \in \mathbb{N}$ be arbitrary and fixed. Write down, using logical notation, a hypothesis which asserts that P(i) holds true for every i between 1 and k (inclusive). (Hint: This should be easy; just write an "and" statement. Think about what it means.) Next, suppose k + 1 $\in S$. Define T = S -{k + 1}. There are three cases: (c) Consider the case that T = $\emptyset$. Prove that S has a least element. (d) Consider the case that $T \neq$\emptyset$ and $\forall$x \in$ S. $x \geq$ k + 1. Prove that S has a least element. (e) Consider the case that $T \neq$\emptyset$ and $\exists$x \in$ S. x < k + 1. Prove that S has a least element. (Hint: Here is where you will need to use an assumption from (b), one of the induction hypotheses!) Since S has a least element in every case, we deduce that P(k + 1) holds. By induction, $\forall$n \in \mathbb{N}$. P(n). (f) Let's show why this proof actually worked! Consider an arbitrary $S \subseteq \mathbb{N}$ such that $S \neq$\emptyset$. How do we know S has a least element? That is, which instance of the claim P(n) is guaranteed to hold? (Hint: This would fail if S = $\emptyset$... ) (g) [Bonus] Why didn't we just induct on the size of the set S? Why would that not prove WOP? Problem 5.7.22. Let W be the set of well-formed strings of parentheses. Any element w of the set W satisfies one of the following conditions: (i) w is the string "( )" (ii) $\exists$x \in W$ such that w is the string "( x )" (i.e. w is the string consisting of parentheses around the string x)


> 🇨🇳 **补充：强归纳的直观** 强归纳中的归纳链像一条"宽桥"——每一步都站在前面所有步骤的积累上向前走。常规归纳则是"单脚跳"——每步只踩一个前面步骤。


(iii) $\exists x, y \in W$ such that w is the string "x y" (i.e. w is the string consisting of the string y appended after the string x) For example, "( ) ( )" is a well-formed string in W, because it consists of the valid string "( )" appended after itself. However, "( ( )" is not a well-formed string in W, because it does not satisfy any of the above conditions. (As a more complicated example, we will let you figure out why "( ( ) ( ( ) ) )" is a well-formed string.) Prove the following statements about this system. (a) Prove that every element $w \in$ W has an even number of parentheses, in total. (Hint: Use a Minimal Criminal argument. Suppose w is a string of the smallest odd length... ) (b) For $w \in$ W, let L(w) be the number of left parentheses appearing in w, and let R(w) be the number right parentheses. Prove that $\forall$w \in W$. L(w) = R(w). (Hint: Induct on the length of the string.) Problem 5.7.23. What is wrong with the following "spoof" that all pens have the same color? "Spoof": We claim that all pens have the same color. We will prove this by showing that a set of pens of any size has only one color represented amongst those pens. We will provide an inductive argument for this claim, by inducting on the size. Consider a group of pens with size 1. Since there is only 1 pen, it certainly has the same color as itself. Now, suppose that any set of n pens has only one color represented inside the group. Take any set of n + 1 pens. Line them up on a table and number them from 1 to n + 1, left to right. Look at the first n of them, i.e. look at pens 1, 2, 3,..., n. This is a set of n pens so, by assumption, there is only one color represented in the group. (We don't know what color that is yet.) Then, look at the last n of the pens; i.e. look at pens 2, 3,..., n + 1. This is also a set of n pens so, by assumption, there is only one color represented in this group, too. Now, pen #2 happens to belong to both of these sets. Thus, whatever color pen #2 is, that is also the color of every pen in both groups. Thus, all n + 1 pens have the same color.


> 🇨🇳 **补充：归纳法的哲学** 归纳法的神奇之处在于用有限的两步覆盖无限的情况。其合法性源于自然数的良序性——每个非空子集有最小元保证了归纳链的"起点"。


By induction, this shows that any group of pens, of any size, has only one color represented. Looking at the finite collection of pens in the world, then, we should only find one color. "□" Problem 5.7.24. An n-gon is a convex polygon with n sides. For example, a 3-gon is a triangle, a 4-gon is any rectangle, and so on. ("Convex" means that there are no "indents" in the shape or, equivalently, that if you take any two points inside the shape and draw the line segment between them, that segment does not go outside the shape.) Prove, by induction on n, that there are n(n-3)


> 🇨🇳 **补充：本书的归纳法之旅** Ch1-Ch2 引入直觉，Ch3-Ch4 提供集合与逻辑工具，Ch5 建立严格框架。至此，读者应具备使用归纳法的完整能力。后续章节将其应用于函数、基数等。


possible diagonals that can be drawn between the vertices of an n-gon. (Do not count the actual boundary sides of the shape as diagonals, only interior diagonals.)
## 5.8 Lookahead With a whole array of proof techniques and logical knowledge at our disposal now, we could try to go just about anywhere in the mathematical universe. We will choose to explore some particular areas, with the goal of talking about functions. We have referred to this idea before, but have not discussed it in a mathematical setting. Over the next two chapters, we will formalize this notion.


> 🇨🇳 **补充：后续展望** 归纳法在第 5 章建立了严格框架后，将成为贯穿全书的证明工具。特别是在讨论函数性质、基数和组合恒等式时，归纳法是核心方法。


