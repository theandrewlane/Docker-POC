#!/usr/bin/env python3

""" Basic Sorting Algorithms Implemented in Python """

# Original retrieved on 05-24-2016 from: https://github.com/danishm/python-sorting-algos/blob/master/sorting.py
# Altered by: Patrick Jenson

import random
import heapq
import timeit

def selection_sort(items):
	""" Implementation of selection sort """
	for i in range(len(items)):
		least = i
		for k in range(i + 1, len(items)):
			if items[k] < items[least]:
				least = k
		items[least], items[i] = items[i], items[least]     # Swap!

def bubble_sort(items):
	""" Implementation of bubble sort """
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]     # Swap!

def insertion_sort(items):
	""" Implementation of insertion sort """
	for i in range(1, len(items)):
		j = i
		while j > 0 and items[j] < items[j-1]:
			items[j], items[j-1] = items[j-1], items[j]
			j -= 1

def merge_sort(items):
	""" Implementation of merge sort """
	if len(items) > 1:
		mid = len(items) // 2
		left = items[:mid]
		right = items[mid:]

		merge_sort(left)
		merge_sort(right)

		i, j, k = 0, 0, 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				items[k] = left[i]
				i = i+1
			else:
				items[k] = right[j]
				j = j+1
			k = k+1

		while i < len(left):
			items[k] = left[i]
			i = i+1
			k = k+1

		while j < len(right):
			items[k] = right[j]
			j = j+1
			k = k+1

def quick_sort(items):
	""" Implementation of quick sort """
	if len(items) > 1:
		pivot_index = len(items) // 2
		smaller_items = []
		larger_items = []

		for i, val in enumerate(items):
			if i != pivot_index:
				if val < items[pivot_index]:
					smaller_items.append(val)
				else:
					larger_items.append(val)

		quick_sort(smaller_items)
		quick_sort(larger_items)
		items[:] = smaller_items + [items[pivot_index]] + larger_items

def heap_sort(items):
	""" Implementation of heap sort """
	heapq.heapify(items)
	items[:] = [heapq.heappop(items) for i in range(len(items))]

def getrand():
	""" Gets an array of random numbers. """
	arr=[random.randint(-50, 100) for c in range(32)]
	return arr

def main():
	""" Runs a comparison of the different basic types of sorts. """
	print("Running a comparison of the different basic types of sorts...")
	selec= timeit.timeit(stmt='selection_sort(getrand())', setup='from __main__ import selection_sort, getrand', number=5000)
	print("Selection sort: {0}s".format(round(selec, 4)))
	bubb= timeit.timeit(stmt='bubble_sort(getrand())', setup='from __main__ import bubble_sort, getrand', number=5000)
	print("   Bubble sort: {0}s".format(round(bubb, 4)))
	insrt= timeit.timeit(stmt='insertion_sort(getrand())', setup='from __main__ import insertion_sort, getrand', number=5000)
	print("   Insert sort: {0}s".format(round(insrt, 4)))
	mrge= timeit.timeit(stmt='merge_sort(getrand())', setup='from __main__ import merge_sort, getrand', number=5000)
	print("    Merge sort: {0}s".format(round(mrge, 4)))
	qck= timeit.timeit(stmt='quick_sort(getrand())', setup='from __main__ import quick_sort, getrand', number=5000)
	print("    Quick sort: {0}s".format(round(qck, 4)))
	hp= timeit.timeit(stmt='heap_sort(getrand())', setup='from __main__ import heap_sort, getrand', number=5000)
	print("     Heap sort: {0}s".format(round(hp, 4)), end="\n\n")
	return 0
	
if __name__ == '__main__':
	exit(main())
