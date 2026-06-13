---
title: Order Relations
---

# Order Relations

Example 6.3.3. Define the following four relations on $\mathbb{R}$: $(x, y) \in R_1 \Leftrightarrow x \leq y$; $(x, y) \in R_2 \Leftrightarrow x < y$; $(x, y) \in R_3 \Leftrightarrow x = y$; $(x, y) \in R_4 \Leftrightarrow \lfloor x \rfloor = \lfloor y \rfloor$ (Recall that $\lfloor x \rfloor = \max\{a \in \mathbb{Z} \mid a \leq x\}$ is the "floor" of a real number; it is the integer we get by rounding down.) Which of these are partial orders? Total orders? Neither? Think about this for a few minutes and try to sketch some proofs of your claims, or explain them out loud to a friend/classmate. Now, here are our thoughts. The relations $R_1$ and $R_3$ are both partial orders, but only $R_1$ is a total order. The relations $R_2$ and $R_4$ are neither partial nor total orders (because $R_2$ is not reflexive and $R_4$ is not anti-symmetric). The idea behind any type of order relation---partial or total---is that we can somehow compare the elements of the set $A$ and assign... well, an ordering to them. Heuristically speaking, a partial order induces "chains" of elements in $A$ so that, along any chain, we can arrange the elements in a line, kind of like the number line and how we usually picture $\mathbb{R}$; for a total order, there is only one "chain" and it is all of $A$. You might object to the idea that $R_2$ isn't somehow an "order-like" relation, though, and you'd have a fair point. The only fundamental difference between $R_2$ and $R_1$ is that we don't allow equality; quite literally, the phrase "or equal to" is built into the definition of "$\leq$", yet that phrase is left out of the definition of "$<$". This results in $R_2$ being non-reflexive, but that's it. You might also notice that the relation $R_4$ doesn't have this same type of relationship with $R_1$; it seems to be something different (and we'll get to that soon enough). This motivates the following few definitions, wherein a partial or total order can be "relaxed" to a related ordering.
<div class="def-definition" markdown>
**Definition 6.3.4. Let A be a set and let R be a relation on A. We say R is**
</div>
irreflexive if and only if $\\forall x \\in A.\\, (x, x) \\notin R$ Notice that this is not the same as merely being not reflexive. Think about the quantifiers: reflexivity means every element is related to itself, so the logical negation of that means there exists at least one element that is not related to itself. Irreflexivity means that every element is not related to itself.
<div class="def-definition" markdown>
**Definition 6.3.5. Let A be a set and let R be a relation on A. We say R is a**
</div>
strict partial order if it is irreflexive, transitive, and anti-symmetric. We say R is a strict total order if it is irreflexive, transitive, anti-symmetric, and satisfies the following property: $\\forall x, y \\in A.\\, x \\neq y \$\Rightarrow$ [(x, y) \\in R \\vee (y, x) \\in R]$


> 🇨🇳 例6.3.3. 在 $\mathbb{R}$ 上定义以下四个关系：$(x, y) \in R_1 \Leftrightarrow x \leq y$，$(x, y) \in R_2 \Leftrightarrow x < y$，$(x, y) \in R_3 \Leftrightarrow x = y$，$(x, y) \in R_4 \Leftrightarrow \lfloor x \rfloor = \lfloor y \rfloor$。（回忆 $\lfloor x \rfloor = \max\{a \in \mathbb{Z} \mid a \leq x\}$ 是实数的"下取整"（floor）；即通过向下取整得到的整数。）其中哪些是偏序（partial order）？全序（total order）？都不是？想几分钟，试着勾画一些证明的轮廓，或者向朋友/同学口述解释。以下是我们的想法：关系 $R_1$ 和 $R_3$ 都是偏序，但只有 $R_1$ 是全序。关系 $R_2$ 和 $R_4$ 既不是偏序也不是全序（因为 $R_2$ 不自反（reflexive），$R_4$ 不反对称（anti-symmetric））。任何类型的序关系——偏序或全序——背后的核心思想是：我们能以某种方式比较集合 $A$ 的元素并为它们赋予……嗯，一种排序。启发式地说，偏序在 $A$ 中产生元素的"链"（chain），使得沿着任何一条链，我们可以将元素排成一条线，有点像数轴和我们通常对 $\mathbb{R}$ 的想象；对于全序，只有一条"链"且它就是整个 $A$。你可能对 $R_2$ 不算某种"类序"关系的说法有异议，而你的异议是有道理的。$R_2$ 和 $R_1$ 之间唯一的本质区别是我们不允许相等；字面上说，"或等于"这个短语被包含在"$\leq$"的定义中，但在"$<$"的定义中被省略了。这导致 $R_2$ 不自反，但仅此而已。你也可能注意到关系 $R_4$ 与 $R_1$ 没有这种类似的关系；它似乎是某种不同的东西（我们很快就会讲到）。这引出了以下定义，其中偏序或全序可以被"放宽"为一种相关的排序。

