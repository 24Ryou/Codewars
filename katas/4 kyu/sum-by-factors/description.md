# Sum by Factors
Given an array of positive or negative integers 

<code> I= [i<sub>1</sub>,..,i<sub>n</sub>]</code>

you have to produce a sorted array P of the form 

<code>[ [p, sum of all i<sub>j</sub> of I for which p is a prime factor (p positive) of i<sub>j</sub>] ...]</code>

P will be sorted by increasing order of the prime numbers.
The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

#### Example:

```fortran
I = (/12, 15/); // result = "(2 12)(3 27)(5 15)"
```
```python
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
```
```elixir
I = [12, 15] # result = [{2, 12}, {3, 27}, {5, 15}]
```
```rust
I = [12, 15] # result = [(2, 12), (3, 27), (5, 15)]
```
```swift
I = [12, 15] # result = [(2, 12), (3, 27), (5, 15)]
```
```ruby
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
```
```java
I = {12, 15}; // result = "(2 12)(3 27)(5 15)"
```
```cpp
I = {12, 15}; // result = "(2 12)(3 27)(5 15)"
```
```c
I = {12, 15}; // result = "(2 12)(3 27)(5 15)"
```
```csharp
I = {12, 15}; // result = "(2 12)(3 27)(5 15)"
```
```clojure
I = [12, 15] ; result = [[2, 12], [3, 27], [5, 15]]
```
```haskell
I = [12, 15] -- result = [(2,12),(3,27),(5,15)]
```

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
