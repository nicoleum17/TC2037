#lang racket
(define insert
  (lambda (pred key lst)
    (cond
      [(null? lst) (list key)]
      [(> key (car lst)) (cons key lst)]
      [(pred key (car lst)) (cons key lst)]
      [else (cons (car lst)
                  (insert pred key (cdr lst)))])))

(define insertion-sort
  (lambda (pred lst)
    (cond
      [(null? lst) '()]
      [else
       (insert pred
               (car lst)
               (insertion-sort pred
                               (cdr lst)))])))

(define compare
  (lambda (p1 p2)
    (if (eq? (car p1) (car p2))
        (< (cadr p1) (cadr p2))
        (< (car p1) (car p2)))))