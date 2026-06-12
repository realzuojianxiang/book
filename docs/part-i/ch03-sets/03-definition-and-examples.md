---
title: Definition and Examples
---

# Definition and Examples

Not only does the order of elements not matter within a set, the repetition of elements does not matter! That is, the set A = {a, a, a} and the set A = {a} are exactly the same. Again, remember that a set is completely characterized by its elements; we only care about what is "in" a set. (We will mention this again in Section 3.4.4, when we talk about the "bag analogy" for sets.) Writing A = {a, a, a} is just a triply-redundant way of saying a $\in A$ and that only a is an element of A. Thus, A = {a} is the most concise way of stating the same information. The Common Property Might Be Being an Element of That Set Now, still following the idea that we can define a set by writing all of the elements, consider the following definition of a set A: A = {2, 7, 12, 888} Surely, this is a set because we just defined it by listing its elements. What is the common, well-defined property that associates its elements, though? With the set V of vowels, we could list the elements and provide a linguistic definition, but for this set A, it seems as though we are relegated to listing the elements without knowing a way of describing their common property. Mathematically speaking, though, a common property uniting 2, 7, 12, 888 is that they are all elements of this set A! In the mathematical universe, we have a license for freedom of abstract thought, and merely by discussing this set A and its elements, we have given them that common property. Does this seem satisfactory to you? Can you come up with another common, well-defined property that would yield exactly the elements of A? (Hint: identify a polynomial p(x) whose roots are exactly 2, 7, 12, and 888.) If the elements of a set have more than one property that associates them together, do you think it matters which property we have in mind when referring to the set? And what do you think about the set S := {2, 7, M, Boston Red Sox}? Could there possibly be a common property other than the fact that we have listed them here? Ellipses Are Sometimes Okay, But Informal Sometimes, when there is no confusion about the set in question, or it has been defined in another way and we wish to list a few elements as illustrative examples, then it is convenient to use ellipses to condense the listing of elements of a set. For instance, we might write E = {even natural numbers} = {2, 4, 6, 8, 10,... } This set is infinitely large, in fact, so we could not even list all of its elements if we tried, but it is clear enough from the first few elements listed that we are referring to even numbers, especially because we have already referred to E as "the set of even natural numbers". However, we cannot stress enough that this is not a precise definition of the set in question. It suffices in an informal context, but it is not mathematically rigorous, and this will become clear as we discuss the following proper way of defining sets.


> 🇨🇳 集合中元素的顺序不重要，元素的重复也不重要！即集合 $A = \{a, a, a\}$ 和 $A = \{a\}$ 完全相同。集合完全由其元素刻画，我们只关心集合中"有什么"元素。用省略号列举元素时方便但不精确，真正的精确定义需要使用集合构造记号。


Set-Builder Notation The best way to define or describing a set is to identify its elements as particular objects of another set that have a specific property. For instance, if we wished to refer to the set S of all natural numbers between 1 and 100 (inclusive), we could list all of those elements, but this requires a lot of unnecessary writing. We could also use the ellipsis notation S = {1, 2, 3,..., 100} but, again, this is not precise without already having a formal definition of S. (Someone might misinterpret the ellipses in a different way.) It is much more precise and concise to write S = {x $\in \mathbb{N}$ | 1 $\leq x$ $\leq$100} We read this as "S is the set of all objects x in the set N of natural numbers such that 1 \leq x \leq100". The bar symbol | is read as "such that" and indicates that the information to the left tells us what "larger set" the objects come from, while the information to the right tells us the specific property that those objects should have. (Caution: do not use | in other contexts to mean "such that". This is only acceptable in the context of defining sets. It is just used as a place-holder to separate the left side---the set we use to draw elements---from the right side---a description of the property those elements should have.) This is an example of the very popular and useful set-builder notation. We call it this because we are building a set by drawing elements from a "larger" set of possibilities, and only including those that have a particular property. To do this, we need to tell the reader (1) what the larger set is, and (2) what the common property is. Let's illustrate this idea with a few examples: S = {x $\in \mathbb{N}$ | 1 \leq x $\leq$100} = {1, 2, 3,..., 100} T = {z $\in \mathbb{Z}$ | we can find some k $\in \mathbb{Z}$ such that z = 2k} = {..., -4, -2, 0, 2, 4,...} U =

 x $\in \mathbb{R}$ | x2 -2 = 0


