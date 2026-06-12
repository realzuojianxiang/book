---
title: Subsets
---

# Subsets

Notice the similarities between these symbols and the inequality symbols we use to compare real numbers. We write inequalities like x $\leq$2 or 5 > z > 0 and understand what those mean based on the "direction" of the symbol and whether we put a bar underneath it. The symbols \subseteq, \subset, \supseteq, \supset work exactly the same way, except they refer to "containment of elements" as opposed to "magnitude of a number". Standard Sets of Numbers The standard sets of numbers we mentioned in the last section are related via the subset relation quite nicely. Specifically, we can say N $\subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$ Again, we take for granted our collective knowledge of these sets of numbers to allow us to make these claims. However, there are some profound and intricate mathematical concepts involved in describing exactly why, say, the set R exists and is a proper superset of Q. For now, though, we use these sets to illustrate the subset relationship. Since we know the subset relationships above are proper, we used that corresponding symbol, "\subset". In general, it is common in mathematical writing to simply use the "\subseteq" symbol, even if it is known that "\subset" would apply. We might only resort to using the "\subset" symbol when it is important, in context, to indicate that the two sets are not equal. If that information is not essential to the context at hand, then we might just use the "\subseteq" symbol. Set-Builder Notation Creates Subsets One way that we have already "used" the idea of a subset was in our use of set-builder notation. This is used to define a set to be all of the elements of a "larger" set that satisfy a certain property. We define a property P(x), draw a variable object x from a larger set X, and include any elements x that satisfy the property P(x). Notice that any element of this new set must be an element of X, simply based on the way we defined it. Thus, the following relationship holds {x \in X | P(x)} \subseteq X regardless of the set X and the property P(x). Depending on the set X and the property P(x), it may be that the proper subset symbol \subset applies but, in general, we can say for sure that \subseteq applies. Try to come up with some examples of sets X and properties P(x) so that \subseteq applies, then try to come up with some examples where \subset applies. Try to come up with one set X and two different properties P1(x) and P2(x) so that \subset applies for P1(x) and \subseteq applies for P2(x). Try to identify two different sets X1 and X2 and two different properties P1(x) and P2(x) so that {x \in X1 | P1(x)} = {x $\in X$2 | P2(x)} Can you do it?


> 🇨🇳 注意这些符号与比较实数的不等式符号之间的相似性。$\subseteq$、$\subset$、$\supseteq$、$\supset$ 的工作方式与 $\leq$、$<$、$\geq$、$>$ 完全相同，只不过它们指"元素的包含关系"而非"数的大小"。标准数集之间有很好的子集关系：$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$。集合构造记号自然产生子集关系：$\{x \in X \mid P(x)\} \subseteq X$，无论集合 $X$ 和性质 $P(x)$ 是什么。


Examples
A set is a subset of another set if and only if every element of the first one is an element of the second one. For instance, this means that the following claims all hold: {142, 857} $\subseteq \mathbb{N} n\sqrt 3,$ −$\pi$, 8.2 o $\subseteq \mathbb{R}$

 x $\in \mathbb{R}$ | x2 = 1


> 🇨🇳 **例子** 集合是另一集合的子集当且仅当第一个的每个元素也是第二个的元素。例如 $\{142, 857\} \subseteq \mathbb{N}$，$\{\sqrt{3}, -\pi, 8.2\} \subseteq \mathbb{R}$，以及 $\{x \in \mathbb{R} \mid x^2 = 1\} \subseteq \mathbb{Z}$。


$\subseteq \mathbb{Z}$ Do you see why these are True? For a subset relationship to fail, then, we must be able to find an element of the first set that is not an element of the second set. For instance, this means that the following claims all hold: {142, −857} ̸$\subseteq \mathbb{N} n\sqrt 3,$ −$\pi$, 8.2 o ̸$\subseteq \mathbb{Q}$

 x $\in \mathbb{R}$ | x2 = 5


> 🇨🇳 子集关系不成立的条件是我们必须能找到第一个集合中不是第二个集合元素的那个元素。例如 $\{142, -857\} \not\subseteq \mathbb{N}$，$\{\sqrt{3}, -\pi, 8.2\} \not\subseteq \mathbb{Q}$，以及 $\{x \in \mathbb{R} \mid x^2 = 5\} \not\subseteq \mathbb{Z}$。


