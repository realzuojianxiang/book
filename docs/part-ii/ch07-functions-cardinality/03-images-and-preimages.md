---
title: Images and Pre-images
---

# Images and Pre-images

7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 TODO: 待翻译


Definition
<div class="def-definition" markdown>
**Definition 7.3.1. Let A, B be sets and let f : A →B be a function.**
</div>
Let X ⊆A. The image of X under the function f is written and defined as Imf(X) = {b ∈B | ∃a ∈X. f(a) = b} That is, the image of X under f is the set of all "outputs" that come from "inputs" in the set X. An equivalent way of writing this is Imf(X) = {f(a) | a ∈X} (We will sometimes abbreviate the notation as just Im(X), when the function is clearly identified and unambiguous, and consequently refer to the set as just "the image of X", instead of "the image of X under f".) When we say the image of f, we mean the image of the entire domain, i.e. Imf(A). Notice that this is defined for any subset of the domain, X ⊆A, so we can talk about the image of any "piece" of the domain, or all of it. We will see some examples now---and exercises later---that consider strict subsets X ⊂A, as well as A itself. One Observation Notice that Imf(A) ⊆B no matter what f and A and B are. This follows by definition, since we used set-builder notation to define the image via elements of B. In the next section, we will explore what happens when Imf(A) = B. For now, let's practice identifying the images of certain functions. In some cases, we will be provided with a function and its image and asked to verify this claim, but in other cases, we will need to develop some techniques to figure out what the image is in the first place!
Examples
Example 7.3.2. Define a function g : A →B by setting A = {a, b, c, d, e} and
B = {1, 2, 3, 4, 5, 6} and g = {(a, 2), (b, 3)(c, 3), (d, 1), (e, 6)} Define X1 = {a, b, c} and X2 = {a, c, e} and X3 = {c, d, e}. You might notice that this is the same function we defined in the schematic diagram in the last section! Let's see that diagram again, because it can help us identify the images in the following list.


> 🇨🇳 TODO: 待翻译


g : A →B A B (1) Img({a}) = {2} This is because g(a) = 2. Notice the use of set brackets. We always find the image of a set, so writing Img(a) would be incorrect. (2) Img({b, c}) = {3} This is because g(b) = g(c) = 3. (3) Img(X1) = {2, 3} This is because g(b) = g(c) = 3 and g(a) = 2. (4) Img(X2) = {2, 3, 6} This is because g(a) = 2 and g(c) = 3 and g(e) = 6. (5) Img(X3) = {1, 3, 6} This is because g(c) = 3 and g(d) = 1 and g(e) = 6. (6) Img(A) = {1, 2, 3, 6} Looking at the set B in the schematic diagram, we see that these are the only values that are "hit" by the function. Notice 4, 5 ∈B but 4, 5 /∈Img(A), so Img(A) ⊂B (a proper subset).
Example 7.3.3. Consider the temperatures (in degrees Celsius) where water is
in its liquid state. Specifically, define the set C = {x ∈R | 0 < x < 100} and define the function F : C →R by ∀c ∈C. F(c) = 9 5c + 32 What is ImF (C)? What does it represent? To approach questions like these, we must (a) identify a claim for what ImF (C) is by defining a set, and then (b) prove that the set we defined is actually equal


> 🇨🇳 TODO: 待翻译


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 TODO: 待翻译


to ImF (C), in the sense of sets. This means we will use a double-containment argument!
Solution: Define S = {y ∈R | 32 < y < 212}. (Notice that this represent the
set of temperatures (in degrees Fahrenheit) where water is in its liquid state.) We claim S = ImF (C). It is hard to give advice about how to come up with claims like this, in general. Most often, this relies on some playing around with the function and testing some values, and perhaps some insight about some other properties of the function. In this specific case, we notice that this function is increasing; that is, if we have two input values with c1 < c2, then we know that F(c1) < F(c2). We can glean this information from the graph of the function (see above) and/or recognizing it is a linear polynomial. Accordingly, to identify the image, we just have to consider the smallest and largest inputs and identify their outputs. (Again, we can glean this information from a graph.) We find that F(0) = 0 + 32 = 32 and F(100) = 900


