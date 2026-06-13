---
title: Inclusion/Exclusion
tags:
  - 组合数学
  - 计数
  - 鸽巢原理
  - 容斥原理
---

# Inclusion/Exclusion

### 8.7.2 Statement and Proof
<div class="def-theorem" markdown>
**Theorem 8.7.1 (Inclusion/Exclusion). Suppose we have a universal set U and**
</div>
some subsets A1, A2,..., An $\subseteq U$. Then, |U -(A1 $\cup$ A2 $\cup$ $\cdots$ $\cup$ An)| = X S$\subseteq [n]$ (-1)|S|


> 🇨🇳 容斥原理（Inclusion/Exclusion Principle）本节推广"从大集合中去除子集后清点剩余"的思想到任意多个集合。


where $\bigcap_{i \in \emptyset} A_i = U$ (Try writing out the above expression in the cases where n = 1 and n = 2 and n = 3 to see why they're the same as the ones we wrote in the previous section. To prove this theorem, we will apply a counting in two ways argument. Specifically, we will consider an element $x \in U$ and argue that it is counted the correct number of times on both sides of the above equation.
<div class="def-proof" markdown>
*Proof.* Let $x \in U$ be arbitrary and fixed. We'll consider two cases.
</div>
First, suppose $x \notin A_i$ for every $i \in$[n]. Then the left-hand side counts x exactly once, since x is not an element of the union of the Ai sets. The right-hand side only counts x in the term where S = $\emptyset$, because x is not an element of any of the Ai sets, so it is not an element of any intersections thereof. Thus, x is counted exactly once on the right-hand side, as well. Second, suppose x is an element of one (or more) of the Ai sets. This means x is not counted on the left-hand side. To help show that x is also counted zero times on the right-hand side, let's define B $\subseteq$[n] to be the set of indices i for which x $\in$ Ai, i.e. $\f\forall$ i $\in$ B. x $\in$ Ai. We have a few observations to make: Consider the terms of the sum that will not count x. For any S $\subseteq \mathbb{N}$, if S ̸$\subseteq$ B, then x $\notin T i\in S$ Ai. (This is because there is some j $\in S such that j \notin B$, but B is all of the indices for which x $\in$ Ai.) This means x is counted 0 times in the terms of the sum for which S ̸$\subseteq$ B. Next, by a result previously proven, we know that B has an equal number of subsets of odd size as it does of even size. For any such subset T $\subseteq$ B, we know x $\in$ T i$\in$ T Ai. Now, if |T| is even, that term will be positive, so x is counted once; if |T| is odd, that term will be negative, so x is removed from the count once. Since there are an equal number of each of these terms, we see that x is accounted for 0 times by these terms, as well. Overall, we have shown that an arbitrary element is counted the same (and correct) number of times on both sides of the equation, in any case. Sometimes, it happens that all of the intersections of k-many of the Ai sets have the same size. This will be true of some of the examples we see in the next section. When that is the case, many of the terms in the expression above can be combined since they are identical. Specifically, rather than summing over subsets $S \subseteq [n]$ to account for all possible intersections of the sets Ai, we can sum over the number of sets being intersected together, rather than which sets are intersected.


> 🇨🇳 **两个集合** $|U - (A_1 \cup A_2)| = |U| - |A_1| - |A_2| + |A_1 \cap A_2|$。为什么加上交集？因为属于 $A_1 \cap A_2$ 的元素被减了两次（一次在 $|A_1|$ 中、一次在 $|A_2|$ 中），必须加回一次。


8.7. INCLUSION/EXCLUSION


> 🇨🇳 **三个集合** $|U - (A_1 \cup A_2 \cup A_3)| = |U| - |A_1| - |A_2| - |A_3| + |A_1 \cap A_2| + |A_1 \cap A_3| + |A_2 \cap A_3| - |A_1 \cap A_2 \cap A_3|$。模式：减单集、加两两交集、减三重交集——交替加减。


<div class="def-theorem" markdown>
**Corollary 8.7.2. Suppose we have a universal set U, and suppose we have**
</div>
some sets A1, A2,..., An that are all subsets of U. Furthemore, suppose that the intersection of any k of the Ai sets has a fixed size---call it S(k)---independent of which sets are intersected. Then, $|U -(A_1 \cup A_2 \cup \cdots \cup A_n)$| = n X k=0 (-1)k (n k ) S(k)
<div class="def-proof" markdown>
*Proof.* This follows from the result of Theorem 8.7.1 by combining identical
</div>
terms. Specifically, we know there are {n k } sets $S \subseteq [n]$ that satisfy |S| = k. By the assumption of this corollary, all such sets with |S| = k| will yield


> 🇨🇳 **一般公式** $|U - (A_1 \cup A_2 \cup \cdots \cup A_n)| = \sum_{S \subseteq [n]} (-1)^{|S|} |\bigcap_{i \in S} A_i|$，其中空集交集 $\bigcap_{i \in \emptyset} A_i = U$。


$\bigcap_{i \in S} A_i = S(k)$ Combining those terms together, and summing over the possible sizes of S, we obtain the above result. This will be helpful in some examples we work through below!
### 8.7.3 Examples
Example 8.7.3. Bridge hands:
Bridge deals out 13 cards per hand. How many such hands have at least one card from each suit? Recall that with poker hands (i.e. 5 cards) this was easy! We just noticed the suit distribution must follow 1112, i.e. some suit appears twice and the others appear once each. (Look back at Example 8.3.6 for the details of this argument.) With 13 cards, though, it's much harder to write down all of those cases, those partitions of 13 into nonzero terms: (1,1,1,10) and (1,1,2,9) and (1,2,3,7) and so on. There are lots of cases! Let's use Inclusion/Exclusion to be more efficient. Let U be the set of all 13 card hands from a standard deck of 52 cards. Let AH be the set of 13 card hands that don't have any Hearts. Let AS be the set of 13 card hands that don't have any Spades. Let AC be the set of 13 card hands that don't have any Clubs. Let AD be the set of 13 card hands that don't have any Diamonds. Then we seek an expression for, = U - {AH $\cup AS \cup AC \cup A$D }


> 🇨🇳 **理解交替加减** 任取 $x \in U$，设 $x$ 恰好属于 $m$ 个 $A_i$。$x$ 在等式右边被计数的净次数为 $\sum_{j=0}^{m} \binom{m}{j} (-1)^j = (1-1)^m = 0^m$。当 $m \geq 1$ 时结果为 0（$x$ 不应在剩余中），当 $m=0$ 时结果为 1（$x$ 应被计一次）。这与左边一致！


Accounting for all possible intersections, we have, = |U| -|AH| -|AS| -|AC| -|AD| + $|A_H \cap A_S|$ + |AH $\cap A_C$| + |AH $\cap A_D$| + |AS $\cap A_C$| + |AS $\cap A_D$| + |AC $\cap A_D$| -|AH $\cap AS \cap A$C| -$|A_H \cap A_S \cap A_D|$ -|AS $\cap AC \cap A$D| -|AH $\cap AD \cap A$C| + |AH $\cap AS \cap AC \cap A$D| Since there are 4 "bad sets", we need to consider all possible ways they can intersect. However, counting these intersections is actually quite convenient because the sizes of the intersection only depend on how many sets are intersected, not which ones they are. Notice that |AH| = |AS| = |AC| = |AD| = {39


> 🇨🇳 **等价形式** 也可写成 $|A_1 \cup \cdots \cup A_n| = \sum_{j=1}^{n} (-1)^{j+1} \sum_{|S|=j} |\bigcap_{i \in S} A_i|$。这就是"不断扩大并集"的逐步修正法。


}. To have a 13 card hand which avoids one set, we just have to select 13 cards from the other 39. Likewise, notice that $|A_H \cap A_S|$ = {26


> 🇨🇳 **例** 在 100 名学生中，60 人学数学，40 人学物理，20 人学化学，10 人同时学数学和物理，8 人同时学数学和化学，5 人同时学物理和化学，3 人三门都学。至少学一门的学生数：$60+40+20-10-8-5+3=100$。


} because we need to avoid 2 suits. This holds for every intersection of two of these sets. Likewise, notice that $|A_H \cap A_S \cap A_D|$ = {13


> 🇨🇳 **例** 1 到 1000 中不被 2、3、5 任一整除的整数个数：$1000 - \lfloor 1000/2 \rfloor - \lfloor 1000/3 \rfloor - \lfloor 1000/5 \rfloor + \lfloor 1000/6 \rfloor + \lfloor 1000/10 \rfloor + \lfloor 1000/15 \rfloor - \lfloor 1000/30 \rfloor = 1000 - 500 - 333 - 200 + 166 + 100 + 66 - 33 = 266$。


} because we need to avoid 3 suits, so we only have 13 cards to pick from (the 4th suit). This holds for every intersection of three of these sets. Thus, we have, = (52


> 🇨🇳 **用容斥求排列数（错排问题）** $n$ 个元素的错排数（没有任何元素在原位的排列数）：$D_n = n! \sum_{j=0}^{n} \frac{(-1)^j}{j!}$。当 $n \to \infty$ 时 $D_n/n! \to 1/e \approx 0.368$。


) total such hands. (Notice that the last term is 0; how can we have a 13 card hand with no suits represented in it?!) One Lesson: Notice how we chose to define the sets U and Ai in this example. We wanted to count the number of hands with a certain property, so we defined sets of hands that do not have that property, and considered how to remove their counts from a total.
Example 8.7.4. Counting surjections: Count the number of functions f :
[5] $\to$[3]. Count the number that are injections. Count the number that are surjections. Let U be the set of all functions from [5] to [3]. We know |U| = 35 because we have 3 choices of output for each of the 5 elements in the domain. There are no such functions that are injective. If a function f : [5] $\to A$ is injective, then | Imf([5])| = 5, but here, the codomain has size 3. Thus, this is not possible.


> 🇨🇳 **简化情形** 当所有 $k$-交集大小只取决于 $k$（不取决于哪些集合）时：$|U - (A_1 \cup \cdots \cup A_n)| = \sum_{k=0}^{n} (-1)^k \binom{n}{k} |S_1 \cap \cdots \cap S_k|$。这大大简化了计算。


8.7. INCLUSION/EXCLUSION


> 🇨🇳 **例** 1 到 1000 中不被 2、3、5 整除的整数数恰好符合简化情形——因为被 $p_1, \ldots, p_k$ 同时整除的整数数为 $\lfloor \mathbb{N} / (p_1 \cdots p_k) \rfloor$，只取决于 $k$ 个素数的乘积。


Now, let's count the surjections! Let A1 be the set of all such functions with the property that 1 $\notin I$mf([5]). Let A2 be the set of all such functions with the property that 2 $\notin$ Imf([5]). Let A3 be the set of all such functions with the property that 3 $\notin$ Imf([5]). Then we seek an expression for N = |U -(A1 $\cup$ A2 $\cup$ A3)|. We have N = |U| -|A1| -|A2| -|A3| + |A1 $\cap$ A2| + |A1 $\cap$ A3| + |A2 $\cap$ A3| -|A1 $\cap$ A2 $\cap$ A3| Remembering that, generally, the number of functions f : [m] $\to$[n] is nm (n choices of output for each of m inputs), we have N = 35 - (3


> 🇨🇳 **容斥与鸽巢** 容斥原理和鸽巢原理都是计数技术的重要工具，但适用场景不同：鸽巢保证存在性而不给出精确计数，容斥给出精确计数。


) 05 = 35 -3 $\cdot$ 25 + 3 = 243 -96 + 3 = 150
Example 8.7.5. Find the number of natural numbers from 1 to 1000 that are
neither perfect squares, cubes, nor fourth powers. Let U = [1000]. For i $\in${2, 3, 4}, let Ai be the set of elements of U that are perfect i-th powers of some natural number. That is, define Ai = x $\in$ U | $\exists$ b $\in \mathbb{N}$. x = bi Then we seek the number M = |U -(A2 $\cup$ A3 $\cup$ A4)|. Notice that |U| = 1000. Notice that the largest square in U is 312 = 961 (since 322 = 1024). Thus, |A2| = 31. Notice that the largest cube in U is 103 = 1000. Thus, |A3| = 10. Notice that the largest fourth power in U is 54 = 625 (since 64 = 1296). Thus, |A4| = 5. Considering intersections, notice that, for instance, A2 $\cap$ A3 is the set of sixth powers since LCM(2, 3) = 6. (LCM is the Least Common Multiple.) Notice that the largest sixth power in U is 36 = 729 (since 46 = 4096). Thus, |A2 $\cap$ A3| = 3. We already found the largest fourth power in U to be 54, so |A2$\cap$ A4| = |A4| = 5. Notice that the largest 12th power in U is 112 = 1 (since 212 = 4096). Thus, |A3 $\cap$ A4| = 1. This also tells us that |A2 $\cap$ A3 $\cap$ A4| = |A3 $\cap A$4| = 1. Putting this all together, we find N = 1000 -31 -10 -5 + 3 + 5 + 1 -1 = 962


