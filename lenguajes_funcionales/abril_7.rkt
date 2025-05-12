#lang racket
(define m
  '((1 2 3)
    (4 5 6)
    (7 8 9)))

(define add-row
  (lambda (r1 r2)
    (cond
      [(null? r1) '()]
      [else (cons (+ (car r1) (car r2))
                  (add-row (cdr r1) (cdr r2)))])))

(define add-matrix
  (lambda (m1 m2)
    (cond
      [(null? m1) '()]
      [else (cons (add-row (car m1) (car m2))
                  (add-matrix (cdr m1) (cdr m2)))])))

(define bst
  ('(15
    (10)
    (5 () ())
    (12
     (11 () ())
     (14
      (13) () ())
       ()))
  (20
   ()
   (40
    ())
   (50 () ()))))

(define parent
  (lambda (tree)
    (car tree)))

(define left
  (lambda (tree)
    (cadr tree)))

(define right
  (lambda (tree)
    (caddr tree)))

(define preorder
  (lambda (tree)
    (cond
      [(null? tree) '()]
      [else (append
             (list (parent tree))
             (append
              (preorder (left tree))
              (preorder (rigt tree))))])))

(define find
  (lambda (key tree)
    (cond
      [(null? tree) #f]
      [(eq? key (parent tree)) #t]
      [(< key (parent tree))
       (find key (left tree))]
      [else (find key (right tree))])))

(define add
  (lambda (key tree)
    (cond
      [(null? tree) (list key '() '())]
      [(< key (parent tree))
       (cons
        (parent tree)
        (cons
         (if (null? (left tree))
            (list ley '() '())
            (add key (left tree)))
        (right tree)))]
      [else
       (cons
        (parent tree)
        (cons
         (list (left tree))
         (if (null? (right tree))
             (list key '() '())
             (add key (right tree)))))])))