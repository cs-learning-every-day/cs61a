
(define (mult x y)
    (define (helper y sum)
        (if (= 0 y)
            sum
            (helper (- y 1) (+ x sum))))
    (helper y 0))


(define (sum-satisfied-k lst f k)
    (define (helper lst k sum)
        (cond ((and (null? lst) (not (= k 0)))
                0)
            ((= k 0) sum)
            (else (if (f (car lst))
                    (helper (cdr lst) (- k 1) (+ sum (car lst)))
                    (helper (cdr lst) k sum)))))
    (helper lst k 0))

(define (remove-range lst i j)
    (define (helper lst idx res)
        (if (null? lst)
            res
            (if (and (>= idx i) (<= idx j))
                (helper (cdr lst) (+ idx 1) res)
                (helper (cdr lst) (+ idx 1) (append res (list (car lst)))))))
    (helper lst 0 '()))
