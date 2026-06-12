---
title: A.6 Cardinality
---

# A.6 Cardinality

<div class="def-definition" markdown>
**Definition 7.6.2. Let S be any set. We say S is infinite if and only if S is**
</div>
not finite. That is, S is infinite if $\forall n \in \mathbb{N} \cup${0}, every possible function f : S \to[n] fails to be a bijection. When S is infinite, we use |S| to indicate the cardinality of the set. It might seem silly to define infinite in this way---not finite---but it certainly reflects the intuitive dichotomy between the two concepts. A set can't be both finite and infinite, so rather than come up with a way to categorize both of them, let's catgeorize one and define the other to be "anything else". Also, we do not write |S| = \inftyto indicate that a set is infinite. As we will see very shortly, there are actually many different "levels" of infinite sets. This might seem incredibly bizarre to you right now, but you will see what we mean. Yes, there are different "sizes" of infinite sets, and we will use |S| to indicate the cardinality of S so that we may compare it to that of other sets. Writing |S| = $\infty$would indicate there is only "one infinity", and this is very much incorrect. Now, that said, we are mostly going to distinsuigh just two types of infinite sets, for our purposes. We are doing this to show you some striking results about the sets we are already familiar with, namely N and Z and Q and R. The following definition tells us what these two types are.
<div class="def-definition" markdown>
**Definition 7.6.3. Let S be any set.**
</div>
We say S is countably infinite if and only if there exists a bijection f : S $\to \mathbb{N}$. We say S is uncountably infinite (or just uncountable) if and only if S is infinite and every function f : S $\to \mathbb{N}$ fails to be a bijection. Given an infinite set S, this definition establishes two possibilities for S, based on how its cardinality |S| compares with N. We use the term countably infinite because it represents why we intuitively think of N as infinite. The set N has "a lot" of elements, so many so that if we tried to count them we would never finish; however, the fact that we can even try to count them in this way indicates something special. There is a 1st element of N, and a 2nd element, and a 3rd, and... We can't name them all in our lifetime, but we could program a magical, immortal robot to print them out one-by-one. If we thought of a natural number ahead of time, no matter how huge that number is, we know the robot will eventually print out that number. Perhaps we can't do this with all infinite sets, though. This is what the notion of an uncountably infinite set is meant to convey. Such a set is infinite, so there is no correspondence with a set of the form [n], but it is also "so large" that we cannot identify a "1st element" and a "2nd element" and a "3rd element" and... This is what a bijection f : S $\to \mathbb{N}$ would convey, a way to label all the elements of S in a way that shows they are paired offwith the natural numbers. If we cannot do this, then the set is uncountably infinite. Now, you might not believe that such sets exist! Don't worry, we will show you some. For now, just


> 🇨🇳 基数（Cardinality）本节用函数的语言来讨论集合的"大小"——包括有限集和无限集。


be aware of the distinction between countably and uncountably infinite: the difference rests on whether a bijection with N exists. Comparing Cardinalities As we mentioned, when S is infinite, we use |S| to compare the cardinality of S to that of other sets. We won't write something like |S| = $\infty$. Rather, we will write something like |S| = |T| to indicate that S and T have the same cardinality, whatever that may be. We might also write something like |S| < |P| to indicate P has a strictly larger cardinality than S. The following definition tells us how the comparison of cardinalities is based on functions and, specifically, different kinds of jections.
<div class="def-definition" markdown>
**Definition 7.6.4. Let S, T be any sets.**
</div>
• We write |S| = |T| if and only if there exists a bijection f : S $\to T$. In this case, we say S has the same cardinality as T. • We write |S| \leq|T| if and only if there exists an injection f : S \to T. In this case, we say S has cardinality at most |T|. • We write |S| < |T| if and only if |S| \leq|T| and |S| \neq |T|. In this case, we say S has a strictly smaller cardinality than T. • We write |S| \geq|T| if and only if there exists a surjection f : S \to T. In this case, we say S has cardinality at least |T|. • We write |S| > |T| if and only if |S| \geq|T| and |S| \neq |T|. In this case, we say S has a strictly larger cardinality than T. Let's explain the motivation behind these definitions in two different ways: In general, f : A \to B being an injection tells us |A| \leq|B| and g : A \to B being a surjection tells us |A| \geq|B|. Think about schematic diagrams for the functions f and g to see why this definition makes sense. Having an injection from A \to B means we can definitely "pair" the elements of A to elements of B without overlapping, but perhaps there are "many more" elements of B left over. Likewise, having a surjection from A $\to B$ means we can definitely "cover" all of B with elements of A, but maybe we had to overlap sometimes to do this, so A could have "more" elements than B. Having both of these situations together (i.e. a bijection from A to B) means that A and B actually have the same cardinality: we can pair offall their elements. This is an intuitive explanation to motivate these definitions, mind you. These types of explanations are not rigorous proofs. But now that we have made these definitions, we can use them to prove and disprove statements! To compare cardinalities of sets---even infinite ones---we just need to find a function with an appropriate property. All of our work in the rest of this chapter will be quite helpful in our journey through the Kingdom of Cardinality.


> 🇨🇳 **有限集的基数** 集合 $S$ 是有限的，若存在 $n \in \mathbb{N} \cup \{0\}$ 和双射 $f: S \to [n]$。此时 $|S| = n$。


Another way to think about these definitions is that "has the same cardinality as" is an "equivalence relation" on the "set of all sets". We have to put quotes around these phrases because, as we explained in detail in Section 3.3.5 about Russell's Paradox, there is no such thing as the "set of all sets". Thus, it doesn't make mathematical sense in our context to talk about an equivalence relation on that "set". In some fuzzy sense, though, this is what's going on: • Given any set S, there is certainly a bijection with itself: the identity function, IdS : S $\to S$. This shows |S| = |S|, i.e. the "has the same cardinality as" relation is "reflexive". • Suppose |S| = |T|, so there is a bijection f : S \to T. Is there a bijection g : T \to S, as well? Why yes, we can use g = f -1, of course! We know that is also a bijection. This shows |T| = |S| via a bijection, as well, i.e. the "has the same cardinality as" relation is "symmetric". • Suppose |S| = |T| = |U|, so there are bijections f : S \to T and g : T \to U. Does there exist a bijection h : S $\to U$, as well? Yes! The composition g \circ f is also a bijection (this is something you will prove/have proven in the exercises). This shows |S| = |U| via a bijection, as well, i.e. the "has the same cardinality as" relation is "transitive". Again, this is not exactly what's going on, but it can really help you sort through these difficult, abstract ideas. We are establishing a way to take any two sets and compare their cardinalities using functions. All of the sets in the universe will be "partitioned" into different "classes" based on their cardinalities. What's truly amazing is what we are about to prove for you: that there are infinitely-many cardinalities. Cantor's Theorem The following result and proof are due to the German mathematician Georg Cantor from the mid- to late-1800s. By now, mathematicians have fully embraced the result and its consequences. However, at the time, this idea was so controversial that some mathematicians refused to believe him. In time, though, his work and ideas helped lead to the development of formal set theory. The proof of this particular result is known as Cantor's Diagonalization Argument. We will use an argument like this later on, where we will point out why it is like a "diagonal". For now, we are more interested in the conclusion of this theorem.
<div class="def-theorem" markdown>
**Theorem 7.6.5. Let S be any set. Then |S| < |P(S)|.**
</div>
This says that the power set of a set always has strictly larger cardinality than the set itself. This makes sense for finite sets. You discovered already that the power set of [n] has 2n elements, i.e. |P([n])| = 2n. (You will prove this by induction, using results about cardinality, in Problem 7.8.30.) We see, indeed, that n < 2n for every n $\in \mathbb{N}$. However, this theorem also asserts that


> 🇨🇳 **可数无限（Countably Infinite）** $S$ 是可数无限的，若存在双射 $f: S \to \mathbb{N}$。即 $S$ 可以与自然数一一对应。


this relationship holds for infinite sets. Wow! Immediately, this tells us that there is a whole chain of infinite sets, each one bigger than the previous one. We can just kept taking the power set of what we had before: |N| < |P(N)| < P {P(N) } < P { P {P(N) }} < $\cdot \cdot \cdot$ Let's prove this theorem. The proof is very short and clever, so don't worry about how to come up with such an argument. Focus on understanding the logical flow.
<div class="def-proof" markdown>
*Proof.* Let S be any set. AFSOC |S| $\geq$|P(S)|.
</div>
This means there exists a function g : S $\to P$(S) that is surjective. Define T = {X \in S | X \notin g(X)}. (This makes sense because, for any X \in S, g(X) \in P(S), i.e. g(X) \subseteq S. Thus, either X \in g(X) or X \notin g(X) must hold.) Notice T \subseteq S, by a set-builder notation definition. This means T \in P(S). Since g is surjective, \exists Y \in S such that g(Y ) = T. Let such a Y be given. Now, is Y \in T? We consider both cases: • If Y \in T, then the definition of T says Y \notin g(Y ). However, g(Y ) = T, so this means Y $\notin T. This is a contradiction \times\times\times\times$ • If Y \notin T, then the definition of T says Y \in g(Y ). However, g(Y ) = T, so this means Y $\in T. This is a contradiction \times\times\times\times In either case, both Y \in T and Y \notin T hold. This is a contradiction \times\times\times\times Therefore, there exists no such surjection from S to P(S), i.e.$ |S| < |P(S)|. Look back at Exercise 4 in Section 7.4.5. Notice that we asked you to define a function from N to P(N), and then we asked you to prove it was not surjective. We didn't have to know what your function was! Since we were aware of this theorem, we knew you couldn't possibly have defined a surjection! Discussion: Axioms and Definitions We want to make an admission. We have glossed over some details about what constitutes a definition as opposed to a theorem, a result that needs proven from fundamental assumptions. By definition (at least, in our context) an injection and a surjection from A to B (in that direction, mind you) constitute sufficient proof of equal cardinalities, which guarantees a bijection. Likewise, an injection from A to B and one from B to A is sufficient to guarantee |A| = |B|, and so there must be a bijection between A and B. It is not totally obvious, though, why these claims should be true. Say we have an injection from A to B and one from B to A. Does this guarantee a bijection between the two sets? Well, one would hope! But this isn't a proof. This result is actually known as the Cantor-Schroeder-Bernstein Theorem:


> 🇨🇳 **不可数无限（Uncountably Infinite）** $S$ 是不可数无限的，若它既非有限也非可数无限。例：$\mathbb{R}$。