**定义6.3.4.** 设 $A$ 为集合，$R$ 为 $A$ 上的关系。我们称 $R$ 是**非自反的（irreflexive）**当且仅当 $\forall x \in A. (x, x) \notin R$。注意这与仅仅"不自反"（not reflexive）不同。想一想量词的含义：自反性意味着每个元素与自身有关系，所以其逻辑否定意味着存在至少一个元素与自身没有关系。非自反性则意味着每个元素与自身都没有关系。

**定义6.3.5.** 设 $A$ 为集合，$R$ 为 $A$ 上的关系。我们称 $R$ 是**严格偏序（strict partial order）**当它是非自反的、传递的且反对称的。我们称 $R$ 是**严格全序（strict total order）**当它是非自反的、传递的、反对称的，且满足以下性质：$\forall x, y \in A. x \neq y $\Rightarrow$ [(x, y) \in R \lor (y, x) \in R]$


You might wonder what the connection is to non-strict order relations here. Well, there is a natural way to convert any order relation into a strict one, and vice-versa. We can always define one from the other by either building in, or removing, whether or not elements are related to themselves. The following lemma summarizes how to do this and, in so doing, shows that there are just as many strict orders as there are non-strict ones.
<div class="def-theorem" markdown>
**Lemma 6.3.6. Let (A, R1) be a partially ordered set. Then the relation S1 defined**
</div>
by $(x, y) \in S_1 \Leftrightarrow [(x, y) \in R_1 \wedge x \neq y]$ is a strict partial order on A. Let (A, $\mathbb{R}^2$) be a totally ordered set. Then the relation S2 defined by $(x, y) \in S_2 \Leftrightarrow [(x, y) \in R_2 \wedge x \neq y]$ is a strict total order on A. Let (A, S3) be a strictly partially ordered set. Then the relation R3 defined by $(x, y) \in R_3 \Leftrightarrow [(x, y) \in S_3 \vee x = y]$ is a (non-strict) partial order. Let (A, S4) be a strictly totally ordered set. Then the relation R4 defined by $(x, y) \in R_4 \Leftrightarrow [(x, y) \in S_4 \vee x = y]$ is a (non-strict) total order. Thinking back to the relations $R_1$ and $R_2$ defined above on $\mathbb{R}$, it might seem a little odd to define "less than" by "less than or equal to and not equal to". It's certainly wordier! However, this is just a consequence of how we describe "$\leq$" linguistically. Mathematically speaking, it is more natural to speak of reflexive relations and partial and total orders, and then alter those to become strict orders. We will see soon enough---when we talk about minimal elements---why reflexivity is a nice property, and this is a reasonable justification for why we would start with a partial order and then amend the definition to allow strict orders, as opposed to the other way around. For now, just notice that $R_2$ is the strict total order that corresponds to the total order $R_1$.
Question: is there a strict partial order that corresponds to the partial order
$R_3$? If so, what is it? If not, why? The relation $R_4$ is not any type of order relation, strict or otherwise. However, notice that $R_4$ does nicely "package" the elements of $\mathbb{R}$ together. Essentially, every real number y satisfying $1 \leq y < 2$ is "the same" under this relation. Likewise for every y satisfying $2 \leq y < 3$, and every y satisfying, say, $-5 \leq y < 4$, and so on. Once that "packaging" is accomplished, we "know" that there is an ordering we can assign to those "packages", but no information about that order is encoded in the relation $R_4$, itself. We would have to do some extra work to impose that ordering. This is why $R_4$ is not an order relation


