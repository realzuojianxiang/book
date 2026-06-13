---
title: Images and Pre-images
---

# Images and Pre-images

7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 像与原像（Images and Preimages）本节定义函数的像和原像，讨论其性质，并给出相关证明方法。


Definition
<div class="def-definition" markdown>
**Definition 7.3.1. Let A, B be sets and let f : A $\to B$ be a function.**
</div>
Let X $\subseteq A$. The image of X under the function f is written and defined as Imf(X) = {b \in B | \exists a \in X. f(a) = b} That is, the image of X under f is the set of all "outputs" that come from "inputs" in the set X. An equivalent way of writing this is Imf(X) = {f(a) | a \in X} (We will sometimes abbreviate the notation as just Im(X), when the function is clearly identified and unambiguous, and consequently refer to the set as just "the image of X", instead of "the image of X under f".) When we say the image of f, we mean the image of the entire domain, i.e. Imf(A). Notice that this is defined for any subset of the domain, X \subseteq A, so we can talk about the image of any "piece" of the domain, or all of it. We will see some examples now---and exercises later---that consider strict subsets X \subset A, as well as A itself. One Observation Notice that Imf(A) $\subseteq B$ no matter what f and A and B are. This follows by definition, since we used set-builder notation to define the image via elements of B. In the next section, we will explore what happens when Imf(A) = B. For now, let's practice identifying the images of certain functions. In some cases, we will be provided with a function and its image and asked to verify this claim, but in other cases, we will need to develop some techniques to figure out what the image is in the first place!
Examples
Example 7.3.2. Define a function g : A $\to B$ by setting A = {a, b, c, d, e} and
B = {1, 2, 3, 4, 5, 6} and g = {(a, 2), (b, 3)(c, 3), (d, 1), (e, 6)} Define X1 = {a, b, c} and X2 = {a, c, e} and X3 = {c, d, e}. You might notice that this is the same function we defined in the schematic diagram in the last section! Let's see that diagram again, because it can help us identify the images in the following list.


> 🇨🇳 **像（Image）** 设 $f: A \to B$ 是函数，$X \subseteq A$。$X$ 在 $f$ 下的像定义为 $\text{Im}_f(X) = \{f(x) \mid x \in X\} = \{b \in B \mid \exists x \in X.\, f(x) = b\}$。即所有 $X$ 中元素经 $f$ 映射到的输出集合。


g : A $\to B$ A B (1) Img({a}) = {2} This is because g(a) = 2. Notice the use of set brackets. We always find the image of a set, so writing Img(a) would be incorrect. (2) Img({b, c}) = {3} This is because g(b) = g(c) = 3. (3) Img(X1) = {2, 3} This is because g(b) = g(c) = 3 and g(a) = 2. (4) Img(X2) = {2, 3, 6} This is because g(a) = 2 and g(c) = 3 and g(e) = 6. (5) Img(X3) = {1, 3, 6} This is because g(c) = 3 and g(d) = 1 and g(e) = 6. (6) Img(A) = {1, 2, 3, 6} Looking at the set B in the schematic diagram, we see that these are the only values that are "hit" by the function. Notice 4, 5 \in B but 4, 5 \notin Img(A), so Img(A) $\subset B$ (a proper subset).
Example 7.3.3. Consider the temperatures (in degrees Celsius) where water is
in its liquid state. Specifically, define the set C = {$x \in \mathbb{R}$ | 0 < x < 100} and define the function F : C $\to $\mathbb{R}$ by \forall c \in \mathbb{C}$. F(c) = 9 5c + 32 What is ImF (C)? What does it represent? To approach questions like these, we must (a) identify a claim for what ImF (C) is by defining a set, and then (b) prove that the set we defined is actually equal


> 🇨🇳 **原像（Preimage）** 设 $f: A \to B$ 是函数，$Z \subseteq B$。$Z$ 在 $f$ 下的原像定义为 $\text{PreIm}_f(Z) = \{a \in A \mid f(a) \in $\mathbb{Z}$\}$。即所有输出落入 $Z$ 中的输入集合。


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 **记号** 像有时写作 $f(X)$，原像写作 $f^{-1}(Z)$。但要注意：$f^{-1}$ 在此只是记号，不意味着 $f$ 有逆函数！


to ImF (C), in the sense of sets. This means we will use a double-containment argument!
Solution: Define S = {$y \in \mathbb{R}$ | 32 < y < 212}. (Notice that this represent the
set of temperatures (in degrees Fahrenheit) where water is in its liquid state.) We claim S = ImF (C). It is hard to give advice about how to come up with claims like this, in general. Most often, this relies on some playing around with the function and testing some values, and perhaps some insight about some other properties of the function. In this specific case, we notice that this function is increasing; that is, if we have two input values with c1 < c2, then we know that F(c1) < F(c2). We can glean this information from the graph of the function (see above) and/or recognizing it is a linear polynomial. Accordingly, to identify the image, we just have to consider the smallest and largest inputs and identify their outputs. (Again, we can glean this information from a graph.) We find that F(0) = 0 + 32 = 32 and F(100) = 900