> 🇨🇳 **集合构造记号（Set-Builder Notation）** 定义或描述集合的最佳方式是将其元素标识为另一集合中具有特定性质的对象。竖线符号 $|$ 读作"使得"，左边告诉我们元素来自哪个"更大的集合"，右边告诉我们这些元素应满足的特定性质。例如 $S = \{x \in \mathbb{N} \mid 1 \leq x \leq 100\}$。


o V =

 x $\in \mathbb{N}$ | x2 -2 = 0


> 🇨🇳 $V = \{x \in \mathbb{N} \mid x^2 - 2 = 0\} = \{\}$ （没有自然数满足 $x^2 = 2$）

= { } The last two examples show how the context is extremely important. The same common property (satisfying x2 -2 = 0) can be satisfied by a different set of elements when we change the larger set from which we draw elements. Two real numbers satisfy that property, but no natural numbers satisfy it! Do any rational numbers satisfy that property? What do you think? This is why it is absolutely essential to specify the larger set. A definition like "U =

 x | x2 -2 = 0


> 🇨🇳 最后两个例子表明上下文极其重要。相同的性质（满足 $x^2 - 2 = 0$）在不同的大集合中可能被不同的元素所满足。两个实数满足该性质，但没有自然数满足它！这就是为什么必须指明大集合。像 $U = \{x \mid x^2 - 2 = 0\}$ 这样的定义是含糊且无意义的。

is meaningless because it is ambiguous and could yield completely different interpretations. Reading Notation Aloud We are really learning a new language here, and these are some of the basic words and rules of grammar. We'll need some practice translating these sen-


> 🇨🇳 **朗读记号** 我们实际上在学习一门新语言，需要练习在数学符号和自然语言之间翻译。例如，上面 $S$ 的定义可以读作："$S$ 是所有满足 $1 \leq x \leq 100$ 的自然数 $x$ 的集合"。注意所有读法都指明了大集合和共同性质；区别只是语言学/语法上的，不改变数学含义。


tences into English (in our heads and out loud) and vice-versa. For example, we can say the definition for S above as any of the following, reasonably: S is the set of all natural numbers x such that x is between 1 and 100, inclusive. S is the set of all natural numbers between 1 and 100, inclusive. S is the set of all natural numbers x that satisfy the inequality 1 $\leq x \leq$100. S is the set of natural numbers x with the property that 1 \leq x \leq100. Notice that all of them identified the larger set and the common property; the only differences between them are linguistic/grammatical, and they do not alter the mathematical meanings. Try to write similar sentences for the other definitions. Try getting a verbal definition of a set from a friend and writing down what they said in mathematical symbols. Consider a definition of the rational numbers Q that we saw before, and notice that we can rewrite it as: Q = na b, where a, b $\in \mathbb{Z}$ and b \neq 0 o =

 x $\in \mathbb{R}$ | we can find a, b $\in \mathbb{Z}$ such that a b = x and b \neq 0 o Notice the subtle difference between the two definitions. The upper one tells us that all rational numbers are of the form a b, and then tells us the particular assumptions of a and b that must be satisfied. The lower one tells us that all rational numbers are real numbers with a particular property, namely that we can express that real number as a ratio of integers. We strongly prefer the lower definition, because it tells us more information. In general, if P(x) represents a sentence (involving English and/or mathematical language) that describes a specific, well-defined property, and X is a given set, then the notation S = {x \in X | P(x)} is read as "S is the set of all elements x of the set X such that the property P(x) is true". In the notation P(x), the letter x represents a variable object, and depending on the particular object we use as x, the property P(x) may hold (i.e. P(x) is true) or may fail (i.e. P(x) is false). If the property holds, then we include x in S (so x \in S), and if it fails, we do not include x in S (so x \notin S). Returning to our example of the set E of even natural numbers, it is more precise to write E = {even natural numbers} = {x $\in \mathbb{N}$ | there is a natural number n such that x = 2n}


