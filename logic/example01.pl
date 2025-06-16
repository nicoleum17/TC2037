ladron(juan).

gusta(maria, comida).
gusta(maria, vino).
gusta(X, Y) :- gusta(Y, vino).

% comentario
puede_robar(X, Y) :- ladron(X), gusta(X,Y).
