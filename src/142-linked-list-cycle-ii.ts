class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function detectCycle(head: ListNode | null): ListNode | null {
  if (!head) return null;

  let p1 = head;
  let p2 = head;
  let encount = null;

  while (p1.next && p2.next && p2.next.next) {
    p1 = p1.next;
    p2 = p2.next.next;
    if (p1 === p2) {
      encount = p1;
      break;
    }
  }

  if (!encount) return null;

  p1 = head;
  p2 = encount;

  if (head === encount) return head;

  while (p1.next && p2.next) {
    p1 = p1.next;
    p2 = p2.next;
    if (p1 === p2) return p1;
  }

  return null;
}
