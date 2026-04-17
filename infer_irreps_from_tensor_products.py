
def infer_irreps_from_tensor_products(
    X: np.ndarray, n: int, *, tol: float = 1e-8
) -> List[np.ndarray]:
    """Infers irreducible representations from successive tensor products of a representation.
    Input:
        X: np.array [lie_dim, d, d] - generators of a representation.
        n: int - number of non-isomorphic irreducible representations to infer.
    Output:
        Ys: List[np.array] - list of n generators of irreducible representations,
            each an np.array of shape [lie_dim, d', d'] for some d'.
    """
    x_prime = rep.direct_sum(np.zeros((X.shape)),rep.direct_sum(X, np.conj(X)))
    print(f"x_prime shape = {x_prime.shape}")
    m = 0
    irreps = []
    irr = lie.decompose_rep_into_irreps(x_prime, tol=tol)
    for ir in irr:
        if(not any((lie.are_isomorphic(ir, irrep_, tol=tol) for irrep_ in irreps))):
            #new_irrs.append(ir)
            irreps.append(ir)
            print(f"x_prime shape = {x_prime.shape}, irreps len = {len(irreps)}")
    print(len(irreps))
    while len(irreps) < n+2:
        print(f"entering while loop, tensoring irrep with shape {irreps[m].shape}")
        for k in range(0,m+1):
            print(f"m={m}, k={k}")
            print(f"entering while loop, tensoring irrep with shape {irreps[m].shape} with {irreps[k].shape}")
            new_i_p = lie.tensor_product(irreps[m], irreps[k])
            print(f"new_i_p shape {new_i_p.shape}")
            new_irrep = decompose_rep_into_irreps(new_i_p, tol=tol)
            print(f"{len(new_irrep)} new irreps")
            #print(f"new_irrep shape = {new_irrep[0].shape}")
            for ir in new_irrep:
                print(f"new irrep shape: {ir.shape}")
                if(not any((lie.are_isomorphic(ir, irrep_, tol=tol) for irrep_ in irreps))):
                    #new_irrs.append(ir)
                    irreps.append(ir)
                    if len(irreps) == n+2: break
                    print(f"new irrep shape = {ir.shape},irreps len = {len(irreps)}")
            if len(irreps) == n+2: break
        m = m + 1
    irreps = sorted(irreps, key=lambda x: x.shape[1])
    return irreps[:n]