class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort (in-place) the array of (position, speed) tuples
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse = True)
        # Get an empty stack of time floats
        fleets = []
        # Iterate over the array of (position, speed) tuples
        for p, s in cars:
            # Append the current fleet
            fleets.append((target - p) / s)
            # Join the previous fleets
            if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        # Return the number of fleets
        return len(fleets) 
        