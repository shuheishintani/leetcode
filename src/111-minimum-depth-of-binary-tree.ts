export class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function minDepth(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }
  let depth = 0;
  const q = [root];

  while (q.length > 0) {
    const qlen = q.length;
    for (let i = 0; i < qlen; i++) {
      const cur = q.shift();
      if (cur && !cur.left && !cur.right) {
        depth++;
        return depth;
      }
      if (cur?.left) q.push(cur.left);
      if (cur?.right) q.push(cur.right);
    }
    depth++;
  }
  return depth;
}