> 🇨🇳 你可能想知道这与非严格序关系之间有什么联系。实际上，有一种自然的方式可以将任何序关系转换为严格的，反之亦然。我们总是可以通过加入或移除元素是否与自身有关系的条件来从一个定义出另一个。以下引理总结了如何做到这一点，并由此表明严格序与非严格序的数量一样多。

**引理6.3.6.** 设 $(A, R_1)$ 是偏序集。则由 $(x, y) \in S_1 \Leftrightarrow [(x, y) \in R_1 \wedge x \neq y]$ 定义的关系 $S_1$ 是 $A$ 上的严格偏序。设 $(A, R_2)$ 是全序集。则由 $(x, y) \in S_2 \Leftrightarrow [(x, y) \in R_2 \wedge x \neq y]$ 定义的关系 $S_2$ 是 $A$ 上的严格全序。设 $(A, S_3)$ 是严格偏序集。则由 $(x, y) \in R_3 \Leftrightarrow [(x, y) \in S_3 \lor x = y]$ 定义的关系 $R_3$ 是（非严格）偏序。设 $(A, S_4)$ 是严格全序集。则由 $(x, y) \in R_4 \Leftrightarrow [(x, y) \in S_4 \lor x = y]$ 定义的关系 $R_4$ 是（非严格）全序。

回想上面在 $\mathbb{R}$ 上定义的关系 $R_1$ 和 $R_2$，用"小于或等于且不等"来定义"小于"可能看起来有些奇怪。这确实更啰嗦！然而，这只是我们用语言描述"$\leq$"的方式造成的结果。从数学角度讲，先讨论自反关系以及偏序和全序更为自然，然后再修改这些定义来得到严格序。我们很快就会谈到——在讨论极小元时——为什么自反性是一个好性质，这也是我们以偏序为起点再修正定义来允许严格序的合理理由，而不是反过来。现在只需注意到 $R_2$ 就是对应于全序 $R_1$ 的严格全序。

问题：是否存在对应于偏序 $R_3$ 的严格偏序？如果有，它是什么？如果没有，为什么？

关系 $R_4$ 不是任何类型的序关系——严格的或其他的。不过，注意到 $R_4$ 确实巧妙地将 $\mathbb{R}$ 的元素"打包"了。本质上，每个满足 $1 \leq y < 2$ 的实数 $y$ 在这个关系下都是"相同的"（same）。同样适用于每个满足 $2 \leq y < 3$ 的 $y$，以及每个满足比如 $-5 \leq y < -4$ 的 $y$，以此类推。一旦完成了这种"打包"，我们就"知道"可以为这些"包"赋予一个排序，但关于该排序的信息并没有编码在关系 $R_4$ 本身之中。我们必须做额外的工作来施加那个排序。这就是为什么 $R_4$ 按其定义方式不是任何类型的序关系


