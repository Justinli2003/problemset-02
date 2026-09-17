# CMPS 6610 Problem Set 02
## Answers

**Name:**_________________________


Place all written answers from `problemset-02.md` here for easier grading.

1. (2 pts) Prove that $\log n! \in \Theta(n \log n).$

   Write $\log n! = \log\left(\prod_{i=1}^{n} i\right) = \sum_{i=1}^{n} \log i.$

   **Upper bound ($O(n\log n)$).** Every term in the sum is at most $\log n$, so
   $$\log n! = \sum_{i=1}^{n}\log i \le \sum_{i=1}^{n}\log n = n\log n.$$
   Hence $\log n! \le n \log n$ for all $n \ge 1$, so $\log n! \in O(n\log n)$
   (with $c = 1$, $n_0 = 1$).

   **Lower bound ($\Omega(n\log n)$).** Throw away the first half of the terms
   (they are all non-negative) and bound the remaining $\lceil n/2 \rceil \ge n/2$
   terms from below by $\log(n/2)$:
   $$\log n! = \sum_{i=1}^{n}\log i \;\ge\; \sum_{i=\lceil n/2\rceil}^{n}\log i
     \;\ge\; \frac{n}{2}\log\frac{n}{2} = \frac{n}{2}\log n - \frac{n}{2}.$$
   For $n \ge 4$ we have $\log n \ge 2$, so $\frac{n}{2} \le \frac{n}{4}\log n$, giving
   $$\log n! \;\ge\; \frac{n}{2}\log n - \frac{n}{4}\log n \;=\; \frac{1}{4}\, n\log n .$$
   Hence $\log n! \in \Omega(n\log n)$ (with $c = 1/4$, $n_0 = 4$).

   Both bounds hold, therefore $\log n! \in \Theta(n\log n)$. $\blacksquare$

   (Aside: this is why any comparison-based sort needs $\Omega(n \log n)$
   comparisons — a decision tree with $n!$ leaves has depth at least $\log n!$.)

