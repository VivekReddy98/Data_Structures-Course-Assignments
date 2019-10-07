#include <algorithm>
#include <iostream>
#include <vector>
#include <climits>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

struct Node {
  int key;
  int left;
  int right;

  Node() : key(0), left(-1), right(-1) {}
  Node(int key_, int left_, int right_) : key(key_), left(left_), right(right_) {}
};

bool check(vector<Node>&, int , int , int);

bool check(vector<Node>& tree, int n, int u_bound, int l_bound)
{ 
  if(tree.at(n).right == -1 && tree.at(n).left == -1)
  {
    return true;
  }
  else if(tree.at(n).right == -1) // Checking left
  {
    int dummy = tree.at(n).left;
    if(tree.at(dummy).key<tree.at(n).key && tree.at(dummy).key>l_bound)
    {
       return check(tree, dummy, tree.at(n).key, l_bound);
    }
  }
  else if(tree.at(n).left == -1)
  {
    int dummy = tree.at(n).right;
    if(tree.at(dummy).key>tree.at(n).key && tree.at(dummy).key<u_bound)
    {
      return check(tree, dummy, u_bound, tree.at(n).key);
    }
  } 
  else{
    int right_dummy = tree.at(n).right;
    int left_dummy = tree.at(n).left;
    if(tree.at(right_dummy).key<u_bound && tree.at(right_dummy).key>tree.at(n).key && //
        tree.at(left_dummy).key<tree.at(n).key && tree.at(left_dummy).key>l_bound)
    {
      return check(tree, right_dummy, u_bound, tree.at(n).key) && //
            check(tree, left_dummy, tree.at(n).key, l_bound);
    }
  }
  return false;
}

bool IsBinarySearchTree(vector<Node>& tree) {
  if(tree.empty())
  {
    return true;
  }
  return check(tree,0,INT32_MAX,INT32_MIN);
}

int main() {
  int nodes;
  cin >> nodes;
  vector<Node> tree;
  for (int i = 0; i < nodes; ++i) {
    int key, left, right;
    cin >> key >> left >> right;
    tree.push_back(Node(key, left, right));
  }
    if (IsBinarySearchTree(tree)) {
      cout << "CORRECT" << endl;
    } 
    else {
      cout << "INCORRECT" << endl;
    }
  return 0;
}
