---
title: Logical Negation of Quantified Statements
tags:
  - 逻辑
  - 命题
  - 量词
  - 证明写作
---

# Logical Negation of Quantified Statements

are referring to, we can necessarily conclude that the proposition R(x) is true. Now, how could this statement be False, and how could we prove that? If it's False that every element $x \in S$ satisfies a certain property, it must be that at least one element does not satisfy that property. To prove this, we would be expected to produce such a value; we would have to define (i.e. identify) an element x and explain why R(x) does not hold for that particular element. (Think about how we understand this negation linguistically. We do this all the time in everyday language without even thinking about it.) The conclusion, then, is that the negation of the original statement is $\exists$x \in S such that R(x) is False We now introduce the notational symbol \neg to mean$ "logical negation" or "not"$. With this in hand we can rewrite the negated statement \neg$ {$\forall x$\in S$. R(x) } as $\exists x$\in S. \negR(x) The concluding phrase of that statement, \negR(x), could be simplified, depending on what R(x) is. For instance, if S = \mathbb{R} and R(x) is$ "x2 $\geq 0$", then the negated statement would read " $\exists x \in \mathbb{R}$ such that x2 < 0 " since "x2 < 0" is logically equivalent to "$\neg (x2 $\geq 0$)$". In general, though, we must leave it as "\negR(x)" without knowing anything further about the proposition R. We will also point out that, in general, the phrases "R(x) is False" and "$\negR(x) is True$" are logically equivalent; they both assert that the proposition R(x) is not true. This notion we are developing right now is what is meant by a counterexample, a term you have likely heard before. To disprove a universally quantified statement, we must prove an existentially quantified statement; that proof involves explicitly defining an element of a set that does not satisfy the specified property, whence the word counterexample.
### 4.4.2 Negation of an existential quantification A statement like $\exists x \in S. R(x) makes an existence claim. It says that there must be some element x that satisfies the property R(x). To disprove a claim like this, we would seek to show that any value of x actually fails to satisfy the property R. Accordingly, we can say that the statement \neg$ {$\exists x$\in S$. R(x) }


> 🇨🇳 即逻辑上等价于语句 orall x \in S.$ 
eg R(x)$。这从直觉上是合理的：要反驳一个存在性主张，你需要证明无论取哪个值，该性质都不成立。假想你正在与朋友辩论：朋友告诉你某个 kwyjibo 具有 zooqa 的性质。你会怎么说？"才不是呢！给我看任何一个 kwyjibo，我知道它不可能是一个 zooqa，因为以下原因……" 当你说"给我看任何一个"时，你实际上执行了一次全称量化！你在说无论考虑哪个 kwyjibo，某事都成立——即 orall $x \in$ K（K 是所有 kwyjibo 的集合），某事为真。请思考并理解为什么我们发现的逻辑否定是有道理的。


is logically equivalent to the statement $\forall x \in S. \negR(x) This makes sense if we think about how to disprove such an existential claim. Pretend you are having a debate with a friend who told you that some kwyjibo has the property that it is a zooqa. How would you disprove him/her$? You might say something like, "Nuh uh! Show me any kwyjibo you want to. I know it can't possibly be a zooqa because of the following reasons... " and then you would explain why the property fails, no matter what. Now, when you say "show me any" you are really performing a universal quantification! You are saying that no matter which kwyjibo you consider, something is true; that is, for every kwyjibo, or $\forall$x \in$ K (where K is the set of all kwyjibos), something is True. Think about this and consider why the logical negations we have discovered/defined make sense to you. Later on in the chapter, when we consider proof techniques, we will explain the strategy of considering an arbitrary kwyjibo and why this actually proves the logical negation we just wrote above. For now, we hope it is clear that $\forall$x \in S. \negR(x) and \exists x \in S$. R(x) have opposite truth values.
### 4.4.3 Negation of general quantified statements The observations we have made so far motivate a general procedure for negating quantified statements. The statement A we defined above is of the form $\exists y \in \mathbb{R}$. C(y) where C(y) is the rest of the statement (which depends on the value of y, of course). We think of C(y) as some property of the quantified variable y; that property might have other quantifiers and variables inside it, but at a fundamental level, it is merely asserting some truth about y. To negate this statement, we follow the method discussed above and write $\forall y \in \mathbb{R}. \negC(y) Now, we know that C(y) is a universally quantified statement itself$: $\forall x$\in \mathbb{R}. y = x3 We know how to negate that type of statement, too! That negation, \negC(y), is \exists x \in \mathbb{R}$. $y \neq$ x3