2. (18 pts, 2pts ea.) **Recurrences**

   For the divide-and-conquer recurrences $T(n) = aT(n/b) + f(n)$ I use the
   master method / "brick" method: compare $f(n)$ against $n^{\log_b a}$.
   If $f$ is polynomially smaller the recursion is **leaf-dominated**
   ($\Theta(n^{\log_b a})$); if they match the tree is **balanced**
   (an extra $\log n$ factor); if $f$ is polynomially larger the recursion is
   **root-dominated** ($\Theta(f(n))$).

  * $T(n)=2T(n/6)+1$

    $a = 2,\ b = 6$, so $n^{\log_6 2} = n^{0.3868\ldots}$ and $f(n) = 1 = n^0$ is
    polynomially smaller. Leaf-dominated: the cost is proportional to the number
    of leaves, $2^{\log_6 n} = n^{\log_6 2}$.

    $$T(n) \in \Theta\!\left(n^{\log_6 2}\right) \approx \Theta(n^{0.387}) \subseteq O(\sqrt{n}).$$

  * $T(n)=6T(n/4)+n$

    $a = 6,\ b = 4$, so $n^{\log_4 6} = n^{1.2925\ldots}$, which is polynomially
    larger than $f(n) = n$. Leaf-dominated.

    $$T(n) \in \Theta\!\left(n^{\log_4 6}\right) \approx \Theta(n^{1.293}).$$

  * $T(n)=7T(n/7)+n$

    $a = 7,\ b = 7$, so $n^{\log_7 7} = n^1 = f(n)$. Balanced: each of the
    $\log_7 n$ levels costs $\Theta(n)$ (this is exactly the mergesort shape).

    $$T(n) \in \Theta(n\log n).$$

  * $T(n)=9T(n/4)+n^2$

    $a = 9,\ b = 4$, so $n^{\log_4 9} = n^{1.5849\ldots} = O(n^{2-\epsilon})$ with
    $\epsilon \approx 0.415$. Root-dominated (regularity holds:
    $9(n/4)^2 = \frac{9}{16}n^2$, and $9/16 < 1$).

    $$T(n) \in \Theta(n^2).$$

  * $T(n)=4T(n/2)+n^3$

    $a = 4,\ b = 2$, so $n^{\log_2 4} = n^2 = O(n^{3-\epsilon})$. Root-dominated
    (regularity: $4(n/2)^3 = \frac{1}{2}n^3$, and $1/2 < 1$).

    $$T(n) \in \Theta(n^3).$$

  * $T(n)=49T(n/25)+n^{3/2}\log n$

    $a = 49,\ b = 25$, so $n^{\log_{25} 49} = n^{1.2091\ldots}$ (since
    $\log_{25}49 = \frac{\ln 49}{\ln 25} = \frac{3.8918}{3.2189} \approx 1.209$).
    Here $f(n) = n^{3/2}\log n$ grows polynomially faster
    ($f(n) = \Omega(n^{\log_b a + \epsilon})$ for, say, $\epsilon = 0.25$), and
    regularity holds: $49\,(n/25)^{3/2}\log(n/25) \le \frac{49}{125}\, n^{3/2}\log n$
    with $49/125 = 0.392 < 1$. Root-dominated.

    $$T(n) \in \Theta\!\left(n^{3/2}\log n\right).$$

  * $T(n)=T(n-1)+2$

    Not a master-method recurrence; unroll it. There are $n$ levels, each
    contributing $2$: $T(n) = 2n + T(0)$.

    $$T(n) \in \Theta(n).$$

  * $T(n)= T(n-1)+n^c$, with $c\geq 1$

    Unrolling gives $T(n) = \sum_{i=1}^{n} i^{c}$. This sum is
    $\Theta(n^{c+1})$: it is at most $n \cdot n^c = n^{c+1}$, and at least
    $\sum_{i=n/2}^{n} i^c \ge \frac{n}{2}\left(\frac{n}{2}\right)^c = \frac{n^{c+1}}{2^{c+1}}$.

    $$T(n) \in \Theta\!\left(n^{c+1}\right).$$

  * $T(n)=T(\sqrt{n})+1$

    Substitute $n = 2^m$ (i.e. $m = \log n$) and let $S(m) = T(2^m)$. Then
    $\sqrt n = 2^{m/2}$, so $S(m) = S(m/2) + 1$, the binary-search recurrence,
    giving $S(m) \in \Theta(\log m)$. Substituting back $m = \log n$:

    $$T(n) \in \Theta(\log\log n).$$

3. (8 pts) **Algorithm Selection**

   | Alg | Work recurrence | Work | Span recurrence | Span |
   |-----|-------------------|------|-----------------|------|
   | $\mathcal{A}$ | $W(n)=2W(n/5)+n^2$ | $\Theta(n^2)$ | $S(n)=S(n/5)+n^2$ | $\Theta(n^2)$ |
   | $\mathcal{B}$ | $W(n)=W(n-1)+\log n$ | $\Theta(n\log n)$ | $S(n)=S(n-1)+\log n$ | $\Theta(n\log n)$ |
   | $\mathcal{C}$ | $W(n)=W(n/3)+W(2n/3)+n^{1.1}$ | $\Theta(n^{1.1})$ | $S(n)=S(2n/3)+n^{1.1}$ | $\Theta(n^{1.1})$ |

   **$\mathcal{A}$:** $n^{\log_5 2} = n^{0.431}$ is polynomially smaller than $n^2$,
   so the recursion is root-dominated: $W \in \Theta(n^2)$. The span recursion is a
   single branch of depth $\log_5 n$ with geometrically shrinking costs, so
   $S \in \Theta(n^2)$ as well.

   **$\mathcal{B}$:** unrolling, $W(n) = \sum_{i=1}^{n}\log i = \log n! \in \Theta(n\log n)$
   by problem 1. Since there is only **one** subproblem, the span equals the work:
   $S \in \Theta(n\log n)$ — the algorithm is entirely sequential.

   **$\mathcal{C}$:** the tree is unbalanced but still root-dominated, because
   $(1/3)^{1.1} + (2/3)^{1.1} \approx 0.299 + 0.640 = 0.939 < 1$. The per-level
   cost therefore shrinks geometrically and $W(n) \in \Theta(n^{1.1})$. The longest
   root-to-leaf path repeatedly takes the $2n/3$ branch, giving
   $S(n) = S(2n/3) + n^{1.1} \in \Theta(n^{1.1})$.

   **Which would I choose?** Asymptotically, $\mathcal{B}$: $n\log n$ grows strictly
   more slowly than $n^{1.1}$ (equivalently, $\log n \in o(n^{0.1})$), and both
   $\mathcal{A}$ and $\mathcal{C}$ are worse in work. Note that *none* of the three
   offers any parallel speedup — every one has $S = \Theta(W)$, so parallelism
   $W/S$ is $\Theta(1)$ and there is nothing to gain from extra processors. With
   parallelism out of the picture the decision reduces to work alone, and
   $\mathcal{B}$ wins.

   Practical caveat: $n^{0.1}$ only overtakes $\log n$ around $n \approx 10^{16}$,
   so for any realistic input $\mathcal{C}$ would actually be faster, and
   $\mathcal{B}$ also recurses to depth $n$, which is a real problem for stack
   space. So: $\mathcal{B}$ by the asymptotics, $\mathcal{C}$ if I had to ship it.

