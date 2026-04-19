## Expected to do/know:
- Understand definitions
  - tensor product, tensor product decomposition, product tables of irreps
  - ~~Lie group~~,  (infinitesimal) generators, ~~commutator~~, ~~Lie algebra~~
  -  ~~group convolution~~, steerable filter
  -  Cartesian tensors with and without symmetry constraints on indices
  -  Branching of irreps under subgroups
  -  Fourier basis, planewaves (translations), circular harmonics (SO(2)), spherical harmonics (SO(3)).
  -  Spherical harmonics as basis of functions on sphere and Wigner-Ds as basis of functions on SO(3).
-  Understand results proved in class or class materials:
   -  ~~How similarity transforms, direct sums, and tensor products of representations of Lie group representations can be rewritten as operations on the generators of the Lie group.~~
   -  ~~Understand the steps in proving equivariance for group convolution.~~
-  Know when to use and how to interpret outputs of the functions you've coded in exercises from the symm4ml class repository.
      -  `group`, `linalg`, `rep`, `vib_modes` (on Exam 1)
      -  `lie`, `so3`, `grid`, `group_conv` functions (not on Exam 1)


## May be expected to do/know
-  Re-write operations on the representations of a Lie group as operations on the generators.
-  Describe or justify procedures for finding basis functions of a particular domain (e.g. products of coordinates or decompose permutation reps)
-  Determine the Lie algebra for a set of generators.
-  Given a step in a proof, identify what property of groups / representations / irrep basis functions is being used to e.g. equate left and right hand sides of an equation.
-  Use code output to interpret branching rules of irreps under subgroup.
-  Identify number of trivial degrees of freedom in tensor.
-  Be able to use a character table to identify how a particular basis function transform (analogous what we did for vibrational modes).
-  Describe how to create representations of $SO(2), O(2),SO(3),$ or $O(3)$ from generators of respective Lie group and mirrors ($O(2)$) or inversion ($O(3)$)
-  Be comfortable with viewing and interpreting spherical harmonic signals.
-  Use Schur's Lemma to restrict the parameters / weights of simple neural network operations like linear layers and convolutional filters.
-  

# Exam Question Topics:
## 2024 Exam 1:
- Question 5: Group Convolution (went through, questions)

## 2024 Practice Exam:
- Question 1: Neural network?
  - Group Actions
  - Activation Functions
- Question 2: Cartesian Tensors
  - `lie.infer_irreps_from_tensor_products`
  - `lie.tensor_product`
  - tensor product selection rule
- Question 3: $SU(2)$
  - Lie groups 
  - Lie Group generators
  - Lie Algebra
  - `lie.are_isomorphic`

## 2024 Exam:
- Question 1: Steerable Convolution (went through, questions)
- Question 2: $SO(4)$, Lie Groups
- Question 3: Spherical Harmonics

## 2025 Exam:
- Question 1: 4d Rotation and Cartesian Tensors
- Question 2: Convolution on Cubes
- 
