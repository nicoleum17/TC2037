#lang racket
;; sumatoria: list -> int
(define sumatoria
  (lambda (datos)
    (sumatoria-aux datos 0)))

(define sumatoria-aux
  (lambda (datos acc)
    (if (null? datos)
        acc
        (sumatoria-aux (cdr datos) (+ (car datos) acc)))))
 
;; incrementa: list -> list
(define incrementa
  (lambda (datos)
    (incrementa-aux datos '())))

(define incrementa-aux
  (lambda (datos acc)
    (if (null? datos)
        (reverse acc)
        (incrementa-aux (cdr datos) (cons (+ 1 (car datos)) acc)))))

