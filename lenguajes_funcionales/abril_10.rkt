#lang racket
(filter even? '(1 2 3 4 5 6 7 8 9 10))

(define m 
  '((1  2  3  4)
    (5  6  7  8)
    (9 10 11 12)))

(define sum-matrix
  (lambda (m)
    (apply +
           (map (lambda (row) (apply + row)) m))))

(sum-matrix m)

(define transpose
  (lambda (m)
    (apply map list m)))

(transpose m)

(define quick-sort
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else
       (append
        (quick-sort
         (filter (lambda (n) (< n (car lst))) lst))
        (list (car lst))
        (quick-sort
         (filter (lambda (n) (< n (car lst))) lst)))])))

(define list-of-numbers
  (lambda (n m)
    (cond
      [(eq? n m) (list m)]
      [else (cons n (list-of-numbers (add1 n) m))])))

(define sieve-aux
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else
       (cons (car lst)
             (sieve-aux
              (filter
               (lambda (n)
                 (not (eq? (remainder n (car lst)) 0)))
               lst)))])))

(define sieve
  (lambda (n)
    (sieve-aux (list-of-numbers 2 n))))

(sieve 30)

(define gfi
  (lambda (inc)
    (lambda (n)
      (+ inc n))))

(define double
  (lambda (fn number)
    (fn (fn number))))

(define double2
  (lambda (fn)
    (lambda (number)
      (fn (fn number)))))
;; recursividad terminal
(define sum
  (lambda (n)
    (cond
      [(= n 0)]
      [else (+ n (sum (sub1 n)))])))

(define sum2-aux
  (lambda (n acc)
    (cond
      [(= n 0) acc]
      [else (sum2-aux (sub1 n) (+ n acc))])))

(define sum2
  (lambda (n)
    (sum2-aux n 0)))


;;recursiva
(define is-even
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else (cons (even? (car lst))
                  (is-even (cdr lst)))])))
(is-even '(1 2 3 4 5 6 7 8 9 10))

;; terminal
(define is-even2-aux
  (lambda (lst acc)
    (cond
      [(null? lst) acc]
      [else (is-even2-aux
             (cdr lst)
             (append acc (list (even? (car lst)))))])))

(define is-even2
  (lambda (lst)
    (is-even2-aux lst '())))

(is-even2 '(1 2 3 4 5 6 7 8 9 10))