> 🇨🇳 TODO: 待翻译


+ 32 = 212 From this, we defined the set S. (Also, notice that we had to use "<" in the inequality because, in fact, 0 /∈C, the domain!) We also give this set a name so that we can refer to it later without implicitly claiming, already, that it is the image. This is a somewhat subtle distinction, but an important one! Now, let's prove our claim.
<div class="def-proof" markdown>
*Proof.* First, we'll prove ImF (C) ⊆S. (In other words, we'll prove that every
</div>
output of the function F actually satisfies the inequality in the definition of S.) (To do this we will start with an arbitrary element of ImF (C), and appeal to the defintion of image to bring an element of the domain into play.) Let y ∈ImF (C) be arbitrary and fixed. By the definition of image, this means ∃x ∈C such that F(x) = y. Let such an x be given. By the definition of C, we know 0 < x < 100. By the definition of F, we know


> 🇨🇳 TODO: 待翻译


F(x) = 9 5x + 32. Since multiplying by a positive number and adding to both sides preserves inequalities, we can deduce that


> 🇨🇳 TODO: 待翻译


5 · 0 + 32 < F(x) < 9 5 · 100 + 32 and, simplifying, this tells u 32 < F(x) < 212 Thus, F(x) ∈S, i.e y ∈S. Therefore, ImF (C) ⊆S. Second, we'll prove S ⊆ImF (C). (In other words, we'll prove that every element of S is actually "achieved" by the function F somehow. This amounts to proving an existential claim, i.e. that some element of the domain exists.) Let s ∈S be arbitrary and fixed. By the definition of S, we know that s ∈R and 32 < s < 212. We need to prove that ∃c ∈C. F(c) = s. (By doing some scratch work on the side, that you can work through on your own, we came up with the following idea. Just set an expression equal to s and solve for c . . . ) Define c = 5 9(s −32). Let's show c ∈C. By using the information we have about s and manipulating the inequalities, we observe that 32 < s < 212 =⇒0 < s −32 < 180 =⇒0 < 5 9(s −32) < 5 9 · 180 = 100 =⇒0 < c < 100 Since c ∈R, certainly, this shows that c ∈C. Next, let's show that F(c) = s. We observe that F(c) = 9 5c + 32 = 9


> 🇨🇳 TODO: 待翻译


5 9(s −32)  + 32 = (s −32) + 32 = s Together, this shows that s ∈ImF (C), as well. Thus, S ⊆ImF (C). Overall, by a double-containment argument, we conclude that S = ImF (C). The second half of our proof is certainly the harder part, and this is generally true of proofs like this. In coming up with a candidate c, we essentially have to "undo" the process that the function F does and find an input c for our given output s. In a case like this, where the function is a numerical/arithmetical operation on real numbers, the best route is to set up the desired equality, like


> 🇨🇳 TODO: 待翻译


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 TODO: 待翻译


and solve the equality for c. This function is linear, so this process only produces one such s but, in general, we might expect multiple values of s to work. Ultimately, we only need one working value to complete this part of the proof, so we can just select any one that works and use that as our claim. Sometimes, though, this makes it harder to find such a value. It all depends on the example at hand. Other times, we might be working with functions that aren't defined on sets of numbers, and we have to use some more abstract insight to come up with a candidate element. Again, this all depends on the given situation, and with practice, you'll become much better at it! Oh right, we asked what this image represents! Since the domain represented the temperatures, in degrees Celsius, at which water is a liquid, the image represents the temperatures, in degrees Fahrenheit, at which water is a liquid. Let's look at another example of proving the image of a function is a particular set.
Example 7.3.4. Define f : R →R by
∀x ∈R. f(x) = x2 1 + x2 Let's determine the image, Imf(R), and prove our claim! Here, again, we must use some outside strategies and intuition to identify the image first. Using some techniques from calculus or algebra, we could plot the graph of this function and try to guess the image. Try that if you'd like. You'll end up with this graph: We can also recognize that the denominator is greater than the numerator and so, as x gets larger and larger, those two quantities get closer and closer together, relatively speaking. (That is, their ratio approaches 1.) Also, both terms are nonegative, since they involve squares, so their ratio is at least 0. In any event, we can piece our observations together and make the following claim:


