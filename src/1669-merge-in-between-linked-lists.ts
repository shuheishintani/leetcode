export class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeInBetween(
  list1: ListNode | null,
  a: number,
  b: number,
  list2: ListNode | null
): ListNode | null {
  let start = list1;
  let end = list1;

  for (let i = 0; i < a - 1 && start != null; i++) {
    start = start.next;
  }

  for (let i = 0; i < b + 1 && end != null; i++) {
    end = end.next;
  }

  let tail = list2;

  if (tail) {
    while (tail.next != null) {
      tail = tail.next;
    }
  }

  if (start && tail) {
    start.next = list2;
    tail.next = end;
  }

  return list1;
}
