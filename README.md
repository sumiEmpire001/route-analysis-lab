# Route Analysis Lab

A Python standard-library CLI implementing Dijkstra's algorithm for shortest paths on weighted, directed graphs. It validates edge weights, reports total path cost, and handles unreachable destinations.

## Run

```bash
python routes.py examples/graph.json Depot Market
```

Input is JSON with an `edges` array. Each edge contains `from`, `to`, and a finite, nonnegative numeric `cost`. The output is the least-cost node sequence and total cost, or null values if no route exists.

## Tests

```bash
python -m unittest discover -s tests -v
```

Eight tests run through GitHub Actions on Python 3.10, 3.12, and 3.13.

## Limitations

This is a graph algorithm demonstration, not a real-world navigation service. It does not calculate road distances, live traffic, travel times, or turn-by-turn directions. Input costs are user supplied.
