# Generated outputs

Run the following command from the repository root to regenerate this folder:

```powershell
python code\variance_extension.py
```

Files:

- `variance_summary.txt`: human-readable parameters, moments, slopes, turning points, and
  the final counterexample verdict.
- `variance_results.csv`: every grid value used in the numerical check, including a direct
  variance and the value from the quadratic identity. The script stops with an assertion
  error if the two disagree.
- `variance_curve.svg`: a vector chart of the three variance paths on the range where all
  numerical examples retain an interior effort solution.

No third-party Python packages are required.
