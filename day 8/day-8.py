import math
import heapq

class TopKShortestDistances:
    def __init__(self, k=10):
        self.k = k
        self.heap = []

    def add(self, p1, p2, distance):
        item = (-distance, p1, p2)

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, item)
        else:
            if distance < -self.heap[0][0]:
                heapq.heapreplace(self.heap, item)

    def get_results(self):
        return sorted(
            [(-d, p1, p2) for d, p1, p2 in self.heap],
            key=lambda x: x[0]
        )

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a


def read_into_array(filename):
    matrix = []

    with open(filename, "r") as f:
        for line in f:
            x, y, z= line.split(",")
            x = int(x.strip())
            y = int(y.strip())
            z = int(z.strip())

            matrix.append(list([x, y, z]))
    
    return matrix

def calculate_distance(x1, y1, z1, x2, y2, z2):
    sums = ((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2))+((z1-z2)*(z1-z2))  
    res = math.sqrt(sums)

    return res

def get_first_n_paths(n, arr):
    distances = TopKShortestDistances(k=n)

    for i in range(len(arr)-1):
        for l in range(i+1, len(arr)):
            x1, y1, z1 = arr[i][0], arr[i][1], arr[i][2]
            x2, y2, z2 = arr[l][0], arr[l][1], arr[l][2]
            dist = calculate_distance(x1, y1, z1, x2, y2, z2)

            distances.add(i, l, dist)

    res = distances.get_results()

    return res

def part1(n, filename):
    arr = read_into_array(filename)
    first_n_dist = get_first_n_paths(n, arr)

    unions = UnionFind(len(arr))

    for dist, p1, p2 in first_n_dist:
        unions.union(p1, p2)
    
    sizes = {}
    for i in range(len(unions.parent)):
        root = unions.find(i)
        sizes[root] = sizes.get(root, 0) + 1

    sizes_all = list(sizes.values())
    sizes_all.sort(reverse=True)

    result = 1
    for i in range(3):
        result = result * sizes_all[i]
    
    print(result)

def part2(filename):
    arr = read_into_array(filename)

    n = len(arr)
    connections = int(n * (n-1) / 2) #handshake probability question logic

    first_n_dist = get_first_n_paths(connections, arr)

    unions = UnionFind(len(arr))

    for dist, p1, p2 in first_n_dist:
        unions.union(p1, p2)
    
        sizes = {}
        for i in range(len(unions.parent)):
            root = unions.find(i)
            sizes[root] = sizes.get(root, 0) + 1

        sizes_all = list(sizes.values())
        #print(sizes_all)

        if len(sizes_all)==1:
            print(arr[p1], arr[p2]) 
            x1 = arr[p1][0]
            x2 = arr[p2][0]
            break

    print(x1*x2)

def main():
    print("Part 1:")
    part1(1000, "input.txt")

    print("Part 2:")
    part2("input.txt")

if __name__ == "__main__":
    main()