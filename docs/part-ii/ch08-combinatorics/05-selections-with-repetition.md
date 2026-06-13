---
title: Selections with Repetition
tags:
  - 组合数学
  - 计数
  - 鸽巢原理
  - 容斥原理
---

# Selections with Repetition

Try it! Then, read the next section for our formula and proof.
### 8.5.2 Formula We will derive a formula for the number of selections with repetition by considering the Pirates & Gold example. First, let's explain why this is like selection with repetition: Pretend that we are the gold distributor in this scenario. We are sitting at a table with k pirates seated around us and a bag full of n gold coins at our side. We can choose how to distribute the coins by passing them out one by one. When we choose to give a gold coin to Pirate #i (for some $i \in [n]$), we are selecting that pirate from amongst the k different types of pirate. Ultimately, to pass out n pieces of gold, we need to make n selections. Thus, we are selecting n objects from k types, overall, and we are allowed to repeatedly select a type. Derivation Think of having our n coins laid out on the table, all in a row. To distribute them amongst the k pirates, we need to lay down "dividers" or "bars" that separate the gold pieces into k piles. Then, Pirate 1 will take the pile on the left, Pirate 2 will take the next pile, etc. This "dividers" argument allows us to count the number of ways to complete this process conveniently! To assign the n pieces of gold to k distinct pirates, we need to have n coins separated by k -1 dividers. Think about why we only need k -1 dividers here. It's easy to see why we only need 1 divider to split a row of coins into 2 piles. Then, we can see that 2 dividers split them into 3 piles. In general, once we have already laid down k -1 dividers, there are k piles established; we don't need to lay down a final divider at the end of the row to represent that the rightmost pile goes to Pirate #k.
Example 8.5.3. For example, with k = 3 and n = 7, we might have a distribution
like this: $\circ$ | $\circ$ $\circ$ $\circ$ $\circ$ | $\circ$ $\circ$ In this case, Pirate #1 receives 1 gold, Pirate #2 receives 4 gold, and Pirate #3 receives 2 gold. Notice that this is different from the following outcome: $\circ$ $\circ$ $\circ$ $\circ$ | $\circ$ $\circ$ | $\circ$ In this case, Pirate #1 receives 4 gold, Pirate #2 receives 2 gold, and Pirate #3 receives 1 gold. We could also have some pirates receive 0 gold: $\circ$ $\circ$ $\circ$ $\circ$ $\circ$ | $\circ$ $\circ$ | Here, Pirate #1 receives 5 gold, Pirate #2 receives 2 gold, and Pirate #3 receives 0 gold.


> 🇨🇳 可重复选取（Selections with Repetition）本节讨论允许重复的选取问题——即从 $[n]$ 中选 $k$ 个元素，元素可以重复出现。这与不允许重复的组合不同。


What do these observations tell us? Well, this means that any assignment of the gold pieces corresponds to a string of length n + k -1 with exactly n coins and exactly k -1 dividers. There is a bijection between the sets of these two objects: gold distributions and divider placements. Given a gold distribution scheme, we can construct the corresponding divider arrangement. (For instance, if we were told Pirate 1 is to receive 5 gold, Pirate 2 is to receive 2 gold, and Pirate 3 is to receive 0 gold, we would construct the divider arrangement in the last example above.) Likewise, given a divider arrangement, we can read it off and determine what gold distribution scheme it corresponds to. This bijection tells us that to count the number of ways to distribute the gold, we just need to count the number of possible divider arrangements there are. We can count these quite easily! A divider arrangements is just a string of length n + k -1 with exactly k -1 dividers. This is because we need n gold and k -1 dividers, so n + k -1 positions, in total. Thus, by the definition of selection, there are (n + k -1 k -1 ) ways to construct such an arragement! (You might have also heard of this argument as "Stars and Bars". This is just another common interpretation of this problem, where the gold pieces are replaced with Stars and the dividers are replaced with Bars.) Because of that bijection between the set of such arrangements and the set of gold assignments, we conclude that {n+k-1 n } is the number of ways we can distribute the gold! We already know that {n k } = binn -k, in general, so we could apply that here and deduce that the number of gold assignments is also (n + k -1 n ) But we could already have seen this in our derivation. We need to construct a string of length n+k -1 with k -1 dividers (and the remaining positions being gold pieces). Equivalently, we need a string of that length with n gold pieces (and the remaining positions being dividers).
### 8.5.3 Equivalent Forms Before moving on to solve some problems with this new formula, let's consider some equivalent formulations of a fundamental selections with repetition problem. Whenever you face a problem that involves these concepts or formulations, you might consider applying the formual we just derived, somehow.


