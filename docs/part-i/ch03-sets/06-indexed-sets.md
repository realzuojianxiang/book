---
title: Indexed Sets
---

# Indexed Sets

number of sets "all at once". There is really no new mathematical content in this section, but the notation involved in these ideas can be confusing and difficult to work with, at first, so we want to guide you through these ideas carefully. Relation to Summation Notation We'll start with a related concept that we have seen before. Remember when we investigated sums of natural numbers in Chapter 1? We mentioned some special notation that allowed us to condense a long string of terms in a sum into one concise form, using the P symbol. For instance, we could write an informal sum ("informal" meaning "not rigorous" because of the use of ellipses) in the P notation as follows: 1 + 2 + 3 + 4 + $\cdot$  $\cdot$  $\cdot$ + (n −1) + n = n X i=1 i Why does this notation work and make sense? The index variable i is the key component of condensing the sum into this form. Writing "i = 1" underneath the P symbol means that the value of the variable i should start at 1 and increase by 1 until it reaches the terminal value, n, written above the P symbol. For each allowable value of i in that range (from 1 to n), we include a term in the sum of the form written to the right of the P symbol; in this case, that term is i. Thus, we should have the terms 1, 2, 3, . . . , n with a + sign between each. We should point out that it is implicitly understood that writing i = 1 and n as the limits on the index variable i means i assumes all values that are natural numbers between 1 and n.
Example
Let's see the process of defining indexed sets via an example first. We will also see how to apply set operations to several sets by using an index variable.
Example 3.6.1. We can similarly condense some set operation notation. For
instance, let's define the sets A1, A2, A3, . . . , A10 by A1 = {1, 2} A2 = {2, 4} A3 = {3, 6} ... Ai = {i, 2i} ... A10 = {10, 20}


> 🇨🇳 **例 3.6.1** 我们可以类似地压缩集合运算记号。例如，定义集合 $A_1, A_2, A_3, \ldots, A_{10}$ 如下：$A_1 = \{1, 2\}$，$A_2 = \{2, 4\}$，$A_3 = \{3, 6\}$，$\ldots$，$A_i = \{i, 2i\}$，$\ldots$，$A_{10} = \{10, 20\}$。


We included the definition of Ai for an arbitrary value i to give these sets a rigorous definition. Without definining that set---which defines Ai for any relevant value of i---we would be leaving it up to the reader to interpret the pattern among the sets A1, A2, A3, A10, and there could be multiple ways of interpreting that. By defining the term Ai explicitly like this, there is no confusion as to what we want these ten sets to be. Furthermore, we can more easily express the union of all of these sets, for instance. Remember that the union of two sets is the set containing all elements of both sets (i.e. an element is included in the union if it is in the first set or the second set, or possibly both). What is the union of more than two sets? It follows the same idea as the definition for just two sets; we want to include an element in the union if it is in any of the constituent sets we are combining via the union operation. How can we write this union concisely and precisely? Let's follow the same motivation of the P notation. The index of these sets runs from 1 to 10, so we should write i = 1 below a "$\cup$" symbol and 10 above it. Each term in the union is of the form {i, 2i}, so we should write that to the right of the "$\cup$" symbol. For indexed unions like this one, though, we use a slightly larger "S" symbol, like so: A1 $\cup$A2 $\cup$A3 $\cup$ $\cdot$  $\cdot$  $\cdot$ $\cup$A10 =


