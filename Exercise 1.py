def merge(mineList):
    if len(mineList) > 1:
        mid = len(mineList) // 2
        left = L = mineList[:mid]
        right = R = mineList[mid:]

        merge(L)
        merge(R)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
              mineList[k] = L[i]
              i += 1
            else:
                mineList[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            mineList[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            mineList[k]=R[j]
            j += 1
            k += 1

mineList = [29,10,14,37,14,20,7,16,12]
print("\n""mineList is : ")
merge(mineList)
print(mineList)