of any kind, the way it is defined. However, it is what we call an "equivalence relation" because of this nice "packaging" property that partitions the elements of the set into separate classes. This is a notion we will explore in the next section. Once we have established those "packages", we can compare them and order them. Let's explore some examples in a context other than $\mathbb{R}$. One of these following relations is actually a standard example of a partial order.
Example 6.3.7. Let S = [3] and consider the power set, P(S). (Remember that
the power set of S is the set of all subsets of S.) Define the following relations on P(S), where $X, Y \subseteq S$: $(X, Y) \in R_1 \Leftrightarrow X \subseteq Y$; $(X, Y) \in R_2 \Leftrightarrow X \subset Y$; $(X, Y) \in R_3 \Leftrightarrow X \cap Y = \emptyset$; $(X, Y) \in R_4 \Leftrightarrow X \triangle Y = S$ Recall that X∆Y is the symmetric difference of X and Y, and is defined as X∆Y = (X -Y ) \cup(Y -X) = (X \cup Y ) -(X \cap Y ). We claim that R1 is a partial order but not a total order. Before we go on to prove this claim, consider this challenge problem: Can you define a total order on P(S)? Can you do it in a way that would generalize to the case where S = [n], for some arbitrary $n \in \mathbb{N}$. Now, to prove that R1 is a partial order, we must show that it is reflexive, transitive, and anti-symmetric. To also show it is not a total order, we must show that it fails the additional property that says any two elements are somehow comparable. We will accomplish some of these steps, and leave the rest as exercises. • Let's prove R1 is anti-symmetric: Let X, Y \in P(S) and assume (X, Y ) \in R1 and (Y, X) $\\in R$1. This means X \subseteq Y and Y \subseteq X, and therefore X = Y, by standard properties of sets. • Let's show R1 is not a total order. Consider X = {1} \subseteq S and Y = {2, 3} \subseteq S. Notice that X ⊈Y and Y ⊈X, so (X, Y ) $\\notin R$1 and (Y, X) \notin R1. That is, X and Y are incomparable under this relation. This relation separates the entire set P(S) into chains that are ordered within themselves, but separate chains may contain elements that are incomparable. For instance, consider the following subsets of P(S): A1 = $\emptyset$, {1}, {1, 2}, $\\{1, 2, 3\\}$


> 🇨🇳 $A_1 = \{\emptyset, \{1\}, \{1, 2\}, \{1, 2, 3\}$\}（从 $\emptyset$ 到全集的包含链）


A2 = $\emptyset$, {1}, {1, 3}, $\\{1, 2, 3\\}$


> 🇨🇳 $A_2 = \{\emptyset, \{1\}, \{1, 3\}, \{1, 2, 3\}$\}（另一条包含链）


A3 = $\emptyset$, {2}, {1, 2}, $\\{1, 2, 3\\}$


> 🇨🇳 $A_3 = \{\emptyset, \{2\}, \{1, 2\}, \{1, 2, 3\}$\}（又一条包含链）


A4 = {3}, {2, 3}


> 🇨🇳 $A_4 = \{\{3\}, \{2, 3\}$\}（一条较短的包含链）