> 🇨🇳 **问题设定** 从 $[n]$ 中选 $k$ 个元素的无序列表，其中元素可重复。等价地，这对应于将 $k$ 个不可辨的球放入 $n$ 个可辨的盒子中。也等价于 $n$ 元字母表上长度为 $k$ 的"单词"但字母顺序无关。


Pirates & Gold This is the original formulation we used to derive the formula, so certainly it is applicable in a context like this. In general, all we need to know is the number of pirates and the number of gold pieces. The number of ways to distribute n identical pieces of gold amongst k distinguishable pirates is (n + k -1 k -1 ). Implicit in our derivation, mind you, is that pirates could conceivably receive 0 gold pieces, so keep that in mind. Some problems might ask you to consider other conditions on the distributions. For example, what if every pirates must receive at least one piece of gold? Integer Sums Consider reformulating the Pirates & Gold problem as follows. Let's define $x_i \in \mathbb{N} \cup \{0\}$ to be the number of gold pieces that Pirate #i receives in the distribution. The conditions of the problem require that $\forall i \in[k]. xi \in \mathbb{N} \cup \{0\}$ and that k X i=1 xi = x1 + x2 + x3 + $\cdots$ + xk = n Aha! What if we had asked about the number of solutions to such an equation? This corresponds exactly (in a bijective manner) with the ways to solve the Pirates & Gold problem. Given a solution to this equation, we just give Pirate #i exactly xi pieces of gold. This gives us a different way of stating the problem: The number of solutions to the equation x1 +x2 + $\cdots$ +xk = n that satisfy the condition $\forall$ i $\in$[k]. $x_i \in \mathbb{N} \cup \{0\}$ is (n + k -1 k -1 ). Balls and Bins What if we were given n identical balls, and we were asked to place them in k different bins. (The bins are distinguishable, so let's say they are labeled from 1 to k.) How many ways can we do this? This is easy to relate to the previous formulation! Let $x_i \in \mathbb{N} \cup \{0\}$ be the number of balls that end up in Bin #i. Then the same exact conditions as the problem above apply here.


> 🇨🇳 **可重复选取数** 从 $[n]$ 中可重复地选 $k$ 个的方法数为 $\binom{k+n-1}{k}$。这就是"星与条（Stars and Bars）"方法的结果：将 k 个星（物品）和 n-1 个条（分隔符）排列，总位置数 k+n-1，选 $k$ 个放星。


The number of ways to distribute n identical balls into k distinguishable bins is (n + k -1 k -1 ). Indistinguishable Dice Consider rolling n identical dice. How many outcomes are there? This is not the same as rolling distinguishable dice (where the dice are different colors, for example.) Instead, an outcome of this process is an unordered list of the numbers that are showing on the faces. For example, if we rolled 3 indistinguishable 6-sided dice, an outcome of that process might be the unordered list (1, 3, 3). To think about this, pretend your friend went into another room and rolled 3 dice, then came back and told you what happened. If he says "I rolled a 1 and two 3s", then you didn't learn about which dice showed which number. (Contrast this with the case where he says "I rolled a 1 on the first die and then a 3 on each of the second and third dice.") By asking about the number of outcomes of indistiguishable dice, we are essentially asking about how many possible responses your friend could give you that do not indicate anything about the order in which the rolls appeared. We can relate this to the "Balls and Bins" formulation by rolling all the dice and placing them into 6 numbered boxes based on what the faces show. Equivalently, to characterize an outcome of this process, we need to know how many dice showed 1, how many showed 2, etc. We don't care (nor could we know!) which dice showed which numbers; we only need to know how many showed each number. The number of outcomes of rolling n indistinguishable k-sided dice is (n + k -1 k -1 ).
### 8.5.4 Examples
Let's practice using this newly-derived formula to solve some problems! We'll examine a couple of different formulations of the fundamental result, in the process.
Example 8.5.4. Let's say we have n = 20 pieces of gold to distribute amongst
k = 3 pirates. Let's say the pirates are Captain Redbeard (Khair ad Din, an Ottoman), Captain Blackbeard (Edward Teach, an Englishman), and Captain Kidd (a Scotsman). Let's figure out how many ways there are to distribute the gold under certain conditions:


