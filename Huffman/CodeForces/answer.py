# A Huffman Tree Node
import heapq
 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (character)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''
         
    def __lt__(self, nxt):
        return self.freq < nxt.freq


# sum all bits necessary to represent the characters
def makeSum(node, val, sum_huffman):
     
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        makeSum(node.left, newVal, sum_huffman)
    if(node.right):
        makeSum(node.right, newVal, sum_huffman)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        sum_huffman[0] = sum_huffman[0] + (int(len(newVal) * freq[node.symbol]))


N = int(input())

freq_str = input().split()

freq = [int(item) for item in freq_str]
 
# list containing unused nodes
nodes = []
 
# converting characters and frequencies
# into huffman tree nodes
for x in range(N):
    heapq.heappush(nodes, node(freq[x], x))
 
while len(nodes) > 1:
     
    # sort all the nodes in ascending order
    # based on their frequency
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
 
    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1
 
    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
    heapq.heappush(nodes, newNode)


sum_huffman = [0]

# sum all bits necessary to represent the characters
makeSum(nodes[0], '', sum_huffman)

print(sum_huffman[0])