> 🇨🇳 **特例** $\text{Im}_f(A)$ 是 $f$ 的值域（Range），$B$ 是陪域（Codomain）。f 是满射当且仅当 $\text{Im}_f(A) = B$。$\text{PreIm}_f(\{b\})$ 是 $b$ 的纤维（Fiber）。


+ 32 = 212 From this, we defined the set S. (Also, notice that we had to use "<" in the inequality because, in fact, 0 $\notin \mathbb{C}$, the domain!) We also give this set a name so that we can refer to it later without implicitly claiming, already, that it is the image. This is a somewhat subtle distinction, but an important one! Now, let's prove our claim.
<div class="def-proof" markdown>
*Proof.* First, we'll prove ImF (C) $\subseteq S$. (In other words, we'll prove that every
</div>
output of the function F actually satisfies the inequality in the definition of S.) (To do this we will start with an arbitrary element of ImF (C), and appeal to the defintion of image to bring an element of the domain into play.) Let y $\in I$mF (C) be arbitrary and fixed. By the definition of image, this means \exists x $\in \mathbb{C}$ such that F(x) = y. Let such an x be given. By the definition of C, we know 0 < x < 100. By the definition of F, we know


> 🇨🇳 **基本性质** (1) $\text{Im}_f(\emptyset) = \emptyset, \text{PreIm}_f(\emptyset) = \emptyset$。(2) $X \subseteq Y \subseteq A \Rightarrow \text{Im}_f(X) \subseteq \text{Im}_f(Y)$。(3) $Z \subseteq W \subseteq B \Rightarrow \text{PreIm}_f(Z) \subseteq \text{PreIm}_f(W)$。


F(x) = 9 5x + 32. Since multiplying by a positive number and adding to both sides preserves inequalities, we can deduce that


> 🇨🇳 **像与原像的关系** (1) 对任意 $X \subseteq A$，$X \subseteq \text{PreIm}_f(\text{Im}_f(X))$，等号成立当且仅当 $f$ 在 $X$ 上单射。(2) 对任意 $Z \subseteq B$，$\text{Im}_f(\text{PreIm}_f(Z)) \subseteq \mathbb{Z}$，等号成立当且仅当 $Z \subseteq \text{Im}_f(A)$。


5 $\cdot$ 0 + 32 < F(x) < 9 5 \cdot 100 + 32 and, simplifying, this tells u 32 < F(x) < 212 Thus, F(x) \in S, i.e y \in S. Therefore, ImF (C) \subseteq S. Second, we'll prove S \subseteq ImF (C). (In other words, we'll prove that every element of S is actually "achieved" by the function F somehow. This amounts to proving an existential claim, i.e. that some element of the domain exists.) Let s \in S be arbitrary and fixed. By the definition of S, we know that s $\in \mathbb{R}$ and 32 < s < 212. We need to prove that \exists c $\in \mathbb{C}$. F(c) = s. (By doing some scratch work on the side, that you can work through on your own, we came up with the following idea. Just set an expression equal to s and solve for c... ) Define c = 5 9(s -32). Let's show c $\in \mathbb{C}$. By using the information we have about s and manipulating the inequalities, we observe that 32 < s < 212 =\Rightarrow0 < s -32 < 180 =\Rightarrow0 < 5 9(s -32) < 5 9 \cdot 180 = 100 =\Rightarrow0 < c < 100 Since c $\in \mathbb{R}$, certainly, this shows that c $\in \mathbb{C}$. Next, let's show that F(c) = s. We observe that F(c) = 9 5c + 32 = 9


> 🇨🇳 **并集运算** $\text{Im}_f(X \cup Y) = \text{Im}_f(X) \cup \text{Im}_f(Y)$。推广：$\text{Im}_f(\bigcup_{i} X_i) = \bigcup_{i} \text{Im}_f(X_i)$。对原像也成立：$\text{PreIm}_f(Z \cup W) = \text{PreIm}_f(Z) \cup \text{PreIm}_f(W)$。


(5 9(s -32) ) + 32 = (s -32) + 32 = s Together, this shows that s $\in I$mF (C), as well. Thus, S $\subseteq I$mF (C). Overall, by a double-containment argument, we conclude that S = ImF (C). The second half of our proof is certainly the harder part, and this is generally true of proofs like this. In coming up with a candidate c, we essentially have to "undo" the process that the function F does and find an input c for our given output s. In a case like this, where the function is a numerical/arithmetical operation on real numbers, the best route is to set up the desired equality, like


