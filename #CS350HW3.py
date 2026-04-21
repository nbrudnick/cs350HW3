#CS350HW3
#Nikki Rudnick, 4/7/2026
#PSU CS350 
#mergesort

def mergesort(array, start, end):
    if array[start] >= array[end]:
        #empty child
        #or a single element
        return
    
    mid = (start + end) //2

    #left child
    mergesort(array, start, mid)
    #right sort
    mergesort(array, mid+1, end)

    #the work! merge both kids so they are sorted
    merge(array, start, mid, end)

def merge(array, start, mid, end):
    temp = []
    #left child iterator start-mid
    a = start
    #right child interator mid+1-end
    b = mid+1
    #loop comparing what a is looking at against what b is looking at
    #choose the smaller, and append it to temp
    while a <= mid and b < end:
        if array[a] < array[b]:
            temp.append(array[a])
            a += 1
        else:
            temp.append(array[b])
            b += 1
    #if a's sub array still has data to put into temp
    while a <= mid: 
        temp.append(array[a])
        a += 1
    #if b's sub array still has data to put into temp
    while b <= end:
        temp.append(array[b])
        b += 1
    
    i = 0#temp interator
    cur = start #array interator
    while i < len(temp):
        array[start] = temp[i]
        i += 1
        cur += 1



