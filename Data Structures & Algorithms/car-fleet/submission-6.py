class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Get the zipped array of (pos, spe) tuples
        cars = [(p, s) for p, s in zip(position, speed)]
        # Sort the array of (pos, spe) tuples
        cars.sort(reverse = True)
        # Get an empty stack of time floats
        fleets = []
        # Iterate over the array of (position, speed) tuples
        for p, s in cars:
            # Append the current fleet
            fleets.append((target - p) / s)
            # Join the previous fleet
            if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        # Return the number of fleets
        return len(fleets) 