These sets are not disjoint, so they do not form a partition of P(S). Notice, though, that R1 does induce a total order within each subset. By "induce" we mean that we use the same defining property of R1 but restrict our domain to the set A1, for instance, instead of all of P(S). Of course, there are even more sets we could define that are chains under this relation. Let's formalize this notion and then continue our example
<div class="def-definition" markdown>
**Definition 6.3.8. Let (A, $\mathbb{R}$) be a partially ordered set, and let B $\subseteq A$. Let ˆR**
</div>
denote the relation induced by R on B; that is, we set $\\forall x, y \\in A.\\, (x, y) \\in \\hat{R} \\Leftrightarrow [x, y \\in B \\wedge (x, y) \\in R]$ If (B, ˆR) is a totally ordered set, then we say B is a chain of A (under $\mathbb{R}$). With this definition in hand, we see that A1, A2, A3, A4 are chains of P(S) under R1. Now, try proving that $\mathbb{R}^2$ is a (strict) partial order, and then try writing some chains of P(S) under the relation $\mathbb{R}^2$. How do they compare to chains of P(S) under R1? In the next subsection, we will see why chains are important; specifically, we will look at special properties of partial orders, chains, and total orders, that allow us to find "smallest" and "greatest" elements of subsets. Before we move on, though, let's see two more related examples of partial orders.
Example 6.3.9. Consider the set $\mathbb{R} \times \mathbb{R}$. We define a relation $R$ on $\mathbb{R} \times \mathbb{R}$ by establishing when a pair of real numbers is related to another pair of real numbers. Specifically, let's say $\{(u, v), (x, y)\} \in R \Leftrightarrow [u \leq x \wedge v \leq y]$ One can prove that $R$ is a partial order on $\mathbb{R} \times \mathbb{R}$. We will prove the transitivity property and leave the rest as exercises:
<div class="def-proof" markdown>
*Proof.* Let (u, v), (x, y), (z, w) $\in \mathbb{R} \times \mathbb{R}. Suppose that ((u, v), (x, y)) \\in R$ and
</div>
that ((x, y), (z, w)) $\in \mathbb{R}. This means u \leq x and x \leq z, so u \leq z$; also, this means v $\leq y and y \leq w, so v \leq w$. Thus, ((u, v), (z, w)) $\\in R$. This shows R is transitive. Hint: to prove R is not a total order, we must find a counterexample. That is, we need a pair (x, y), (u, v) such that neither $((x, y), (u, v)) \\in R$ nor $((u, v), (x, y)) \\in R$. Think about the relation R visually, i.e. geometrically, to come up with such an example. Think about what the chains are under this relation. Try to describe them geometrically and draw a few representatives.
Example 6.3.10. Let A be the standard English alphabet of 26 letters, and let
W be the set of all finite strings of letters from A. That is, W is the set of all possible "words", where we allow any combination of letters to be included in our "dictionary". Let's try to define L, the standard lexicographic ordering on


> 🇨🇳 例6.3.10. 设 $A$ 是标准的26个英文字母组成的集合，W 是由 A 中字母组成的所有有限字符串的集合。即 W 是所有可能的"单词"的集合，其中我们允许任何字母组合被包含在我们的"词典"中。让我们尝试定义 W 上的标准词典序（lexicographic ordering）L。将 A 表示为集合 [26] 会有所帮助，其中 $a = 1, b = 2, \ldots, z = 26$。于是，一个单词 w \in W 可表示为 $w = (w_1, w_2, \ldots, w_n)$，其中 $n \in \mathbb{N}$ 且 $orall i \in [n]. w_i \in A$。注意到对于任意两个单词 $v, w \\in W$，我们可以从左到右逐字母比较它们，直到找到差异之处。在差异出现的位置，根据那两个字母的比较来排序两个单词。如果其中一个比另一个长且其余字母相同，我们希望将较长的排在较短的后面，就像词典中"there"排在"therefore"之前。$(v, w) \in L \Leftrightarrow$ 在使得 $v_i 
eq w_i$ 的最小下标 i 处，有 $v_i < w_i$（其中空格位置被视为27）。想想为什么这对应于词典中单词的通常排序。（你能否用更严谨的数学记号来定义它？试试看！）


W. It helps to represent A as the set [26], where a = 1 and b = 2 and so on, until z = 26. Then, we say a word $w \\in W$ is represented by $w = (w_1, w_2, \\ldots, w_n)$ where n $\in \mathbb{N} and \forall i \in[n]. wi \in A$ Notice that for any two words $v, w \\in W$, we can compare them "letter by letter" reading left to right until we reach a difference between them. Wherever that difference occurs, we sort the two words according to the comparison of those two letters. If one word is longer than the other and they have the same letters otherwise, we want to sort the longer one after the shorter one, just like "there" comes before "therefore" in the dictionary. (v, w) $\in L \Leftrightarrow a$t the smallest index i where vi $\neq$ wi, we have vi < wi (and where a blank space is treated as 27) Think about why this corresponds to the usual ordering of words in the dictionary. (Could you define this using more rigorous mathematical notation? Try it!) Now that we've looked at several examples of order relations, we recommend you try several of the exercises to practice identifying these relations and proving their properties. After that, we can move on to talk about many other interesting and useful properties of order relations!
### 6.3.1 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What is the difference between a partial order and a total order? (2) Give an example of a partial order that is not total. Give an example of a total order. Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Let S = [2], and define R on P(S) by $(x, y) \\in R \\Leftrightarrow x$ has at least as many elements as $y$. Prove that S is not a partial order.