̸$\subseteq \mathbb{Z}$ Finding All Subsets of a Set Let's work with a specific set for a little while. Define A = {1, 2, 3}. Can we identify all of the subsets of A? Sure, why not? {1} \subseteq A {2} \subseteq A {3} \subseteq A {1, 2} \subseteq A {1, 3} \subseteq A {2, 3} \subseteq A A = {1, 2, 3} \subseteq A $\emptyset \subseteq A$ Identifying the first six subsets was fairly straightforward, but it's important to remember that A and \emptyset are subsets, as well. (Notice: it is true, in general, that for any set S, S \subseteq S and $\emptyset \subseteq S$. Think about this!) Consider the set B whose elements are all of the sets we listed above: B =

 {1} , {2} , {3} , {1, 2} , {1, 3} , {2, 3} , A, $\emptyset$


> 🇨🇳 **找出集合的所有子集** 设 $A = \{1, 2, 3\}$。$A$ 的所有子集为：$\{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, A, \emptyset$。注意 $A$ 本身和 $\emptyset$ 也是子集！定义 $B$ 为包含这些子集的集合。

It is true that any element X $\in B satisfies X \subseteq A$. Do you see why?


> 🇨🇳 $B$ 的每个元素 $X$ 都满足 $X \subseteq A$。你看出为什么了吗？


### 3.4.2 The Power Set This process of identifying all subsets of a given set is common and useful, so we identify the resulting set with a special name.
<div class="def-definition" markdown>
**Definition 3.4.2. Given a set A, the power set of A is defined to be the set**
</div>
whose elements are all of the subsets of A. It is denoted by P(A). Our parenthetical observation from the above paragraph tells us that S $\in P(S) and \emptyset \in P$(S), for any set S. Look back at our example set A = {1, 2, 3} above. What do you notice about the number of elements in P(A)? How does it relate to the number of elements in A? Do you think there is a general relationship between the number of elements in S and P(S), for an arbitrary set S?
Example 3.4.3. Let's find P($\emptyset$). What are the subsets of the empty set? There
is only one, the empty set itself! (That is, $\emptyset \subseteq \emptyset$, but no other set satisfies this.) Accordingly, the power set P(\emptyset) has one element, the empty set: P(\emptyset) = { \emptyset} Notice that this is different from the empty set itself: \emptyset̸= { $\emptyset$} Why is this true? Compare the elements! The empty set has no elements, but the set on the right has exactly one element. (In general, this can be a helpful way to compare two sets.) To give you some practice, we'll point out that would read the above line aloud as: "The empty set and the set containing the empty set are two different sets."
Example 3.4.4. Let's try this process with another set, say A = { $\emptyset, {1, \emptyset$} }.
We can list the elements of P(A) as P(A) = { {$\emptyset} , {{1, \emptyset}} , {\emptyset, {1, \emptyset}} , \emptyset$, } This may look strange, with all of the empty sets and curly braces, but it is important to keep the subset relationships straight. It is true, in this example, that $\emptyset \in A, {\emptyset} \subseteq A, {\emptyset} \in P(A), {\emptyset} \subseteq P$(A) Why are these relationships true? Think carefully about them, and try to write a few more on your own. The distinction between "\in" and "$\subseteq$" is very important!


> 🇨🇳 **3.4.2 幂集** 集合 $A$ 的**幂集** $\mathcal{P}(A)$ 是 $A$ 的所有子集构成的集合。对任意集合 S，有 $S \in \mathcal{P}(S)$ 和 $\emptyset \in \mathcal{P}(S)$。注意 $\mathcal{P}(\emptyset) = \{\emptyset\}$ 且 $\emptyset \neq \{\emptyset\}$（前者无元素，后者有一个元素）。例 3.4.4 中 $\emptyset \in A$、$\{\emptyset\} \subseteq A$、$\{\emptyset\} \in \mathcal{P}(A)$、$\{\emptyset\} \subseteq \mathcal{P}(A)$——区分 $\in$ 和 $\subseteq$ 非常重要！


### 3.4.3 Set Equality When are two sets equal? The main idea is that two sets are equal if they contain "the same elements", but this is not a precise definition of equality. How can we describe that property more explicitly and rigorously? To say that two sets, A and B, have "the same elements" means that any element of A is also an element of B, and every element of B is also an element of A. If both of these properties hold, then we can be guaranteed that the two sets contain precisely the same elements and are, thus, equal. If you think about it, you'll notice that we can phrase this in terms of subsets. How convenient!
<div class="def-definition" markdown>
**Definition 3.4.5. We say two sets, A and B, are equal, and write A = B, if**
</div>
and only if A $\subseteq B and B \subseteq A$. (What happens if we use the \subset symbol in the definition, instead of $\subseteq$? Is this the same notion of set equality? Why or why not?) This definition will be very useful in the future when we learn how to prove two sets are equal and we can't simply list the elements of each and compare them. By constructing two arguments and proving the subset relationship in "both directions", we can show that two sets are equal. For now, let's see this definition applied to a straightforward example.
Example 3.4.6. How can we use this to definition to observe that the following
equality holds? {x $\in \mathbb{Z}$ | x $\geq$1} = N We just need to see that the $\subseteq and \supseteq r$elationship applies between the two sides. First, is it true that every integer that is at least 1 is a natural number? Yes! This explains why {x $\in \mathbb{Z}$ | x $\geq$1} $\subseteq \mathbb{N}$ Second, is it true that every natural number is a positive integer that is at least 1? Yes! This explains why {x $\in \mathbb{Z}$ | x $\geq$1} $\supseteq \mathbb{N}$ Together, this shows that the equality stated above is correct.
### 3.4.4 The "Bag" Analogy It has been our experience that sets are a rather difficult notion to grasp when they are introduced. Specifically, the notation associated with sets throws students for a loop, and they end up writing down things that make no sense! It is essential to keep straight the differences between the symbols $\in and \subseteq$. Here is a helpful analogy to keep in mind: a set is like a bag with some stuff in it. The bag itself is irrelevant; we just care about what kind of stuffinside (i.e. what the elements are). Think of the bag as a non-descript plastic bag you'd get at the grocery store, even. All those bags are identical; to distinguish between any two bags, we need to know what kind of things are inside them.


> 🇨🇳 **3.4.3 集合相等** 两个集合 $A = B$ 当且仅当 $A \subseteq B$ 且 $B \subseteq A$。这是"双向包含"证明的基础。例：$\{x \in \mathbb{Z} \mid x \geq 1\} = \mathbb{N}$，因为两边互相包含。

> **3.4.4 "袋子"类比** 集合就像一个装了东西的袋子。袋子本身无关紧要，我们只关心里面有什么。把一个苹果和一个橙子放进袋子，放入的顺序无关紧要，也不管有几个同样的苹果——集合完全由其元素刻画。集合也可以是其他集合的元素——谁阻止我把一个袋子放进另一个袋子里？


If I put an apple and an orange in a grocery bag, surely it doesn't matter in what order I put them in. All you would need to know is that I have some apples and oranges. It also doesn't matter how many apples or oranges I have in the bag, because we only care about what kind of stuffis in there. Think of it as answering questions of the form "Are there any s in the bag? Yes or no?" It doesn't matter if I have two identical apples or seven or just one in my bag; if you ask me whether I have any apples, I'll just say "Yes". This is related to the notion that the order and repetition of elements in a set don't matter. A set is completely characterized by what its elements are. This also helps when we think about sets as elements of other sets, themselves. Who's to stop me from just putting a whole bag inside another bag¿ Look at the set A we defined in the example above: A = { $\emptyset, {1, \emptyset$} } This set A is a bag. What's inside the bag? There are two objects inside the bag (i.e. there are two elements of A). They both happen to be bags, themselves! One of them is a plain-old empty bag, with nothing inside it. (That's the empty set.) Okay, that's cool. The other one has two objects inside it. One of those objects is the number 1. Cool. The other such object is another empty bag. Distinguishing "\in" and "\subseteq" This analogy also helps with understanding the differences between "\in" and "\subseteq". Keep the example A in mind again. When we write x \in A, we mean x is an object inside the bag A. If we peeked into A, we would see an x sitting there at the bottom amongst the stuff. Let's use this idea to compare two examples. • We see that $\emptyset \in A$ is true here. If we look inside the bag A, we see an empty bag amongst the stuff(the elements). • We also see that {\emptyset} \notin A is true here. If we look inside the bag A, we don't see a bag containing only an empty bag. (This is what {\emptyset} is, mind you: an empty bag inside another bag.) Do you see such an object? Where? I defy you to show me, amongst the stuffinside the bag A, a bag containing only an empty bag. What do I see inside the bag A? Well, I see two things: an empty bag, and a bag that has two objects inside it (an empty bag, and the number 1). Neither of those objects is what we were looking for! When we write X \subseteq A, we mean that the two bags, X and A, are somehow comparable. Specifically, we are saying that all of the stuffinside X is also stuff inside A. We are really rooting through all of the objects inside X, taking them out one by one, and making sure we also see that object inside A. Let's use this idea to compare two examples. • We see that {\emptyset} $\subseteq A$ is true here. We are comparing the bag on the left with the bag on the right. What stuffis inside the bag on the left?


