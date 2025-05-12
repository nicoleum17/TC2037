#lang racket
;; duplicate: lst => lst
(define duplicate
  (lambda (lst)
    (cond
      [(null? lst)'()]
      [else (cons (car lst)
                  (cons (car lst)
                        (duplicate (cdr lst))))])))

;; positives: lst => lst
(define positives
  (lambda (lst)
         (cond
           [(null? lst)'()]
           [(positive? (car lst))
                 (cons (car lst)
                       (positives (cdr lst)))]
           [else (positives (cdr lst))])))

;; list-of-symbols: lst => bool
(define list-of-symbols?
  (lambda (lst)
    (cond
      [(null? lst) #t]
      [(symbol? (car lst)) (list-of-symbols? (cdr lst))]
      [else #f])))

;; swapper: atom atom lst => lst
(define swapper
  (lambda (a b lst)
    (cond
      [(null? lst)'()]
      [(eq? a (car lst)) (cons b
                             (swapper a b (cdr lst)))]
      [(eq? b (car lst)) (cons a
                             (swapper a b (cdr lst)))]
      [else (cons (car lst)
                  (swapper a b (cdr lst)))])))

;; dot-product: lst lst => number
(define dot-product
  (lambda (lsta lstb)
    (cond
      [(null? lsta) 0]
      [(null? lstb) 0]
      [else (+ (* (car lsta) (car lstb))
             (dot-product (cdr lsta) (cdr lstb)))])))





