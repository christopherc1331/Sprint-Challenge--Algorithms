#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(log n)

because your runtime is dependant on (n) but you are stepping towards the end of the loop at increments of n\*n instead of +1 increments

b)
O(n log n)

the first (n) is because you are looping over (n), and that in and of itself is going to require a time complexity of (n) to complete

the (log n) is because your runtime is dependant on (n) but you are stepping towards the end of the loop at increments of n\*n instead of +1 increments,

c)

O(2^n)

because you're using recursion to reach the base case

## Exercise II

1.  first you would check the middle floor in the building to see if the egg breaks at that level
2.  if the egg does break then you would check the middle level betwen the current level and the floor level
3.  if the egg doesn't break then you would check the floor above
4.  it breaks then (f) is the current floor
5.  if the egg doesn't break on step 4 then you would check the middle level between the current level and the top floor
6.  you would repeat steps 1-5 until you reached the base case in steps 4 & 5 then return f

This would be a time complexity of (log n) because every time we don't find the right floor, we cut the possible floors that could be our solution in half
