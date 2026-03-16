- Hermitian matrices
- full rank matrices
- matrix multiplication\
**Unitary matrices**\
$U^{\dagger}U = UU^{\dagger} = cI$ constant matrix w scalar $c$\
$\langle U x | U y \rangle = \langle x | y \rangle$ **|** $U^{-1}=U^{\dagger}=[U^*]^T$ \
Diagonalizable, or $\exists V, U=VDV^{\dagger}$ where $V$ is Unitary and $D$ is both diagonal and unitary
Eigenspaces of $U$ are orthogonal \
vectors $v,u$ are orthogonal if $\langle v | u \rangle = 0$ \
**orthogonal compliment** of $W$ \
Tensor Product: for lists of matrices, $\overset{\text{kr}}{\otimes}$ each matric, stack

#### Groups
Set of elements $G=\{g_0,...,g_n\}$\
Order of $G$ is $n$ ***|*** One $g\in G$ is identity $E$ or $I$\
$\forall g_i,g_j,g_k\in G, g_ig_j\in G, g_i(g_jg_k)=(g_ig_j)g_k, \exists g_i^{-1}$\
closed (all vals in multi table $<n$)\
create group $G$ from subset of elements ($g,h$) by calculating $gh$ until you run out\
rearrangement theorem: each row/column of multi table contains each element once (sudoku table rules). \
Proof: if $g_i=g_j^{-1} X$, then $g_j g_i=g_j g_j^{-1} X=X$ (all $g$ contained). If $X=g_j g_i=g_j g_k$ then $g_j^{-1}g_j g_i=g_j^{-1}g_k$ so $g_i=g_k$ contradicting group def\
**abelian group:** multi table is symmetric ($M_{ab}=M_{ba}$)\
inverse of element in group is just location of Identity element in multi table\
order of element $g\in G$ is num times multiply by itself to get back to $g$

#### Subgroups
$S$: subset of elements in $G$ that form their own group. all have identity $I$\
each group $G$ has at least 2 subgroups, one that's just $I$ and one that's all elements in $G$.\
if $|G|=n$, all subgroups have number of elements equal to the factors of $n$\
find subgroups by iterating through all options of factor length, trim multi table to match, check if it's a valid group\
**Lagrange's Theorem:** Order of subroup $S$ always divisor of order of group $G$\
$|G|=[G:H] \cdot |H|$ where $[G:H]=$ num distinct cosets (**index** of $H$ in $G$)

#### Coset
If $g\in G$ are all elements in the group $G$, and $h\in H$ are all elements in the subgroup $H$ of $G$, then the "left coset of H" is $GH$, or all elements in $G$ multiplied by all elements in $H$. The right coset is just $HG$. \

#### Conjugacy class
$a,b\in G$ are "conjugate" if, for some $X\in G$, $b=XaX^{-1}$. all together make a "conjugacy class". Identity $E$ always in conjugacy class by itself \
if you map $a$ using $x$, you get $b$. \
In code, find inverses of all $g \in G$, then loop through all $h\in G, G[i]=h$. then for each $f\in G, G[j]=f$, append `table[j][table[i][inv[j]]]` 

#### Self-conjugate (normal) subgroups
a self-conjugate subgroup $H$ of $G$ is a subgroup of $G$ where $\forall h \in H, H[i]=h$, $G_{j,m}\in H$ where $m=G_{i,j^{-1}}$ TODO HERE \
A subgroup $H$ is self-conjugate (normal) if $ghg^{-1} = h$ for all $g \in G$, $h\in H$

#### Factor group
The factor group $G/H$ treats each coset of $H$ as a single element. 

#### Projector
$\hat{v}=\frac{v}{|v|}$ \
$\text{proj}(v) = \hat{v} \otimes \hat{v}^{\dagger}$  \
Projector for subspace $P$ if $P=[v_1,...,v_n]$ is $P^{\text{subspace}}=\sum_{i=1}^n \text{proj}(v_i)$ 

#### Gram-Schmidt
The projector onto the space spanned by orthogonal vectors is the sum of their individual projectors. \
Initialize: orthonormal vectors $Q = \{\}$, projector $P=0$ \
For each vector $v \in$ `vectors`: \
1. Normalize $v \rightarrow \hat{v}$ 
2. Subtract out the existing subspace: $u = \hat{v} - P\hat{v}$ 
3. If $||u|| = 0$, continue (vector is already in the span)
4. If $||u|| > 0$, normalize $u \rightarrow \hat{u}$, add $\hat{u}$ to $Q$, update $P += \hat{u} \otimes \hat{u}^{\dagger}$\
$P=\sum_{i=1}^{n2}v_i v_i^{\dagger}$