> 🇨🇳 **交集运算** $\text{Im}_f(X \cap Y) \subseteq \text{Im}_f(X) \cap \text{Im}_f(Y)$（等号一般不成立！除非 $f$ 单射）。对原像，等号成立：$\text{PreIm}_f(Z \cap W) = \text{PreIm}_f(Z) \cap \text{PreIm}_f(W)$。


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 **补集运算** $\text{PreIm}_f(B - Z) = A - \text{PreIm}_f(Z)$。原像与补集可交换！但像与补集一般不可交换：$\text{Im}_f(A - X)$ 与 $B - \text{Im}_f(X)$ 不一定相等。


and solve the equality for c. This function is linear, so this process only produces one such s but, in general, we might expect multiple values of s to work. Ultimately, we only need one working value to complete this part of the proof, so we can just select any one that works and use that as our claim. Sometimes, though, this makes it harder to find such a value. It all depends on the example at hand. Other times, we might be working with functions that aren't defined on sets of numbers, and we have to use some more abstract insight to come up with a candidate element. Again, this all depends on the given situation, and with practice, you'll become much better at it! Oh right, we asked what this image represents! Since the domain represented the temperatures, in degrees Celsius, at which water is a liquid, the image represents the temperatures, in degrees Fahrenheit, at which water is a liquid. Let's look at another example of proving the image of a function is a particular set.
Example 7.3.4. Define f : $\mathbb{R} \to \mathbb{R}$ by
$\forall x \in \mathbb{R}$. f(x) = x2 1 + x2 Let's determine the image, Imf(R), and prove our claim! Here, again, we must use some outside strategies and intuition to identify the image first. Using some techniques from calculus or algebra, we could plot the graph of this function and try to guess the image. Try that if you'd like. You'll end up with this graph: We can also recognize that the denominator is greater than the numerator and so, as x gets larger and larger, those two quantities get closer and closer together, relatively speaking. (That is, their ratio approaches 1.) Also, both terms are nonegative, since they involve squares, so their ratio is at least 0. In any event, we can piece our observations together and make the following claim:


> 🇨🇳 **例** 设 $f: \{1,2,3\} \to \{a,b\}$，$f(1)=f(2)=a, f(3)=b$。$\text{Im}_f(\{1,2\}) = \{a\}$。$\text{PreIm}_f(\{a\}) = \{1,2\}$。$A - \text{PreIm}_f(\{a\}) = \{3\} = \text{PreIm}_f(\{b\}) = \text{PreIm}_f(B - \{a\})$ ✓。


Define the set T = {$y \in \mathbb{R}$ | 0 $\leq y$ < 1} We claim that T = Imf(R). We now follow the same type of strategy we employed in the previous example. Before we do so, let's remember that the second part of that proof---showing the claimed set is a subset of the image---was the harder part, and try to anticipate what will happen there. In that part, we will be working with an arbitrary element y $\in T$ and we will want to find an element $x \in \mathbb{R}$ that satisfies f(x) = y. To find such an x, let's set up the equality and try to solve for x: $y = x2 1 + x2 \Leftrightarrow (1 + x2)y = x2 \Leftrightarrow y$ + yx2 -$x2 = 0 \Leftrightarrow$(y -1)x2 = -$y \Leftrightarrow x$2 = y 1 -y Now what? Can we be assured y 1-$y \in \mathbb{R}$, even? Can we be assured it's nonnegative, so that there exists such an x? What about the fact that there might be two roots? Think about these potential issues and try to write your own version of this proof before reading on for ours!
<div class="def-proof" markdown>
*Proof.* First, let's prove Imf(R) $\subseteq T$.
</div>
Let y $\in I$mf(R) be arbitrary and fixed. By the definition of image, we know \exists $x \in \mathbb{R}$ such that f(x) = y. Let such an x be given. Since $x \in \mathbb{R}$, we know x2 $\geq 0$ and 0 < x2 + 1. We can then deduce that 0 <


> 🇨🇳 **求像的证明方法** 要证 $\text{Im}_f(X) = S$：先证 $\text{Im}_f(X) \subseteq S$（任取 $y \in \text{Im}_f(X)$，找 $x \in X$ 使 $f(x)=y$，推出 $y \in S$）；再证 $S \subseteq \text{Im}_f(X)$（任取 $y \in S$，构造 $x \in X$ 使 $f(x)=y$），此步较难。


