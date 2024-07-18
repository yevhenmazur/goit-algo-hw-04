# goit-algo-hw-04
Homework for the topic "Sorting algorithms"

### The task
Compare the three sorting algorithms: _merge_, _insert_, and _Timsort_ in terms of execution time. The analysis should be supported by empirical data obtained by testing the algorithms on different data sets. Empirically test theoretical estimates of algorithm complexity, for example, by sorting on large arrays.

### The result

![The result image](https://github.com/yevhenmazur/goit-algo-hw-04/blob/main/result.png?raw=true)

### Conclusion
_Timsort_ shows tens of thousands of times faster performance than _Insertion Sort_ and hundreds of times faster than _Merge Sort_.
Another interesting thing is that it inherits from Merge Sort the ability to run faster when the array is highly unordered (mixing_factor ~= 100).
