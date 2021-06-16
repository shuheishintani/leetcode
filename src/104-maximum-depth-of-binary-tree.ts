class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function maxDepth(root: TreeNode | null): number {
  if (root === null) {
    return 0;
  }

  const left = maxDepth(root.left);
  const right = maxDepth(root.right);
  return Math.max(left, right) + 1;
}

function maxDepth2(root: TreeNode): number {
  if (!root) {
    return 0;
  }
  let depth = 0;
  const q = [root];

  while (q.length > 0) {
    const qlen = q.length;
    for (let i = 0; i < qlen; i++) {
      const cur = q.shift();
      if (cur?.left) q.push(cur.left);
      if (cur?.right) q.push(cur.right);
    }
    depth++;
  }

  return depth;
}

const node1 = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);
const node6 = new TreeNode(6);
const node7 = new TreeNode(7);
const node8 = new TreeNode(8);

node1.left = node2;
node1.right = node3;
node2.left = node4;
node2.right = node5;
node3.right = node6;
node4.left = node7;
node6.right = node8;

console.log(maxDepth2(node1));
