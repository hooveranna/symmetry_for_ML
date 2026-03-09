import itertools
import numpy as np
import math
from pprint import pprint
from typing import List, Tuple, Set, FrozenSet

def permutation_matrices(n):
    """Generates all permutation matrices of n elements

    Input:
        n: int

    Output:
        matrices: np.array of shape [n!, n, n]
    """
    answer = []
    #loop through every possible ordering of the n spotx
    for spot in itertools.permutations(range(0, n),n):
        empty_matrix = np.zeros((n,n), dtype=np.int_)
        for i, v in enumerate(spot):
            empty_matrix[i, v] = 1
        answer.append(empty_matrix)

    return np.array(answer)

def generate_group(matrices, decimals=4):
    """Generate new group elements from matrices (group representations)

    Input:
        matrices: np.array of shape [n, d, d] of known elements
        decimals: int number of decimals to round to when comparing matrices

    Output:
        group: np.array of shape [m, d, d], where m is the size of the resultant group
    """
    keep_trying = True
    while keep_trying:
        matrix_adding = matrices.copy()
        for pair in itertools.product(matrices, repeat=2):
            new_matrix = np.round(np.dot(pair[0], pair[1]), decimals)
            matrix_adding = np.vstack((matrix_adding, [new_matrix]))
            print(f"len of new_matrices = {len(matrix_adding)}")
        new_matrices = np.unique(matrix_adding, axis=0)
        if len(new_matrices) == len(matrices):
            keep_trying = False
        matrices = new_matrices.copy()
    return matrices

def make_multiplication_table(matrices: np.ndarray, *, tol: float=1e-08) -> np.ndarray:
    """Makes multiplication table for group.

    Input:
        matrices: np.array of shape [n, d, d], n matrices of dimension d that form a group under matrix multiplication.
        tol: float numberical tolerance

    Output:
        Group multiplication table.
        np.array of shape [n, n] where entries correspond to indices of first dim of matrices.
    """
    n = len(matrices)
    result = np.zeros((n,n), dtype=np.int_)
    for i in range(0, n):
        result[i, 0] = i
        for j in range(1, n):
            # find matrix given by matrices[i] * matrices[j]
            result_mat = np.round(np.dot(matrices[i], matrices[j]), 8)
            # find that index in matrices
            loc = np.all(matrices == result_mat, axis=(1,2)).tolist().index(True)
            # set
            result[i, j] = loc
    return result

def identity(table: np.ndarray) -> int:
    """Returns the index of the identity element.

    Input:
        table: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the group.

    Output:
        Index of identity element.

    Raises:
        ValueError("No or multiple identities") if there is no or multiple identities.
    """
    id_found = 0
    id_m = -1
    for i in range(0, len(table)):
        row = table[i]
        if row.tolist() == list(range(0, len(table))):
            id_found = id_found + 1
            id_m = i
    if id_found != 1:
        raise ValueError("No or multiple identities")
    return id_m

def inverses(table: np.ndarray) -> np.ndarray:
    """Returns the indices of the inverses of each element.

    Input:
        table: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the group.

    Output:
        np.array of shape [n] where the ith entry is the index of the inverse of the ith element.

    Raises:
        ValueError("Every element does not have one inverse") if there is no or multiple inverses.
    """
    id_v = identity(table)
    n = len(table)
    # make a list of length n, with every 'inverse' set to -1
    answer = np.full(n, -1)
    for i in range(0, n):
        for j in range(0, n):
            # if this spot has the identity, it hasn't been marked before, 
            if table[i, j] == id_v:
                if answer[i] != -1 or table[i, j] != table[j, i]:
                    raise ValueError("Every element does not have one inverse 1")
                else:
                    answer[i] = j
    if np.any(answer == -1):
        raise ValueError("Every element does not have one inverse 3")
    return answer

def is_closed(table: np.ndarray) -> bool:
    """Tests whether the multiplication table is closed.
    aka all vals in the table are one of the rows of the table

    Input:
        table: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the group.

    Output:
        True if the table represents a closed binary operation, False otherwise.
    """
    n = len(table)
    for i in range(0, n):
        for j in range(0, n):
            if table[i, j] >= n:
                return False
    return True

def is_associative(table: np.ndarray) -> bool:
    """Tests whether the multiplication table is associative.
    literally just if all operations are associative within the table

    Input:
        table: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the group.

    Output:
        True if the table represents an associative binary operation, False otherwise.
    """
    associative = True
    n = len(table)
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                if i != j or i != k or j != k:
                    if table[table[i,j], k] != table[i, table[j, k]]:
                        associative = False
                        return associative
    return associative