> 🇨🇳 注意有理数 $\mathbb{Q}$ 的两种定义的微妙区别。上一种说所有有理数都是 \frac{a}{b} 的形式，下一种说所有有理数是可以表示为两个整数之比的实数。我们更推荐下一种，因为它提供了更多信息。一般地，$S = \{x \in X \mid P(x)\}$ 读作"S 是集合 X 中满足性质 P(x) 的所有元素 x 的集合"。对于偶自然数集合 E，更精确的写法是 $E = \{x \in \mathbb{N} \mid \exists n \in \mathbb{N}, x = 2n\}$。


Notice that there are two "layers" of properties here. A natural number is included in our set E if we can find another natural number n with the additional property that x = 2n. Try to write down a similar definition for the set of odd numbers, or the set of perfect squares. What about the set of primes? The set of palindromic numbers? The set of perfect numbers? Can you write definitions for these sets using set-builder notation?
### 3.3.4 The Empty Set What if no elements satisfy a property P(x)? What happens then? For instance, consider the definition S =

 x $\in \mathbb{N}$ | x2 -2 = 0


> 🇨🇳 **3.3.4 空集** 如果没有元素满足性质 $P(x)$ 会怎样？例如考虑 $S = \{x \in \mathbb{N} \mid x^2 - 2 = 0\}$。我们要求的数为 $\sqrt{2}$，但 $\sqrt{2} \notin \mathbb{N}$，因此该集合没有元素。没有元素的集合就是空集 $\emptyset$。


We know that the number x we are "looking for" $with that property is \sqrt 2 (and$ - $\sqrt 2, too) but \sqrt 2 / \in \mathbb{N}$. Thus, no matter what element of N we let x represent, the property P(x)---given by "x2 -2 = 0"---actually fails. Thus, there are no elements of this set. Is this really a set? Remember, a set is completely characterized by its elements, and a set having no elements, such as this one, is characterized by that fact. If we attempted to list its elements, we would end up writing {}. This set is so special, in fact, that we give it a name and symbol:
<div class="def-definition" markdown>
**Definition 3.3.2. The empty set is the set which has no elements.**
</div>
It is denoted by the symbol $\emptyset$. There are many ways to define the empty set using set-builder notation. (And yes, we do mean the empty set; there is only one set with no elements!) We saw one example above, and we're sure you can come up with many others. Consider for example, the following sets: {a $\in \mathbb{N}$ | a < 0} {r $\in \mathbb{R}$ | r2 < 0} {q $\in \mathbb{Q}$ | q2 $\notin \mathbb{Q}$} Do you see why these all define the same set, the one with no elements? Context Matters We should also note again the significance of specifying the larger set X from which we draw our variable element x in a set-builder definition like the one above. For instance, consider the following two sets: S1 = {x $\in \mathbb{N}$ | |x| = 5} = {5} S2 = {x $\in \mathbb{R}$ | |x| = 5} = {-5, 5} (Note: It is also quite common to index sets with the subscript notation you see above, allowing us to use the same letter many times.)


> 🇨🇳 具体的例子：$\{a \in \mathbb{N} \mid a < 0\}$、$\{r \in \mathbb{R} \mid r^2 < 0\}$、$\{q \in \mathbb{Q} \mid q^2 \notin \mathbb{Q}\}$ 都定义了空集。上下文也很重要：$S_1 = \{x \in \mathbb{N} \mid |x| = 5\} = \{5\}$，而 $S_2 = \{x \in \mathbb{R} \mid |x| = 5\} = \{-5, 5\}$——同一个性质在不同大集合中产生完全不同的集合！


