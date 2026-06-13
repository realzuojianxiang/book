---
title: Definition and Examples
---

# Definition and Examples

We write $f : A \to B$ to mean $f$ is a function from $A$ to $B$. If $(a, b) \in f$, then we write $f(a) = b$ knowing that $b$ is the unique element that satisfies that property for the given $a$. That's it! It might be strange now to think about a function as a relation, which is actually a particular type of set, but that's what it is. Formulating functions in these terms allows us to talk about them in the language of sets and relations, but notice that we will still be able to use some familiar notation. Knowing that for every "input" $a$ (i.e. every element of the domain), there is a unique "output" $b$ (i.e. an element of the codomain), we can write $f(a) = b$ and know that the "=" is, actually, an equality. There is no other element of $B$ that could satisfy this relationship, because that $b$ is unique. Part of this definition incorporates the idea we mentioned above: we want to know what type of object a function will "output". This is what specifying the codomain accomplishes. For example, it wouldn't make sense to define the function $f : $\mathbb{R}$ \to \mathbb{R}$ by $f(x) = \sqrt{x}$; there are some elements (namely, negative numbers) of the domain where the "output" would be undefined. (Technically, the output would be a complex number, which is not an element of the codomain $\mathbb{R}$; in the context of $\mathbb{R}$, though, we would think of a complex number as being "undefined".) When a function is defined properly, and the domain and codomain are specified, and the related pairs do belong to the Cartesian product of the sets, we say the function is well-defined. Sometimes, we will present you with a relation on two sets and ask you to decide whether or not it is a well-defined function. In that case, we are really just asking whether the relation corresponds to a proper function. The word "Range" The word codomain might be new to you. In fact, you might be more accustomed to using the word range to refer to the set of potential "outputs" of a function. We want to completely avoid using the word "range" in this context because of a potential ambiguity. Some authors and teachers use the word "range" to mean what we mean here by "codomain": the set of potential "outputs" of a function. However, some authors and teachers use the word to mean what we mean here by "image". As you will see when we define this term properly in Section 7.3, this is the set of actually-achieved "outputs" of the function. In general, the image is a subset of the codomain, but it might be a proper subset. When someone uses the word "range", they might be thinking of one of these interpretations, but you might be thinking of the other one! To avoid this confusion, we will only use the words codomain and image.


> 🇨🇳 我们写 $f: A \to B$ 表示 $f$ 是从 $A$ 到 $B$ 的函数。如果 $(a, b) \in f$，我们就写 $f(a) = b$，知道 $b$ 是满足该性质的唯一元素。把函数看作一种关系（实际上是特定类型的集合）现在可能觉得很奇怪，但事实就是如此。用这些术语来表述函数，使我们能够用集合和关系的语言来讨论它们。

> **"Range"这个词** "陪域（codomain）"这个词对你来说可能很新。你可能更习惯于用"值域（range）"来指代函数可能输出的集合。我们希望完全避免在这里使用"range"一词，因为它有歧义——有些作者用它指陪域，有些作者用它指像（image）。为避免混淆，我们只使用"陪域"和"像"这两个词。


### 7.2.2 Examples
Let's see some examples (and non-examples) of functions, using our new definition. While working with these examples, we will describe proper notation for defining functions and working with them, and we will describe how to "visualize" some functions and appeal to our intuitions. Notation There are several ways of properly defining a function. The following are all acceptable ways of defining "the squaring function on the real numbers": Let $f \subseteq $\mathbb{R} \times \mathbb{R}$ be the function defined by $(x, y) \in f \Leftrightarrow y = x^2$. Let $f : $\mathbb{R}$ \to \mathbb{R}$ be the function defined by $f =$

$\{(x, x^2) \mid x \in \mathbb{R}$\}$


