; cerner_2^5_2019

; Fibonacci Sequence
; Calculates the nth Fibonacci number using Tail Recursion
; To calculate 50th Fibonacci number: '(fib 50)'

(define a 0)
(define b 1)
(define temp 0)

(define (fib n)
  (cond ((<= n 0) a)
        ((= n 1) b)
        (else (and (and (and (set! temp b) (set! b (+ a b)) (set! a temp)) (fib (- n 1) a b))))))