> 🇨🇳 **区分 $\in$ 和 $\subseteq$** 当我们写 $x \in A$ 时，意思是 $x$ 是袋子 $A$ 里的一个对象。$\emptyset \in A$ 为真——往袋子里看，我们能看到一个空袋子。$\{\emptyset\} \notin A$ 为真——我们看不到一个只包含空袋子的袋子。当写 $X \subseteq A$ 时，意思是袋子 $X$ 里的所有东西也在袋子 A 里。$\{\emptyset\} \subseteq A$ 为真——袋子里只有一个空袋子，而袋 A 里也有一个空袋子。$\{1\} \not\subseteq A$ 为真——1 不是直接放在袋 $A$ 底部的东西。


There's just one object in there, and it is an empty bag, itself. Now, we peek inside A. Do we also see an empty bag in there? Yes we do! Thus, the "$\subseteq$" symbol applies here. • We also see that {1} ̸\subseteq A is true here. To compare these two bags, we'll pull out an object from the bag on the left and see if it is also in the bag A. Here, we only have one object to pull out: the number 1. Now, let's peek inside the bag A. Do we see a 1 sitting in there amongst the stuff? No, we don't! We would have to peek inside something at the bottom of the bag A to find the number 1; that number isn't just sitting out in plain sight. Thus, {1} ̸\subseteq A. Look back over some examples we have discussed already with this new analogy in mind. Does it help you understand the definitions and examples? Does it help you understand the difference between "\in" and "\subseteq" and "$\supseteq$"? If not, can you think of another analogy that would help you?
### 3.4.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) Is N $\subseteq \mathbb{R}$? Is R $\subseteq \mathbb{N}$? Is Q $\subseteq \mathbb{Z}$? Why or why not? (2) What is the difference between \subset and \subseteq? Give an example of sets A, B such that A \subseteq B is True but A \subset B is False. (3) What is the difference between \in and \subseteq? Give an example of sets C, D such that C \subseteq D but C \notin D. (4) Let S be any set. What is the power set of S? What type of mathematical object is it? How is it defined? (5) Suppose S \subseteq T. Does this mean S = T? Why or why not? (6) Explain why $\emptyset \subseteq S and \emptyset \in P$(S) for any set S. (7) Suppose X $\in P$(A). How are X and A related, then? (8) Is it possible for A = P(A) to be true? (This one is rather tricky, but think about it!)


