---
title: Logical Equivalence
---

# Logical Equivalence

### 4.6.1 Definition and Uses
The following definition introduces a convenient symbol for the notion of logical equivalence described in the above paragraph:
<div class="def-definition" markdown>
**Definition 4.6.1. Let P and Q be mathematical statements. We use the symbol**
</div>
"$\Leftrightarrow$" to mean "is logically equivalent to", or "has the same truth value as". That is, we write "$P \Leftrightarrow \mathbb{Q}$" when P and Q always have the same truth value, regardless of whether it is T or F. We read "$P \Leftrightarrow \mathbb{Q}$" aloud as "P is logically equivalent to Q" or "P if and only if Q". This type of statement is known as a biconditional (or a bi-implication). Let's take the truth tables we saw in the last section and add a new column for this symbol: $P \mathbb{Q} \negP \negP \veeQ P = \Rightarrow \mathbb{Q} \mathbb{Q} =\Rightarrow P P \Leftrightarrow \mathbb{Q} T T F T T T T T F F F F T F F T T T T F F F F T T T T T In the column for P \Leftrightarrow Q, an entry has the truth value T when (and only when) P and \mathbb{Q} have the same truth value. This happens in Row 1, where both are T, and in Row 4, where both are F. Notice, then, that P \Leftrightarrow \mathbb{Q}$ has the truth value T if and only if (P =$\Rightarrow Q) \wedge(Q = \Rightarrow P$) is a True statement. This is the notion of logical equivalence: $P \Leftrightarrow \mathbb{Q}$ means that both P =$\Rightarrow \mathbb{Q} and \mathbb{Q} =\Rightarrow P$ hold. Whatever truth value P has, Q is guaranteed to have the same truth value, and vice-versa: • Supposing that P is True, then P =$\Rightarrow \mathbb{Q}$ tells us that Q must also be True. • Supposing that P is False, then Q =$\Rightarrow P$ tells us that Q cannot be True (since Q =$\Rightarrow P$ would be False, in that case), so Q must also be False. Either way, P and Q have the same truth value.
Examples
Example 4.6.2. Look again at the third and fourth columns in the truth table
above. They prove the following logical equivalence: (P =$\Rightarrow Q) \Leftrightarrow (\negP \veeQ) Whatever the truth value of P = \Rightarrow \mathbb{Q} (which, of course, depends on P and Q), it must be the same as the truth value of \negP \veeQ. We've mentioned this equivalence before, and we will make use of it fairly often in the future.$


> 🇨🇳 逻辑等价（Logical Equivalence）两个命题 $P$ 和 $Q$ 逻辑等价，记作 $P \Leftrightarrow \mathbb{Q}$，意味着它们对所有可能的赋值具有相同的真值。本节讨论如何用真值表和逻辑规则来判定等价性。


Example 4.6.3. Look at this truth table:
$P \mathbb{Q} \negP \negQ P = \Rightarrow \mathbb{Q} \negQ = \Rightarrow \negP T T F F T T T F F T F F F T T F T T F F T T T T Regardless of the truth values of P and Q, we find that P = \Rightarrow \mathbb{Q} and \negQ = \Rightarrow \negP have the same truth values. Thus, they are logically equivalent, and we can write$: (P =$\Rightarrow Q) \Leftrightarrow (\negQ = \Rightarrow \negP) This is the fact that we stated (without proof) in the previous section$: The contrapositive of a conditional statement is logically equivalent to the original statement. A different proof of this fact makes use of the way to express a conditional statement as a disjunction. Recall the logical equivalence {P =$\Rightarrow \mathbb{Q}$ } $\Leftrightarrow$ {$\negP \veeQ$ } that we mentioned in the previous example. Now, think about the contrapositive of that original conditional statement: $\negQ = \Rightarrow \negP Applying the same disjunctive form to that statement yields the following equivalence$: {$\negQ = \Rightarrow \negP$ } $\Leftrightarrow$ {$\neg(\negQ) \vee\negP$ } $Now, noticing that \neg(\negQ) is equivalent to just Q, and remembering that the order of a disjunction is irrelevant (i.e. P \veeQ and \mathbb{Q} \veeP have the same truth value) we find that$ {$\negQ = \Rightarrow \negP$ } $\Leftrightarrow$ {$\negP \veeQ$ } $\Leftrightarrow$ {P =$\Rightarrow \mathbb{Q}$ } This shows, in another way, that a conditional statement and its contrapositive have the same truth value!
Example 4.6.4. Later in this section, we will prove the following logical equiva-
lences, which hold no matter what the propositions P and Q and R are: $\neg(P \wedgeQ) \Leftrightarrow \negP \vee\negQ (P \wedgeQ) \wedgeR \Leftrightarrow P \wedge(Q \wedgeR) P \vee(Q \wedgeR) \Leftrightarrow (P \veeQ) \wedge(P \veeR) \neg(P = \Rightarrow Q) \Leftrightarrow P \wedge\negQ Each of these is an assertion that the expressions on both sides of the \Leftrightarrow$ symbol have the same truth value. Can you see why these claims are True? Can you think of how to prove them?


> 🇨🇳 **用真值表验证等价** 要证 $P \Leftrightarrow \mathbb{Q}$，构造包含 $P$ 和 $Q$ 的真值表，验证两列完全相同。这是最直接但有时最繁琐的方法。


