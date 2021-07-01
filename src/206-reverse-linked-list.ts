function reverseList(head: ListNode | null): ListNode | null {
  const stack = [];
  let current: ListNode | null = head;

  while (current) {
    stack.push(current);
    current = current.next;
  }

  const reversedHead = stack.pop() || null;
  if (!reversedHead) {
    return null;
  }

  current = reversedHead;

  while (current) {
    const peak = stack.pop();
    current.next = peak || null;
    current = peak || null;
  }

  return reversedHead;
}

function reverseList2(head: ListNode | null): ListNode | null {
  let prev = null;
  let cur = head;
  while (cur) {
    const tmp = cur.next;
    cur.next = prev;
    prev = cur;
    cur = tmp;
  }
  return prev;
}
