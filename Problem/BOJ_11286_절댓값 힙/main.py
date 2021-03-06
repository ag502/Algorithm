from sys import stdin
import heapq

def main():
    num_of_number = int(stdin.readline())
    heap = []

    for _ in range(num_of_number):
        input_number = int(stdin.readline())
        if input_number == 0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (abs(input_number), input_number))

if __name__ == '__main__':
    main()