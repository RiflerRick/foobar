"""
Clearly the naive approach is not going to work in all possible cases. One point of failure for the above approach was that each time trying to find the least time and going for that may not be accurate. 

For instance if we are at the bulkhead and it is found that the least distance is at start, we go to start instead of trying to save a bunny. This may lead to less number of bunnies rescued.
On the other hand for some other case it may be necessary to actually go to start from where we can gain time and actually save more bunnies than actually trying to save bunny first hand.

Clearly the accurate approach would be a graph algorithm that can easily find out at each step whether it is possible to save more bunnies.
"""