> 🇨🇳 **7.2.2 例子** 定义"平方函数"的几种方式：设 $f \subseteq $\mathbb{R} \times \mathbb{R}$ 为由 $(x, y) \in f \Leftrightarrow y = x^2$ 定义的函数；设 $f: $\mathbb{R}$ \to \mathbb{R}$ 为由 $f = \{(x, x^2) \mid x \in \mathbb{R}$\}$ 定义的函数；设 $f: $\mathbb{R}$ \to \mathbb{R}$ 为由 $\forall x \in \mathbb{R}$, f(x) = x^2$ 定义的函数。我们通常使用第三种记号风格，因为它更容易理解。定义函数时需要指定：定义域、陪域、函数名和规则或集合。

> 例 7.2.2：将自然数转换为二进制表示的函数 $B: $\mathbb{N}$ \to S$（$S$ 为有限二进制串集合）。


. Let $f : $\mathbb{R}$ \to \mathbb{R}$ be the function defined by $\forall x \in \mathbb{R}$.\ f(x) = x^2$. Think about how each of these appeals to the definition of a function we saw above. The first appeals directly to the idea that a function is a type of set, namely a relation from $\mathbb{R}$ to $\mathbb{R}$. The second uses the same idea but expresses $f$ via set-builder notation instead of an if and only if statement. The third appeals to the idea that every "input" of $f$ has a unique "output", so we can simply declare what that "output" is for all $x \in \mathbb{R}$. We will usually stick to the third notation style because it easier to understand, and appeals more directly to our intuitions about functions. Sometimes, we will use the other notation styles; we might be trying to emphasize the underlying structure of a function, or it might just be easier to write, depending on the context. In general, though, when defining a function, we need to specify all the important components for the reader: the domain, the codomain, the letter name, and either a rule or a set that assigns the ordered pairs. If you're wondering why it's so important to specify the codomain when defining a function, think of it in terms of writing computer code. If you define a function, you usually have to declare the object type of the output variable. (This depends on the language, of course.) For instance, in Java, you might write public int PlusOne (int x) { return x+1; } This defines a function that inputs an integer, adds one, and outputs another integer. Notice that you had to tell the program what type of object was going in and what type would be coming out.
Example 7.2.2. Consider the function that takes a natural number and outputs
its binary representation. Let's use B to represent this function. Doing some calculating, we see that we want B(1) = 1 and B(2) = 10 and B(10) = 1010, for instance. What is the domain of this function? What is the codomain? Can


> 🇨🇳 例 7.2.3：平方函数 $f: $\mathbb{R}$ \to \mathbb{R}$、$g: $\mathbb{R}$ \to \mathbb{C}$、$h: $\mathbb{Z}$ \to \mathbb{R}$。$f = g$ 因为它们有相同的有序对；$f \neq h$ 因为 $h$ 的定义域更小（$\mathbb{Z} \subset \mathbb{R}$），$f(1/2) = 1/4$ 但 $h(1/2)$ 无定义。