x2+1. By multiplying the previous two inequalities---which we can do since all the terms are non-negative---we may deduce that 0 $\leq$ x2 1+x2. Next, we know that 0 \leq x2 < x2 + 1, so x2 1+x2 < 1, as well. (Note: why was it important to point out that x2 \geq0? What can go wrong there?) This shows that 0 \leq x2 1+x2 < 1. Since y = f(x) = x2 1+x2, this is equivalent to saying 0 \leq y < 1. Thus, y \in T, and so Imf(R) \subseteq T. Second, let's prove T \subseteq Imf(R). Let y \in T be arbitrary and fixed. This means y $\in $\mathbb{R}$ and 0 \leq y$ < 1. To show y $\in I$mf(R), as well, we must produce an x such that f(x) = y.


> 🇨🇳 **求原像的证明方法** 要证 $\text{PreIm}_f(Z) = T$：先证 $\text{PreIm}_f(Z) \subseteq T$（任取 $a \in \text{PreIm}_f(Z)$，由 $f(a) \in \mathbb{Z}$ 推出 $a \in T$）；再证 $T \subseteq \text{PreIm}_f(Z)$（任取 $x \in T$，证 $f(x) \in \mathbb{Z}$）。


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 **例** 设 $f: $\mathbb{R}$ \to $\mathbb{R}$, f(x) = x^2$。求 $\text{Im}_f(\{-1,1\}) = \{1\}$，$\text{PreIm}_f(\{1\}) = \{-1,1\}$，$\text{PreIm}_f(\{-1\}) = \emptyset$。


We claim that x = q y 1-y works. Notice that y $\geq 0$, and y < 1 implies -y > -1 so 1 -y > 0. Thus, y 1-y \geq0, and so $x \in \mathbb{R}$ is well-defined as a square root, and x belongs to the domain R. Next, notice that x2 = y 1-y, and so f(x) = x2 1 + x2 = y 1-y 1 + y 1-y = y 1-y (1-y)+y 1-y = y 1-y


> 🇨🇳 **例** 设 $f: $\mathbb{N}$ \to $\mathbb{N}$, f(n) = 2n$。$\text{Im}_f($\mathbb{N}$) = \{$偶数$\}$。$\text{PreIm}_f(\{$偶数$\}) = \mathbb{N}$。$\text{PreIm}_f(\{$奇数$\}) = \emptyset$。


1-y = y 1 -y $\cdot$ 1 -y


> 🇨🇳 **证明 $\text{PreIm}_f(Z \cap W) = \text{PreIm}_f(Z) \cap \text{PreIm}_f(W)** a \in \text{PreIm}_f(Z \cap W) \Leftrightarrow f(a) \in $\mathbb{Z}$ \cap W \Leftrightarrow f(a) \in \mathbb{Z}$ 且 $f(a) \in W \Leftrightarrow a \in \text{PreIm}_f(Z)$ 且 $a \in \text{PreIm}_f(W) \Leftrightarrow a \in \text{PreIm}_f(Z) \cap \text{PreIm}_f(W)$。


= y 1 = y This shows that y $\in I$mf(R), and so T $\subseteq I$mf(R). Overall, by a double-containment proof, we conclude that T = Imf(R). Notice how we addressed the issues discussed before the proof. Yes, two potential x values existed that would work (namely, the + and -square roots) but we only needed one, so we just picked one (the positive one) and ran with it. (Questions: What if this function was defined only on the nonnegative real numbers? What about just the negative real numbers? How might that restriction affect our choice?)
Example 7.3.5. Consider the function p : $N \times $\mathbb{N}$ \to \mathbb{N}$ defined by
$\forall(a, b) \in $\mathbb{N}$ \times $\mathbb{N}$. p(a, b) = ab + a What is Imp(N \times $\mathbb{N}$)$? This example might feel a little trickier because the domain is a Cartesian product of sets; that is, p inputs an ordered pair of natural numbers and outputs a single natural number. A good approach in a situation like this is to just start plugging in some values and seeing what happens. Consider the following table of values as a way to get started, where the left column indicates values of a, the top row indicates values of b, and the table entries are the values of p(a, b).


> 🇨🇳 **证明 $\text{Im}_f(X \cap Y) \subseteq \text{Im}_f(X) \cap \text{Im}_f(Y)$** 设 $b \in \text{Im}_f(X \cap Y)$。则 $\exists a \in X \cap Y$ 使 $f(a)=b$。由 $a \in X$ 得 $b \in \text{Im}_f(X)$，由 $a \in Y$ 得 $b \in \text{Im}_f(Y)$。故 $b \in \text{Im}_f(X) \cap \text{Im}_f(Y)$。


It looks like every natural number is "achieved" by the function p, except for 1. Specifically, look at the top row of the array of values: there are all the natural numbers except 1. Let's use this insight in the following proof.
<div class="def-proof" markdown>
*Proof.* Let V = N -${1}. We claim V = Imp(N \times $\mathbb{N}$).$
</div>
$First, we prove Imp(N \times $\mathbb{N}$) \subseteq V. Let n \in Imp(N \times $\mathbb{N}$) be arbitrary and fixed. This means n \in $\mathbb{N}$ and \exists(a, b) \in $\mathbb{N}$ \times $\mathbb{N}$ such that p(a, b) = n. Let such (a, b) be$


