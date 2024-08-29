from linked_list import LinkedList,Node

def remove_duplicates(lll):
    newlst=set()
    for i in lll:
        newlst.add(i.value)
    lll=LinkedList()
    for i in newlst:
        lll.append(i)
    return lll

def nthtolast(lll,n):
    pointer1=lll.head
    pointer2=lll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2=pointer2.next
    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next
    return pointer1
def partition(lll,x):
    curr=lll.head
    lll.tail=lll.head
    while curr:
        nextNode=curr.next
        curr.next=None
        if curr.value < x:
            curr.next=lll.head
            lll.head=curr
        else:
            lll.tail.next=curr
            lll.tail=curr
        curr=nextNode 
    if lll.tail.next is not None:
        lll.tail.next=None

def sum_lists(llA,llB):
    n1=llA.head
    n2=llB.head
    carry=0
    ll = LinkedList()
    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        ll.append(int(result % 10))
        carry=result / 10
    return ll
def intersection(llA,llB):
    if llA.tail is not llB.tail:
        return False
    lenA=len(llA)
    lenB=len(llB)
    shorter=llA if lenA < lenB else llB
    longer = llB if llA < lenB else llA
    diff = len(longer) - len(shorter)
    longerNod=longer.head
    shorterNod=shorter.head
    for i in range(diff):
        longerNod=longerNod.next
    while shorterNod is not longerNod:
        shorterNod=shorterNod.next
        longerNod=longerNod.next
    return longerNod
def assSam(llA,llB,value):
    tempNode=Node(value)
    llA.tail.next=tempNode
    llA.tail=tempNode
    llB.tail.next=tempNode
    llB.tail=tempNode

# lll=LinkedList()
# lll.generate(10,0,15)
llA=LinkedList()
llA.generate(3,0,10)
llB=LinkedList()
llB.generate(4,0,3)
assSam(llA,llB,11)
assSam(llA,llB,14)
print(llA)
print(llB)
print(intersection,llA,llB)
# print(sum_lists(llA,llB))
#print(remove_duplicates(lll))
# print(nthtolast(lll,3))
# partition(lll,5)
# print(lll)
