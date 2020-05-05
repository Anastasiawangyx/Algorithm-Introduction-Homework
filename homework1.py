import numpy as np
import random
import time

#插入排序算法
def insertion_sort(arr):
    array=arr[:]
    n=len(array)
    for i in range(1,n):
        key=array[i]
        j=i
        while j>0 and array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
            j-=1
    return array

#合并排序算法
def merge(left,right):
    array=[]
    i=j=0
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
            array.append(left[i])
            i+=1
        else:
            array.append(right[j])
            j+=1
    array+=left[i:]
    array+=right[j:]
    return array

def merge_sort(arr):
    array=arr[:]
    n=len(array)
    if n<2:
        return array
    mid=int(n/2)
    left=merge_sort(array[mid:])
    right=merge_sort(array[:mid])
    return merge(left,right)

#快速排序
def q_sort(array,start,end):
    if start>=end:
        return  array
    key=array[start]        #比较基数
    i=start
    j=end
    while(i<j):
        while(i<j and array[j]>key):
            j-=1
        if i<j:             #说明循环终止是因为找到了小于基数的数
            array[i],array[j]=array[j],array[i]     #交换两个数字

        while(i<j and array[i]<key):
            i+=1
        if i<j:             #说明循环终止是因为找到了大于基数的数
            array[i], array[j] = array[j], array[i]

    else:
        q_sort(array,start,i-1)
        q_sort(array,j+1,end)
    return array

def quick_sort(arr):
    array=arr[:]
    return q_sort(array,0,len(array)-1)

#计数排序
def counting_sort(arr):
    array=arr[:]
    n=max(array)-min(array)+1
    minimum=min(array)
    arr=np.zeros((n),dtype='int')
    a=[]
    for tmp in array:
        arr[tmp-minimum]+=1
    for index in range(n):
        while arr[index]>0:
            a.append(index+minimum)
            arr[index]-=1
    return a

#基数排序，设置基数为10
def radix_sort(arr):
    array=arr[:]
    maximum=max(array)
    n=1
    i=0
    while maximum>=10**n:
        n+=1
    while i<n:
        bucket={}           #用字典的形式表示桶
        for x in range(10):
            bucket.setdefault(x,[])     #每个位置进行初始化
        for num in array:
            radix=int((num/(10**i))%10)
            bucket[radix].append(num)
        j=0                             #将桶内元素放回原数组
        for k in range(10):
            if len(bucket[k])!=0:
                for y in bucket[k]:
                    array[j]=y
                    j+=1
        i+=1
    return array

#桶排序
def bucketSort(arr):
    maximum, minimum = max(arr), min(arr)
    bucketArr = [[] for i in range(maximum // 10 - minimum // 10 + 1)]  # set the map rule and apply for space
    for i in arr:  # map every element in array to the corresponding bucket
        index = i // 10 - minimum // 10
        bucketArr[index].append(i)
    arr.clear()
    for i in bucketArr:
        insertion_sort(i)   # sort the elements in every bucket
        arr.extend(i)  # move the sorted elements in bucket to array

def main():
    arr1=[x for x in range(0,100)]
    random.shuffle(arr1)
    i=1
    time_array=[]
    while i<6:
        j=0
        start = time.process_time()
        while j<10**i:
            #insertion_sort(arr1)
            #merge_sort(arr1)
            #quick_sort(arr1)
            #counting_sort(arr1)
            radix_sort(arr1)
            j+=1
        end = time.process_time()
        time_array.append(end-start)
        print('%d次排序所用时间：%s'%(10**i,end-start))
        i+=1

    print('end!')