> 🇨🇳 **反例：$\text{Im}_f(X \cap Y) \neq \text{Im}_f(X) \cap \text{Im}_f(Y)$** 设 $f:\{1,2\} \to \{a\}$，$f(1)=f(2)=a$。$\text{Im}_f(\{1\} \cap \{2\}) = \text{Im}_f(\emptyset) = \emptyset$，但 $\text{Im}_f(\{1\}) \cap \text{Im}_f(\{2\}) = \{a\}$。


given. This means n = ab + a. Since a, b $\geq1, then ab \geq$1 and so n = ab + a \geq2. By the defintion of V, this shows that n $\in V. Thus, Imp(N \times $\mathbb{N}$) \subseteq V$. (Try to write the next half of the proof before reading on and seeing ours! ) Second, we prove V $\subseteq Imp(N \times $\mathbb{N}$). Let v \in V$ be arbitary and fixed. This means v $\in $\mathbb{N}$ and v \geq$2. Define (a, b) = (v -1, 1). Notice that v -1 \geq1, so v -1 $\in \mathbb{N}$ and thus (a, b) $\in $\mathbb{N}$ \times $\mathbb{N}$. Also, notice that p(a, b) = p(v$ -1, 1) = (v -1) \cdot 1 + 1 = v -1 + 1 = v Thus, p(a, b) = v, and so (a, b) $\in Imp(N \times $\mathbb{N}$). Therefore, V \subseteq Imp(N \times $\mathbb{N}$). By a double-containment proof, we have shown V = Imp(N \times $\mathbb{N}$).$
### 7.3.2 Proofs about Images You might have observed the following fact by playing around with some of the examples we have seen. Either way, we can make state and prove this claim by working with the definition of image. Notice that it is a claim about an arbitrary function; it holds no matter what f is!
Proposition 7.3.6. Let A, B be sets.
Let f : A $\to B$ be a function. Let S, T \subseteq A. Then, Imf(S \cap T) \subseteq Imf(S) $\cap I$mf(T)
<div class="def-proof" markdown>
*Proof.* Let z $\in Imf(S \cap T$) be arbitrary and fixed. This means $\exists a \in S \cap T$ such
</div>
that f(a) = z. Let such an a be given. Since a $\in S \cap T, we know a \in S and a \in T. Thus, z \in Imf(S) and z \in I$mf(T), by the definition of image. We deduce that z $\in Imf(S) \cap I$mf(T), by the definition of intersection. This shows the desired set containment. Why didn't we claim an equality here? It turns out that equality need not hold, in fact! That is, there exists at least one function such that the reverse containment---namely, Imf(S)$\cap Imf(T) \subseteq Imf(S\cap T$)---is False. We will provide an example of such a function below. (You should try to come up with an example of a function where this reverse containment does hold. Together, we will have shown that one cannot make a conclusion that necessarily holds about this containment!)


> 🇨🇳 **单射的刻画** 以下等价：(a) $f$ 是单射；(b) $\forall X,Y \subseteq A.\, \text{Im}_f(X \cap Y) = \text{Im}_f(X) \cap \text{Im}_f(Y)$；(c) $\forall X \subseteq A.\, X = \text{PreIm}_f(\text{Im}_f(X))$。


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 **满射的刻画** 以下等价：(a) $f$ 是满射；(b) $\forall $\mathbb{Z}$ \subseteq B.\, \text{Im}_f(\text{PreIm}_f(Z)) = \mathbb{Z}$。


We will use a schematic diagram to come up with an example with the desired properties. We will then use this to formally define a function and state its properties, pointing out how they match what will be established in our claim. We want to point out that employing this technique is perfectly valid, as long as you go back and write down a formal definition afterwards. Turning in just a schematic diagram as a "proof" is not rigorous enough, but this can certainly help guide your intuition into producing fruitful ideas for a proof! Furthermore, keep in mind that there is no need to construct the most complicated or interesting counterexample in situations like this. If you're trying to disprove a universally-quantified statement, you just need one example that works! In particular, don't feel like you need to define a function that works with numbers, using some formula. Sometimes, this will actually make your job much harder! It's typically the case that a counterexample can be made using sets with just a few (i.e. two or three) elements each.
Example 7.3.7. We claim that there exist sets A, B, S, T and a function f : A $\to$
B such that Imf(S) $\cap I$mf(T) ̸$\subseteq I$mf(S $\cap T$). Let's figure out how to construct such an example. Based on our comment above, we are going to try to make an example where the sets involve three or so elements. Let's get the process started by taking A to be {1, 2, 3} and defining f(1):