<div class="def-theorem" markdown>
**Theorem 7.6.6 (Cantor-Schroeder-Bernstein). Suppose A, B are any sets, and**
</div>
f : A $\to B$ and g : B $\to A$ are injections. Then there exists a bijection h : A $\to B$. Yes, that is a theorem; it is not trivial! One of the proofs is, in fact, constructive: it provides an algorithmic method for constructing that bijection h : A \to B, using the two injections, f : A \to B and g : B \to A. For our purposes---and for time and space restrictions---there is no need to separate this out as a theorem, let alone one with a constructive proof. It is sufficient to consider injections and surjections and their consequences vis-`a-vis cardinalities as definitions; these results "feel" intuitive and we can accept them. Just realize, though, that we are basing them on rigorous mathematical knowledge. If you are interested in learning about these subtleties and their consequences, consider taking a course or reading a book about set theory. In essence, the real issue is that we pre-supposed any two sets, A and B, can have their cardinalities compared in some meaningful way, mathematically speaking. That is, for any A and B, we have pre-supposed that we can somehow declare that |A| \leq|B| or |B| $\leq$|A| makes sense (or both, perhaps, if the sets are of "equal size"). But how can we guarantee one such comparison, or maybe both, will always apply, for any two given sets? It's not a trivial consideration! In the context of this book, one of our axioms is that the cardinalities of any two sets we consider can be compared. In the context of the mathematical universe at large, though, this is something that needs to be proved from more fundamental assumptions.
### 7.6.2 Finite Sets Before moving into the somewhat bizarre (but fascinating!) world of infinite sets, let's focus on some results about finite sets. These results will be easier to understand, intuitively, and will give us some good practice in working with functions and their properties to prove facts about cardinalities.
Theorems
For each of these results, we will state a theorem/proposition/lemma, and either prove it or have you help us with the proof via some exercises.
<div class="def-theorem" markdown>
**Theorem 7.6.7. Suppose A, B are disjoint finite sets. Then |A$\cup B$| = |A|+|B|.**
</div>
Play around with some examples to see why this claim is True. Do you see why we need the sets to be disjoint for this to work? Can you prove this claim? Remember that we want to find a bijection between the two sets...
<div class="def-proof" markdown>
*Proof.* Let A, B be finite sets that are disjoint.
</div>
We know $\exists a, b \in \mathbb{N} \cup${0} and there exist bijections f : A \to[a] and g : B $\to$[b].


> 🇨🇳 **等势（Same Cardinality）** $|S| = |T|$ 定义为：存在双射 $f: S \to T$。注意：我们不说 $|S| = \infty$，只比较集合之间的相对大小。


(That is, we suppose |A| = a and |B| = b). Let such a, b, f, g be given. WWTS |A $\cup B$| = |A| + |B| = a + b; that is, WWTS there is a bijection h : A \cup B \to[a + b]. Define the function h : A \cup B \to[a + b] by \forall x \in A \cup B. h(x) = ( f(x) if x \in A g(x) + a if x \in B Notice that h is well-defined because A \cap B = \emptyset, so every x \in A \cup B satisfies x \in A or x \in B and certainly not both. Also, 1 \leq h(x) \leq a for every x \in A, and a + 1 \leq h(x) \leq a + b for every x \in B, so h(x) \in[a + b] for every x in the domain of h. We claim that the function H : [a + b] \to A \cup B, defined by \forall y \in[a + b]. H(y) = ( f -1(y) if 1 \leq y \leq a g-1(y -a) if a + 1 \leq y \leq a + b is the inverse of h. If this holds, then we have proven that h is a bijection. Let's show that H is well-defined. Every y \in[a + b] satisfies exactly one of the two inequalities given in the definition of H. Also, f and g were given to be bijections, so f -1 and g-1 are well-defined functions (that are bijections themselves, even). Furthermore, if a + 1 \leq y \leq a + b then 1 \leq y -a \leq b so y -a \in[b] (the domain of g-1). Let's show that h \circ H = Id[a+b]. Let y \in[a + b] be given. We have two cases. (1) Suppose 1 \leq y \leq a; that is, suppose y \in[a]. Then, (h \circ H)(y) = h(H(y)) = h {f -1(y) } = f {f -1(y) } = Id$[a](y)$ = y where we used the fact f -1(y) \in A. (2) Suppose a + 1 \leq y \leq b; that is, suppose y -a \in[b]. Then, (h \circ H)(y) = h(H(y)) = h {g-1(y -a) } = g {g-1(y -a)) + a = Id$[b](y-a)$ + a = (y -a) + a = y where we used the fact that g-1(y -a) \in B. In either case, we find (h \circ H)(y) = y, and both cases are disjoint and cover all possibilities. Next, let's show that H \circ h = IdA\cup B. Let x \in A \cup B be given. We have two cases. (1) Suppose x \in A. Then, (H \circ h)(x) = H(h(x)) = H {f(x) } = f -1{f(x) } = IdA(x) = A where we used the fact that f(x) $\in$[a].


> 🇨🇳 **例：有限集** $|\{a,b,c\}| = 3$（与 $[3]$ 双射）。$|\emptyset| = 0$。


(2) Suppose x $\in B$. Then, (H \circ h)(x) = H(h(x)) = H {g(x) + a } = g-1 ({g(x) + a } -a ) = g-1{g(x) } = IdB(x) = x where we have used the fact that g(x) \in[b] so a + 1 \leq g(x) + a \leq a + b. In either case, we find (H \circ h)(x) = x, and both cases are disjoint and cover all possibilities. Thus, H = h-1, so h has an inverse. Therefore, h is a bijection. Therefore, |A $\cup B$| = [a + b] = a + b = |A| + |B|.
<div class="def-theorem" markdown>
**Corollary 7.6.8. Suppose S, T are finite sets and S $\subseteq T$. Then, |T -S| =**
</div>
|T| -|S|.
<div class="def-proof" markdown>
*Proof.* Define U = T -S. Notice that U $\cap S = \emptyset$. Apply the above theorem to
</div>
U and S to get |U| + |S| = |U $\cup S$| = |T| then subtract from both sides to get |T -S| = |U| = |T| -|S|. You can use the two results above to prove the following generalization:
Proposition 7.6.9. Suppose A, B are finite sets. Then |A $\cup B$| = |A| + |B| -
|A $\cap B$|.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 1 in Section 7.6.5.
</div>
Here's another corollary to the theorem above.
<div class="def-theorem" markdown>
**Corollary 7.6.10. Suppose A1, A2,..., An are finite and pairwise-disjoint (re-**
</div>
member this means any two of the sets are disjoint). Then |A1 $\cup \cdot \cdot \cdot \cup A$n| = |A1| + $\cdot \cdot \cdot$ + |An|.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 2 in Section 7.6.5.
</div>
You should also look at Problem 7.8.32 in this chapter's exercises. There, we guide you through a proof (by induction on two variables!) about the size of the Cartesian product of two finite sets.
### 7.6.3 Countably Infinite Sets Let's move on to investigate the land of countably infinite sets. We will start by talking about a famous thought experiment, named after the mathematician David Hilbert.


> 🇨🇳 **例：可数集** $|\mathbb{N}| = |\mathbb{Z}|$（双射：$f(0)=1, f(1)=2, f(-1)=3, f(2)=4, f(-2)=5, \ldots$，即 $f(n) = 2n+1$（$n \geq 0$），$f(n) = 2|n|$（$n < 0$））。


The Hilbert Hotel Let's play make-believe. This will help us get a handle on infinite weirdness. Pretened we own a hotel. There are countably infinitely many rooms in our magical building. They are numbered as Room 1, Room 2, Room 3,.... That is to say, our rooms are indexed by the set of natural numbers, N. We want to accomodate as many people as we can (to make lots of money!) and because our hotel is so swanky and accomodating, our guests are totally willing to move to a new room whenever we ask them to. It just takes them a couple of minutes to gather their belongings and walk down the hall to a new room. We also have a loudspeaker system that allows us to communicate a message to all of the guests at once. • Suppose all the rooms are full. It's a very busy weekend. One guy walks into the lobby looking for a room. Can we squeeze him in? If not, why? If so, how? It turns out that we can! We can just shift all the guests down one room and place this new guy into Room 1. The catch, though, is to take advantage of our loudspeaker system. If we had to go and knock on everyone's door telling them to move down one room, we would never actually finish; we would spend all of eternity knocking on doors and delivering messages. Instead, we make the following announcement: Attention guests: If you find yourself in Room n, please move to Room n + 1. Thank you! After five minutes, the guests have all moved, and Room 1 is vacant for our new guest. Morally speaking, we have just verified that the set N and the set N $\cup{\star$} have the same cardinality, for any particular object \star. In particular, say, |N| = |N $\cup${0}|. Our hotel has only countably many rooms, and we have accomodated one person associated with each natural number, as well as one more person. • It's the next day. Our rooms are still full. Suppose a Scrabble convention with countably infinitely many people shows up. The people are all wearing nametags with natural numbers on them, so there is Person 1, Person 2, Person 3,.... Can we accomodate these folks? How can we assign them rooms? How do we move around the guests currently in the hotel? It turns out that we can! The idea is to free up an infinite set of rooms.


> 🇨🇳 **例：可数集** $|\mathbb{N}| = |\mathbb{Q}|$——有理数集可数！证明：将正有理数排成 $p/q$ 的表格（行=分子，列=分母），按对角线枚举，跳过重复。负有理数和零类似处理。


Again, the catch is to do this by making one blanket announcement to all of the guests at once, as opposed to knocking on everyone's door. We recognize that the set of even-numbered rooms and the set of oddnumbered rooms are both infinite in size, so let's make the current guests in the hotel occupy the even-numbered rooms and assign the new guests from the convention to the odd-numbered rooms. We make the following announcement to the hotel guests via the loudspeaker: Attention guests: If you find yourself in Room n, please move to Room 2n. Thank you! Then, we make the following announcement to the convention folks waiting in the lobby: Attention convention-goers: If you are wearing nametag number n, please go to Room 2n -1. Thank you! After five minutes, every hotel guest has moved, and after another five minutes, every convention-goer has found their room. Voil´a! Morally speaking, we have just verified that the union of two disjoint countably infinite sets is countably infinite, as well. That is, we took the set A of current hotel guests (notice A is countably infinite) and the set B of convention guests waiting for rooms (notice B is countably infinite, and notice that A $\cap B = \emptyset$) and found a bijection between A $\cup B$ and N, where N represents the set of Rooms. • Now, suppose another convention shows up. They play Scrabble in a different language, so they don't want to be associated with the other convention. How can we move folks around to get everyone a room? We can do the exact same thing! It's as if we were facing the same situation as before, with just a full hotel and a countably infinite set of people waiting for rooms. • Now, suppose countably infinitely many conventions show up, each of them not wanting to be associated with the others. Oh my! Luckily, the hotel convention organizer has assigned every convention a natural number, and each member within a convention gets a hat with that number on it. Also, within each convention, each person is assigned a natural number, and they wear a badge with that number. Thus, each person has two forms of identification: a hat and a badge. So we have Person 1 from Convention 1, and Person 3 from Convention 7, and Person 12 from Convention 8, and so on and so forth. How do we rearrange all of these people in the hotel? Can we even do it? How can we do it efficiently?


> 🇨🇳 **不可数：$\mathbb{R}$** 康托尔对角线法证明 \mathbb{R} 不可数。反证：设 \mathbb{R} 可数，列出 $r_1, r_2, \ldots$。构造 x 使 $x$ 的第 n 位小数与 $r_n$ 不同——则 $x$ 不在列表中，矛盾！


The catch here is that we cannot apply the same method as the previous two cases over and over. Yes, we can squeeze in Convention 1 using that method. After that's done, we would squeeze in Convention 2. And so on. But never would we get to all of the conventions. It's the same problem we had before where knocking on every individual door would take forever to accomplish; we needed to send a message to everyone at once. Likewise, here, we need to send a message to all of the hotel guests, and then a message to all of the convention-goers waiting outside the door. It needs to be a general "formula" about which room to go to. If it helps, think of this from the other side of the situation. Pretend you are in Convention x and you are Person y in that convention. You are eagerly awaiting a comfortable bed to sleep in for the night. You want to know exactly what room to go to. ASAP. You don't want to wait around and see all of the conventions ahead of you given rooms, one by one. You want to all go in at once and find your corresponding rooms. Here's one way to do it. Let's take advantage of the structure of the prime numbers. We know there are countably infinitely many primes, and that for any two different primes p and q (i.e. p \neq q), it is true that pk \neq qk for any natural number k. With this in mind, we see that assigning individual conventions to the rooms that are powers of a corresponding prime number, we can ensure that no two (potential) guests get assigned to the same room. We make the following announcement to our current hotel guests: Attention guests: If you find yourself in Room n, please move to Room 2n. Thank you! We then make the following announcement to the conventions waiting outside the door: Attention convention-goers: If you are Person number k from Convention number 1, please go to Room 3k. If you are Person number k from Convention number 2, please go to Room 5k. If you are Person number k from Convention number 3, please go to Room 7k. In general, if you are Person number k from Convention number n, please go to the Room numbered by the (n + 1)-th prime number raised to the $k$-th power. Thank you! (Note: We are assuming that all of our guests and potential guests are math genii, and they can quickly figure out what the (n + 1)-th prime


> 🇨🇳 **康托尔对角线论证的细节** 设 $r_n = 0.d_{n1}d_{n2}d_{n3}\ldots$。令 $x = 0.e_1e_2e_3\ldots$，其中 $e_n \neq d_{nn}$ 且 $e_n \notin \{0,9\}$（避免 $0.999\ldots=1$ 问题）。则 $x$ 与每个 $r_n$ 都不同。


number is and raise it to the $k$-th power. Otherwise, we wouldn't want them to stay at our luxurious, mathematical hotel in the first place!) Notice that this guarantees everyone has a room all to themself. Nobody has to share a room. However, it does leave many rooms empty. Who is in Room 1? Room 6? Room 18? In general, can you characterize the set of rooms that will be empty? How could we have been more "efficient" about this? Is there a certain announcement we could make so that all the rooms are filled? $Morally speaking, we just verified that \mathbb{N} and \mathbb{N} \times \mathbb{N} have the same cardinality. We had countably infinitely many conventions with countably infinitely many people in each, so every person we wanted to accomodate corresponds to an ordered pair of natural numbers, where the first coordinate is their Person number and the second coordinate is their Convention number. Since we were able to match this set of people with the set of rooms (which corresponds to N), then we showed \mathbb{N} \times \mathbb{N} is countable. (Note$: We actually "overdid" $it and found a way to embed the set \mathbb{N} \times \mathbb{N} in a strict subset of N!) This hopefully gives you a flavor for how to think about countable infinities. One important point to keep in mind is that infinity is a cardinality, not a number, in our context here. It's not as if the natural numbers$ "keep going" and there's some magical number $\infty$lying out there past them all. Here, we refer to countably infinite as a cardinality; it represents how "big" something is. It's more like a magnitude than a position.
Examples
Let's take some of the ideas conveyed by the Hilbert Hotel examples and express them more formally. We'll make use of injections and surjections and bijections. (Oh my!) The following result will be helpful as we go along, so let's prove it now.
<div class="def-theorem" markdown>
**Lemma 7.6.11. Let S, T be any sets. Suppose S $\subseteq T$. Then |S| $\leq$|T|.**
</div>
<div class="def-proof" markdown>
*Proof.* Define the "identity function" f : S $\to T, given by \forall x \in S$. f(x) = x.
</div>
Since S $\subseteq T$, this is a well-defined function. (Note: We couldn't technically define this as the usual identity function IdS, because the domain and codomain might not be equal sets; in essence, f does the same action as IdA but has a different codomain). Notice that f is injective! (Note: It's not necessarily bijective, because it might be that S \neq T.) Since f is injective, this tells us that |A| $\leq$|B|.


> 🇨🇳 **子集的基数** 若存在单射 $f: A \to B$，则 $|A| \leq |B|$。若存在满射 $f: A \to B$，则 $|A| \geq |B|$。


You might be wondering why we can't conclude |A| < |B| here. Why is it "$\leq$" instead? Certainly, {1, 2} $\subseteq${1, 2, 3} and |{1, 2}| = 2 < 3 = |{1, 2, 3}. This is true for finite sets, but as we shall see in this section, there are infinite sets that have strict subsets of equal cardinality!
Example 7.6.12. Z is countably infinite:
We know N is countably infinite by definition. The identify function IdN : N $\to \mathbb{N}$ is obviously a bijection, so N is countable. In this example, we will prove that Z is countably infinite! To accomplish this, we need to find a bijection f : Z $\to \mathbb{N}$. We will state one here and then prove it is a bijection by finding its inverse. Before reading on, try to find a bijection on your own! Maybe you'll come up with a different function than ours! If you need a hint for coming up with one, think about this: to prove an infinite set is countably infinite, we want to find a way to start listing the elements one by one. Try to find a pattern that identifies the "1st" integer, and then the "2nd, and then the "3rd",... Let's define a function f : Z $\to \mathbb{N}$ and then prove it is a bijection by identifying f -1. Explicit bijection: We choose to define f : Z $\to \mathbb{N} by setting \forall z \in \mathbb{Z}$. f(z) = ( -2z + 2 if z \leq0 2z -1 if z > 0 We chose this function because it "pairs off' the integers with the natural numbers like this:..., -3, -2, -1, 0, 1, 2, 3,... ↕ ↕ ↕ ↕ ↕ ↕ ↕..., 8, 6, 4, 2, 1, 3, 5,... (That is, we are pairing offthe even natural with the non-positive integers, and the odd natural with the positive integers. Looking at this correspondence, we can see how to "reverse" it. This is how we will find f's inverse.) Next, Define F : N $\to \mathbb{Z}$ by F(n) = ( -n 2 + 1 if n is even n+1


> 🇨🇳 **Cantor-Schröder-Bernstein 定理** 若存在单射 $f: A \to B$ 和单射 $g: B \to A$，则存在双射 $h: A \to B$，故 $|A| = |B|$。这提供了"等势"的更方便的判定方式。


if n is odd Let's show F = f -1. Let z $\in \mathbb{Z}$ be given. We have two cases. • Suppose z \geq1. Then f(z) = 2z -1. Notice that 2z -1 $\in \mathbb{N}$ and 2z -1 is odd. This means (F \circ f)(z) = F(f(z)) = F(2z -1) = (2z -1) + 1


> 🇨🇳 **$|\mathcal{P}(\mathbb{N})| > |\mathbb{N}|$** 康托尔定理：对任何集合 A，$|A| < |\mathcal{P}(A)|$。证明：单射 $f: A \to \mathcal{P}(A)$（$a \mapsto \{a\}$）给出 $|A| \leq |\mathcal{P}(A)|$。反证等势：设双射 $g: A \to \mathcal{P}(A)$，令 $D = \{a \in A \mid a \notin g(a)\}$，则 $D \in \mathcal{P}(A)$ 但 $D \neq g(a)$ 对所有 $a$——矛盾！


• Suppose z $\leq$0. Then f(z) = -2z+2. Notice that -2z \geq0 so -2z+2 \geq2 so -2z + 2 $\in \mathbb{N}$. Also, -2z + 2 is even. This means (F \circ f)(z) = F(f(z)) = F(-2z + 2) = --2z + 2


> 🇨🇳 **无限集的直觉** 无限集可以与自己的一部分等势——如 $|\mathbb{N}| = |2\mathbb{N}|$（偶数集）。这在有限集中不可能：有限集不能与自己的真子集等势。


+ 1 = -(-z + 1) + 1 = (z -1) + 1 = z In either case, (F \circ f)(z) = z. This shows F \circ f = IdZ. Next, let n $\in \mathbb{N}$. We have two cases. • Suppose n is even. Then F(n) = -n 2 + 1. Notice that n 2 \geq1 and so -n 2 \leq-1 + 1 = 0. This means (f \circ F)(n) = f(F(n)) = f { -n 2 + 1 } = -2 { -n 2 + 1 } + 2 = (2n 2 -2 ) + 2 = n • Suppose n is odd. Then F(n) = n+1 2. Notice that n + 1 $\geq$2 and so n+1


> 🇨🇳 **Dedekind 无限** 集合 $A$ 是无限的（Dedekind 定义），当且仅当存在 C \subset A（真子集）使 $|A| = |C|$。


$\geq$1. This means (f \circ F)(n) = f(F(n)) = f (n + 1


> 🇨🇳 **可数集的性质** (1) 可数个有限集的并仍可数。(2) 有限个可数集的并仍可数。(3) $\mathbb{N} \times \mathbb{N}$ 可数。


-1 = (n + 1) -1 = n In either case, (f \circ F)(n) = n. This shows f \circ F = IdN. Therefore, F = f -1. This shows that Z and N have the same cardinality, that |Z| = |N|. You might feel like there are "twice as many" integers as naturals, but this is where your intution fails. We can pair up the elements of these two sets one-by-one, so they must be of the same size! This is an example that shows you why the conclusion of Lemma 7.6.11 is the best it can be. Here, N $\subset \mathbb{Z}$ (a strict subset) and yet |N| = |Z|. This can only happen when have infinite (not finite) sets, and here is one such example. (Later in this section, we will in fact prove that this is an equivalent way of characterizing when a set is infinite: whether or not we can find a bijection between the set and a strict subset of itself.)
$Example 7.6.13. \mathbb{N} \times \mathbb{N} is countably infinite$:
$With the Hilbert Hotel discussion in the previous section, we essentially argued for the fact that \mathbb{N} \times \mathbb{N} has the same cardinality as N. When we had infintely-countably-many conventions, each with infinitely-countably-many people in them, we could still fit them all into our hotel with infinitely-countablymany rooms! That was more of an intuitive discussion, though, so let's formally prove this fact here. We will find an explicit bijection between the two sets.$


> 🇨🇳 **连续统假设** $|\mathbb{N}| < |\mathbb{R}|$ 之间是否存在其他基数？这是连续统假设（CH）的问题——哥德尔和科恩证明了 CH 独立于 ZFC：既不能被证明也不能被否定。


Rather than finding its inverse, though, we will prove it is surjective, and ask for your help in showing that it is injective. Explicit bijection: Define f : $N \times \mathbb{N} \to \mathbb{N} by setting \forall(x, y) \in \mathbb{N} \times \mathbb{N}. f(x, y) = 2x$-1(2y -1) In proving that f is a bijection, we will be proving this fact: Every natural number can be written uniquely as a power of 2 times an odd natural number. Look at the function we defined. It takes a pair of natural numbers and outputs a power of 2 times an odd natural number. Proving this is a bijection shows that it never outputs the same natural twice (injectivity) and every natural number is an output of some pair (surjectivity). You might try playing around with the function, plugging in some values and seeing what happens. Also, you might try working "backwards", trying to figure out what f -1 might possibly do. For instance, take your favorite n $\in \mathbb{N}$. Can you express it as a power of 2 times an odd? If n is odd, this is quite easy, since 20 = 1. For instance, 11 = 1 \cdot 11 = 20 \cdot (2 \cdot 6 -1) = f(1, 6) (Notice that we had to use x -1 and 2y -1 in the definition of f because we are working with N, and 0 $\notin \mathbb{N}$.) If n is even, we can just divide by 2 iteratively until we can't anymore; what's left must be an odd number. For instance: 40 = 2 \cdot 20 = 4 \cdot 10 = 8 \cdot 5 = 23 \cdot (2 \cdot 3 -1) = f(4, 3) and 32 = 2 \cdot 16 = $2^2 \cdot 8$ = $2^3 \cdot 4$ = $2^4 \cdot 2$ = 25 = 25 \cdot (2 \cdot 1 -1) = f(6, 1) This observation is crucial in proving that f is surjective: f is surjective: We claim \forall n $\in \mathbb{N}. n \in Imf(N \times \mathbb{N}). We prove this by a$ "minimal criminal" argument. BC: Notice that f(1, 1) = $2^0 \cdot 1$ = 1. Thus, 1 $\in Imf(N \times \mathbb{N}). IH$: Suppose we have n $\in \mathbb{N}$ -{1} that has no such representation as a power of 2 times an odd, i.e. suppose n $\notin Imf(N \times \mathbb{N}). IS$: We have two cases: • If n is odd, then... well, n \cdot 20 = n $\cdot$ 1 = n is such a representation. That is, we know n+1


> 🇨🇳 **基数算术** 对无限基数 $\kappa, \lambda$：$\kappa + \lambda = \max(\kappa, \lambda)$，$\kappa \cdot \lambda = \max(\kappa, \lambda)$。$2^{\aleph_0} = |\mathbb{R}|$。


$\in \mathbb{N}$ and we see that f ( 1, n + 1


> 🇨🇳 **练习** (1) 构造 $\mathbb{Z}$ 与 $\mathbb{N}$ 之间的双射。(2) 证明 $\mathbb{N} \times \mathbb{N}$ 可数。(3) 用对角线法证明 $(0,1)$ 不可数。


) = 20 $\cdot$ ( 2 $\cdot$ n + 1


> 🇨🇳 (4) 证明 $|[0,1]| = |(0,1)|$。(5) 证明 $|\mathbb{R}| = |(0,1)|$。(6) 证明可数个可数集的并仍可数。


-1 ) = 1 $\cdot$ (n + 1 -1) = n so n $\in Imf(N\timesN). This contradicts our assumption that n / \in Imf(N\timesN) so this case is not valid.$


> 🇨🇳 (7) 解释康托尔定理的证明——集合 $D$ 的构造为何产生矛盾。(8) 计算 $|\mathbb{R} \times \mathbb{R}|$——$\mathbb{R} \times \mathbb{R}$ 与 $\mathbb{R}$ 等势吗？


• If n is even, then, consider n 2. AFSOC we have a representation of n 2 as a power of 2 times an odd, i.e. suppose n 2 $\in Imf(N \times \mathbb{N}). This means \exists(x, y) \in \mathbb{N} \times \mathbb{N}. f(x, y) = n 2. Let such (x, y) be given. Consider, then, f(x + 1, y) (which is valid since x + 1 \in \mathbb{N}$, as well). We see that f(x + 1, y) = 2x+1 \cdot (2y -1) = 2 \cdot {2x \cdot (2y -1) } = 2 \cdot f(x, y) = 2 \cdot n 2 = n This shows we would have such a representation for n; i.e., in fact, n \in $Imf(N\timesN). Again, this contradicts our assumption that n / \in Imf(N\timesN). Thus, n 2 also has no such representation, i.e. n 2 / \in Imf(N \times \mathbb{N}). We have shown that, supposing n is a counterexample to the claim, n 2 is a smaller counterexample to the claim. By a$ "minimal criminal" argument (since we proved our base case), we conclude that the claim holds for every n $\in \mathbb{N}$. This shows f is surjective. (Note: You might want to look back at Section 5.5.1 to refresh your memory about how "minimal criminal" arguments work.) f is injective: You prove this! See Exercise 7.8.21. Together, we have proven that f is a bijection, and so |N \times N| = |N|$. That is, \mathbb{N} \times \mathbb{N}, the set of all ordered pairs of natural numbers, is countably infinite. Does this surprise you at all$? Does it seem counter-intuitive? What do you think might be true about the set N3 of all ordered triplets of natural numbers? $What do you think would happen if we took \mathbb{N} \times \mathbb{N} \times \mathbb{N} \cdot \cdot \cdot$ ? Think about these ideas. Discuss them with your classmates, and try to prove something!
$Example 7.6.14. \mathbb{N} \times \mathbb{N} as a lattice$:
Before moving on to another example, let's show you one more way of thinking about why |$N \times \mathbb{N}$| = |N|$. This will be an intuitive explanation, more like a description of how to define a bijection between the sets without actually making the definition. However, it's a common argument and is well worth seeing. The idea is to think of \mathbb{N} \times \mathbb{N} as a lattice of points, like so$:


> 🇨🇳 **$[0,1]$ 的不可数性** Cantor 对角线法证明 (0,1) 不可数，进而 [0,1] 也不可数。$|\mathbb{R}| = |(0,1)|$——由双射 $f(x) = \frac{2x-1}{x(1-x)}$ 给出（调整有理端点后）。


To show that this infinite grid of points is countably infinite, we can describe a path that traverses all of the points (surjectivity!) exactly once (injectivity!) and is indexed by the natural numbers (countably infinite!). That is, we can just describe a way to traverse the whole grid in a series of steps; there will be a "1st point" and a "2nd point" and so on. The key observation to make is that the "northwestern" diagonals of this grid are all finite. Start from the point (5, 1), for instance, and move upwards and leftwards, diagonally. You will traverse over (4, 2) and (3, 3) and (2, 4) and (1, 5), and then reach the boundary of the grid. This is true no matter where you start along the bottom row of lattice points. Let's use this fact to label each lattice points with a natural number based on (a) which diagonal it lies on, and (b) where it lies along that diagonal. We'll treat the diagonal starting at (1, 1) as the 1st diagonal, the one starting at (2, 1) as the 2nd, and so on. This gives us the following labels:


> 🇨🇳 **区间等势** $(0,1)$、$[0,1]$、$(a,b)$、$\mathbb{R}$ 都等势。（a,b）与 $\mathbb{R}$ 的双射：$f(x) = \tan(\pi(x - 1/2))$。


We can see that every point in the lattice will lie on exactly one such diagonal. Furthermore, there are countably-infinitely-many such diagonals (they are indexed by N) and there are only finitely-many points on each diagonal. This means (as we will prove below) that the collection of all the points on the diagonals is countably infinite. You ought to try formalizing this argument by writing down a function that achieves the labeling we've demonstrated. Or, you could at least work with a similar one that also works, i.e. you could move southeastwards instead, or reverse the direction of alternate diagonals...
Example 7.6.15. Q is countably infinite:
This result is one of the more striking examples of our intuition failing with infinite sets and their cardinalities. Think about the elements of Q as laid out on the real number line. They're everywhere! In fact, look at Exercise 4.11.26; there, you proved that the rationals are dense, and it is also true that they are dense in R (i.e. between any two distinct real numbers lies a rational number). Furthermore, the set of rationals seems so much larger than Z: between 0 and 1 alone, there lies infinitely many rational numbers! For these reasons, you might believe that Q is uncountably infinite, but this is False. In this example, we will present several arguments for this fact, especially because we realize it is so strange and striking. (1) Intuitive argument: Consider the following "representation" of Q as a union of sets: Q "=" "$N \times \mathbb{N}$" $\cup$"-"$(N \times \mathbb{N}) \cup {0} In some sense, \mathbb{N} \times \mathbb{N} corresponds to all the positive rationals. To see why, just consider the function f$ : $N \times \mathbb{N}$ $\to \mathbb{Q}$+ defined by f(x, y) = x y. We definitely output all positive rationals (so f is a surjection), but 4 2 = 2 1 so this is not an injection. At least, this shows |N \times N| \geq|Q| $because f is a surjection. Since \mathbb{N} \times \mathbb{N} is countably infinite, and we certainly expect \mathbb{Q} to be infinite, this shows the positive rationals are countably infinite. The set of negative rationals---let's call it \mathbb{Q}$----must have the same cardinality as the set of positive rationals---let's call it Q+. There is a clear bijection between them: define g : Q+ $\to \mathbb{Q}$-by setting $\forall q$ $\in \mathbb{Q}$+. g(q) = -q. All this leaves out is 0 $\in \mathbb{Q}$. The union of two countably infinite sets is also countably infinite (as we will prove below), and adding on one more element won't change that. Thus, Q is countably infinite. Mind you, this is quite "hand-wavey". All of the "scare quotes" in the "equation" above mean you should take this as just a heuristic argument, and not a proof. However, there are ways to make all of these arguments formal. Try working on this on your own! (2) Listing Q:


> 🇨🇳 **不同级别的无限** $|\mathbb{N}| = \aleph_0$（阿列夫零），$|\mathbb{R}| = \mathfrak{c}$（连续统），$|\mathcal{P}(\mathbb{R})|$ 更大……无限不止一种"大小"！


Consider writing a computer program to print out all the positive rational numbers in a list. What algorithm would you use? As long as you can guarantee that your program will "eventually" succeed and print them all, then you have shown Q can be enumerated one-by-one, so it must be countably infinite. (Remember, this is why we use N as the canonical countably infinite set: we can enumerate its elements one-by-one, we can count them.) Here's one way that we might write such a program: Follow the same "path through the lattice" $argument that we used with \mathbb{N} \times \mathbb{N} in the previous example. This time, though, just$ "skip over" any rational you have already printed. That is, we would print the pair (1, 1) $\leftrightarrow$1 and then (2, 1) $\leftrightarrow$2 and then (1, 2) $\leftrightarrow$1 2 and then (3, 1) $\leftrightarrow$3 and then... Aha! We have to omit writing (2, 2) $\leftrightarrow$1. How did we know that? We see that we already printed 1. How did we know that? We just looked over the list of rationals we had already printed and checked to see if what we were about to print has already appeared. If so, we move on; if not, we print it and then move on. In terms of the enumeration process, this just means that for every point in the lattice we pass through, we have to check finitely-many things; namely, we have to look over the finitely-large set of rationals we have already printed. This means the printing process at any individual step will take "a little longer" but not infinitely-longer. Thus, our program will eventually print out every rational number; no matter which one you have in mind, we will get to it in finite time. (3) Q is at most countably infinite: Here's another argument about Q being countable. (If this feels like overkill, that's fine, just move on. We just know that this is a surprising result and having a few ways of thinking about it might help!) Consider this: We can definitely agree a priori that |Q| \geq|N|. This follows from the fact that Q $\supseteq N. Now, the only question is whether or not these cardinalities are equal. To reach that conclusion, we would need to find either (a) an injection from \mathbb{Q} to a countable set, or (b) a surjection from a countable set to Q. We will prove below that that \mathbb{Z} \times \mathbb{N} is countable. (That is, we will prove generally that the Cartesian product of any two countably infinite sets is also countably infinite.) We can then define the function f$ : Z \times N $\to \mathbb{Q} by \forall(z, n) \in \mathbb{Z} \times \mathbb{N}. f(z, n) = z n This is a surjection onto Q. It is definitely not injective (why not$?) but we don't care. It shows that |Z \times N| = |Q|. Once we have proven that |$Z \times \mathbb{N}$| = |N|, this will have shown that |N| = |Q|.


> 🇨🇳 **幂集的层级** $|A| < |\mathcal{P}(A)| < |\mathcal{P}(\mathcal{P}(A))| < \cdots$——通过反复取幂集得到越来越大的无限基数。


(4) Stern-Brocot Tree: There are other visual representations of Q, too! The Stern-Brocot Tree is particularly enlightening. This idea was, in fact, first introduced and developed by a French watchmaker named Achille Brocot who was looking for ways to approximate the measurements of gears he needed to make while building watches. Around the same time (the 1850s and 1860s), the German mathematician Moritz Stern developed the idea. It's amazing to think that a non-mathematician would indpendently develop this fascinating idea to solve a real-world problem he was facing! (Do not worry too much about the terminology of graphs and trees here. We will not have occasion to talk about these much further, and are only introducing this as a helpful way to represent Q and demonstrate it is countably infinite.) The root of this tree is 1. (This is the number at the very top of the diagram.) The parent-child relation (the way to generate what lies below a point in the tree) is defined in terms of continued fractions. (We won't describe here what that means; instead, we describe below how to construct the tree.) What happens with this setup is that any path through the tree from the root to another node yields a sequence of rational numbers that are better and better approximations to the ultimate node; furthermore, each successive rational in the sequence has a larger denominator than the previous one. This is the property that motivated Monsieur Brocot. He needed to determine how big to make two gears inside a watch so that the ratio of their sizes was very close to a particular number. By working downwards through this tree, he could find better approximate ratios to the number he needed! Pretty cool, right? To actually construct the tree, we find mediants. Given two rationals a b and c d, the mediant of those two is defined as a+b c+d. (Notice that this is a special


> 🇨🇳 **可数集的运算** (1) $A$ 可数、$B$ 有限 $\to A \cup B$ 可数。(2) $A,B$ 可数 $\to A \cup B$ 可数。(3) $A,B$ 可数 $\to A \times B$ 可数。


object, the mediant; it is not the correct way to add two fractions!) Each level of the tree consists of all the mediants made from consecutive pairs of rationals in the level above; we don't "count" the directly vertical elements; they are just carried over for ease of reading and construction. Also, notice that the fractions


> 🇨🇳 **不可数集的运算** (1) $A$ 不可数、$B$ 任意 $\to A \cup B$ 不可数。(2) $A$ 不可数、$B$ 任意 $\to A \times B$ 不可数。(3) 可数无限个有限集的积不可数。


0 (which is undefined, even!) are included in the outside columns to help generate the elements on the outside of each level. (Play around with the properties of this tree, and read more about. It is an interesting mathematical object!) We won't prove here that this tree contains all the rational numbers, but we think you can see why this is believable. Also, we think you can see why the set of all nodes in this tree is countably infinite. Each level has only finitely many nodes, and there are countably-infinitely-many levels.
Theorems
$Now we know that three of our standard sets of numbers---N and \mathbb{Z} and Q---are all countably infinite, as well as the set \mathbb{N} \times \mathbb{N}. With the following theorems, we will show you some ways to generate more countably infinite sets from existing ones. Let's get you warmed up with one helpful result. It says that we can take a countably infinite set and$ "tack on" finitely-many extra elements, and this keeps the result contably infinite, as well.
<div class="def-theorem" markdown>
**Lemma 7.6.16. If A is countably infinite and B is finite and A $\cap B = \emptyset$, then**
</div>
A $\cup B$ is countably infinite.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 7.8.19.
</div>
Hint: Try using a similar idea to our proof of Theorem 7.6.7.
Remark 7.6.17. Note: The assumption that A $\cap B = \emptyset i$s not essential in this
Lemma, but it makes the proof easier.
When A $\cap B \neq \emptyset$, we can apply the result just proven to the set A -B (which is countably infinite) and the set B -A (which is finite) to get the countably infinite set (A -B) \cup(B -A) (since they're disjoint). We can then apply the above result again to that set---(A-B)\cup(B-A)---and A\cap B to get the countably infinite set A \cup B = (A -B) \cup(B -A) \cup(A $\cap B$) The next result says that this works with A, B both countably infinite, as well.
<div class="def-theorem" markdown>
**Lemma 7.6.18. If A and B are countably infinite and A $\cap B = \emptyset, then A \cup B$**
</div>
is countably infinite.


> 🇨🇳 **$\mathbb{Q}$ 可数的详细证明** 正有理数枚举：排列 \frac{p}{q}（$p,q \in \mathbb{N}$）为二维表格，按对角线遍历。跳过非最简分数（如 2/4 与 1/2 重复）。总枚举数 = $|\mathbb{N}|$。


<div class="def-proof" markdown>
*Proof.* Since A and B are countably infinite, there exist bijections f : A $\to \mathbb{N}$
</div>
and g : B $\to \mathbb{N}$. Let such functions be given. We will use them to find a bijection h : A \cup B $\to \mathbb{N}$. First, define the function p : N $\to \mathbb{Z}$ -N by setting \forall n $\in \mathbb{N}$. p(n) = -n + 1. This is a bijection because p-1 : Z-N $\to \mathbb{N}$ is given by p-1(z) = -z+1. (Check this for yourself!) Since p and g are bijections, we know p \circ g : B $\to \mathbb{Z}$ -N is a bijection, as well. Next, we define the piece-wise function q : A \cup B $\to \mathbb{Z}$ by setting \forall x \in A \cup B. q(x) = ( f(x) if x \in A p(g(x)) if x \in B This is well-defined because A\cap B = \emptyset. Furthermore, this is a bijection because it is a bijection on each of the pieces is a bijection. (Again, check this for yourself to make sure it makes sense. Also, see Exercise 7.8.31 which proves this, in generality.) From previous work, we know how to find a bijection r : Z $\to \mathbb{N}$. (Remember how we did that? Look back at Example 7.6.12!) Finally, define h : A\cup B $\to \mathbb{N}$ by h = r \circ q. This is a composition of bijections, so it is a bijection. This proves |A \cup B| = |N|, i.e. A \cup B is countably infinite. The next corollary says that we did not, in fact, need to assume that A\cap B = $\emptyset$. It made the proof easier. We will ask you to prove this corollary.
<div class="def-theorem" markdown>
**Corollary 7.6.19. If A and B are countably infinite, then A $\cup B$ is countably**
</div>
infinite.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 7.8.20.
</div>
(Hint: Apply Lemma 7.6.18 to appropriately-chosen sets... ) This proves several cases about finding the union of sets. Let's prove a result about taking a Cartesian product.
<div class="def-theorem" markdown>
**$Theorem 7.6.20. If A and B are countably infinite, then A \times B is countably$**
</div>
$infinite. This one is actually easy to prove, but only because we've already proven a result about a canonical set that is a Cartesian product and is countably infinite, itself. Look at how we use \mathbb{N} \times \mathbb{N} in the proof$:
<div class="def-proof" markdown>
*Proof.* Suppose A, B are countably infinite. Then there exist bijections f : A $\to$
</div>
N and g : B $\to \mathbb{N}$. Let such functions be given. Define the function h : A \times B $\to \mathbb{N} \times \mathbb{N} by \forall(x, y) \in A \times B. h(x, y) =$ {f(x), g(y) }


> 🇨🇳 **Hilbert 旅馆** 无限旅馆已满员：新客来了？把 1 号房客移到 2 号房，2 号移到 3 号……新客住 1 号房——无限集总能为新元素"腾地方"！


We claim this is a bijection. Since f, g are invertible, we claim that H : $N\timesN \to A \times B given by \forall$(k, ℓ) $\in \mathbb{N} \times \mathbb{N}. H(k,$ ℓ) = {f -1(k), g-1(ℓ) } satisfies H = h-1. To see why, notice that $\forall(x, y) \in A \times B. (H$ \circ h)(x, y) = H(h(x, y)) = H {f(x), g(y) } = {f -1(f(x)), g-1(g(y)) } = (x, y) and \forall(k, ℓ) $\in \mathbb{N} \times \mathbb{N}. (h$ \circ H)(k, ℓ) = h(H(k, ℓ)) = h {f -1(k), g-1(ℓ) } = {f(f -1(k)), g(g-1(ℓ)) } = (k, ℓ) so H \circ $h = IdA\timesB and h$ \circ $H = IdN\timesN. This shows H = h$-1. Therfore, h is a bijection, and so |$A \times B$| = |$N \times \mathbb{N}$| = |N|. By applying induction to the two previous results, we can prove the following:
<div class="def-theorem" markdown>
**Corollary 7.6.21. Suppose A1,..., An are countable (where n $\in \mathbb{N}$, so we only**
</div>
have finitely many sets). Then A1 $\cup \cdot \cdot \cdot \cup An and A1 \times \cdot \cdot \cdot \times An are countably infinite.$
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 7.8.22
</div>
A Countable Union of Countable Sets is Countable You might wonder now what happens when we take a union or product of a countably-infinitenumber of sets, each of which is countably infinite... Let's tackle the union case here. This result is so fundamental and important, that we've even reiterated it in the section title here!
<div class="def-theorem" markdown>
**Theorem 7.6.22. Suppose we have, for each n $\in \mathbb{N}$, a countably infinite set**
</div>
An. Then the set A = [ n$\in \mathbb{N} An = A1 \cup A2 \cup A3 \cup \cdot \cdot \cdot$ is also countably infinite. We will prove this in the case that the sets are pairwise-disjoint, and leave the rest of the details to you.


> 🇨🇳 **$\mathbb{R}$ 的子集** 区间 $(a,b)$、$[a,b]$、半开区间、射线——全部与 $\mathbb{R}$ 等势。无论区间"看起来"多大多小。


<div class="def-proof" markdown>
*Proof.* Suppose we have, for each n $\in \mathbb{N}$, a countably infinite set An. Further-
</div>
more, suppose $\forall i, j \in \mathbb{N}. i \neq j =\Rightarrow Ai \cap Aj = \emptyset$. Define A = [ n$\in \mathbb{N}$ An We claim A is countably infinite. Since each An is countably infinite, we know there exists a bijection fn : An $\to \mathbb{N}$, for every n $\in \mathbb{N}$. This lets us "number" the elements of every set An, based on what the bijections fn do. Furthermore, we have a number on the An sets (they are indexed by N). In essence, then, we have a "numbering" $of the elements of A that corresponds to \mathbb{N} \times \mathbb{N}. Let's formally define this correspondence. Let's define a function F$ : A $\to \mathbb{N} \times \mathbb{N}. Given any x \in A, we know \exists n \in \mathbb{N}. x \in A$n and that this n is unique. (This follows because the given sets were pairwise-disjoint). Set F(x) = {n, fn(x) }. We claim that F is a bijection. To see why, consider the function G : $N\timesN \to A defined by \forall(a, b) \in \mathbb{N} \times \mathbb{N}. G(a, b) = f$ -1 a (b) That is, G uses the first coordinate a to identify the set Aa, and then uses the function fa to identify the element of Aa that produced b $\in \mathbb{N}$ as an output. (We will leave it to the reader to verify that, indeed, G = F -1.) This shows that |A| = |$N \times \mathbb{N}$| = |N|, so A is countably infinite. In the case where the An sets are not necessarily pairwise-disjoint... we leave this as Exercise 7.8.37.
<div class="def-theorem" markdown>
**Corollary 7.6.23. Suppose we have, for every n $\in \mathbb{N}$, a finite set An. Fur-**
</div>
thermore, suppose that these sets are pairwise-disjoint. Define A = [ n$\in \mathbb{N}$ An Then A is countably infinite.
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 7.8.36
</div>
This result is very powerful. Let's see it applied to two examples.
Example 7.6.24. The set of all powers of primes:
Recall the Hilbert Hotel discussion, where we accomodated infinitely many conventiones of people that were each infinitely large. We sent people to rooms corresponding to powers of primes. For every n $\in \mathbb{N}$, define pn to be the n-th prime number. Then, for every n $\in \mathbb{N}$, define An = {pk n | k $\in \mathbb{N}$}


> 🇨🇳 **$\{0,1\}^\mathbb{N}$ 不可数** 无限二进制字符串的集合与 $(0,1)$ 等势——每个字符串对应一个二进制小数。故不可数。


which is the set of all powers of the $n$-th prime. The theorem above says that [ n$\in \mathbb{N}$ An = {all powers of primes} is countably infinite, as well. Indeed, we should have expected that because that union is just a subset of the natural numbers, which is countably infinite itself!
Example 7.6.25. The set of all finite binary strings:
A binary string is defined to be an ordered list of 0s and 1s. A finite binary string is one that is of finite length. For example, the following are all finite binary strings: 0, 1, 101010,


> 🇨🇳 **Cantor-Schröder-Bernstein 的应用** 要证 $|A| = |B|$，不必直接构造双射——只需构造 A \to B 的单射和 B \to A 的单射。例：$|\mathbb{R}| = |\mathbb{R}^2|$：$\mathbb{R} \to \mathbb{R}^2$ 单射明显；$\mathbb{R}^2 \to \mathbb{R}$ 可用交织数字构造。


For every n $\in \mathbb{N}$, let's define Fn to be the set of all binary strings of length n. For instance, F1 = { 0, 1 } F2 = { 00, 01, 10, 11 } F3 = { 000, 001, 010, 100, 011, 101, 110, 111 } and so on. (Notice that |Fn| = 2n. Try to prove that!) Then, define the set of all finite binary strings by F = [ n$\in \mathbb{N}$ Fn An element of F must have come from some set in the big union; this means that an arbirtrary element x \in F is some binary string with some finite length. That length could be a huuuuuuuge number, but it is finite. (This points out the distinction between allowing something to be "arbitrarily large (but finite)" and allowing something to be "infinite".) The point of this example is that F is countably infinite, according to the theorem above! (Well, it follows from the corollary stated right after, actually.) Contrast this with the set S of all infinite binary strings, which is---as we will prove shortly---uncountably infinite. We will use these sets of binary strings fairly often as examples! Passing OffTo A "Limit" We proved above that if A and B are countably infinite, then so are A $\cup B and A \times B. We also encouraged you to prove (by induction on the number of sets in the union/product) that A1 \cup A2 \cup \cdot \cdot \cdot \cup A$n = [ i\in[n] Ai and Y i$\in [n] Ai = A1 \times A2 \times \cdot \cdot \cdot \times An are both countably infinite, as well, for any n \in \mathbb{N}$.


> 🇨🇳 (9) 解释 Hilbert 旅馆如何接纳可数多个新客（不只一个）。(10) 证明 $|\{0,1\}^\mathbb{N}| = |\mathcal{P}(\mathbb{N})|$。


What do these results tell us, if anything, about A1 $\cup A2 \cup A3 \cup \cdot \cdot \cdot = [ k\in \mathbb{N} Ak and A1 \times A2 \times A3 \cdot \cdot \cdot = Y k\in \mathbb{N}$ Ak That is, what happens when we try to "jump to the limit" from having a finite union/product (of arbitrarily large size, but still finite) to having an infinite union/product? Can we make necessary conclusions? Can we find counterexamples? The main idea is that "passing to a limit" does create some mathematical object, but we can't necessarily pre-suppose that this object has the exact same properties as all of the objects in the sequence that defines that object. Think about the finite sets [n], for every n. Each of them is finite, but "in the limit" we get N which is not finite. So yes, we do get some object (another set), but it doesn't have to have the same properties. The important theorem above shows that passing to the limit in the union definitely preserves countability. As we will see below in the next section, the product definitely does not preserve countability. (In fact, even an infinite product of finite sets is uncountable. Yikes!) A similar notion appears in calculus. We promised we would not use calculus, but there is such a natural relationship between these ideas, so we feel compelled to mention an easy example. If you don't get anything out of this, no worries; if you do, though, try to remember this connection and think about how it might fundamentally change your view of everything you learned in calculus.) Consider a limit, something like lim x$\to \infty$


> 🇨🇳 (11) 证 $|[0,1]| = |\mathbb{R}|$。(12) 用 CSB 定理证 $|\mathbb{R}| = |\mathbb{R} \times \mathbb{R}|$。


x = 0 In what sense is this limit equal to 0? Why would we, as mathematicians over the years, choose to define limits in this way? Formally, this limit makes sense because of the quantified definition of a limit. Let P be the set of positive real numbers. Then the definition of limit (applied to this example) says $\forall$ε $\in P$. $\exists M \in \mathbb{N}. \forall n \in \mathbb{N}$. {n > M =$\Rightarrow$


> 🇨🇳 **补充：基数的历史** 康托尔（Cantor, 1874-1897）开创了集合论和超限数理论。他的对角线法是数学史上最具创造力的论证之一。


x < ε } That is, for any small positive threshold (ε > 0), we can find a specific cutoff point (a large natural number M that depends on ε somehow) such that, for every point after M, the function 1 x falls within that ε-threshold of the limit point, zero. Notice that this is very different than saying some nonsense like " 1 $\infty$= 0" That's not what's going on. We never actually get to "plug in" the end of the limit and evaluate it. The limit is defined in terms of quantifications, some things that are happening for arbitrarily large values, but not for an infinite value.


> 🇨🇳 **补充：序型与基数** 基数只关心"有多少"，序型还关心"如何排列"。$\mathbb{N}$ 和 $\mathbb{Z}$ 有相同基数但不同序型。


### 7.6.4 Uncountable Sets To start our discussion of uncountable sets, let's prove a result we've mentioned already. Specifically, we will prove that a countably infinite Cartesian product of sets is uncountbly infinite. Notice that we don't even need to have the sets be infinite: we can make them all finite with size 2! We will use this result in the next part to demonstrate some examples of uncountable sets, including a familiar set we already know... An Uncountable Cartesian Product
<div class="def-theorem" markdown>
**Theorem 7.6.26. A countably infinite Cartesian product of sets with just two**
</div>
$elements is uncountably infinite. That is, {0, 1}N = {0, 1} \times {0, 1} \times {0, 1} \times \cdot \cdot \cdot$ is uncountably infinite.
<div class="def-proof" markdown>
*Proof.* AFSOC that this set {0, 1}N is actually countably infinite. This means
</div>
we can find a bijection between this set and N; that is, we can identify a correspondence between all the elements of this set and all of the natural numbers. Thus, there is a 1st element of this set, the element that corresponds to 1; there is a 2nd element of this set, the element that corresponds to 2; and so on. We don't know exactly what these elements are, we are just guaranteed that this correspondence exists. Still, we can write out all the elements yi of {0, 1}N in a list. Each yi is an ordered, infinite list of 0s and 1s, so we can write them like this:


> 🇨🇳 **补充：选择公理** "对任何一族非空集合，存在一个选择函数"——AC 在基数理论中不可或缺（如可数个可数集的并可数需要 AC）。


$\leftrightarrow$ (a1,1, a1,2, a1,3, a1,4, a1,5,...) = y1


> 🇨🇳 **补充：大基数** 超越 $\mathbb{R}$ 的"大基数"存在吗？不可达基数、紧致基数等——这些是大基数公理的研究对象。


$\leftrightarrow$ (a2,1, a2,2, a2,3, a2,4, a2,5,...) = y2


> 🇨🇳 **补充：$p$ 进数** 另一种"无限"——p 进数不是更大的集合，而是 \mathbb{Q} 的另一种完备化（与 $\mathbb{R}$ 平行）。


$\leftrightarrow$ (a3,1, a3,2, a3,3, a3,4, a3,5,...) = y3


> 🇨🇳 **补充：可构造性** 哥德尔的可构造宇宙 $L$ 中 CH 成立——但这个模型比一般 ZFC 模型"更小"。


$\leftrightarrow$ (a4,1, a4,2, a4,3, a4,4, a4,5,...) = y4


> 🇨🇳 **补充：计算复杂度** 可数性在计算理论中很重要：所有程序都是可数的（有限字符串），但所有函数不可数——故大多数函数不可计算。


$\leftrightarrow$ (a5,1, a5,2, a5,3, a5,4, a5,5,...) = y5... Every value ai,j is either 0 or 1. The i tells us which natural number we correspond to (i.e. the vertical position in the list) and the j tells us which coordinate we are in (i.e. the horizontal position in the list). Since we have assumed the correspondence is a bijection, we know that this list contains all of the elements of {0, 1}N. To complete the contradiction argument, we will construct an element of {0, 1}N that is guaranteed to not appear in this list! (This is a version of Cantor's Diagonalization Argument.) Let's define the object x = (x1, x2, x3,... ) by saying xi = (


> 🇨🇳 **补充：停机问题** 图灵证明了停机问题不可判定——对角线法的另一个应用。$|\text{所有图灵机}| = |\mathbb{N}|$，但 $|\text{所有函数}| = |\mathcal{P}(\mathbb{N})| > |\mathbb{N}|$。


That is, we are constructing x by going down the main diagonal of the grid of elements (so we see all of the elements ai,i) and switching the value from a 1 to a 0, or vice-versa. The following diagram is a specific example of how to do this, and is not part of this more general proof. However, we are including it for the sake of illustration:


> 🇨🇳 **补充：物理中的无限** 物理学中"无限"有不同含义：可数无限（光子能量）、不可数（时空连续性）、可除无限（微积分中）。


$\leftrightarrow$ {1, 1, 0, 0, 1,... } = y1


> 🇨🇳 **补充：集合论的基础性** 基数理论暴露了朴素集合论中的悖论（如罗素悖论），促成了公理集合论的建立。


$\leftrightarrow$ {1, 0, 0, 0, 1,... } = y2


> 🇨🇳 **补充：可数性等级** $\aleph_0$（可数）$\to$ $\mathfrak{c}$（连续统）$\to$ $2^{\mathfrak{c}} \to$ ……每一级严格更大。是否有无穷多个"中间级"？这是一个深奥的未解问题。


$\leftrightarrow$ {0, 0, 1, 1, 0,... } = y3


> 🇨🇳 更多高级练习 (13) 证明 $|\text{常数数列}| = |\mathbb{N}|$。(14) 证明 $|\text{有限子集族}| = |\mathbb{N}|$（$\mathbb{N}$ 的有限子集的集合可数）。


$\leftrightarrow$ {1, 1, 0, 1, 1,... } = y4


> 🇨🇳 (15) 解释为什么"所有有限集的集合"不是集合（避免罗素悖论）。(16) 是否存在 $A$ 使 $|\mathbb{N}| < |A| < |\mathbb{R}|$？讨论。


$\leftrightarrow$ {0, 1, 1, 1, 0,... } = y5... x = { 0, 1, 0, 0, 1,... } Why would we choose to do this? Well, think about whether or not the object x could possibly belong to the list of elements above. • Is x = y1? No, because x is different from y1 in their first coordinates. (In our example x1 = 0 because y1,1 = 1.) • Is x = y2? No, because x is different from y2 in their second coordinates. (In our example, x2 = 1 because y2,2 = 0.) • Is x = y3? No, because x is different from y3 in their third coordinates. (In our example, x3 = 0 because y3,3 = 1.) In general, for an arbitrary i $\in \mathbb{N}$, we can guarantee that x and yi differ in the i-th coordinate. Accordingly, none of the yi objects can be equal to this new object x. That is, {\forall i $\in \mathbb{N}$. xi \neq yi,i } =\Rightarrow {\forall i $\in \mathbb{N}$. x \neq yi } $But the way we defined x, it is just an ordered, infinite list of 0s and 1s, so it is definitely an element of {0, 1}N, itself. This is a contradiction. We assumed we could list all the elements of our set, but we then used this ordering to construct an element of our set that definitely does not appear in the list. \times\times\times\times Therefore, {0, 1}N is uncountably infinite.$
Note: This is a very slick argument. It's one of my favorite proofs in all of
mathematics. Cantor was a genius for coming up with it and, what's even more interesting, it's actually fairly simple and memorable, as well. We belive taht you won't forget this "go down the main diagonal and switch the values" argument. The fact that we could even sumamrize the whole proof in nine words


> 🇨🇳 回顾总结 (17) 基数的核心概念：有限$\to$可数$\to$不可数。(18) 核心定理：Cantor 定理、CSB 定理、对角线法。(19) 无限不止一种大小——这是康托尔最深刻的思想。


like that is further indication of its brilliance.
Corollary: A countably infinite product of any sets with at least two elements
each is uncountably infinite. (Note: We really only need to say that none of the sets in the product are empty and that only finitely many of them are allowed to have exactly one element.)
Examples
You might be wondering now: what types of sets are uncountably infinite? Do we know any? Sure we do! Here are some examples.
Example 7.6.27. The set of all infinite binary strings:
You may have noticed that the set we used in the proof above---namely {0, 1}N--- is "essentially" the set S of infinite binary strings! An element of {0, 1}N is an infinitely-long ordered list of coordinates, each of which is 0 or 1. An element of S is an infinitely-long ordered list of 0s and 1s, but just without the parentheses and commas. As such, there is a very natural bijection between the two (just drop the parentheses and commas, or throw them back in), so we will identify these two sets as the same. We saw above in Example 7.6.25 that the set of all finite binary strings is countably infinite. This latest result shows that the set of all infinite binary strings is uncountably infinite. An alternate proof of this fact involves finding a bijection between S and P(N), and then applying Cantor's Theorem that says |N| < |P(N)|. (See Exercise 7.8.33 for these details.)
Example 7.6.28. R is uncountably infinite:
This is our first example of a standard set of numbers that is uncountably infinite. We can use the above result to prove this fact. This claim makes some intuitive sense, since it "looks like" the real number line is "so much bigger" than just N or Z. But we also saw that Q is countably infinite, and there are tons of rational numbers scattered across the real number line; in fact, between any two real numbers there lies infinitely many rationals! What we will see now is that, yes, it is true that R is uncountably infinite. Furthermore, we will even show that R and P(N) are of the same "size" of infinity; that is, we will show |R| = |P(N)|. (Remember that this is way more informative than just saying both sets are uncountable; there are many levels of uncountably infinite sets, we are just choosing not to talk about them too much so we don't hurt our brains.) Morally speaking, the idea behind showing R is uncountably infinite, first of all, is to relate R to the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}N. Every real number can be expressed in decimal notation, which is just some ordered list of countably infinite many digits. There's a decimal point in there somewhere, and there are


> 🇨🇳 向下一章过渡 (20) 基数概念将在组合数学中再次使用——特别是计数和容斥。(21) 函数作为"对应工具"的角色贯穿了整个第 7 章。


issues like 0.999999 $\cdot \cdot \cdot$ = 1, but those aren't huge deals. Since we already saw that even a "small" set like {0, 1} yields an uncountable set when we take its product infinitely many times, then certainly a "bigger" set, like {0, 1,..., 9} will also give an uncountable set, even factoring in those issues. This is the intuitive argument you can carry around in your head and use to explain the result to your friends. (In fact, this is the argument you will find in most textbooks, as well.) More formally, we can just prove that |R| = |P(N)|. This stronger result implies that R is uncountably infinite (because Cantor's Theorem tells us |N| < |P(N)|.) To do this, we will consider the set I = {y $\in \mathbb{R}$ | 0 $\leq y$ $\leq$1} which is the interval [0, 1] $\subseteq \mathbb{R}$. We will show that |{0, 1}N| = |P(N)| = |I| and then apply some results about bijections between intervals and R. Consider the function f1 : {0, 1}N $\to I$ that takes in an infinite binary string, puts a decimal point in front of all the 0s and 1s, and says, "Evaluate this number as a decimal expansion". As an example, consider the element that is (1, 1, 0, 0, 1, 0,... ) where the rest are 0s. Then f1(1, 1, 0, 0, 1, 0,... ) = 0.110010...DEC =


> 🇨🇳 第 7 章总结 (22) 函数定义 $\to$ 像与原像 $\to$ 函数性质 $\to$ 复合与逆 $\to$ 基数。从具体到抽象、从有限到无限。


Notice that this is a function because any output is definitely a real number (since it has a decimal expansion; we just provided it) and it is somewhere between 0 and 1, since we put the decimal point in front. Furthermore, notice that f1 is an injection; two different infinite binary strings must be different in some coordinate, so they yield two decimal expansions that differ somewhere and, thus, cannot be the same real number. This shows that |{0, 1}N| $\leq$|I|. Consider the function f2 : {0, 1}N $\to I$ that takes in an infinite binary string, puts a decimal point in front of all the 0s and 1s, and says, "Evaluate this number as a binary expansion". As an example, consider the same element as above. Then f2(1, 1, 0, 0, 1, 0,... ) = 0.110010...BIN = 1 21 + 1 22 + 1 25 = 25


> 🇨🇳 最后的精简练习 (23) 证明 $\{\text{偶数}\}$ 可数 (24) 证明 $\{\text{有理代数数}\}$ 可数 (25) $\mathbb{R} \setminus \mathbb{Q}$ 可数吗？


Notice that this is a function because any output is definitely a real number; just evaluate the resulting sum of fractions and it yields a real number between 0 and 1 (and even if the series is infinite, it is guaranteed to converge). For example, the input of all 0s yields 0 as an output, and the input of all 1s yields 1 as an output since


> 🇨🇳 精简练习续 (26) $|\mathbb{N}^3| = |\mathbb{N}|$？证明。(27) 给出 $\mathbb{N} \to \{0,1\}$ 不可数的直接证明。


2 + 1 4 + 1 8 + $\cdot \cdot \cdot = X k\in \mathbb{N}$


> 🇨🇳 最后的总结 (28) 无限的层级是数学中最深刻的结果之一。从 $\aleph_0$ 到 $\mathfrak{c}$ 再到更高的超限——我们永远在探索更大的"无限"。


Furthermore, notice that f2 is a surjection. This fact hinges on some external knowledge about rational/irrational numbers; specifically, it is true that any irrational number can be approximated by a sequence of dyadic rational numbers (rationals whose denominators are powers of 2). We won't state or prove these results, but we think that by playing around with some examples, you'll start to see why this works. In fact, do some Googling for binary expansions of irrational numbers and you'll find some interesting results. Since f2 is a surjection, this shows |{0, 1}N| $\geq$|I|. Accordingly, we conclude that |{0, 1}N| = I. We also know |P(N)| = |{0, 1}N| (see Exercise 7.8.33), so we now know that |I| = |P(N)|. The last step is to prove that |I| = |R|. Look at Exercise 5 in Section 7.5.4. There, you found a bijection between the set J = {y $\in \mathbb{R}$ | -1 < y < 1} and R. It is easy to find a bijection between J and the set K = {y $\in \mathbb{R}$ | 0 < y < 1} (try it now!). This shows that |R| = |J| = |K|. Furthermore, K $\subseteq I$ and they differ by only two elements, 0 and 1, so |K| = |I|. Finally, this shows that |I| = |R|, so we conclude that |R| = |P(N)| Look at the two arguments we mentioned: • Considering the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}N, and • Considering the set {0, 1}N Both arguments involved some knowledge about decimal expansions (and binary expansions). It seems there is no easy way around this, so we hope that the results above are still convincing. In particular, you might want to play around with the idea that f2 in the discussion above is a surjection but not an injection. Can you convince yourself of these claims? Can you convince someone else?
Theorems
Let's see one results about uncountable sets. Then, we will state a final theorem about infinite sets, in general, before moving onwards!
<div class="def-theorem" markdown>
**Lemma 7.6.29. Suppose A is uncountably infinite and B is countably infinite,**
</div>
and B $\subseteq A$. Then A -B is uncountably infinite. (Note: We don't need to assume that B \subseteq A here. If this were not the case, we would just consider A and B $\cap A$ as the sets, instead.)
<div class="def-proof" markdown>
*Proof.* Left for the reader as Exercise 5 in Section 7.6.5.
</div>
(Hint: Use a contradiction argument... )


> 🇨🇳 补充 (29) 康托尔的精神：数学的无限不是混沌，而是可以通过精确推理来理解的对象。(30) 第 7 章完成！下一章：组合数学与计数。


Characterizing a Set as Infinite To define infinite sets, we first defined finite sets, and then declared any set to be infinite if it is not finite. The following thereom shows us that we could have defined infinite in a different way. Namely, we can say a set is infinite if and only if we can find a bijection to a proper subset of itself. First, let's state and prove this helpful lemma; we will need it in the proof of the theorem below.
<div class="def-theorem" markdown>
**$Lemma 7.6.30. Let A be any set. Then, A is infinite \Leftrightarrow there exists B \subset A$**
</div>
such that B is countably infinite.
<div class="def-proof" markdown>
*Proof.* $The \Leftarrow= direction is obvious. If A is bigger than some infinite set, it is$
</div>
also infinite. The =$\Rightarrow d$irection is more interesting. Suppose A is infinite. Let $\star$$\in A$ be some special element. We will take it out of consideration and construct a set B that is countably infinite and does not contain \staras an element. This will guarantee B \subset A, with B \neq A. Consider A1 = A -{\star}. This set is also infinite, so we can choose some element b1 \in A1. Consider A2 = A1 -{b1} = A -{\star, b1}. This set is also infinite, so we can choose some element b2 \in A2. Consider A3 = A2 -{b2} = A -{\star, b1, b2}. This set is also infinite, so we can choose some element b3 $\in A$3. We can continue this process forever. Define B = {b1, b2, b3,... }. (Note: we are "passing to a limit" here, but this is acceptable because we are not using this to "preserve" any properties of B. We are merely constructing the object B.) Notice that B is countably infinite because there is an obvious bijection with N. With this lemma in hand, we can state and prove the next result:
<div class="def-theorem" markdown>
**Theorem 7.6.31. Let A be any set. Then, A is infinite**
</div>
$\Leftrightarrow$ there exists B \subset A such that there exists f : A $\to B$ that is bijective.
<div class="def-proof" markdown>
*Proof.* ( =$\Rightarrow$) Suppose A is infinite. We must identify a proper subset B $\subset A$
</div>
and a bijection f : A $\to B$. Since A \neq \emptyset, take any x \in A. Consider B = A -{x}. Notice B \subset A. We want to show there is a bijection f : A \to B. By Lemma 7.6.30 above, we know we can find a countably infinite strict subset C $\subset B$. (Note: A is infinite, so B = A -{x} is also infinite, since we only removed one element. If you need more convincing, AFSOC B is finite, so it has some size; what, then, is the size of A?) Since C is countably infinite, we can list the elements of C as {y1, y2, y3,... }.


> 🇨🇳 补充 (31) 基数为等价关系——"等势"将全体集合分成不同的基数类。(32) 每个基数类的"大小"由一个基数数表示。(33) $\aleph_0 < \mathfrak{c} < 2^{\mathfrak{c}} < \ldots$ 构成无限增长的链。


(Note: The idea is that there exists some bijection g : N $\to \mathbb{C}$, so we can let y1 = g(1) and y2 = g(2) and so on.) Define f : A \to B by \forall y \in A. f(y) =    y if y \neq yi for all i $\in \mathbb{N}$ and y \neq x y1 if y = x yi+1 if y = yi for some i $\in \mathbb{N}$ This is a bijection because we can identify its inverse function F : B \to A, which is \forall z \in B. F(z) =      z if z \neq yi for every i $\in \mathbb{N}$ x if z = y1 yi-1 if z = yi for some i $\in \mathbb{N}$ -{1} We will leave it as an exercise for the reader to verify that F = f -$1. (Draw a picture to intuitively convince yourself, at the very least.) (\Leftarrow=) This direction claims that infinite sets are the only sets that have this property. We will prove this claim by contrapositive. That is, we will show that any finite set cannot have a bijection to a proper subset. Suppose A is finite. This means it has a (unique) size, say n \in \mathbb{N}$. Consider an arbitrary proper subset B \subset A. WWTS there cannot exist a bijection from A to B. AFSOC there is such a bijection f : A \to B. Since B is finite and B \subset A, B has some size m < n. Thus, there is a bijection g : B \to[m]. Composing these bijections, we get a bijection h : A \to[m]. Thus, |A| = n and |A| $= m, so m = n. However, we also know m < n. This is a contradiction. \times\times\times\times (Note$: we can also make this argument via the Pigeonhole Principle, which we haven't yet discussed but will soon. Essentially, we can't have a bijection p : [n] $\to$[m] when n > m because there are "too few boxes" in which to stuff n "pigeons".) In the context of solving a problem, perhaps you'll want to argue that some set is infinite. Rather than proving that you cannot possibly find a bijection to any finite set, considering using this theorem! If you can identify a proper subset and a bijection, then you have accomplished your goal, with the help of this result.
### 7.6.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory!


> 🇨🇳 补充 (34) Cantor 的名言："数学的本质是自由。"(35) 回顾从第 1 章到第 7 章的旅程——从"什么是数学"到"无限有多少种"。


(1) When is a set finite? (2) What are two ways to characterize when a set is infinite? (3) What is the difference between countably and uncountably infinite? Give two examples of each type. (4) Given two countably infinite sets, A and B, what set operations can we perform on them that are guaranteed to yield a countably infinite set? Might any set operations on them yield a finite set? $(5) Is \mathbb{R} \times \mathbb{N} countably or uncountably infinite$? What about R -N? Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Prove Proposition 7.6.9. That is, prove: If A and B are finite sets, then |A \cup B| = |A| + |B| -|A \cap B| (2) Prove Corollary 7.6.10. That is, prove: If A1,..., An are finite and pairwise-disjoint, then |A1 \cup \cdot \cdot \cdot \cup An| = |A1| + \cdot \cdot \cdot + |An| (3) Find the flaw in the following "spoof" that R is countably infinite: Let S $\subseteq \mathbb{R}$ be the set defined by S = {y $\in \mathbb{R}$ | 0 $\leq y$ < 1}. For every x $\in S$, define the set Ax = {x + z | z $\in \mathbb{Z}$}. (For example, A1/2 = {..., -3 2, -1 2, 1 2, 3 2,... }.) Since Z is countably infinite, each set Ax is countably infinite. Also, notice that R = [ x$\in S$ Ax This is a union of countably infinite sets, so R is also countably infinite. Be sure to point out any particular step that is incorrect, as well as why that step is incorrect. Ideally, you should point out why the ultimate conclusion of the spoof is incorrect, but without just explicitly stating "R is uncountable because we proved that". Why is the incorrect step a misuse of a result, and why is the conclusion of that particular step invalid?


> 🇨🇳 补充 (36) 基数理论是现代数学的基石——没有它，测度论、拓扑、分析学都无从谈起。(37) 对角线法是数学中最优雅的论证之一——简单到令人惊讶。


(4) For each of the following desired situations, provide an example or state that it is impossible. For example, if the situation were "Finite sets A and B such that A $\cup B$ has size 4", an answer might be "Consider A = {1, 2} and B = {3, 4}." If the situation were, "For every x $\in \mathbb{N}$, an infinite set Sx, such that [ x$\in \mathbb{N}$ Sx is finite", the answer would be "Impossible". There is no need to prove your answers here; a good example should suffice. (a) An uncountably infinite set A and a countably infinite set B such that A \cap B is finite. (b) Uncountably infinite sets C and D such that C-D is countably infinite. (c) Uncountably infinite sets E and F such that E -F is uncountably infinite. (d) For every x $\in \mathbb{N}$, a countably infinite set Sx, such that [ x$\in \mathbb{N}$ Sx is uncountably infinite. (e) For every y $\in \mathbb{R}$, a countably infinite set Ty, such that [ y$\in \mathbb{R}$ Ty is countably infinite. (5) Prove Lemma 7.6.29. That is, suppose A is uncountably infinite and B $\subseteq A$ is countably infinite; prove that A -B is uncountably infinite. Use this result to explain why the set of irrational real numbers is uncountably infinite.
## 7.7 Summary Now, we have fully explored functions and their related properties! We saw that a function is just a relation with a particular property. This desired property corresponds to how we usually think of a function as having an "output" for every possible "input". We formalized these notions mathematically by defining terminology like domain, codomain, and image. Further properties of functions include injectivity and surjectivity. We saw many examples and non-examples of functions with these properties, and discussed how to prove/disprove these properties, relating back to our logical proof techniques. The notion of a bijection has been particularly helpful and powerful. We related this to the notion of an inverse function. Specifically, we saw and proved that a function is bijective if and only if it has an inverse! This made for an important result later on when we discussed cardinality, where "the bijection is king". The notion of "pairing offelements" helped us make sense of some of the more wild and counter-intuitive results about the "sizes of sets". We characterized infinite sets as either countably infinite or uncountably infinite. However, we also proved the historically significant result that is Cantor's


> 🇨🇳 补充 (38) 基数与计算——可数涉及"可枚举"，不可数涉及"不可枚举"——这直接联系可计算性理论。(39) Godel 不完备性的证明也使用了类似对角线的技术。


Theorem, which shows that there are, in fact, infinitely-many cardinalities! For
our purposes here, it was sufficient to distinguish these two types of infinite sets. We saw several examples of each, and proved some theorems about how to create sets of specific cardinalities from others. Ultimately, we find these results intriguing and mathematically instructive. From now on, though, we will be focusing on finite sets only.
## 7.8 Chapter Exercises These problems incorporate all of the material covered in this chapter, as well as any previous material we've seen, and possibly some assumed mathematical knowledge. We don't expect you to work through all of these, of course, but the more you work on, the more you will learn! Remember that you can't truly learn mathematics without doing mathematics. Get your hands dirty working on a problem. Read a few statements and walk around thinking about them. Try to write a proof and show it to a friend, and see if they're convinced. Keep practicing your ability to take your thoughts and write them out in a clear, precise, and logical way. Write a proof and then edit it, to make it better. Most of all, just keep doing mathematics! Short-answer problems, that only require an explanation or stated answer without a rigorous proof, have been marked with a }. Particularly challenging problems have been marked with a $\star$. Problem 7.8.1. For each of the following "rules" and proposed domains and codomains, determine whether the "rule" defines a well-defined function. Explain your answer using examples, if necessary. (a) Let a : Z -{1} $\to \mathbb{R}$ be defined by a(x) = x2 x -1. (b) Let b : Q $\to \mathbb{Q}$ be defined by b(x) = p |x|. (c) Let c : Z $\to \mathbb{Z}$ be defined on every input x $\in \mathbb{Z}$ by outputting an s $\in \mathbb{Z}$ such that x \equivs mod 3. (d) Let d : N $\to \mathbb{N}$ be defined by d(x) = j x


> 🇨🇳 补充 (40) 基数运算与算术不同——$\aleph_0 + \aleph_0 = \aleph_0$（不是 $2\aleph_0$！）(41) $\aleph_0 \cdot \aleph_0 = \aleph_0$——无限算术有чиные规则。


k. (e) Let e : P(N) $\to P$(Z) be defined by taking in a set of natural numbers and outputting the set of all integer multiples of the least element of that set. Problem 7.8.2. Consider the sets R3 = {(x, y, z) | x, y, z $\in \mathbb{R}$} and R2 = {(a, b) | a, b $\in \mathbb{R}$}. Consider the function f : R3 $\to \mathbb{R}$2 defined by f(x, y, z) = (xz, yz). Is f injective? Surjective? Prove your claims.


> 🇨🇳 补充 (42) 函数是连接集合的桥梁——通过函数我们定义了像、原像、单射、满射、基数。第 7 章将这一切串联起来了。


Problem 7.8.3. Define f : R $\to \mathbb{R}$ and g : R $\to \mathbb{R}$ by f(x) = x + 1 and g(x) = x2 + x. Find formulas for the compositions f \circ g and g \circ f. (Notice that they are different.) Prove that neither of those compositions is injective. Problem 7.8.4. Let f : Z $\to \mathbb{Z}$ be given by f(x) = 2x -3. Let g : Z $\to \mathbb{N}$ be given by g(z) = |z| + 4. What is the domain of g \circ f? What is the codomain? Write down a rule that defines g \circ f. Is this function injective? Surjective? What is Img \circ f(Z)? $Prove your claims. Problem 7.8.5. Each of the following rules defines a function from \mathbb{N} \times \mathbb{N} \to \mathbb{Z}$. For each, determine whether the resulting function is injective or surjective, or both, or neither. Prove your claims. (a) f1(a, b) = a -b (b) f2(a, b) = 2a + 3b (c) f3(a, b) = a (d) f4(a, b) = a2 -b2 (e) f5(a, b) = 2a \cdot 3b Problem 7.8.6. Define functions f1, f2, f3, f4 with domain N and codomain P(N) with the following properties, or else explain why the desired properties are not possible to achieve. • f1 is injective and not surjective • f2 is neither injective nor surjective • f3 is surjective and not injective • f4 is bijective Problem 7.8.7. Consider the function f : Z \times Z $\to \mathbb{Z} \times \mathbb{Z} defined by \forall(x, y) \in \mathbb{Z} \times \mathbb{Z}. f(x, y) = (y + 1, 3$ -x) Find a function F that is the inverse of f, and prove that it is. What does this tell you about the function f? Problem 7.8.8. Define the set S = {x $\in \mathbb{R}$ | 0 < x < 1}. Define the function g : S $\to \mathbb{R}$ by g(x) = 2x -1 2x(1 -x)


> 🇨🇳 补充 (43) 基数比较关系中还是偏序——$|A| \leq |B|$ 或 $|B| \leq |A|$ 必有一个成立（需要选择公理）。


Prove that Img(S) = R. (Hint: You'll need to use the Quadratic Formula.) Problem 7.8.9. Suppose f : A $\to B$ and g : B $\to \mathbb{C}$ are functions. (a) Suppose f, g are surjections. Prove that g \circ f : A $\to \mathbb{C}$ is also a surjection. (b) Suppose f, g are injections. Prove that g \circ f : A $\to \mathbb{C}$ is also an injection. (c) Suppose f, g are bijections. Prove that g \circ f : A $\to \mathbb{C}$ is also a bijection. Problem 7.8.10. Suppose f : A \to B and g : B $\to \mathbb{C}$ are bijections. Define h : A $\to \mathbb{C}$ to be h = g \circ f. Prove that h is invertible and that h-1 = f -1 \circ g-1. (Hint: Use the Associativity of Function Composition.) Problem 7.8.11. Let f : A \to B and g : B $\to \mathbb{C}$ be functions. Let X \subseteq A. Prove that Img \circ f(X) = Img(Imf(X)). Problem 7.8.12. Let f : A \to B be a bijection, so f -1 : B \to A is a function. Let X \subseteq A. Prove that Imf(X) = PreImf -1(X). Problem 7.8.13. Let A, B be sets and let f : A \to B be a function. Suppose X, Y \subseteq A. (a) Is it necessarily true that the following equality holds? Imf(X \cup Y ) = Imf(X) \cup Imf(Y ) State your claim and prove it. (b) Is it necessarily true that the following equality holds? Imf(X \cap Y ) = Imf(X) \cap Imf(Y ) State your claim and prove it. Problem 7.8.14. Let f : A \to B be a function. Define the relation ∼on B by saying, for any x, y \in B, x ∼$y \Leftrightarrow P$reImf({x}) = PreImf({y}) Explain why ∼is an equivalence relation. What are the equivalence classes? Supposing that f is surjective, what are the equivalence classes? Problem 7.8.15. Let f : A \to B be a function. Define the relation \approx on A by saying, for any x, y \in A, x $\approx y \Leftrightarrow f$(x) = f(y)


> 🇨🇳 补充 (44) 没有选择公理时，可能出现"不可比"的集合——两个集合互不嵌入。这是集合论精妙的角落。


Is $\approx a$n equivalence relation? If so, prove it, and describe the equivalence classes. If not, provide a counterexample. Now, suppose that f is an injection. Is \approx an equivalence relation? If so, prove it, and describe the equivalence classes. If not, provide a counterexample. Problem 7.8.16. Let f : A \to B be a function, and let X, Y \subseteq A. Consider the claim that Imf(X) \cap Imf(Y ) \subseteq Imf(X \cap Y ). What is wrong with the following "spoof" of that claim? Let z \in Imf(X) \cap Imf(Y ). Since z \in Imf(X), this means \exists a \in X such that f(a) = z. Since z \in Imf(Y ), this means \exists a \in Y such that f(a) = z. Since a \in X and a \in Y, we this means a \in X \cap Y. Since f(a) = z, this means z \in Imf(X \cap Y ). Provide a counterexample to show that the claim is, in fact, False. Problem 7.8.17. Prove/disprove whether P(N) and P(Z) have the same cardinality. Problem 7.8.18. Fix an arbitrary n $\in \mathbb{N}$. Consider the set [n] = {1, 2, 3,..., n}. Let E be the set of subsets of [n] that have an even number of elements (like \emptyset or {1, 4}), and let O be the set of subsets of [n] that have an odd number of elements (like {5} or {1, 2, 3}). Define a function p : E \to O that is a bijection, and prove that it is a bijection. (Hint: Write out some small cases, where n = 1 and n = 2 and n = 3. Then try to generalize.) Problem 7.8.19. Prove Lemma 7.6.16. Hint: Try using a similar idea to our proof of Theorem 7.6.7: use the size of B to "bump up" the bijection between A and N by a certain amount. Problem 7.8.20. Prove Corollary 7.6.19. That is, suppose A and B are countably infinite sets; prove that A \cup B is countably infinite by applying Lemma 7.6.18 to appropriately-chosen sets. Problem 7.8.21. Look back at Example 7.6.13. There, we defined f : N\timesN $\to \mathbb{N} by setting \forall(x, y) \in \mathbb{N} \times \mathbb{N}. f(x, y) = 2x$-1(2y -1) Prove that f is injective. Problem 7.8.22. Prove Corollary 7.6.21. That is, suppose we have finitely-many sets---A1, A2,..., An---where each set is countably infinite; prove that A1 \cup A2 $\cup \cdot \cdot \cdot \cup An and A1 \times A2 \times \cdot \cdot \cdot \times An are both also countably infinite.$


> 🇨🇳 补充 (45) 康托尔的工作在他生前未能完全被接受——Kronecker 等人激烈反对。但历史证明康托尔是对的。


Problem 7.8.23. Consider the set A, defined by A = {(a, b) $\in \mathbb{N} \times \mathbb{N}$ | a $\leq b$} Prove that A is countably infinite in two ways: (1) By writing A as a union of sets and citing a result. (2) By finding an explicit bijection between A and a countable set of your choosing. Problem 7.8.24. Define g : $N \times \mathbb{N} \to \mathbb{N}$ by setting g : $N \times \mathbb{N} \to \mathbb{N} \forall(x, y) \in \mathbb{N} \times \mathbb{N}. g(x, y) = (x + y)2 + x Prove that g is (a) injective and (b) not surjective. Problem 7.8.25. Let A, B, \mathbb{C} be sets. Let f$ : A $\to B$ and g : B $\to \mathbb{C}$ and h : B $\to \mathbb{C}$ be functions. (a) Suppose g = h. Is it necessarily True that g \circ f = h \circ f? Prove or disprove this claim. (b) Suppose g \circ f = h \circ f. Is it necessarily True that g = h? Prove or disprove this claim. Problem 7.8.26. Let A, B be finite sets, with |A| = |B| = n. Suppose f : A $\to B is a function. Prove that f is injective \Leftrightarrow f$ is surjective Problem 7.8.27. Consider the following claim: Suppose f : A \to B and g : B $\to \mathbb{C}$ are functions. Suppose g \circ f : A $\to \mathbb{C}$ is injective. Then g is also injective. What is wrong with the following "spoof" of this claim? Suppose g \circ f is an injection. We want to show g is an injection. Let x, y \in B be given. Suppose g(x) = g(y). We know \exists a, b $\in A$ such that f(a) = x and f(b) = y. Since g is a well-defined function, this means g(f(a)) = g(x) and g(f(b)) = g(y). Since g \circ f is injective and g(f(a)) = g(f(b)), this means a = b. Since f is a well-defined function, then f(a) = f(b). This means x = y. Thus, g is injective.


> 🇨🇳 补充 (46) 总结基数部分：核心是有限/可数/不可数三级分类+三种核心工具（对角线法、CSB定理、Cantor定理）。


Also, find a counterexample that shows the claim's conclusion is incorrect. Problem 7.8.28. Let a, b $\in \mathbb{R}$ be arbitrary and fixed. Suppose a2 + b2 \neq 0. Consider the function f : R \times R $\to \mathbb{R} \times \mathbb{R} defined by \forall(x, y) \in \mathbb{R} \times \mathbb{R}. f(x, y) = (ax$ -by, bx + ay) Prove that f is a bijection by finding its inverse and proving that inverse is correct. Problem 7.8.29. Let A and B be finite sets and suppose |A| = |B|. Suppose f : A \to B is a function that is injective. Prove that f must also necessarily be surjective by showing imf(A) = B. Problem 7.8.30. Let k $\in \mathbb{N}$ -{1} be given. Define S1 = {X \in P( [k] ) | k \notin X} and S2 = {X \in P( [k] ) | k \in X} (a) Prove that the sets S1 and S2 form a partition of P( [k] ). (b) Define a function f1 : S1 \to P( [k -1] ) that is a bijection and prove that it is. (c) Define a function f2 : S2 \to P( [k -1] ) that is a bijection and prove that it is. (d) Use what you proved in (a) and (b) and (c) to write an induction proof that P( [n] ) has 2n elements, for every n $\in \mathbb{N}$.
Note: Because of the restriction k $\geq$2 above, make n = 1 your base case, use
n = k $\geq$1 in your Induction Hypothesis, and prove the claim for n = k + 1 in the Induction Step. Problem 7.8.31. Let A, B, C, D be sets, and suppose A \cap B = C \cap D = \emptyset. Suppose f : A \to B and g : C \to D are bijections. Define the piece-wise function h : A \cup B $\to \mathbb{C} \cup D by setting \forall x \in A \cup B$. h(x) = ( f(x) if x \in A g(x) if x \in B) Explain why h is a well-defined function. Then, prove it is a bijection. Problem 7.8.32. In this problem, you will prove that whenever A and B are finite with |A| = a and |B| = b, it follows that |A \times B| = ab. This will be structured as a "double induction" proof on the two variables a, b $\in \mathbb{N}. (a) Show that [1] \times [1] = 1. (This is very, very easy, but necessary.)$


> 🇨🇳 补充 (47) 本节最后提醒：记住哪些集合是可数的（$\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{N}^k$），哪些是不可数的（$\mathbb{R}, \mathcal{P}(\mathbb{N}), \{0,1\}^\mathbb{N}$）。


(b) Suppose n $\in \mathbb{N} and [1] \times [n] = n. Show that [1] \times [n + 1] = n + 1. (c) Explain why (a) and (b) have shown that \forall n \in \mathbb{N}. [1] \times [n] = n. (d) Suppose k \in \mathbb{N} and suppose \forall n \in \mathbb{N}. [k] \times [n] = kn. Show that \forall n \in \mathbb{N}. [k + 1] \times [n] = (k + 1)n. (e) Explain why (c) and (d) have shown that \forall k, n \in \mathbb{N}. [k] \times [n] = kn. (f) Explain why (e) proves the result stated in the problem description above. Problem 7.8.33. Let S be the set of all infinite binary strings. (That is, elements of S are infinitely-long strings of 0s and 1s.) Find a bijection between S and P(N). Use this to prove that S is uncountably infinite. Problem 7.8.34. For each of the following sets, you are given its cardinality. Prove that the given cardinality is correct by finding a bijection to a relevant set and/or citing a result. (Hint$: If you don't use some kind of inductive argument, your proof might not be rigorous enough... ) (a) A is the set of all functions from N to N. Show that A is uncountably infinite. (Hint: Compare A with the set S of all functions from N to {1, 2}. Can you explain why S is uncountably infinite? What does this say about A?... ) (b) B is the set of all functions from N to N with the additional property that \forall x $\in \mathbb{N}$. f(x + 1) = f(x) + 1 Show that B is countably infinite. (c) C is the set of all functions from N to N with the additional properties that \forall x $\in \mathbb{N}. f(x + 1) = f(x) + 1 f(1) = 42 Show that \mathbb{C} is finite, and has only one element. Problem 7.8.35. Look back at Example 7.6.14 where we argued (informally) that \mathbb{N} \times \mathbb{N} is countably infinite by depicting the set as a lattice of points and describing a countably infinite path that covers all its points. Formalize this argument by defining a function f$ : N\timesN $\to \mathbb{N}$ (or vice-versa) that achieves the path we described (or a similar one) and proving it is a bijection. Problem 7.8.36. Prove Corollary 7.6.23. That is prove, that a countably infinite union of finite sets that are pairwise-disjoint is countably infinite.


> 🇨🇳 补充 (48) 无限集的直觉反例：一条更长的线段不比短线段有"更多点"——它们等势！$|(0,1)| = |(0,100)|$。


Problem 7.8.37.. Consider Theorem 7.6.22, which states that a countably infinite union of countably infinite sets is also countably infinite. In our proof, we only considered the case where the given sets were pairwise-disjoint. In this problem, you should prove the general case, where the sets are not necessarily pairwise-disjoint. (Hint: $Consider the functions we used in our proof. Can you adapt them to find a surjection from \mathbb{N} \times \mathbb{N} to the union of the sets$?) Problem 7.8.38. Consider the set S of all infinite binary strings. We proved that S is uncountably infinite before. Consider the set T \subseteq S that is the set of all infinite binary strings with only finitely many 1s. In this problem, you will prove that T is, in fact, countably infinite! (a) Consider the set Nk of all ordered k-tuples of natural numbers. (Note: $N1 = \mathbb{N} and N2 = \mathbb{N} \times \mathbb{N}.) Provide an inductive argument that shows that Nk is countably infinite for every k \in \mathbb{N}$. (Hint: This should be a pretty short proof. You should appeal to a result proven in lecture about Cartesian products of countably infinite sets.) (b) For every k $\in \mathbb{N}, let Tk \subseteq T$ be the set of all infinite binary strings with exactly k 1s. Find a bijective (or, at least, injective) function from Tk to Nk. Explain why your function is well-defined and is a bijection (or injection). (c) Use (b) to deduce that Tk is countably infinite. (Careful: If you found only an injection, you should also explain why Tk is not finite.) (d) Express T as a union of sets and deduce that T is countably infinite. (Hint: You'll need to apply an important Theorem from lecture.) (Side note: Think about the consequences of this result. With a simple bijection, you can deduce that the set of all infinite binary strings with only finitely many 0s is also countably infinite. This means that the reason S, the set of all infinite binary strings, is uncountably infinite is completely tied to the set of strings with both infinitely many 1s and 0s. That set alone is big enough to make S uncountable! Problem 7.8.39. (a) Let n $\in \mathbb{N}$. Consider the set S = {f : [n] \to[n] | f is a bijection } Show that S is closed under composition; that is, prove that \forall f, g \in S. f \circ g $\in S$ (Hint: Cite a problem from this section of chapter exercises.)


> 🇨🇳 补充 (49) 这是 Galileo 最早注意到的无限的反直觉性质——无限集可以与自己的真子集等势，这在有限集绝不可能。


(b) Consider the set T = n f : N $\to \mathbb{N}$ | f is a bijection and {i $\in \mathbb{N}$ | f(i) \neq i} is finite o Show that T is also closed under composition. (c) Show that T is closed under inverses; that is, prove that \forall f \in T. f -$1 exists \wedgef$ -1 \in T (d) Consider the set U = f : N $\to \mathbb{N}$ | f is a bijection


> 🇨🇳 补充 (50) 最后的回顾：第 7 章的5节——定义$\to$像/原像$\to$性质$\to$复合与逆$\to$基数——形成了一条完整的逻辑链。


Prove that U is closed under inverses. (e) Prove that $\forall f \in T. \forall g \in U$ -T. {f \circ g $\notin T \wedgeg$ \circ f $\notin T$ } (f) Find a counterexample to show that U -T is not closed under composition. (g) Furthermore, given A $\subseteq \mathbb{N}$ with A finite, find functions f, g \in U -T such that {i $\in \mathbb{N}$ | (f \circ g)(i) \neq i} = A (h) What are the cardinalities of S, T, U? If your answer is "finite", also state the size. If your answer is "infinite", also state whether it is countable or uncountable and prove your claim by finding a bijection to an appropriate set or citing a relevant result.
## 7.9 Lookahead In the next chapter, we will study combinatorics, the mathematical branch of "counting things". We saw in the section on cardinality that many results about finite sets seemed rather intuitive. When we study combinatorics, we will be describing the elements of a set by characterizing what properties they have, rathern than simply stating them all or listing them. This will actually make it quite interesting (and sometimes very difficult!) to determine just how many elements we have described. Combinatorics is the study of techniques to determine the number of elements of a set with certain properties. We will state and prove some fundamental principles of counting (appealing to results from this chapter, in fact) and use them to build more advanced techniques and solve some interesting problems.


> 🇨🇳 补充 (51) 函数的定义（第 7.2 节）$\to$ 通过像/原像分析函数行为（7.3）\to 通过单射/满射刻画函数类型（7.4）\to 复合与逆的操作（7.5）$\to$ 用双射定义基数（7.6）。