> 🇨🇳 我们包含了对任意值 $i$ 下 $A_i$ 的定义，是为了给这些集合一个严格的定义。如果不显式定义 $A_i$——即对所有相关值 $i$ 定义 $A_i$——我们就把 $A_1, A_2, A_3, \ldots, A_{10}$ 之间规律的解读留给了读者，而这种规律可能存在多种解读方式。通过像这样显式定义 $A_i$，就不会对我们想要的这十个集合产生任何混淆。此外，我们也能更方便地表达所有这些集合的并集。还记得两个集合的并集是包含两个集合所有元素的集合（即一个元素若在第一个集合或第二个集合中，或同时在两者中，则该元素被包含在并集中）。多于两个集合的并集又是什么呢？它与仅两个集合的并集定义遵循相同的思想：如果一个元素在我们通过并集运算组合的任何一个组成集合中，我们就希望将该元素包含在并集中。我们如何能简洁而精确地写出这个并集呢？让我们遵循与求和记号 $\sum$ 相同的动机。这些集合的索引从 1 到 10，所以我们应该在 "$\cup$" 符号下方写 $i = 1$，上方写 $10$。并集中的每一项都具有 $\{i, 2i\}$ 的形式，所以我们应该将其写在 "$\cup$" 符号的右侧。不过，对于这样的索引并集，我们使用一个稍大一些的 "$\bigcup$" 符号，如下：$A_1 \cup A_2 \cup A_3 \cup \cdots \cup A_{10} = \bigcup_{i=1}^{10} \{i, 2i\}$。这种写法远比列出所有 10 个集合的元素来得简洁，可见这种记号多么有用。我们会不断提醒你左侧并集中的省略号是不精确的，事实上右侧这样的表达式才是关于这个并集的真正严格的数学陈述。左侧的表达式更多是一种直观的、启发式的方式来描述作用于这十个集合的并集运算。


[ i=1 {i, 2i} This is far more concise than writing the elements of all 10 sets, so you can see how useful this notation is. We will keep reminding you of the imprecision of the ellipses in the union on the left and tell you that, in fact, an expression like the one on the right is a truly rigorous mathematical statement about this union. The expression on the left is more of an intuitive, heuristic way of describing the union operation applied to these ten sets. When The Index Set Is Not a Range of Numbers Let's examine a more difficult example to motivate the next development in this notation technique. What if we asked you to write the following sum in summation notation: the sum of the squared reciprocals of all prime numbers. How can we accomplish this? (Note: We just want to express all the terms of the sum without evaluating the sum. That's a difficult endeavor left for another time!) Unfortunately, we cannot use the exact same notation as above, because we don't want to sum over a range of index values between two natural numbers; rather, we want to only include terms in the sum corresponding to prime numbers. The solution to this is to define an index set I that will describe the allowable values of the index that we will then "plug into" the arbitrary term written to the right of the sum. In this case, if we have a prime number i, we would like to include the term


> 🇨🇳 **当指标集不是数的区间时** 让我们看一个更难的例子来推动这种记号技术的下一步发展。如果让你用求和记号写出以下求和：所有素数的平方倒数之和。该怎么做呢？（注意：我们只想表达求和中的所有项，而非对其求值。那是一项困难的任务，留待将来！）不幸的是，我们不能使用与之前完全相同的记号，因为我们不希望在两个自然数之间的索引值范围内求和；相反，我们只想在求和中包含对应于素数的项。解决方法是定义一个**指标集** $I$，它将描述索引的允许取值，然后我们将这些值"代入"求和符号右侧写出的通项中。在这种情况下，若 $i$ 是素数，我们希望包含项 $\dfrac{1}{i^2}$。


i2 in our sum, so this expression will be written to the right of the P symbol. We would like to express in our notation that the value i should be a prime


> 🇨🇳 $\dfrac{1}{i^2}$ 在我们的求和中，因此这个表达式将被写在求和符号 $\sum$ 的右侧。我们希望用记号表达索引 $i$ 的值应该是素数，并且所有可能的素数都应被包含。


number and that all possible prime numbers should be included. The index set I of allowable values should, therefore, be the set of all prime numbers. That is, we can write this sum as X i$\in$I


> 🇨🇳 因此，允许取值的指标集 $I$ 应该是所有素数的集合。也就是说，我们可以将这个求和写为 $\sum_{i \in I} \dfrac{1}{i^2}$，其中 $I = \{i \in \mathbb{N} \mid i \text{ 是素数}\}$。看这个记号实现了什么！我们不仅将无穷多项压缩为一个表达式，还指明了任意索引 $i$ 的值应限制为素数——素数不像求和 $\sum_{i=1}^{n} i$ 中的索引那样以"通常"的方便方式排列。


