---
title: Properties of Functions
tags:
  - 函数
  - 单射
  - 满射
  - 基数
---

# Properties of Functions

Definition
<div class="def-definition" markdown>
**Definition 7.4.1. Let A, B be sets and let $f : A \\to B$ be a function. We say f**
</div>
is a surjective function if and only if Imf(A) = B. Equivalently, we just say "f is surjective" (adjectival form), or that "f is a surjection" (nounal form). (The word "onto" is a fairly commonly used synonym for this term, so we will mention it here but won't use it again. This is just in case you've seen this word somewhere else.) Referring back to the definition of image, we can state this property equivalently in the form of a quantified statement: $f is surjective \Leftrightarrow \f\forall b \in B. \exists a \in A$. f(a) = b That is, f is surjective if and only if every output has at least one corresponding input. Think for a minute about why the second form of this definition is really the same as the first one. The property that Imf(A) = B is a statement about sets. We already know that, by definition, Imf(A) \subseteq B (nothing in the image can fall "outside" of the codomain), so this further property means that B \subseteq Imf(A), as well. This is precisely what the second form of the definition says: every element of the codomain satisfies the defining property of being an element of the image. Also, notice that nothing about the definition says the a we find to correspond to a b must be unique! All this property requires is that, for every b \in B, we can identify at least one a $\in A$ that satisfies f(a) = b. There might be more than one, there might be exactly one. It doesn't matter, as long as there aren't none. What does the property of being a surjection mean in terms of a schematic diagram? Since every element of the codomain is "hit" by the function, this means that every dot on the right-hand side of the schematic has an incoming arrow. (Remember: this type of heuristic language is fine to keep in mind--- we are using it to help describe these concepts, after all---but this does not constitute a proof. Any sentence of this sort that you use in a proof should be accompanied by a more rigorous statement, using mathematical language and/or logical symbols.) Why would we care about such a property? In general, it can be difficult to declare exactly what the image of a function is, and we might (at first) be able to only declare what the codomain is. Proving that, in fact, all of the codomain elements are outputs of the function can be additiona, helpful information! Negating the Definition Typically, we will define a function and then ask: is this a surjection or not? If we believe a function is a surjection, we should prove that by showing the


> 🇨🇳 函数的性质（Properties of Functions）本节定义并讨论函数的三个基本性质：单射、满射、双射，以及它们的判定方法。