> 🇨🇳 这一步使用了我们上面看到的另一个否定方法。然后将所有部分组合起来，我们可以说 $
eg A$ 是语句 orall y \in \mathbb{R}. \exists x \in \mathbb{R}. y$ 
eq x^3$。这个命题可以被证明为真，从而说明原始语句必定为假。（我们将此证明留作练习。提示：给定任何 y \in \mathbb{R} ，定义一个 x 的值使得 $y 
eq x^3$ 为真。注意你对 x 的选择将依赖于 $y$ 的值。）观察否定是如何产生的：我们认识到原始语句是一系列嵌套量词（Nested Quantifiers），末尾是一个变元命题，然后将否定从外层量词"传递"到内层量词。


$This step just uses the other negation procedure that we saw above. Then, putting it all together, we can say that \negA is the statement \forall y \in \mathbb{R}. \exists x \in \mathbb{R}$. $y \neq$ x3 This claim we can prove to be true, thus showing that the original statement must be False. (We leave this proof as an exercise. Hint: Given any $y \in \mathbb{R}$, define a value of x that will force $y \neq$ x3 to be true. Notice that your choice of x will depend the value of y; how does it?) Look at how this negation came about: we recognized that the original statement was a sequence of nested quantifiers (i.e. a sequence of several quantified variables in a row) with a variable proposition at the end, and we saw that we could treat part of the sequence of quantifiers as its own statement. We then "passed the negation" from the outside quantifier to the inside one, and pieced those negations together. Following this same idea, we can figure out how to identify a statement with a longer sequence of quantifiers. For instance, look at a statement like $\forall$a \in$ A. $\exists$b \in$ B. $\exists$c \in \mathbb{C}$. $\forall d$, $e \in$ D. Q(a, b, c, d, e) To start negating it, we would break offthe first quantification, and treat the rest as its own proposition, R(a), that depends only on a: $\forall$a \in$ A. {$\exists$b \in$ B. $\exists$c \in \mathbb{C}$. $\forall d$, $e \in$ D. Q(a, b, c, d, e) | {z } R(a) } The negation can therefore be written as $\exists$a \in A. \negR(a) but we would then have to figure out another way to write \negR(a). But hey, we would just do the same thing! We would just separate$ "$\exists$b \in$ B" from the rest and... you see where this is going. Try working out the steps on your own, and make sure that you end up with the following as the logical negation of the original statement: $\exists$a \in$ A. $\forall$b \in$ B. $\forall$c \in \mathbb{C}$. $\exists d$, $e \in D. \negQ(a, b, c, d, e) In general, we can say this$: To negate a statement composed only of quantifiers and variable propositions, just switch every " $\forall$" to " $\exists$", and vice-versa, and negate the propositions. Don't alter any of the sets over which we quantify, merely the quantifiers themselves and the ensuing propositions; it wouldn't make sense to change the universe of discourse. Later on, we will look at how to negate other types of statements, more complicated ones built from other connectives. Before we do that, we need to move on and define and discuss those other connectives.


> 🇨🇳 **一般法则**：要否定一个仅由量词和变元命题组成的语句，只需将每个 $orall$ 换为 $\exists$，将每个 $\exists$ 换为 $orall$，并否定末尾的命题。不要修改量化的集合，只修改量词本身及随后的命题——改变论域（Universe of Discourse）是没有意义的。