> 🇨🇳 **练习** (1) 设 $f: \{1,2,3,4\} \to \{a,b,c\}$，$f(1)=a, f(2)=b, f(3)=b, f(4)=c$。求 $\text{Im}_f(\{1,2\})$、$\text{PreIm}_f(\{b\})$、$\text{PreIm}_f(\{c\})$。


$\star$ Now, just to have a defintion in hand, let's choose S = {1, 2}. It seems like it will be more reasonable to work with 2 elements in S, so we'll make that choice. Also, it seems like we should make f(1) \neq f(2). Otherwise, Imf(S) would contain only one element, and there would have been no point in making S have two elements. So let's define f(2), as well:


> 🇨🇳 (2) 证明 $\text{PreIm}_f(Z \cup W) = \text{PreIm}_f(Z) \cup \text{PreIm}_f(W)$。(3) 证明 $\text{PreIm}_f(B-Z) = A - \text{PreIm}_f(Z)$。


$\star$ S Imf(S) Now, we need to choose T. It will be interesting to have S \cap T \neq \emptyset, but it would be hard to handle (perhaps) if T \supseteq S. So, let's say T = {2, 3}. Then, we just need to choose f(3). In considering each of these cases, look at the schematic diagram above, and imagine drawing an arrow to represent f(3). • What if f(3) = f(2) = □? In this case, Im( T) = { □}, so Imf(S)\cap Imf(T) = { □}. But Imf(S\cap T) = { □}, as well! This doesn't work. • What if f(3) is something else, like f(3) =, ? This doesn't work either! We will have Imf(S)\cap Imf(T) = { □} = Imf(S\cap T). • What if f(3) = f(1) = $\star$? It looks like this works!


> 🇨🇳 (4) 举例说明 $\text{Im}_f(A-X)$ 未必等于 $B - \text{Im}_f(X)$。(5) 证明：$f$ 单射时 $\text{Im}_f(X \cap Y) = \text{Im}_f(X) \cap \text{Im}_f(Y)$。


$\star$ S Imf(S) T Imf(T) = Imf(S \cap T) We have made it so that Imf(S) \cap Imf(T) is a strict superset of Imf(S $\cap T$). Look back over our construction, and see if you understand our thought process. What were the restrictions we had to conform to? Where did we have freedom of choice? What did we decide to do? We want to point out that this is absolutely not the only such example, though! Try to come up with others! Right now, all we have left to do is take the final diagram we constructed and use it to define an example and then prove it works. Here we go!


> 🇨🇳 (6) 设 $f: $\mathbb{R}$ \to $\mathbb{R}$, f(x) = x+1$。求 $\text{Im}_f([0,1])$ 和 $\text{PreIm}_f([0,1])$。(7) 证明像不保持差集运算——即 $\text{Im}_f(X-Y)$ 未必等于 $\text{Im}_f(X) - \text{Im}_f(Y)$。


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 **指示函数与像/原像** 像和原像操作与集合运算的交互性质使它们成为分析函数行为的强大工具。原像对并、交、补、差四种运算都"可交换"，而像只对并集可交换。


<div class="def-proof" markdown>
*Proof.* Define A = {1, 2, 3} and B = {$\star$, □}.
</div>
Define f : A $\to B$ by setting f(1) = \star, and f(2) = □, and f(3) = \star. Define S = {1, 2} and T = {2, 3}. Observe that S \cap T = {2}, so Imf(S \cap T) = {f(2)} = {□}. However, observe that Imf(S) = Imf(T) = B, so Imf(S) \cap Imf(T) \neq {□}. Since $\star$$\in Imf(S) \cap Imf(T) but \star$$\notin Imf(S \cap T$), this proves our claim. We have now seen an example of how to prove a claim about arbitrary functions and images, as well as how to construct a specific counterexample to disprove a claim. In the exercises, you will be asked to solve similar problems. Sometimes, you will need to figure out whether a claim is True or not. (Here, we told you which claim was valid beforehand.) We recommend trying one of two things: (1) Try to prove the claim, and see if it breaks down somewhere, or (2) Try to construct a counterexample, and see if you have trouble doing so. If you complete either task... well, hey, you figured it out! But if you're struggling, it might help you figure out what's really going on. Specifically, you will be asked to examine the claim we discussed above, but with "\cup" instead of "$\cap$". What do you think will happen? Go ahead and try it!
### 7.3.3 Pre-Image: Definition and Examples A natural question you might have now is: What about going the other way? Can we take a subset of the codomain and identify the elements whose outputs "land" in that set? Of course! This next definition provides us a term for this notion, and you'll notice many similarities with the definition of image.
Definition
<div class="def-definition" markdown>
**Definition 7.3.8. Let A, B be sets and let f : A $\to B$ be a function. Let Y $\subseteq B$.**
</div>
The pre-image of Y under the function f is written and defined as PreImf(Y ) = {a $\in A$ | f(a) $\in Y$ } That is, the pre-image of Y under f is the set of all "inputs" that produce an "output" in Y. (We will sometimes abbreviate the notation as just PreIm(Y ), when the function is clearly identified and unambiguous, and consequently refer to the set as just "the pre-image of Y ", instead of "the pre-image of Y under f".) Think about this first: What is PreImf(B), where B is the entire codomain? Look back at the definition: this is the set of all inputs (in A) whose outputs "land" in B. That's all of A, of course, since f is a well-defined function! Accordingly, we will really only be working with sets Y $\subset B$, since those cases are more interesting.