#### Orthogonal Complement
 $C = \{v \in V : \langle u, v \rangle = 0, \forall u \in U\}$. \
 Gram-Schmidt to get $P$ projector of $V$ \
get $W=I-P$  \
Gram-Schmidt again on $W^{\dagger}$ to get both $C$ and $P^{\dagger}$\
$C$ = list of orthonormal vectors spanning orthogonal compliment. **not unique** \
$P^{\dagger}$ = projector onto orthogonal compliment **unique**

#### Nullspace
First find Row space of $M$, which is conjugate of $M$'s rows,
Then find orthogonal compliment of new matrix w/Gram Schmidt

#### Similarity transforms (Schur's Lemma)
matrix $S^{n\times n}$ similar to $R^{m \times m}$ if $\exists Q$ such that $SQ=QR$. $Q$ is change of basis matrix between $S$ and $R$. \
$SQ-QR=0$\
$\sum_j S_{ij} Q_{jk} - \sum_{\ell} Q_{i\ell} R_{\ell k}=0$ \
$\sum_{j\ell} (S_{ij}\sigma_{k\ell}-\sigma_{ij}R_{\ell k}) Q_{j\ell}=0$ can re-arrange since working with scalars instead of matrices so commute \
$((S\otimes I_n)-(I_m \otimes R^T))\text{vec}(Q) =0$ since $R_{\ell k} = (R^T)_{k\ell}$ \
$(S\otimes I_n)-(I_m \otimes R^T) = P^{mn \times mn}$  \
Find nullspace of $P$, giving vectors $v_i$ of length $mn$\
reshape to get $Q^{m\times n}$ \
If $S,R$ lists of matrices, find $Q,P$ for every combo of $S,R$, then stack vertically to get big $P$ then get nullspace (coded in `infer_change_of_basis`)\
if $Q$ exists b/w two reps of $G$, neither are irreps unless $Q$ is 1 constant matrix \(part 2) for irreps TODO: expand


#### Representations of groups
how elements of teh group $G$ acts on vector space $V$. Homomorphisms. Rep $D$ of group $G, |G|=n$ is a list of length $n$ of matrices. Shown as $D : G \rightarrow V \times V$ \
$D$ is a representation of $G$ if, $\forall i,j \in [0,n], D[i] \cdot D[j] = D[G[i,j]]$ 

#### Isomorphic
Two reps $D,R$ are isomorphic if $\exists Q$ that satisfies similarity transform $DQ=QR$, or if `len(infer_change_of_basis(D,R))`>0\
**groups** might be isomorphic to each other if there's the same number of elements in each 'order'. **Are** isomorphic if a reordering of $g\in G$ results in $H$'s multi table. \
**isomorphisms** between groups are mappings, so $g_1\rarr h_4,...$ for all $g,h$\
**homomorphism** maps all values in $G$ to smaller set of values in $H$, so $g_1\rarr h_4, g_3\rarr h_4$\
Tables: relabel the columns/rows, get a 'mapping'\
Reps: changing the basis of rep, get a 'change of basis matrix

#### Homomorphism
comparing 2 groups with each other with some function/operation\
$\rho(g_i)\rho(g_j)=rho(g_ig_j)$ or $\text{rep}(g_i)\text{rep}(g_j)=\text{rep}(G(i,j))$

#### Direct Sum
Direct sum of two reps $D,R$, or $D \oplus R = \begin{bmatrix} D & 0 \\ 0 & R \end{bmatrix}$ which is block diagonal. using `np.block()`

#### Irreducible Representation of a Group
rep $D$ of $G$ is irreducible if $\nexists U$ unitary matrix such that $U d U^{-1}$ is block diagonal for all $d \in D$. Check this by finding $Q$ in $dQ=Qd$ for all $d\in D$. $|D|=n$, and $D_i^{\ell \times \ell}$\
Sum of all dim of all irreps for $G$ is $n$, or $\sum_{i=0}^{\text{num irreps}}\ell_i^2=n$\
So if I `infer_change_of_basis(D,D)` returns $Q$ that are all constant matrices ($Q=I*k$ where $k$ is scalar), $D$ is an irrep.  \
Number of irreps = number of conjugacy classes\
2 irreps are not equivalent if they don't have the same characters


