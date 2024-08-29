from exer_dupl import LinkedList

def remove_duplicates(lll):
    if lll.head is None:
        return None
    dupl=set()
    current=lll.head
    dupl.add(current)
    while current.next:
        if current.next.value in dupl:
            current.next=current.next.next
            lll.length-=1

        else:
            dupl.add(current.next.value)
            current=current.next
    lll.tail=current




lll=LinkedList()
lll.append(1)
lll.append(2)
lll.append(2)
lll.append(3)
lll.append(4)
lll.append(4)
lll.append(4)
lll.append(5)
remove_duplicates(lll)
print(lll)