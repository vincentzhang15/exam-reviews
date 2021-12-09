def bubble_sort(data):
    if __name__ == "__main__": print("BUBBLE SORT ------------------------------------------------\nOriginal:", data)
    for i in range(len(data) - 1, 0, -1): # Sorted boundary
        for j in range(i): # Swap up to boundary
            if __name__ == "__main__": print(f"i:{i}, j:{j}, j+1:{j+1}", end=" ")
            if data[j] > data[j+1]: # Swap if necessary
                if __name__ == "__main__": print(f"Swapping {data[j]} and {data[j+1]}", end="")
                data[j], data[j+1] = data[j+1], data[j]
                # Concurrent swap alternative: 3 variables
            if __name__ == "__main__": print()
        if __name__ == "__main__": print(f'Pass {len(data)-i}: {data}')

if __name__ == "__main__":
    bubble_sort([3, 1, 6, 4, 9, 8])
    print('\n'*2)

"""Output
Original: [10, 2, 2, 7, 8, 1]
i:5, j:0, j+1:1
i:5, j:1, j+1:2
i:5, j:2, j+1:3
i:5, j:3, j+1:4
i:5, j:4, j+1:5
Pass 1: [2, 2, 7, 8, 1, 10]
i:4, j:0, j+1:1
i:4, j:1, j+1:2
i:4, j:2, j+1:3
i:4, j:3, j+1:4
Pass 2: [2, 2, 7, 1, 8, 10]
i:3, j:0, j+1:1
i:3, j:1, j+1:2
i:3, j:2, j+1:3
Pass 3: [2, 2, 1, 7, 8, 10]
i:2, j:0, j+1:1
i:2, j:1, j+1:2
Pass 4: [2, 1, 2, 7, 8, 10]
i:1, j:0, j+1:1
Pass 5: [1, 2, 2, 7, 8, 10]
"""



def selection_sort(data):
    if __name__ == "__main__": print("SELECTION SORT ------------------------------------------------\nOriginal:", data)
    for i in range(len(data) - 1): # < i: sorted part
        min_index = i
        for j in range(i + 1, len(data)): # Find min
            if __name__ == "__main__": print(f"i:{i}, j:{j}")
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
        if __name__ == "__main__": print(f'Pass {i+1}: {data}')
if __name__ == "__main__":
    selection_sort([10, 8, 7, 2, 2, 1])
    print('\n'*2)

"""Output
Original: [10, 8, 7, 2, 2, 1]
i:0, j:1
i:0, j:2
i:0, j:3
i:0, j:4
i:0, j:5
Pass 1: [1, 8, 7, 2, 2, 10]
i:1, j:2
i:1, j:3
i:1, j:4
i:1, j:5
Pass 2: [1, 2, 7, 8, 2, 10]
i:2, j:3
i:2, j:4
i:2, j:5
Pass 3: [1, 2, 2, 8, 7, 10]
i:3, j:4
i:3, j:5
Pass 4: [1, 2, 2, 7, 8, 10]
i:4, j:5
Pass 5: [1, 2, 2, 7, 8, 10]
"""



def insertion_sort(data):
    if __name__ == "__main__": print("INSERTION SORT ------------------------------------------------\nOriginal:", data)
    for i in range(1, len(data)): # < i sorted
        j = i
        value = data[j]
        # Shift to correct position
        while j > 0 and data[j-1] > value:
            if __name__ == "__main__": print(f"i:{i}, j:{j}, j-1:{j-1}")
            data[j] = data[j-1]
            j -= 1
        data[j] = value
        if __name__ == "__main__": print(f'Pass {i}: {data}')
if __name__ == "__main__":
    insertion_sort([10, 2, 2, 7, 8, 1])
    print('\n'*2)

"""Output
Original: [10, 2, 2, 7, 8, 1]
i:1, j:1, j-1:0
Pass 1: [2, 10, 2, 7, 8, 1]
i:2, j:2, j-1:1
Pass 2: [2, 2, 10, 7, 8, 1]
i:3, j:3, j-1:2
Pass 3: [2, 2, 7, 10, 8, 1]
i:4, j:4, j-1:3
Pass 4: [2, 2, 7, 8, 10, 1]
i:5, j:5, j-1:4
i:5, j:4, j-1:3
i:5, j:3, j-1:2
i:5, j:2, j-1:1
i:5, j:1, j-1:0
Pass 5: [1, 2, 2, 7, 8, 10]
"""