If and Only If Logical equivalence has a nice relationship with the phrase "if and only if". To say "P if and only if Q" means we are asserting that both "P if Q" and "P only if Q" hold. One of these corresponds to P =$\Rightarrow \mathbb{Q}$ and the other corresponds to Q =$\Rightarrow P$, so asserting both are true means exactly what we have described: $P \Leftrightarrow \mathbb{Q}$ is the same as saying (P =$\Rightarrow Q) \wedge(Q = \Rightarrow P$) Now, which one is which, though? When we say "P if Q", this means "If Q, then P." That is, "P if Q" is the same as saying Q =$\Rightarrow P$ Sussing out the other direction is a little harder! What does "P only if Q" really mean? This sentence is asserting that, in a situation where P holds, it must also be the case that Q holds. That is, knowing P holds means we also immediately know Q holds. Put even another way, whenever P is true, we necessarily know that Q is true. This is the same as saying P =$\Rightarrow \mathbb{Q}$ holds! Another way of thinking about it is as follows. Saying "P only if Q" $is the same as saying it cannot be the case that P holds and \mathbb{Q} does not. Written logically, we have \neg$ {$P \wedge\negQ$ } Later on in this section, we will state and prove DeMorgan's Laws for Logic. One of those laws tells us how to negate that statement inside the parentheses. (You might already know these logical laws, in fact. If not, you can glance ahead at Sections 4.6.5 and 4.6.6 for a preview.) The conclusion is: $\negP \veeQ Hey look, that's logically equivalent to P = \Rightarrow \mathbb{Q}$, as we observed already! Cool. Just further confirmation that "P only if Q" means P =$\Rightarrow \mathbb{Q}$. Using "$\Leftrightarrow$" in Definitions We will also often use the "$\Leftrightarrow$" symbol in a definition to indicate that the term defined is an equivalent term for the property that is used in the definition. For example: We say $x \in \mathbb{Z} is even \Leftrightarrow \exists k \in \mathbb{Z}$. x = 2k That is, the notion of an integer being even is equivalent to knowing that the number is twice an integer. Similarly, we can define odd: We say $x \in \mathbb{Z} is odd \Leftrightarrow \exists k \in \mathbb{Z}$. x = 2k + 1 These are formal definitions, mind you, and are the only way of guaranteeing an integer is even (or odd). We will use these definitions soon to rigorously prove some facts about integers and arithmetic. Every time we want to assert a particular integer (call it x) is even, we need to show there exists an integer k that satisfies x = 2k. That is, we have to satisfy the definition by appealing to the logical equivalence given in the definition.


> 🇨🇳 **例** 验证 $\neg(P \wedge Q) \Leftrightarrow (\neg P \vee \neg Q)$（德摩根律之一）：

| $P$ | $Q$ | $P \wedge \mathbb{Q}$ | $\neg(P \wedge Q)$ | $\neg P$ | $\neg \mathbb{Q}$ | $\neg P \vee \neg \mathbb{Q}$ |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

两侧完全相同，故等价。


Biconditional Statements: A Technical Distinction We can also use the symbol "$\Leftrightarrow$" to express two conditional statements at once. Technically speaking, this is not exactly the same as asserting a logical equivalence, but it conveys a similar idea, so we allow the symbol to be used in both ways. A logical equivalence involves some undefined propositions, and it asserts that the two statements will have the same truth value, regardless of the truth values of those propositions. For instance, (P =$\Rightarrow Q) \Leftrightarrow (\negP \veeQ) is a perfect example of a logical equivalence. Without telling you what P and \mathbb{Q} are, we can't be sure exactly what P = \Rightarrow \mathbb{Q} and \negP \veeQ mean. However, we don't need to know what P and \mathbb{Q} are to know that those two statements definitely have the same truth value. The situation is slightly different when the two statements on either side of the$ "$\Leftrightarrow$" are actually proper mathematical statements, with no undefined propositions. For instance, consider this statement: $\forall x \in \mathbb{R}. (x > 0) \Leftrightarrow ( 1 x > 0 )$ This is a logical claim, and it asserts that, whenever x is a real number, knowing one of those two facts---x > 0 or 1 x > 0---necessarily guarantees the other. That is, if I told you I have a real number in mind and it is positive, you get to conclude that its reciprocal is positive, too. Also, if I told you I have a real number in mind whose reciprocal is positive, you would get to conclude that the number itself is positive, too. It goes both ways. (Question: What if I told you I had a negative real number in mind? Could you conclude anything about its reciprocal? Why or why not?) Do you see how this is different? Given an arbitrary $x \in \mathbb{R}$, the statement "x > 0" is decidedly either True or False. Its truth value isn't left undetermined. This distinguishes it from the example given above, where the truth value of the individual statements is unknown, yet we can still declare those truth values must be identical. For lack of a better, widespread term for these kinds of statements, we will refer to them as biconditionals. This is because they are really meant to represent two conditional statements that go "in opposite directions": $\forall$x \in \mathbb{R}$. [ ( (x > 0) =$\Rightarrow ( 1 x > 0 )$ ) $\wedge ( ( 1 x > 0 )$ =$\Rightarrow (x > 0)$ ) ] This is what the statement above says: each part of the statement implies the other one. This term is not necessarily standard in other mathematical writing, but we wanted to point out this technical distinction so you are aware of it. You might approach a mathematicial logician or set theorist and use the phrase "logical


> 🇨🇳 **重要等价律**

**德摩根律（De Morgan's Laws）：**
- $\neg(P \wedge Q) \Leftrightarrow \neg P \vee \neg \mathbb{Q}$
- $\neg(P \vee Q) \Leftrightarrow \neg P \wedge \neg \mathbb{Q}$

**条件语句等价：** $P \Rightarrow \mathbb{Q} \Leftrightarrow \neg P \vee \mathbb{Q} \Leftrightarrow \neg \mathbb{Q} \Rightarrow \neg P$


equivalence", and they might be confused or take offense to the way in which you use it. This is not a big worry, mind you! Since we are learning about these fundamental ideas now for the first time, we don't necessarily have to keep in mind all of the technical details that lie underneath these concepts. Also, in the remainder of this book, we might use "logical equivalence" and "biconditional" interchangeably. This is fine and acceptable for now. The main point behind using the "$\Leftrightarrow$" symbol is to assert that two statements have the same truth value. The only difference between a "logical equivalence" and a "biconditional" is whether or not those statements contained therein have any arbitrary, undefined propositions. This is a minor distinction to be made, in the grand scheme of things, so we will consider it only briefly here.
### 4.6.2 Necessary and Sufficient Conditions There are two terms occasionally used in mathematics that convey the two directions of a biconditional statement: necessary and sufficient. They correspond exactly to the "only if" and "if" parts of the biconditional. These terms are motivated by the natural types of questions mathematicians ask. Sufficient: P, if Q If we identify some interesting fact or property---call it P---of a mathematical object, we might wonder, "When can we guarantee such a property holds? Is there some condition we can check that will give us a 'Yes' answer right away?" This is what a sufficient condition is, a property that guarantees P will also hold. It is "sufficient" in the sense that it is "enough" to conclude P; we don't need any other outside information. Let's say we have identified a proposition Q as a sufficent condition for P. How can we express this logically? Well, knowing Q is sufficient to conclude P, so we can easily write this as a conditional statement: Q =$\Rightarrow P$ means Q is a sufficient condition for P Said another way, this conditional statement expresses: "P, if Q". Necessary: P only if Q We also might wonder, "How can we guarantee that P fails? Is there some condition we can check that will tell us this right away?" This is what a necessary condition is, a property that is necessary or essential for the property P to hold. This condition is not necessarily enough to conclude that P holds, but for P to even have a chance of holding, this condition better hold, too. Think about the logical connections here. Say we have established a property Q that is a necessary condition for P. How can we express the relationship between P and Q, symbolically? That's right, we can use a conditional statement. Knowing P holds tells us that Q definitely holds; it was necessary for P


