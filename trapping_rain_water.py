# You are given an array non-negative integers heights which represent an elevation map. Each value heights[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

class Solution:
    def trap(self, height: List[int]) -> int:

        trimmed = self.trim_edges(height)

        highest_height = max(trimmed)

        length_bars = len(trimmed)

        full_volume = 0

        for i in range(highest_height, -1, -1):
            beginning = -1
            end = -1
            found_beginning = False
            found_end = False
            blocks = 0
            for j in range(length_bars):
                if trimmed[j] > i and not found_beginning:
                    beginning = j
                    found_beginning = True
                    continue

                if trimmed[j] > i and not found_end:
                    end = j
                    found_end = True
                    continue

                if trimmed[j] > i:
                    blocks += 1
                    end = j

            if beginning != -1 and end != -1:
                volume = end - beginning - blocks - 1
                print("beginning: " + str(beginning) + "\nend: " + str(end) + "\nblocks: " + str(
                    blocks) + "\nvolume: " + str(volume) + "\n")
                full_volume += volume

        return full_volume

    def trim_edges(self, height: List[int]) -> List[int]:

        trimmed_left = []

        edge = True
        for i in range(len(height) - 1):
            if height[i] < height[i + 1] and edge:
                continue
            edge = False
            trimmed_left.append(height[i])
        trimmed_left.append(height[-1])

        trimmed_right = []

        edge = True
        for i in range(len(trimmed_left) - 1):
            if height[-i - 1] < height[-i - 2] and edge:
                continue
            edge = False
            trimmed_right.append(height[-i - 1])
        trimmed_right.append(trimmed_left[0])

        trimmed_right.reverse()

        return trimmed_right