> 🇨🇳 **练习** (1) 1 到 1000 中不被 2 也不被 7 整除的整数有多少？(2) 在 200 名学生中，100 人学数学，80 人学物理，60 人学生物，30 人同时学数学和物理，25 人同时学数学和生物，20 人同时学物理和生物，10 人三门都学。至少学一门的有多少人？


### 8.7.4 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) When is the Principle of Inclusion/Exclusion applicable? (2) What strategy did we use to prove the Principle of Inclusion/Exclusion? (3) Why did we require Ai $\subseteq U$ for each i? Do you think the result still holds if these conditions are not satisfied? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) How many natural numbers less than 100 are not multiples of 2 or 5? (2) How many natural numbers less than 1000 are not perfect powers of 2 or 3 or 5? (3) How many lattice paths go from (0, 0) to (10, 10) without going through (3, 3)? (4) How many lattice paths go from (0, 0) to (10, 10) without going through either (3, 3) or (6, 8)? (5) How many functions f : [6] $\to$[3] are surjections?
## 8.8 Summary We have now developed several basic counting techniques and developed them into even more advanced techniques. We started by simply discussing the Rules of Sum and Product, which were based on results from the previous chapter about the cardinality of finite sets. We were able to use these to develop some fundamental counting objects and describe how to count them. This included the vastly useful binomial coefficients. We derived the formula for binomial coefficients for ourselves, implement a counting strategy. Then, we applied these principles to plenty of examples, to give ourselves practice with working through the nuances of counting arguments: sometimes there are many cases involved,