> 🇨🇳 **补充** 像/原像的说服力在于：原像继承了陪域的集合结构（并、交、补全都保持），而像只部分继承（只保持并集）。这反映了函数映射的"信息压缩"——不同输入可以映射到同一输出。


Examples
Example 7.3.9. This first example uses the same function we defined in the last
section when we discussed images. We'll show you the schematic diagram again, but spare you from re-defining all the details of the function. (See Example 7.3.2 for the details.) a b c d e


> 🇨🇳 **补充2** 公式 $X \subseteq \text{PreIm}_f(\text{Im}_f(X))$ 表示"先照像再逆推"可能找到更多输入——因为其他输入也可能映射到相同的像。


g : A $\to B$ A B Define Z1 = {1, 2, 3} and Z2 = {2, 3, 4} and Z3 = {4, 5, 6}. Let's identify the following pre-images and explain them. (1) PreImg({1}) = d This is because g(d) = 1 and no other x \in A satisfies g(x) = 1. (Note: We need to use set brackets here. "PreImg(1)" would make no sense.) (2) PreImg({4}) = \emptyset This is because no x \in A satisfies g(x) = 4 (3) PreImg(Z1) = {a, b, c, d} This is because g(a) = 2, g(b) = g(c) = 3, and g(d) = 1, but no other x \in A satisfies g(x) $\in \mathbb{Z}$1. (4) PreImg(Z2) = {a, b, c} This is because g(a) = 2 and g(b) = g(c) = 3, but no other x \in A satisfies g(x) $\in \mathbb{Z}$2. (5) PreImg(Z3) = {e} This is because g(e) = 6, but no other x \in A satisfies g(x) $\in \mathbb{Z}$3. (6) PreImg({5}) = \emptyset This is because \forall x $\in A$. g(x) \neq 5.
Example 7.3.10. Let f : $\mathbb{R} \to \mathbb{R}$ be the function defined by \forall $x \in \mathbb{R}$. f(x) = x2.
Let's identify a few pre-images with this function. We will let you figure out why our claims are valid, as well as how to explain and prove them, this time!


> 🇨🇳 **补充3** $\text{Im}_f(\text{PreIm}_f(Z)) \subseteq \mathbb{Z}$ 表示"先逆推再照像"只会缩小范围——不过若 $Z$ 完全在像中，则缩小为零。


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 **补充4** 像和原像本质上描述了函数如何将集合从一个空间"搬运"到另一个空间：像把子集向前推，原像把子集向后拉。


(1) PreImf({1}) = {-1, 1} (2) PreImf({$y \in \mathbb{R}$ | y < 0}) = \emptyset (3) PreIm({$y \in \mathbb{R}$|y \geq0}) = R (4) PreIm({$y \in \mathbb{R}$|0 < y < 1}) = {$x \in \mathbb{R}$ | -1 < x < 1}
### 7.3.4 Proofs about Pre-Images Notice that the following claim is one of equality. Compare this to Proposition 7.3.6, which has a similar statement about images but it is only a set containment. Interesting, right?
Proposition 7.3.11. Let A, B be sets. Let f : A $\to B$ be a function. Let
X, Y $\subseteq B$. Then, PreImf(X \cap Y ) = PreImf(X) \cap PreImf(Y ) Notice how the proof below appeals directly to the formal definition of preimages. We will jump right in and prove both parts. The exercises will ask you to investigate this claim with "\cup" instead of "$\cap$".
<div class="def-proof" markdown>
*Proof.* Let x $\in PreImf(X \cap Y$ ) be arbitrary and fixed.
</div>
By the definition of pre-image, this means f(x) $\in X \cap Y$. Accordingly, f(x) $\in X and f(x) \in Y. Since f(x) \in X$, this means that x \in PreImf(X) (by the definition of preimage). Similarly, since f(x) \in Y, this means that x \in PreImf(Y ). Thus, by the definition of intersection, we can deduce that x \in PreIm(X) \cap PreIm(Y ). This shows PreIm(X \cap Y ) \subseteq PreIm(X) \cap PreIm(Y ). Next, let y \in PreIm(X) \cap PreIm(Y ) be arbitrary and fixed. By the definition of pre-image, this means y \in PreImf(X) and y \in PreImf(Y ). Since y \in PreImf(X), we can deduce that f(y) \in X, by the definition of preimage. Similarly, since y \in PreImf(Y ), we can deduce that f(y) \in Y. By the definition of interesection, this tells us f(y) \in X \cap Y. Then, by the definition of pre-image, this tells us y \in PreIm(X \cap Y ). This shows PreIm(X \cap Y ) \supseteq PreIm(X) $\cap P$reIm(Y ). By a double-containment proof, we have proven the claim. You might read through this and think, "How does one come up with a proof like this?" Well, there isn't a whole lot of ingenuity behind a result like this. All we did was appeal directly to definitions. Everything fell into place from there.


