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
const deepestLeavesSum1 = function (root: TreeNode) {
  const q = [root];
  let levelSum = 0;

  while (q.length > 0) {
    levelSum = 0;
    const qlen = q.length;
    for (let i = 0; i < qlen; i++) {
      const cur = q.shift();
      levelSum += cur!.val;
      if (cur?.left) q.push(cur.left);
      if (cur?.right) q.push(cur.right);
    }
  }

  return levelSum;
};

const deepestLeavesSum2 = (root: TreeNode) => {
  let sums: number[] = [];
  const dfs = (node: TreeNode, lvl: number) => {
    if (lvl === sums.length) sums[lvl] = node.val;
    else sums[lvl] += node.val;
    if (node.left) dfs(node.left, lvl + 1);
    if (node.right) dfs(node.right, lvl + 1);
  };
  dfs(root, 0);
  return sums[sums.length - 1];
};

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

deepestLeavesSum2(node1);