4. (8 pts) **More Algorithm Selection**

   | Alg | Work recurrence | Work | Span recurrence | Span |
   |-----|-------------------|------|-----------------|------|
   | $\mathcal{A}$ | $W(n)=5W(n/2)+n$ | $\Theta(n^{\log_2 5}) \approx \Theta(n^{2.322})$ | $S(n)=S(n/2)+n$ | $\Theta(n)$ |
   | $\mathcal{B}$ | $W(n)=2W(n-1)+1$ | $\Theta(2^n)$ | $S(n)=S(n-1)+1$ | $\Theta(n)$ |
   | $\mathcal{C}$ | $W(n)=9W(n/3)+n^2$ | $\Theta(n^2\log n)$ | $S(n)=S(n/3)+n^2$ | $\Theta(n^2)$ |

   **$\mathcal{A}$:** $n^{\log_2 5} = n^{2.3219\ldots}$ is polynomially larger than
   $f(n) = n$, so the recursion is leaf-dominated: $W \in \Theta(n^{\log_2 5})$.
   Span: $S(n) = S(n/2) + n$ is root-dominated, $S \in \Theta(n)$.

   **$\mathcal{B}$:** unrolling, $W(n) = 2^n W(1) + (2^n - 1) \in \Theta(2^n)$ —
   exponential. Span: $S(n) = S(n-1) + O(1) \in \Theta(n)$.

   **$\mathcal{C}$:** $a = 9,\ b = 3$ gives $n^{\log_3 9} = n^2 = f(n)$, the balanced
   case: each of the $\log_3 n$ levels costs $\Theta(n^2)$, so
   $W \in \Theta(n^2\log n)$. Span: $S(n) = S(n/3) + n^2$ is root-dominated,
   $S \in \Theta(n^2)$.

   **Which would I choose?** $\mathcal{B}$ is out immediately — exponential work is
   unusable beyond tiny $n$, and its $\Theta(n)$ span is irrelevant because
   realizing it would take $\Theta(2^n/n)$ processors.

   Between $\mathcal{A}$ and $\mathcal{C}$ there is a genuine work/span tradeoff:
   $\mathcal{C}$ does less work ($n^2\log n \prec n^{2.322}$) but $\mathcal{A}$ has a
   far better span ($n$ vs. $n^2$) and therefore much more parallelism
   ($n^{1.322}$ vs. $\log n$). Using $T_P \approx W/P + S$:

   - Sequentially, or with few processors, **$\mathcal{C}$** wins, since
     $n^2\log n$ beats $n^{2.322}$ ($\log n$ stays well below $n^{0.322}$ for any
     realistic $n$).
   - With very many processors, the runtime of $\mathcal{A}$ bottoms out at
     $\Theta(n)$ while that of $\mathcal{C}$ can never drop below $\Theta(n^2)$, so
     **$\mathcal{A}$** wins once $P \gtrsim n^{1.322}$.

   I would choose **$\mathcal{C}$** as the default — it is the better algorithm in
   work, which is what determines runtime on an ordinary machine — and switch to
   $\mathcal{A}$ only in a massively parallel setting where its $\Theta(n)$ span can
   actually be exploited.