> 🇨🇳 (3) 求 $\{1,2,\ldots,8\}$ 的错排数 $D_8$。(4) 证明容斥公式的简化情形：当所有 $k$-交集大小只取决于 $k$ 时，公式可简化为 $\sum_{k=0}^{n} (-1)^k \binom{n}{k} c_k$。


sometimes we have to be clever about applying the Rule of Product, sometimes we need to be worried about an over/undercount. On that note, we discussed how to take a proposed argument and demonstrate that it is incorrect. The proof technique of counting in two ways is incredibly important, and you will see it appear in plenty of other mathematical areas. We saw some instructive examples---which were useful theorems in their own right---and have posed many problems of this kind in the exercises to give you sufficient practice. We used the counting in two ways technique to later prove some further results and techniques, including the Binomial Theorem, the formula for selections with repetition. We briefly discussed some more advanced counting techniques, the Pigeonhole Principle and Inclusion/Exclusion. These are considered to be more advanced partly because it can be difficult to see when and how to apply them. By working through some illustrative examples, we hope we have given you a better intuition for how these techniques can be useful, so that you will see when to use them in problem-solving.
## 8.9 Chapter Exercises These problems incorporate all of the material covered in this chapter, as well as any previous material we've seen, and possibly some assumed mathematical knowledge. We don't expect you to work through all of these, of course, but the more you work on, the more you will learn! Remember that you can't truly learn mathematics without doing mathematics. Get your hands dirty working on a problem. Read a few statements and walk around thinking about them. Try to write a proof and show it to a friend, and see if they're convinced. Keep practicing your ability to take your thoughts and write them out in a clear, precise, and logical way. Write a proof and then edit it, to make it better. Most of all, just keep doing mathematics! Short-answer problems, that only require an explanation or stated answer without a rigorous proof, have been marked with a }. Particularly challenging problems have been marked with a $\star$. Problem 8.9.1. In this problem, you will prove the Rule of Product (see
<div class="def-theorem" markdown>
**Theorem 8.2.10).**
</div>
Prove, by induction on n, that the Cartesian product of n finite sets has size equal to the product of the sizes of those sets. Problem 8.9.2. Let n $\in \mathbb{N}$ (with $n \geq 3$) and let S be the set of all binary strings of length n. Each of the following expressions is the size of some subset of S. For each one, identify such a subset and explain why it works.


