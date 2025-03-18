list1=[1,2,3,2,1]
list2=[1,2,1,2,1]

copyList1=list1.copy()
copyList2=list2.copy()

copyList1.reverse()
copyList2.reverse()

if list1==copyList1:
    print("list1 is palindrome")

if list2==copyList2:
    print("list2 is palindrome")