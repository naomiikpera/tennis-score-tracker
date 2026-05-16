# Tennis Match

This is a simple Python program that determines the winner of a tennis-style match based on a score record.

## How It Works

- Each round is separated by a dash.
- A `1` represents a point for player 1.
- A `2` represents a point for player 2.
- The player with more points in a round wins that round.
- If both players have the same number of points, both players get a round point.

## Example

```python
result = tennis_match("Anthony", "Caitlin", "1122-22211-11122-1212-")
print(result)