### 4.4.4 Method Summary Let's summarize what we have discovered in this section. • Negating a universal quantification: $Let X be a set and let P(x) be a proposition. Then the negation of a universal quantification, like this, \neg$ {$\forall x$\in X$. P(x) } is written as $\exists$x \in X. \negP(x) In words, we have shown that saying It is not the case that, for every x \in X$, P(x) holds. is equivalent to saying There exists an element $x \in$ X such that P(x) fails. • Negating an existential quantification: $Let X be a set and let Q(x) be a proposition. Then the negation of an existential quantification, like this, \neg$ {$\exists$x \in X$. Q(x) } is written as $\forall$x \in X. \negQ(x) In words, we have shown that saying It is not the case that there exists an x \in X$ such that Q(x) holds. is equivalent to saying For every element $x \in X$, Q(x) fails. Don't Change the Quantification Set! We mentioned above that it wouldn't make sense to change the universe of discourse when negating a statement. To think about why this makes sense, take a real-life example. Suppose we said "Every book on this bookshelf is written in English." How would you prove to us that we are lying, that our statement is actually False? You would have to produce a book on this shelf that is written in a different language. You couldn't bring in a French novel from the room down the hall and say, "See, you were wrong!" That wouldn't prove anything about the claim we made; the realms of discourse are different, and we didn't make any claim


> 🇨🇳 原始主张只对集合 T 中的元素做了断言，因此它的否定也一样。你不能从别的房间拿来一本法语小说说"看，你说错了！"那不能证明关于我们书架的主张有任何问题——论域不同。同理，当我们否定 $orall b \in T. P(b)$ 时，得到 \exists b \in T.$ 
eg P(b)$，而不改变论域 T。


about what's going on in any bookshelves in other rooms. We only asserted something about this particular shelf. For the same reason, when negate a statement like $\forall b \in T$. P(b) we obtain $\exists b \in T. \negP(b) without changing that realm of discourse, the set T. The original claim only asserts something about elements of T, so its negation does only that, as well.$
### 4.4.5 The Law of the Excluded Middle You know what? Let's actually discuss why we can talk about a statement and its logical negation. Built into our definition of mathematical/logical statement is the idea that such a sentence must have exactly one truth value, either True or False. Why can we do this? Well, we're in charge of the definitions here! Mathematicians have to set the ground rules---the axioms---of their systems and we want our logical system to ensure that every claim we make is decidedly True or False, and not both, and not neither. This dichotomy is truly an axiom of our system. It is widely adopted in most of mathematics, and is famously known as The Law of the Excluded Middle. The name comes from this very idea, that every claim is True or False, so there is no middle ground between those two sides; that middle is excluded. In essence, this makes what we do in mathematics fruitful: every claim has a truth value, and our goal is to find that truth value. Sometimes, though, we have to fall back on this axiom, this law we agreed upon, and just guarantee that some claim is either True or False, without knowing which truth value actually applies. We present an interesting and striking example of this idea here.
Proposition 4.4.1. There exist real numbers a and b that are both irrational
such that ab is rational. (Remember that a rational number is one that can be expressed as a fraction of integers, and an irrational number is a real number that is not rational. Can you think of some examples of both rational and irrational numbers?)
<div class="def-proof" markdown>
*Proof.* We know
</div>
$\sqrt 2 is irrational. (Question$: Why? Can you prove that? $Try it now. We will prove this very soon, as well!) The number \sqrt$


> 🇨🇳 排中律的运用：$\sqrt{2}^{\sqrt{2}}$ 要么是有理数要么是无理数。（这就是排中律的用法。）让我们分别考虑两种情况。


$\sqrt 2 is either rational or irrational. (This is where the Excluded Middle is used.) Let's consider these two cases separately.$ • $Suppose that the number \sqrt$


