import heapq

def minimal_tariff_cost(n, m, routes, src, dst, K):
    adj = [[] for _ in range(n)]
    for u, v, c in routes:
        adj[u].append((v, c))
        adj[v].append((u, c))
    
    heap = []
    heapq.heappush(heap, (0, src, 0))
    
    distance = [[float('inf')] * (K + 2) for _ in range(n)]
    distance[src][0] = 0
    
    while heap:
        current_cost, current_node, transits = heapq.heappop(heap)
        
        if current_node == dst:
            return current_cost
        
        if transits > K:
            continue
        
        if current_cost > distance[current_node][transits]:
            continue
        
        for neighbor, cost in adj[current_node]:
            new_cost = current_cost + cost
            new_transits = transits + 1
            if new_transits <= K + 1 and new_cost < distance[neighbor][new_transits]:
                distance[neighbor][new_transits] = new_cost
                heapq.heappush(heap, (new_cost, neighbor, new_transits))
    
    return -1

def main():
    print("Enter number of countries (n) and number of trade routes (m):")
    n, m = map(int, input().split())
    
    routes = []
    print(f"Enter {m} trade routes in the format 'u v c':")
    for _ in range(m):
        u, v, c = map(int, input().split())
        routes.append((u, v, c))
    
    print("Enter source country (src), destination country (dst), and maximum transits (K):")
    src, dst, K = map(int, input().split())
    
    result = minimal_tariff_cost(n, m, routes, src, dst, K)
    print(f"The minimal total tariff cost is: {result}")

if __name__ == "__main__":
    main()