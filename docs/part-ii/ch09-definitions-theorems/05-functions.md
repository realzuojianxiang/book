---
title: A.5 Functions
---

# A.5 Functions

(Intuitively, this is the set of all codomain elements "hit" by elements of X.) • Let f : A $\to B$ be a function. Let Z $\subseteq B$. The pre-image of Z under the function f is PreImf(Z) = {a $\in A$ | f(a) $\in \mathbb{Z}$} (Intuitively, this is the set of all "inputs" whose output "lands" in Z.) • Note: Imf($\emptyset$) = $\emptyset a$nd PreImf($\emptyset$) = $\emptyset$. A.5.2 Jections • Let f : A $\to B$ be a function. If Imf(A) = B, then we say f is surjective, or it is a surjection. The definition of image gives us this equivalent formulation of surjectivity: $f is surjective \Leftrightarrow \forall b \in B. \exists a \in A$. f(a) = b (Intuitively, f is surjective when all of the codomain elements are "hit" by the function.) • Let f : A $\to B$ be a function. If f has the property that $\forall a$1, a2 $\in A$. a1 \neq a2 =$\Rightarrow f$(a1) \neq f(a2) then we say f is injective, or it is an injection. The contrapositive of this conditional statement yields an equivalent formulation of injectivity: $\forall a$1, a2 $\in A$. f(a1) = f(a2) =$\Rightarrow a$1 = a2 (Intuitively, f is injective when two different inputs always yield different outputs, or equivalently when having equal outputs means they came from the same input.) • If a function f is both injective and surjective, then we say f is bijective, or it is a bijection. A.5.3 Composition of Functions • Let f : A $\to B$ and g : B $\to \mathbb{C}$ be functions. The function g ◦f : A $\to \mathbb{C}$ defined by $\forall a$ $\in A$. (g ◦f)(a) = g(f(a)) is the composition of g with f, or "g composed with f".
Note: It helps to read the "◦" as "after" to remind you of the order of
operations: g ◦f means g is applied after f. We find f(a) and then find g(f(a)).


> 🇨🇳 （直观上，这是所有输出"落入" $Z$ 的输入组成的集合。）注意：$\text{Im}_f(\emptyset) = \emptyset$，$\text{PreIm}_f(\emptyset) = \emptyset$。
>
> **A.5.2 满射、单射、双射 (Jections)** 设 $f: A \to B$ 为函数。若 $\text{Im}_f(A) = B$，称 $f$ 为**满射（Surjective）**，等价表述为 $\forall b \in B.\, \exists a \in A.\, f(a) = b$——陪域中所有元素都被"命中"。若 $\forall a_1, a_2 \in A.\, a_1 \neq a_2 \Rightarrow f(a_1) \neq f(a_2)$，称 $f$ 为**单射（Injective）**，等价于 $\forall a_1, a_2 \in A.\, f(a_1) = f(a_2) \Rightarrow a_1 = a_2$——不同输入总产生不同输出。若 f 既是单射又是满射，称 $f$ 为**双射（Bijective）**。
>
> **A.5.3 函数的复合** 设 $f: A \to B$，$g: B \to C$，则 $g \circ f: A \to C$ 定义为 $(g \circ f)(a) = g(f(a))$，称为 $g$ 与 $f$ 的**复合**。提示：将 "$\circ$" 读作"之后"，$g \circ f$ 即 $g$ 在 $f$ 之后作用。


APPENDIX A. DEFINITIONS AND THEOREMS • Notation: We write (g ◦f)(x) = g(f(x)). We do not write g ◦f(x). The parentheses are important! • Let f : A $\to B$ and g : B $\to \mathbb{C}$ and h : C $\to D$ be functions. Then (h ◦g) ◦f = h ◦(g ◦f). This means composition is associative. • Suppose f : A $\to B$ and g : B $\to \mathbb{C}$ are both in/sur/bi-jections. Then g ◦f is also an in/sur/bi-jection. A.5.4 Inverses • Let X be any set. The identity function IdX : X $\to X$ is defined by $\forall z$ $\in X$. IdX(z) = z. • Let f : A $\to B$ be a function. If there is a function F : B $\to A$ such that f ◦F : B $\to B$ satisfies f ◦F = IdB and F ◦f : A $\to A$ satisfies F ◦f = IdA then we say F is the inverse of f and write F = f −1. Notice that the formal defintion clearly includes the necessity of checking that both ways of composing the two functions yields an identity function. There exist examples where one way works and the other doesn't! (Note: When proving a function is the inverse of another one, we aren't allowed to write f −1 yet because we are, in fact, in the midst of proving that f even has an inverse.) If f has an inverse, we say f is invertible. • Theorem: f : A $\to B is bijective \Leftrightarrow f$ has an inverse f −1 : B $\to A$. • Theorem: Let f : A $\to B$ and g : B $\to \mathbb{C}$ both be bijections. Then g ◦f : A $\to \mathbb{C}$ is also a bijection, so it has an inverse; that inverse is (g ◦f)−1 = f −1 ◦g−1. A.5.5 Proof Techniques for Functions • Prove that f is surjective: -- Let b $\in B$ be arbitrary and fixed. -- Define a = . -- Show that a $\in A$. -- Show that f(a) = b. -- This shows that b $\in I$mf(A), so B $\subseteq I$mf(A). -- Since Imf(A) $\subseteq B$ by definition, this shows Imf(A) = B, so f is surjective. • Prove that f is not surjective:


> 🇨🇳 记号：写 $(g \circ f)(x) = g(f(x))$，不写 $g \circ f(x)$，括号不可省！复合满足结合律：$(h \circ g) \circ f = h \circ (g \circ f)$。若 $f$、$g$ 同为单射/满射/双射，则 $g \circ f$ 亦然。
>
> **A.5.4 逆函数** 恒等函数 $\text{Id}_X : X \to X$ 定义为 $\text{Id}_X(z) = z$。若存在 $F: B \to A$ 使 $f \circ F = \text{Id}_B$ 且 $F \circ f = \text{Id}_A$，则 $F = f^{-1}$，称 $f$ **可逆**。注意必须验证两个方向的复合都得到恒等函数。**定理**：$f: A \to B$ 为双射 $\Leftrightarrow$ f 有逆 $f^{-1}: B \to A$。双射的复合仍为双射，且 $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$。
>
> **A.5.5 函数的证明技巧**
> 证明满射：任取 $b \in B$，构造 $a \in A$ 使 $f(a) = b$，从而 $\text{Im}_f(A) = B$。证明非满射：找 $b \in B$ 使 $\forall a \in A.\, f(a) \neq b$。


-- Define b = . -- Show that b $\in B$. -- Let a $\in A$ be arbitrary and fixed. -- Show that f(a) \neq b. (Alternatively, suppose f(a) = b and find a contradiction.) -- This shows that $\exists b \in B. b \notin I$mf(A), so f is not surjective. • Prove that f is injective: -- Let x, y $\in A$ be arbitrary and fixed. -- Suppose that f(x) = f(y). -- Deduce that x = y. Alternatively: -- Let x, y $\in A$ be arbitrary and fixed. -- Suppose that x \neq y. -- Deduce that f(x) \neq f(y). • Prove that f is not injective: -- Define x = and define y = . -- Show that x $\in A$ and y $\in A$. -- Show that x \neq y. -- Show that f(x) = f(y). -- This shows $\exists x$, y $\in A$. x ̸$= y \wedgef(x) = f(y), so f is not injective.$ • Prove that f is bijective: -- Prove that f is injective. -- Prove that f is surjective. Alternatively: -- Define a function F : B $\to A$. -- Prove that F ◦f = IdA. -- Prove that f ◦F = IdB. -- This shows that F = f −1, so f is invertible and therefore it is bijective. • Prove that f is not bijective: -- Show that f is not injective, or else show that f is not surjective. Alternatively,


> 🇨🇳 证明单射：任取 $x, y \in A$，由 $f(x) = f(y)$ 推出 $x = y$；或由 $x \neq y$ 推出 $f(x) \neq f(y)$。证明非单射：找 $x \neq y \in A$ 使 $f(x) = f(y)$。证明双射：证单射 + 证满射；或构造 $F: B \to A$ 使 $F \circ f = \text{Id}_A$ 且 $f \circ F = \text{Id}_B$，从而 $F = f^{-1}$，$f$ 双射。证明非双射：证非单射或非满射；或反设双射导出矛盾。


APPENDIX A. DEFINITIONS AND THEOREMS -- AFSOC f is bijective, so it has an inverse f −1. Find a contradiction. • For some X $\subseteq A$, find the image Imf(X): -- Define a set S. Claim that S = Imf(X). (Note: Coming up with this definition is the hard part, and will involve a bunch of scratch work. There is no need to show this as part of your proof. Just start with the definition.) -- Prove that Imf(X) $\subseteq S$. ∗Let y $\in I$mf(X) be arbitrary and fixed. ∗This means $\exists a$ $\in X$. f(a) = y. ∗Use the properties of f to show that f(a) $\in S$. ∗This shows that y $\in S$. -- Prove that S $\subseteq I$mf(X). ∗Let z $\in S$ be arbitrary and fixed. ∗Define x = . ∗Show that x $\in X$. ∗Show that f(x) = z. ∗This shows that z $\in I$mf(X). -- Conclude by a double-containment argument that Imf(X) = S. • For some Z $\subseteq B$, find the preimage PreImf(Z): -- Define a set T. Claim that T = PreImf(Z). (Note: Coming up with this definition is the hard part, and will involve a bunch of scratch work. There is no need to show this as part of your proof. Just start with the definition.) -- Prove that PreImf(Z) $\subseteq T$. ∗Let a $\in P$reImf(Z) be arbitrary and fixed. ∗This means f(a) $\in \mathbb{Z}$. ∗Use the properties of f to show that a $\in T$. -- Prove that T $\subseteq P$reImf(Z). ∗Let x $\in T$ be arbitrary and fixed. ∗Use the properties of f to show that f(x) $\in \mathbb{Z}$. ∗This shows that x $\in P$reImf(Z). -- Conclude by a double-containment argument that PreImf(Z) = T. • Find the inverse of f. -- Define a function F : B $\to A$. (Note: Coming up with this definition is the hard part, and will involve a bunch of scratch work. There is no need to show this as part of your proof. Just start with the definition.)


