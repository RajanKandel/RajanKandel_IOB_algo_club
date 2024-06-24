

Finding the least square fit: 
Step 1. Begin with an m × n matrix A. If A = 0, go to Step 7.
Step 2. Determine the leftmost non-zero column.
Step 3. Use elementary row operations to put a 1 in the topmost position (we call this position pivot
position) of this column.
Step 4. Use elementary row operations to put zeros (strictly) below the pivot position.
Step 5. If there are no more non-zero rows (strictly) below the pivot position, then go to Step 7.
Step 6. Apply Step 2-5 to the submatrix consisting of the rows that lie (strictly below) the pivot position.
Step 7. The resulting matrix is in row-echelon form

we can reduce a Row Echelon Form to the Reduced Row Echelon Form:
Step 8. Determine all the leading ones in the row-echelon form obtained in Step 7.
Step 9. Determine the right most column containing a leading one (we call this column pivot column).
Step 10. Use elementary row operations to erase all the non-zero entries above the leading one in the
pivot column.
Step 11. If there are no more columns containing leading ones to the left of the pivot column, then go to
Step 13.
Step 12. Apply Step 9-11 to the submatrix consisting of the columns that lie to the left of the pivot column.
Step 13. The resulting matrix is in reduced row-echelon form.

Reference:
>  https://www.math.purdue.edu/~shao92/documents/Algorithm%20REF.pdf