def test_group(table: np.ndarray):
    """Tests whether the multiplication table is valid.

    Input:
        table: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the group.

    Raises:
        ValueError("Invalid indices") if the table contains invalid indices (is not closed).
        ValueError("No or multiple identities") if the table does not contain exactly one identity.
        ValueError("Every element does not have one inverse") if not every element has an inverse.
        ValueError("Not associative") if the table is not associative.
    """
    if not is_closed(table):
        raise ValueError("Invalid indices")
    identity(table)
    inverses(table)
    if not is_associative(table):
        raise ValueError("Not associative")
    
def factors(n):
    divisors = set()
    
    # Loop runs up to square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            
            # If both divisors are same (perfect square), add only once
            if n // i == i:
                divisors.add(i)
            else:
                
                # Add both divisors
                divisors.add(i)
                divisors.add(n // i)
    return divisors

def subgroups(table):
    """Find all subgroups of group.

    Input:
        table: np.array of shape [n, n]

    Output:
        Set of frozensets of element indices.
    """
    n = len(table)
    # each group has at least 2 subgroups: just the identity, and all values
    result = {frozenset(list(range(0, n))), frozenset({identity(table)})}
    fs = factors(n)
    fs.remove(n) # already handled above
    fs.remove(1) # can only be the identity, also handled above
    # the number of elements in a subgroup will always be = a factor of n
    for factor in fs:
        # for all combinations of elements in the group of length factor
        for subset in itertools.combinations(list(range(0,n)), factor):
            table_m = table.copy()
            for i in range(n-1, -1, -1):
                if i in subset:
                    # if the element is in the subset, move it so it's in the spot of subset
                    table_m[table_m == i] = subset.index(i)
                else:
                    # if this element in the table isn't in the subset, remove it from the new table
                    table_m = np.delete(table_m, i, axis=0)
                    table_m = np.delete(table_m, i, axis=1)
            
            try:
                # check if the newly made multiplication table is a group!
                test_group(table_m)
            except ValueError:
                continue
            result.add(frozenset(subset))
    return result

def right_coset(table, subgroup_indices):
    """Returns the right coset of the ith element.

    Input:
        table: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the group.
        subgroup_indices: Indices of elements in the subgroup.

    Output:
        Set of right cosets for each element in the group. Each coset is represented as a frozenset of indices.

    Example:
        right_coset(np.array([[0, 1], [1, 0]]), {0}) == {frozenset({1}), frozenset({0})}
    """
    n = len(table)
    result = {frozenset(subgroup_indices)}
    for i in range(0, n):
        new_s = []
        for s in subgroup_indices:
            new_s.append(table[s][i])
        if frozenset(new_s) not in result:
            result.add(frozenset(new_s))
    return result

def left_coset(table, subgroup_indices):
    """Returns the left coset of the ith element.

    Input:
        table: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the group.
        subgroup_indices: Indices of elements in the subgroup.

    Output:
        Set of left cosets for each element in the group. Each coset is represented as a set of indices.
    """
    n = len(table)
    result = {frozenset(subgroup_indices)}
    for i in range(0, n):
        new_s = []
        for s in subgroup_indices:
            new_s.append(table[i][s])
        if frozenset(new_s) not in result:
            result.add(frozenset(new_s))
    return result

def conjugacy_classes(table: np.ndarray)-> set[frozenset[int]]:
    """Returns the conjugacy classes of the group.

    Input:
        table: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the group.

    Output:
        Set of conjugacy classes. Each conjugacy class is a set of integers.
    """
    n = len(table)
    result = set()
    inv = inverses(table)
    for i in range(0, n):
        conj = []
        for j in range(0, n):
            # for all pairs of values in `table`, get the value at table[i]
            conj.append(table[j][table[i][inv[j]]])
        result.add(frozenset(conj))
    return result

def selfconjugate_subgroups(table: np.ndarray) -> set[frozenset[int]]:
    """Returns the set of self-conjugate (normal) subgroups.
    
    Input:
        table: np.array of shape [n, n] where entries correspond to indices of group elements.

    Output: set[frozenset[int]]
        list of all selfconjugate subgroups of table
    """
    sgs = subgroups(table)
    inv = inverses(table)
    result = set()
    for sg in sgs:
        is_self_conjugate = True
        for h in sg:
            for g in range(0, len(table)):
                if table[g][table[h][inv[g]]] not in sg:
                    is_self_conjugate = False
                    break
        if is_self_conjugate:
            result.add(frozenset(sg))

    return result

def factor_group(table, selfconj_sub):
    """Returns the factor group of the group.

    Input:
        table: np.array of shape [n, n] where entries correspond to indices of group elements.
        selfconj_sub: set of indices for self-conjugate subgroup.

    Output:
        Multiplication table of factor group of order n2 as sets of  elements of the group
        np.array sets of ints of shape [n2, n2]
        Multiplication table of factor group in terms of indices of right cosests
        np.array of shape [n2, n2] where entries correspond to indices of first dim of matrices.
    """
    coset_table = list(right_coset(table, selfconj_sub))
    coset_table2 = left_coset(table, selfconj_sub)
    print(f"coset table = {coset_table}")

    int_table = []
    for i in range(0, len(coset_table)):
        new_row = []
        for j in range(0, len(coset_table)):
            c_1 = list(coset_table[i])
            c_2 = list(coset_table[j])

            val = table[c_1[0], c_2[0]]
            for k in coset_table:
                if val in k:
                    print(f"c_1 is {c_1}, c_2 is {c_2}, val is [{c_1[0]},{c_2[0]}] = {val}, k is {k}")
                    new_row.append(coset_table.index(k))
                    break
        int_table.append(new_row)

    return ([list(coset_table), list(coset_table2)], int_table)

def isomorphisms(table_src: np.array, table_dst: np.array)-> set[tuple[int]]:
    """Finds all isomorphisms between two multiplication tables.
    Returns a set of tuples h of length n.

    Input:
        table_src: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the source group.
        table_dst: np.array of shape [n, n] where the entry at [i, j] is the index of the product of the ith and jth elements in the destination group.

    Output:
        A set of isomorphisms encoded as tuples ``h`` of length ``n``.
        Each element ``h[i]`` is the index of the image of the ith element in the source group.
    """
    result = set()
    n = len(table_src)
    for subset in itertools.permutations(list(range(0,n)), n):
        print(subset)
        # takes table_dst and switches the ordering around to match the ordering in subset
        t = permute_mul_table(table_dst, np.array(subset))
        is_iso = True
        if np.all(subset == (0, 2, 3, 1)):
            print("stop here")
        for i in range(0,n):
            for j in range(0,n):
                if t[i][j] != table_src[i][j]:
                    is_iso = False
                    break
        print(t)
        print("_________")
        if is_iso:
            result.add(subset)
    return result


################ end of groups hw #####################
################ beginning of lin alg #################


def projector(v):
    """Return the projector onto the vector v.

    Input:
        v: a d dimensional complex vector

    Output:
        P: a rank 1 matrix such that P @ v = v
    """
    n = len(v)
    v_mag = np.linalg.norm(v)
    if v_mag == 0:
        v_hat = np.zeros((n))
    else:
        v_hat = v / v_mag
    v_dag = v_hat.conj().T
    return np.kron(v_hat, v_dag).reshape(n,n)

def gram_schmidt(vectors, *, tol=1e-8):
    """Return the Gram-Schmidt orthonormalization of the vectors.

    Input:
        vectors: an (n1, d) matrix of n1 complex vectors of dimension d
        tol: a tolerance for the zero vector

    Output:
        Q: an (n2, d) matrix of n2 orthonormal vectors, with n2 <= n1
        P: a (d, d) projector onto the span of the orthonormal vectors in Q
    """
    u_hat_list = []
    proj_mat = np.zeros((len(vectors[0]), len(vectors[0])))
    for i in range(0, len(vectors)):
        v = vectors[i]
        n = len(v)
        # step 1: normalize v
        v_mag = np.linalg.norm(v)
        if v_mag == 0:
            v_hat = np.zeros((n))
        else:
            v_hat = v / v_mag
        # step 2: subtract out existing subspace to find u
        u = v_hat - np.dot(proj_mat, v_hat)
        u_mag = np.linalg.norm(u)
        # step 3: if u_mag = 0, continue
        if u_mag < tol:
            continue
        else:
            # step 4: normalize u, add u to Q, update P
            u_hat = u / u_mag
            u_hat_list.append(u_hat)
            proj_mat = proj_mat + projector(u_hat)
    return (np.array(u_hat_list), proj_mat)

def orthogonal_complement(vectors, *, tol=1e-8):
    """Return orthogonal vectors spanning the orthogonal complement of the span of the input vectors.

    Input:
        vectors: an (n1, d) matrix of n1 complex vectors of dimension d
        tol: a tolerance for the zero vector

    Output:
        Q: an (n2, d) matrix of n2 orthonormal vectors spanning the orthoganl complement, with d - n1 <= n2 <= d
        P: a (d, d) projector onto the orthogonal complement of the input vectors
    """
    _, p = gram_schmidt(vectors, tol=tol)
    
    p_dag = np.eye(len(p)) - p

    u, _, _ = np.linalg.svd(p_dag)
    return (u, p_dag)

def nullspace(matrix, *, tol=1e-8):
    """Return the nullspace of the matrix.

    Input:
        matrix: an (n, d) matrix of n complex vectors of dimension d
        tol: a tolerance for the zero eigenvalue

    Output:
        Q: an (m, d) matrix containing orthogonal vectors spanning the nullspace (obtained by Gram-Schmidt)
        P: a (d, d) projector onto the span of the nullspace
    """
    row_space = []
    for i in range(0, len(matrix)):
        row_space.append(np.conjugate(matrix[i]))
    
    return orthogonal_complement(np.array(row_space), tol=tol)

def infer_change_of_basis(x1: np.ndarray, x2: np.ndarray, *, tol=1e-8):
    """Compute the change of basis matrix from X1 to X2.
    tip: Use the function nullspace

    Input:
        X1: an (n, d1, d1) array of n (d1, d1) matrices
        X2: an (n, d2, d2) array of n (d2, d2) matrices

    Output:
        Sols: An (m, d1, d2) array of m solutions.
        Each solution is a (d1, d2) matrix that satisfies X1 @ S = S @ X2,
        and together they form an orthognal basis for the set of solutions (under the inner product of the flattened versions).
    """
    nsp_input = []
    print(f"n = {len(x1)}, d1 = {len(x1[0])}, d2 = {len(x2[0])}")
    for x1 in x1:
        for x2 in x2:
            main_mat = np.kron(x1, np.eye(len(x2))) - np.kron(np.eye(len(x1)), x2.T)
            print(main_mat)
            # stacking the matrices since we want the same Q
            for row in main_mat:
                nsp_input.append(row)
    print(nsp_input)
    print(f"len(nsp_input) = {len(nsp_input)}, {len(nsp_input[0])}")
    print(f"{np.array(nsp_input).shape}")
    answer = nullspace(np.array(nsp_input), tol=tol)
    return answer[0]

def is_a_representation(table, rep, *, tol=1e-8):
    """Checks if rep is a representation of the group represented by a given multiplication table.

    Input:
        table: np.array [n, n] where table[i, j] = k means i * j = k.
        rep: np.array [n, d, d] describing a possible representation of the group. rep[i] is a matrix corresponding to the action of the i-th element of the group.

    Output:
        True if rep is a representation.
    """
    # YOUR CODE HERE
    # if `rep` is a representation of `table`, then 
    n = len(table)
    # confirm that the identity element maps to the identity matrix
    loc_id = identity(table)
    if not np.allclose(rep[loc_id], np.eye(len(rep[loc_id])), atol=tol):
        return False
    for i in range(0, n):
        for j in range(0, n):
            left = np.dot(rep[i], rep[j])
            right = rep[table[i, j]]
            if not np.allclose(left, right):
                return False
    return True

def are_isomorphic(rep1, rep2, *, tol=1e-8):
    """Checks if representations are isomorphic.

    Input:
        rep1: np.array [n, d, d] representation of group. rep1[i] is a matrix that
            represents i-th element of group.
        rep2: np.array [n, d, d] representation of group. rep2[i] is a matrix that
            represents i-th element of group.
        You can assume that rep1 and rep2 are valid group representations.
        
    Output:
        True if representations are isomorphic.
    """
    basis_change = infer_change_of_basis(rep1, rep2, tol=tol)
    if len(basis_change) > 0:
        return True
    return False

def direct_sum(rep1, rep2):
    """Computes direct sum of two representations.

    Input:
        rep1: np.array [n, d1, d1] representation of group. rep[i] is a matrix that
            represents i-th element of group.
        rep2: np.array [n, d2, d2] representation of group. rep[i] is a matrix that
            represents i-th element of group.
        You can assume that rep1 and rep2 are valid group representations.

    Output:
        Direct sum of representations. np.array [n, d1 + d2, d1 + d2].
    """
    n = len(rep1)
    d1 = len(rep1[0])
    d2 = len(rep2[0])
    rep = []
    print(np.zeros((d1, d2)))
    print(f"n = {n}, d1 = {d1}, d2 = {d2}")
    for i in range(0, n):
        new_mat = np.block([
            [rep1[i], np.zeros((d1, d2))],
            [np.zeros((d2, d1)), rep2[i]]
        ])
        rep.append(new_mat)
    return rep

def is_an_irrep(table, rep, *, tol=1e-8):
    """Checks if rep is an irreducible representation of group represented by multiplication table.

    Input:
        table: np.array [n, n] where table[i, j] = k means i * j = k.
        rep: np.array [n, d, d] representation of group. rep[i] is matrix that
            represents i-th element of group.

    Output:
        True if rep is an irreducible representation.
    """
    if not is_a_representation(table, rep):
        return False
    q_list = infer_change_of_basis(rep, rep)
    q_shape = q_list.shape
    if len(q_shape) == 2 and q_shape[0] == q_shape[1]:
        if not np.allclose(q_list / q_list.item(0), np.eye(len(q_list)), tol):
            return False

    # check if all matrices in q_list are constant matrices (scalar multiples of the identity)
    for q in q_list:
        if not np.allclose(q / q.item(0), np.eye(len(q)), tol):
            return False

    return True

def check_orthogonality_theorem(irreps):
    """Checks orthogonality theorem for a set of input representations.

    Input:
        irreps: List of representations, np.arrays of shape [n, d, d], where n is the order of group and d is the dimension of the representation. Not necessarily irreducible!

    Output:
        True if the theorem holds (i.e. the representations in the list are irreducible, unitary and pairwise orthogonal and have the appropriate self-inner product), False otherwise.
    """
    n = len(irreps)
    h = len(irreps[0])
    f = len(irreps[0][0])

    # for each pair of irreducible representations
    for k in range(0, n):
        for m in range(0, n):
            gamma_j = irreps[k]
            gamma_jp = irreps[m]
            ell_j = len(gamma_j[0])
            # for each spot in the representation
            for mu_1, nu_1 in itertools.combinations_with_replacement(
                list(range(0, f)),2
            ):
                for mu_2, nu_2 in itertools.combinations_with_replacement(
                    list(range(0, f)),2
                ):
                    d = []
                    d_p = []
                    # get vector for each rep in gammas
                    for i in range(0, h):
                        d.append(gamma_j[i][mu_1][nu_1])
                        d_p.append(gamma_jp[i][mu_2][nu_2])
                    left_total = np.sum(np.inner(d, d_p))
                    if (
                        (k != m or mu_1 != mu_2 or nu_1 != nu_2) and 
                        not np.allclose(left_total, 0)
                    ):
                        print(f"gamma_j = {gamma_j} not orthogonal to gamma_jp = {gamma_jp}")
                        return False
                    if k == m and not np.allclose(left_total, h / ell_j):
                        print(f"gamma_j = {gamma_j} inner product ({left_total}) not equal to h/l = {h}/{ell_j} = {h / ell_j}")
                        return False
    return True

################ end of linalg_rep1 hw #####################

def similarity_transform(rep: np.array, U: np.array) -> np.array:
    """Returns transformed representation U rep U^{-1}.

    Input:
        rep: np.array [n, d, d] representation of the group. rep[i] is a matrix that
            represents the representation at the i-th element of group.
        U: np.array [d, d] invertible complex matrix

    Output:
        Transformed representation. np.array [n, d, d]
    """
    rep_prime = []
    for r in rep:
        right_half = np.inner(r, U)
        left_half = np.dot(U, right_half)
        rep_prime.append(left_half)
    return rep_prime

def character_table(
        irreps: List[np.array], 
        conj_classes: Set[FrozenSet[int]]
) -> np.ndarray:
    """Returns character table for a group.

    Input:
        irreps: List of np.arrays of shape [n, d, d], where n is the order of the group and d is the dimension of the irrep (which may vary).
        conj_classes: List of sets of integers, where the total number of integers across all sets in the list is n.
        Each set contains elements of a conjugacy class.

    Output:
        Character table. np.array [len(irreps), len(conj_classes)] (where the class / irrep order is unchanged)
    """

    c_table = np.zeros((len(irreps), len(conj_classes)))

    for i in range(0, len(irreps)):
        irrep = irreps[i]
        for j in range(0, len(conj_classes)):
            conj_class = list(list(conj_classes)[j])
            c_table[i,j] = np.trace(irrep[conj_class[0]])
    
    return c_table

def regular_representation(table: np.array) -> np.array:
    """Returns regular representation for group represented by a multiplication table.

    Input:
        table: np.array [n, n] where table[i, j] = k means i * j = k.

    Output:
        Regular representation. array [n, n, n] where reg_rep[i, :, :] = D(i) and D(i)e_j = e_{ij}.
        Equivalently, D(g) |h> = |gh>
    """
    n = len(table)
    reg_rep = []
    for i in range(0, n):
        right_side = np.zeros((n,n))
        for j in range(0,n):
            right_side[table[i,j],j] = 1
        reg_rep.append(np.inner(right_side, np.identity(n)))
    return reg_rep

def unique_with_tol(a: np.array, *, tol: float):
    """Find unique elements of an array with a tolerance.

    Input:
        a: np.array of shape num_elements x d1 x ... x dm of which to find the unique elements
        tol: tolerance

    Output:
        centers: np.array of shape num_clusters x d1 x ... x dm containing the centers of the clusters
        inverses: np.array of shape num_elements containing the index of the corresponding center for each element of a

    Raises:
        ValueError: if the cluster are not clearly distinct

    Note:
        this function is "stable", the first element always belongs to the
        first cluster, the second element not in the first cluster belongs to the
        second cluster, etc.
    """
    assert a.ndim >= 1
    shape = a.shape
    a = a.reshape(len(a), -1)

    distances = np.linalg.norm(a[:, None] - a[None, :], axis=-1)
    inverses = -1 * np.ones(len(a), dtype=int)
    index = 0

    while True:
        (m,) = np.nonzero(inverses == -1)
        if len(m) == 0:
            break
        i = m[0]

        if np.any(inverses[distances[i] < tol] != -1):
            raise ValueError("The clusters are not clearly distinct.")

        inverses[distances[i] < tol] = index

        index += 1

    centers = np.zeros((np.max(inverses) + 1, a.shape[1]), dtype=a.dtype)
    np.add.at(centers, inverses, a)
    centers /= np.bincount(inverses)[:, None]

    centers = centers.reshape(len(centers), *shape[1:])
    return centers, inverses

def eigenspaces(
    val: np.ndarray, vec: np.ndarray, *, tol: float = 1e-8
) -> List[tuple[float, np.ndarray]]:
    """Regroup eigenvectors by eigenvalues.

    Input:
        val: eigenvalues (output of np.linalg.eig)
        vec: eigenvectors (output of np.linalg.eig)
        tol: tolerance for the eigenvalues similarity

    Output:
        list of (eigenvalue, eigenvectors) tuples
    """
    unique_val, i = unique_with_tol(val, tol=tol)
    return [(val, vec[:, i == j]) for j, val in enumerate(unique_val)]

def decompose_rep_into_irreps(rep: np.array, *, tol: float=1e-08) -> List[np.array]:
    """Decomposes representation into irreducible representations.

    Input:
        rep: np.array [n, d, d] representation of group. rep[g] is a matrix that
            represents g-th element of group.

    Output:
        Irreducible representations. List of np.array [n, d_i, d_i] where d_i is a dimension of i-th irrep.
            Note: you can output the irreps in any order and in any basis.
            If an irrep is included multiple times in the decomposition (i.e. with multiplicity greater than 1), please simply include it multiple times in the output list.
    """
    n = len(rep)
    # step 1
    # dim of Q is some m rxr square matrices
    q = infer_change_of_basis(rep, rep)
    # check if q is just one matrix or not
    if len(q.shape) == 2:
        q = [q]
    m = len(q)
    q_bar = np.zeros((len(q[0]), len(q[0][0])))
    w = []
    # step 2
    # |alpha| = m
    alpha = np.random.rand(m)
    for i in range(0,m):
        q_bar_i = alpha[i] * q[i]
        q_bar = q_bar + q_bar_i
        # step 3: find eval and evect, then find espace W
    q_bar_eval, q_bar_evect = np.linalg.eig(q_bar)
    w = eigenspaces(q_bar_eval, q_bar_evect, tol=tol)
    pprint(w)
    print(len(w))
    print(len(w[0]))
    l = len(w)
    p = []
    b = []
    for j in range(0,l):
        print(f"at j = {j}, w[{j}][1], with shape {w[j][1].shape}= {w[j][1]}")
        b_j, p_j = gram_schmidt(w[j][1].T)
        p.append(p_j)
        b.append(b_j.T)
    rho = []
    pprint(b)
    print(f"r = {l}")
    for k in range(0,l):
        rho_k = []
        print(f"b[{k}] = {b[k]}")
        for g in range(0,n):
            rho_k_m = np.matmul(b[k].conj().T, np.matmul(rep[g],b[k]))
            rho_k.append(rho_k_m)
        rho.append(rho_k)
    return rho

def are_isomorphic(rep1, rep2, *, tol=1e-8):
    """Checks if representations are isomorphic.

    Input:
        rep1: np.array [n, d, d] representation of group. rep1[i] is a matrix that
            represents i-th element of group.
        rep2: np.array [n, d, d] representation of group. rep2[i] is a matrix that
            represents i-th element of group.
        You can assume that rep1 and rep2 are valid group representations.
        
    Output:
        True if representations are isomorphic.
    """
    basis_change = infer_change_of_basis(rep1, rep2, tol=tol)
    if len(basis_change) > 0:
        return True
    return False

def infer_irreps(table: np.array, *, tol: float=1e-08) -> List[np.array]:
    """Infers irreducible representations of group represented by multiplication table.

    Input:
        table: np.array [n, n] where table[i, j] = k means i * j = k.

    Output:
        Irreducible representations. List of np.array [n, d, d] where d is a dimension of irrep.
            Note: you can output the irreps in any order and in any basis.
    """
    # each row of the multiplication table directly incodes a regular representaiton matrix
    n = len(table)
    # so we should have n nxn matrices in this representation
    rep = []
    for i in range(0,n):
        rep_i = np.zeros((n,n))
        for j in range(0,n):
            rep_i[table[i][j]][j] = 1
        rep.append(rep_i)
    # 2: decompose into irreps
    irreps = decompose_rep_into_irreps(np.stack(rep), tol=tol)
    irreps_to_remove = []
    print(f"len of irreps is {len(irreps)}")
    k = 0
    # 3: remove duplicates
    for i in range(0, len(irreps)):
        for j in range(0, len(irreps)):
            if i != j and i not in irreps_to_remove and j not in irreps_to_remove:
                if are_isomorphic(irreps[i], irreps[j], tol=tol):
                    irreps_to_remove.append(j)
    irreps = [v for idx, v in enumerate(irreps) if idx not in irreps_to_remove]
    print(f"len of irreps = {len(irreps)}, should have removed {len(irreps_to_remove)}, irreps are:")
    print(irreps)
    return irreps

def tensor_product(rep1: np.array, rep2: np.array) -> np.array:
    """Returns tensor product of two representations.

    Input:
        rep1: np.array [n, d1, d1] a representation of the group.
        rep2: np.array [n, d2, d2] another representation of the group.

    Output:
        Tensor product of rep1 and rep2. np.array [n, d1*d2, d1*d2], equal to the Kronecker product of rep1[i,:,:] and rep2[i,:,:] at group element i
    """
    n = len(rep1)
    rep = []
    for i in range(0,n):
        rep.append(np.kron(rep1[i], rep2[i]))
    return np.stack(rep)

def reduce_tensor_product(rep1: np.array, rep2: np.array, rep3: np.array) -> np.ndarray:
    """Returns the change of basis matrix that reduces the tensor product of rep1 and rep2 into rep3.

    Input:
        rep1: np.array [n, d1, d1]
        rep2: np.array [n, d2, d2]
        rep3: np.array [n, d3, d3]

    Output:
        Basis of the space of change of basis. mat = np.array [n_sol, d1, d2, d3]
            where each Q=mat[i].reshape(d1*d2,d3) satisfies tensor_product(rep1, rep2) @ Q = Q @ rep3,
            and such that the mat[i] matrices together form a basis for the subspace of all such Q.
    """
    d1 = len(rep1[0])
    d2 = len(rep2[0])
    d3 = len(rep3[0])
    # rho_4 = (rho_1 \otimes rho_2)
    rho_4 = tensor_product(rep1, rep2)

    qs = infer_change_of_basis(rho_4, rep3)
    ans = qs.reshape(len(qs), d1, d2, d3)
    return ans
    