> 🇨🇳 证明 $F$ 是良定义的函数：证 $B$ 中每个输入都有且仅有一个属于 $A$ 的输出。证 $F \circ f = 	ext{Id}_A$。证 $f \circ F = 	ext{Id}_B$。由此得 $F = f^{-1}$（从而 $f$ 为双射）。


-- Show that F is a well-defined function: show that every input from B has exactly one output that lies in A. -- Show that F ◦f = IdA. -- Show that f ◦F = IdB. -- Deduce that F = f −1. (Since f has an inverse, it is therefore a bijection, as well.)


> 🇨🇳 **A.6 基数（Cardinality）**
>
> **A.6.1 定义** 设 $S$ 为任意集合。称 $S$ **有限（Finite）**，若 $\exists n \in \mathbb{N} \cup \{0\}$ 使存在双射 $f: S 	o [n]$。空集 $\emptyset$ 有限，因为 $[0] = \emptyset$。称 $S$ **无限（Infinite）**，若 S 非有限。称 S **可数无限（Countably Infinite）**，若存在双射 $f: S 	o \mathbb{N}$。称 S **不可数无限（Uncountably Infinite）**，若每个函数 $f: S 	o \mathbb{N}$ 都不是双射。用 $|S|$ 表示 $S$ 的基数。有限时 $|S| = n$；无限时仅用 $|S|$ 与其他集合比较，不写 $|S| = \infty$，而写 $|S| = |T|$ 表示等势，$|S| < |T|$ 表示 $T$ 的基数严格更大。$|S| = |T|$ 当且仅当存在双射 $f: S 	o T$。
>
> **A.6.2 一般结果** 若 $|A| = |C|$ 且 $|B| = |D|$，则 $|A 	imes B| = |C 	imes D|$。若还有 $A \cap B = \emptyset$ 且 $C \cap D = \emptyset$，则 $|A \cup B| = |C \cup D|$。若存在单射 $f: A 	o B$，则 $|A| \leq |B|$。若存在满射 $f: A 	o B$，则 $|A| \geq |B|$。


APPENDIX A. DEFINITIONS AND THEOREMS A.6 Cardinality A.6.1
Definitions
Let S be any set. • We say S is finite if $\exists n \in \mathbb{N} \cup${0} such that there exists a bijection f : S $\to$[n].
Note: The empty set S = $\emptyset i$s finite, since [0] = $\emptyset$.
• We say S is infinite if S is not finite; that is, if $\forall n \in \mathbb{N} \cup${0}, every function f : S $\to$[n] fails to be a bijection. • We say S is countably infinite (or just countable) if there exists a bijection f : S $\to \mathbb{N}$. • We say S is uncountably infinite (or just uncountable) if every function f : S $\to \mathbb{N}$ fails to be a bijection. • We use |S| to indicate the cardinality of S. When S is finite, so there is some n $\in \mathbb{N}$ $\cup${0} and a bijection f : S $\to$[n], we write |S| = n to mean that S has n elements. We say n is the size of S. When S is infinite, we only use |S| to compare the cardinality of S to that of other sets. That is, we don't write things like |S| = $\infty$; rather, we write something like |S| = |T| to indicate that S and T have the same cardinality, whatever that may be, or something like |S| < |T| to indicate T has a strictly larger cardinality than S. • We write |S| = |T| and say S has the same cardinality as T if and only if there exists a bijection f : S $\to T$. A.6.2 Results In general, the following results hold. Some of the remaining results follow from these general statements. • Suppose |A| = |C| and |B| = |D|. Then |$A \times B$| = |$C \times D$|. • Suppose |A| = |C| and |B| = |D|, and suppose A$\cap B$ = $\emptyset a$nd C $\cap D$ = $\emptyset$. Then |A $\cup B$| = |C $\cup D$|. • Suppose there is an injection f : A $\to B$. Then |A| $\leq$|B|. • Suppose there is a surjection f : A $\to B$. Then |A| $\geq$|B|.


> 🇨🇳 （基数一般结果已合并于上方翻译）