This specification is clearly important, in this case, because it yields two entirely different sets! For this reason, we must be precise and clear when defining a set in this way. A definition like S = {x | |x| = 5} should be regarded as ambiguous and undesirable, since it leads to issues like the one above.
### 3.3.5 Russell's Paradox Perhaps it seems like we are picking nits here, but the reasoning behind our vehemence is rooted in some fundamental ideas of set theory. We wish to avoid some complex issues and paradoxes that might arise without this policy in place. There is a particularly famous example of a paradox involving sets that illustraes why we have the requirement described in the above paragraph, namely that we must specify a larger set when we use set-builder notation. This example is known as Russell's Paradox (after the British mathematician Bertrand Russell), and we we will present and discuss it in this section. Sets Whose Elements Are Sets First, we should point out that this discussion will introduce the notion that sets can also be elements of other sets. This may seem like a strange and far-fetchedly abstract idea right now, but it is a fundamental concept in mathematics. For a concrete example, think back to our set B of all Major League Baseball Teams. We could also regard each team as a set, where its elements are the players on the team. Thus, it would make sense to say Derek Jeter $\in \mathbb{N}$ew York Yankees \in B since Derek Jeter is an element of the set New York Yankees, which is itself an element of the set B. (Notice, however, that Derek Jeter \notin B. The relationship signified by "\in" is not transitive. We will hold offon defining this term until much later. For now, we will point out that the relationship signified by "\leq" on the set of real numbers is transitive. If we know x \leq y \leq z, then we can deduce x \leq z. This is not the case with the "\in" relationship, though.) Another example is S = {1, 2, 3, {10}, \emptyset}. Yes, the empty set itself can be an element of another set, as can the set {10}. Why couldn't they? As a thought exercise, we suggest thinking about the difference between \emptyset, {\emptyset}, {{$\emptyset$}}, and so on. Why are they different sets? One final example involves the natural numbers N. Let's use O and E to represent the odd and even natural numbers, respectively. What, then, is the set S = {O, E}, and how does it differ, if at all, from N? This is a subtle question, so think about it carefully. The Paradoxical "Set" Spend some time on the side thinking about this notion of sets whose elements are sets. For now, though, let us forge ahead with our explanation of Russell's Paradox. Consider the following definition of a "set". We say "set" because it


> 🇨🇳 **3.3.5 罗素悖论** 我们坚持要求在集合构造记号中指明更大集合的原因，根植于集合论的一些基本思想。著名的罗素悖论说明了不这样做会引发什么问题。首先，集合可以作为其他集合的元素。例如 $S = \{1, 2, 3, \{10\}, \emptyset\}$。注意 $\emptyset \in S$ 但 $\emptyset \neq \{\emptyset\} \neq \{\{\emptyset\}\}$，它们是不同的集合。


is actually not a properly-defined set, but it remains to be seen exactly why this is the case. When it becomes clear this is not a set, this will be an argument for requiring the specification of a larger set to draw from when we use set-builder notation; this is because the definition below does not specify a larger set. Here is that definition: R = {x | x $\notin x$} That's it! Is this a set? What are the elements of R? Think about what the definition above says: the elements of R are sets that also happen to not have themselves as elements. Can you identify any elements of R? Can you identify any objects that are not elements of R? The first question is far easier to answer: any of the sets we have discussed so far would be elements of R. For instance, the empty set \emptyset contains no elements, so it certainly doesn't have itself as an element. Thus, $\emptyset \in \mathbb{R}$. Also, notice thatN $\notin \mathbb{N}$ (because the set of natural numbers is not a natural number, itself) and thus N $\in \mathbb{R}$. Identifying objects that are not elements of R is a very tricky matter, and we will help you by asking the following question: Is R an element of itself? Is it true or false that R $\in \mathbb{R}$? Think about this carefully before reading on. We will walk you through the appropriate considerations. • Suppose R $\in \mathbb{R}$ is True. The defining property of R tells us that any of its elements is a set that does not have itself as an element. Thus, we can deduce that R $\notin \mathbb{R}$. Wait a minute! Knowing that R $\in \mathbb{R}$ led us to deduce that, in fact, R $\notin \mathbb{R}$. Surely, these contradictory facts cannot both hold simultaneously. Accordingly, it must be that our original assumption was bad, so it must be the case that R $\notin \mathbb{R}$, instead. • Now, suppose R $\notin \mathbb{R}$ is True. The defining property of R tells us that any object that is not an element of R must be an element of itself. (Otherwise, it would have been included as an element of R.) Thus, we can deduce that R $\in \mathbb{R}$. Wait a minute! Knowing that R $\in \mathbb{R}$ led us to deduce that, in fact, R $\notin \mathbb{R}$. This is also contradictory. No matter which option we choose---R $\in \mathbb{R} or \mathbb{R} \notin \mathbb{R}$---we find that the other must also be true, but certainly these contradictory options cannot both be true. Therein lies the paradox. This is not a properly-defined set. If it were, we would find ourselves stuck in the two cases we just saw, and neither of them can be true. It is also not the case that R is simply $\emptyset$; no, it must be that R does not exist as a set.


