---
title: Pigeonhole Principle
---

# Pigeonhole Principle

This is very informal, of course, but it should help you see where it might come in handy. The Pigeonhole Principple is useful, for instance, when we have a bunch of objects that fall into a certain number of categories. If we know how many objects we have, and how many possible categories there are, then we can guarantee the existence of some category that has at least some certain number of objects in it.
Example 8.6.1. Here is a canonical example of the principle being applied:
Of any 3 people, two must have the same sex. Notice that this doesn't say which sex is represented at least twice. It just guarantees the existence of such a category. To convince yourself of this fact, you could enumerate the possibilities (where M means a male, and F means a female): MMM, MMF, MFF, FFF. In each case, at least one of the sexes appears twice (or more). Here's a logically equivalent version of the above statement: If we flip 3 coins, at least two must show the same face. Here's a similar statement to the ones above: If we roll 7 dice, at least two must show the same number. Are you beginning to see the general idea? Here's one more version of these claims, and a transition to the next part, where we state and prove a generalized version. If we have n + 1 pieces of paper to stuffinto n different drawers, some drawer will end up getting at least 2 pieces of paper. This is, by the way, the etymological derivation of "pigeonhole": it's a term for the drawers you'd find on an old-fashioned rolltop desk. We'd rather not think about manhandling gentle creatures into tiny boxes!
### 8.6.2 Statement and Proof There are two versions of this principle, so we'll state and prove them both. The first version is how we'll be using it in combinatorial problems.
<div class="def-theorem" markdown>
**Theorem 8.6.2 (Pigeonhole Principle). (1) If a set S with |S| = n is parti-**
</div>
tioned into k disjoint subsets whose union is S, and if k < n, then at least one of the subsets in the partition has more than one element. Furthermore, that part actually has at least ⌈n k ⌉elements. (That is, if we separate n objects into k piles, there must be one pile with at least n k objects in it.)


> 🇨🇳 鸽巢原理（Pigeonhole Principle）很非形式化，但能帮你看到它的用处。鸽巢原理在有若干对象分属若干类别时特别有用：若知道对象总数和类别数，就能保证存在某个类至少包含一定数量的对象。

**例 8.6.1** 典型应用：任意 3 人中必有两人的性别相同——注意不说哪种性别出现至少两次，只保证这样的类别存在。枚举验证：MMM、MMF、MFF、FFF，每种情况至少一个性别出现两次（或更多）。等价说法：掷 3 枚硬币，至少两面相同。类似说法：掷 7 枚骰子，至少两面相同。更一般地说：若将 $n+1$ 张纸放入 $n$ 个抽屉，某个抽屉至少有 2 张。"pigeonhole"就是老式翻盖桌上那些小格的名称。

**8.6.2 陈述与证明** 鸽巢原理有两个版本。

**(1)** 若集合 $S$（$|S|=n$）被划分为 $k$ 个不相交子集且并集为 $S$，若 $k < n$，则至少一个子集有多于一个元素，实际上至少有 $\lceil n/k \rceil$ 个元素。

**(2)** 若 $x_1, x_2, \ldots, x_n$ 为实数且 $\sum_{i=1}^{n} x_i \geq z$，则存在某个 $i$ 使 $x_i \geq z/n$。（即 $n$ 个实数中必有一个不小于平均值。）

**证明** (1) 反证：设每个 $|S_i| < n/k$，则 $n = |S| = \sum_{i=1}^{k} |S_i| < \sum_{i=1}^{k} n/k = n$，矛盾！(2) 反证：设所有 $x_i < z/n$，则 $z = \sum x_i < \sum z/n = z$，矛盾！两个证明代数上完全相同，体现了同一个底层思想。


(2) If x1, x2,..., xn are real numbers with the property that Pn i=1 xi $\geq z$, then there is at least one index i such that xi $\geq z$ n. (That is, if we have n real numbers, there must be one number that is at least as large as the average).
<div class="def-proof" markdown>
*Proof.* AFSOC k < n and S is partitioned into S1,..., Sk that also satisfy
</div>
|Si| < n k for every i. Since the sets form a partition of S, we have n = |S| = k X i=1 |Si| $< k X i=1 n k = n so n < n. This is a contradiction! \times\times\times\times AFSOC all of the numbers xi satisfy xi < z n. Then, z = n X i=1 xi < n X i=1 z n = n \cdot z n = z so z < z. This is a contradiction. \times\times\times\times \mathbb{N}otice how similar these proofs are! They look identical, algebraically. Indeed, they represent the same underlying idea.$
### 8.6.3 Examples
Let's dive right in and see how to use the Pigeonhole Principle in combinatorics problems. We'll show you how it works with some practice examples. In general, the hardest part about using the Pigeonhole Principle is in deciding what the "pigeonholes" actually are!
Example 8.6.3. Of 8 people, there must be two whose birthdays are on the same
day of the week this year. Also, of 13 people, there must be two whose birthdays are in the same month. For the first claim, we can take our "pigeonholes" to be the 7 days of the week. Taking 8 people and partitioning them based on the day of the week their birthday occurs on this year, we find there are 8 objects going into 7 parts. Thus, one part has at least 8 7 objects in it. Since we are working with whole objects, this actually means some part has at least 2 objects in it. A similar argument applies for the second claim. We just use the 12 months of the years as our "pigeonholes".
Example 8.6.4. In New York City, there are at least 8 people with the exact
same number of hairs on their head. This follows from knowing a couple of facts. First, scientists estimate that there are between 100000 and 150000 hairs on the human head. Let's be conservative and widen that range to 0 to 1 million. Second, New York City has about 8


