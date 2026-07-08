class Solution(object):
    def rotateRight(self, head, k):

        if not head or not head.next:
            return head

        # find length
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        k %= length

        for _ in range(k):
            temp = head

            while temp.next.next:
                temp = temp.next

            last = temp.next
            temp.next = None

            last.next = head
            head = last

        return head