codomain and image are the same set. If we believe it is not a surjection, we should prove that by finding a counterexample. Let's look at the logical negation of the statement that defines a surjective function: $\neg( \f\forall b \in B. \exists a \in A. f(a) = b) \Leftrightarrow \exists b \in B. \f\forall a \in A$. f(a) \neq b That is, to prove a function f is not a surjection, we must find an element of the codomain that is not an element of the image. This involves some scratch work and intuition to identify such a b. From there, we must somehow show that no possible a satisfies f(a) = b. We might argue this directly by taking an arbitrary a \in A and explaining why f(a) \neq b. Alternatively, we might argue this by contradiction: assuming that there is an a $\in A$ such that f(a) = b, we seek a contradiction. Either of these appraoches is reasonable, and they are logically equivalent.
Examples
Let's see these techniques in action with a few examples. For some of them, we might be able to use some graphical intuition or try a few test cases to figure out a guess, but ultimately we need to settle in and prove some logical statements to validate our claims.
Example 7.4.2. Consider $p : \\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{N}$ defined by $p(a, b) = ab$. Is p surjective?
Yes, it is! It looks like we can just allow a to be 1, so that the function outputs whatever b is. Let's make this observation more formal with a proof:
<div class="def-proof" markdown>
*Proof.* Let $n \in \mathbb{N}$ be arbitrary and fixed. Define (a, b) = (1, n).
</div>
Notice that (1, n) $\in \mathbb{N}$ \times \mathbb{N}$ and p(1, n) = 1 \cdot$ n = n. Since n was arbitrary, this shows p is surjective.
Example 7.4.3. Let C be the set of all cars in the United States. Let S be the
set of all strings of letters and digits that are of length at most 7 (i.e. these are the potential strings you might see on a car's license plate). Let f : C $\to S$ be defined by inputting a car and outputting its license plate string. Is the function f a surjection? No, definitely not! In case you weren't aware, curse words are disallowed on license plates! So certainly, there exist many strings of letters that you will never see on a license plate in the United States. (We'll let you provide some examples on your own... ) Because we have exhibited an element of S that is not an element of Imf(C)---or, at least, you thought of an example---we have shown that f is not a surjection.
Example 7.4.4. Let $d : \\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{Z}$ be the function defined by
$\f\forall(a, b) \in \mathbb{N}$ \times \mathbb{N}$. d(a, b) = a$ -b


> 🇨🇳 **单射（Injective / One-to-One）** 函数 $f: A \to B$ 是单射，若 $\f\forall a_1, a_2 \in A.\, a_1 \neq a_2 $\Rightarrow$ f(a_1) \neq f(a_2)$。等价条件：$\f\forall a_1, a_2 \in A.\, f(a_1) = f(a_2) $\Rightarrow$ a_1 = a_2$。直觉：不同输入永远产生不同输出。


Let's determine whether d is a surjection and prove our claim. We might start by trying some "small values" for the input variables a and b. In the table below, the left column is a and the top row is b, and the entries are d(a, b) = a -b:


> 🇨🇳 **满射（Surjective / Onto）** 函数 $f: A \to B$ 是满射，若 $\text{Im}_f(A) = B$，即 $\f\forall b \in B.\, \exists a \in A.\, f(a) = b$。直觉：陪域中每个元素都被"命中"。


It looks like all of the integers $z \in \mathbb{Z}$ will appear in this table. However, they don't all appear in one particular row or column. Rather, it looks like all the non-negative integers appear in the first column, while all the non-positive integers appear in the first row. Let's use these observations to write a proof. We'll take an arbitrary integer $z \in \mathbb{Z}$ and consider two cases; if z $\geq 0$, we will do one thing, and if z < 0, we will do something else. As long as we succeed in both cases, we will have proven that d is a surjection.
<div class="def-proof" markdown>
*Proof.* We claim d is a surjection. Let $z \in \mathbb{Z}$ be arbitrary and fixed. WWTS
</div>
$\exists(a, b) \in \mathbb{N}$ \times \mathbb{N}$. d(a, b) = z. To do this, we consider two cases$: (1) Suppose z \geq0. Then define (a, b) = (z + 1, 1). Since z \geq0, we know z + 1 \geq1 and so z + 1 $\in \mathbb{N}$. This guarantees (z + 1, 1) $\in \mathbb{N}$ \times \mathbb{N}$. Also, notice that d(z + 1, 1) = (z + 1)$ -1 = z. (2) Suppose z < 0. Then define (a, b) = (1, -z + 1). Since z < 0, we know -z > 0 and so -z +1 \geq2, meaning -z +1 $\in \mathbb{N}$. This guarantees (1, -z + 1) $\in \mathbb{N}$ \times \mathbb{N}$. Also, notice that d(1,$ -z + 1) = 1 -(-z + 1) = z. In either case, we are able to define (a, b) $\in \mathbb{N}$ \times \mathbb{N}$. d(a, b) = z. Since z \in \mathbb{Z}$ was arbitrary, this proves that d is surjective.
Example 7.4.5. Let $g : \\mathbb{R} - \\{-1\\} \\to \\mathbb{R}$ be the function defined by
$\f\forall x \in \mathbb{R}$. $g(x) = \\frac{x}{1 + x}$ (Notice why we have removed -1 from the domain. This ensures g is a welldefined function!) Let's determine whether g is a surjection and prove our claim. As mentioned before, we can do some scratch work to figure out our claim: we could try plugging in some values of x, testing "extreme cases" by letting x get very close to -1 or letting x grow larger and larger... All of this can help us plot a graph of the function, or we can just use some graphing software:


> 🇨🇳 **双射（Bijective）** 函数 $f: A \to B$ 是双射，若它同时是单射和满射。双射建立定义域与陪域之间的一一对应。直觉：每个输出恰好来自一个输入，每个输出都被命中。


Regardless, none of this proves anything! What it does do is help us observe that this function g is not surjective. There seems to be a horizontal asymptote at y = 1. That is, the function g never "reaches" 1, but rather gets infinitely close. In terms of our new definition of surjectivity, this is decidedly a NO answer! Try to prove this now. How can you show that the element -1 $\in \mathbb{R}$ is not an element of the image Img($\mathbb{R}$)? Try it! Then read on for our proof. We will actually present two proofs here, for you to compare and contrast. They both accomplish the same goal---showing g is not surjective---but one does so by a contradiction method and the other by a direct method (using cases). Which do you think is better? Did you come up with one of these? Which is easier to read? We have no definitive opinion on these questions; they are both equally valid proofs! Proof 1 (Direct). Let $x \in \mathbb{R}$-{-1} be arbitrary and fixed. WWTS that g(x) $\neq$ 1. We consider two cases: • Suppose x > -1. This means x + 1 > 0, and so


> 🇨🇳 **示例** $f: \mathbb{R} \to \mathbb{R}$, f(x) = 2x$ 是双射。$f: \mathbb{R} \to \mathbb{R}$, f(x) = x^2$ 不是单射（$f(1)=f(-1)$）也不是满射（负数没有原像）。


x+1 > 0. We also know x + 1 > x (which is true for every $x \in \mathbb{R}$.) By multiplying this inequality by the positive term


> 🇨🇳 **示例** $f: \mathbb{N} \to \mathbb{N}$, f(n) = n+1$ 是单射但非满射（1 没有原像）。$f: \mathbb{Z} \to \mathbb{N}$, f(n) = |n| + 1$ 是满射但非单射（$f(n) = f(-n)$）。


x+1, we deduce that $1 > \\frac{x}{x+1}$. Certainly, then, $g(x) = \\frac{x}{x+1}$ $\neq$ 1. • Suppose x < -1. This means x + 1 < 0, and so


> 🇨🇳 **证明单射的标准方法** 设 $f: A \to B$。要证单射：任取 $x, y \in A$，假设 $f(x) = f(y)$，推出 $x = y$。注意这是用等价条件（而非原定义）来证明。


x+1 < 0. We also know x + 1 > x. By multiplying this inequality by the negative term


> 🇨🇳 **证明满射的标准方法** 任取 $b \in B$（任意且固定的），构造 $a \in A$ 使 $f(a) = b$。关键在于如何找到 $a$——这通常需要草稿验证。


x+1 and switching the sign, we deduce that $1 < \\frac{x}{x+1}$. Certainly, then, $g(x) = \\frac{x}{x+1}$ \neq 1. In either case g(x) \neq 1. These cases cover all possibilities because $x \in \mathbb{R}$-{-1} was arbitrary (and we need not consider x = -1). This shows 1 $\\notin \\mathrm{Im}_g(\\mathbb{R} - \\{-1\\})$ so g is not a surjection.


> 🇨🇳 **证明非单射** 只需找到两个不同输入产生相同输出：定义 $x$ 和 $y$，验证 $x \neq y$ 且 $f(x) = f(y)$。


Notice that this first proof proves an interesting qualitative observation about the graph: that the function lies above the horizonatal asymptote to the left of x = -1 and above the asymptote to the right of x = -1. Proof 2 (Contradiction). AFSOC that g is surjective. This means $\f\forall y \in \mathbb{R}$. y \in I$mg(R -{-1}) In particular, then, we know 1 \in Img(R -{-1}), so \exists $x \in \mathbb{R}$ -{-$1}. g(x) = 1. Let such an x be given. This means $g(x) = \\frac{x}{x+1}$ = 1. Multiplying both sides, we find x = x + 1. Subtracting, we find 0 = 1, clearly a contradiction \times\times\times\times Therefore, $1 \\notin \\mathrm{Im}_g$($\mathbb{R}$ -{-1}), so g is not a surjection. Notice that this second proof does prove that g is not a surjection, but it doesn't add any other information about how the function behaves (like the previous proof did). Let's move on from surjections and talk about a closley related property of functions.
### 7.4.2 Injective (1-to-1) Functions When trying to prove a function is surjective, we took an arbitrary element of the codomain and had to find at least one element of the domain that corresponded to the original element. Sometimes there is exactly one such element, sometimes there are many, and sometimes there are none. What we will do now is consider those functions that fall into the "exactly one" case. We won't be presuming here that functions are already surjective. Rather, we are imposing this condition: we want there to be no more than one input for any given output. There might be exactly one or there might be none, but there certainly aren't two or more. These types of functions are special enough that we give them a name.
Definition
<div class="def-definition" markdown>
**Definition 7.4.6. Let A, B be sets and let $f : A \\to B$ be a function. We say f**
</div>
is an injective function if and only if it has the property that $\\f\forall a_1, a_2 \\in A$. a1 \neq a2 =$\Rightarrow f$(a1) $\neq$ f(a2) Equivalently, we just say "f is injective" (adjectival form), or that "f is an injection" (nounal form). (The term "1-to-1"---sometimes written "1-1"---is a fairly commonly used synonym for this word, so we will mention it here but won't use it again. This is just in case you've seen this term somewhere else.) In other words, this defining property requires that "distinct inputs yield distinct


> 🇨🇳 **证明非满射** 找到一个陪域元素没有原像：定义 $b \in B$，证明 $\f\forall a \in A.\, f(a) \neq b$。


outputs". Also, remembering that the contrapositive of a statement is logically equivalent, we can express this property as $\\f\forall a_1, a_2 \\in A$. f(a1) = f(a2) =$\Rightarrow a$1 = a2 This expresses the equivalent notion that "if two outputs are equal, they must come from the same input". Think about how this definition conveys the notion we described above. Say we have an injective function f : A \to B, and let's say we are given an element b \in B. Does this definition say that there is at most one element x \in A such that f(x) = b? What possibilities does the definition allow? Motivation Let's motivate this by a particular application of functions. Think of a function as a code-word machine for you to send and receive secret messages with a friend. Your friend writes down a secret message, puts it in the encoder, and out pops a scrambled code that he sends to you. Later, you receive this scrambled code. You would really like to know that this code only came from at most one input phrase. What if you try to decode it and it comes out with both I HATE YOU and I LOVE YOU? What are you supposed to think then? Did your friend mean to sedn you both messages? What a terrible code system you've designed if both of those conflicting messages are encoded as the same scrambled message! In this context, it would be much nicer to have an encoding function where two distinct inputs can't possibly give the same output. This is presicely the defining property of being an injection. Negating the Definition It might be helpful to think about the property of being an injection in terms of a schematic diagram, and in terms of the negation of the definition. Let's find that negation first: \n\neg {\f\forall a1, a2 \in A. a1 \neq a2 =$\Rightarrow f$(a1) \neq f(a2) } $\Leftrightarrow$ {$\exists a$1, a2 $\in A$. a1 ̸$= a2 \wedgef(a1) = f(a2)$ } (Remember that the negation of P =$\Rightarrow $\mathbb{Q}$ is P \wedge\negQ!) This says a function is not injective if and only if we can find two distinct domain elements that output the same codomain element. With that in mind, here are canonical examples of an injective and non-injective function$:


> 🇨🇳 **例** 证明 $f: \mathbb{R} \to \mathbb{R}$, f(x) = 3x - 7$ 是双射。单射：$f(x) = f(y) $\Rightarrow$ 3x-7=3y-7 $\Rightarrow$ x=y$。满射：给定 $b$，取 $a = (b+7)/3$，则 $f(a) = b$。


$f : A \\to B$ injective A B $f : A \\to B$ NOT injective The non-injective function has two distinct domain elements that output the same codomain element, whereas the injective function avoids this situation. It might feel a little odd to phrase a property in this kind of negative sense---a function is only injective if it doesn't have... ---but this is actually somewhat common in mathematics. (We will even see this idea later on when we talk about infinite sets, which are just... sets that are not finite!) This negative formulation is easy enough to remember, and we can always relate it to another, positive formulation: an injective function has only 0 or 1 inputs corresponding to any given output.
Examples
Let's think about how to prove/disprove the injectivity of functions. As you might guess, the first two versions of the definition given above are useful when trying to show a function is injective: take two distinct elements of the domain and show their outputs are different, or take two equal outputs and show they came from equal inputs. The negation can also be used to show a function is injective via a proof by contradiction. Also, the third version is useful when proving a function is not injective: a counterexample amounts to finding two distinct inputs with the same output. Let's see these techniques in action with a few examples. In fact, we will use some of the same examples we looked at in the previous section about surjections!
Example 7.4.7. Consider $p : \\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{N}$ defined by $p(a, b) = ab$. Is p injective?
By trying some particular values of (a, b), we can see that p is definitely not an injection. Pick any number that has two different factorizations, like 12 = 3 $\cdot 4 = 2 \cdot$ 6. By letting (a, b) = (3, 4) and (c, d) = (2, 6), we can easily prove this claim. But we can do this even more easily, by noting that the order of the coordinates of an element like (a, b) matters!
<div class="def-proof" markdown>
*Proof.* This function is not injective.
</div>
Let (a, b) = (1, 2) and (c, d) = (2, 1). Notice that (a, b) \neq (c, d) because 1 \neq 2. Also, notice that p(a, b) = 1 $\cdot$ 2 = 2 and p(c, d) = 2 $\cdot$ 1 = 2. Thus, p(a, b) = p(c, d). This shows that p is not injective.


> 🇨🇳 **例** 证明 $f: \mathbb{R} \to \mathbb{R}$, f(x) = x^2$ 非单射：$f(1) = f(-1) = 1$ 但 $1 \neq -1$。非满射：$b = -1$，但 $x^2 \geq 0 > -1$，故 $\f\forall x.\, f(x) \neq -1$。


Example 7.4.8. Let C be the set of all cars in the United States. Let S be the
set of all strings of letters and digits that are of length at most 7 (i.e. these are the potential strings you might see on a car's license plate). Let f : C $\to S$ be defined by inputting a car and outputting its license plate string. Is the function f an injection? No, we don't think so! The same license plate string could appear on different cars that are registered in different states. Now, we don't have any examples of this on hand, so this isn't a totally formal proof, but hopefully you see the idea. Could we amend the function definition to make it an injection? Sure, we could try! Consider also defining S to be the set of U.S. states. Let the function g : C $\to L \times S be defined by inputting a car and outputting the order pair of that car's license plate string and home state. This will be an injection, because no two cars in the same state can have the same plate. (Again, this is not really a formal proof$; we are just trying to illustrate the concept of injectivity with a non-numerical example.)
Example 7.4.9. Let $d : \\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{Z}$ be the function defined by d(a, b) = a -b.
Determine whether d is an injection and prove your claim. It turns out d is not an injection! Notice that a -b = (a + 1) -(b + 1). We can use this to find a counterexample: Consider the pairs (2, 1) $\in \mathbb{N}$ \times \mathbb{N}$ and (3, 2) \in \mathbb{N}$ \times \mathbb{N}$. Notice that d(2, 1) = 1 and d(3, 2) = 1. Since (2, 1)$ $\neq$ (3, 2) and yet d(2, 1) = d(3, 2), we conclude that d is not an injection.
Example 7.4.10. Let $F : P(\\mathbb{N}) \\to P(\\mathbb{Z})$ be defined by
$\f\forall X \in P$($\mathbb{N}$). F(X) = [ a\in X {a, -a} Do you see what this function does? (Can you explain why it's even a welldefined function?) Let's show you a few examples to give you an idea: F {{1} } = [ a\in{1} {a, -a} = {-1, 1} F {{1, 3, 5} } = [ a\in{1,3,5} {a, -a} = {-1, 1} \cup{-3, 3} \cup{-5, 5} = {-5, -3, -1, 1, 3, 5} F(\emptyset) = [ a$\in \emptyset$ {-a, a} = $\emptyset$ F($\mathbb{N}$) = $\mathbb{Z}$ -{0} We claim that F is an injection. Think about how to prove this before reading our proof. In particular, think about the different strategies we might employ here, based on the formal definition of injectivity. Might one strategy be more fruitful than another?


> 🇨🇳 **有限集上的性质** 若 $|A| = m, |B| = n$：(1) $f$ 单射 $\Rightarrow m \leq n$；(2) $f$ 满射 $\Rightarrow m \geq n$；(3) $f$ 双射 $\Rightarrow m = n$。(4) 当 $m = n$ 时，单射、满射、双射三者等价。


<div class="def-proof" markdown>
*Proof.* WWTS F is an injection. Let X, Y $\in P$($\mathbb{N}$).
</div>
Suppose that X \neq Y. WWTS F(X) \neq F(Y ). Since X \neq Y, we have two cases: either X ̸$\subseteq Y$ or Y ̸$\subseteq X$ (or both). Suppose X ̸$\subseteq Y. This means \exists n \in X. n \notin Y$. Let such an n be given. Since n \in{-n, n} and n \in X, we see that n \in F(X), by the definition of F. However, since n \notin Y, we see that \f\forall a \in Y. n \notin{-a, a}. This follows because n \notin Y, as well as the fact that $n \in \mathbb{N}$ and Y \subseteq \mathbb{N}$, so \f\forall a \in Y$. n \neq -a $\in \mathbb{Z}$. Accordingly, n \notin F(Y ). This shows that F(X) \neq F(Y ). In the other case, where Y ̸\subseteq X, we can follow the exact same argument with the roles reversed (i.e. switching X and Y in every step). This shows that F(Y ) \neq F(X). Together, we have shown that \f\forall X, Y \in $\\mathcal{P}(\\mathbb{N})$. X \neq Y =$\Rightarrow$ F(X) \neq F(Y ). This shows F is an injection. Think about how this proof might go if we used a different technique. Say we started by assuming X, Y $\in P$($\mathbb{N}$) and that F(X) = F(Y ). Can we deduce that X = Y ?
### 7.4.3 Proof Techniques for Jections Let's summarize the concepts of this section so far by presenting some proof templates. These can be used when you are trying to prove/disprove that a function is injective/surjective. We like using the shorthand "Jections" to refer to these two function properties together. Prove that f is surjective 1. Let b $\in B$ be arbitrary and fixed. 2. Define a =. 3. Show that a \in A. 4. Show that f(a) = b. 5. This shows that b \in Imf(A). Thus, Imf(A) = B, so f is surjective. Prove that f is not surjective 1. Define b =. 2. Show that b \in B. 3. Let a $\in A$ be arbitrary and fixed.


> 🇨🇳 **鸽巢原理与单射** 若 $f: A \to B$ 是单射，则 $|A| \leq |B|$。其逆否命题：若 $|A| > |B|$，则任何函数 $f: A \to B$ 都不是单射。这正是鸽巢原理的函数表述！


4. Show that f(a) \neq b. (Alternatively, suppose f(a) = b and find a contradiction.) 5. This shows that $\exists b \in B. b \notin I$mf(A), so f is not surjective. Prove that f is injective 1. Let x, y \in A be arbitrary and fixed. 2. Suppose that f(x) = f(y). 3. Deduce that x = y. Alternatively: 1. Let x, y \in A be arbitrary and fixed. 2. Suppose that x \neq y. 3. Deduce that f(x) \neq f(y). Prove that f is not injective 1. Define x = and define y =. 2. Show that x \in A and y $\in A$. 3. Show that x $\neq$ y. 4. Show that f(x) = f(y). Prove that f is bijective 1. Prove that f is injective. 2. Prove that f is surjective.
### 7.4.4 Bijections You might have guessed what we have been building towards here. Think about the two main properties of functions we just studied: surjectivity and injectivity. What happens when a function has both of these properties? What if a function has the property that, for every element of the codomain, there is at least one corresponding element in the domain (surjectivity) and there is also at most one such element (injectivity)? That's right: for every output, there is exactly one input! This is an incredibly nice property to have, and will be the foundation for our forthcoming discussion of cardinality (i.e. the size of a set). Let's make a definition and then discuss some examples.


> 🇨🇳 **例** 5 个学生分 4 间宿舍，至少一间住 2 人以上。若 $f$ 是"学生$\to$宿舍"的函数，则 $|\text{domain}|=5 > 4 = |\text{codomain}|$，故 $f$ 不可能单射。


Definition
<div class="def-definition" markdown>
**Definition 7.4.11. Let A, B be sets and let $f : A \\to B$ be a function. We say**
</div>
f is a bijective function if and only if f is both injective and surjective. Equivalently, we just say "f is bijective" (adjectival form), or that "f is a bijection" (nounal form). We will sometimes say that f is a bijection between the sets A and B, instead of saying "from A to B". (The reason for this will become clear in the next section!) Notice that this definition is, logically speaking, an AND statement. For the moment, anyway, the only technique we have to prove a function is bijective is to just prove it is surjective and prove it is injective. Similarly, to prove a function is not bijective, we need to prove it is either not surjective or not injective. (It might be that both properties fail, but one such proof is sufficient to show a function is not bijective.) Rather than go over these same techniques (which are nicely summarized right before this section), we will just point out whether some of the examples we have seen thus far are bijections are not.
Example 7.4.12.
(a) Let $p : \\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{N}$ be the function defined by $p(a, b) = ab$. We proved that p is surjective but not injective, so it is not a bijection. (b) Let $d : \\mathbb{N} \\times \\mathbb{N} \\to \\mathbb{Z}$ be the function defined by d(a, b) = a -b. We proved that d is surjective but not injective, so it is not a bijection. (c) Let $g : \\mathbb{R} - \\{-1\\} \\to \\mathbb{R}$ be the function defined by \f\forall $x \in \mathbb{R}$. $g(x) = \\frac{x}{1 + x}$ We proved that g is not surjective. (Specifically, we showed 1 \notin Img($\mathbb{R}$ - {-1}).) We will ask you in this section's exercises to prove that g is an injection, though. Together this means g is not a bijection. However, consider defining $h : \\mathbb{R} - \\{-1\\} \\to \\mathbb{R} - \\{1\\}$ by the same "rule" as g, i.e. \f\forall $x \in \mathbb{R}$ -{1}. h(x) = x 1+x. We asked you to prove in the exercises of Section 7.3.5 that this function satisfies Imh($\mathbb{R}$ -{-1}) = $\mathbb{R}$ -{1}. This shows that h is a surjection. Furthermore, we will ask you to prove in this section's exercises that a function defined in this way---by taking an injection, using the same "rule", and redefining the codomain to be the image---produces a bijection. Together, all of this proves that h is a bijection from $\mathbb{R}$-{-1} to $\mathbb{R}$-{1}.
Example 7.4.13. Let's look at one new example, specifically chosen to preview
some of the main ideas coming up ahead. Define E $\subseteq \mathbb{N}$ to be the set of all even


> 🇨🇳 **函数的复合与性质** 若 $f: A \to B$ 和 $g: B \to \mathbb{C}$ 都是单射/满射/双射，则 $g \circ f$ 也是。但逆命题不成立——g \circ f 单射只推出 f 单射，g \circ f 满射只推出 $g$ 满射。


natural numbers; that is, E = {e $\in \mathbb{N}$ | $\exists k$ $\in \mathbb{N}$. e = 2k} Define the function d : $\mathbb{N}$ $\to E$ by d(n) = 2n. We claim d is a bijection.
<div class="def-proof" markdown>
*Proof.* First, let's prove d is a surjection. Let e $\in E$ be given.
</div>
By the definition of E, $\exists k \in \mathbb{N}$ such that e = 2k. Let such a k be given. This tells us d(k) = 2k = e. Since e was arbitrary, we conclude that d is a surjection. Second, let's prove d is an injection. Let m, $n \in \mathbb{N}$ and assume d(m) = d(n). This means 2m = 2n. Canceling the 2s from both sides, we find that m = n. Thus, d is an injection. Together, this proves that d is a bijection. We'll motivate some future considerations by posing some questions: Does it seem a little strange to you that there is a bijection between $\mathbb{N}$ and E, a set that is a proper subset of $\mathbb{N}$? Is it always possible to find a bijection between a set and a subset of itself? Have we seen other examples of this situation before? Motivation The main idea behind a bijection $f : A \\to B$ is that we can pair up the elements of A and B and identify them with each other, one by one. This idea follows from the definitions of both surjectivity and injectivity: every output has exactly one corresponding input. Furthermore, think more carefully about what we show in the proofs of such properties. In proving f is surjective, we show we can "move" from the codomain back to the domain in at least one way, and then in proving f is injective, we show that this is the only way to do it. In a sense, we are showing how to "undo" the function f and reverse its action. In fact, we are implicitly defining a new function from B back to A. Have you previously talked about the inverse of a function? That is precisely what we are rediscovering now! To make this notion of "moving back from the codomain to the domain" rigorous enough, we need to have a brief discussion about how to "combine" functions appropriately. Right after that, we will be able to give a precise definition of what we mean by the inverse of a function, and relate this to bijections. All of this happens in the next section.
### 7.4.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you


> 🇨🇳 **练习** (1) 判断 $f: \mathbb{Z} \to \mathbb{Z}$, f(n) = 2n-1$ 是否单射/满射/双射，并证明。(2) 判断 $f: $\mathbb{N} \times \mathbb{N}$ \to \mathbb{N}$, f(m,n) = 2^m \cdot 3^n$ 是否单射。


can confidently answer these before moving on will help your understanding and memory! (1) Write down a definition of surjective in terms of an image. Then, write down a definition of surjective in terms of quantifiers. (2) Describe two different ways of proving that a function is injective. (3) Can a function be both injective and surjective? If so, give an example. (4) Can a function be neither injective nor surjective? If so, give an example. (5) Consider the following schematic diagrams. For each one, declare whether or not it is a function; and, if it is, declare whether or not it is (a) an injection and (b) a surjection. Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Suppose f : $\mathbb{R} \to \mathbb{R}$ is an increasing function; that is, suppose \f\forall x, $y \in \mathbb{R}$. x < y =$\Rightarrow f$(x) < f(y) Prove that f must be injective. Then, prove that f need not be surjective by defining an increasing function that is not surjective. (2) Let $g : \\mathbb{R} - \\{-1\\} \\to \\mathbb{R}$ be the function defined by \f\forall $x \in \mathbb{R}$. $g(x) = \\frac{x}{1 + x}$ Is g injective or not? Prove your claim. (3) Give an example of a function f : $\\mathcal{P}(\\mathbb{N})$ $\to \mathbb{N}$ that is surjective. Prove that it is. (Hint: Be careful about the fact that $\emptyset \in P$($\mathbb{N}$). Also, consider looking at Section 5.5.2 for some inspiration... ) (4) Give an example of a function F : $\mathbb{N}$ $\to P$($\mathbb{N}$) that is injective. Prove that it is. Then, prove that your function F is not surjective. (Note: Yes, we are asking you to prove your function is not surjective without knowing what function you defined. We know we are right! You will learn about our trick later in this chapter... )


> 🇨🇳 (3) 证明：若 $f: A \to B$ 和 $g: B \to \mathbb{C}$ 都是双射，则 $g \circ f$ 也是双射。(4) 举一个 g \circ f 是单射但 $g$ 不是单射的例子。


(5) Suppose $f : A \\to B$ and $g : B \\to \\mathbb{C}$ are surjective functions. Prove that g \circ f : A $\to \mathbb{C}$ is also surjective. (6) Let f : A \to B be an injective function. Define g : A \to Imf(A) by setting \f\forall x \in A. g(x) = f(x). Prove that g is a bijection. (7) Define F : $\mathbb{R}$\timesR $\to \mathbb{R}$\timesR by F(x, y) = (x+y, 2x$-y). Prove F is bijective. (Hint: In your scratch work, you should try to solve a system of two equations. See Section 1.3.2 for some suggestions about how to do that.) (8) Let A, B be sets. Let g : A \to B be an injection. Let X \subseteq A. Let h : X \to B be the function defined by \f\forall x $\in X$. h(x) = g(x). (That is, h is defined by the same "rule" as g, but on a "restricted domain".) Prove that h is also an injection.
## 7.5 Compositions and Inverses
### 7.5.1 Composition of Functions Motivation Let's think about the schematic interpretation of functions for a moment. Imagine that we have a function $f : A \\to B$ and we also have a function $g : B \\to \\mathbb{C}$, defined like this: A f : A \to B B B C $g : B \\to \\mathbb{C}$ In a heuristic sense, f is like a "map" that gives us a particular route from elements of A to elements of B, while g is like a "map" from elements of B to elements of C. What would happen if we were to simply follow the "maps" one after the other? That is, let's combine the two by overlaying them,


> 🇨🇳 (5) 设 $A = \{1,2,3,4\}$，$B = \{a,b,c\}$。是否存在 $A$ 到 $B$ 的单射？满射？(6) 证明：有限集上，函数是单射当且仅当它是满射（当 $|A|=|B|$ 时）。


$g : B \\to \\mathbb{C}$ A $f : A \\to B$ B and then simply travel from A all the way to C, cutting out the middle man: A C g \circ f : A $\to \mathbb{C}$ This seems like a reasonable thing to do, right? Yes, of course it is! Whenever we have mathematical objects at our disposal, we're always curious about how we can resonably combine them and manipulate them and generalize them. In the case of functions, we call this combination a composition of functions. You might notice that such a composition really only makes sense if the codomain of the "first" function and the domain of the "second" function are the same. This is incorporated in the following definition.
Definition
<div class="def-definition" markdown>
**Definition 7.5.1. Let A, B, C be sets, and let $f : A \\to B$ and $g : B \\to \\mathbb{C}$ be**
</div>
functions. Consider the function h : A $\to \mathbb{C} defined by \f\forall a \in A$. h(a) = g(f(a)) We say that h is the composition of g with f and we write h = g \circ f. We also shorten this terminology and say h is "g composed with f". This incorporates all the ideas we mentioned above. It requires that the codomain of f (the "first" function applied) to be the domain of g (the "second" function applied). Another intuitive idea is to think of a function as a machine or a black box. Elements of the domain go in and elements of the codomain come out. We don't necessarily know what the machine does; we only see what comes out. Now,


> 🇨🇳 (7) 逆否命题在证明单射中的使用：写出"$f$ 不是单射"和"$f$ 不是满射"的否定形式，并用真值表验证。


think of hooking up two machines, one for f and one for g; take the output of f's machine and plug it into g's machine. What comes out is an element of C. We can take the work of these two machines and think of it as the work of one bigger machine. This is what the composition g \circ f does; it's one larger machine that takes the operations of two machines and does them in a specified order. Notation Notice the ordering of the notation g \circ f and how it compares to the order in which we apply the functions: f comes first, and then g, i.e. g(f(a)). In words, we would read "g(f(a))" as "g of f of a". In fact, if you find yourself having trouble remembering this order, here's a recommendation: read the " \circ " out loud as "after". Thus, h = g \circ f would mean "g after f", because we take an element of a, apply f first, and then apply g. It is also important to remember the notation of composed functions and to distinguish the function g \circ f itself from an application of the function g \circ f to some element x $\in A$. For instance, to write "g of f of x" using the " \circ " notation, we would write (g \circ f)(x) because we are "hitting" the element x with the function g \circ f. However, the following notation make no sense because it mixes up the ideas of functions and elements: g \circ f(x) Do you see the difference? The object f(x) is an element of B, the codomain of f. But g is a function. What does it mean to compose a function with an element of a set? This doesn't work. Be careful with this, in general! This distinction will be especially important when we have to compose several functions together, like (h \circ (g \circ k) \circ f)(z), where z is an element of f's domain, and f, g, h, k are functions.
Examples
Example 7.5.2. Let C : $\mathbb{R} \to \mathbb{R}$ be defined by
$\f\forall x \in \mathbb{R}$. C(x) = x -273.15 Let F : $\mathbb{R}$ $\to \mathbb{R}$ be defined by \f\forall x \in \mathbb{R}$. F(x) = 9 5x + 32 The function C converts a temperature from degrees Kelvin to degrees Celsisus. The function F converts from degrees Celsius to degrees Fahrenheit. Then the function F \circ C converts from degrees Kelvin to degrees Fahrenheit


> 🇨🇳 **有限函数的计数** 从 $[m]$ 到 $[n]$ 的函数数为 $n^m$。单射函数数（$m \leq n$ 时）为 $P(n,m) = \frac{n!}{(n-m)!}$。双射函数数（$m=n$ 时）为 $n!$。


directly. We can compose the "rules" for the functions and find a formula for this direct conversion: $\f\forall x \in \mathbb{R}$. (F \circ C)(x) = F(C(x)) = F(x -273.15) = 9 5 $\cdot$ {x -273.15) + 32 = 9 5x -459.67
Example 7.5.3. Let f : $\mathbb{R}$ $\to \mathbb{Z}$ be the function defined by
$\f\forall x \in \mathbb{R}$. f(x) = ⌊x⌋ (Recall that ⌊x⌋is the floor of x: it is the largest integer $z \in \mathbb{Z}$ that satisfies z \leq x. Let g : $\mathbb{Z}$ $\to \mathbb{N}$ be the function defined by \f\forall $z \in \mathbb{Z}$. g(z) = ( -z if z < 0 z + 1 if z \geq0 Let's find g \circ f. Notice that whenever $x \in \mathbb{R}$ satisfies x < 0, we will have ⌊x⌋x < 0, as well. Similarly, whenever $x \in \mathbb{R}$ satisfies x \geq0, we will have ⌊x⌋\geq0. This tells us that the composition g \circ f will also be a piece-wise function: \f\forall $x \in \mathbb{R}$. (g \circ f)(x) = ( -⌊x⌋ if x < 0 ⌊x⌋+ 1 if x $\geq 0$
Questions: Is this function injective? Surjective? Try to prove your claims!
Example 7.5.4. Define f : $\mathbb{N} \to \mathbb{N}$ and g : $\mathbb{N} \to \mathbb{N}$ and h : $\mathbb{N} \to \mathbb{N}$ by
$\f\forall n \in \mathbb{N}$. f(n) = n + 3 $\f\forall n \in \mathbb{N}$. g(n) = n2 \f\forall n \in \mathbb{N}$. h(n) = 2n -1 (Question: Are you sure these are well-defined functions? Why?) We can find "rules" for the compositions g \circ f and h \circ f: $\f\forall n \in \mathbb{N}$. (g \circ f)(n) = g(f(n)) = g(n + 3) = (n + 3)2 = n2 + 6n + 9 $\f\forall n \in \mathbb{N}$. (h \circ g)(n) = h(g(n)) = h(n2) = 2n2 -1 We can then use these to find a rule for a further composition, like h \circ (g \circ f): $\f\forall n \in \mathbb{N}$. {h \circ (g \circ f) } (n) = h {(g \circ f)(n) } = h {n2 + 6n + 9 } = 2(n2 + 6n + 9) -1 = 2n2 + 12n + 17 Likewise, we can use these to find a rule for (h \circ g) \circ f: $\f\forall n \in \mathbb{N}$. {(h \circ g) \circ f } (n) = {h \circ g)(f(n)) = (h \circ g)(n + 3) = 2(n + 3)2 -1 = 2(n2 + 6n + 9) -1 = 2n2 + 12n + 17


> 🇨🇳 **像的单射性** $f$ 是单射当且仅当 $f$ 在 $A$ 的任意两个不相交子集上的像也不相交。等价地，$X \cap Y = \emptyset $\Rightarrow$ f(X) \cap f(Y) = \emptyset$。


Look at that, they're the same rule! That is, we just proved that (h \circ g) \circ f = h \circ (g \circ f) in the sense of functions by showing that they yield the same output on every allowable input. Composition is Associative There was nothing particularly special about the functions f, g, h used in the previous example. The result we obtained is actually true in general. The following theorem and its proof will show this. We are proving that function composition is associative. This means that whenever we have a string of compositions, we can move the parentheses around at will; we know that the order in which we apply the parentheses doesn't matter.
<div class="def-theorem" markdown>
**Theorem 7.5.5. Let A, B, C, D be any sets. Let $f : A \\to B$ and $g : B \\to \\mathbb{C}$**
</div>
and h : C $\to D$ be functions. Then, h \circ (g \circ f) = (h \circ g) \circ f
<div class="def-proof" markdown>
*Proof.* WWTS that the outputs of the two functions h \circ (g \circ f) and (h \circ g) \circ f
</div>
are the same, for every possible input. Let x $\in A$ be given. Applying the definition of composition, we see that $[h \circ (g \circ f)](x)$ = h {g \circ f)(x) } = h {g(f(x)) } and $[(h \circ g) \circ f](x)$ = {h \circ g } (f(x)) = h {g(f(x)) } Compositions and Jections Here's something interesting to ponder now: What happens if we take the composition of two functions with a shared property? Does that property "carry over", as well? For instance, if we compose two injections, do we get another injection? Does only one of the composed functions need to be an injection to guarantee the composition is an injection? Similarly, let's say we have a composition of two functions. If we know the composition is a surjection, can we necessarily deduce that one of the functions we composed is also a surjection? Do they both need to be? We will state and prove some claims about questions like these in this short section. We will let you prove some related facts (or find appropriate counterexamples, as the case may be) in the exericses, both for this section and at the end of the chapter.
Proposition 7.5.6. Let A, B, C be sets and let $f : A \\to B$ and $g : B \\to \\mathbb{C}$ be
functions. If g \circ f is injective, then f is necessarily injective.


> 🇨🇳 **满射的像** $f$ 是满射当且仅当 $f(A) = B$。有时更容易证明某个特定的像等于陪域，从而证明满射。


(Notice that this doesn't assume any properties of g; it doesn't even have to be injective, necessarily! As an exercise, try to find an example of functions $f : A \\to B$ and $g : B \\to \\mathbb{C}$ such that g \circ f is injective and g is injective, and also an example where g \circ f is injective but g is not injective.)
<div class="def-proof" markdown>
*Proof.* Let x, y $\in A$ be given. Suppose f(x) = f(y). WWTS x = y.
</div>
Since g is a well-defined function, g(f(x)) = g(f(y)). This means (g \circ f)(x) = (g \circ f)(y). Since g \circ f is injective, x = y. This was our goal, so the claim is proven. It turns out that the converse of the claim we just proved is False. Since that claim is one about all functions, disproving it requires us to produce a counterexample.
Proposition 7.5.7. Let A, B, C be sets and let $f : A \\to B$ and $g : B \\to \\mathbb{C}$ be
functions. Suppose f is injective. Then it is not necessarily the case that g \circ f is injective. Try doing some scratch work on your own to come up with a counterexample before reading about ours. Remember that you don't need to find the most interesting or complicated one, nor do you necessarily need one defined by a rule; you just need to be able to define one!
<div class="def-proof" markdown>
*Proof.* We will exhibit a counterexample.
</div>
Define A = {1, 2} and B = {♥, ♦} and C = {$\star$}. Define f by setting f(1) = ♥and f(2) = ♦. Notice f is injective because f(1) \neq f(2). Define g by setting g(1) = g(2) = \star. Notice g \circ f is defined by (g \circ f)(1) = \starand (g \circ f)(2) = $\star$. This shows g \circ f is not injective, because (g \circ f)(1) = (g \circ f)(2) but 1 $\neq$ 2.
### 7.5.2 Inverses Motivation As we said before, a bijection $f : A \\to B$ has a very nice property, in that f "pairs off" the elements of the two sets, A and B. Given an element a \in A, there is exactly one element b \in B that satisfies f(a) = b. This is because f is a well-defined function. But we also know that a is the only domain element associated with b in this way. This is because f is a bijection. Because of this unique association in both directions, we can think of "reversing" the action of f. Given an element b $\in B$, identify the a that would produce that b. This is what an inverse function does. Here, we will define it in terms of function composition and identity functions. This is also the reason we say a bijection


> 🇨🇳 **运算保持性质** 设 $f: A \to A$。若 $f$ 是单射，则 $f \circ f$ 也是单射；若 $f$ 是满射，则 $f \circ f$ 也是满射。这对反复复合也成立。


is between two sets as opposed to just from one set to the other; as soon as we have it one way, we know we can have it the other way, too! Before we see the definition, let's quickly recall the definition of the identity function that we saw before. It plays an important role in the forthcoming definition of inverse.
Definition: Given a set X, the identity function IdX : X $\to X$
is defined by $\f\forall z \in X$. IdX(z) = z.
Definition
Notice that this definition doesn't say anything about the functions being bijections. This is purely a formal definition of what an inverse function means. Afterwards, we will have to prove any claims about hwo inverses and bijections are related.
<div class="def-definition" markdown>
**Definition 7.5.8. Let $f : A \\to B$ be a function. Suppose there is a function**
</div>
g : B $\to A$ such that f \circ g : A \to A satisfies f \circ g = IdA and g \circ f : B $\to B$ satisfies g \circ f = IdB. Then we say g is the inverse of f and write g = f -1. (Notice that some conditions are implicitly stated by the assumptions and conclusions in the definition above. Specifically, it must be that B = Imf(A), to make sure g is a function. Likewise, A = Img(B).)
Example
Let's look back at a function we saw before when we discussed bijections. With your help in the exercises, we learned that this function is a bijection. Here, we will find its inverse.
Example 7.5.9. Let $h : \\mathbb{R} - \\{-1\\} \\to \\mathbb{R} - \\{1\\}$ be defined by
$\f\forall x \in \mathbb{R}$ -{-1}. h(x) = x 1 + x To find a candidate function that will be the inverse of h, it usually helps to set the "rule" for h equal to some new variable, and then solve for x. Here, let's say h(x) = y. How can we "reverse" this process and identify what x is, in terms of y? Observe that we can make some algebraic steps, as follows: $h(x) = y \Leftrightarrow x 1 + x = y \Leftrightarrow (1 + x)y = x \Leftrightarrow xy + y = x \Leftrightarrow y$ = x(1 -$y) \Leftrightarrow x$ = y 1 -y


> 🇨🇳 **构造反例** 当需要证明某命题不成立时，构造反例是最直接的方法。例："$g \circ f$ 满射推出 $f$ 满射"的反例——$A=\{1\}, B=\{1,2\}, C=\{1\}$，$f(1)=1, g(1)=g(2)=1$。$g \circ f(1)=1$ 是满射，但 $f$ 不是满射。


This scratch work has given us a candidate for the inverse of h. We haven't proven anything with these observations! What we have to do now is make a claim and then demonstrate, for the reader, all of the essential facts. Notice that we took care to define a new function H, and used it to prove that H = h-1, in fact. It would be presumptuous and erroneous to define h-1 and then work with it. We are trying to show h has an inverse, so we can't just declare it has one at the beginning of our proof!
<div class="def-proof" markdown>
*Proof.* Define S = $\mathbb{R}$ -{-1} and T = $\mathbb{R}$ -{1} for convenient shorthand, so
</div>
h : S $\to T$. Let H : T $\to S$ be the function defined by $\f\forall y \in T$. H(y) = y 1-y. First, let's show that H is a well-defined function. For every y \in T, we know y \neq 1, so 1 -y \neq 0. Thus, the fraction y 1-y is a well-defined real number. Furthermore, we can argue that y 1-y \neq -1. AFSOC that y 1-y = -1. Then multiplying through by 1 -y tells us y = y -1, a clear contradiction. Second, let's show that H \circ h = IdS. Let x \in S be given. Observe that (H \circ h)(x) = H(h(x)) = H ( x 1 + x ) = x 1+x 1 - x 1+x \cdot 1 + x 1 + x = x (1 + x) -x = x 1 = x Third, let's show that h \circ H = IdT. Let y \in T be given. Observe that (h \circ H)(y) = h(H(y)) = h ( y 1 -y ) = y 1-y 1 + y 1-y \cdot 1 -y 1 -y = y (1 + y) -y = y 1 = y Therefore, by the definition of inverse, H = h-1. Checking Both Directions Let's say f : A \to B is a function, and you have made a claim about f having an inverse by defining a function g : B $\to A$. It is extremely important that you show both compositions yield the identity function; that is, you must show both f \circ g = IdB and g \circ f = IdA You might occasionally forget to do so, or you just might not see why this is necessary. To help you understand this importance, we have included Exercise


> 🇨🇳 **等价刻画** 以下等价：$f$ 是双射 $\Leftrightarrow$ $f$ 有逆函数 $\Leftrightarrow$ $f$ 既是单射又是满射。这三种表述可以互换使用。


2 in Section 7.5.4 below. It asks you to find an example where "one way" yields the identity function but the "other way" does not, so that the proposed function is actually not an inverse. Try to find several examples, if you can. The more striking you make this point, the better!
### $7.5.3 Bijective \Leftrightarrow I$nvertible As we have been hinting at all along, a bijective function has an inverse. This claim's converse holds, as well, so we can state and prove this if and only if statement. The word in the section heading here---invertible---is often used to mean "has an inverse".
<div class="def-theorem" markdown>
**Theorem 7.5.10. Let A, B be any sets. Let $f : A \\to B$ be a function. Then,**
</div>
$f is bijective \Leftrightarrow f$ has an inverse f -1 : B $\to A$
<div class="def-proof" markdown>
*Proof.* ( =$\Rightarrow$) Assume f is bijective. This means f is surjective and injective.
</div>
We need to define an inverse function for f. Let's define g : B $\to A$ as follows: Let b \in B be given. Since f is surjective, we know \exists a \in A. f(a) = b. Let such an a be given. Since f is injective, we know that \f\forall x \in A. x \neq a =$\Rightarrow f$(x) \neq f(a) = b That is, we know this a is the unique element of A that satisfies f(a) = b. Let's define g(b) = a. This is a well-defined function because of these observations. Next, observe that (f \circ g)(b) = f(g(b)) = f(a) = b, so f \circ g = IdB. Also, observe that (g \circ f)(a) = g(f(a)) = g(b) = a, so g \circ f = IdA. Therefore, g = f -$1, so f has an inverse. (\Leftarrow=) Assume f has an inverse function, f$ -1 : B $\to A$. First, let's show f is injective. Let a1, a2 $\in A$ be given. Observe that f(a1) = f(a2) =$\Rightarrow f$ -1(f(a1)) = f -1(f(a2)) f -1 : B \to A is a function =$\Rightarrow$(f -1 \circ f)(a1) = (f -1 \circ f)(a2) definition of composition =$\Rightarrow I$dA(a1) = IdA(a2) definition of identity =$\Rightarrow a$1 = a2 definition of identity Thus, f is injective. Second, let's show f surjective. Let b \in B be given. Since f -1 is a function, we know \exists a $\in A$. f -1(b) = a. Let such an a be given. Then observe thatf -1(b) =


> 🇨🇳 **上下界** 单射给出 $|A| \leq |B|$，满射给出 $|A| \geq |B|$。两者同时成立则 $|A| = |B| = |\text{像}|$。


a. f -1(b) = a =$\Rightarrow f$(f -1(b)) = f(a) f : A \to B is a function =$\Rightarrow$(f \circ f -1)(b) = f(a) definition of composition =$\Rightarrow I$dB(b) = f(a) definition of identity =$\Rightarrow b$ = f(a) definition of identity Proving a Function is Bijective This helpful theorem now provides us with another technique for proving that a given function f : A \to B is a bijection. Rather than proving f is an injection and a surjection, we can just define a new function g : B $\to A$ and prove that it is the inverse of f, i.e. g = f -1. Then, this theorem applies and tells us that f is a bijection! Depending on the context, one or the other of these strategies might be easier to apply, or you might just be more comfortable with one of them. Keep in mind that both strategies are viable, though! Inverse of an Inverse The following corollary follows immediately from the theorem above. We call it a corollary and not its own theorem because it doesn't really assert anything amazingly new; rather, its conclusion comes from applying the theorem above, as you'll see in the proof.
<div class="def-theorem" markdown>
**Corollary 7.5.11. Let A, B be any sets. Let $f : A \\to B$ be a function.**
</div>
If f is a bijection, then f -1 exists and it is also a bijection. Furthermore, {f -1}-1 = f.
<div class="def-proof" markdown>
*Proof.* Suppose f has an inverse, f -1 : B $\to A$. This means f \circ f -1 = IdB and
</div>
f -1 \circ f = IdA, by the definition of inverse. These are precisely the conditions that show {f -1} = f, again by the definition of inverse! This shows f -1 has an inverse (namely, f itself) so the theorem above tells us that f -1 must be a bijection. Inverse of a Composition Before we move on to some exercises and the next section, let's get your help in putting together the main ideas of this chapter so far. Specifically, we are going to state two results here. The proofs are left for you in the chapter exercises. By working through those proofs, you will (a) solidify your understanding of many of the concepts introduced so far---functions, jections, compositions, inverses--- and (b) obtain a helpful result about how to define the inverse of a composition of functions!


> 🇨🇳 **无限集的特殊性** 在无限集上，单射+满射 = 双射 仍然成立，但"单射推出满射"不再成立——例 $f: \mathbb{N} \to \mathbb{N}$, n \mapsto n+1$ 是单射非满射（1 无原像）。


Proposition 7.5.12. Let $f : A \\to B$ and $g : B \\to \\mathbb{C}$ be bijective functions.
Define h : A $\to \mathbb{C}$ to be h = g \circ f. Then h is also bijective.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Problem 7.8.9.
</div>
Proposition 7.5.13. Let $f : A \\to B$ and $g : B \\to \\mathbb{C}$ be bijective functions.
Define h : A $\to \mathbb{C}$ to be h = g \circ f. Then h is invertible and h-1 = f -1 \circ g-1.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Problem 7.8.10
</div>
### 7.5.4 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) Is the composition of functions associative? (That is, does the order of parentheses matter?) Why or why not? (2) Is the composition of functions commutative? (That is, can we reverse the order?) Why or why not? (3) Suppose $f : A \\to B$ and g : B $\to A$ are functions. How do we prove that g = f -1? (4) Suppose $f : A \\to B$ is a bijection. Is its inverse also a bijection? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Let O be the set of odd natural numbers and let E be the set of even natural numbers. Define a function f : O \to E that is a bijection and prove that it is so by finding its inverse. (2) In this problem, we want you to construct an example that shows the importance of verifying both compositions yield the identity function when we're trying to find the inverse of a function. Define sets A, B and functions f : A \to B and g : B \to A such that \f\forall x $\in A$. g(f(x)) = x


> 🇨🇳 **应用：哈希函数** 哈希函数 $h: U \to [n]$ 通常不是单射（鸽巢原理）。冲突（collision）的处理是哈希表设计的核心问题。


but $\exists y \in B$. f(g(y)) \neq y (Suggestion: You might find an example where A and B both only have one or two elements... Or, you might find an example where A = B = $\mathbb{N}$.) (3) Let U = {$y \in \mathbb{R}$ | -1 < y < 1} and I = {$y \in \mathbb{R}$ | -6 < y < 12}. Let g : U \to I be the function defined by \f\forall x \in U. g(x) = 9x + 3. Prove that g is a bijection by finding g-1. (4) Define the function f : $\mathbb{Z}$ $\to \mathbb{N}$ by \f\forall $z \in \mathbb{Z}$. f(z) = ( -2z + 2 if z \leq0 2z -1 if z > 0 Prove that f is a bijection by finding f -1. (Hint: Your proposed inverse function will also be piece-wise defined. Be careful about the cases that will then come up in your proof.) (5) Challenge: Define I = {$y \in \mathbb{R}$ | -1 < y < 1}. Find a function f : I $\to \mathbb{R}$ that is a bijection and prove that it is. (Hint: You do not need to use any trigonometric functions. Consider using |x| somewhere in your expression... )
## 7.6 Cardinality
### 7.6.1 Motivation and Definition One important reason for caring about bijections is that they allow us to compare the sizes of sets! This is a notion for which you have some intuitition. For example, it's pretty clear that the set {1, 2, 3, 4, 5} has 5 elements. It is finite. However, the set $\mathbb{N}$ = {1, 2, 3, 4, 5,... } is infinite. We also understand that Z is an infinite set. So are $\mathbb{Q}$ and $\mathbb{R}$. What are their sizes? Can we even compare them? How could we do so mathematically? What does it really mean to be an infinite set? Are there "different infinities"?


> 🇨🇳 **总结** 函数的三个基本性质——单射、满射、双射——是数学分析的核心工具。判定方法、证明模板和反例构造都必须熟练掌握。


