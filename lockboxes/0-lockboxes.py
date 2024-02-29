#!/usr/bin/python3
"""First Algorithm Problem"""


def canUnlockAll(boxes):
    unlockedBoxes = set([0])
    leftToExplore = [0]
    while leftToExplore:
        actualBoxeIndex = leftToExplore.pop()
        keys = boxes[actualBoxeIndex]
        for key in keys:
            if key < len(boxes) and key not in unlockedBoxes:
                unlockedBoxes.add(key)
                leftToExplore.append(key)
                
    return len(unlockedBoxes) == len(boxes)