> 🇨🇳 (5) 1 到 10000 中既不是完全平方数也不是完全立方数的整数有多少？(6) 用容斥原理证明 $n! \geq D_n \geq n!(1-1/e)$。


For example, if I were presented with (n


> 🇨🇳 **证明思路** 容斥公式的核心证明：任取 $x \in U$，设 $x$ 属于恰好 $m$ 个 $A_i$。$x$ 在 $j$-重交集中被计 $\binom{m}{j}$ 次。净计数：$\sum_{j=0}^{m} (-1)^j \binom{m}{j} = (1-1)^m = 0$（若 $m \geq 1$）或 $1$（若 $m=0$）。这与 $x$ 应在剩余中当且仅当 $x$ 不属于任何 $A_i$ 完全一致。


) I would say, Let S1 $\subseteq S$ be the set of all strings with either 3 or 4 or 5 positions that are 0s. We can partition this set into the set of strings with exactly k positions that are 0s, for each k = 3, 4, 5. In each case, we can find the size of that part by selecting k of the n total positions to be 0s, and fixing the rest to be 1s. By ROS, then, we find that |S1| is the sum above. (a) 2n-2 (b) 2n - (n n ) - ( n n -1 ) - ( n n -2 ) - ( n n -3 ) (c) (n


> 🇨🇳 **容斥的直觉："逐步修正"** 可以这样理解：(1) 从 $|U|$ 开始；(2) 减去各 $|A_i|$——多减了交集部分，(3) 加回两两交集——多加了三重交集，(4) 减去三重交集……不断修正，直到所有修正完成。


) (d) ⌊n/2⌋ X k=0 (n k ) Problem 8.9.3. A student organization holds meetings every week, with one chosen leader and two assistants to run the meeting efficiently. If there are 14 weeks in the semester, how many students must be in the organization to guarantee that they can have a different set of leaders and assistants at every meeting? Problem 8.9.4. Say we have 50 pieces of Halloween candy to distribute amongst 4 different children. How many ways can we do this? What if all of the pieces of candy are identical? What if there are 10 pieces each of 5 different kinds? Problem 8.9.5. Let U be the set of all 5-card hands, as dealt from a standard deck of cards, that have exactly two Kings and exactly one Heart. Find |U|. Problem 8.9.6. For each of the following conditions, consider drawing a 7-card hand from a standard deck of cards. (a) How many 7 card hands are there? (b) How many 7 card hands have no cards ranked above 8? (Note: A is the highest rank.) (c) How many 7 card hands have exactly two Kings? (d) How many 7 card hands include contain exactly one pair? (That is, one pair and five other cards of different ranks.)