you write down the "rule" that defines it rigorously? Doesn't it seem better to just leave it the way we stated it, in words? We would define this function in the following way. Let S be the set of all finite binary strings, i.e. sequences of 0s and 1s. Let $B : $\mathbb{N}$ \to S$ be the function defined by $B = \{(n, s) \mid n \in \mathbb{N}$ \text{ and } s \text{ is the binary representation of } n\}$
Example 7.2.3. Consider the "squaring function" again: Let $f : $\mathbb{R}$ \to \mathbb{R}$ be
defined by $\forall x \in \mathbb{R}$.\ f(x) = x^2$. Is this function any different from the following functions? • Let $g : $\mathbb{R}$ \to \mathbb{C}$ be the function defined by $\forall x \in \mathbb{R}$.\ g(x) = x^2$ • Let $h : $\mathbb{Z}$ \to \mathbb{R}$ be the function defined by $\forall x \in \mathbb{Z}$.\ h(x) = x^2$ The function $g$ has a different codomain but, in fact, $\mathbb{R} \subseteq \mathbb{C}$. All of the ordered pairs $(x, x^2) \in g$ still satisfy $x \in \mathbb{R}$ and $x^2 \in \mathbb{R}$. In this sense, $f$ and $g$ are the same function, and we would write $f = g$. We will see later on precisely what it means for two functions to be equal. For now, it suffices to say that the underlying relations corresponding to $f$ and $g$ have the same ordered pairs of real numbers as elements. The function $g$ theoretically allows for complex numbers in the second coordinate, but the way the domain and the "rule" are established, this doesn't actually happen. The function $h$ has a different domain, and $\mathbb{Z} \subset \mathbb{R}$ (a proper subset). Thus, there are many ordered pairs in the relation corresponding to the function $f$ that don't belong to the relation corresponding to the function $h$. For instance, $(1/2, 1/4) \in f$ but $(1/2, 1/4) \notin h$. Said another way, $f(1/2) = 1/4$, but the concept of $h(1/2)$ is not well-defined; $1/2$ does not belong to the domain of $h$.
Example 7.2.4. We can define a function piece-wise, as well. For instance,
consider the absolute value function, defined on $\mathbb{R}$: Let $a : $\mathbb{R}$ \to \mathbb{R}$ be the function defined by $\forall x \in \mathbb{R}$.\ a(x) = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}$ Every domain element falls into exactly one of the cases, so there is no ambiguity. "Well-defined" Functions It is not always clear that a defined relation is actually a function. Given a proposed domain, codomain, and a "rule" or set, how can we check that these represent a function? This is what the next definition (based entirely on the definition of function we saw above) addresses:


> 🇨🇳 **"良定义的"函数** 要检查一个定义的关系是否是函数：(1) 规则在定义域的所有元素上都有定义，(2) 对每个 $a \in A$，规则输出陪域 $B$ 中唯一的元素。两种情况可能出错：没有输出、多个输出、或输出不在陪域中。


<div class="def-definition" markdown>
**Definition 7.2.5. Given a domain $A$, a codomain $B$, and a proposed "rule"**
</div>
for $f$, then we say $f$ is a well-defined function if and only if (1) the rule is defined on all elements of $A$, and (2) for every $a \in A$, the rule outputs a unique element of the set $B$. Let's use this in an example here. Later in this section, we will see some non-examples of functions, and we will again appeal to this definition of welldefined.
Example 7.2.6. Let $f : $\mathbb{Z}$ \to \mathbb{N}$ be the function defined by
$\forall z \in \mathbb{Z}$.\ f(z) = |2z + 1|$ Wait, how can we be so sure that $|2z + 1|$ will be a natural number, for any integer $z$? It's not immediately obvious, but we can figure it out. Suppose $z \in \mathbb{Z}$ satisfies $z \geq 1$. Then certainly $2z+1 \in \mathbb{Z}$ and $|2z+1| = 2z+1 \geq 3$. Thus, $f(z) \in \mathbb{N}$. Suppose $z \in \mathbb{Z}$ satisfies $z \leq -1$. Then $2z + 1 \in \mathbb{Z}$ and $2z + 1 \leq -1$. Thus, $f(z) = |2z + 1| \geq 1$, so $f(z) \in \mathbb{N}$. Suppose $z = 0$. Then $f(z) = |2 \cdot 0 + 1| = 1$, so $f(z) \in \mathbb{N}$. In any case, we see that the "rule" that defines $f$ does indeed yield a natural number, an element of the codomain. Furthermore, it yields exactly one such number. Therefore, this is a well-defined function.
Example 7.2.7. Let P be the set of all people in the world. Let b : P $\to \mathbb{N} \cup \{0\}$
be the function defined by b = {(p, n) | p $\in P \wedgeperson p has n sisters} (Notice that we have used one of the sets-emphasizing notation styles here, for practice. Also, it might look funny to combine math symbols and words, as in$ "b(p) = the number of sisters person p has".) Is this a well-defined function? We would say so. Walk up to someone (i.e. an element p \in P) and ask them how many sisters they have (i.e. what b(p) is). They will tell you a non-negative integer in return. Also, they wouldn't possibly tell you two different numbers. Now, you could point out that in today's society of divorces and remarriages, plenty of people have half-sisters, and 1 2 $\notin \mathbb{N} \cup \{0\}$. Fine. Fair point. But with the "simplifying assumption" that everyone has some whole number of sisters, this function is well-defined. The Identity Function
Example 7.2.8. Let S be any set. Must there exist a function from S to S?
Certainly, we can think of tons of functions from $\mathbb{R}$ to $\mathbb{R}$, but what if S is just some arbitrary set? Can we guarantee there is a function from S to S? It turns


