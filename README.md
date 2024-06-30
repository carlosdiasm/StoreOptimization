# Store Optimization Project

## Introduction

Optimization problems involve selecting the best element from a set of available alternatives according to a specific criterion [Boyd and Vandenberghe 2004]. In the context of Computer Science, these problems are often classified as NP-Hard, meaning they do not have a known deterministic polynomial solution [Hochba 1997]. This project aims to present two design techniques to address these intractable problems: Brute Force and Implicit Enumeration (Branch-and-Bound).

The optimization problem analyzed in this project is the optimization of the location of franchised stores in a given region. The goal is to identify an arrangement of locations that avoids competition between stores of the same franchise and presents the lowest installation cost for these stores in the region of interest.

For each of the \( n \) franchises, there is a list of candidate locations. For each candidate point, the installation cost and its \( x, y \) coordinates are known. Any two franchises cannot be closer than \( D \) kilometers. All coordinates \( x, y \) of the candidate points are within the range of 0 to 500 kilometers. If it is not possible to find a solution that includes all \( n \) franchises due to the distance restriction, the optimal solution will be the one that maximizes the number of installed franchises while respecting the distance restriction.

The following sections will present the solutions to the problem, considering their worst-case time and memory complexity. The implementation of the programs, which were divided into modules, will also be presented. Finally, a test report of the programs will be included, presenting some possible store location arrangements and their respective installation costs, the complexity analysis of the developed programs, and the comparison of the execution times and efficiency between the Brute Force and Branch-and-Bound techniques [Lawler and Wood 1966].


## References

- Boyd, S., & Vandenberghe, L. (2004). Convex Optimization.
- Hochba, D. S. (1997). Approximation Algorithms for NP-Hard Problems.
- Lawler, E. L., & Wood, D. E. (1966). Branch-and-Bound Methods: A Survey.

## Contact

For any questions or issues, please open an issue on this repository or contact the authors.
