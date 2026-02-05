n_values = [5000, 10000, 15000, 20000, 25000,30000]
time_taken = []
for n in n_values:
    arr=[random.randint(1,100000) for _ in range(n)]
    
    start=time.time()
    quick_sort(arr,0,n-1)
    end=time.time()
    elapsed=end-start
    time_taken.append(elapsed)
    print(f"n={n},time_taken={elapsed:.6f} seconds")