> 🇨🇳 **例** 从 3 种口味的冰淇淋中选 5 勺（可重复），有多少种方法？$\binom{5+3-1}{5} = \binom{7}{5} = 21$。


(1) How many ways are there total? This is like selecting 20 objects from 3 types, with repetition allowed. Whenever we select a pirate, that means we give him a piece of gold. By the above selection formula, there are (20 + 3 -1


> 🇨🇳 **证明星与条方法** 设 $x_i$ 为第 $i$ 种选的个数（$x_i \geq 0$）。问题等价于求 $x_1 + x_2 + \cdots + x_n = k$ 的非负整数解个数。令 $y_i = x_i + 1$（保证 $y_i \geq 1$），则 $y_1 + \cdots + y_n = k + n$，求正整数解个数——即在 k+n 个位置的 n-1 个间隔中放置隔板：$\binom{k+n-1}{n-1} = \binom{k+n-1}{k}$。


= 231 ways to do this. (2) How many ways ensure every pirate gets at least 2 pieces? Let's just give everyone two pieces of gold right away. Then, we have 20-6 = 14 pieces of gold left to distribute amongst all 3 pirates, so there are (14 + 2


> 🇨🇳 **例** 求 $x + y + z = 10$ 的非负整数解个数：$\binom{10+3-1}{10} = \binom{12}{10} = 66$。


= 120 ways to do this. Think about why this works. We are essentially re-defining what "getting 0 gold pieces" means. Instead of starting with 20 pieces and worrying about whether or not everyone gets at least two pieces, we can just ensure that condition is met right away, and then distribute what's left over. (3) How many ways ensure Redbeard and Blackbeard get at least 2 and Kidd gets at least 6? Just like the last one, let's give Redbear and Blackbeard 2 pieces each, and let's give Kidd 6 pieces. This leaves us with 20 -4 -6 = 10 pieces left to distribute amongst all 3 pirates, so there are (10 + 2


> 🇨🇳 **例** 求 $x + y + z = 10$ 的正整数解个数（$x,y,z \geq 1$）：$\binom{10-1}{3-1} = \binom{9}{2} = 36$。


= 66 ways to do this. (4) How many ways ensure Redbeard and Blackbeard get at least 2 while Kidd gets no more than 2? There are a couple of ways to approach this one. (i) Let's establish cases based on whether Kidd gets 0 or 1 or 2 golds. In each case, we will give Redbeard and Blackbeard 2 pieceseach right away, and then give Kidd the corresponding amount (0 or 1 or 2). This leaves us with 16 or 15 or 14 pieces left to distribute only amongst the first two pirates, so there are (16 + 1


> 🇨🇳 **与排列和组合的关系** 总结四种选择方式：
- 排列（有序不重复）：$\frac{n!}{(n-k)!}$
- 组合（无序不重复）：$\binom{n}{k}$
- 可重复排列（有序可重复）：$n^k$
- 可重复组合（无序可重复）：$\binom{k+n-1}{k}$


) = 17 + 16 + 15 = 48


> 🇨🇳 区分的关键在于"是否有序"和"是否允许重复"。四种组合对应四种不同的计数公式。


(ii) Let's consider all of the ways to ensure Redbeard and Blackbeard get at least 2 golds each, and then remove from this the number of ways where Kidd gets too many, i.e. at least 3 golds. If we give Red/Blackbeard 2 golds each, then we have 16 pieces left to distribute amongst all 3 of the pirates, so there are (16 + 2