> 🇨🇳 TODO: 待翻译


Define the set T = {y ∈R | 0 ≤y < 1} We claim that T = Imf(R). We now follow the same type of strategy we employed in the previous example. Before we do so, let's remember that the second part of that proof---showing the claimed set is a subset of the image---was the harder part, and try to anticipate what will happen there. In that part, we will be working with an arbitrary element y ∈T and we will want to find an element x ∈R that satisfies f(x) = y. To find such an x, let's set up the equality and try to solve for x: y = x2 1 + x2 ⇐⇒(1 + x2)y = x2 ⇐⇒y + yx2 −x2 = 0 ⇐⇒(y −1)x2 = −y ⇐⇒x2 = y 1 −y Now what? Can we be assured y 1−y ∈R, even? Can we be assured it's nonnegative, so that there exists such an x? What about the fact that there might be two roots? Think about these potential issues and try to write your own version of this proof before reading on for ours!
<div class="def-proof" markdown>
*Proof.* First, let's prove Imf(R) ⊆T.
</div>
Let y ∈Imf(R) be arbitrary and fixed. By the definition of image, we know ∃x ∈R such that f(x) = y. Let such an x be given. Since x ∈R, we know x2 ≥0 and 0 < x2 + 1. We can then deduce that 0 <


> 🇨🇳 TODO: 待翻译


x2+1. By multiplying the previous two inequalities---which we can do since all the terms are non-negative---we may deduce that 0 ≤ x2 1+x2 . Next, we know that 0 ≤x2 < x2 + 1, so x2 1+x2 < 1, as well. (Note: why was it important to point out that x2 ≥0? What can go wrong there?) This shows that 0 ≤ x2 1+x2 < 1. Since y = f(x) = x2 1+x2 , this is equivalent to saying 0 ≤y < 1. Thus, y ∈T, and so Imf(R) ⊆T. Second, let's prove T ⊆Imf(R). Let y ∈T be arbitrary and fixed. This means y ∈R and 0 ≤y < 1. To show y ∈Imf(R), as well, we must produce an x such that f(x) = y.


> 🇨🇳 TODO: 待翻译


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 TODO: 待翻译


We claim that x = q y 1−y works. Notice that y ≥0, and y < 1 implies −y > −1 so 1 −y > 0. Thus, y 1−y ≥0, and so x ∈R is well-defined as a square root, and x belongs to the domain R. Next, notice that x2 = y 1−y, and so f(x) = x2 1 + x2 = y 1−y 1 + y 1−y = y 1−y (1−y)+y 1−y = y 1−y


> 🇨🇳 TODO: 待翻译


1−y = y 1 −y · 1 −y


> 🇨🇳 TODO: 待翻译


= y 1 = y This shows that y ∈Imf(R), and so T ⊆Imf(R). Overall, by a double-containment proof, we conclude that T = Imf(R). Notice how we addressed the issues discussed before the proof. Yes, two potential x values existed that would work (namely, the + and −square roots) but we only needed one, so we just picked one (the positive one) and ran with it. (Questions: What if this function was defined only on the nonnegative real numbers? What about just the negative real numbers? How might that restriction affect our choice?)
Example 7.3.5. Consider the function p : N × N →N defined by
∀(a, b) ∈N × N. p(a, b) = ab + a What is Imp(N × N)? This example might feel a little trickier because the domain is a Cartesian product of sets; that is, p inputs an ordered pair of natural numbers and outputs a single natural number. A good approach in a situation like this is to just start plugging in some values and seeing what happens. Consider the following table of values as a way to get started, where the left column indicates values of a, the top row indicates values of b, and the table entries are the values of p(a, b).


