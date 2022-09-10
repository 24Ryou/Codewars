# Array.diff
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list `a`, which are present in list `b` keeping their order.

```c
array_diff({1, 2}, 2, {1}, 1, *z) == {2} (z == 1)
```

array_diff([1,2],[1]) == [2]
