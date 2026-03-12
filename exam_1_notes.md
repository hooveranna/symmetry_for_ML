- Hermitian matrices
- Wonderful Orthogonality Theorem
- properties of Unitary matrices
	- $U^{\dagger}U = UU^{\dagger} = I$
	- $\langle U x | U y \rangle = \langle x | y \rangle$
	- Diagonalizable, or $\exists V, U=VDV^{\dagger}$ where $V$ is Unitary and $D$ is both diagonal and unitary
	- Eigenspaces of $U$ are orthogonal
	- $U^{-1}=U^{\dagger}$ 
- full rank matrices
- rearrangement theorem: each row/column of multiplication table must contain each element once (sudoku table rules)
- inverse of element in group is just location of Identity element in multiplication table
- matrix multiplication
- isomorphic definition (and how to check)
- vectors $v,u$ are orthogonal if $\langle v | u \rangle = 0$ 
- **orthogonal compliment** of $W$ 

#### Groups
Set of elements $G=\{g_0,...,g_n\}$\
Order of $G$ is $n$\
One $g\in G$ is identity\
$\forall g_i,g_j,g_k\in G, g_ig_j\in G, g_i(g_jg_k)=(g_ig_j)g_k, \exists g_i^{-1}$\
closed (all vals in multi table $<n$)\
create group $G$ from subset of elements ($g,h$) by calculating $gh$ until you run out

#### Subgroups
- each group $G$ has at least 2 subgroups, one that's just $I$ and one that's all elements in $G$.
- if $|G|=n$, all subgroups have number of elements equal to the factors of $n$
- find subgroups by iterating through all options of factor length, trim multiplication table to match, check if it's a valid group
- all subgroups have $I$ in them

#### Coset
If $g\in G$ are all elements in the group $G$, and $h\in H$ are all elements in the subgroup $H$ of $G$, then the "left coset of H" is $GH$, or all elements in $G$ multiplied by all elements in $H$. 

#### Conjugacy class
$a,b\in G$ are "conjugate" if, for some $X\in G$, $b=XaX^{-1}$. all together make a "conjugacy class". Identity $E$ always in conjugacy class by itself \
if you map $a$ using $x$, you get $b$. \
In code, find inverses of all $g \in G$, then loop through all $h\in G, G[i]=h$. then for each $f\in G, G[j]=f$, append `table[j][table[i][inv[j]]]` 

#### Self-conjugate (normal) subgroups
a self-conjugate subgroup $H$ of $G$ is a subgroup of $G$ where $\forall h \in H, H[i]=h$, $G[j][G[i][\text{inv}[j]]] \in H$  \
A subgroup $H$ is self-conjugate (normal) if $gHg^{-1} = H$ for all $g \in G$ 

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
4. If $||u|| > 0$, normalize $u \rightarrow \hat{u}$, add $\hat{u}$ to $Q$, update $P += \hat{u} \otimes \hat{u}^{\dagger}$

#### Orthogonal Complement
 $C = \{v \in V : \langle u, v \rangle = 0, \forall u \in U\}$. \
 Gram-Schmidt to get $P$ projector of $V$ \
get $W=I-P$  \
Gram-Schmidt again on $W^{\dagger}$ to get both $C$ and $P^{\dagger}$\
$C$ = list of orthonormal vectors spanning orthogonal compliment. **not unique** \
$P^{\dagger}$ = projector onto orthogonal compliment **unique**

#### Nullspace
First find Row space of $M$, which is conjugate of $M$'s rows \
Then find orthogonal compliment of new matrix

#### Similarity transforms
matrix $S^{n\times n}$ similar to $R^{m \times m}$ if $\exists Q$ such that $SQ=QR$. $Q$ is change of basis matrix between $S$ and $R$. \
$SQ-QR=0$\
$\sum_j S_{ij} Q_{jk} - \sum_{\ell} Q_{i\ell} R_{\ell k}=0$ \
$\sum_{j\ell} (S_{ij}\sigma_{k\ell}-\sigma_{ij}R_{\ell k}) Q_{j\ell}=0$ can re-arrange since working with scalars instead of matrices so commute \
$((S\otimes I_n)-(I_m \otimes R^T))\text{vec}(Q) =0$ since $R_{\ell k} = (R^T)_{k\ell}$ \
$(S\otimes I_n)-(I_m \otimes R^T) = P^{mn \times mn}$  \
Find nullspace of $P$, giving vectors of length $mn$\
reshape to get $Q^{m\times n}$ \
If $S,R$ lists of matrices, find $P$ for every combo of $S,R$, then stack vertically to get big $P$ then get nullspace


#### Representations of groups
Rep $D$ of group $G, |G|=n$ is a list of length $n$ of matrices. Shown as $D : G \rightarrow V \times V$ \\
$D$ is a representation of $G$ if, $\forall i,j \in [0,n], D[i] \cdot D[j] = D[G[i,j]]$ 

#### Isomorphic
Two reps $D,R$ are isomorphic if $\exists Q$ that satisfies similarity transform $DQ=QR$, or if `len(infer_change_of_basis(D,R))`>0\
**groups** might be isomorphic to each other if there's the same number of elements in each 'order'

- Tables: relabel the columns/rows, get a 'mapping'
- Reps: chainging the basis of rep, get a 'change of basis matrix

#### Homomorphism
$\rho(g_i)\rho(g_j)=rho(g_ig_j)$ or $\text{rep}(g_i)\text{rep}(g_j)=\text{rep}(G(i,j))$

#### Direct Sum
Direct sum of two reps $D,R$, or $D \oplus R = \begin{bmatrix} D & 0 \\ 0 & R \end{bmatrix}$ which is block diagonal. using `np.block()`

#### Irreducible Representation of a Group
rep $D$ of $G$ is irreducible if $\nexists U$ unitary matrix such that $U d U^{-1}$ is block diagonal for all $d \in D$. Check this by finding $Q$ in $dQ=Qd$ for all $d\in D$. $|D|=n$, and $D_i^{\ell \times \ell}$\
Sum of all dim of all irreps for $G$ is $n$, or $\sum_{i=0}^{\text{num irreps}}\ell_i^2=n$\
So if I `infer_change_of_basis(D,D)` returns $Q$ that are all constant matrices ($Q=I*k$ where $k$ is scalar), $D$ is an irrep.  


#### Regular Representation
regular rep $R$ of group $G$ is $R^{n\times n\times n}$ if $|G|=n$ \
$R^{\text{reg}}(g) |h\rangle = |gh\rangle$ where $g,h\in G$ "left reg rep"\
Each irrep $\Gamma_j$ appears exactly $\ell_j$ times when decomposing $R^{\text{reg}}$ where $|\Gamma_j|=\ell_j$
TODO: code implementation of this



If I can, I should try to summarize the strategy I took for each homework function in as short as possible language (knowing I'll be able to see the docstrings)

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