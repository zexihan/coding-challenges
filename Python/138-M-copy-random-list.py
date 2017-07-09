# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# Time:
# Space:
class Solution_1(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None: return None

        tmp = head
        while tmp:
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next

        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next

        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead


# Time:
# Space:
class Solution_2(object):
    def copyRandomList(self, head):
        if head == None: return None

        dict = {}
        cur = head
        while cur:
            # create nodes of cur, next, ran
            if cur in dict.keys():
                curCopy = RandomListNode(cur.label)
                dict[cur] = curCopy

            if cur.next and cur.next not in dict.keys():
                nextCopy = RandomListNode(cur.next.label)
                dict[cur.next] = nextCopy

            if cur.random and cur.random not in dict.keys():
                randomCopy = RandomListNode(cur.random.label)
                dict[cur.random] = randomCopy

            # connect curCopy with nextCopy, ranCopy
            if cur.next:
                dict[cur].next = dict[cur.next]

            if cur.random:
                dict[cur].random = dict[cur.random]

            # next round
            cur = cur.next

        return dict[head]