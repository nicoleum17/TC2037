#lang racket
(define lst '(1 2 3 4 5 6 7 8 9 10))

(define count
  (lambda (lst)
    (cond
      [(null? lst) 0]
      [else (+ 1 (count (cdr lst)))])))

(define sum
  (lambda (lst)
    (cond
      [(null? lst) 0]
      [else (+ (car lst)
               (sum (cdr lst)))])))

(define count-even
  (lambda (lst)
    (cond
      [(null? lst) 0]
      ;; (equal? (remainder (car lst) 2) 0)
      [(even? (car lst))
       (+ 1 (count-even (cdr lst)))]
      [else (count-even (cdr lst))])))

(define greater
  (lambda (lst)
    (cond
      [(null? lst) 'error]
      [(null? (cdr lst)) (car lst)]
      [else
       (let ((result (greater (cdr lst))))
         (if (> (car lst) result)
             (car lst)
             result))])))

(define zeros
  (lambda (n)
    (cond
      [(<= n 0) '()]
      [else (cons 0
                  (zeros (sub1 n)))])))

(define dec
  (lambda (n)
    (cond
      [(<= n 0) '()]
      [else (cons n (dec (sub1 n)))])))

(define incR
  (lambda (n)
    (reverse (dec n))))

(define inc
  (lambda (n)
    (cond
      [(<= n 0) '()]
      [else (append (inc (sub1 n))
                    (list n))])))

(define fib-list
  (lambda (n)
    (cond
      [(<= n 1) '(1)]
      [(= n 2) '(1 1)]
      [else (let ((other (fib-list (sub1 n))))
              (cons (+ (car other) (cadr other)) other))])))