> 🇨🇳 **应用：欧拉函数** $\phi(n)$（$n$ 以下与 $n$ 互素的正整数个数）可用容斥计算。设 $p_1, \ldots, p_k$ 为 $n$ 的不同素因子，则 $\phi(n) = n \prod_{i=1}^{k} (1 - 1/p_i)$。


(e) How many 7 card hands have at least 3 ♥s? Problem 8.9.7. Find the number of ordered arrangements of 5 distinct digits from {0, 1, 2,..., 9}. Then, find the number of such arrangements that do not place 5 and 6 adjacent to each other. Problem 8.9.8. Let T5,4 be the set of all 5-tuples drawn from the set [4]. (For example, (1, 4, 4, 1, 2) $\in T$5,4.) (a) What is |T5,4|? (b) How many elements of T5,4 have no odd numbers? (c) How many elements of T5,4 have no repeated numbers? (d) How many elements of T5,4 have exactly 2 distinct numbers? (For example, (1, 2, 2, 1, 2) should be counted but (1, 1, 1, 1, 1) should not, and neither should (1, 2, 3, 3, 3).) (e) How many elements of T5,4 have no adjacent identical numbers? (For example, (1, 3, 1, 3, 4) should be counted but (2, 3, 1, 1, 3) should not, and neither should (1, 1, 1, 4, 3).) Problem 8.9.9. For each of the following properties, find the number of ways to roll 5 distinguishable dice so that the property holds. (Don't consider the combination of properties; each one is separate). (a) No even numbers appear on the faces. (b) Exactly 2 even numbers appear on the faces. (c) The sum of all the faces is odd. (d) The numbers on the faces form a "full house". (That is, there are exactly three of one number and exactly two of another.) (e) The numbers on the faces form a "straight". Problem 8.9.10. How many anagrams are there of the word MILLIMETER? How many such anagrams have the two Ms adjacent? How many such anagrams have the Ms non-adjacent? Problem 8.9.11. How many natural numbers between 1 and 1000 (inclusive) have the property that none of the digits are even? How many have the property that no digits are repeated? How many have the property that the sum of the digits is even? (Be careful: Remember that a string like 0011 is really the number 11.) Problem 8.9.12. Consider drawing two cards in order from the top of a deck of cards. How many outcomes are such that the first card is an Ace and the second card is a Heart?


> 🇨🇳 **例** $\phi(60) = \phi(2^2 \cdot 3 \cdot 5) = 60(1-1/2)(1-1/3)(1-1/5) = 60 \cdot 1/2 \cdot 2/3 \cdot 4/5 = 16$。


Problem 8.9.13. How many 15 card hands have at least one card from each rank? Problem 8.9.14. Prove the Binomial Theorem (see Theorem 8.4.8) by induction on n. Problem 8.9.15. Prove that (n k ) 2k = k X i=0 (n i )(n -i k -i ) Problem 8.9.16. Let a, b, k $\in \mathbb{N}$ with $a + b \geq k$. Prove that (a + b k ) = k X i=0 (a i )( b k -i ) Problem 8.9.17. Three men walk into the bathroom and find seven urinals in a row on the wall. In how many ways can the men arrange themselves so that they don't violate the "bro code"? (That is, they must make sure no two adjacent urinals are occupied.) Problem 8.9.18. Let $n \in \mathbb{N}$ be given. Prove the following identities by counting in two ways arguments. (Hint: It's likely that you can use the same "story" or formulation in all parts; that is, try slightly modifying your argument from (a) to prove (b) and (c).) (a) n X i=1 (i -1) = (n


> 🇨🇳 **容斥与概率** 容斥也用于概率论：$P(A_1 \cup \cdots \cup A_n) = \sum_{j=1}^{n} (-1)^{j+1} \sum_{|S|=j} P(\bigcap_{i \in S} A_i)$。这就是"至少一个事件发生"的概率。


) (b) n X i=1 (i -1)(n -i) = (n


> 🇨🇳 **补充** 容斥的本质是"过度计数 $\to$ 修正"的迭代过程。直觉上：先减太多再多补、先加太多再减、交替进行至收敛。


) (c) n X i=1 (i -1


> 🇨🇳 **补充2** 容斥公式对无限集也成立（需测度论），但在组合数学中通常只用于有限集。


) Problem 8.9.19. Prove that n X i=0 (r + i i ) = (r + n + 1 n ) by a counting in two ways argument. Problem 8.9.20. Prove that (n k ) - (n -2 k ) = 2 (n -2 k -1 ) + (n -2 k -2 ) by a counting in two ways argument. Use the exact form given; do not simplify algebraically.