> 🇨🇳 罗素悖论：设 $R = \{x \mid x \notin x\}$。问：$R \in \mathbb{R}$ 吗？若 $R \in \mathbb{R}$，则由定义 $R \notin \mathbb{R}$，矛盾；若 $R \notin \mathbb{R}$，则由定义 $R$ 应被纳入 $R$，即 $R \in \mathbb{R}$，又矛盾！因此 $R$ 不是一个合法的集合。


The "Set of all Sets" is Not a Set Could we amend the definition of R somehow to produce the "set" that the definition is trying to convey? What "larger set" should we draw our objects x from so that the definition makes sense and properly identifies a set? Look back at the English-language interpretation we wrote after the definition: "the elements of R are sets that also happen to not have themselves as elements." The objects x that we wish to test for the desired property (x $\notin x$) are really all sets. Perhaps, then, we should just define X to be the set of all sets, and use the phrase "x \in X" as part of our definition of R. That would fix it, right? R = {x \in X | x \notin x} Well, no, not at all! The "set of all sets" is, itself, not a set. If it were, this would lead us to exactly the same paradox as before! Nothing would be different, except we would have explicitly stated the "larger set" from which we draw objects x that was previously left implicitly-specified. The main issue is that not specifying a "larger set" from which to draw objects, or implicitly referring to the "set of all sets", results in this type of undesirable paradox. Accordigly, we must not allow such definitions. Any attempt to define a set that draws objects x from the "set of all sets", whether implicitly or explicitly, is not a proper definition of a set. Further Discussion There is nothing inherently wrong with the property P(x) given by "x $\notin x$", though. The issue is with that "larger set" we use. For instance, take the set S =

 x $\in$

1 2, 3 4, 5 x $\notin x$ What are its elements? The only possibilities are those elements drawn from the larger set

1 2, 3 4, 5


> 🇨🇳 **"所有集合的集合"也不是集合** 能否通过指定更大的集合来修正 $R$ 的定义？不可以！"所有集合的集合"本身就不是集合——如果是，同样的悖论仍然会出现。性质 "x \notin x" 本身没有问题，问题在于我们把所有集合作为大集合。例如 $S = \{x \in \{\frac{1}{2}, \frac{3}{4}, 5\} \mid x \notin x\}$ 是合法的集合，因为其元素都不是包含自身的集合。


. Notice that none of those numbers are sets that contain themselves as elements. Thus, this is a proper definition of the set

1 2, 3 4, 5


> 🇨🇳 注意这些数都不是包含自身的集合，所以这是对集合 $\{\frac{1}{2}, \frac{3}{4}, 5\}$ 本身的合法定义。


, itself! With the previous definition for R, the object we were attempting to define was allowed as one of the variable objects x in its own definition, and that is where the issue arose. We hope that we haven't led your thoughts too far astray from the original discussion of examples of sets, but we felt it was important to point out that it is possible to construct ill-defined "collections" that are not sets in the mathematical sense of the word. For the most part, we will not face any such issues with the sets we work with in this book, but to gloss over these issues or simply not mention them at all would be unfair to you, as a student. If you find yourself interested in these issues, seek out an introductory book on set theory. There are other ways that definitions of "sets" can be ill-formed, as well, but the ensuing examples are based on (English) linguistic issues and not any mathematical underpinnings, as in Russell's Paradox. For instance, we could


