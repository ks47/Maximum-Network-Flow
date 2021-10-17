# Maximum-Network-Flow
Python implementation of Edmunds Karp algorithm for a multi-source, multi-sink graph

## Problem
To maximize the flow (could be water, traffic, etc.) in a given network starting from the multiple given sources, going to multiple given sinks.

## Solution
The above solution creates a pseudo-source and a pseudo-sink for the given network and then applies Edmunds Karp algorithm to it. In EK algorithm we continuoulsy find a path from source to sink using breadth first search and then increase the flow in that path by whatever its bottleneck value is (min weight among the edges of the path).