> 🇨🇳 **恒等函数** 对任意集合 $S$，恒等函数 $\text{Id}: S \to S$ 定义为 $\forall x \in S, \text{Id}(x) = x$——"输出就是输入本身"。（把函数想象成机器的话，这是最懒的机器，什么都不做，直接吐出进来的东西。）

> **非例子** 三种使"规则"不构成函数的情况：(1) 定义域中某元素无输出——如 $G: $\mathbb{N} \times \mathbb{N}$ \to \mathbb{N}$，$G(a,b) = a-b$，$G(5,10) = -5 \notin \mathbb{N}$；(2) 定义域中某元素有多个输出——如 A(W) \to W"输出异位词"，$A(\text{INTEGRAL})$ 有多个输出；(3) 输出不在陪域中。


out that... yes, we can! Think back to a similar question we considered when talking about relations. (See Example 6.2.9.) We know that we can always define the equality relation on the set S; that is, we can define R on S by (x, y) $\in \mathbb{R}$ \Leftrightarrow x$ = y. This relation consists of all ordered pairs of the form (x, x), for every x $\in S$. Does this relation represent a function? We only need to check the definitional property: does every input have exactly one output? Sure looks like it! Any element of a set is only equal to itself, and nothing else. Thus, R does represent a function. This is a special enough function that we give it its own name.
<div class="def-definition" markdown>
**Definition 7.2.9. Let S be a set. The identity function on S is defined to**
</div>
be the function Id : S $\to S given by \forall x \in S$. Id(x) = x That is, the identity function "outputs exactly what it inputs". (Thinking of a function as a machine, this is a lazy machine that does nothing, and just spits out whatever came in.) Sometimes, we wish to refer to the identity functions as defined on different sets. To avoid confusion in that case, we will write $\mathrm{Id}_S$ to mean "the identity function on the set S". Non-Examples Sometimes, in the context of solving a problem, we might write down a proposed "rule" between two sets and wonder whether it is a function. Perhaps we need it to be a function to help us work something out. How could this fail? That is, what could we be looking for to show that a proposed rule is not a function? Look back at the definition of well-defined function (see Definition 7.2.5). Three different things could go wrong: • There might be an element of the domain for which no "output" is defined. • There might be an element of the domain for which more than one "output" is defined. • There might be an element of the domain for which exactly one "output" is defined, but it is not an element of the codomain. The following examples illustrate these possibilities.
Example 7.2.10. Let G : $N \times \mathbb{N}$ \to \mathbb{N}$ be defined by
$\forall(a, b) \in \mathbb{N}$ \times \mathbb{N}$. G(a, b) = a$ -b This is not a well-defined function because there are many domain elements whose "output" is not an element of the codomain. For instance, (5, 10) $\in \mathbb{N}$\timesN and G(5, 10) =$ -5, but -5 $\notin \mathbb{N}$.


> 🇨🇳 例 7.2.10：$G: $\mathbb{N} \times \mathbb{N}$ \to \mathbb{N}$，$G(a,b) = a-b$，这不是良定义的函数，因为 $G(5,10) = -5 \notin \mathbb{N}$。

> 例 7.2.11：$A: W \to W$ 将单词变为异位字母排列词。这不是良定义的：A(\text{HI}) 不存在；$A(\text{INTEGRAL})$ 有多个输出。