> 🇨🇳 **例** 骰子掷 3 次得到的有序结果是可重复排列（$6^3=216$）；掷 3 次后忽略顺序的结果是可重复组合（$\binom{3+6-1}{3}=56$）。


= 153 ways to do this step. Then, if we give Red/Blackbeard 2 golds each and give Kidd 3 pieces and then distribute the remaining 13 amongst all 3 of the pirates, there are (13 + 2


> 🇨🇳 **例** 从 10 人中选 3 人组委员会（无序不重复）：$\binom{10}{3}=120$。将 10 个不同奖品分给 3 个人每人一个（有序不重复）：$\frac{10!}{7!}=720$。


= 105 ways to do this step. We want to remove these possiblities from the previous count. Thus, in total, there are (18


> 🇨🇳 **边界情形** 当 $k=0$：可重复选取数为 $\binom{n-1}{0}=1$（空选）。当 $n=1$：只有一种元素可选，结果为 1。当 $k < n$ 但 $n$ 很大时，公式仍然有效。


) = 153 -105 = 48 ways to give Redbeard and Blackbeard at least two each, but give Kidd no more than 2. (Look, we get the same answer both ways!)
Example 8.5.5. Consider the following equation:
x1 + x2 + x3 + x4 + x5 = 25 Let's identify the number of solutions to this equation where each variable xi is a non-negative integer. We'll impose certain conditions and count the number of solutions that satisfy them. (1) How many solutions are there total? Applying the formula we derived, we see there are (25 + (5 -1) 5 -1 ) = (29


> 🇨🇳 **例** 有一道甜点自助餐，有 8 种蛋糕。选 4 块蛋糕（可重复选同一种），有多少种方式？$\binom{4+8-1}{4} = \binom{11}{4} = 330$。


) (2) How many solutions satisfy x1 $\geq$4? This is exactly like asking for Captain Redbeard to get at least 4 gold pieces. We are going to "pre-distribute" 4 "counts" to the variable x1, and then distribute the remaining 21 "counts" to all five variables. More formally, we define y1 = x1 -4. The condition requires only y1 $\geq 0. Thus, we are trying to solve the equation x1 + x2 + x3 + x4 + x5 = 25 \Leftrightarrow$(x1 -$4) + x2 + x3 + x4 + x5 = 21 \Leftrightarrow y$1 + x2 + x3 + x4 + x5 = 21


> 🇨🇳 **练习** (1) 从 5 种水果中选 12 个水果（可重复），有多少种方式？(2) 求 $a+b+c+d=15$ 的非负整数解个数。(3) 一条街上 20 户人家，今晚有几户开灯。有多少种开灯方式？


Applying the formula, we see there are (21 + (5 -1) 5 -1 ) = (25


> 🇨🇳 (4) 将 100 元分配给 3 个基金（每个至少 10 元），有多少种方式？(5) 区分以下问题类型并求解：从 52 张牌中抽 5 张手牌；将 10 个学生排成一列；从 7 种冰淇淋中买 3 勺（可重复）。


) such solutions. (3) How many solutions satisfy x1, x2 $\geq$5 and x3, x4, x5 $\geq$2? Using a method exactly like the last one, we see that we're trying to solve y1 + y2 + y3 + y4 + y5 = 9 where yi = xi -5 for i = 1, 2, and yi = xi -2 for i = 3, 4, 5. The right-hand side has been changed to 25 -5 -5 -2 -2 -2 = 9. By the formula, we know there are (9 + (5 -1) 5 -1 ) such solutions. (4) How many solutions satisfy x2 $\leq$5? We can do this in one of two ways. First, let's take the total number of solutions (found in the first part of this example) and remove the number of solutions that fail this desired condition. That is, let's take the number of solutions where x2 $\geq$6, which is ((25 -6) + (5 -1) 5 -1 ) = (23


> 🇨🇳 **应用：方程的整数解** 星与条方法的核心应用是计数方程的非负/正整数解。手段：令 $y_i = x_i + c$（$c$ 为常数）使变量满足所需下界条件。


) and remove it from the total, yielding (29


> 🇨🇳 \n** autogenerated summary ** 可重复选取课到此结束。核心要点：$\binom{k+n-1}{k}$，星与条证明方法，以及与排列/组合的四种情况对比。


) Second, we could write this as a sum, finding the number of solutions that satisfy x2 = ℓ, for 0 $\leq$ℓ$\leq$5:


> 🇨🇳 \n** 补充 ** 可重复选取与"将不可辨球放入可辨盒子"问题等价。两种直观理解互相补充。


) Interestingly enough, if we had only thought to solve this in the second way, we could still reduce the expression to the first one. We just need to use the Summation Identity! Observe that


> 🇨🇳 \n** 补充2 ** 注意：可重复选取中 $k$ 可以大于 $n$（与不重复选取不同），公式始终有效。


### 8.5.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What is the difference between a selection and a selection with repetition? (2) What is the number of ways to select n objects from k objects? (Careful about letters here!) (3) What is the number of ways to select n objects from k types of objects? (4) How are the "Pirates & Gold" and "Integer Sums" formulations equivalent? (5) Adapt the argument we used to derive the formula {n+k-1 k-1 } and use it to prove the same formula counts the number of solutions to the "Integer Sums" formulation. Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) A clothing store makes 5 different colors of shirts (red, green, blue, white, and black). (a) We need to buy 10 shirts. How many ways can we do this, assuming we can order any number of shirts of each color (i.e. there's an unlimited supply of each color)? (b) We need to acquire some shirts, either 10 or 11 or 12, we're not sure yet. How many ways can we do this, again assuming an unlimited supply of each color? (c) We need to acquire 10 or 11 or 12 shirts, but in each case we need at least 1 shirt of each color. How many ways can we do this? (d) Now, we need to order 25 shirts, but we are told that there are only 3 red shirts left (while each other color still has an unlimited supply). How many ways can we do this? (e) Now, we still need to order 25 shirts, but we are told there are only 3 red shirts and 5 blue shirts left (while each other color still has an unlimited supply). How many ways can we do this?


> 🇨🇳 \n** 补充3 ** 当问题要求某变量有下界时，先做变量替换再去掉下界。


(2) Consider rolling 20 indistinguishable dice. (a) How many total outcomes are there? (b) How many have each number appearing at least twice? (c) How many have at most three 6s? (d) How many have at least four 6s? (3) What is wrong with the "proof" of the following claim? Consider 4 buckets of coins: one bucket contains pennies, one contains nickels, one contains dimes, and one contains quarters. There are over 50 coins in each bucket (so we don't have to worry about running out of any type of coin). We want to select 50 coins from these buckets; we want to make sure that we select at least 10 pennies and at least 10 nickels but at most 10 dimes and at most 10 quarters.
Claim: The number of ways to do this is
(53


> 🇨🇳 \n** 补充4 ** 记住四种选择方式的对比表，这是组合数学的基础。


) = 23261
Proof: Consider the total number of ways to select 50 coins from 4
types, with no added restrictions. This is selecting k = 50 objects from n = 4 types, so there are {53


> 🇨🇳 \n** 补充5 ** 练习中要注意区分"有序/无序"和"可重复/不可重复"两个维度。


} ways to do this. Now, we want to remove from this total the number of ways to select the coins where we do pick at least 10 pennies and at least 10 nickels but also at least 11 dimes and at least 11 quarters. To count these selections, we just want to actually select all of those coins (there are 42 total) and then select 8 more from all four types. We know there are {11


> 🇨🇳 \n** 补充6 ** 星与条方法的物理直觉：$k$ 个物品是星，$n-1$ 个分隔是条，排列星星与条即对应一种选取方案。


} ways to choose k = 8 objects from n = 4 types. Subtracting the second number from the first, we get the number given in the claim.
## 8.6 Pigeonhole Principle
### 8.6.1 Motivation This is a result we have hinted at before. We even proved a particular version of it way back when we studied proof techniques for the first time! (See Example
4.9.2.) The general idea is this:
If we have too much "stuff" to put into too few "boxes", then some box has a bunch of "stuff".


> 🇨🇳 \n** 补充7 ** 正整数解的"间隔法"思路：$k$ 个物品排成一列，在 $k-1$ 个间隔中选 $n-1$ 个放隔板。


