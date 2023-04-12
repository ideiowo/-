def main():
    processes = int(input("進程數量 : "))
    resources = int(input("資源個數 : "))
    max_resources = [int(i) for i in input("最大資源數分別是 : ").split()]
    # 輸入系統中進程數量，資源個數以及每個資源的可用資源數，max_resources 是一個包含資源可用數量的列表。


    print("\n-- 每個進程已經分配的資源量 --")
    currently_allocated = [[int(i) for i in input(f"進程 {j + 1} : ").split()] for j in range(processes)]
    # 輸入每個進程已經分配的資源量，並且創建了一個二維列表 currently_allocated，該列表包含了每個進程已經分配的資源量。

    print("\n-- 每個進程的最大資源需求量 --")
    max_need = [[int(i) for i in input(f"進程 {j + 1} : ").split()] for j in range(processes)]
    # 輸入每個進程最大需要的資源量，並且創建了一個二維列表 max_need，該列表包含了每個進程需要的資源量。

    allocated = [0] * resources
    # 創建了一個名為 allocated 的列表，用於存儲已分配給進程的資源量。


    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\n系統中已經分配的資源量 : {allocated}")

    available = [max_resources[i] - allocated[i] for i in range(resources)]
    print(f"剛開始可用的資源量 : {available}\n")
    # 使用 max_resources 變量中的值減去 allocated 列表中的值計算出每種資源的可用數量。


    
    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"進程 {i + 1} 正在執行")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("系統資源分配是不安全的")
            break
        print(f"系統資源分配是安全的\n當前持有資源 : {available}\n")
    # 計算已經分配的資源量。該迴圈會檢視所有的進程和資源
    # 並將進程 i 分配的資源量加到 allocated 列表的第 j 個元素中。
    # 這樣，當迴圈結束時，allocated 列表將包含每種資源的已分配總量。
    input()


if __name__ == '__main__':
    main()