> 🇨🇳 假设 $\sqrt{2}^{\sqrt{2}}$ 确实是有理数。那么取 $a = \sqrt{2}$ 和 $b = \sqrt{2}$ 就是我们所需的例子，因为 a 和 b 都是无理数，而 $a^b$ 是有理数。


$\sqrt 2 is, indeed, rational. Then a = \sqrt 2 and b = \sqrt 2 is the example we seek, because a and b are both irrational and ab is rational.$


> 🇨🇳 现在假设 $\sqrt{2}^{\sqrt{2}}$ 是无理数。在这种情况下，我们可以取 $a = \sqrt{2}^{\sqrt{2}}$ 和 $b = \sqrt{2}$ 作为所求的例子，


• $Now, suppose that the number \sqrt$


> 🇨🇳 因为 $a$ 和 $b$ 都是无理数，而 $a^b = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}} = (\sqrt{2})^2 = 2$，这是有理数。


$\sqrt 2 is irrational. In this case, we can use a = \sqrt$


> 🇨🇳 在两种情况下，我们都找到了实数 $a, b \in \mathbb{R}$ 使得 $a$ 和 $b$ 都是无理数但 $a^b$ 是有理数。这就是一个非构造性证明（Non-constructive Proof）的例子。它告诉我们某种东西存在（甚至缩小到了两种可能性），却没有确切告诉我们哪一种就是我们一直在寻找的那种。正是排中律（Law of the Excluded Middle）的直接使用导致了这种结果。大多数证明将是构造性的（但不全是）。