Example 7.2.11. Let W be the set of words in the English language. Let A :
W $\to W$ be defined by taking in a word and outputting an anagram of that word that is not the original word. This is not well-defined for several reasons. For example, A(HI) does not exist; the same goes for A(FUNCTION). Also, notice that, for instance, A(INTEGRAL) has multiple (i.e. non-unique) outputs: TRIANGLE, ALERTING, ALTERING,...
### 7.2.3 Equality of Functions It is sometimes the case that two functions are defined by different "rules" or formulas, but they correspond to the same underlying relation! In that sense, the two functions are equal. We would like to describe what this means in terms of function notation, first, and then we will prove this idea we've come up with using the underlying relation and set notation. How might two functions be equal? Certainly their domains must be the same. If not, then one of the domain sets contains an element that doesn't belong to the other domain set, and this is a problem. (Think about it: one of the functions would be defined on an element for which the other function is undefined, so there's no way they can be equal). So, let's say we have two sets, A and B, and two functions, f : A $\to B$ and g : A $\to B$. What do we require of f and g for them to be equal? The defining characteristic of the functions is that for any input, say x $\in A$, there is a unique output f(x) and a unique output g(x). If f and g are to be the same function, we better have f(x) = g(x)! This lets us state the following theorem.
<div class="def-theorem" markdown>
**Theorem 7.2.12. Let A, B be sets, and let f : A $\to B$ and g : A $\to B$ be**
</div>
functions. Suppose that $\forall x \in A$. f(x) = g(x) Then we say f and g are equal as functions, and we write f = g. This is indeed a theorem. The idea is very intuitive, but it is not explicitly part of the definition of a function. Thus, we have to prove this idea. To complete this proof, we will consider the ordered pairs that belong to the relations f and g. By showing that these ordered pairs are the same, we can conclude f = g in the sense of sets. Notice that we are making a double-containment argument!
<div class="def-proof" markdown>
*Proof.* Let A, B be sets, and let f : A $\to B$ and g : A $\to B$ be functions.
</div>
Suppose that $\forall x \in A$. f(x) = g(x) First, we prove f $\subseteq g. Let (a, b) \in f$ be given. Since f is a function, this means f(a) = b. By the main assumption, f(a) = g(a), and so g(a) = b, as well. Thus, (a, b) \in g. This shows that (a, b) \in f =\Rightarrow(a, b) \in g and, therefore, $f \subseteq g$.


> 🇨🇳 **7.2.3 函数相等** **定理 7.2.12：** 设 $f: A \to B$ 和 $g: A \to B$ 为函数。若 $\forall x \in A, f(x) = g(x)$，则 $f = g$。证明用双向包含论证：(1) $f \subseteq g$：设 $(a,b) \in f$，则 $f(a) = b$，由假设 $g(a) = b$，故 $(a,b) \in g$；(2) $g \subseteq f$ 同理。因此 $f = g$。


Second, we prove $g \subseteq f$ in a similar manner. Let (c, d) \in g be given. Since g is a function, this means g(c) = d. By the main assumption, f(c) = g(c), and so, f(c) = d, as well. Thus, (c, d) \in f. This shows that (c, d) \in g =\Rightarrow(c, d) \in f and, therefore, g \subseteq f. Since we have shown f \subseteq g and $g \subseteq f$, we may conclude f = g. This provides us with a handy way of showing that two functions are equal without having to delve into the underlying relation/set structure. Instead, we just have to show that every element of the domain produces the same output under both functions. Let's see how this works in a couple of examples.
Example 7.2.13. Let A = {-1, 0, 1}.
Define the functions f1 : A $\to \mathbb{Z}$ and f2 : A $\to \mathbb{Z}$ by $\forall x \in A. f1(x) = x \wedgef2(x) = x3 Let's prove that f1 = f2. Since the domain only contains three elements, we can verify these outputs one by one. Notice that f1($-1) = -1 = (-1)3 = f2(-1) f1(0) = 0 = 03 = f2(0) f1(1) = 1 = 13 = f2(1) Thus, for every allowable input (i.e. \forall x $\in A$) the functions f1 and f2 have the same output (i.e. f1(x) = f2(x)). Therefore, f1 = f2.
Example 7.2.14. Let B = {1, 2, 3}.
Define the functions g1 : B $\to \mathbb{Z}$ and g2 : B $\to \mathbb{Z}$ by $\forall n \in B$. g1(n) = n3 -n2 -$6 \wedgeg2(n) = 5n2$ -11n Let's prove that g1 = g2. Again, we only have three elements to consider, so we can just verify all of the equalities by hand: g1(1) = 13 -12 -6 = 1 -1 -6 = -6 g2(1) = 5 \cdot 12 -$1^1 \cdot 1$ = 5 -11 = -6 g1(2) = 23 -22 -6 = 8 -4 -6 = -2 g2(2) = 5 \cdot 22 -$1^1 \cdot 2$ = 20 -22 = -2 g1(3) = 33 -32 -6 = 27 -9 -6 = 12 g2(3) = 5 \cdot 32 -$1^1 \cdot 3$ = 45 -33 = 12 Thus, \forall n $\in B$. g1(n) = g2(n), and so g1 = g2.


