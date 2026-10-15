# Primary-source comparison, 15 October 2026

The audit read the locally retained complete primary PDFs and checked the corresponding primary-source pages. It compares actual hypotheses; it is not an exhaustive priority search.

## Manabe

Hikaru Manabe, *Purely Periodic Three-move Subtraction Games*, arXiv:2609.05358v2, 16 September 2026. Verified version: https://arxiv.org/abs/2609.05358v2 .

The sufficient tests in Lemma 14, Theorem 27 and Proposition 61 have no admissible primitive angle at b=4a, a>=2: the first two sets specialize to {a,4a}, {2a,4a}, and the third contains only multiples of a. Their failure is not by itself a proof of non-pure-periodicity. Conjecture 52 asserts necessity. Proposition 55 supplies it only for c>=2(a+b) and pure least period <=a+b. The paper independently reproves this short-period exclusion (Corollary 3.3) and proves positive preperiod for the full b=4a slice using its own classification and obstruction. This is a special-slice verification of that prediction, not a proof of the general conjecture. Manabe's ancillary Lean files formalize that author's work; their existence does not formalize this manuscript.

## Zhang

Shenxing Zhang, *On the linearity of the periods of subtraction games*, TCS 985 (2024), 114350; author's revised version dated 30 July 2025. Verified PDF: https://zhangshenxing.github.io/publications/Zhang2024tcs%20On%20the%20linearity%20of%20the%20periods%20of%20subtraction%20games.pdf .

Theorem 1.4's fixed base sets contain 1 with all moves odd, are {1,b}, are {a,2a}, or are consecutive intervals. Proposition 3.1 is specifically {a,2a,c}. A common dilation preserves the ratio of the first two moves and cannot identify it with {a,4a,c}. The revised manuscript's large-c formulas imply eventual affine formulas on the primitive residue classes for each fixed a. That is a restricted instance of Conjecture 1.3, not a derivation from that conjecture. Corrections in Zhang's Remark 4 concern Ho's small-move-one tables and do not imply an error in this manuscript's unrelated records.

## Ho

Nhan Bao Ho, *On the expansion of three-element subtraction sets*, TCS 582 (2015), 35–47; inspected arXiv:1202.2986v3. Verified page: https://arxiv.org/abs/1202.2986v3 .

Lemma 1 is a related finite-window periodicity criterion; the revised manuscript reproves the proposed-word formulation and keeps minimality separate. Tables 1–3 have smallest move 1. Table 4 is additive. Table 5's family {a,b,a+b+1} restricts b=2a+r with r<=min(2,a-1), so b=4a does not satisfy it. Table 6 concerns {a,b,b+2ja}, with nonzero remainder of b modulo a; substituting b=4a would instead make c a multiple of a and violate primitive admissibility. Theorem 5's odd-a family {a,2a+1,3a} is also different. The exact classifications stated there therefore do not supply the present full family. We have not exhausted every possible consequence of the published expansion sets.

## Ward

Mark Daniel Ward, *A Conjecture about Periods in Subtraction Games*, arXiv:1606.04029v1. Verified page: https://arxiv.org/abs/1606.04029v1 . The arXiv version record is 2016; the retained PDF itself prints 28 October 2018 on its title page. We cite the immutable version identifier rather than treating that typeset date as a new arXiv version.

Conjecture 1, Case II predicts that p is the gcd of all pair sums divisible by p, among seven potential values. The special four-value conclusion here is proved from words, not assumed from that conjecture. The paper does not claim to settle arbitrary three-move games or Ward's general conjecture. Its additive Case I does not occur because c=5a is incompatible with gcd(a,c)=1 and a>=2.

## What remains unresolved about priority

The precise unmatched comparison is whether any earlier result, including consequences of Ho's expansion sets or sources cited by these authors, already yields individual outer-residue words, some rational-seam p,q values, or a version of the half-strip/balanced-necklace mechanism for this exact primitive b=4a family. The four inspected classifications do not provide the full result under these hypotheses, but that fact does not establish first publication of every component. The paper states its mathematical contribution concretely and reserves those historical comparisons. A broader archival search or author correspondence would be needed for a definitive priority claim; none is claimed here.

The manuscript also cites Miklós–Post for the losing-position perspective, explicitly distinguishing binary outcome periods from full nim-periods. Its necessary obstruction is proved within the manuscript and does not rely on identifying those two notions.