> 🇨🇳 **3.4.5 问题与练习** 自我提醒：(1) $\mathbb{N} \subseteq \mathbb{R}$ 吗？$\mathbb{R} \subseteq \mathbb{N}$ 吗？$\mathbb{Q} \subseteq \mathbb{Z}$ 吗？(2) $\subset$ 和 $\subseteq$ 的区别？(3) $\in$ 和 $\subseteq$ 的区别？(4) 集合 $S$ 的幂集是什么？(5) $S \subseteq T$ 意味着 $S = T$ 吗？(6) 为什么对任何 $S$ 有 $\emptyset \subseteq S$ 和 $\emptyset \in \mathcal{P}(S)$？(7) 若 $X \in \mathcal{P}(A)$，$X$ 和 $A$ 的关系是什么？(8) $A = \mathcal{P}(A)$ 可能成立吗？


Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Write out the elements of the set P(P($\emptyset$)). (2) Write out the elements of the sets P([1]) and P([2]) and P([3]). Can you make a conjecture about how many elements P([n]) has? (Can you prove it? We don't expect you to now, but soon enough; think about it!) (3) Let A = {x, ♥, {4} , \emptyset}. For each of the following statements, decide whether it is True or False and briefly explain why. (a) x \in A (b) x \subseteq A (c) {x, ♥} \subseteq A (d) {x, \emptyset} \subset A (e) {x, ♥, z, 7} \supseteq A (f) {x} \in P(A) (g) {x} \subseteq P(A) (h) {♥, x} \in P(A) (i) {4} \in P(A) (j) {\emptyset} \in P(A) (k) {\emptyset} \subseteq P(A) Hint: 7 of these are True, and 4 are False. (4) Give an example of sets A, B such that A \in B and A \subseteq B are both true. (5) Is {1, 2, 12} $\subseteq \mathbb{R}$? (6) Is {−5, 8, 12} $\subseteq \mathbb{N}$? (7) Is {1, 3, 7} \in P(N)? (8) Is N \in P(Z)? (9) Is P(N) \subseteq P(Z)? Are they equal sets? Why or why not? (10) Give an example of an infinite set T such that T \in P(Z) but T \notin P(N). (11) Suppose G, H are sets and they satisfy P(G) = P(H). Can we conclude that G = H? Why or why not? (Don't try to formally prove this; just think about it and try to talk it out.) (12) Give an example of a set W such that W \subseteq P(N) but W $\notin P$(N).