i2 , where I = {i $\in$N | i is prime} Look at what this notation accomplishes! Not only have we condensed an infinite number of terms into one expression, we have indicated that the values of the arbitrary index i should be restricted to prime numbers, which do not behave in the "usual" and convenient way as with a sum like Pn i=1 i.
Example 3.6.2. This concept of an index set is extremely useful and extends to
arbitrary sets and even non-mathematical objects. For instance, in our discussion of sets above we used the set B of all Major League Baseball teams. How can we use this set to express the set P of all Major League Baseball players? Each team is, itself, a set whose elements are the players on that team, so a union of all of the teams (i.e. a union of all sets in B) should produce exactly this set of all players! In this case, our index set is B, and for each element b $\in$B, we want to include b as a set in our union. Thus, we would write P = [ b$\in$B b The individual terms in this union are not even dependent on natural numbers, so there would have been no way to express this union without the use of an index set, like this. Also, this union is dependent on the fact that the terms of the union are elements of the index set B, but they are also sets themselves; thus, applying the union operation to them makes mathematical sense. This might still seem like an odd idea, so be sure to think carefully about this idea of sets having elements that are sets, themselves. Reading Indexed Expressions Aloud To verbalize these types of expressions, and to help you think of them in your head, let's give you an example. We might read the expression up above as "The sum, over all i that are prime, of


> 🇨🇳 **例 3.6.2** 指标集的概念极为有用，可以推广到任意集合甚至非数学对象。例如，在前文讨论集合时，我们用过所有 MLB 球队组成的集合 $B$。如何用这个集合来表示所有 MLB 球员组成的集合 $P$ 呢？每支球队本身就是一个以球员为元素的集合，因此所有球队（即 $B$ 中所有集合）的并集恰好就是全体球员的集合！此时，指标集是 $B$，对每个元素 $b \in B$，我们将 $b$ 作为一个集合包含在并集中。于是我们写为 $P = \bigcup_{b \in B} b$。这个并集中的各项甚至不依赖于自然数，因此若不使用指标集就无法表达这个并集。此外，这个并集依赖于并集的项是指标集 $B$ 的元素、同时又是集合这一事实——因此对它们施以并集运算在数学上是合理的。这看起来可能仍然是一个奇怪的想法，所以请务必仔细思考"集合的元素本身也是集合"这一概念。**口读索引表达式** 为了口述这类表达式并帮助你在脑中建立概念，我们来看一个例子。我们可能会将上面的表达式读作"对所有素数 $i$，求 $i^2$ 之和"或


i2 ." or "The sum of


> 🇨🇳 "$i^2$ 的和，其中 $i$ 遍历所有素数。"类似地，我们可能会将上面的另一个表达式读作"对所有属于 2012 赛季 MLB 球队的 $b$，取这些 $b$ 的并集"或


i2 , where i ranges over all prime numbers." Likewise, we might read the other expression above as "The union, over all b that are MLB teams in the 2012 season, of those b." or "The union of all sets b, where b ranges over all MLB teams from the 2012 season."


> 🇨🇳 "所有集合 $b$ 的并集，其中 $b$ 遍历 2012 赛季的所有 MLB 球队。"


### 3.6.2 Indexed Unions and Intersections Let's give a precise definition of this union operation for more than one set, since we have only rigorously defined the union of two sets.
<div class="def-definition" markdown>
**Definition 3.6.3. The union of a collection of sets Ai indexed by the set I is**
</div>
[ i$\in$I Ai = {x $\in$U | x $\in$Ai for some (i.e. at least one) i $\in$I} where we assume there is a set U such that Ai $\subseteq$U for every i $\in$I. In mathematical language, the phrase "for some i $\in$I" means that we want there to be at least one i $\in$I with the specified property. If an element x satisfies x /$\in$Ai for every i $\in$I, then this says x is not in any of the sets in our collection, so it should not be included in the union. Following this idea, we can make a similar definition for set intersections.
<div class="def-definition" markdown>
**Definition 3.6.4. The intersection of a collection of sets Ai indexed by the set**
</div>
I is \ i$\in$I Ai = {x $\in$U | x $\in$Ai for every i $\in$I} where we assume there is a set U such that Ai $\subseteq$U for every i $\in$I.
### 3.6.3 Examples
Let's return to a previous example and make these ideas clearer.
Example 3.6.5. Previously, in Example 3.6.1, we defined
Ai = {i, 2i} for every natural number i between 1 and 10. Another way of defining this collection is to consider the index set I = [10] (recall the notation [n] = {i $\in$N | 1 $\leq$i $\leq$n}) and define A to be the set A = {Ai | i $\in$I} , where Ai = {i, 2i} for every i $\in$I This defines every set Ai, dependent on the index value i chosen from the index set I, and it "collects" all of these sets into one set A. Then, another way of writing that union we wrote before would be [ i$\in$I Ai with the given definitions of I and Ai. (Think carefully about how this union differs from the set A. Also, what exactly is this union? How can we express its elements conveniently? Do we need to list every element? What if we change the index set I to be N? What is the union in that case?)


> 🇨🇳 仔细思考这个并集与集合 $A$ 的区别。此外，这个并集究竟是什么？我们如何方便地表达其元素？是否需要列出每个元素？如果将指标集 $I$ 改为 $\mathbb{N}$，并集会变成什么？


Example 3.6.6. Let I = {1, 2, 3} and, for every i $\in$I, define
Ai = {i −2, i −1, i, i + 1, i + 2} Let's identify and write out the elements of the following sets: [ i$\in$I Ai and \ i$\in$I Ai Notice that we can write out the elements of each Ai set, as follows: A1 = {−1, 0, 1, 2, 3} A2 = {0, 1, 2, 3, 4} A3 = {1, 2, 3, 4, 5} Thus, [ i$\in$I Ai = A1 $\cup$A2 $\cup$A3 = {−1, 0, 1, 2, 3, 4, 5} and \ i$\in$I Ai = A1 $\cap$A2 $\cap$A3 = {1, 2, 3} Now, consider J = {−1, 0, 1}, with Aj defined in the same way as before. Let's identify the elements of the sets [ j$\in$J Aj and \ j$\in$J Aj Writing out the elements of each set, we can determine that [ j$\in$J Aj = A−1 $\cup$A0 $\cup$A1 = {−3, −2, −1, 0, 1, 2, 3} and \ j$\in$J Aj = A−1 $\cap$A0 $\cap$A1 = {−1, 0, 1} Try answering the same questions with different index sets. For instance, consider K = {1, 2, 3, 4, 5} or L = {−3, −2, −1, 0, 1, 2, 3}.
Example 3.6.7. Define the index set I = N. For every i $\in$I, define the set
Ci =  x $\in$R | 1 $\leq$x $\leq$i + 1 i  Then we claim that [ i$\in$I Ci = {y $\in$R | 1 $\leq$y $\leq$2} and \ i$\in$I Ci = {1} Can you see why these are true? We will discuss the techniques required to prove such equalities later on. For now, we ask you to just think about why these are true. Can you explain them to a classmate or a friend? What sort of techniques might you use to prove these claims?


> 🇨🇳 你能看出为什么这些等式成立吗？我们将在稍后讨论证明此类等式所需的技巧。现在，我们只请你思考它们为什么成立。你能向同学或朋友解释这些吗？你可能会用到什么样的技巧来证明这些论断？


Example 3.6.8. Let S be the set of students taking this course. For every s $\in$S,
let Cs be the set of courses that student s is taking this semester. What do the following expressions represent? [ s$\in$S Cs and \ s$\in$S Cs We bet you can identify at least one element of the set on the right!
### 3.6.4 Partitions Now that we have a way of writing down a union of many sets, we can define a helpful notion: that of a partition. Linguistically speaking, a partition is a way of "breaking something apart into pieces", and that's pretty much what this word means, mathematically speaking. To wit, a partition is just a collection of subsets of a set that do not overlap and whose union is the entire set. Let's write down that definition here and then see some examples and non-examples. We will have occasion to use this definition many times in the future, so let's get a handle on it now while we're talking about sets and indexed unions.
<div class="def-definition" markdown>
**Definition 3.6.9. Let A be a set. A partition of A is a collection of sets that**
</div>
are pairwise disjoint and whose union is A. That is, a partition is formed by an index set I and non-empty sets Si (defined for every i $\in$I) that satisfy the following conditions: (1) For every i $\in$I, Si $\subseteq$A. (2) For every i, j $\in$I with i ̸= j, we have Si $\cap$Sj = $\emptyset$. (3) [ i$\in$I Si = A The sets Si are called parts of the partition. The idea here is that the sets Si "carve up" the set A into non-overlapping, nonempty pieces.
Example 3.6.10. Let's see a couple of examples.
(1) Consider the set N. Let O be the set of odd natural numbers, and let E be the set of even natural numbers. Then {O, E} is a partition of N. This is because • E, O ̸= $\emptyset$, and • E, O $\subseteq$N, and • E $\cap$O = $\emptyset$, and • E $\cup$O = N


> 🇨🇳 **例 3.6.10** (1) 考虑集合 $\mathbb{N}$。令 $O$ 为奇自然数集，$E$ 为偶自然数集。则 $\{O, E\}$ 是 $\mathbb{N}$ 的一个划分。这是因为：$E, O \neq \emptyset$，且 $E, O \subseteq \mathbb{N}$，且 $E \cap O = \emptyset$，且 $E \cup O = \mathbb{N}$。


(2) Consider the set R. For every z $\in$Z, define the set Sz by Sz = {r $\in$R | z $\leq$r < z + 1} We claim {. . . , S−2, S−1, S0, S1, S2, . . . } is a partition of R. Can you see why? Try to write out the conditions required for this collection of sets to be a partition, and see if you can understand why they hold. Specifically, remember that we need these sets to be pairwise disjoint. This means that any two sets must be disjoint. Notice that this is quite different from requiring the the intersection of all the sets together to be empty. For instance, consider the collection of sets  {1, 2}, {2, 3}, {3, 4}


> 🇨🇳 注意："两两不相交"意味着任意两个集合都必须不相交。这与要求所有集合的交集为空截然不同。例如，考虑集合族 $\{\{1, 2\}, \{2, 3\}, \{3, 4\}\}$——它不是两两不相交的，因为例如 $\{1, 2\} \cap \{2, 3\} = \{2\} \neq \emptyset$。然而，所有三个集合的交集是空集，因为没有元素同时属于这三个集合。


This collection is not pairwise disjoint because, for example, {1, 2} $\cap${2, 3} = {2} ̸= $\emptyset$ However, the intersection of all three sets is empty, because no element is common to all three of them together.
Example 3.6.11. Now, let's see a couple of non-examples.
(1) Consider the set R. Let P be the set of positive real numbers and let N be the set of negative real numbers. Then {N, P} is not a partition because 0 /$\in$N $\cup$P. Can you modify the choices we made here to identify a partition of R into two parts? (2) Consider the set Z. Let A2 be the set of integers that are multiples of 2, let A3 be the set of integers that are multiples of 3, and let A5 be the set of integers that are multiples of 5. The collection {A2, A3, A5} is not a partition for two reasons. First, these sets are not pairwise disjoint. Notice that 6 $\in$A2 and 6 $\in$A3, since 6 = 2 $\cdot$ 3. Second, these sets do not "cover" all of Z. Notice that 7 $\in$Z but 7 /$\in$A2 $\cup$A3 $\cup$A5. As we mentioned, we will have occasion to use this definition frequently in the future, so keep it in mind.
### 3.6.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory!


> 🇨🇳 **回顾自检** 简要回答以下问题，可以口头回答也可以书面回答。这些问题都基于你刚读过的章节，所以如果你记不起某个具体的定义、概念或例子，请回去重读那部分。确保在继续之前你有信心回答这些问题——这将有助于你的理解和记忆！


(1) What is an index set? (2) Let I = N, and for every i $\in$I, let Ai = {i, −i}. Why are the following sets all the same set? [ i$\in$I Ai [ x$\in$N Ax [ j$\in$I Aj By the way, what are the elements of this set? (3) List the elements of the following sets: (a) [ x$\in$N {x} (b) \ x$\in$N {x} (c) [ x$\in$N {x, 0, −x} (4) Why do you think we didn't talk about an "indexed difference" or an "indexed complementation", and only talked about unions and intersections? (5) What is a partition? What conditions does a collection of sets have to satisfy to be a partition of a set? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Let A = {−2, −1, 0, 1, 2}. Let B = {1, 3, 5}. For every i $\in$Z, let Si = {i −2, i, i + 2, i + 4}. What is [ i$\in$A Si? What is \ x$\in$B Sx? (2) For every n $\in$N, let An = [n]. What is \ n$\in$N An? What about [ n$\in$N An? (3) Find a way to write the set of all integers between -10 and 10 (inclusive) using set-builder notation. Then, define the same set using an indexed union. Can you do this in a way so that the sets in your union are pairwisedisjoint (meaning that no two of them have any elements in common)? (Hint: Yes, you can.)


> 🇨🇳 **动手试试** 尝试回答以下简答题。它们需要你实际写下一些内容，或口头描述（也许可以对着朋友或同学）。目标是让你练习使用新的概念、定义和记号。它们应该比较简单；确保你能完成这些问题将对你有所帮助！


(4) For every n $\in$N, let Mn be the set of all multiples of n. (For example, M3 = {3, 6, 9, . . . }.) Write a definition for Mn using set-builder notation. Then, express N as a union, using these sets. (Challenge: Can you use these sets to define a partition of N?) (5) Let X be any set. What is [ S$\in$P(X) S? What about \ S$\in$P(X) S? (It might help to try this with a specific set, like X = {1, 2}, to see what happens, first.) (6) Identify an index set and define some sets that allow you to express Q as an indexed union. Can you do this so that there are infinitely many elements in the index set? (Challenge: Can you make this collection a partition of Q?)
## 3.7 Cartesian Products There is one more way of "combining" sets to produce other sets that we want to investigate. This method is based on the idea of order. When we define sets by listing the elements, the order is irrelevant; that is, the sets {1, 2, 3} and {3, 1, 2} and {2, 1, 3} are all equal because they contain the same elements. (More specifically, they are all subsets of each other in both directions). Looking at mathematical objects where order is relevant, though, allows us to combine sets in new ways and produce new sets. You are likely already familiar with the idea of the real plane, R2 (also known as the Cartesian plane after the French matheamtician Ren´e Descartes). Each "point" on the plane is described by two values, an x-coordinate and a ycoordinate, and the order in which we write those coordinates is important. We usually think of the x-coordinate as first and the y-coordinate as second, and this helps to distinguish two points based on this order. For instance, the point (1, 0) lies on the x-axis but the point (0, 1) lies on the y-axis. They are not the same point. There is a deeper, mathematical idea underlying the Cartesian plane. Given any two sets, A and B, we can look at the set of all ordered pairs of elements from A and B. By pair we mean an expression (a, b) where a and b are elements of A and B, respectively. By ordered we mean that writing a first and b second is important. In the case of the real plane, it is especially important because any real number could appear as the x-coordinate or the y-coordinate of a point, but the point (x, y) is generally different from the point (y, x). (When are they equal? Think carefully about this.)
### 3.7.1 Definition
Let's give an explicit definition of this new set before examining some examples.


> 🇨🇳 **笛卡尔积** 还有一种"组合"集合来产生新集合的方式值得研究。这种方式基于"序"的概念。当我们通过列举元素来定义集合时，顺序无关紧要——即 $\{1, 2, 3\}$、$\{3, 1, 2\}$ 和 $\{2, 1, 3\}$ 都是相等的，因为它们包含相同的元素。但当顺序相关时，我们可以以新的方式组合集合来产生新集合。你大概已经熟悉实平面 $\mathbb{R}^2$ 的概念（也称为笛卡尔平面，得名于法国数学家勒内·笛卡尔）。平面上的每个"点"由两个值描述——$x$ 坐标和 $y$ 坐标——而书写坐标的顺序是重要的。给定任意两个集合 $A$ 和 $B$，我们可以考察由 $A$ 和 $B$ 中的元素组成的所有**有序对**的集合。所谓"对"（Pair），是指形如 $(a, b)$ 的表达式，其中 $a$ 和 $b$ 分别是 $A$ 和 $B$ 的元素。所谓"有序的"（Ordered），是指先写 $a$ 再写 $b$ 这一顺序是重要的。在给出笛卡尔积的正式定义之前，让我们先看一些例子。

