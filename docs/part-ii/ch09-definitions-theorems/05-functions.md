---
title: A.5 Functions
---

# A.5 Functions

(Intuitively, this is the set of all codomain elements "hit" by elements of X.) • Let f : A →B be a function. Let Z ⊆B. The pre-image of Z under the function f is PreImf(Z) = {a ∈A | f(a) ∈Z} (Intuitively, this is the set of all "inputs" whose output "lands" in Z.) • Note: Imf(∅) = ∅and PreImf(∅) = ∅. A.5.2 Jections • Let f : A →B be a function. If Imf(A) = B, then we say f is surjective, or it is a surjection. The definition of image gives us this equivalent formulation of surjectivity: f is surjective ⇐⇒∀b ∈B. ∃a ∈A. f(a) = b (Intuitively, f is surjective when all of the codomain elements are "hit" by the function.) • Let f : A →B be a function. If f has the property that ∀a1, a2 ∈A. a1 ̸= a2 =⇒f(a1) ̸= f(a2) then we say f is injective, or it is an injection. The contrapositive of this conditional statement yields an equivalent formulation of injectivity: ∀a1, a2 ∈A. f(a1) = f(a2) =⇒a1 = a2 (Intuitively, f is injective when two different inputs always yield different outputs, or equivalently when having equal outputs means they came from the same input.) • If a function f is both injective and surjective, then we say f is bijective, or it is a bijection. A.5.3 Composition of Functions • Let f : A →B and g : B →C be functions. The function g ◦f : A →C defined by ∀a ∈A. (g ◦f)(a) = g(f(a)) is the composition of g with f, or "g composed with f".
Note: It helps to read the "◦" as "after" to remind you of the order of
operations: g ◦f means g is applied after f. We find f(a) and then find g(f(a)).


> 🇨🇳 TODO: 待翻译


APPENDIX A. DEFINITIONS AND THEOREMS • Notation: We write (g ◦f)(x) = g(f(x)). We do not write g ◦f(x). The parentheses are important! • Let f : A →B and g : B →C and h : C →D be functions. Then (h ◦g) ◦f = h ◦(g ◦f). This means composition is associative. • Suppose f : A →B and g : B →C are both in/sur/bi-jections. Then g ◦f is also an in/sur/bi-jection. A.5.4 Inverses • Let X be any set. The identity function IdX : X →X is defined by ∀z ∈X. IdX(z) = z. • Let f : A →B be a function. If there is a function F : B →A such that f ◦F : B →B satisfies f ◦F = IdB and F ◦f : A →A satisfies F ◦f = IdA then we say F is the inverse of f and write F = f −1. Notice that the formal defintion clearly includes the necessity of checking that both ways of composing the two functions yields an identity function. There exist examples where one way works and the other doesn't! (Note: When proving a function is the inverse of another one, we aren't allowed to write f −1 yet because we are, in fact, in the midst of proving that f even has an inverse.) If f has an inverse, we say f is invertible. • Theorem: f : A →B is bijective ⇐⇒f has an inverse f −1 : B →A. • Theorem: Let f : A →B and g : B →C both be bijections. Then g ◦f : A →C is also a bijection, so it has an inverse; that inverse is (g ◦f)−1 = f −1 ◦g−1. A.5.5 Proof Techniques for Functions • Prove that f is surjective: -- Let b ∈B be arbitrary and fixed. -- Define a = . -- Show that a ∈A. -- Show that f(a) = b. -- This shows that b ∈Imf(A), so B ⊆Imf(A). -- Since Imf(A) ⊆B by definition, this shows Imf(A) = B, so f is surjective. • Prove that f is not surjective:


> 🇨🇳 TODO: 待翻译


-- Define b = . -- Show that b ∈B. -- Let a ∈A be arbitrary and fixed. -- Show that f(a) ̸= b. (Alternatively, suppose f(a) = b and find a contradiction.) -- This shows that ∃b ∈B. b /∈Imf(A), so f is not surjective. • Prove that f is injective: -- Let x, y ∈A be arbitrary and fixed. -- Suppose that f(x) = f(y). -- Deduce that x = y. Alternatively: -- Let x, y ∈A be arbitrary and fixed. -- Suppose that x ̸= y. -- Deduce that f(x) ̸= f(y). • Prove that f is not injective: -- Define x = and define y = . -- Show that x ∈A and y ∈A. -- Show that x ̸= y. -- Show that f(x) = f(y). -- This shows ∃x, y ∈A. x ̸= y ∧f(x) = f(y), so f is not injective. • Prove that f is bijective: -- Prove that f is injective. -- Prove that f is surjective. Alternatively: -- Define a function F : B →A. -- Prove that F ◦f = IdA. -- Prove that f ◦F = IdB. -- This shows that F = f −1, so f is invertible and therefore it is bijective. • Prove that f is not bijective: -- Show that f is not injective, or else show that f is not surjective. Alternatively,


