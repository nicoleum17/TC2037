pow(_, 0, 1).
pow(A, B, Res) :-
    B > 0,
    B1 is B - 1,
    pow(A, B1, Res1),
    Res is Res1 * A.
