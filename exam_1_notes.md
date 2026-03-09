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

#### Subgroups
- each group $G$ has at least 2 subgroups, one that's just $I$ and one that's all elements in $G$.
- if $|G|=n$, all subgroups have number of elements equal to the factors of $n$
- find subgroups by iterating through all options of factor length, trim multiplication table to match, check if it's a valid group
#### Rules for a group
- associative
- has an identity row/column
- closed (all vals in table $<n$)
- 
#### Coset
If $g\in G$ are all elements in the group $G$, and $h\in H$ are all elements in the subgroup $H$ of $G$, then the "left coset of H" is $GH$, or all elements in $G$ multiplied by all elements in $H$. 

#### Conjugacy class
$A,B\in G$ are "conjugate" if, for some $X\in G$, $B=XAX^{-1}$. all together make a "conjugacy class". Identity $E$ always in conjugacy class by itself
In code, find inverses of all $g \in G$, then loop through all $h\in G, G[i]=h$. then for each $f\in G, G[j]=f$, append `table[j][table[i][inv[j]]]` 

#### Self-conjugate subgroups
a self-conjugate subgroup $H$ of $G$ is a subgroup of $G$ where $\forall h \in H, H[i]=h$, $G[j][G[i][\text{inv}[j]]] \in H$ 
A subgroup $H$ is self-conjugate (normal) if $gHg^{-1} = H$ for all $g \in G$ 
#### Factor group
The factor group $G/H$ treats each coset of $H$ as a single element. 

#### Projector
$\hat{v}=\frac{v}{|v|}$
$\text{proj}(v) = \hat{v} \otimes \hat{v}^{\dagger}$ 
Projector for subspace $P$ if $P=[v_1,...,v_n]$ is $P^{\text{subspace}}=\sum_{i=1}^n \text{proj}(v_i)$ 

#### Gram-Schmidt
The projector onto the space spanned by orthogonal vectors is the sum of their individual projectors.
Initialize: orthonormal vectors $Q = \{\}$, projector $P=0$
For each vector $v \in$ `vectors`:
1. Normalize $v \rightarrow \hat{v}$
2. Subtract out the existing subspace: $u = \hat{v} - P\hat{v}$
3. If $||u|| = 0$, continue (vector is already in the span)
4. If $||u|| > 0$, normalize $u \rightarrow \hat{u}$, add $\hat{u}$ to $Q$, update $P += \hat{u} \otimes \hat{u}^{\dagger}$

#### Orthogonal Complement
 $C = \{v \in V : \langle u, v \rangle = 0, \forall u \in U\}$.
 Gram-Schmidt to get $P$ projector of $V$
get $P^{\dagger}=I-P$ 
Use SVD to get $P^{\dagger}=U\Sigma V^{\dagger}$ , $C=U$ 
#### Nullspace
First find Row space of $M$, which is conjugate of $M$'s rows
Then find orthogonal compliment of new matrix

#### Similarity transforms
matrix $S^{n\times n}$ similar to $R^{m \times m}$ if $\exists Q$ such that $SQ=QR$. $Q$ is change of basis matrix between $S$ and $R$. 
$SQ-QR=0$
$\sum_j S_{ij} Q_{jk} - \sum_{\ell} Q_{i\ell} R_{\ell k}=0$ 
$\sum_{j\ell} (S_{ij}\sigma_{k\ell}-\sigma_{ij}R_{\ell k}) Q_{j\ell}=0$ can re-arrange since working with scalars instead of matrices so commute 
$((S\otimes I_n)-(I_m \otimes R^T))\text{vec}(Q) =0$ since $R_{\ell k} = (R^T)_{k\ell}$ 
$(S\otimes I_n)-(I_m \otimes R^T) = P^{mn \times mn}$  
Find nullspace of $P$, giving vectors of length $mn$
reshape to get $Q^{m\times n}$ 
If $S,R$ lists of matrices, find $P$ for every combo of $S,R$, then stack vertically to get big $P$ then get nullspace


#### Representations of groups
Rep $D$ of group $G, |G|=n$ is a list of length $n$ of matrices. Shown as $D : G \rightarrow V \times V$ 
$D$ is a representation of $G$ if, $\forall i,j \in [0,n], D[i] \cdot D[j] = D[G[i,j]]$ 


If I can, I should try to summarize the strategy I took for each homework function in as short as possible language (knowing I'll be able to see the docstrings)

special types of matrices

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