> 🇨🇳 **分配律（Distributive Laws）：**
- $P \wedge (Q \vee R) \Leftrightarrow (P \wedge Q) \vee (P \wedge R)$
- $P \vee (Q \wedge R) \Leftrightarrow (P \vee Q) \wedge (P \vee R)$


to be true. This is expressed as P =$\Rightarrow \mathbb{Q}$ means Q is a necessary condition for P Said another way, this conditional statement expresses: "P only if Q"$. We could also think of this in terms of the contrapositive. If \mathbb{Q} does not hold, then P cannot hold, either. That is, \negQ = \Rightarrow \negP which is the contrapositive of the conditional statement above, P = \Rightarrow \mathbb{Q}$. We know these are logically equivalent forms of the same statement.
Examples
Example 4.6.5. Let P(x) the proposition "x is an integer that is divisible by 6".
For each of the following conditions, let's identify whether it is a necessary or sufficient condition (or possibly both!) for P(x) to hold. (1) Let Q(x) be "x is an integer that is divisible by 3". To determine whether Q(x) is a necessary condition, let's assume P(x) holds. Can we deduce Q(x) holds, too? Well, yes! To say an integer x is divisible by 6 means that it is divisible by both 2 and 3. Thus, it is certainly divisible by 3, so Q(x) holds. To determine whether Q(x) is a sufficient condition, let's assume Q(x) holds. Can we deduce P(x) holds, too? Hmm... knowing that x is an integer divisible by 3, is it also definitely divisible by 2, allowing us to conclude it is divisible by 6? We think not! Consider x = 3; notice Q(3) holds but P(3) does not. This shows Q(x) is only a necessary condition, and not a sufficient one. (2) Let R(x) be "x is an integer that is divisible by 12." Following similar reasoning to the above example, we can conclude that R(x) is a sufficient condition for P(x), but not a necessary one (because we can have x = 6, where P(6) holds but R(6) does not hold). (3) Let S(x) be "x is an integer such that x2 is divisible by 6". We'll let you work with this one on your own... Is S(x) a necessary condition for P(x)? Is it a sufficient one? Be careful, and notice that we specified x, itself, is an integer...
### 4.6.3 Proving Logical Equivalences: Associative Laws Now, let's actually prove some logical equivalences! In doing so, we will be working on our ability to read and understand and write logical statements using quantifiers and connectives. We will also be developing some fundamental


> 🇨🇳 **结合律（Associative Laws）：**
- $(P \wedge Q) \wedge \mathbb{R} \Leftrightarrow P \wedge (Q \wedge R)$
- $(P \vee Q) \vee \mathbb{R} \Leftrightarrow P \vee (Q \vee R)$

**交换律（Commutative Laws）：**
- $P \wedge \mathbb{Q} \Leftrightarrow \mathbb{Q} \wedge P$
- $P \vee \mathbb{Q} \Leftrightarrow \mathbb{Q} \vee P$


logical results that we can apply in the near future to develop proof techniques. These techniques will be the foundation of the rest of our work, and everything else we do will involve implementing some combination of these proof strategies and logical concepts. Let's start with some of the simpler symbolic logical laws. Showing something is associative essentially means we can "move around the parentheses" willy-nilly and end up with the same thing. You probably use the fact that addition is associative all the time! To add x to y +z, we can just add z to x+y instead and know we get the same answer. That is, we can rest assured that x + (y + z) = (x + y) + z We can move the parentheses around wherever we want to and so, ultimately, we can just pretend as if they aren't even there and just write x + y + z because the order in which we interpret the two additions is irrelevant. The same kind of result applies to conjuctions and disjunctions of logical statements, and that's what we will prove now.
<div class="def-theorem" markdown>
**Theorem 4.6.6. Let P, Q, R be logical statements. Then**
</div>
$P \wedge(Q \wedgeR) \Leftrightarrow (P \wedgeQ) \wedgeR and P \vee(Q \veeR) \Leftrightarrow (P \veeQ) \veeR We will actually prove these claims in two separate ways$: (1) via truth tables, and (2) via semantics (i.e. words). They are both perfectly valid, but we want to show you both of them to let you decide which style you like better. Proof 1. First, we will prove these claims via truth tables. Observe the table for conjunctions: $P \mathbb{Q} \mathbb{R} P \wedgeQ \mathbb{Q} \wedgeR P \wedge(Q \wedgeR) (P \wedgeQ) \wedgeR T T T T T T T T T F T F F F T F T F F F F T F F F F F F F T T F T F F F T F F F F F F F T F F F F F F F F F F F Thus, P \wedge(Q \wedgeR) \Leftrightarrow (P \wedgeQ) \wedgeR because their corresponding columns are identical, in every case.$


> 🇨🇳 **双重否定律（Double Negation）：** $\neg(\neg P) \Leftrightarrow P$

**幂等律（Idempotent Laws）：**
- $P \wedge P \Leftrightarrow P$
- $P \vee P \Leftrightarrow P$

**恒真律与恒假律：**
- $P \vee \neg P \Leftrightarrow \text{True}$（排中律）
- $P \wedge \neg P \Leftrightarrow \text{False}$（矛盾律）