5. (4 pts) **Integer Multiplication Timing Results**

   Both algorithms are implemented in `main.py`:

   - `quadratic_multiply` splits $x = a2^{n/2}+b$, $y = c2^{n/2}+d$ and makes
     **four** recursive calls ($ac,\ ad,\ bc,\ bd$):
     $W(n) = 4W(n/2) + O(n) \in \Theta(n^{\log_2 4}) = \Theta(n^2)$.
   - `subquadratic_multiply` (Karatsuba-Ofman) recovers the middle term as
     $(a+b)(c+d) - ac - bd$ and so makes only **three** recursive calls:
     $W(n) = 3W(n/2) + O(n) \in \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$.

   The input size $n$ for these algorithms is the **number of bits**, so the
   sizes used by `compare_multiply()` (decimal $10 \ldots 10^9$, i.e. only 4–30
   bits) are far too small and too narrow to reveal the asymptotics. At that scale
   the two routines are indistinguishable, and Karatsuba is actually a bit
   *slower*, because of its larger constant (the extra additions/subtractions):

   |          n |   quadratic (ms) |   subquadratic (ms) |
   |------------|-------------|----------------|
   |         10 |       0.068 |          0.042 |
   |        100 |       0.058 |          0.083 |
   |       1000 |       0.109 |          0.206 |
   |      10000 |       0.110 |          0.236 |
   |     100000 |       0.203 |          0.283 |
   |    1000000 |       0.348 |          0.364 |
   |   10000000 |       0.264 |          0.375 |
   |  100000000 |       0.517 |          0.669 |
   | 1000000000 |       0.637 |          1.064 |

   So I added `compare_multiply_bits()`, which scales the number of bits $n$
   directly (multiplying two $n$-bit all-ones numbers), doubling $n$ each row:

   |   n (bits) |   quadratic (ms) |   subquadratic (ms) |   quad ratio |   subquad ratio |
   |------------|------------------|---------------------|--------------|-----------------|
   |         16 |            0.819 |               0.926 |            — |               — |
   |         32 |            2.927 |               1.447 |         3.57 |            1.56 |
   |         64 |            8.194 |               6.726 |         2.80 |            4.65 |
   |        128 |           36.464 |              17.456 |         4.45 |            2.60 |
   |        256 |          142.600 |              48.625 |         3.91 |            2.79 |
   |        512 |          642.298 |             150.421 |         4.50 |            3.09 |
   |       1024 |         2375.800 |             450.411 |         3.70 |            2.99 |
   |       2048 |         9936.564 |            1334.532 |         4.18 |            2.96 |

   **This matches the analysis closely.** Since each row doubles $n$, a
   $\Theta(n^k)$ algorithm should show a ratio of $2^k$ between consecutive rows:

   - `quadratic_multiply` settles at a ratio of about **4.0** ($2^2 = 4$),
     confirming $\Theta(n^2)$. The measured exponent over the last doubling is
     $\log_2(9936.6/2375.8) = 2.06$, versus the predicted $2$.
   - `subquadratic_multiply` settles at about **3.0** ($2^{\log_2 3} = 3$),
     confirming $\Theta(n^{\log_2 3})$. The measured exponent over the last
     doubling is $\log_2(1334.5/450.4) = 1.57$, versus the predicted $1.585$.

   The small rows (16–64 bits) are noisy because constant factors and interpreter
   overhead dominate there; the ratios converge to the predicted values once
   $n \ge 256$ or so.

   The crossover is visible as well: Karatsuba is slower at 16 bits, roughly even
   at 64 bits, and by 2048 bits it is **7.4×** faster — and that gap keeps
   widening, since the ratio of the two running times grows as
   $n^2 / n^{1.585} = n^{0.415}$.