> 🇨🇳 **补充5** 在拓扑学和测度论中，像和原像的概念被推广到开集/闭集/可测集。原像保持集合运算的性质在这些领域特别重要。


If you find yourself stuck while working on a problem, or you're just unsure of where to start... just write down the relevant definitions. Try to apply them to the statement you're trying to prove. See what happens! A Proof with Pre-Images and Images Let's work on one result that involves both of the concepts we have introduce in this section. We will prove one containment and ask you to disprove the other one in the exercises.
Proposition 7.3.12. Let A, B be sets. Let f : A $\to B$ be a function. Let
Y $\subseteq B$. Then, Imf {PreImf(Y ) } $\subseteq Y$
<div class="def-proof" markdown>
*Proof.* Let b $\in I$mf
</div>
{PreImf(Y ) } be arbitrary and fixed. By the definition of image, this means $\exists a \in P$reImf(Y ). f(a) = b. Let such an a be given. Since a \in PreImf(Y ), this means f(a) \in Y, by the definition of pre-image. Since b = f(a) and f(a) \in Y, this means b $\in Y$. This proves the claim.
### 7.3.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What are the differences between image and pre-image? (2) Suppose f : A $\to B$ is a function. What is PreImf(B)? (3) Suppose g : $\mathbb{R} \to \mathbb{R}$ is a function. Why is the expression Img(0) not a proper statement? What do you think the writer of such an expression meant? (4) Say f : A \to B is a function and Y \subseteq B. What does it mean if PreImf(B) = \emptyset? Is this possible? (5) Say f : A \to B is a function and X \subseteq A. What does it mean if Imf(A) = $\emptyset$? Is this possible?


> 🇨🇳 **补充6** 像/原像的直觉：像 = "$X$ 中的所有输入能到达哪些输出？"原像 = "哪些输入能到达 $Z$ 中的输出？"


Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Let h : R -{-1} $\to $\mathbb{R}$ be defined by \forall x \in \mathbb{R}$ -{-1}. h(x) = x 1+x. Prove that Imh(R -{-1}) = R -{1}. Then, define P = {$y \in \mathbb{R}$ | y > 1} and U = {$y \in \mathbb{R}$ | y > -1}. Prove that PreImh(P) = U. (2) Let f : A \to B be a function. Let S, T \subseteq A. For each of the following claims, prove it must hold, or disprove it by finding a counterexample. (a) Imf(S \cup T) \subseteq Imf(S) \cup Imf(T) (b) Imf(S \cup T) \supseteq Imf(S) \cup Imf(T) (3) Let f : A \to B be a function. Let Y, Z \subseteq B. For each of the following claims, prove it must hold, or disprove it by finding a counterexample. (a) PreImf(Y $\cup $\mathbb{Z}$) \subseteq P$reImf(Y ) \cup PreImf(Z) (b) PreImf(Y $\cup $\mathbb{Z}$) \supseteq P$reImf(Y ) \cup PreImf(Z) (4) Look back at Proposition 7.3.12. Consider the reverse containment: Imf {PreImf(Y ) } \supseteq Y Disprove the claim that this holds for any function f : A \to B and any Y $\subseteq B$ by constructing a specific counterexample and proving that it works.
## 7.4 Properties of Functions
### 7.4.1 Surjective (Onto) Functions You might be wondering something by now... If we can identify the image of the domain under a given function, why bother with a codomain that's any "larger" than that set? Sure f : $\mathbb{R} \to \mathbb{R}$ defined by f(x) = x2 is a fine function, but changing the codomain to just the nonegative real numbers doesn't really affect anything. It might even make it better, because nothing in the codomain is "missed" by the function! If you're thinking this way, then you have anticipated our next definition, which encapsulates precisely this property of a function: when the codomain and the image of the domain are the same set.


> 🇨🇳 **补充7** 总结：原像是"好算的"（保持所有集合运算），像是"难算的"（只保持并集，交集和差集需要额外条件）。