> 🇨🇳 TODO: 待翻译


It looks like every natural number is "achieved" by the function p, except for 1. Specifically, look at the top row of the array of values: there are all the natural numbers except 1. Let's use this insight in the following proof.
<div class="def-proof" markdown>
*Proof.* Let V = N −{1}. We claim V = Imp(N × N).
</div>
First, we prove Imp(N × N) ⊆V . Let n ∈Imp(N × N) be arbitrary and fixed. This means n ∈N and ∃(a, b) ∈N × N such that p(a, b) = n. Let such (a, b) be


> 🇨🇳 TODO: 待翻译


given. This means n = ab + a. Since a, b ≥1, then ab ≥1 and so n = ab + a ≥2. By the defintion of V , this shows that n ∈V . Thus, Imp(N × N) ⊆V . (Try to write the next half of the proof before reading on and seeing ours! ) Second, we prove V ⊆Imp(N × N). Let v ∈V be arbitary and fixed. This means v ∈N and v ≥2. Define (a, b) = (v −1, 1). Notice that v −1 ≥1, so v −1 ∈N and thus (a, b) ∈N × N. Also, notice that p(a, b) = p(v −1, 1) = (v −1) · 1 + 1 = v −1 + 1 = v Thus, p(a, b) = v, and so (a, b) ∈Imp(N × N). Therefore, V ⊆Imp(N × N). By a double-containment proof, we have shown V = Imp(N × N).
### 7.3.2 Proofs about Images You might have observed the following fact by playing around with some of the examples we have seen. Either way, we can make state and prove this claim by working with the definition of image. Notice that it is a claim about an arbitrary function; it holds no matter what f is!
Proposition 7.3.6. Let A, B be sets.
Let f : A →B be a function. Let S, T ⊆A. Then, Imf(S ∩T) ⊆Imf(S) ∩Imf(T)
<div class="def-proof" markdown>
*Proof.* Let z ∈Imf(S ∩T) be arbitrary and fixed. This means ∃a ∈S ∩T such
</div>
that f(a) = z. Let such an a be given. Since a ∈S ∩T, we know a ∈S and a ∈T. Thus, z ∈Imf(S) and z ∈Imf(T), by the definition of image. We deduce that z ∈Imf(S) ∩Imf(T), by the definition of intersection. This shows the desired set containment. Why didn't we claim an equality here? It turns out that equality need not hold, in fact! That is, there exists at least one function such that the reverse containment---namely, Imf(S)∩Imf(T) ⊆Imf(S∩T)---is False. We will provide an example of such a function below. (You should try to come up with an example of a function where this reverse containment does hold. Together, we will have shown that one cannot make a conclusion that necessarily holds about this containment!)


> 🇨🇳 TODO: 待翻译


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 TODO: 待翻译


We will use a schematic diagram to come up with an example with the desired properties. We will then use this to formally define a function and state its properties, pointing out how they match what will be established in our claim. We want to point out that employing this technique is perfectly valid, as long as you go back and write down a formal definition afterwards. Turning in just a schematic diagram as a "proof" is not rigorous enough, but this can certainly help guide your intuition into producing fruitful ideas for a proof! Furthermore, keep in mind that there is no need to construct the most complicated or interesting counterexample in situations like this. If you're trying to disprove a universally-quantified statement, you just need one example that works! In particular, don't feel like you need to define a function that works with numbers, using some formula. Sometimes, this will actually make your job much harder! It's typically the case that a counterexample can be made using sets with just a few (i.e. two or three) elements each.
Example 7.3.7. We claim that there exist sets A, B, S, T and a function f : A →
B such that Imf(S) ∩Imf(T) ̸⊆Imf(S ∩T). Let's figure out how to construct such an example. Based on our comment above, we are going to try to make an example where the sets involve three or so elements. Let's get the process started by taking A to be {1, 2, 3} and defining f(1):


