#lang racket
(define inc1
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else (cons (add1 (car lst))
                  (inc1 (cdr lst)))])))

(define append2
  (lambda (lst1 lst2)
    (cond
      [(null? lst1) lst2]
      [else (cons (car lst1)
                  (append2 (cdr lst1) lst2))])))

(define reverse2
  (lambda (lst)
    (cond
      [(null? lst) '()]
      [else (append (reverse2 (cdr lst))
                    (list (car lst)))])))

(define deep-list
  '(1 (2 3) (4 (5 6 7 (8 (((9))) 10) 11))))

(define deep-count
  (lambda (lst)
    (cond
      [(null? lst) 0]
      [(list? (car lst)) (+ (deep-count (car lst))
                            (deep-count (cdr lst)))]
      [else (+ 1 (deep-count (cdr lst)))])))

(define deep-sum
  (lambda (lst)
    (cond
      [(null? lst) 0]
      [(list? (car lst)) (+ (deep-sum (car lst))
                            (deep-sum (cdr lst)))]
      [else (+ (car lst) (deep-sum (cdr lst)))])))

(define deep-even
  (lambda (lst)
    (cond
     [(null? lst) 0]
     [(list? (car lst)) (+ (deep-even (car lst))
                           (deep-even (cdr lst)))]
     [(even? (car lst)) (+ 1
                           (deep-even (cdr lst)))])))

(define deep-greater
  (lambda (lst)
         (cond
           [(null? lst) 0]
           [(list? (car lst))
            (let ((one (deep-greater (car lst)))
                  (two (deep-greater (cdr lst))))
              (if (> one two) one two))]
           [else
            (let ((result (deep-greater (cdr lst))))
              (if (> (car lst) result) (car lst) result))])))