> 🇨🇳 **动手试试** (1) 写出 $\mathcal{P}(\mathcal{P}(\emptyset))$ 的元素。(2) 写出 $\mathcal{P}([1])$、$\mathcal{P}([2])$、$\mathcal{P}([3])$ 的元素。猜猜 $\mathcal{P}([n])$ 有多少元素？(3) 设 $A = \{x, \heartsuit, \{4\}, \emptyset\}$，判断各命题真伪。(4)-(12) 更多练习。


## 3.5 Set Operations When you first learned about numbers, a natural next step was to learn about how to combine them: multiplication, addition, and so on. Thus, a natural next step for us now is to investigate how we can take two sets and operate on them to produce other sets. How can we combine sets in interesting ways? There are several such operations that have standard, notational symbols and we will introduce you to those operations now. Throughout this section, we assume that we are given two sets A and B that are each subsets of a larger universal set U. That is, we assume A $\subseteq U and B \subseteq$ U. The reason we make this assumption is that each operation involves defining another set by identifying elements of a larger set with a specific property, so we must have some set U that is guaranteed to contain all of the elements of A and B so we can even work with those elements. (Again, ensuring this may seem nit-picky, but it is meant to avoid nasty paradoxes like the one we investigated before.) Assuming those sets A, B, U exist, though, we can forge ahead with our definitions.
### 3.5.1 Intersection This operation collects the elements common to two sets and includes them in a new set, called the intersection.
<div class="def-definition" markdown>
**Definition 3.5.1. Let A and B be any sets. The intersection of A and B**
</div>
is the set of elements that belong to both A and B, and is denoted by A $\cap B$. Symbolically, we define A \cap B = {x \in U | x \in A and x $\in B$}
Example 3.5.2. Define the following sets:
S1 = {1, 2, 3, 4, 5} S2 = {1, 3, 7} S3 = {2, 4, 7} U = N Then, we see that, for example, S1 $\cap S$2 = {1, 3} S1 \cap S3 = {2, 4} S2 \cap S3 = {7} Also, since S1 \cap S2 is, itself, a set, it makes sense to consider (S1 \cap S2) \cap S3. However, those two sets share no elements, so we write (S1 \cap S2) \cap S3 = $\emptyset$


> 🇨🇳 **3.5 集合运算** 正如学习数字之后自然学习加减乘除，学习集合之后自然研究集合运算。以下假设 $A, B \subseteq U$。

> **3.5.1 交集** $A \cap B = \{x \in U \mid x \in A \text{ 且 } x \in B\}$。例 3.5.2：$S_1 = \{1,2,3,4,5\}$，$S_2 = \{1,3,7\}$，$S_3 = \{2,4,7\}$。则 $S_1 \cap S_2 = \{1,3\}$，$S_2 \cap S_3 = \{7\}$，$(S_1 \cap S_2) \cap S_3 = \emptyset$。