> 🇨🇳 TODO: 待翻译


⋆ Now, just to have a defintion in hand, let's choose S = {1, 2}. It seems like it will be more reasonable to work with 2 elements in S, so we'll make that choice. Also, it seems like we should make f(1) ̸= f(2). Otherwise, Imf(S) would contain only one element, and there would have been no point in making S have two elements. So let's define f(2), as well:


> 🇨🇳 TODO: 待翻译


⋆ S Imf(S) Now, we need to choose T. It will be interesting to have S ∩T ̸= ∅, but it would be hard to handle (perhaps) if T ⊇S. So, let's say T = {2, 3}. Then, we just need to choose f(3). In considering each of these cases, look at the schematic diagram above, and imagine drawing an arrow to represent f(3). • What if f(3) = f(2) = □? In this case, Im( T) = { □}, so Imf(S)∩Imf(T) = { □}. But Imf(S∩T) = { □}, as well! This doesn't work. • What if f(3) is something else, like f(3) = , ? This doesn't work either! We will have Imf(S)∩Imf(T) = { □} = Imf(S∩ T). • What if f(3) = f(1) = ⋆? It looks like this works!


> 🇨🇳 TODO: 待翻译


⋆ S Imf(S) T Imf(T) = Imf(S ∩T) We have made it so that Imf(S) ∩Imf(T) is a strict superset of Imf(S ∩T). Look back over our construction, and see if you understand our thought process. What were the restrictions we had to conform to? Where did we have freedom of choice? What did we decide to do? We want to point out that this is absolutely not the only such example, though! Try to come up with others! Right now, all we have left to do is take the final diagram we constructed and use it to define an example and then prove it works. Here we go!


> 🇨🇳 TODO: 待翻译


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 TODO: 待翻译


<div class="def-proof" markdown>
*Proof.* Define A = {1, 2, 3} and B = {⋆, □}.
</div>
Define f : A →B by setting f(1) = ⋆, and f(2) = □, and f(3) = ⋆. Define S = {1, 2} and T = {2, 3}. Observe that S ∩T = {2}, so Imf(S ∩T) = {f(2)} = {□}. However, observe that Imf(S) = Imf(T) = B, so Imf(S) ∩Imf(T) ̸= {□}. Since ⋆∈Imf(S) ∩Imf(T) but ⋆/∈Imf(S ∩T), this proves our claim. We have now seen an example of how to prove a claim about arbitrary functions and images, as well as how to construct a specific counterexample to disprove a claim. In the exercises, you will be asked to solve similar problems. Sometimes, you will need to figure out whether a claim is True or not. (Here, we told you which claim was valid beforehand.) We recommend trying one of two things: (1) Try to prove the claim, and see if it breaks down somewhere, or (2) Try to construct a counterexample, and see if you have trouble doing so. If you complete either task . . . well, hey, you figured it out! But if you're struggling, it might help you figure out what's really going on. Specifically, you will be asked to examine the claim we discussed above, but with "∪" instead of "∩". What do you think will happen? Go ahead and try it!
### 7.3.3 Pre-Image: Definition and Examples A natural question you might have now is: What about going the other way? Can we take a subset of the codomain and identify the elements whose outputs "land" in that set? Of course! This next definition provides us a term for this notion, and you'll notice many similarities with the definition of image.
Definition
<div class="def-definition" markdown>
**Definition 7.3.8. Let A, B be sets and let f : A →B be a function. Let Y ⊆B.**
</div>
The pre-image of Y under the function f is written and defined as PreImf(Y ) = {a ∈A | f(a) ∈Y } That is, the pre-image of Y under f is the set of all "inputs" that produce an "output" in Y . (We will sometimes abbreviate the notation as just PreIm(Y ), when the function is clearly identified and unambiguous, and consequently refer to the set as just "the pre-image of Y ", instead of "the pre-image of Y under f".) Think about this first: What is PreImf(B), where B is the entire codomain? Look back at the definition: this is the set of all inputs (in A) whose outputs "land" in B. That's all of A, of course, since f is a well-defined function! Accordingly, we will really only be working with sets Y ⊂B, since those cases are more interesting.


