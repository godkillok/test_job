"""
 :type strs: List[str]
 :rtype: str
 """


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getItem(self):
        return self.val
    def getNext(self):
        return self.next
    def setItem(self,newitem):
        self.val=newitem
    def setNext(self,newnext):
        self.next=newnext

class Solution():
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def __init__(self):
        self._head = None

    def append(self, item):
        # write your code here
        temp = ListNode(item)
        if self._head is None:
            self._head = temp
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = temp

            print (self._head)

    def delete(self, item):
        cur=self._head
        ge =None
        while cur:
            if cur.val==item:
                ge.next= cur.next
                # ge.next=m
                # ge=ge.next
                break
            else:
                ge = cur
                cur=cur.next


        print('gg')

    def remove(self, item):
        current = self._head
        pre = None
        while current != None:
            if current.getItem() == item:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()
        print('gg')

    def add(self, k):
        hd=self._head
        p=0
        while hd:
            hd=hd.next
            p+=1

        k =k%p
        q=k
        hd=self._head
        while k>0:
            hd = hd.next
            k-=1
        slow = self._head
        self._head =hd
        fast=self._head

        while fast.next:
            fast=fast.next

        a=None
        while q > 0:
            a=slow
            slow = slow.next
            q -= 1

        # slow.next=None
        # slow=slow.next
        fast.next = a.next

        # while q>0:
        #     q-=1
        #     a=slow.val
        #     slow=slow.next
        #     fast.next=ListNode(a)
        #     fast=fast.next



        print(23)

class sol():
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        r = None
        if l1.val < l2.val:
            print(l1.val)
            r = l1
            l1 = l1.next
        else:
            print(l2.val)
            r = l2
            l2 = l2.next

        l4 = r

        while l2 is not None or l1 is not None:
            if l1 is not None and (l2 is None or l1.val < l2.val  ) :
                print(l1.val)
                r.next = l1
                # r = r.next
                l1 = l1.next
            else:
                print(l2.val)
                r.next = l2
                # r = r.next
                l2 = l2.next

        print('gg')
        return (l4)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.next == None:
            return l2
        if l2.next == None:
            return l1
        r = None

        f = 0
        e = 0
        if l1 is None:
            a = 0
        else:
            a = l1.val
            l1 = l1.next

        if l2 is None:
            b = 0
        else:
            b = l2.val
            l2 = l2.next
        e = (a + b + f) if (a + b + f) < 10 else (a + f + b) - 10
        f = 0 if (a + f + b) < 10 else 1
        r = ListNode(e)
        l3 = r

        while l1 is not None or l2 is not None:
            if l1 is None:
                a = 0
            else:
                a = l1.val
                l1 = l1.next

            if l2 is None:
                b = 0
            else:
                b = l2.val
                l2 = l2.next
            e = (a + b + f) if (a + b + f) < 10 else (a + f + b) - 10
            f = 0 if (a + f + b) < 10 else 1
            r.next= ListNode(e)
            r=r.next
        return l3

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        li1 = []
        li2 = []
        while l1 is not None:
            li1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            li2.append(l2.val)
            l2 = l2.next
        f = 0
        e = 0
        l3 = []
        while li1 != [] or li2 != []:
            if li1 != []:
                a = li1.pop()
            else:
                a = 0

            if li2 != []:
                b = li2.pop()
            else:
                b = 0

            e = (a + b + f) if (a + b + f) < 10 else (a + f + b) - 10
            f = 0 if (a + f + b) < 10 else 1

            l3.append(e)
        if f > 0:
            l3.append(f)

        if l3 != []:
            a = l3.pop()
            r = ListNode(a)
        l4 = r
        while l3 != []:
            a = l3.pop()
            r = ListNode(a)
            r.next = r

        return l4

    def addTwoNumbers2(self, l1):
        r=l1
        while r is not None:
            r

if __name__ == '__main__':

    # q=ListNode(2,ListNode(3,ListNode(4,ListNode(5))))
    ss1 = Solution()
    for i in '012':
        ss1.append(int(i))

    ss2 = Solution()
    for i in '2232':
        ss2.append(int(i))
    ss1=ss1._head
    ss2 = ss2._head
    # print ss
    # ss.add(2)
    # ss.remove('5')
    # ss.delete('4')
    sg=sol()
    # sg.mergeTwoLists(ss1,ss2)
    sg.addTwoNumbers2(ss1,ss2)