> 🇨🇳 例 7.2.14：$B = \{1,2,3\}$，$g_1(n) = n^3 - n^2 - 6$，$g_2(n) = 5n^2 - 11n$。对每个 $n \in B$ 验证输出相等，故 $g_1 = g_2$。更有趣的证法：$g_1(n) - g_2(n) = (n-1)(n-2)(n-3) = 0$（因为 $n \in \{1,2,3\}$），故 $g_1(n) = g_2(n)$。


Since the domains in these two examples were "small", we were able to examine every element one-by-one. This is not always the case, though. Sometimes, we must consider an arbitrary element of the domain (since the desired property we are proving begins with a "$\forall$" quantifier) and work with it. As it turns out, there is an interesting way of doing that with this example, so let's show you that now to get an idea of how it works. Let n \in B be given. Since g1(n), g2(n) $\in \mathbb{Z}$, we can consider their difference. Specifically, we see that g1(n) -g2(n) = (n3 -n2 -6) -(5n2 -11n) = n3 -6n2 -11n -6 = (n -1)(n -2)(n -3) (Note: the reader can verify the last equality by simply expanding the product of the three terms.) Since n \in B, we know n = 1 or n = 2 or n = 3. In each case, one of the terms---either n -1 or n -2 or n -3---must be zero. Thus, g1(n) -g2(n) = (n -1)(n -2)(n -3) = 0 Accordingly, by adding to both sides, we find g1(n) = g2(n). Since this holds for arbitrary n $\in B$, we conclude that g1 = g2. We will remark that this is certainly trickier than the "check all the cases" approach in this specific example. How did we know to look at the difference? How did we know that it would factor like that?! This is why mathematics is so interesting! We might have the ingenuity to check something like that by thinking about how to approach a more general problem, where the domain is too large to consider every case one by one. We might recognize the factorization, or think to guess at it from the fact that B = {1, 2, 3}. And if you think about it carefully enough, you might realize how we came up with this example!, Let's look at one final example of equality of functions which is a bit more complicated. It involves some ideas that we haven't assumed any familiarity with, and we won't discuss them again, but we found it interesting and illustrative enough to include it here.
Example 7.2.15. We will define two functions here and argue why they are equal.
Let the domain and codomain of each function be $\mathbb{R}^2$, the real plane. Now, let's define two functions, F1 and F2 by describing their actions geometrically (i.e. visually). We want F1 to input a point on the plane---let's call it p---and output the point achieved by rotating p counterclockwise by 90°around the origin and then reflecting through the origin. We want F2 to input p and output the point achieved by rotating p clockwise by 90°. To get a better idea of what this means, look at the following pictorial representations of F1 and F2 applied to a particular point.


> 🇨🇳 例 7.2.15：$F_1$ 将点逆时针旋转90°再关于原点反射，$F_2$ 将点顺时针旋转90°。我们论证 $F_1 = F_2$。用矩阵和方法：旋转可用旋转矩阵表示，反射只需取反坐标。计算得两者都映射 (a,b) 到 $(b,-a)$。