> 🇨🇳 TODO: 待翻译


Examples
Example 7.3.9. This first example uses the same function we defined in the last
section when we discussed images. We'll show you the schematic diagram again, but spare you from re-defining all the details of the function. (See Example 7.3.2 for the details.) a b c d e


> 🇨🇳 TODO: 待翻译


g : A →B A B Define Z1 = {1, 2, 3} and Z2 = {2, 3, 4} and Z3 = {4, 5, 6}. Let's identify the following pre-images and explain them. (1) PreImg({1}) = d This is because g(d) = 1 and no other x ∈A satisfies g(x) = 1. (Note: We need to use set brackets here. "PreImg(1)" would make no sense.) (2) PreImg({4}) = ∅ This is because no x ∈A satisfies g(x) = 4 (3) PreImg(Z1) = {a, b, c, d} This is because g(a) = 2, g(b) = g(c) = 3, and g(d) = 1, but no other x ∈A satisfies g(x) ∈Z1. (4) PreImg(Z2) = {a, b, c} This is because g(a) = 2 and g(b) = g(c) = 3, but no other x ∈A satisfies g(x) ∈Z2. (5) PreImg(Z3) = {e} This is because g(e) = 6, but no other x ∈A satisfies g(x) ∈Z3. (6) PreImg({5}) = ∅ This is because ∀x ∈A. g(x) ̸= 5.
Example 7.3.10. Let f : R →R be the function defined by ∀x ∈R. f(x) = x2.
Let's identify a few pre-images with this function. We will let you figure out why our claims are valid, as well as how to explain and prove them, this time!


> 🇨🇳 TODO: 待翻译


7.3. IMAGES AND PRE-IMAGES


> 🇨🇳 TODO: 待翻译


(1) PreImf({1}) = {−1, 1} (2) PreImf({y ∈R | y < 0}) = ∅ (3) PreIm({y ∈R|y ≥0}) = R (4) PreIm({y ∈R|0 < y < 1}) = {x ∈R | −1 < x < 1}
### 7.3.4 Proofs about Pre-Images Notice that the following claim is one of equality. Compare this to Proposition 7.3.6, which has a similar statement about images but it is only a set containment. Interesting, right?
Proposition 7.3.11. Let A, B be sets. Let f : A →B be a function. Let
X, Y ⊆B. Then, PreImf(X ∩Y ) = PreImf(X) ∩PreImf(Y ) Notice how the proof below appeals directly to the formal definition of preimages. We will jump right in and prove both parts. The exercises will ask you to investigate this claim with "∪" instead of "∩".
<div class="def-proof" markdown>
*Proof.* Let x ∈PreImf(X ∩Y ) be arbitrary and fixed.
</div>
By the definition of pre-image, this means f(x) ∈X ∩Y . Accordingly, f(x) ∈X and f(x) ∈Y . Since f(x) ∈X, this means that x ∈PreImf(X) (by the definition of preimage). Similarly, since f(x) ∈Y , this means that x ∈PreImf(Y ). Thus, by the definition of intersection, we can deduce that x ∈PreIm(X) ∩ PreIm(Y ). This shows PreIm(X ∩Y ) ⊆PreIm(X) ∩PreIm(Y ). Next, let y ∈PreIm(X) ∩PreIm(Y ) be arbitrary and fixed. By the definition of pre-image, this means y ∈PreImf(X) and y ∈PreImf(Y ). Since y ∈PreImf(X), we can deduce that f(y) ∈X, by the definition of preimage. Similarly, since y ∈PreImf(Y ), we can deduce that f(y) ∈Y . By the definition of interesection, this tells us f(y) ∈X ∩Y . Then, by the definition of pre-image, this tells us y ∈PreIm(X ∩Y ). This shows PreIm(X ∩Y ) ⊇PreIm(X) ∩PreIm(Y ). By a double-containment proof, we have proven the claim. You might read through this and think, "How does one come up with a proof like this?" Well, there isn't a whole lot of ingenuity behind a result like this. All we did was appeal directly to definitions. Everything fell into place from there.