> 🇨🇳 **补充3** 交错和 $\sum (-1)^j \binom{m}{j} = 0$（$m \geq 1$）是整个证明的核心——这是二项式定理在 $x=1,y=-1$ 时的特例。


Problem 8.9.21. Prove that (n k ) - (n -2 k ) = (n -1 k -1 ) + (n -2 k -1 ) by a counting in two ways argument. Use the exact form given; do not simplify algebraically. Problem 8.9.22. Prove that (n k ) - (n -3 k ) = (n -1 k -1 ) + (n -2 k -1 ) + (n -3 k -1 ) by a counting in two ways argument. Use the exact form given; do not simplify algebraically. Problem 8.9.23. Prove that 4n = n X k=0 (n k ) 3k by a counting in two ways argument. Problem 8.9.24. Let p $\in \mathbb{N}$ be prime. Let $k \in \mathbb{N}$ be given with 1 $\leq$ k < p. Prove that {p k } is divisible by p. Problem 8.9.25. Let p $\in \mathbb{N}$ be prime. Use the previous Problem 8.9.24 to prove that $\f\forall$ x, y $\in \mathbb{Z}$. (x + y)p \equivxp + yp mod p (Look back at Problem 6.7.22 where we investigated this before. You just proved it in generality!) Problem 8.9.26. Let p $\in \mathbb{N}$ be prime, and let a $\in \mathbb{Z}$. Use the result of Problem
### 8.9.24 and the Binomial Theorem to prove that
ap $\equiv$a mod p This result is known as Fermat's Little Theorem. Problem 8.9.27. Prove the Summation Identity (see Theorem 8.4.5) by a counting in two ways argument that considers lattice paths. Specifically, we suggest partitioning the set of lattice paths from (0, 0) to (k + 1, n -k) based on where the first Rightwards step occurs. Problem 8.9.28. In this problem, you will prove the following summation formula that you've proved by induction before! $\f\forall$ n $\in \mathbb{N}$. n X k=1 k3 = (n(n + 1)


> 🇨🇳 **补充4** 错排 $D_n = n!(1 - 1 + 1/2! - 1/3! + \cdots + (-1)^n/n!)$ 是容斥最经典的应用之一。


)2 (a) Let $k \in \mathbb{N}$ be given. Prove the following equality by a counting in two ways argument: $\f\forall k \in \mathbb{N}$. k3 = 6 (k


> 🇨🇳 **补充5** 在编程竞赛中，容斥公式常用于"至少满足一个条件"的计数——将"恰好的"分解为"至少"的交错和。


) (Hint: Consider counting words of length 3 from an alphabet of k letters.)