> 🇨🇳 其他病态定义的例子还有："所有20世纪经典小说的集合"——"经典"不是良好定义的性质；"明天将要出生的人的集合"——时间依赖性使定义永远无法确定。最重要的结论是：在公认的集合论公理下，不存在所有集合的集合。


say "Let N be the set of all classic novels from the 20th century." Being a "classic novel" is not a well-defined property, and cannot be used to identify elements of such a set. The notion of a "classic" is subjective and not rigorously precise. Also, we could say "Let B be the set of people who will be born tomorrow" but this temporal dependence in the definition ensures that we will never actually know what the elements of B are. When tomorrow arrives, the definition will then refer to the next day, and so on. Can you come up with some other examples of ill-formed "collections" of elements? Can you come up with any paradoxes like the one above? In general, the following statement is the most important idea to take away from this discussion of Russel's Paradox: Under the agreed-upon rules of sets (the axioms of set theory), there is no set of all sets.
### 3.3.6 Standard Sets and Their Notation We have referred to and used some common sets of numbers already, so we will list now some sets and their standard symbols: • The natural numbers: N = {1, 2, 3, 4,... } • The first n natural numbers: [n] := {1, 2, 3,..., n -1, n} • The integers: Z = {..., -3, -2, -1, 0, 1, 2, 3,... } • The rational numbers: Q =

 m n | m, n $\in \mathbb{Z}$ and n \neq 0


> 🇨🇳 **3.3.6 标准集合及其记号** 我们已经使用了一些常见的数集，现在列出其标准符号：
> - 自然数：$\mathbb{N} = \{1, 2, 3, 4, \ldots\}$
> - 前 $n$ 个自然数：$[n] := \{1, 2, 3, \ldots, n\}$
> - 整数：$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$
> - 有理数：$\mathbb{Q} = \{\frac{m}{n} \mid m, n \in \mathbb{Z}, n \neq 0\}$


• The real numbers: R • The complex numbers: C We have used N and Z a few times already. The rational numbers Q (we use Q since R was already taken, and rational numbers are quotients) are all of the fractions, or ratios of integers, both positive and negative. The real numbers are harder to describe. Why could we not list a few elements, like we did with N and Z? Why is it that R \neq Q? For now, we essentially take for granted our collective knowledge of these sets of numbers, but think for a minute about that. (We mention the complex numbers C because you might be familiar with them, but we will not have occasion to use them in this book.) How do we know that a set like N exists? Why is it that we think of R as a number line? How many "more" elements are there in Z, as compared to N? How many "more" elements are there in R, as compared to Q? Can we even answer these questions? In the very near future, we will rigorously derive the set N and prove that it exists as the only set with a particular property. This will be essential when we return to our investigation of mathematical induction. (Remember our goals from that chapter?)


> 🇨🇳 - 实数：$\mathbb{R}$
> - 复数：$\mathbb{C}$
>
> 有理数 $\mathbb{Q}$（用 Q 是因为 R 已被占用，且有理数是商 quotients）是整数的分数或比率。实数更难描述——为什么 $\mathbb{R} \neq \mathbb{Q}$？目前我们暂且接受对这些数集的常识，但请思考这些问题。\mathbb{Z} 比 \mathbb{N} 多多少元素？\mathbb{R} 比 \mathbb{Q} 多多少元素？我们甚至能回答这些问题吗？很快我们将严格推导 $\mathbb{N}$ 并证明它作为具有特定性质的唯一集合而存在。