Next, observe the table for disjunctions: $P \mathbb{Q} \mathbb{R} P \veeQ \mathbb{Q} \veeR P \vee(Q \veeR) (P \veeQ) \veeR T T T T T T T T T F T T T T T F T T T T T T F F T F T T F T T T T T T F T F T T T T F F T F T T T F F F F F F F Thus, P \vee(Q \veeR) \Leftrightarrow (P \veeQ) \veeR because their corresponding columns are identical, in every case. Proof 2. Second, let's prove these claims by analyzing them, semantically. Consider the first claim, P \wedge(Q \wedgeR) \Leftrightarrow (P \wedgeQ) \wedgeR To show that the two sides are logically equivalent, we need to show both of the following conditional statements are True$: $P \wedge(Q \wedgeR) = \Rightarrow (P \wedgeQ) \wedgeR and (P \wedgeQ) \wedgeR = \Rightarrow P \wedge(Q \wedgeR) ( = \Rightarrow ) Let's prove the first conditional statement. Suppose P \wedge(Q\wedgeR) is True. This means P is True and \mathbb{Q} \wedgeR is True. By definition, this means P is True and \mathbb{Q} is True and \mathbb{R} is True. Certainly, then P \wedgeQ is True and \mathbb{R} is True, by definition. Thus, (P \wedgeQ) \wedgeR is True, as well. (\Leftarrow=) Now, let's prove the second conditional statement. Suppose (P \wedgeQ)\wedgeR is True. This means P \wedgeQ is True and \mathbb{R} is True. By definition, this means P is True and \mathbb{Q} is True and \mathbb{R} is True. Certainly, then P is True and \mathbb{Q} \wedgeR is True, by definition. Thus, P \wedge(Q \wedgeR) is True, as well. Since we have shown both conditional statements, we conclude the two sides are, indeed, logically equivalent. Next, consider the second claim of the theorem, P \vee(Q \veeR) \Leftrightarrow (P \veeQ) \veeR To show that the two sides are logically equivalent, we need to show both of the following conditional statements are True$: $P \vee(Q \veeR) = \Rightarrow (P \veeQ) \veeR and (P \veeQ) \veeR = \Rightarrow P \vee(Q \veeR) ( = \Rightarrow ) Let's prove the first conditional statement. Suppose P \vee(Q\veeR) is True. This means either P is True or \mathbb{Q} \veeR is True. This gives us two cases.$


> 🇨🇳 **利用等价律化简** 等价律允许我们将复杂命题逐步化简。这比真值表更高效，尤其当变量很多时。


$1. Suppose P is True. This means P \veeQ is True, by definition. Thus, (P \veeQ) \veeR is True, also by definition. 2. Suppose \mathbb{Q} \veeR is True. This means either \mathbb{Q} is True or \mathbb{R} is True. Again, this gives us two cases. (a) Suppose \mathbb{Q} is True. This means P \veeQ is True, by definition. Thus, (P \veeQ) \veeR is True, also by definition. (b) Suppose \mathbb{R} is True. This means (P \veeQ) \veeR is True, by definition. In any case, we find that (P \veeQ) \veeR is True. Thus, this conditional statement is True. (\Leftarrow=) Let's prove the second conditional statement. Suppose (P \veeQ) \veeR is True. This means either P \veeQ is True or \mathbb{R} is True. This gives us two cases. 1. Suppose P \veeQ is True. This means either P is True or \mathbb{Q} is True. This gives us two cases. (a) Suppose P is True. This means P \vee(Q \veeR) is true, by definition. (b) Suppose \mathbb{Q} is True. This means \mathbb{Q} \veeR is True, by definition. Thus, P \vee(Q \veeR) is true, also by definition. 2. Suppose \mathbb{R} is True. This means \mathbb{Q} \veeR is True, by definition. Thus, P \vee (Q \veeR) is True, also by definition. In any case, we conclude that P \vee(Q \veeR) is True. Thus, this conditional statement is True. Since we have shown both conditional statements hold, we conclude the two sides are, indeed, logically equivalent. Okay, what have we accomplished with these proofs$? What have we proven, and how? Why did it work? Let's mention a consequence of these proofs, before going on to discuss and compare the proffs, themselves. We proved that the "$\wedge$" and "$\vee$" connectives are associative, so the order in which we evaluate parenthetical statements involving only one such connective does not matter. For example, we now know that "$P \wedge(Q \wedgeR)$" has the same meaning as "$(P \wedgeQ) \wedgeR$". Accordingly, in the future, we will just write these statements without the parentheses: "$P \wedgeQ\wedgeR$". Reflecting: Truth Tables vs. Semantics Let's talk about the truth tables first. Since P, Q, and R are logical statements, they are each, individually, True or False. The eight rows of the truth tables consider all possible assignments of truth values to those three constituent statements. The first three columns tell us whether P, Q, R are True or False. The next two columns correspond to the more complicated constituent parts of the logical statements in the claim, and the last two columns correspond to the two parts of the actual claim in the theorem. By comparing those last two columns,


> 🇨🇳 **例** 化简 $\neg((P \wedge Q) \vee (\neg P \wedge Q))$：

$= \neg(P \wedge Q) \wedge \neg(\neg P \wedge Q)$（德摩根律）
$= (\neg P \vee \neg Q) \wedge (P \vee \neg Q)$（德摩根律）
$= ((\neg P \vee P) \vee \neg Q)$（分配律方向）
$= \text{True} \wedge \neg \mathbb{Q}$（排中律）
$= \neg \mathbb{Q}$

结果：$\neg \mathbb{Q}$


we can decide whether or not those two statements are logically equivalent. (Remember that "logically equivalent" means "has the same truth value as, no matter the assignment of truth values to P and Q and R". Thus, observing that the two columns have identicals entries, row by row, is sufficient to show that the two statements are logically equivalent.) Next, let's talk about the semantic proofs. How do you feel about them? They were certainly longer, right? Disregarding that, though, did they feel like good proofs? Were they clear? Correct, even? Reread the proofs above and think about these questions. We will emphasize that they are fully correct proofs. The use of cases is essential when trying to prove a disjunction (an "or" statement) holds. When we suppose something is True and deduce that something else is True, that's how we prove a conditional statement is True. We will further analyze these techniques very soon, but we hope that giving you a first example like this will help you later on. For the remainder of this section, we will use a truth table to verify simple claims like these. The proofs are much shorter that way! We are sure that you can go through the details of a semantic proof, like the ones we gave above, if you need further convincing or extra practice with interpreting symbolic logical claims as English sentences.
### 4.6.4 Proving Logical Equivalences: Distributive Laws In arithmetic, you've used the fact that multiplication distributes across addition. That is, we know that $\forall x, y, z \in \mathbb{R}. x \cdot (y + z)$ = $x \cdot$ y + $x \cdot$ z Hey, look, we wrote this in symbolic notation! Do you see why it says what you already know about the distributive property? Here we will state and prove two similar laws. They will tell us that the logical connectives "$\wedge$" and "$\vee$" also distribute across each other.
<div class="def-theorem" markdown>
**Theorem 4.6.7. Let P, Q, and R be logical statements. Then**
</div>
$P \wedge(Q \veeR) \Leftrightarrow (P \wedgeQ) \vee(P \wedgeR) and P \vee(Q \wedgeR) \Leftrightarrow (P \veeQ) \wedge(P \veeR)$
<div class="def-proof" markdown>
*Proof.* We will use truth tables to verify these two claims. Observe, for the first
</div>


