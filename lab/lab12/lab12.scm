; Lab 14: Final Review

(define (compose-all funcs)
  (define (helper x)
    (define (iter lst y)
      (if (null? lst)
          y
          (iter (cdr lst) ((car lst) y))))
      (iter funcs x))
    helper
)