### 3.3.7 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What does the symbol "$\in$" mean? (2) How would you read the statement "x \in S" out loud? (3) Is it possible for a set to be an element of another set? If so, give an example. Is it possible for a set to be an element of itself? (4) How would read the statement "{x $\in \mathbb{N}$ | x \leq5}" out loud? Can you list the elements of this set? (5) What is this set: {z $\in \mathbb{Z}$ | z $\in \mathbb{N}$}? (6) What is this set: {x \in[10] | x $\geq$7}? (7) For each of the following sets, state how many elements they have: (a) \emptyset (b) {1, 2, 10} (c) {1, \emptyset} (d) { \emptyset} (8) Is x \in{ 1, 2, {x} }? Is {x} $\in${ 1, 2, {x} }? (9) Let A = {a, b, c} and B = {b, c, a} and C = {a, a, b, c, a, b}. Are these sets equal or not? (10) Is Z = Q? Why or why not? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Write a definition of the set of natural numbers that are multiples of 4 using set-builder notation. (2) Consider the set S = {3, 4, 5, 6}. Define S in two different ways using setbuilder notation.


> 🇨🇳 **3.3.7 问题与练习** 自我提醒：(1) $\in$ 的含义是什么？(2) 如何朗读 x \in S？(3) 集合可以作为另一个集合的元素吗？给自己举例。(4) 如何朗读 $\{x \in \mathbb{N} \mid x \leq 5\}$？(5) $\{z \in \mathbb{Z} \mid z \in \mathbb{N}\}$ 是什么？(6) $\{x \in [10] \mid x \geq 7\}$ 是什么？(7) 各集合有多少元素？(8) $x \in \{1, 2, \{x\}\}$ 吗？$\{x\} \in \{1, 2, \{x\}\}$ 吗？(9) $A = \{a, b, c\}$ 和 $B = \{b, c, a\}$ 和 $C = \{a, a, b, c, a, b\}$ 相等吗？(10) $\mathbb{Z} = \mathbb{Q}$ 吗？


(3) Give an example of a set X that satisfies N $\in X but \mathbb{Z} \notin X$. (4) Give an example of a set with 100 elements. (5) Give an example of a sets A, B, C such that A $\in B and B \in \mathbb{C} but A \notin \mathbb{C}$. (6) Write a definition of the set of odd integers using set-builder notation. (7) Write a definition of the set of integers that are not natural numbers using set-builder notation. (8) Consider the following sets: A =

 x $\in \mathbb{R}$ | x2 -3x + 2 $\geq$0


> 🇨🇳 (3)-(7) 练习题。


B = {y $\in \mathbb{R}$ | y $\leq$1 or y $\geq$2} Explain why A = B. (9) Consider the following sets: C =

 x $\in \mathbb{R}$ | x2 -4 $\geq$0


> 🇨🇳 (8) 解释为什么 $A = B$。


D = {y $\in \mathbb{R}$ | y $\geq$2} Is C = D? Why or why not? Write your explanation with good mathematical notation, using $\in and \notin$. (10) Try explaining Russell's Paradox to a friend, even one who does not study mathematics. What do they understand about it? Do they object? Do their ideas make sense? Have a discussion!
## 3.4 Subsets
### 3.4.1 Definition and Examples
Let's discuss a topic whose basic idea we have already been using. Specifically, let's investigate the notion of subsets.
<div class="def-definition" markdown>
**Definition 3.4.1. Given two sets A and B, if every element of A is also an**
</div>
element of B, then we say A is a subset of B. The mathematical symbol for subset is $\subseteq$, so we would write A \subseteq B. If we want to indicate that A is a subset of B but is also not equal to B, we would write A \subset B and say that A is a proper subset of B. We can also write these relationships as B \supseteq A, or B $\supset A$, respectively. In these cases, we would say B is a superset of A or B is a proper superset of A, respectively.


> 🇨🇳 **3.4 子集** **3.4.1 定义与例子** 如果集合 $A$ 的每个元素也是 $B$ 的元素，则说 $A$ 是 $B$ 的子集。记作 $A \subseteq B$。若 $A \subseteq B$ 且 $A \neq B$，则说 $A$ 是 $B$ 的真子集，记作 $A \subset B$。同样可以写成 $B \supseteq A$（$B$ 是 $A$ 的超集）或 $B \supset A$（$B$ 是 $A$ 的真超集）。
