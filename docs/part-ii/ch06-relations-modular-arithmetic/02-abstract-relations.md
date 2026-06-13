---
title: Abstract (Binary) Relations
tags:
  - 关系
  - 等价关系
  - 序关系
  - 模运算
---

# Abstract (Binary) Relations

6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 上节定义了关系的基本概念并给出了 $A \neq B$ 时的例子。当 $A = B$ 时，关系 R 定义在同一个集合的元素对上，这是最常见也最重要的情形。下面继续看几个这样的例子及关于关系的基本观察。


Example 6.2.5. Let A = B = $\mathbb{Z}$ and define a relation R on $\mathbb{Z}$ by setting
$(x, y) \\in R \\Leftrightarrow x and y$ have the same parity Then $(2, 8) \in \mathbb{R} and (-3, 7) \in \mathbb{R} and (-99, -99) \in \mathbb{R}, but (1, 2) \\notin R and (0, -3) \\notin R and (\pi, 0) \\notin R (since \pi \notin \mathbb{Z}$).
Example 6.2.6. Define a relation L on $\mathbb{R}$ by setting
$(x, y) \\in L \\Leftrightarrow x < y$. Then $(-1, \\pi) \\in L$ and $(0, 100) \\in L$ but $(2, 2) \\notin L$ and $(\\pi, -1) \\notin L$. Notice that these are ordered pairs (which we may forget about since $A = B = \mathbb{R}$) so the order of the elements matters. Indeed, knowing that $(x, y) \\in L$ doesn\'t necessarily imply that $(y, x) \\in L$, in general. In this example, that implication is always False, in fact! Recall that we sometimes write x \, L \, y to say (x, y) \in L, so let us note that we could say $-1 \\, L \\, \\pi$ but $\\pi \\not L \\, -1$ here, and $2 \\not L \\, 2$. The Empty Relation
Remark 6.2.7. The examples we have seen thus far are interesting relations, in
some sense. Given any x, $y \\in R$, we can determine whether x < y or not by just comparing them and deciding whether that property holds. That is, each of the examples we have seen thus far were defined by saying $(a, b) \\in R \\Leftrightarrow P(a, b)$ is true for some property P(a, b). A relation doesn't necessarily need to be defined this way, though. For instance, we know $\\emptyset \\subseteq S$ for any set $S$. Thus, given two sets, we can always define the trivial relation by using the fact that $\\emptyset \\subseteq A \\times B$; that is, the trivial relation is the one where no elements are related! This is relatively "uninteresting" for sure, but it still satisfies the definition of a relation, so we allow it. Any Set of Ordered Pairs is a Relation
Remark 6.2.8. Given sets A, B, any subset $R \\subseteq A \\times B$ defines a relation. It
might be difficult (or impossible, perhaps) to identify a property that characterizes that relation. For instance, if $A = \\{1, 3, 5\\}$ and $B = \\{\\star, \\heartsuit\\}$, then we can define a relation between A and B by setting $R = \\{(1, \\star), (5, \\heartsuit)\\}$ Why is 1 related to $\star$? Why is 3 not related to anything? Who knows? It's just a set of ordered pairs! This is, mathematically speaking, totally fine.


> 🇨🇳 **例 6.2.5.** 设 $A = B = \mathbb{Z}$，定义 $\mathbb{Z}$ 上的关系 R：$(x, y) \\in R \\Leftrightarrow x$ 与 $y$ 具有相同的奇偶性（Parity）。则 $(2, 8) \\in R$（均为偶数），$(-3, 7) \\in R$（均为奇数），$(-99, -99) \\in R$，但 $(1, 2) \\notin R$、$(0, -3) \\notin R$，且 $(\pi, 0) \\notin R$（因为 $\pi \notin \mathbb{Z}$）。
>
> **例 6.2.6.** 在 $\mathbb{R}$ 上定义关系 L：$(x, y) \in L \Leftrightarrow x < y$。注意这些是有序对（Ordered Pair），元素的顺序很重要。知道 $(x, y) \in L$ 并不蕴含 $(y, x) \in L$，事实上在本例中该蕴含永远为假！我们有时也写 $x \, L \, y$ 来表示 $(x, y) \in L$。
>
> **空关系** **注 6.2.7.** 迄今所有例子都通过某个性质 P(a, b) 定义：$(a, b) \\in R \\Leftrightarrow P(a, b)$ 为真。但关系不一定需要如此定义。由 $\\emptyset \\subseteq A \\times B$，我们可定义**空关系**（平凡关系）——没有任何元素相关的关系。这虽然"无趣"，但满足关系的定义。
>
> **任何有序对的集合都是关系** **注 6.2.8.** 给定集合 A、B，任何子集 $R \subseteq A \times B$ 都定义了一个关系，即使很难（甚至不可能）找到刻画它的性质。例如，若 A = {1, 3, 5}，B = {\star, ♥}，则 $R = \{(1, \text{\star}), (5, \text{♥})\}$ 就定义了一个关系。为什么 1 与 $\star$ 相关？为什么 3 不与任何元素相关？谁知道呢——它就是一个有序对的集合！在数学上完全合法。


