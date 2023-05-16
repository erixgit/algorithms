(defun factorial (n)
  (cond ((eq n 0) 1)
    (T (* n (factorial (- n 1))))))
