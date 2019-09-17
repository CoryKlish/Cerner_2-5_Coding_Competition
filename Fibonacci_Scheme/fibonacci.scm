; cerner_2^5_2019

; Fibonacci Sequence
; Calculates the nth Fibonacci number using Tail Recursion
; Pass 'a' as 0 (First Fibonacci number)
; Pass 'b' as 1 (Second Fibonacci number)
; To calculate 50th Fibonacci number: '(fib 50 0 1)'

(define (fib n a b)
  (cond ((<= n 0) a)
        ((= n 1) b)
        (else (fib (- n 1) b (+ a b))) 