p Rotate 90° F1(p) Reflect through origin p Rotate 90° F2(p) We claim that F1 = F2, in the sense of functions. By playing around with several examples, we can see that this might be true; that is, we can't come up with counterexamples, and we might even begin to "see" why it's true. But none of this is a rigorous proof. It's just an intuitive way of understanding something. To rigorously prove this fact, we'll need to use some mathematical machinery outside the scope of this class. For that reason, we'll really only "sketch" this proof, and leave some of the technical details to be explored by interested readers. The main idea is this: we can represent points in the plane by vectors, the functions by matrices, and the action of a function on a point by matrix multiplication. Do not worry if you have no knowledge of matrices or vectors; you can just skip this example and you won't be missing anything essential! If you'd like to follow along, though, we'll say this: matrices are just arrays of real numbers, and vectors are matrices with just one column. The point (1, 1) in the real plane is represented by the vector [1


> 🇨🇳 （矩阵表示方法——可跳过）向量 $\begin{pmatrix} a \\ b \end{pmatrix}$，逆时针90°旋转矩阵 $= \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$。


, for instance. The action of rotation of a vector can be represented by a rotation matrix. (You might see this in an intermediate physics course, like electromagnetics or mechanics.) For example, the action of rotation counterclockwise by 90°can be represented by the matrix [0 -1


> 🇨🇳 顺时针90°旋转矩阵 $= \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$。


] Rotating the point (a, b) counterclockwise by 90°amounts to multiplying the corresponding vector by this matrix, following the usual matrix multiplication rules (where we multiply a row on the left by a column on the right, entry by entry, and add). As an example, let's rotate the point (1, 1): [0 -1


> 🇨🇳 对点 $(1,1)$ 逆时针旋转90°：$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$。


] = [0 + (-1) 1 + 0 ] = [-1


> 🇨🇳 $= \begin{pmatrix} -1 \\ 1 \end{pmatrix}$——与直觉一致。

> 反射取反：$F_1(\begin{pmatrix} a \\ b \end{pmatrix}) = -\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} b \\ -a \end{pmatrix}$，$F_2(\begin{pmatrix} a \\ b \end{pmatrix}) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} b \\ -a \end{pmatrix}$。因此 $F_1 = F_2$！


] Look at that, it matches up with what we'd expect! Check out the picture above to see this rotation in action.


> 🇨🇳 两者结果相同，验证了 $F_1 = F_2$。

> **7.2.4 示意图** 示意图用来直观表示函数，类似韦恩图表示集合。它不是严格的，但有助于构造反例和形成直觉。


Similarly, we can represent clockwise rotation by 90°by this matrix: [ 0


> 🇨🇳 顺时针旋转矩阵已处理。


] (Note the similarities in the entries, even. There's a reason for that, which we'll leave you to discover via some Googling. Or Binging, we suppose.) Reflection through the origin can also be represented by matrix multiplication, but there's an even easier way to think about it: just negate both of the coordinates. For instance, the reflection of (-1, 1) through the origin is (1, -1). This allows us to fully represent the actions of F1 and F2. Since F1 says "rotate counterclockwise by 90°and negate both entries", we can write F1 ([a b ]) = - [0 -1


> 🇨🇳 反射通过原点 = 取反两坐标。$F_1$ 和 $F_2$ 的矩阵运算都给出 $\begin{pmatrix} b \\ -a \end{pmatrix}$。


] [a b ] = [ b -a ] (where the -sign out front accomplishes the negation), and since F2 says "rotate clockwise by 90°", we can write F2 ([a b ]) = [ 0


> 🇨🇳 $F_2$ 的矩阵运算已处理。


] [a b ] = [ b -a ] By following the rules of matrix and vector multiplication, we can easily see that these two expressions are equal, for any a and b. So, assuming some knowledge about rotation matrices, this proves F1 = F2!
### 7.2.4 Schematics Before we move on to talking about some more abstract properties of functions and how to prove them, we will describe one helpful way of representing functions. We want to emphasize that this method is not rigorous in a mathematical sense, and using these representations in a proof is probably not the best idea. (On a graded homework problem, say, you might not receive full credit, despite "having the right idea".) However, this method does provide some intuitive insight into how functions work, and can guide you into discovering something and figuring out how to prove it more rigorously. In particular, this method will be quite helpful in constructing counterexamples to particular claims about function properties. The idea of a schematic diagram is similar to how we used venn diagrams to represent sets. A set is a collection of elements, not a shaded circle on a piece of paper, but these shaded circles and their overlaps can help us figure out and describe something about sets. Likewise, a function is a relation on two sets with a particular property, not something like this:


> 🇨🇳 **7.2.5 问题与练习** (1) 写出函数的定义。(2) 定义域和陪域的区别？(3) 函数良定义意味着什么？(4) 恒等函数是什么？(5) 如何证明两个函数相等？


g : A $\to B$ A B However, this does somehow represent the idea of a function. In this picture, we have represented the domain A by an oval, and the same with the codomain B. The elements of A and B are represented by dots inside those ovals (and they are labeled), and we have drawn arrows between those dots based on what the function g : A $\to B$ does. Mostly, this method is used to explore a certain property of a function and perhaps construct a counterexample to a claim. By drawing some dots and arrows and playing around with how they connect, we can perhaps develop the underlying structure of an example; then, we can go back and assign some names and formulas to the parts of the diagram and make the picture more rigorous. We will use some schematic diagrams to illustrate some properties and concepts as we proceed, but these will always be accompanied by a more rigorous statement or description. We encourage you to employ a similar method.
### 7.2.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) Write down the definition of a function, without looking it up. Then, compare to our definition. Does yours convey the same information? If not, what did you miss? (2) What is the difference between the domain and the codomain of a function? (3) What does it mean for a function to be well-defined?


> 🇨🇳 示意图方法——用椭圆表示定义域和陪域，用点表示元素，用箭头表示函数映射。这不是严格的数学方法，但有助于构造反例和直觉建立。**7.2.5 练习** 见上文翻译。


(4) What is the identity function and how is it defined? (5) How can we prove that two functions are equal? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Use proper notation to define a function that inputs an integer and outputs the square root of its absolute value. What is the domain of this function? What is its codomain? (2) Use proper notation to define a function that inputs a pair of natural numbers and outputs their average (arithmetic mean). What is the domain of this function? What is its codomain? (3) Let A = {-2, -1, 0, 1, 2}. Let g : A $\to A be defined by \forall x \in A$. g(x) = x2 -3. Draw a schematic diagram to determine whether g is well-defined or not. Is it? (4) Let X be any set. Use proper notation to define a function that inputs a subset of X and outputs that set's complement (in the context of X). What is the domain of this function? What is its codomain? (5) Let B = {-1, 0, 1}. Let h : B $\to B be defined by \forall b \in B$. h(b) = b3. What special function is this equal to? (6) Let f : $Z \times \mathbb{Z}$ \to \mathbb{N}$ be defined by \forall(x, y) \in \mathbb{Z}$ \times \mathbb{Z}$. f(x, y) = 1 2$|x + 1| $\cdot$ |y|. Is this a well-defined function? Why or why not?
## 7.3 Images and Pre-images
### 7.3.1 Image: Definition and Examples Think back to the definition of a function. We required that every input have a unique output. This ensures that a function is defined everywhere on its domain. What about the codomain, though? All we required there was that all of the outputs belong to the codomain. We never said anything about "how much" of the codomain is "covered". The idea of the image of a function is to capture exactly this notion. As we will see from some examples, it is not always easy to determine precisely what the image of a function is, even when we know what the codomain is. It is for this reason that we defined a function and its codomain first, before introducing the image; so don't think we were trying to fool you or anything!


> 🇨🇳 **7.3 像与原像** 函数的定义要求每个输入都有唯一输出，但没有说"覆盖"了陪域的多少。像（image）的概念正是用来刻画这一点——函数实际取到的输出值。注意像总是陪域的子集，但可能是真子集。