> 🇨🇳 **补充6** 容斥与莫比乌斯反演有深层联系，在数论和组合数学中有更高级的应用。


(b) Use the Summation Identity and the equality you just proved in (a) to prove the claim given above in the problem statement! Bonus Can you generalize this method to find a formula for P k4? Problem 8.9.29. Let $n \in \mathbb{N}$ be given. How many lattice paths go from (0, 0) to (3n, 3n) without going through either of (n, n) or (2n, 2n)? Problem 8.9.30. Let $n \in \mathbb{N}$ be given. Suppose we have n CMU students and n Pitt students. (Assume, of course, that nobody attends both schools, so these two sets of n students are disjoint.) (a) How many ways can we split these 2n students into n pairs? (Note: There should be no ordering to the pairs, nor the people within the pairs.) (b) How many ways can we split these 2n students into n pairs, where each pair must contain one CMU student and one Pitt student? (Again, there is no order amongst or within the pairs.) Problem 8.9.31. Let n $\in \mathbb{N}, and let S \subseteq \mathbb{N}$ be of size |S| = n + 1. Prove that $\exists x, y \in S$ such that x $\neq$ y and x -y is a multiple of n. Problem 8.9.32. Consider the set [22]. Let S $\subseteq$[22] be given such that |S| = 7. Here, you will prove that there must exist two disjoint, non-empty subsets X, Y $\subseteq$ S whose elements have the same sum. 1. How many non-empty subsets of S are there? 2. Let T $\subseteq$ S be given. What is the minimum possible value of the sum of the elements of T? What is the maximum possible value? 3. Use (a) and (b) to deduce that there are two sets X, Y $\subseteq$ S whose elements have the same sum. 4. Explain, further, that you can make X and Y be disjoint. Problem 8.9.33. Consider an equilateral triangle with side length 1 cm. Suppose 10 points have been placed inside the triangle (and not on the boundary). Prove that there must be two points separated by a distance d that is less than 1 3 cm. Problem 8.9.34. Let $n \in \mathbb{N}$ be given. Prove the following identity by a counting in two ways argument: (2n n ) = n X k=0 (n k )2 Problem 8.9.35. Let $n \in \mathbb{N}$ be given. Consider the following identity: 4n = n X k=0 (n k ) 2n Deduce it from the Binomial Theorem. Then, prove it by a counting in two ways argument.


> 🇨🇳 **补充7** 计算容斥公式的复杂度：$n$ 个集合需要 $2^n - 1$ 项，所以当 $n$ 很大时计算量惊人。这是简化情形特别重要的原因。