> 🇨🇳 TODO: 待翻译


APPENDIX A. DEFINITIONS AND THEOREMS -- AFSOC f is bijective, so it has an inverse f −1. Find a contradiction. • For some X ⊆A, find the image Imf(X): -- Define a set S. Claim that S = Imf(X). (Note: Coming up with this definition is the hard part, and will involve a bunch of scratch work. There is no need to show this as part of your proof. Just start with the definition.) -- Prove that Imf(X) ⊆S. ∗Let y ∈Imf(X) be arbitrary and fixed. ∗This means ∃a ∈X. f(a) = y. ∗Use the properties of f to show that f(a) ∈S. ∗This shows that y ∈S. -- Prove that S ⊆Imf(X). ∗Let z ∈S be arbitrary and fixed. ∗Define x = . ∗Show that x ∈X. ∗Show that f(x) = z. ∗This shows that z ∈Imf(X). -- Conclude by a double-containment argument that Imf(X) = S. • For some Z ⊆B, find the preimage PreImf(Z): -- Define a set T. Claim that T = PreImf(Z). (Note: Coming up with this definition is the hard part, and will involve a bunch of scratch work. There is no need to show this as part of your proof. Just start with the definition.) -- Prove that PreImf(Z) ⊆T. ∗Let a ∈PreImf(Z) be arbitrary and fixed. ∗This means f(a) ∈Z. ∗Use the properties of f to show that a ∈T. -- Prove that T ⊆PreImf(Z). ∗Let x ∈T be arbitrary and fixed. ∗Use the properties of f to show that f(x) ∈Z. ∗This shows that x ∈PreImf(Z). -- Conclude by a double-containment argument that PreImf(Z) = T. • Find the inverse of f. -- Define a function F : B →A. (Note: Coming up with this definition is the hard part, and will involve a bunch of scratch work. There is no need to show this as part of your proof. Just start with the definition.)


> 🇨🇳 TODO: 待翻译


-- Show that F is a well-defined function: show that every input from B has exactly one output that lies in A. -- Show that F ◦f = IdA. -- Show that f ◦F = IdB. -- Deduce that F = f −1. (Since f has an inverse, it is therefore a bijection, as well.)


> 🇨🇳 TODO: 待翻译


APPENDIX A. DEFINITIONS AND THEOREMS A.6 Cardinality A.6.1
Definitions
Let S be any set. • We say S is finite if ∃n ∈N ∪{0} such that there exists a bijection f : S →[n].
Note: The empty set S = ∅is finite, since [0] = ∅.
• We say S is infinite if S is not finite; that is, if ∀n ∈N ∪{0}, every function f : S →[n] fails to be a bijection. • We say S is countably infinite (or just countable) if there exists a bijection f : S →N. • We say S is uncountably infinite (or just uncountable) if every function f : S →N fails to be a bijection. • We use |S| to indicate the cardinality of S. When S is finite, so there is some n ∈N ∪{0} and a bijection f : S →[n], we write |S| = n to mean that S has n elements. We say n is the size of S. When S is infinite, we only use |S| to compare the cardinality of S to that of other sets. That is, we don't write things like |S| = ∞; rather, we write something like |S| = |T| to indicate that S and T have the same cardinality, whatever that may be, or something like |S| < |T| to indicate T has a strictly larger cardinality than S. • We write |S| = |T| and say S has the same cardinality as T if and only if there exists a bijection f : S →T. A.6.2 Results In general, the following results hold. Some of the remaining results follow from these general statements. • Suppose |A| = |C| and |B| = |D|. Then |A × B| = |C × D|. • Suppose |A| = |C| and |B| = |D|, and suppose A∩B = ∅and C ∩D = ∅. Then |A ∪B| = |C ∪D|. • Suppose there is an injection f : A →B. Then |A| ≤|B|. • Suppose there is a surjection f : A →B. Then |A| ≥|B|.


> 🇨🇳 TODO: 待翻译


