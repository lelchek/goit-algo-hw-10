# Definite Integral Calculation Using Monte Carlo Method

## Task

Compute the value of a definite integral using the Monte Carlo method and verify the result by comparing it with the numerical result obtained using the `quad` function from the `scipy.integrate` module.

---

## Function and Interval

The following function was used:

\[
f(x) = x^2 + 10
\]

The integral was evaluated on the interval:
\[
[0, 2]
\]

---

## Reference Result (SciPy `quad`)

\[
\int_{0}^{2} (x^2 + 10)\,dx = 22.666666666666667
\]

---

## Monte Carlo Results

The Monte Carlo simulation was executed with different numbers of experiments and compared with the result obtained using `scipy.integrate.quad`.

| Number of experiments | Monte Carlo result | Absolute error | Relative error |
|----------------------|-------------------|---------------|----------------|
| 100                  | 22.679645         | 0.012979      | 0.0573 %       |
| 500                  | 22.676472         | 0.009805      | 0.0433 %       |
| 1000                 | 22.665278         | 0.001389      | 0.0061 %       |

---

## Conclusion

The Monte Carlo approximation is close to the reference value obtained using `scipy.integrate.quad`.
Increasing the number of experiments leads to a decrease in both absolute and relative errors, confirming the correctness of the implementation.