Problem 8.9.36. Let $n, k \in \mathbb{N}$ be given. Consider Equation \star: X i$\in$[k] xi = x1 + x2 + $\cdots$ + xk = n In this problem, we will discuss solutions to \star, where a solution is an assignment of values for x1, x2,..., xk such that their sum is n and such that each one satisfies $x_i \in \mathbb{N} \cup \{0\}$. (a) How many solutions to \starexist? (b) How many solutions to \staralso satisfy x1 $\geq$3? (c) How many solutions to \staralso satisfy $\f\forall$ i $\in$[k]. xi $\geq$2? (d) How many solutions to \staralso satisfy x1 $\leq$4? (e) Consider the following modification to \star: x1 + x2 + $\cdots$ + xk $\leq$ n How many solutions to this inequality exist? (Again, a solution requires $x_i \in \mathbb{N} \cup \{0\}$.) Problem 8.9.37. Suppose we have 10 pirates who need to divvy up 100 pieces of gold. Suppose Captains Redbeard and Blackbeard are among the 10 pirates. (a) How many ways are there to divvy the gold so that Redbeard gets at least 5 pieces of gold but Blackbeard gets at most 5 pieces? (b) How many ways are there to divvy the gold so that Redbeard gets at least 10 pieces of gold but Blackbeard gets somewhere between 5 and 15 (inclusive) pieces of gold? (c) How many ways are there to divvy the gold so that Redbeard gets somewhere between 0 and 10 (inclusive) pieces of gold and Blackbeard gets somewhere between 10 and 20 (inclusive) pieces of gold? (Hint: Use Inclusion/Exclusion.)
## 8.10 Lookahead There isn't much to look ahead for, at this point! At least, there isn't anything else in this book. We hope this has only served to whet your appetite for mathematical knowledge and problem-solving. Think about where we started: we were doing nothing more than posing fun puzzles and trying to solve them by applying our current knowledge and logical techniques. In reality, that's all we are doing now, as well! It's just that we have developed so much mathematical


> 🇨🇳 **补充8** 在统计物理中，容斥用于计算"至少一个粒子在某状态"的概率——与"生日问题"有关。


terminology and so many results and so many problem-solving skills that we are able to approach and discuss far more advanced problems. Did you think, when you started reading this book, that you would be solving problems like this? Do you feel like you have a better understanding, an appreciation, of what mathematicians work on and how they approach the world? We hope so!, We have also developed several essential skills that are applicable in life outside of mathematics, as well. It's likely that you won't encounter formal symbolic logic in your daily life, but you will certainly have to process complicated statements with conjunctions and disjunctions and conditionals. We do this on a daily basis, as human beings who converse with one another and convey complex thought processes. By working through some of the foundational aspects of formal logic, we are all better now at analyzing complicated statements and assessing their truth, as well as being able to write down or otherwise share our own thoughts. Likewise, you might not face formal statements of combinatorial identities in your daily life, but our work with counting in two ways proofs will help your anlytical thinking skills. We had to sometimes be creative about how to develop a "story" to describe a set of elements to be counted in two ways. This required some creativity and ingenuity, and exercising those brain muscles can only be helpful. Furthermore, the practice of reading a proposed "proof" and analyzing whether or not it is, in fact, an over/undercount has made us better at understanding and critiquing the arguments of others. Surely, this is something you do on a daily basis, but perhaps not in mathematical terms. Overall, we have developed an ability to think in a mathematical way. We have learned: how to read and understand a problem; how to approach a problem from several angles, and be willing to pursue potential dead ends to further our understanding; how to identify common structures that underlie different problems and exploit these similarities with certain techniques; and ultimately, how to take everything we have figured out about a problem and formulate our ideas into a written, presentable argument to be read by others. This entire process will make us all not only better problem-solvers, but better communicators. In a rapidly-changing world where communication is more and more important (as it becomes easier and easier to connect to other people quickly), the ability to share our thoughts effectively, correctly, and clearly is an essential life skill. But by all means, don't let this be the end of our mathematical journey! Go forth and prosper, and spread your knowledge and joy of mathematics. Work on these problems and more with other people. Seek out the areas of mathematics that inspire you. See if you can use these concepts to solve a real-world problem you're facing. Most of all, just get out there and do mathematics.


> 🇨🇳 **补充9** 总结：容斥是"减多加少再减再加"的计数策略，与鸽巢的"存在性保证"互为补充。