> 🇨🇳 **用等价律证明逆否等价** 我们可以用等价律逐步变形来证明 $P \Rightarrow \mathbb{Q} \Leftrightarrow \neg \mathbb{Q} \Rightarrow \neg P$：

$P \Rightarrow \mathbb{Q} \Leftrightarrow \neg P \vee \mathbb{Q}$（条件等价）
$\Leftrightarrow \mathbb{Q} \vee \neg P$（交换律）
$\Leftrightarrow \neg(\neg Q) \vee \neg P$（双重否定）
$\Leftrightarrow \neg \mathbb{Q} \Rightarrow \neg P$（条件等价）


$claim, that P \mathbb{Q} \mathbb{R} \mathbb{Q} \veeR P \wedgeQ P \wedgeR P \wedge(Q \veeR) (P \wedgeQ) \vee(P \wedgeR) T T T T T T T T T T F T T F T T T F T T F T T T T F F F F F F F F T T T F F F F F T F T F F F F F F T T F F F F F F F F F F F F Notice that the last two columns are identical, thus proving the desired logical equivalence. Observe, for the second claim, that P \mathbb{Q} \mathbb{R} \mathbb{Q} \wedgeR P \veeQ P \veeR P \vee(Q \wedgeR) (P \veeQ) \wedge(P \veeR) T T T T T T T T T T F F T T T T T F T F T T T T T F F F T T T T F T T T T T T T F T F F T F F F F F T F F T F F F F F F F F F F Again, notice that the last two columns are identical, thus proving the desired logical equivalence.$
### 4.6.5 Proving Logical Equivalences: De Morgan's Laws (Logic) Let's prove some logical equivalences involving negations. The following two laws are named for the British mathematician Augustus De Morgan. He is credited with establishing these logical laws, as well as introducing the term mathematical induction! We are grateful and indebted to his work in mathematics. De Morgan's Laws for Logic state some logical equivalences about negating conjunctions and disjunctions.
<div class="def-theorem" markdown>
**Theorem 4.6.8. Let P and Q be logical statements. Then**
</div>
$\neg$ {$P \wedgeQ$ } $\Leftrightarrow \negP \vee\negQ and \neg$ {$P \veeQ) \Leftrightarrow \negP \wedge\negQ$


> 🇨🇳 **条件语句的否定** 我们来推导 $\neg(P \Rightarrow Q)$ 的等价形式：

$\neg(P \Rightarrow Q) \Leftrightarrow \neg(\neg P \vee Q)$（条件等价）
$\Leftrightarrow P \wedge \neg \mathbb{Q}$（德摩根律 + 双重否定）

即：否定条件语句得到"假设成立但结论不成立"。


<div class="def-proof" markdown>
*Proof.* We prove the first claim by a truth table:
</div>
$P \negP \mathbb{Q} \negQ P \wedgeQ \neg(P \wedgeQ) \negP \vee\negQ T F T F T F F T F F T F T T F T T F F T T F T F T F T T And then we prove the second claim by a truth table$: $P \negP \mathbb{Q} \negQ P \veeQ \neg(P \veeQ) \negP \wedge\negQ T F T F T F F T F F T T F F F T T F T F F F T F T F T T These two laws are extremely useful! In fact, we can use them to prove similar statements about sets.$
### 4.6.6 Using Logical Equivalences: DeMorgan's Laws (Sets) The following statements "look a lot like" the statements in DeMorgan's Laws for Logic we saw above. We will see exactly why they look so similar when we see the proof!
<div class="def-theorem" markdown>
**Theorem 4.6.9. Let A and B be any sets, and suppose that A, $B \subseteq U$, so the**
</div>
complement operation is defined in the context of U. Then, $A \cap B = A \cup B and A \cup B = A \cap B$ We will prove these claims using logical equivalences and DeMorgan's Laws for Logic. Our method will be to show that, in either case, the property of being an element of the set on the left-hand side of the equation is logically equivalent to being an element of the set on the right-hand side. This proves both parts of a double-containment argument in one fell swoop.
<div class="def-proof" markdown>
*Proof.* Let's prove the first set equality. Let $x \in U$ be arbitrary and fixed. Then,
</div>
$x \in A \cup B \Leftrightarrow x \notin A \cup B$
Definition of complement
$\Leftrightarrow \neg (x \in A \cup B$)
Definition of $\notin$
$\Leftrightarrow \neg [(x \in A) \vee(x \in B$)]
Definition of $\cup$ and $\vee$
$\Leftrightarrow \neg(x \in A) \wedge\neg(x \in B) DeMorgan's Law for Logic \Leftrightarrow(x \notin A) \wedge(x / \in B$)
Definition of $\notin$
$\Leftrightarrow(x \in A) \wedge(x \in B$)
Definition of complement
$\Leftrightarrow x \in A \cap B$
$Definition of \wedgeand \cap$


> 🇨🇳 **双条件语句的否定** $\neg(P \Leftrightarrow Q)$：

$\Leftrightarrow \neg((P \Rightarrow Q) \wedge (Q \Rightarrow P))$
$\Leftrightarrow \neg(P \Rightarrow Q) \vee \neg(Q \Rightarrow P)$（德摩根律）
$\Leftrightarrow (P \wedge \neg Q) \vee (Q \wedge \neg P)$