> 🇨🇳 TODO: 待翻译


If you find yourself stuck while working on a problem, or you're just unsure of where to start . . . just write down the relevant definitions. Try to apply them to the statement you're trying to prove. See what happens! A Proof with Pre-Images and Images Let's work on one result that involves both of the concepts we have introduce in this section. We will prove one containment and ask you to disprove the other one in the exercises.
Proposition 7.3.12. Let A, B be sets. Let f : A →B be a function. Let
Y ⊆B. Then, Imf  PreImf(Y )  ⊆Y
<div class="def-proof" markdown>
*Proof.* Let b ∈Imf
</div>
 PreImf(Y )  be arbitrary and fixed. By the definition of image, this means ∃a ∈PreImf(Y ). f(a) = b. Let such an a be given. Since a ∈PreImf(Y ), this means f(a) ∈Y , by the definition of pre-image. Since b = f(a) and f(a) ∈Y , this means b ∈Y . This proves the claim.
### 7.3.5 Questions & Exercises
Remind Yourself Answering the following questions briefly, either out loud or in writing. These are all based on the section you just read, so if you can't recall a specific definition or concept or example, go back and reread that part. Making sure you can confidently answer these before moving on will help your understanding and memory! (1) What are the differences between image and pre-image? (2) Suppose f : A →B is a function. What is PreImf(B)? (3) Suppose g : R →R is a function. Why is the expression Img(0) not a proper statement? What do you think the writer of such an expression meant? (4) Say f : A →B is a function and Y ⊆B. What does it mean if PreImf(B) = ∅? Is this possible? (5) Say f : A →B is a function and X ⊆A. What does it mean if Imf(A) = ∅? Is this possible?


> 🇨🇳 TODO: 待翻译


Try It Try answering the following short-answer questions. They require you to actually write something down, or describe something out loud (to a friend/classmate, perhaps). The goal is to get you to practice working with new concepts, definitions, and notation. They are meant to be easy, though; making sure you can work through them will help you! (1) Let h : R −{−1} →R be defined by ∀x ∈R −{−1}. h(x) = x 1+x. Prove that Imh(R −{−1}) = R −{1}. Then, define P = {y ∈R | y > 1} and U = {y ∈R | y > −1}. Prove that PreImh(P) = U. (2) Let f : A →B be a function. Let S, T ⊆A. For each of the following claims, prove it must hold, or disprove it by finding a counterexample. (a) Imf(S ∪T) ⊆Imf(S) ∪Imf(T) (b) Imf(S ∪T) ⊇Imf(S) ∪Imf(T) (3) Let f : A →B be a function. Let Y, Z ⊆B. For each of the following claims, prove it must hold, or disprove it by finding a counterexample. (a) PreImf(Y ∪Z) ⊆PreImf(Y ) ∪PreImf(Z) (b) PreImf(Y ∪Z) ⊇PreImf(Y ) ∪PreImf(Z) (4) Look back at Proposition 7.3.12. Consider the reverse containment: Imf  PreImf(Y )  ⊇Y Disprove the claim that this holds for any function f : A →B and any Y ⊆B by constructing a specific counterexample and proving that it works.
## 7.4 Properties of Functions
### 7.4.1 Surjective (Onto) Functions You might be wondering something by now . . . If we can identify the image of the domain under a given function, why bother with a codomain that's any "larger" than that set? Sure f : R →R defined by f(x) = x2 is a fine function, but changing the codomain to just the nonegative real numbers doesn't really affect anything. It might even make it better, because nothing in the codomain is "missed" by the function! If you're thinking this way, then you have anticipated our next definition, which encapsulates precisely this property of a function: when the codomain and the image of the domain are the same set.


> 🇨🇳 TODO: 待翻译