$\sqrt 2 and b = \sqrt 2 as the example we seek, because a and b are both irrational and ab = ( \sqrt$


> 🇨🇳 构造性证明在主观上更好，因为如果我们声称某物存在，我们应该能够展示它。有时，构造性证明并不立刻清晰，我们必须做一个非构造性证明，就像我们在这里所做的那样。


$\sqrt 2 \cdot \sqrt 2 = ( \sqrt 2)2 = 2 which is rational. In either case, we have found an example of real numbers a, b \in \mathbb{R}$ such that both a and b are irrational and yet ab is rational. This proves the claim. This is an example of a non-constructive proof. It tells us something exists (and narrows it down to two possibilities, even) without actually telling us exactly which possibility is the one we sought all long. It is a direct use of the Law of the Excluded Middle that causes this. (Question: $Can you prove somehow that \sqrt$


> 🇨🇳 回顾第3.6.2节中定义的索引集运算——并和交。主要的想法是：一个对象是否属于索引并集，取决于它是否是至少一个组成集合的元素——这正是一个存在量化。一个对象是否属于索引交集，取决于它是否是所有组成集合的元素——这正是一个全称量化。有了这些观察，我们可以用新的量词记号重写索引集运算的定义。


$\sqrt 2 is irrational$? It is True, but there is no known "simple" proof of this fact. Maybe you can find one!) Most of the proofs we do here will be of the constructive variety (but not all). These might be more satisfying to you, and we're inclined to agree. If we claim something exists, we should be able to show it to you, right? If we just talked for a while about why some such object exists somewhere else, without being able to point to it, you would have to believe us, but you might not feel great about it. Constructive proofs are subjectively better because of this, and we will always strive for one when we can. Sometimes, though, a constructive proof is not immediately clear, and we have to make a non-constructive one, like we did here.
### 4.4.6 Looking Back: Indexed Set Operations and Quantifiers Look back at Section 3.6.2, where we defined set operations---union and intersection, in Definitions 3.6.3 and 3.6.4, respectively---performed over index sets. The main idea was that we could express the union/intersection of an entire class of sets all at once using a shorthand notation. Look carefully at those definitions. What characterized whether an object actually is an element of an indexed union, for example? That object needed to be an element of at least one of the constituent sets of the union. That is, there needed to exist some set of which that obejct is an element. This sounds like an existential quantification, doesn't it? Likewise, what characterized whether an object is an element of an indexed intersection? That object needed to be an element of all the constituent sets. That is, for all of those sets, that object must be an element thereof. This is a universal quantification. With those observations now made, we can rewrite those definitions of indexed set operations using our new quantifier notation:


> 🇨🇳 回到第3.6.2节的例子和练习重新尝试。现在这些定义是否更好理解了？通过量词，我们看到索引并集本质上是存在量化的集合版本，索引交集本质上是全称量化的集合版本。


<div class="def-definition" markdown>
**Definition 4.4.2. Suppose I is an index set and $\forall i \in I. Ai \subseteq U$, for some**
</div>
universal set U. Then [ i$\in I Ai = {x \in U$ | $\exists k \in I. x \in Ak} \ i\in I$ Ai = {$x \in U$ | $\forall i \in I. x \in A$i} Try working with some of the examples and exercises in that Section 3.6.2 again. Do the definitions make more sense now?
### 4.4.7 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What is the negation of a mathematical statement? How are a statement and its negation related? (2) Why is the negation of $a \forall claim an \exists o$ne? Why is the negation of an $\exists claim a \forall o$ne? (3) What is a non-constructive proof? To what type of claim---$\exists or \forall$---does this term apply? (4) Consider the claim $\forall x \in S$. P(x) Why is its negation neither of the following? $\forall x \notin S. P(x) \exists x \notin S. \negP(x) Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though$; making sure you can work through them will help you! (1) For each of the following statements, write its negation. Which one---the original or the negation---is True?


> 🇨🇳 (a) $orall a \in A. \exists b \in B. Q(a, b)$ 的否定是 \exists a \in A. orall b \in B.$ 
eg Q(a, b)$ (b) orall a \in A.$ 
eg P(a)$ 的否定是 \exists a \in A. P(a) (c) orall c \in \mathbb{C}. orall d \in D.$ 
eg Q(c, d)$ 的否定是 \exists c \in \mathbb{C}. \exists d \in D. Q(c, d) (d) \exists a_1, a_2 \in A. orall d \in D. R(a_1, a_2, d) 的否定是 orall a_1, a_2 \in A. \exists d \in D.$ 
eg R(a_1, a_2, d)$ (e) orall b_1, b_2, b_3 \in B.$ 
eg R(b_1, b_2, b_3)$ 的否定是 \exists b_1, b_2, b_3 \in B. R(b_1, b_2, b_3) (f) \exists b \in B. orall c \in \mathbb{C}. orall d \in D. R(d, b, c) 的否定是 orall b \in B. \exists c \in \mathbb{C}. \exists d \in D.$ 
eg R(d, b, c)$


(a) $\forall x \in \mathbb{R}. \exists n \in \mathbb{N}$. n > x (b) $\exists n \in \mathbb{N}. \forall x \in \mathbb{R}$. n > x (c) $\forall x \in \mathbb{R}. \exists y \in \mathbb{R}$. y = x3 (d) $\exists y \in \mathbb{R}. \forall x \in \mathbb{R}$. y = x3 (2) For each of the following statements, write its negation. Which one---the original or the negation---is True? (a) $\exists S \in P(N). \forall x \in \mathbb{N}. x \in S (b) \forall S \in P(N). \exists x \in \mathbb{N}. x \in S (c) \forall x \in \mathbb{N}. \exists S \in P(N). x \in S (d) \exists x \in \mathbb{N}. \forall S \in P(N). x \in S (3)$ Let I = {$x \in \mathbb{R}$ | 0 < x < 1}. For each of the following defined sets, write out the defining condition that determines whether a number $y \in \mathbb{R}$ is an element of the set, using quantifiers. Then, determine what the set is, and write your answer using set-builder notation. (Try to prove your claim, as well, using a double-containment argument!) (a) S = [ x$\in I$ {$y \in \mathbb{R}$ | x < y < 2} (b) T = \ x$\in I$ {$y \in \mathbb{R}$ | -x < y < x} (c) V = [ x$\in I$ {$y \in \mathbb{R}$ | -3x < y < 4x} (4) Let P = {$y \in \mathbb{R}$ | y > 0}. Consider this statement: $\forall$ε $\in P$. $\exists$δ $\in P$. $\forall x$ \in{$y \in \mathbb{R}$ | -δ < y < δ}. |x3| < ε Write out the logical negation of this statement. What does this statement say? What does its negation say? Which one is True? Can you prove it? (5) Let A, B, C, D be arbitrary sets. Let P(x), Q(x, y), R(x, y, z) be arbitrary variable propositions. Write the negation of each of the following statements.


> 🇨🇳 请思考排中律为何如此重要：它保证每个陈述要么为真要么为假，没有中间地带。这使我们能够通过证明否命题为假来间接证明原命题为真——即反证法（Proof by Contradiction）的基础。


(a) $\forall a \in A. \exists b \in B. Q(a, b) (b) \forall a \in A. \negP(a) (c) \forall c \in \mathbb{C}. \forall d \in D. \negQ(c, d) (d) \exists a1, a2 \in A. \forall d \in D$. R(a1, a2, d) (e) $\forall b1, b2, b3 \in B. \negR(b1, b2, b3) (f) \exists b \in B. \forall c \in \mathbb{C}. \forall d \in D$. R(d, b, c)
## 4.5 Logical Connectives To build mathematical statements from simpler ones (meaning ones composed of just quantifiers and propositions) we can connect several statements with certain words and phrases---such as "and", "or", and "implies"---to create more complicated statements and assert further claims and truths. We call these words and phrases logical connectives, and each of them has their own corresponding mathematical symbol and meaning. These meanings will make sense to you, based on our intuitive grasp of the English language and rational thought, but we emphasize that one of the major goals of introducing mathematical logic and its corresponding notation is to build these intuitions into rigorous and unambiguous concepts. Throughout this section, let us assume that P and Q are arbitrary mathematical statements. These statements themselves can be composed of complicated combinations of quantifiers and other connectives and all sorts of mathematical notions. The point is that the way we combine P and Q into a larger statement is independent of their individual compositions. Before, we saw that "$\neg( \forall x \in X$. R(x))" is equivalent to "$\exists x \in X. \negR(x)$"$, regardless of what the statement R(x) was and how complicated it might have been. This idea continues here. We can talk about how to combine two statements without knowing what they are, individually. We should also point out that these constituent statements, P and Q, may actually be variable propositions. For instance, we will consider how to connect two variable propositions, P(x) and Q(x), that each depend on some variable x. The definitions and methods we develop in this section apply to these variable propositions even though these propositions, themselves, do not have truth values without being told what the value of the variable x is. When we want to talk about those propositions meaningfully and mathematically, we will have to quantify the variable x. Thus, if we have variable propositions P(x) and Q(x), we can still meaningfully define P(x)\wedgeQ(x) (where \wedgemeans$ "and" as you'll see in the next section). We could then, in an example or a problem, talk about a claim of the form $\exists x \in X. P(x) \wedgeQ(x) This is a mathematical statement. Essentially, the point we want to make is that these connectives still apply to variable propositions, but the relevant variables will have to be quantified$


> 🇨🇳 **练习**：(1) 对下列每个语句写出其否定，哪个为真？(2) 对下列每个语句写出其否定，哪个为真？(3) 设 $I = {x \in \mathbb{R}$ | 0 < x < 1}，写出每个定义集合的判定条件。(4) 设 $P = {y \in \mathbb{R}$ | y > 0}，写出语句的逻辑否定。(5) 设 A, B, C, D 为任意集合，P(x), Q(x,y), R(x,y,z) 为任意变元命题，写出每个语句的否定。