The Equality Relation
Example 6.2.9. Another example of a way to define a relation on any set X is to
define the equality relation. That is, let $(x, y) \\in R \\Leftrightarrow x = y$. Notice that this doesn't depend on what X is or what types of objects it contains as elements, merely that it is a set. Similarities Between Relations
Example 6.2.10. Let S be the set of students in your class. Define a relation
R1 between S and N by saying $(s, n) \\in R_1$ if person $s \\in S$ is $n$ years old. Write out a few elements of this relation set. Now, define a relation $\mathbb{R}^2$ on S itself by saying $(s, t) \\in R_2$ if persons $s$ and $t$ are the same age (in years). Write out a few elements of this relation set. How do the relations R1 and $\mathbb{R}^2$ compare? Do they somehow "encode" the same information about the elements of the set S? Why or why not? Is there a way we can use R1 to determine $\mathbb{R}^2$? What about the other way around? Think about this carefully and try to write a few sentences that summarize your thoughts about this. We will adress these questions immediately in the next subsection, but take some time now to investigate on your own! Relations "Encode" Information The previous example is meant to illustrate the real use of abstract relations and motivate why we even talk about them at all (besides our overarching goal of rigorizing the notion of a function). In some sense, a relation is a way of "storing" information about elements of two sets, or one set; it's a way of comparing two elements and declaring whether or not they satisfy some property. In a more general sense, though, a relation can provide information about how "well" a set's (or sets') elements behave in terms of a specific property. For instance, notice that in the previous example, the relation R1 told us a little "more" about the elements of S. Certainly, R1 tells us who is the same age as anyone else: we can look for two pairs like (s, n) and (t, n), say, with the same second coordinate. But R1 also tells us what that age is: just look at that second coordinate the pairs share. This does not work with $\mathbb{R}^2$. Knowing $(s, t) \\in R_2$ just tells us students $s$ and $t$ are the same age; it does not tell us what that age is! In that sense, R1 is a "better" relation and provides "more" information. There are also reasons why $\mathbb{R}^2$ is "better", too, though! For example, look at one of its nice properties: if (x, y) $\\in R$2, it is necessarily true that (y, x) $\\in R$2, as well. This is certainly not true of R1 because when $(s, n) \\in R_1$, it doesn't even make sense to say whether or not $(n, s) \\notin R_1$ because the order of the pair does not match the domain and codomain! Does this property now make $\mathbb{R}^2$ a "better" relation? Well, yes and no. It depends on context and what type of information we want to encode and retrieve. In certain situations, maybe you'd want to use R1, and other times you'd want $\mathbb{R}^2$.


> 🇨🇳 **相等关系** **例 6.2.9.** 在任何集合 X 上可定义相等关系（Equality Relation）：$(x, y) \\in R \\Leftrightarrow x = y$。注意这不依赖于 X 的具体内容，仅要求它是一个集合。
>
> **关系之间的相似性** **例 6.2.10.** 设 S 为班上学生集合。在 S 与 $\mathbb{N}$ 之间定义 $R_1$：$(s, n) \in \mathbb{R}_1$ 当且仅当学生 s 的年龄为 n 岁。在 S 上定义 $R_2$：$(s, t) \in \mathbb{R}_2$ 当且仅当 s 和 t 同岁。$R_1$ 和 $R_2$ 是否"编码"了相同的信息？能否由 $R_1$ 推出 $R_2$？反过来呢？
>
> **关系"编码"信息** 关系的核心用途是一种"存储"集合元素信息的方式——一种比较两个元素并声明它们是否满足某性质的方法。$R_1$ 提供了"更多"信息：既知道谁和谁同岁，又知道具体年龄。$R_2$ 只告诉我们两个学生同岁，却不告知年龄。但 $R_2$ 也有其优势：若 $(x, y) \in \mathbb{R}_2$，则必然 $(y, x) \in \mathbb{R}_2$。这对 $R_1$ 不成立，因为 $(s, n) \in \mathbb{R}_1$ 时，$(n, s) \in \mathbb{R}_1$ 的序与定义域和陪域不匹配。哪种关系"更好"取决于具体语境和我们要编码与检索的信息类型。


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 我们稍有些超前了——目前还无法描述这些性质意味着什么以及它们是否令人期望。但我们确实好奇这些性质在什么情况下成立（或不成立），尤其是当一个关系中**所有**元素对都具有（或不具有）某性质时。下一小节将定义和探讨抽象关系的几种常见性质。任何关系并不保证（也不要求）拥有其中一个或多个性质，但这些性质在数学和实际应用中已被证明是有趣且有用的。之后我们将看到大量关系的例子，并讨论如何证明这些性质成立或反证其不成立。在此过程中，我们还将培养处理关系的直觉，甚至弄清楚我们首先想要证明什么样的命题！


But we're getting slightly ahead of ourselves here! We can't yet describe to you what these properties mean and why they may or may not be desirable. On the whole, though, we are curious about these types of properties and when they do (and do not) hold for all pairs of elements in a given set. In the next subsection, we will define and explore several common properties of abstract relations. It is not a guarantee (or requirement) that any relation possess one or more of these properties, but these are the ones that have proven to be interesting and useful in the mathematical and real-world contexts in which relations arise. After that, we'll see lots of examples of relations and discuss how to prove these properties hold. While doing this, we'll develop some intuitions for how to work with relations and even figure out the kinds of claims we'd be trying to prove in the first place!
### 6.2.2 Properties of Relations Let's start right offby defining a few properties. For each of these properties, every relation either does or does not satisfy it. We encourage you to read each property one by one and try to construct a relation that does satisfy the property, and then one that doesn't. This will help you truly understand the underlying principles of the property and how relations work. (Then, try to define some relations that have some combination of the properties!) After these definitions, we will provide some canonical examples that you might have even come up with yourself! But seriously, do try to come up with some on your own and share any interesting ones that you have!
Definitions: Properties of a Relation on a Set
These properties rely on being able to reverse the order of a pair. That is, given $(x, y) \\in R$, we might wonder about the pair (y, x); however, the relationship between the domain and codomain demands that $(y, x) \in A \times B$, as well. Thus, we will require $A \times B = B \times A$, which only happens when $A = \\emptyset$ or $B = \\emptyset$ or $A = B$. (Remember we proved this earlier when talking about sets in Chapter 3!) Since $A = \emptyset and B = \emptyset$ are uninteresting cases, we will assume in these properties that $A = B$ (and $A \\neq \\emptyset$), so we are defining a relation on one non-empty set and comparing its elements with each other.
<div class="def-definition" markdown>
**Definition 6.2.11. Let A be a set and let R be a relation on A, i.e. $R \\subseteq A \\times A$.**
</div>
• We say $R$ is reflexive if $\\forall x \\in A.\\, (x, x) \\in R$. That is, every element is related to itself. • We say $R$ is symmetric if $\\forall x, y \\in A.\\, (x, y) \\in R \$\Rightarrow$ (y, x) \\in R$. That is, the order of the comparison doesn't matter.


> 🇨🇳 **6.2.2 关系的性质** 让我们直接定义几个性质。对于每个性质，每个关系要么满足它，要么不满足。我们建议你逐一阅读每个性质，并尝试构造一个满足该性质的关系和一个不满足的关系——这将帮助你真正理解性质背后的原理以及关系的工作方式。
>
> **定义：集合上关系的性质** 这些性质依赖于能够交换有序对的顺序——即给定 $(x, y) \\in R$，我们可能想考察 $(y, x)$；然而这要求域和陪域的关系能满足 $(y, x) \in A \times B$，因此需要 $A \times B = B \times A$，而这仅在 $A = \emptyset$ 或 $B = \emptyset$ 或 $A = B$ 时成立。由于 $A = \emptyset$ 和 $B = \emptyset$ 是无趣的情形，我们假定 A = B（且 $A \neq \emptyset$），即在同一个非空集合上定义关系并比较其元素。
>
> **定义 6.2.11.** 设 A 为集合，R 为 A 上的关系，即 $R \\subseteq A \\times A$。
>
> • 若 $\forall x \in A. (x, x) \\in R$，则称 R 是**自反的**（Reflexive），即每个元素与自身相关。
> • 若 $\forall x, y \in A. (x, y) \in \mathbb{R} $\Rightarrow$ (y, x) \\in R$，则称 R 是**对称的**（Symmetric），即比较的顺序无关紧要。


• We say $R$ is transitive if $\\forall x, y, z \\in A.\\, [(x, y) \\in R \\wedge (y, z) \\in R] \$\Rightarrow$ (x, z) \\in R$ That is, relationships can transition through a middle-man. • We say $R$ is anti-symmetric if $\\forall x, y \\in A.\\, [(x, y) \\in R \\wedge (y, x) \\in R] \$\Rightarrow$ x = y$ That is, two different elements can be related in at most one way, or not at all. To see why this is the same statement, let's look at the contrapositive of the conditional statement in the line above: $\\forall x, y \\in A.\\, x \\neq y \$\Rightarrow$ [(x, y) \\notin R \\vee (y, x) \\notin R]$
Note: it is important to point out that anti-symmetric is NOT the same
as not symmetric. Look carefully at the logical order and quantifiers of the properties to make sense of this. For example, the $\\leq$ relation on $\\mathbb{R}$ is antisymmetric but not symmetric. Think about why this is the case. In fact, try to come up with a relation that is both anti-symmetric AND symmetric. It actually isn't that hard! We've already mentioned one fundamental relation that has this property.
### 6.2.3 Examples
Again, try to come up with some relations that do and do not satisfy the four properties we just defined. We will present some nice, canonical examples of relations defined on $\mathbb{N}$ below to give you some concrete ideas to keep in mind. Feel free to add to this list as you come up with simple examples, perhaps defined on other sets like $\mathbb{Z}$ and $\mathbb{R}$.
Example 6.2.12. Throughout this example, relations are defined on the set $\mathbb{N}$.
• Define $R_1$ on $\\mathbb{N}$ by $(x, y) \\in R_1 \\Leftrightarrow x$ divides $y$ (i.e. $y$ is divisible by $x$, or $\\exists k \\in \\mathbb{N}$ such that $y = kx$. This definition is formally restated below; see Definition 6.2.15) Then $R_1$ is reflexive, because $x | x$ since $x = 1 \cdot x$. The divisibility relation is reflexive. • Define $R_2$ on $\\mathbb{N}$ by $(x, y) \\in R_2 \\Leftrightarrow x$ and $y$ have the same parity Then $R_2$ is symmetric because if x and $y$ have the same parity then certainly y and $x$ have the same parity. The "has the same parity" relation is symmetric.


> 🇨🇳 • 若 $\\forall x, y, z \\in A.\\, [(x, y) \\in R \\wedge (y, z) \\in R] \$\Rightarrow$ (x, z) \\in R$，则称 R 是**传递的**（Transitive），即关系可以通过"中间人"传递。
>
> • 若 $\\forall x, y \\in A.\\, [(x, y) \\in R \\wedge (y, x) \\in R] \$\Rightarrow$ x = y$，则称 R 是**反对称的**（Anti-symmetric），即两个不同元素至多以一种方式相关（或完全不相关）。等价地，观察条件语句的逆否命题：$\\forall x, y \\in A.\\, x \\neq y \$\Rightarrow$ [(x, y) \\notin R \\vee (y, x) \\notin R]$。
>
> **注意：** 反对称（anti-symmetric）**并非**"不对称"（not symmetric）。仔细审视这些性质的逻辑顺序和量词以理解这一点。例如，$\mathbb{R}$ 上的 $\leq$ 关系是反对称的但不是对称的。事实上，可以构造一个同时满足对称且反对称的关系——这并不困难，我们已提及的一个基本关系就具有此性质。
>
> **例 6.2.12.** 以下关系定义在 $\mathbb{N}$ 上。
> • 定义 $R_1$：$(x, y) \in \mathbb{R}_1 \Leftrightarrow x$ 整除 $y$（即 $y$ 可被 $x$ 整除，或 $\exists k \in \mathbb{N}$ 使得 $y = kx$）。$R_1$ 是自反的，因为 $x | x$（取 $x = 1 \cdot x$）。整除关系是自反的。
> • 定义 $R_2$：$(x, y) \in \mathbb{R}_2 \Leftrightarrow x$ 和 $y$ 具有相同的奇偶性。$R_2$ 是对称的，因为若 $x$ 和 $y$ 具有相同奇偶性，则 $y$ 和 $x$ 当然也具有相同奇偶性。同奇偶性关系是对称的。


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 • 定义 $R_3$：$(x, y) \in \mathbb{R}_3 \Leftrightarrow x < y$。$R_3$ 是传递的，因为若 $x < y$ 且 $y < z$，则 $x < y < z$，即 $x < z$。"$<$" 关系是传递的。
>
> • 定义 $R_4$：$(x, y) \in \mathbb{R}_4 \Leftrightarrow x \leq y$。$R_4$ 是反对称的，因为若 $x \leq y$ 且 $y \leq x$，则 $x \leq y \leq x$，即 $x = y$。"$\leq$" 关系是反对称的。
>
> **例 6.2.13.** 记住关系只是有序对的集合，不必由性质定义。设 S = {a, b, c}，定义关系 $R = \{(a, a), (a, c), (b, c), (c, b)\}$。则 R：• 不自反：$(c, c) \\notin R$；• 不对称：$(a, c) \\in R$ 但 $(c, a) \\notin R$；• 不传递：$(a, c) \\in R$ 且 $(c, b) \\in R$ 但 $(a, b) \\notin R$；• 不反对称：$(b, c) \\in R$ 且 $(c, b) \\in R$ 但 $b \neq c$。
>
> **例 6.2.14.** 练习使用不同的关系记号。设 S 为班上所有人的集合，定义关系 $\star$：$x \star y \Leftrightarrow x$ 和 $y$ 出生在同一个月。则该关系是自反的（每个人与自己同月出生，即 x \star x）、对称的（若 x \star y 则 $y \star x$）、传递的（"相同"这个概念反复适用）。


• Define $R_3$ on $\\mathbb{N}$ by $(x, y) \\in R_3 \\Leftrightarrow x < y$. Then $R_3$ is transitive because if $x < y and y < z then x < y < z, so x < z$. The "$<$" relation is transitive. • Define $R_4$ on $\\mathbb{N}$ by $(x, y) \\in R_4 \\Leftrightarrow x \\leq y$. Then $R_4$ is anti-symmetric because if $x \leq y and y \leq x then x \leq y \leq x so x = y$. The "$\leq$" relation is anti-symmetric.
Example 6.2.13. Remember that a relation is just a set of ordered pairs. We
don't have to define it in terms of a property. Let's see an example phrased this way, and investigate its properties: Define the relation $R$ on the set $S = \\{a, b, c\\}$ by $R = \\{(a, a), (a, c), (b, c), (c, b)\\}$ Notice that this relation is: • Not Reflexive: $(c, c) \\notin R$ • Not Symmetric: $(a, c) \\in R$ but $(c, a) \\notin R$ • Not Transitive: $(a, c) \\in R$ and $(c, b) \\in R$ but $(a, b) \\notin R$ • Not Anti-Symmetric: $(b, c) \\in R$ and $(c, b) \\in R$ but $b \\neq c$
Example 6.2.14. Let's get a little practice using slightly different notation for
relations. Remember that we can also write something like $x \\, R \\, y$ to mean $(x, y) \\in R$. Define the relation \star on the set S of people in your class by saying, for any x, y \in S, $x \star y \Leftrightarrow x and y$ were born in the same month We claim that this relation is reflexive, symmetric, and transitive. Do you see why? • The relation is reflexive because each person is certainly born in the same month as themself (i.e, x \star x). • The relation is symmetric because if person x and person y were born in the same month (i.e. x \star y), then certainly person y and person x (just a different order!) were born in the same month (i.e. $y \star x$). • The relation is transitive because... well, you get the idea, right? We're just appealing to the concept of the word "same" over and over!


> 🇨🇳 关于反对称性呢？这取决于具体班级：如果有两个不同的人出生在同一个月，则该关系**不是**反对称的；但如果每个人都出生在不同的月份，则是反对称的（因为没有人和自己以外的任何人相关）。仔细想想这一点...


What about anti-symmetry here? It depends! Are there two different people in your class that were born in the same month? If so, this relation is not antisymmetric. However, was everybody in your class born in a different month? If so, this relation is anti-symmetric, because no one will be related to anybody but themself! Think about this...
### 6.2.4 Proving/Disproving Properties of Relations When we are presented with a set and a relation on that set, we will immediately wonder whether any of these properties hold. By playing around with some particular elements of the set in question, we can try to conjecture whether or not the relation satisfies a property, and then attempt to prove/disprove it. This sometimes amounts to a bit of "guessing and checking" but, ultimately, to prove a property holds, we must prove a statement of the form "For all... it is true that... ". (Look back at our proof techniques from Section 4.9!) Thus, proving a relations property amounts to taking an arbitrary element (or elements) and arguing about how they are related. To disprove such a statement, we would prove its logical negation, which is of the form "There exists... such that...." (Again, look back at our proof techniques!) Thus, disproving a property amounts to finding a counterexample. Let's look at a couple of examples of proving/disproving relation properties. There are several more examples of these styles of proofs in the exercises, as well. The "Divides" Relation on $\mathbb{Z}$ We will present (or, perhaps, remind you of) one definition first, because it will be the basis of one of our examples. This is a formal definition of what it means for one integer to divide another integer.
<div class="def-definition" markdown>
**Definition 6.2.15. Let $a, b \\in \\mathbb{Z}$. We say $x$ divides $y$, and write $x \\mid y$, if and**
</div>
only if $\\exists k \\in \\mathbb{Z}.\\, y = kx$
Example 6.2.16. Define the relation R on $\mathbb{Z}$ by
$(x, y) \\in R \\Leftrightarrow x \\mid y$ Let's determine whether R satisfies any of the four properties of relations, and then prove/disprove all our claims! In general, depending on the set and relation in question, you might immediately notice whether or not a property holds, via some intuition or just being able to "see" it right away. If so, great! If not (which is far more likely) we recommend starting a "proof" as if a property actually held, and seeing if you can finish. If you do, well then, you just proved the property! If you struggle at some point, maybe that's because the property doesn't hold, and the point in your proof where you're caught up will give you some insight into finding a counterexample. This strategy doesn't always work (maybe you're


> 🇨🇳 **6.2.4 证明/证反关系的性质** 给定一个集合及其上的关系，我们会立即想知道哪些性质成立。通过尝试集合中的一些具体元素，我们可以猜测关系是否满足某个性质，然后尝试证明或证反。证明一个性质成立需要证明形如"对所有……，……为真"的命题（回顾第 4.9 节的证明技巧），即取任意元素并论证它们如何相关。证反则需要找到反例——证明存在……使得……。
>
> **$\mathbb{Z}$ 上的"整除"关系** 先给出一个定义，因为它是我们其中一个例子的基础。
>
> **定义 6.2.15.** 设 $a, b \in \mathbb{Z}$。我们说 $x$ 整除 $y$，记作 $$x \\mid y$$，当且仅当 $\exists k \in \mathbb{Z}$ 使得 $y = kx$。
>
> **例 6.2.16.** 在 $\mathbb{Z}$ 上定义关系 R：$(x, y) \\in R \\Leftrightarrow x \\mid y$。让我们判定 R 是否满足四个关系性质，然后对每个论断给出证明或证反！
>
> 一种常用策略是：先假设性质成立并开始写"证明"，如果能完成则性质得证；如果在某处卡住，那个卡住的地方可能恰好提供了反例的线索。另一种更简单的策略是：用自然语言大声说出关系和所问性质的含义——有时候用日常语言而非抽象符号思考，会让你的大脑领悟某些有用的东西！


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 我们将在下面的例子中看到上述策略的实际运用。
>
> • R 是否自反？用自然语言来说：**"任何整数都能被自身整除。"** 当然可以！取任意 $x \in \mathbb{Z}$，则 $x | x$，因为 $x = 1 \cdot x$ 且 $1 \in \mathbb{Z}$。故 $(x, x) \\in R$，R 是自反的。大声思考帮助我们意识到这一事实，使之更容易用数学语言表达。


struggling through a proof because it's actually challenging, say) but it can be quite helpful, so keep it in mind. We will see it in action in this example, too. One other strategy---an even simpler one, actually---is to just make a statement out loud, or write down in words what the relation and the property in question is. Sometimes, just making yourself say something in plain language, instead of reading abstract symbols on the page, will force you brain into realizing something helpful! We'll see this strategy in action here, too. • Let's see if $R$ is reflexive. What would that actually mean? Let's make ourselves say this out loud. Would we expect that: "Any integer is divisible by itself." Of course! Now, let's try to write that down in the symbolic terms required in a proof.
<div class="def-proof" markdown>
*Proof.* We claim $R$ is reflexive. Let x $\in \mathbb{Z}$ be arbitrary and fixed. Then
</div>
x | x since x = 1 $\cdot x and 1 \in \mathbb{Z}. Thus, (x, x) \\in R$. Therefore, $R$ is reflexive. Voil`a! Just thinking out loud helped us realize a fact, and that made it easier for us to write down that statement in mathematical language. • Let's see if $R$ is symmetric. This property is defined in terms of an implication, a conditional statement. So, let's assume we have an arbitrary related pair, (x, y) $\\in R$. Would we necessarily believe (y, x) $\\in R$, too? Said another way: Assuming x divides y, can we also say that y divides x? This actually seems rather unlikely! Knowing $x \\mid y$ tells us that $y = kx$ for some $k \\in \\mathbb{Z}$, but why would that lead us to believe that $x = \\frac{1}{k} y$ means $y \\mid x$? What if 1 k $\notin \mathbb{Z}$? You might be tempted at this point to say something like "Well, 1 k is only an integer when k = 1 or k = -1 so that's that." That isn't quite a full explanation! Remember that to disprove a "For all... " claim, we need to provide an explicit counterexample whenever possible. We don't need to characterize all of the cases where the property does and does not hold and try to explain things in generality. We just need an example to convince someone that the property does not hold. This is much more illustrative and direct than flailing our arms about and pointing out how some counterexample exists out there somewhere. Let's just show our reader one and move on!
<div class="def-proof" markdown>
*Proof.* Consider 2, 6 $\in \mathbb{Z}$. Since $6 = 3 \\cdot 2$, we have $(2, 6) \\in R$.
</div>
However, writing 2 = ℓ $\cdot$ 6 requires ℓ= 1 3, and 1 3 $\notin \mathbb{Z}. Thus, (6, 2) \\notin R$. This shows that $R$ is not symmetric.


> 🇨🇳 • R 是否对称？假设 $(x, y) \\in R$，即 $$x \\mid y$$，能否推出 $y | x$？这看起来不太可能！$$x \\mid y$$ 意味着 $y = kx$（$k \in \mathbb{Z}$），但 $x = \frac{1}{k} y$ 中的 $\frac{1}{k}$ 未必是整数。我们只需提供一个明确的反例：取 $2, 6 \in \mathbb{Z}$，因 $6 = 3 \cdot 2$，有 $(2, 6) \\in R$。但 $2 = \ell \cdot 6$ 要求 $\ell = \frac{1}{3}$，而 $\frac{1}{3} \notin \mathbb{Z}$，故 $(6, 2) \\notin R$。这表明 R 不是对称的。注意我们不需要分析所有不能成立的情况——只需给出一个具体反例即可。


• Let's see if $R$ is transitive. In general, transitivity is typically the most difficult property to think about. This is partly due to the fact that it's defined by a conditional statement with two hypotheses, and it uses three variables. In this specific example, we will assume $x \\mid y$ and y | z, and then wonder whether x | z necessarily. Try saying that out loud with words and seeing if you believe it or not. It seems like it's true, right? Now, try writing down the hypotheses and the conclusion in mathematical language. Can you see how to piece those together? Try writing out your version of this proof before reading on.
<div class="def-proof" markdown>
*Proof.* Let x, y, $z \in \mathbb{Z}$ be arbitrary and fixed. Suppose $(x, y) \\in R$ and
</div>
$(y, z) \\in R$. This means $x \\mid y$ and $y \\mid z$, so \exists k, ℓ$\in \mathbb{Z}$ such that y = kx and z = ℓy. Let such k, ℓbe given. Substituting the first equation into the second, we find that z = ℓy = ℓ(kx) = (kℓ)x Since kℓ$\in \mathbb{Z}$, as well, we have shown that x | z. Thus, $(x, z) \\in R$, necessarily. Therefore, $R$ is transitive. • Let's see if $R$ is anti-symmetric. This property is also defined by a conditional statement with two hypotheses, so we will assume we have an x and a y and that $x \\mid y$ and y | x. Can we conclude that x = y? This question hearkens back to proving that R was not symmetric. Remember, we proved that $x \\mid y$ does not necessarily imply y | x and, actually, if you thought about it for a moment, it's actually very unlikely that $x \\mid y$ and y | x can both be true. How can this be? Think about it carefully and try to come up with your own proof before you read ours.
<div class="def-proof" markdown>
*Proof.* Let x, y $\in \mathbb{Z}$ be arbitrary and fixed. Suppose $(x, y) \\in R$ and $(y, x) \\in R$. This means $x \\mid y$ and y | x, so \exists k, ℓ$\in \mathbb{Z}$ such that y = kx and x = ℓy. Let such k, ℓbe given. Substituting the first equation into the second, we find that y = kx = k(ℓy) = (kℓ)y. We now have two cases. Case 1: Suppose y = 0. Then we cannot divide both sides by y. Instead, we observe that x = ℓy = ℓ \cdot 0 = 0, and therefore x = 0, as well. Thus, x = y in this case. Case 2: Suppose $y \\neq 0$. Then we can divide both sides by $y$. This yields kℓ= 1. Since k, ℓ$\in \mathbb{Z}$ this means either k = ℓ= 1 or k = ℓ= -1.
</div>


> 🇨🇳 • R 是否传递？传递性通常是最难思考的性质，部分原因在于它的定义涉及两个前提和三个变量。假设 $$x \\mid y$$ 且 $y | z$，$x | z$ 是否一定成立？用自然语言来说似乎成立。用数学语言写出来：取任意 $x, y, z \in \mathbb{Z}$，设 $$x \\mid y$$ 且 $y | z$，则 $\exists k, \ell \in \mathbb{Z}$ 使得 $y = kx$，$z = \ell y$。代入得 $z = \ell y = \ell(kx) = (k\ell)x$。因为 $k\ell \in \mathbb{Z}$，所以 $x | z$，即 $(x, z) \\in R$。因此 R 是传递的。
>
> **证法。** 取任意 $x, y \in \mathbb{Z}$，设 $(x, y) \\in R$ 且 $(y, x) \\in R$，即 $$x \\mid y$$ 且 $y | x$。则 $\exists k, \ell \in \mathbb{Z}$ 使得 $y = kx$，$x = \ell y$。代入得 $y = kx = k(\ell y) = (k\ell)y$。分两种情况：若 $y = 0$，则 $x = \ell \cdot 0 = 0$，所以 $x = y$。若 $y \neq 0$，除以 $y$ 得 $k\ell = 1$。由 $k, \ell \in \mathbb{Z}$，要么 $k = \ell = 1$，要么 $k = \ell = -1$。如果 $k = \ell = 1$，则 $x = y$。但在另一种情况下...


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 糟糕！后一种情况（$k = \ell = -1$）意味着 $y = -x$。例如 $y = 3$，$x = -3$ 时，$$x \\mid y$$ 且 $y | x$ 但 $x \neq y$。这就是我们需要的反例！尝试完成"证明"帮助我们找到了它。
>
> 反例：取 $x = 3$，$y = -3$。$$x \\mid y$$（因为 $3 = (-1)(-3)$）且 $y | x$（因为 $-3 = (-1) \cdot 3$），且 $-1 \in \mathbb{Z}$。但显然 $x \neq y$。因此 R 不是反对称的。
>
> **后续思考**：将此关系定义在 $\mathbb{N}$ 上时，哪些性质会改变？在 \mathbb{N} 上，"整除"关系同时满足自反、传递和反对称（因为 \mathbb{N} 不含负数，k\ell = 1 只能推出 k = \ell = 1，从而 $x = y$），但仍不对称。这些答案将引出下一小节的内容。
>
> **构造具有特定性质的关系** 有趣的"游戏"是：取一个集合，构造满足特定性质子集的关系 R（4 个性质共有 16 种组合方式）。**例 6.2.17.** 目标：设 S 为班上学生集合，定义关系 R 使其满足 (1) 不自反、(2) 不对称、(3) 传递、(4) 反对称。要保证不自反，需确保没有任何元素与自身相关；不对称需 $(x, y) \\in R$ 时 $(y, x) \\notin R$；传递需 $(x, y) \\in R$ 且 $(y, z) \\in R$ 时 $(x, z) \\in R$；反对称的逆否形式要求任何两个元素至多以一种方式相关。性质 (1) 要求定义不能含有"或等于"的形式，性质 (2) 要求定义只能以"一种方式"关联 x 和 y。我们可以猜测一种比较性质可能有效——类似于 $\mathbb{Z}$ 上的"小于"关系。让我们试试。


If k = ℓ= 1, then x = ℓy = y. In the other case... ̸ Oh, shucks! This doesn't work! Do you see what happened? In "most" of the cases, we did conclude that x = y, but there is actually a possibility that y = -x. For instance, when y = 3 and x = -3, notice that $x \\mid y$ and y | x but x $\neq$ y. THIS is the counterexample we need, and trying to finish our "proof" helped us find it. Perhaps you saw this case coming all along; if so, way to go! Let's wrap this up by presenting that counterexample:
<div class="def-proof" markdown>
*Proof.* Consider $x = 3$ and $y = -3$, so $x, y \\in \\mathbb{Z}$. Notice that $x \\mid y$ and
</div>
y | x because $3 = (-1)(-3)$ and $-3 = (-1) \\cdot 3$, and since $-1 \\in \\mathbb{Z}$. However, certainly x $\neq$ y. This shows that R is not anti-symmetric. As a follow-up question, consider what happens when we define this relation on the set $\mathbb{N}$ instead of $\mathbb{Z}$. What changes? Which properties hold now? Are any answers different than with $\mathbb{Z}$? Do think about this. The answers to those questions will motivate our next subsection. Constructing a Relation with Specific Properties One more example before we move on. An interesting "game" to play is to take a set and construct a relation R that satisfies some specific subset of the four properties. (Note: there are 16 different ways that the 4 properties can/cannot hold.) We will ask you questions like this in the exercises, so let's work through one example here.
Example 6.2.17. Goal: Let S be the set of students in this class. Define a
relation R that is (1) not reflexive, (2) not symmetric, (3) transitive, and (4) anti-symmetric. To ensure that $R$ is not reflexive, we must make sure that no element is related to itself. To ensure $R$ is not symmetric, we must make sure that whenever a pair $(x, y) \\in R$, then $(y, x) \\notin R$. To ensure $R$ is transitive, we must make sure whenever $(x, y) \\in R$ and $(y, z) \\in R$, then $(x, z) \\in R$. And to ensure $R$ is anti-symmetric, we will think of the contrapositive form of the property's definition, which requires that any pair of elements is related in at most one way. This last property is perhaps the hardest to think about; it says that for every x, y \in S, either x is related to y but not the other way, or else y is related to x and not the other way, or else x and y just aren't related either way. That is, we must not allow any pairs to satisfy both $(x, y) \\in R$ and $(y, x) \\in R$. (Again, reread the definition of anti-symmetric and write down the contrapositive of the conditional statement and think about why this works.) Now let's try to construct R so that it satisfies these properties. Property (1) means that our definition can't allow anything of the form "or is equal to", and (2) means that the definition must relate any x and y in "only one way". Thus, we might guess that a comparison property, something like the "less than" relation on $\mathbb{Z}$, might work. Let's try it out and attempt to prove/disprove the desired properties.


> 🇨🇳 定义 S 上的关系 R：$x \, \mathbb{R} \, y \Leftrightarrow x$ 严格比 $y$ 年轻（以年计）。验证其性质：
>
> • R **不自反**：任何人 $x$ 与自己同龄，故 $x \not \mathbb{R} \, x$。
> • R **不对称**：若 $x$ 严格比 $y$ 年轻，则 $y$ 严格比 $x$ 年长，故 $y \not \mathbb{R} \, x$。
> • R **传递**：若 $x$ 严格比 $y$ 年轻且 $y$ 严格比 $z$ 年轻，则 $x$ 严格比 $z$ 年轻。
> • R **反对称**：对任何两人 $x, y$，一个比另一个年轻或同龄，不可能互相都比对方年轻。（本质上，我们通过确保反对称性定义中的前提永远不成立来保证条件语句恒为真。）
>
> 因此该关系满足所有要求的性质。以上论证未完全严格（未给出具体反例），因为我们不知道你班上有谁。一般而言，形如 $(x, y) \\in R \\Leftrightarrow x$ "小于" $y$ 的关系（无论"小于"在具体语境中如何定义）都是不自反、不对称、传递且反对称的。"大于"关系也同样如此——可以验证 $\mathbb{N}$、$\mathbb{Z}$、$\mathbb{R}$ 上的 $<$ 关系和 $>$ 关系，或"年龄小于""个子较高""孩子更多"等关系。那么 \leq 关系呢？它与 $<$ 有何不同？哪些性质会改变？这些问题将在下一小节通过**序关系**（Order Relation）来探讨——\leq 和 $\geq$ 类型的关系就是典型的序关系。


Let us define $R$ on $S$ by $x \\, R \\, y \\Leftrightarrow x$ is strictly younger than $y$ (in years) Now, let's explore its properties and make sure they are what we wanted them to be. Try to prove/disprove them on your own before reading our solutions! Also, play around with a different relation on S (make one up!) and see how its properties are different. Can you come up with another relation that has the exact same properties as this one? • $R$ is not reflexive. This is because any person x \in S has the exact same age as him/herself, and so x ̸R x. • $R$ is not symmetric. This is because if x is strictly younger than y, then y is strictly older than x, so y ̸R x • $R$ is transitive. This is because if x is (strictly) younger than y and y is (strictly) younger than z, then certainly x is (strictly) younger than z. • $R$ is anti-symmetric. This is because for any two people x, y \in S, one of them must be younger than the other, or else they are the same age; they cannot both be strictly younger than each other. (Essentially, we are ensuring anti-symmetry holds by making sure the hypothesis of the conditional statement in that property's definition never holds, so the conditional itself is always True.) Thus, this relation R satisfies all of the desired properties. You'll notice that we were not completely rigorous in these arguments, but there's a good reason for it. Specifically, we didn't produce explicit counterexamples for the properties that fail. It would be best if we could identify two students in your class and show how one is younger than the other but not the other way around. But we don't know who's in your class! That's why we left our arguments as "explaining the existence of something without pointing to it explicitly". We will point out that, in general, a relation of this form---one defined as $(x, y) \\in R \\Leftrightarrow x$ is "less" than $y$ (however "less" makes sense in that context)--- will be non-reflexive, non-symmetric, transitive, and anti-symmetric. In fact, we can even replace "less" with "greater" and this still holds. To see why this is true, think about the "<" relation on $\mathbb{N}$, or $\mathbb{Z}$, or $\mathbb{R}$. Think about the ">" relation on those sets. Think about the "is younger than" relation on the set of people, or the "is taller than" relation, or the "has more children than" relation. What about the "$\\leq$" relation on $\\mathbb{Z}$? How is this different than the "<" relation? What properties change? (These types of questions will be explored a little bit further in the next subsection, where we examine a particular type of relation that behaves like these "$\\leq$" and "$\\geq$" relations. They are called order relations, naturally.)


6.2. ABSTRACT (BINARY) RELATIONS


> 🇨🇳 ### 6.2.5 问题与练习
>
> **温故知新** 简要回答以下问题（口头或书面均可）。若回忆不起某定义、概念或例子，请回看相关部分。
>
> (1) 用集合的语言如何定义（二元）关系？
> (2) 若关系 R 定义在 A 与 B 之间，要能讨论 R 是否自反等性质，A 和 B 必须满足什么条件？
> (3) 何时关系是自反的？给出一个自反关系的例子。
> (4) 何时关系是对称的？给出一个对称关系的例子。
> (5) 何时关系是传递的？给出一个传递关系的例子。
> (6) 何时关系是反对称的？给出一个反对称关系的例子。
> (7) "不对称"与"反对称"有什么区别？给出一个同时满足对称和反对称的关系。
>
> **动手试试** 回答以下简答题，要求你实际写下来或口头描述（可以向朋友/同学口述）。目的是让你练习使用新概念、定义和记号。


### 6.2.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) How is (binary) relation defined, in terms of sets? (2) Say we have a relation R defined between A and B. What must true about A and B for us to be able to talk about whether $R$ is reflexive, say? (3) When is a relation reflexive? Give an example of a set and a reflexive relation on that set. (4) When is a relation symmetric? Give an example of a set and a symmetric relation on that set. (5) When is a relation transitive? Give an example of a set and a transitive relation on that set. (6) When is a relation anti-symmetric? Give an example of a set and an anti-symmetric relation on that set. (7) What is the difference between not symmetric and anti-symmetric? Give an example of a set and a relation on that set which is both symmetric and anti-symmetric. Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Consider the set $A = \\{1, 2, 3\\}$. For each of the following relations, defined on A or P(A) as specified, decide whether it is (i) reflexive, (ii) symmetric, (iii) transitive, (iv) anti-symmetric. Not much justification is required, just a Yes or No and a sentence or two. (a) Ra on A defined by Ra = { (1, 1), (1, 2), (2, 1), (2, 2), (3, 3) } (b) Rb on A defined by Rb = { (1, 1), (1, 2), (2, 2), (2, 3), (3, 3) } (c) Rc on P(A) defined by $\\forall S, T \\in P(A).\\, (S, T) \\in R_c \\Leftrightarrow S \\cap T = \\emptyset$ (d) Rd on P(A) defined by $\\forall S, T \\in P(A).\\, (S, T) \\in R_d \\Leftrightarrow S \\cap T \\neq \\emptyset$


> 🇨🇳 (1) 设 $A = \\{1, 2, 3\\}$。对以下每个关系，判断其是否 (i) 自反、(ii) 对称、(iii) 传递、(iv) 反对称，简要说明。
> (a) $R_a = \{(1,1), (1,2), (2,1), (2,2), (3,3)\}$
> (b) $R_b = \{(1,1), (1,2), (2,2), (2,3), (3,3)\}$
> (c) $R_c$ 在 $\mathcal{P}(A)$ 上定义：$\forall S, T \in \mathcal{P}(A)$，$(S, T) \in \mathbb{R}_c \Leftrightarrow S \cap T = \emptyset$
> (d) $R_d$ 在 $\mathcal{P}(A)$ 上定义：$\forall S, T \in \mathcal{P}(A)$，$(S, T) \in \mathbb{R}_d \Leftrightarrow S \cap T \neq \emptyset$
>
> (2) 在 $\mathbb{Z}$ 上定义关系 $\star$：$\forall x, y \in \mathbb{Z}$，$x \star y \Leftrightarrow 3 | (x - y)$。
> (a) 证明 $\star$ 是自反的。(b) 证明 \star 是对称的。(c) 证明 $\star$ 是传递的。（注意 "|" 表示"整除"，请使用定义 6.2.15 中的形式定义。）
>
> (3) 在 $\mathbb{Z}$ 上定义关系 $\sim$：$\forall x, y \in \mathbb{Z}$，$x \sim y \Leftrightarrow 3 | (x + 2y)$。
> (a) 证明 $\sim$ 是自反的。(b) 证明 \sim 是对称的。(c) 证明 $\sim$ 是传递的。
>
> (4) 在 $\mathbb{R}$ 上定义关系 T：$(x, y) \in T \Leftrightarrow \frac{y}{x} \in \mathbb{R} \wedge \frac{y}{x} \geq 0$。判断 T 的各性质并证明。


(e) Re on P(A) defined by $\\forall S, T \\in P(A).\\, (S, T) \\in R_e \\Leftrightarrow S \\subseteq T$ (2) Define the relation \staron Z by saying $\forall x, y \in \mathbb{Z}. x \stary \Leftrightarrow$3 | x -y (a) Prove that \staris reflexive. (b) Prove that \staris symmetric. (c) Prove that \staris transitive. (Remember that "|" means "divides". Be sure to use the formal definition; see Definition 6.2.15.) (3) Define the relation ∼on $\mathbb{Z}$ by saying \forall x, y $\in \mathbb{Z}$. x ∼$y \Leftrightarrow$3 | x + 2y (a) Prove that ∼is reflexive. (b) Prove that ∼is symmetric. (c) Prove that ∼is transitive. (4) Define the relation T on $\mathbb{R}$ by saying, for any x, y $\in \mathbb{R}, (x, y) \in T \Leftrightarrow$ { y x $\in \mathbb{R} \wedgey x \geq$0 } (a) Find $x \\in R$ such that (x, x) \notin T. Does this mean T is not reflexive? Why or why not? (b) Find x, $y \\in R$ such that (x, y) \in T and (y, x) \in T. Does this mean T is symmetric? Why or why not? (c) Find x, $y \\in R$ such that (x, y) \in T but (y, x) \notin T. Does this mean T is not symmetric? Why or why not? (d) Determine whether or not T is transitive, and prove your claim. (5) Define the relation $\leftrightarrow$on P($\mathbb{N}$) by saying, for any X, Y $\subseteq \mathbb{N}, X \leftrightarrow Y \Leftrightarrow$ { X $\subseteq Y \vee X \cap Y$ = $\emptyset$ } Prove/disprove each of the four standard properties for this relation (i.e. reflexive, symmetric, transitive, anti-symmetric). (6) What is wrong with the following "proof" that the symmetric and transitive properties imply the reflexive property? Let A be a non-empty set. Let R be a relation on A. Suppose $R$ is symmetric and transitive. We will show $R$ is reflexive.


> 🇨🇳 (5) 在 $\mathcal{P}(\mathbb{N})$ 上定义关系 $\leftrightarrow$：$X \leftrightarrow Y \Leftrightarrow X \subseteq Y \vee X \cap Y = \emptyset$。对每个标准性质（自反、对称、传递、反对称）给出证明或证反。
>
> (6) 以下"证明"有什么错误？——它声称对称性和传递性蕴含自反性：
>
> 设 A 为非空集合，R 为 A 上的关系。假设 R 对称且传递，证明 R 自反。取任意 $x \in A$，定义 $T = \{y \in A \mid (x, y) \in \mathbb{R}\}$。取 $y \in T$，则 $(x, y) \\in R$。由对称性得 $(y, x) \\in R$。由传递性及 $(x, y) \\in R$、$(y, x) \\in R$，得 $(x, x) \\in R$。因 $x$ 任意，故自反性成立。
>
> **提示：** 此"证明"中哪一步存在漏洞？（关键在于 $T$ 是否非空——若不存在任何 y 使得 (x, y) \in $\mathbb{R}$，则无法选取 $y \in T$。）


Let $x \\in A$ be arbitrary and fixed. Define the set $T$ to be $\\{y \\in A \\mid (x, y) \\in R\\}$ Let $y \\in T$ be given. Thus, $(x, y) \\in R$. Since $R$ is symmetric, we can deduce $(y, x) \\in R$. Since $R$ is transitive, and $(x, y) \\in R$ and $(y, x) \\in R$, we deduce that $(x, x) \\in R$. Since x was arbitrary, we have shown that the reflexive property holds.
## 6.3 [Optional Reading] Order Relations Let us discuss some relations that behave like "$\leq$" and have similar inherent properties. This is motivated by the fact that these relations are easily definable on the standard sets of numbers we have---$\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$---and they also apply to some other, potentially surprising, situations. We will give a definition first and then consider some examples. We will then use those examples to motivate some interesting properties of order relations and then state and prove those facts.
<div class="def-definition" markdown>
**Definition 6.3.1. Let R be a relation defined on the set A.**
</div>
• If $R$ is reflexive, transitive, and anti-symmetric, then we say R is a partial order on A. • If $R$ is reflexive, transitive, and anti-symmetric and, in addition, it satisfies $\\forall x, y \\in A.\\, (x, y) \\in R \\vee (y, x) \\in R$ then we say R is a total order on A. (That is, a total order is a partial order such that every two elements of the set are comparable one way or the other.) This definition tells us what partial and total orders are. The next definition just gives us some useful shorthand for referring to partial and total orders on sets.
<div class="def-definition" markdown>
**Definition 6.3.2. When R is a partial order on A, we say that the pair (A, $\mathbb{R}$)**
</div>
is a partially ordered set, or sometimes just a poset, for short. When R is a total order on A, we say that the pair (A, $\mathbb{R}$) is a totally ordered set, or sometimes just a toset, for short. We will attempt to explain the reasons for these terms by giving several related examples.


> 🇨🇳 ## 6.3 [拓展阅读] 序关系（Order Relations）
>
> 让我们讨论一些行为类似 "$\leq$" 的关系。这类关系可以在 \mathbb{N}、\mathbb{Z}、\mathbb{Q}、$\mathbb{R}$ 上自然定义，也适用于其他一些可能令人意外的场景。
>
> **定义 6.3.1.** 设 R 为集合 A 上的关系。
> • 若 R 是自反的、传递的且反对称的，则称 R 为 A 上的**偏序**（Partial Order）。
> • 若 R 是偏序且满足 $\forall x, y \in A. (x, y) \in \mathbb{R} \vee (y, x) \\in R$（即任意两个元素都可比较），则称 R 为 A 上的**全序**（Total Order）。
>
> **定义 6.3.2.** 当 R 是 A 上的偏序时，称有序对 $(A, R)$ 为**偏序集**（Partially Ordered Set），简称 **poset**。当 R 是 A 上的全序时，称 $(A, R)$ 为**全序集**（Totally Ordered Set），简称 **toset**。后续将通过多个相关例子来解释这些术语的由来。