> 🇨🇳 百万人口。将"鸽洞"定义为头发数 0 到 100 万，8 百万人分入 100 万+1 个洞，由鸽巢原理得某个洞至少有 8 人。


million people. By defining our "pigeonholes" to be the numbers 0 to 1 million (based on how many hairs are on each person's head), we get the result. (In fact, this argument might not be necessary. I bet we could walk around the city and find 8 bald people pretty quickly!)
Example 8.6.5. Look back at Section 1.4.4 where we investigated finding a group
of mutual friends amongst a larger group. In that problem's solution, we actually used the Pigeonhole Principle! We had 5 objects that were arbitrarily separated into 2 categories. This let us deduce that some category had at least 3 of the objects.
Example 8.6.6. Suppose n golfers (n $\geq$2) compete in a match play tournament,
round robin style. How many matches are played? After those matches, must there exist two golfers with the exact same number of wins and losses? If not, can you impose conditions that guarantee that? Using a counting argument, we find that n(n-1)


> 🇨🇳 (为什么？你能补全细节吗？试试！)然而，我们无法保证两人战绩相同。例如 $n=3$ 时，选手 1 两战皆负，选手 2 胜 1 负 1，选手 3 两战皆胜，记录各不相同。但如果限制无人全胜，则可保证两人战绩相同。每人打 n-1 场，无人 n-1 胜，可能胜场数为 $0, 1, \ldots, n-2$ 共 n-1 种，而选手有 $n$ 人，由鸽巢原理必有两人胜场相同！


matches are played. (Why? Can you fill in the details? Try it!) However, we can't guarantee two people with the same record. For instance, suppose n = 3 and that Player 1 lost to both others, Player 2 beat Player 1 but lost to Player 3, and that Player 3 beat both others. This yields records of 0-2 and 1-1 and 2-0, respectively, and we see that none are the same. Now, if we impose the condition that no one is undefeated, then we can guarantee two players have the same record. Each player plays n -1 matches (one match against everyone except themself). Since no one is undefeated, no one has n-1 wins. Thus, the possible number of wins for each player is 0 or 1 or 2 or... or n -2. There are n -1 options there. By the Pigeonhole Principle, amongst n players, there must be two of these win counts repeated!
Example 8.6.7. Proposed claim: "Amongst any set of m distinct natural
numbers, there are at least two such numbers whose sum or difference is a multiple of 10." Find the smallest value of m such that this claim is valid. By trying out some small cases, we can see that m $\leq$6 will not work. Even with m = 6, we can pick the set of numbers {1, 2, 3, 4, 5, 10}. Notice that no two of them have a sum/difference that is a multiple of 10. (Note: We aren't allowed to trivially pick the same number twice, like 5 -5 = 0 or 5 + 5 = 10, to get a multiple of 10.) Might m = 7 be the number we are looking for? Let's try to prove it! Suppose we have an arbitrary set of 7 natural numbers. Let's assign them to the Pigeonhole Boxes that are categorized by their last digit (that is, place each number n in a box based on the smallest positive value of x satisfying x $\equiv$n mod 10) as follows: {1, 9}, {2, 8}, {3, 7}, {4, 6}, {5}, {0}. That is, we have 6 boxes.


> 🇨🇳 这样我们有 6 个盒子。


Since we have 7 numbers, then some box has two numbers. That means those numbers either have last digits that sum to 0 modulo 10 (for example 2 and 8 or 5 and 5), or else those numbers have the same last digit so their difference is 0 modulo 10. Either way, we have a sum or difference that is 0 modulo 10, i.e. a multiple of 10.
### 8.6.4 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What are the two versions of the Pigeonhole Principle? (2) What proof technique did we use to prove the Pigeonhole Principle? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Suppose there are 5 professors in the math department. Every year, 2 are chosen to teach Concepts of Math. How many years can the department go without repeating the same selection of 2 professors? Prove this is optimal by exhibiting such a sequence of that length, as well as invoking the Pigeonhole Principle to show that any longer sequence necessarily uses a pairing more than once. (2) Let $n \in \mathbb{N}$ and consider the set [2n]. Suppose we have a set S \subseteq[2n] of size |S| = n + 1. Prove that there must be two elements x, y $\in S that are relatively prime. (3) Suppose we have a square park with dimensions 1 km \times 1 km. We want to build a golf course on the park, but we only have space for 5 holes. In particular, for safety reasons, we need to consider the distance between the locations of the actual cups (the holes in the ground). Prove that no matter how we place 5 holes, there must exist two holes that are separated by a distance d that satisfies d \leq \sqrt$


> 🇨🇳 $\frac{\sqrt{2}}{2}$


2 km. (Note: We are allowed to place a hole on the boundary of the park.) Next, prove that this bound is optimal; that is, exhibit a way to place 5


> 🇨🇳 $\frac{\sqrt{2}}{2}$


8.7. INCLUSION/EXCLUSION


> 🇨🇳 千米。接下来证明此界限是最优的——即给出一种放置 5 个洞的方法使任两洞距离不小于


$holes on the park grounds (again, the boundary is allowed) such that the distance between any two holes is greater than or equal to \sqrt$


> 🇨🇳 $\frac{\sqrt{2}}{2}$


2 km.
## 8.7 Inclusion/Exclusion
### 8.7.1 Motivation The Principle of Inclusion/Exclusion is a handy result that helps figure out how to remove sets from a large one and count the elements leftover. We have already seen this in action in a simple form. If we have A $\subseteq U$, and we want to find |U -A|, we can just count |U| and |A| and subtract them. This follows from the Rule of Sum, applied to the partition {A, U -A} of the set U. What happens if we remove two sets from a larger one? What if they overlap somehow? Do we have to account for that? What if we remove three sets? Or four sets? Or n sets? Can we write an expression for the number of elements leftover that holds, in generality? Can we use it to solve counting problems? Here are some expressions that describe what is going for "small cases". Suppose we have a universal set U and some subsets A1, A2,..., An \subseteq U. We want to count the elements of U that are outside of all of the Ai sets. We can do this by writing: |U -A1| = |U| -|A1| |U -(A1 \cup A)2)| = |U| -|A1| -|A2| + |A1 \cap A2| |U -(A1 \cup A2 \cup A3)| = |U| -|A1| -|A2| -|A3| + |A1 \cap A2| + |A1 \cap A3| + |A2 \cap A3| -|A1 \cap A2 \cap A3| Do you see why these work? Try thinking of an element x \in U and considering how many of the Ai sets it belongs to. Where will this element get counted in the expressions on the left- and right-hand sides? Is it counted the appropriate number of times on both sides? Can you see how to generalize this idea? It might help to think of these expressions as "guessing" at a correct count and then continually "fixing" to adjust for over/undercounting. For instance, we could derive the last expression above as follows: Let's find |U -(A1 \cup A2 $\cup A$3)|. Let's take the number of elements in U and remove the number of elements in the sets A1, A2, A3. Oh, shucks! What about the elements that belong to two of the sets. We have now removed those from our count too many times, so we should add back the number of elements that belong to the intersection of two sets. Oh, shucks! What about the elements that belong to all three sets. We have now added those back in too many times, so we need to remove them again. You might see now how to generalize these expressions, and prove them, for any number of sets. That is what we will do in the next section.


> 🇨🇳 **8.7 容斥原理（Inclusion/Exclusion）**

**8.7.1 动机** 容斥原理帮助我们从一个大的集合中去除子集后清点剩余元素。简单形式我们已见过：若 $A \subseteq U$，则 $|U-A| = |U| - |A|$。若去除两个集合呢？如果它们有重叠怎么办？三个？$n$ 个？能否写出一般表达式？

以下是小情形的表达式。设全域 $U$ 和子集 $A_1, A_2, \ldots, A_n \subseteq U$，要计 $U$ 中不属于所有 $A_i$ 的元素：
- $|U-A_1| = |U| - |A_1|$
- $|U-(A_1 \cup A_2)| = |U| - |A_1| - |A_2| + |A_1 \cap A_2|$
- $|U-(A_1 \cup A_2 \cup A_3)| = |U| - |A_1| - |A_2| - |A_3| + |A_1 \cap A_2| + |A_1 \cap A_3| + |A_2 \cap A_3| - |A_1 \cap A_2 \cap A_3|$

理解方式：任取 $x \in U$，考虑 $x$ 属于几个 $A_i$——在等式两边各被计了几次？是否被恰当地计数？也可将表达式理解为"先猜一个计数，然后不断修正"：先取 $|U|$ 减去各 $|A_i|$——哎，属于两个集合的元素被多减了一次，要加回来——哎，属于三个集合的元素又被多加了一次，要再减去……这就是下一节要推广和证明的。