即"恰好一个成立，另一个不成立"——这正是"异或"（XOR）的定义。


Remember that" $\wedge$" is a logical operation, while "$\cap$" is a set operation. We had to be careful about which one made sense in every sentence we wrote. Also, notice that we used DeMorgan's Law for Logic in the middle of the proof, to convert a negation of a disjunction into the conjunction of two negations. This chain of logical equivalences shows that $x \in A$ \cup B \Leftrightarrow x \in A \cap B$ so, in the context of U, the property of being an element of $A \cup$ B is logically equivalent to the property of being an element of $A \cap$ B. Therefore, $A \cup$ B = $A \cap$ B Let's prove the second equality now, with a similar method. Let $x \in$ U be arbitrary and fixed. Then, $x \in A$ \cap B \Leftrightarrow x \notin A \cap B$
Definition of complement
$\Leftrightarrow \neg (x \in A \cap B$)
Definition of $\notin$
$\Leftrightarrow \neg [(x \in A) \wedge(x \in B$)]
Definition of $\cap$ and $\wedge$
$\Leftrightarrow \neg(x \in A) \vee\neg(x \in B) DeMorgan's Law for Logic \Leftrightarrow(x \notin A) \vee(x / \in B$)
Definition of $\notin$
$\Leftrightarrow(x \in A) \vee(x \in B$)
Definition of complement
$\Leftrightarrow x \in A \cup B$
$Definition of \veeand \cup$
This chain of logical equivalences shows that $x \in A \cap B \Leftrightarrow x \in A \cup B$ so, in the context of U, the property of being an element of $A \cap$ B is logically equivalent to the property of being an element of $A \cup$ B. Therefore, $A \cap$ B = $A \cup$ B Voil`a! We have proven both equalities stated in the theorem. Notice the striking similarities between the two proofs. They used exactly the same method, and the only real difference is flipping a "$\cap$" to a "$\cup$", and viceversa. Because we proved something about how to do this already (DeMorgan's Laws for Logic), we can cite that result and make this proof short and sweet. Wouldn't you agree this is far easier and more concise than writing out a full double-containment proof for these two claims? (Try it!)
### 4.6.7 Proving Set Containments via Conditional Statements Whenever you can, go ahead and use the method we used in the previous section, with DeMorgan's Laws for Logic and Sets; that is, feel free to prove set


> 🇨🇳 **量词与联结词的交互** 量词和联结词之间也有重要等价：

- $\neg(\forall x.\, P(x)) \Leftrightarrow \exists x.\, \neg P(x)$
- $\neg(\exists x.\, P(x)) \Leftrightarrow \forall x.\, \neg P(x)$

这是前几节讨论过的量词否定规则，用等价的语言重述。


relationships via conditional statements and logical equivalences. In general, when you're proving an equality, you need to be sure that all of your claims really are "$\Leftrightarrow$" claims. In the previous section, we only applied definitions and a theorem about logical equivalences, so we were positive about all of the directions of the "$\Leftrightarrow$" arrows in the proof. Whenever you write a proof like this, read over it again once you're done and ask yourself at every line, "Does this actually work? Does the implication work both ways here?" Let's see another example of this technique in action. It will be slightly more complicated, in that we have to define some variable propositions because the claim given is not fundamentally identical to DeMorgan's Laws for Logic. We will, though, invoke a logical law that we just proved, and use it to establish a sets law.
Proposition 4.6.10. Let A, B, C be any sets, with A, B, $C \subseteq U$, where U is a
universal set. Then, $A \cap (B -C)$ = ($A \cap B$) -C Much like the previous example, DeMorgan's Laws for Sets, we will establish a logical equivalence between being an element of the left-hand side and being an element of the right-hand side. (Again, this is like proving both sides of a double-containment proof all at once.) To do this, we will just establish some variable propositions that refer to the properties of being an element of A, B, and C, respectively. From there, the result will follow from a logical law.
<div class="def-proof" markdown>
*Proof.* Let A, B, C be any sets, with A, B, $C \subseteq U$, where U is a universal set.
</div>
We define the following variable propositions: Let P(x) be "$x \in A$" Let Q(x) be "$x \in$ B" Let R(x) be "$x \in \mathbb{C}$" Let $x \in$ U be arbitrary and fixed. With these definitions, we can write the following chain of logical equivalences (where "Defn" is just space-saving shorthand for "Definition"): $x \in A$ \cap (B -$C)$ \Leftrightarrow x \in A \wedge(x \in B$ -C) Defn of $\cap \Leftrightarrow x \in A \wedge(x \in B \wedgex / \in \mathbb{C}$) Defn of - $\Leftrightarrow P(x) \wedge(Q(x) \wedge\negR(x)) Defn of P(x), Q(x), R(x), / \in \Leftrightarrow (P(x) \wedgeQ(x)) \wedge\negR(x) Associative Law for \wedge \Leftrightarrow(x \in A \wedgex \in B) \wedgex / \in \mathbb{C} Defn of P(x), Q(x), R(x) \Leftrightarrow x \in A \cap B \wedgex / \in \mathbb{C} Defn of \cap \Leftrightarrow x \in(A \cap B$) -C Defn of - This shows that $x \in A \cap (B -$C)$ \Leftrightarrow x \in(A \cap B$) -C


> 🇨🇳 **练习** (1) 用真值表验证 $P \Rightarrow \mathbb{Q} \Leftrightarrow \neg P \vee \mathbb{Q}$。(2) 用等价律化简 $\neg(P \vee (Q \wedge \neg P))$。


holds True for any element x in the universe U. Therefore, $A \cap (B -C)$ = ($A \cap B$) -C Think about why we needed to make sure all of these claims are truly if and only if statements. We are ensuring that any element x that is an element of a set on one side of the equality is also necessarily an element of the set on the other side; but, furthermore, we are ensuring that any element x that is not an element of one set is also not an element of the other set. The biconditional statements "go both ways", so we prove both the "is an element of" and "is not an element of" parts of the claim all at once. To illustrate our previous warnings, consider the following claim as an example of a proof where one "direction" $of a \Leftrightarrow c$laim fails.
Proposition 4.6.11. Let X, Y, Z be any sets, with X, Y, $Z \subseteq U$, for some
universal set U. Then, the following containment holds: ($X \cup Y$ ) -$Z \subseteq X$\cup (Y -Z)$ You might recognize this claim as Problem 3.11.17! In that problem, we asked you to prove this claim using a containment argument, taking an arbitrary $x \in$ U and supposing it is an element of the left-hand side set, then deducing it must also be an element of the right-hand side set. We will do (essentially) the same thing here, but the argument will be recast in logical terms and symbols. We will do this to (1) give us more practice with making these types of arguments, but also (2) to recognize precisely where in the argument the "reverse" direction fails. Remember that, in Problem 3.11.17, we also asked you to find an example that shows that the $\supseteq d$irection is not necessarily True. This means that the logical argument working in that direction would break down somewhere. We will see precisely where that is, and we can use it to help us come up with that required counterexample.
<div class="def-proof" markdown>
*Proof.* Let X, Y, Z be any sets, with X, Y, $Z \subseteq U$, for some universal set U.
</div>
Let $x \in U$ be arbitrary and fixed. We can write the following chain of logical equivalences: $x \in ($X \cup$ Y )$ -$Z \Leftrightarrow x \in X \cup Y \wedgex / \in \mathbb{Z}$ Defn of - $\Leftrightarrow(x \in X \veex \in Y ) \wedgex / \in \mathbb{Z} Defn of \cup \Leftrightarrow(x \in X \wedgex / \in \mathbb{Z}) \vee(x \in Y \wedgex / \in \mathbb{Z}$) Distr. Law Scratch work:


> 🇨🇳 (3) 证明 $(P \Rightarrow Q) \wedge (Q \Rightarrow P) \Leftrightarrow P \Leftrightarrow \mathbb{Q}$。(4) 写出 $\neg(P \Leftrightarrow Q)$ 的最简等价形式。


From here, what further logical equivalences could we assert? We could simplify the right-hand side and express it as $x \in X$ -$Z \veex$\in X$ -Z and, therefore, $x \in (X -Z)$\cup (Y -Z)$ This is not what the claim was, but this procedure so far would be a valid proof of a different claim, namely that ($X \cup$ Y ) -Z = (X -Z) $\cup (Y -Z)$ However, our right-hand side is $X \cup (Y -Z)$ but we are not trying to prove an equality, merely a containment. Thus, the goal of the rest of our proof is to prove this conditional claim: { ($x \in X \wedgex / \in \mathbb{Z}) \vee(x \in Y \wedgex / \in \mathbb{Z}$) } =$\Rightarrow x \in X \cup (Y -Z)$ To help us figure out how to get there, let's do some scratch work here to rewrite the statement on the right-hand side; then, we can see how to get there from where we are already: $x \in X$ \cup (Y -$Z)$ \Leftrightarrow x \in X \veex \in Y$ -Z Defn of $\cup \Leftrightarrow x \in X \vee(x \in Y \wedgex / \in \mathbb{Z}$) Defn of - This is similar to the last logical equivalence we derived up above, but this one differs in the term on the left. Can you see how the one up above implies this one? Think about it, and then read on for the rest of our proof, resumed. Now, we want to show that { ($x \in X \wedgex / \in \mathbb{Z}) \vee(x \in Y \wedgex / \in \mathbb{Z}$) } =$\Rightarrow x$\in X \cup (Y -Z)$ To do this, let's suppose the expression on the left-hand side is True. This means either $x \in X \wedgex / \in \mathbb{Z} or x \in Y \wedgex / \in \mathbb{Z} (or possibly both)$. Thus, we have two cases:


> 🇨🇳 (5) 用等价律证明 $\neg(\neg P \vee Q) \Leftrightarrow P \wedge \neg \mathbb{Q}$。(6) 解释为什么 $P \Rightarrow \mathbb{Q}$ 与 $Q \Rightarrow P$ 不等价，并给出一个具体例子。


1. Suppose the first expression is True, so that $x \in X \wedgex / \in \mathbb{Z}$. This certainly means that $x \in$ X, and thus $x \in X \veex \in Y$ -Z holds. 2. Suppose the second expression is True, so that $x \in Y \wedgex / \in \mathbb{Z}$. This means that $x \in$ Y -Z, and thus $x \in X \veex \in Y$ -Z holds. In either case, we find that $x \in X \veex \in Y$ -Z holds, and therefore, $x \in X$ \cup (Y -Z)$ holds, in either case, by the definition of $\cup$. Overall, this shows that $x \in ($X \cup$ Y )$ -Z =$\Rightarrow x \in X \cup (Y -Z)$ holds for every element $x \in$ U. Therefore, by the definition of $\subseteq$, we have ($X \cup$ Y ) -$Z \subseteq X$ \cup (Y -Z)$ Recognizing where we are, and where we wanted to go, helped us finish this proof. We had no hope of completing it using logical equivalences alone because, in fact, the sets given in the claim are not always equal! Looking back at the proof, can we identify the step whose logical equivalence was invalid, and can we use it to help construct a counterexample to the (False) claim that those sets are always equal? We had reached as far as this valid statement ($x \in X \wedgex / \in \mathbb{Z}) \vee(x \in Y \wedgex / \in \mathbb{Z}$) and we used it to deduce this statement $x \in X \vee(x \in Y \wedgex / \in \mathbb{Z}$) It seems clear, from our argument in the proof, that the first statement does imply the second one; that is, if we suppose the first statement holds, we can figure out that the second statement one holds, as well. The only difference between them is in the first term, and knowing two parts of an "$\wedge$" statement hold certainly lets us conclude a particular one of them holds. This deduction does not work in the other direction. Suppose that second statement holds. If it's the right term that is valid---that $x \in Y \wedgex / \in \mathbb{Z}$--- then this also makes the first statement hold. However, since we have an "$\vee$" statement, we have to consider the case where the left term is the one that holds. In that case, knowing only $x \in$ X does not let us deduce that $x \in X \wedgex / \in \mathbb{Z}$ holds. Supposing an "$\wedge$" holds lets us deduce either one of its parts holds, but just knowing only one part cannot tell us that both hold! We can use this to construct a counterexample. We see that we just need to ensure that there is some particular element $x \in U$ that satisfies the left term


> 🇨🇳 (7) 化简 $\neg((P \wedge Q) \Rightarrow R)$。(8) 证明分配律 $P \wedge (Q \vee R) \Leftrightarrow (P \wedge Q) \vee (P \wedge R)$。


in the second statement, namely $x \in X$, but does not satisfy the left term in the first statement, namely $x \in X \wedgex / \in \mathbb{Z}$. Said another way, we just need to ensure that there is an element $x \in X$ \cap \mathbb{Z}$. The following example accomplishes exactly that.
Example 4.6.12. We claim that
($X \cup Y$ ) -$Z \subseteq X$\cup (Y -Z)$ holds for any sets X, Y, Z, but equaltiy need not hold. See the proof of Proposition 4.6.11 to see why the containment claimed above does hold. Now, consider the following example. Let's define X = {1} Y = {2} Z = {1, 2} Notice that ($X \cup$ Y ) -Z = ({1} $\cup${2}) -{1, 2} = {1, 2} -{1, 2} = $\emptyset$ and $X \cup (Y -Z)$ = {1} $\cup ({2} -{1, 2})$ = {1} $\cup${$\emptyset$} = {1} Since $\emptyset \subset${1} (a proper) subset, we conclude that ($X \cup$ Y ) -$Z \neq$X \cup (Y -Z)$ in this case. This shows that equality need not hold in the claim above. This strategy now lets us go back and complete many proofs involving sets in a more efficient and rigorous manner! Rather than fumbling through the linguistics of "ands" and "ors", we can use our logical notation and laws that we have proven. Many of the exercises in this section deal with sets, specifically because of this. If you need to flip back to Chapter 3 and remind yourself of any relevant definitions, go right ahead!
### 4.6.8 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What are the Associative Laws for Logic? (2) What are the Distributive Laws for Logic?


> 🇨🇳 (9) 化简 $\neg(P \Leftrightarrow Q)$。(10) 什么条件下 $P \Rightarrow \mathbb{Q}$ 与 $Q \Rightarrow P$ 同时为真？这说明了什么？


(3) What are DeMorgan's Laws for Logic? What are DeMorgan's Laws for Sets? How are they related? (4) What is the difference between a necessary and a sufficient condition? (5) What happens when a condition is both necessary and sufficient? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) We used Truth Tables to prove DeMorgan's Laws for Logic. Can you come up with a semantic proof? Can you explain DeMorgan's Laws to a nonmathematician friend and convince them they are valid? (2) Let P(x) be the variable proposition "x is an integer that is divisible by 10". Come up with two necessary conditions and two sufficient conditions for this statement. (3) Let A, B, C be any sets, where A, B, $C \subseteq U$, for some universal set U. Use logical equivalences and logical laws to prove the following claims. (a) $A \cap ($B \cup \mathbb{C}$)$ = ($A \cap$ B) $\cup ($A \cap \mathbb{C}) (b) (A \cup B$)$\cap A$ = B -A (c) $A \cup$ B = $A \cap$ B (d) (A -B) $\cap \mathbb{C}$ = A -($B \cup \mathbb{C}$) (4) Use conditional statements and logical equivalences to prove that the containment A -($B \cup \mathbb{C}) \subseteq A \cap$ {$B \cap \mathbb{C}$ } holds for any sets A, B, C. Then, find an example that shows that equality need not hold. (Hint: In general, a helpful idea in constructing a strict set containment is to see if you can make one side the empty set.) (5) Let D, E, F be any sets. Consider the sets D -(E -F) and (D -E) -F


> 🇨🇳 **补充等价律**

**吸收律（Absorption Laws）：**
- $P \wedge (P \vee Q) \Leftrightarrow P$
- $P \vee (P \wedge Q) \Leftrightarrow P$

**蕴含律：** $P \Rightarrow \mathbb{Q} \Leftrightarrow \neg \mathbb{Q} \Rightarrow \neg P$

**逆否等价的推论：** 条件语句的否定 $\neg(P \Rightarrow Q) \Leftrightarrow P \wedge \neg \mathbb{Q}$ 是证明中反证法的理论基础。


How do they compare? Are they always equal? Is one always a subset of the other, or vice-versa? Clearly state your claims, then either prove them or provide relevant counterexamples.
## $4.7 Negation of Any Mathematical Statement We saw already how to negate quantified statements. With DeMorgan's Laws in hand, we now know how to negate \wedgeand \veestatements. What's left$? Aha, conditional statements!
### 4.7.1 Negating Conditional Statements Consider a claim of the form P =$\Rightarrow \mathbb{Q}$. It says that whenever P is true, Q is also true. How do we negate such a statement? What would the logical negation even mean? Think back to how we defined " =$\Rightarrow$" as a logical connective. In which cases did we get to call the speaker of the conditional statement a liar. Those are precisely the cases where we would say the logical negation is True. The only such case was when the hypothesis P was True but the conclusion Q was False. To prove this equivalence, we need to remember the way to write P =$\Rightarrow \mathbb{Q}$ as an "$\vee$" statement: (P =$\Rightarrow Q) \Leftrightarrow (\negP \veeQ) This will help us in the proof of the following claim.$
<div class="def-theorem" markdown>
**Lemma 4.7.1. The logical negation of a conditional statement is given by**
</div>
$\neg(P = \Rightarrow Q) \Leftrightarrow P \wedge\negQ$
<div class="def-proof" markdown>
*Proof.* Observe that
</div>
$\neg(P = \Rightarrow Q) \Leftrightarrow \neg(\negP \veeQ) Logical equivalence proven already \Leftrightarrow \neg(\negP) \wedge\negQ DeMorgan's Law for Logic \Leftrightarrow P \wedge\negQ since \neg(\negP) \Leftrightarrow P$ This makes intuitive sense: $to show that a conditional claim is False, we need to find a case where the hypothesis holds but the conclusion fails. Despite the risk of putting bad ideas into your head that weren't already there, we are going to point out some statements that are NOT logically equivalent to \neg(P = \Rightarrow Q). These are common mistakes that we see students use fairly often. Let's check them out and see why they don't actually work. For each of them, keep in mind that we want the logical negation \neg(P = \Rightarrow \mathbb{Q}$) to


> 🇨🇳 总结：逻辑等价的判定有两种方法——真值表（穷举但机械）和等价律化简（快速但需要技巧）。熟练掌握两种方法对证明写作至关重要。


