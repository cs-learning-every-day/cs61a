(define (caar x) (car (car x)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))

; ; Problem 15
; ; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (helper idx items)
    (if (null? items)
        nil
        (cons (list idx (car items))
              (helper (+ idx 1) (cdr items)))))
  (helper 0 s))

; END PROBLEM 15
; ; Problem 16
; ; Merge two lists LIST1 and LIST2 according to COMP and return
; ; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond 
    ((null? list1)
     list2)
    ((null? list2)
     list1)
    (else
     (let [(item1 (car list1))
           (item2 (car list2))]
       (if (comp item1 item2)
           (cons item1 (merge comp (cdr list1) list2))
           (cons item2 (merge comp list1 (cdr list2))))))))

; END PROBLEM 16
(merge < '(1 5 7 9) '(4 8 10))

; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))

; expect (10 9 8 7 5 4 3 1)


; (1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1)
; ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1))
; ; Problem 17
(define (nondecreaselist s)
  ; BEGIN PROBLEM 17
  (cond 
    ((null? s)       nil)
    ((null? (cdr s)) (list s))
    ((> (car s) (cadr s))
        (cons (list (car s))
              (nondecreaselist (cdr s))))
    (else (let [(next (nondecreaselist (cdr s)))]
            (cons (cons (car s)
                        (car next))
                  (cdr next))))))

; END PROBLEM 17
