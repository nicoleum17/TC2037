#lang racket
;; enlist: list => list
(define enlist
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else (cons
             (cons (car lst) '()) (enlist (cdr lst)))])))

;;invert-pairs: list => list
(define invert-pairs
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [(list? (car lst))
       (cons (list (cadar lst) (caar lst))
             (invert-pairs (cdr lst)))])))

;;deep-reverse: list => list
(define deep-reverse
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [(list? (car lst)) (append (deep-reverse (cdr lst))
                               (list (deep-reverse (car lst))))]
      [else (append (deep-reverse (cdr lst))
                    (list (car lst)))])))

;; igual: atom list => number
(define igual
  (lambda (a lst)
    (cond
      [(null? lst) 0]
      [(equal? a (car lst)) (+ 1 (igual a (cdr lst)))]
      [else 0])))

;; a_list: atom number => list
(define a_list
  (lambda (a n)
    (cond
      [(= n 0) '()]
      [(> n 0) (cons a (a_list a (sub1 n)))])))

;; resto: atom list => list
(define resto
  (lambda (a lst)
    (cond
      [(null? lst) '()]
      [(equal? a (car lst)) (resto a (cdr lst))]
      [else lst])))

;; pack: list => list
(define pack
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else (cons (a_list (car lst) (igual (car lst) lst))
                  (pack (resto (car lst) lst)))])))

;; encode: list => list
(define encode
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else (cons (list (igual (car lst) lst) (car lst))
                  (encode (resto (car lst) lst)))])))