> 🇨🇳 (1) 设 $S = [2]$，在 $\mathcal{P}(S)$ 上定义 $R$：$(x, y) \in \mathbb{R} \Leftrightarrow x$ 至少有和 $y$ 一样多的元素。证明 $S$ 不是偏序。


(2) Let S = [3], T = [2], and define $R \\subseteq S \\times T$ by $(x, y) \\in R \\Leftrightarrow x \\supseteq y$. Prove/disprove each of the four standard properties of relations for R (i.e. reflexive, symmetric, transitive, anti-symmetric.) Use your results to determine whether R is any kind of order relation(s).
## 6.4 Equivalence Relations
### 6.4.1 Definition and Examples
Let's shift gears only slightly and talk about another type of relation that satisfies a different subset of the four standard properties of relations. In fact, let's return to a particular relation we mentioned in a previous example: on the set $\mathbb{R}$, define R to be the relation where (x, y) $\in \mathbb{R} \Leftrightarrow$⌊x⌋= ⌊y⌋ (In case you missed it in the Optional Reading, this is seen in Example 6.3.3.) Notice that this relation is • reflexive because \forall $x \\in R$. ⌊x⌋= ⌊x⌋ • symmetric because \forall x, $y \\in R$. ⌊x⌋= ⌊y⌋=$\Rightarrow$⌊y⌋= ⌊x⌋ • transitive because \forall x, y, z $\\in R$. {⌊x⌋= ⌊y⌋\wedge⌊y⌋= ⌊z⌋ } =$\Rightarrow$⌊x⌋= ⌊z⌋ This particular set of properties has some interesting and useful consequences, so we assign a name to any relation that has these three properties.
<div class="def-definition" markdown>
**Definition 6.4.1. Let A be a set and R a relation on A. If R is reflexive,**
</div>
symmetric, and transitive, then we say R is an equivalence relation. That's it! Given any relation R on a set S, all we have to do is go through and prove/disprove these three properties to determine whether R is, in fact, an equivalence relation. Let's run through some of the examples of relations that we have seen already and determine whether they are equivalence relations or not, based on what we've proven about them.
Example 6.4.2. (1) Look back at the equality relation on an arbitrary set X
that we defined in Example 6.2.9. This is an equivalence relation. Certainly, (x, x) $\\in R$, since x = x. However, the hypothesis x R y is false for any x $\neq$ y, which makes the conditional statement true. Thus, the only "relevant case" in the symmetric property is the one where x = y, in which case, yes, y = x, too. Similarly, for the transitive property, if either x $\neq$ y or y $\neq$ z, the hypothesis of the defining conditional statement is false, so the statement itself is true; and when x = y and y = z, yes, certainly x = z. This may not seem like a particularly enlightening development, but it is nice to know that there is always at least one equivalence relation we can define on any set.


> 🇨🇳 例6.4.2. (1) 回顾在任意集合 $X$ 上定义的相等关系（例6.2.9）。这是一个等价关系。显然，(x, x) \in R，因为 x = x。然而，对于任何 $x 
eq y$，假设 x \, \mathbb{R} \, y 是假的，这使得条件语句为真。因此，对称性中唯一"相关的情况"是 x = y 的情况，此时确实也有 y = x。类似地，对于传递性，如果 $x 
eq y$ 或 $y 
eq z$，定义条件语句的假设为假，从而语句本身为真；而当 x = y 且 y = z 时，当然有 $x = z$。这可能看起来不是一个特别有启发性的结论，但很高兴知道我们总能在任何集合上定义至少一个等价关系。


