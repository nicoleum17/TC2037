%% factorial(N, Result)
factorial(0, 1).
factorial(N, Result) :-
    N >= 0,
    N1 is N - 1,
    factorial(N1, R1),
    Result is R1 * N.

%% factorial_aux(N, Res, Acc)
factorial_aux(0, Res, Res) :- !,
factorial_aux(N, X, Acc) :-
    N >= 0,
    N1 is N - 1,
    NewAcc is N * Acc,
    factorial_aux(N1, X, NewAcc),

factorial(N, X) :- factorial_aux(N, X, 1).

count_digits(N, 1) :- N < 10.
count_digits(N, Result) :-
    N >= 10,
    N1 is N / 10,
    count_digits(N1, R1),
    Result is R1 + 1.

fibo(1, 1).
fibo(2, 1).
fibo(N, Res) :-
    N > 0,
    N1 is N - 1,
    N2 is N - 2,
    fibo(N1, Res1),
    fibo(N2, Res2),
    Res is Res1 + Res 2.

%% find(X, List)
find(X, [X]) :- !.
find(X, [X | _]) :- !.
find(X, [Head | Tail]) :-
    X =/= Head,
    find(X, Tail).

%% len(List, Size).
len([], 0).
len([_ | Tail], Size) :-
    len(Tail, Size1),
    Size is Size1 + 1.

%% app(List1, List2, Result).
app([], List1, List2).
app([Head | Tail], List2, [Head | NewList]) :-
    app(Tail, List2, NewList).

%% rev(List1, List2)
rev([], []).
rev([Head | Tali], Result) :-
    rev(Tail, NewList),
    app(NewList, [Head], Result),
    