#### Regular Representation
regular rep $R$ of group $G$ is $R^{n\times n\times n}$ if $|G|=n$ \
$R^{\text{reg}}(g) |h\rangle \rarr |gh\rangle$ where $g,h\in G$ "left reg rep"\
Each irrep $\Gamma_j$ appears exactly $\ell_j$ times when decomposing $R^{\text{reg}}$ where $|\Gamma_j|=\ell_j$\
To make $R$ from $G$'s mult table $T$, first $T$ must be reordered so identity $g_i^{-1}$ is along diagonal\
$R(g_i)_j =$ row of length $n$ that's all 0 except for value at $T_{i,j}$ which is 1.\
$(R_i)_j \rightarrow G_{ij}$, where $(R_i)_j$ is vec of zeros of length $n$, and $T_{ij}$ indicates which in $(R_i)_j$ is 1.\
If you get irreps from regular rep, make sure to check for duplicate irreps (2 irreps isomorphic=same irrep)\
for $g_i\neq E$, $\chi^{R_{\text{reg}}}(g_i)=0$. $R(E)=I_n$, so $\chi^R(E)=n$

#### Wonderful Orthogonality Theorem (WOT)
(arrow going through squares of matrices for irreps)\
(proof uses rearrangement theorem for $SR$, then Schur's lemma)\
$\sum_{i=0}^n (\Gamma_a(g_i))_{\mu\nu} (\Gamma_b(g_i^{-1}))_{\mu'\nu'} = \frac{n}{\ell_a}\delta_{\Gamma_a\Gamma_b}\delta_{\mu\mu'}\delta_{\nu\nu'}$ ($=\sum_{i=0}^n (\Gamma_a(g_i))_{\mu\nu} \left[(\Gamma_b(g_i))_{\mu'\nu'}\right]^*$ if $\Gamma$ unitary)\
$\ell_a=|\Gamma_a(g_i)|$\
all $(\mu,\nu)$ coordinates in matrices in irrep $\Gamma_a$ make a vector, which is orthogonal to the same vector in $\Gamma_b$ as long as $a\neq b$

#### Characters / Character Table
$\chi^{(\Gamma_a)}(g_i) = \text{tr}\left(\Gamma_a(g_i)\right)$, so each rep's matrices get one scalar character per $g\in G$. \
If $g_i, g_j$ in the same conjugacy class, or for some $X\in G$, $b=XaX^{-1}$, then $\chi^{(\Gamma_a)}(g_i)=\chi^{(\Gamma_a)}(g_k)$ since $\text{tr}(\Gamma_a(g_i))=\text{tr}\left(\Gamma_a(x) \Gamma_a(g_k) \Gamma_a(x)^{-1}\right)=\text{tr}\left(\Gamma_a(x)^{-1}\Gamma_a(x) \Gamma_a(b) \right)=\text{tr}(\Gamma_a(b))$\
Same num conjugacy classes as irreps\
if $B=\{b_1,b_2,b_3,...b_m\}$ is list of conjugacy classes in $G$, and $g_{b_ij}$ = $j$'th group element in conjugacy class $b_i$, then
| | $(1)$ $b_1$ | $(3)$ $b_2$ | $(w)$ $b_3$ |
|---|---|---|---|
| $\Gamma_1$ | $\chi^{(\Gamma_1)}(g_{b_1})$ | $\chi^{(\Gamma_1)}(g_{b_2})$ | $\chi^{(\Gamma_1)}(g_{b_3})$ |
| $\Gamma_2$ | $\chi^{(\Gamma_2)}(g_{b_1})$ | $\chi^{(\Gamma_2)}(g_{b_2})$ | $\chi^{(\Gamma_2)}(g_{b_3})$ |
| $\Gamma_3$ | $\chi^{(\Gamma_3)}(g_{b_1})$ | $\chi^{(\Gamma_3)}(g_{b_2})$ | $\chi^{(\Gamma_3)}(g_{b_3})$ |

where $w=|b_3|$ num elements in conjugacy class $b_3$\
Each row/column must be orthogonal to each other by WOT for characters (1 and 2 respectively)\
Conjugacy class $C_{nv}\rightarrow n = $ rotations to beginning, $v = $ includes mirrors (non-abelian)\
$\Gamma_1$ "trivial" or "scalar" rep, and $\chi^{(\Gamma_1)}(g_{b_i})=1$\
$b_1=I$, so $\chi^{(\Gamma_j)}(g_{b_1})=$ dimension of irrep\
**Pseudoscalar** irrep that = $\Gamma^{\text{scalar/trivial}}$ except for mirror conjugacy classes ($\sigma$), where character is negative \
**Pseudovector** = $\Gamma^{\text{pseudov}}$ irrep that takes $\Gamma^{\text{vec}}(-1*I)$

#### WOT for Characters
**only** true for irreps (can be used to test irrep) \
$\sum_{i=0}^n \chi^{(\Gamma_a)}(g_i) \chi^{(\Gamma_b)}(g_i^{-1})=n\delta_{\Gamma_a,\Gamma_b}=\sum_{i=0}^n \chi^{(\Gamma_a)}(g_i) \left[\chi^{(\Gamma_b)}(g_i)\right]^*=\sum_{j=0}^m N_j \chi^{\Gamma_a}(g_{b_j})\left[\chi^{\Gamma_b}(g_{b_j})\right]^*$ where $N_j=|b_j|$ \
$g_{b_j}=$ any element $g\in b_j$\
2 is $\sum_{i=0}^p N_a \chi^{\Gamma_i}(g_{b_a})\left[\chi^{\Gamma_i}(g_{b_b})\right]^* = n \delta_{ab}$ (column of char table must be orthogonal), $p=$ number of irreps for $G$.

#### Decompose rep into irreps/Decomposition Formula
any rep can be decomposed into irreps\
Num times irrep $\Gamma_a$ appears in representation $D$ with character $\chi^{(D)}$ is:\
$a_a = \frac{1}{n}\sum_{j=0}^m N_j \left[\chi^{(\Gamma_a)}(g_{b_j})\right]^* \chi^{(D)}(g_{b_j}) =  \frac{1}{n}\sum_{i=0}^n \left[\chi^{(\Gamma_a)}(g_{i})\right]^* \chi^{(D)}(g_i)$\

#### Vibrational Modes
"Internal degrees of freedom of object with $m$ atoms" aka changing bond lengths & angles\
look at all DoF, $-$ translation & rotation\
each molecule has 3 modes: Rotation ($P^{\text{rot}}$), translation ($P^{\text{tranzs}}$), vibration ($P^{\text{vib}}$). Their projectors are: \
$P^{\text{vib}} = I_{3m} - P^{\text{trans}} - P^{\text{rot}}$\
$[P^{\text{trans}}]^{3m\times 3m} = |t_x\rangle \langle t_x| + |t_y\rangle \langle t_y| + |t_z\rangle \langle t_z|$ all atoms moved by the same displacement\
$t_x = \frac{1}{\sqrt{m}}(\underset{\text{atom 1}}{1,0,0},\underset{\text{atom 2}}{1,0,0},...,\underset{\text{atom }n}{1,0,0})$\
$[P^{\text{rot}}]^{\times} = \sum_{i=1}^{d_{\text{rot}}} \hat{d}_i \hat{d}_i^T$ where $d_{\text{rot}}=3$ for nonlinear molecules and 2 for linear. \
A tiny rotation about axis $\hat{a}$ displaces $i$ at position $r_i$ relative to center of mass by $\delta r_i = \hat{a} \times r_i$\
$d_{u\in\{x,y,x\}}^{1\times 3m} = \begin{bmatrix}\hat{e}_u \times r_1 \\ \vdots \\ \hat{e}_u \times r_n\end{bmatrix}$ where $r_i$ is the location of the $i$'th atom. $d_u$ not orthogonal to each other\
Gram-Schmidt orthonormalize $d$, and outer-product it with itself, then add $P_x + P_y + P_z$\
$[\Gamma^{\text{vec}}]^{3\times 3}$: all possible \
**Permutation Representation:** $\Gamma^{\text{a.s.}}(g_i)$ for each $g_i$, matrix multiply $[\Gamma^{\text{vec}}]^{3\times 3}$ with each vector position $r_i(x,y,z)$ and check which vertex it lands on. \
$[\Gamma^{\text{a.s.}}]^{n\times m \times m}\rightarrow[\Gamma^{\text{a.s.}}(g_i)]^{m \times m}$ if $\Gamma^{\text{vec}}(g_i) r_j = r_k$, $\Gamma^{\text{a.s.}}(g_i)[k,j]=1$, else 0\
**Vibration Representation**: \
$[\Gamma^{\text{a.s.}} \overset{\text{kr}}{\otimes}\Gamma^{\text{vec}}]^{n\times 3m \times 3m} = \Gamma^{\text{a.s.}}(g_i) \overset{\text{kr}}{\otimes}\Gamma^{\text{vec}}(g_i) \forall g_i \in G$ (aka tensor product them together)\
If doing character table, remember $\text{trace}(a \otimes b) = \text{trace}(a)\text{trace}(b)$\
Find $Q^{3m \times n_{\text{vib}}}$ orthonormal basis for column space of $P^{\text{vib}}$ w/gram-schmidt \
$[\Gamma^{\text{vib}}(g_i)]^{n_{\text{vib}}\times n_{\text{vib}}} = Q^T(g_i)[[\Gamma^{\text{a.s.}}(g_i)]^{m\times m} \otimes [\Gamma^{\text{vec}}(g_i)]^{3\times 3}]^{3m \times 3m} Q(g_i)$

$[\Gamma^{\text{vib}}]^{3m-6\times 1} = [\Gamma^{\text{a.s.}}]^{m\times m} \otimes [\Gamma^{\text{vec}}]^{3\times 3} - [\Gamma^{\text{trans}}]^{3\times 1} - [\Gamma^{\text{rot}}]^{3\times 1}$ \
vib mode 'transforms as' irrep. when application of $g\in G$ to vib mode gives same characters as irrep. 1=preserved, else=not. if dim of irrep $>1$, compare to conj class where char has same dim.

#### Counting irrep multiplicities 
$n_i = \langle \chi_i | \chi_i \rangle =$

#### Special types of matrices

| Type| Condition | Key Property|
| ----------------- | --------- | --- |
| Orthogonal (real) | $A^T A=AA^T=I$ , $\text{det}=\pm 1$ (special=+1)| $A^T=A^{-1}$ |
| Unitary (complex) | $A^{\dagger}A=AA^{\dagger}=I$ $\|\text{det}\|=1$ (special no \|\|) | $A^{\dagger}=(A^*)^T=A^{-1}$ |
| Symmetric | $A=A^{T}$| real eigenvalues|
| Hermitian | $A=A^{\dagger}=(A^*)^T$ | real eigenvalues|

subspace $X$ of matrix $M^{m \times n}$ with rank $r$ are all vectors $x\in X$ that satisfy:
Row space: $Mx \neq 0$, dim $r$, conjugated rows of $M$
Nullspace: $Mx = 0$, dim $n-r$, orthogonal compliment of row space
Column space: $M^{\dagger}x=0$ dim $r$
Left nullspace: $M^{\dagger}y=0$ dim $m-r$

## Notes From Review Session

#### Projection Matrix
$P^V$ go from generic vector to closest vector in subspace $V$, = $w w^T$ if $w$ in orthonormal basis for $V$.

**Schur's lemma part 1 is most important**
if matrix $M$ commutes with all r in rep, either m is constant or rep is reducible.\




### Guidelines from course
#### For Sure
- Understand definitions:
	- group, subgroup, self-conjugate (normal) subgroup, order of a group, conjugacy classes, left coset, right coset, isomorphism between two groups, homomorphism between two groups, abelian vs. non-abelian groups (Lectures 2-3)
	- group representation (matrices + vector space), reducible representation, irreducible representation, (left and right) regular representation of a finite group, character of a representation
- Understand results of Lemmas and Theorems proved / shown in class:
	- Rearrangement Theorem
	- Lagrange's Theorem
	- Schur's Lemma
	- The Wonderful Orthogonality Theorem for Representations
	- The Wonderful Orthogonality Theorem for Character
- Know when to use and how to interpret outputs of the functions you've coded in exercises from the symm4ml class repository
	- First exercise: groups module
	- Second and third exercises: functions from linalg and rep modules
	- Fourth exercise: vib_modes module
- Understand and be able to use the general procedure for finding vibrational modes.

#### Maybe
- Generate a group from a subset of elements (done)
- Difference between abelian vs. non-abelian groups, and classifying group based on multiplication table
- Making, completing, and identifying errors in multiplication and character tables
- Use results of Lemmas and Theorems to classify nature of representations
- Interpret the output of the functions you have coded in the first 4 exercises in this course (groups, linalg, rep, vib_modes)
- Construct the Left and Right Regular Representations from the multiplication table of a group
- Decompose representation into irreps of a given group given characters of the representation.
- Use the Wonderful Orthogonality Theorem for Character and basic facts of representations to complete an incomplete character table.
- Compute the irreps of possible vibrational modes "by hand" if given a character table and a (simple) set of points that have the symmetry of that character table.
- Identify possible irreps that could lower the symmetry of a system from a group to a given subgroup.
- Given a step in a proof, identify what property of groups / representations or lemma / theorem is being used to e.g. equate the left and right hand sides of an equation.
- Use of np.einsum, broadcasting, and reshape to translate equations into code.
	- There are exercises for np.einsum and Broadcasting here under the 2. Einsum and 3. Broadcasting headings, respectively.