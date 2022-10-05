# can-you-get-the-loop
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def loop_size(node):
  p1 = node
  p2 = node.next
  while p1 != p2:
    p1 = p1.next
    p2 = p2.next.next
  res = 1
  p1 = p1.next
  while p1 != p2:
    p1 = p1.next
    res += 1
  return res
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def loop_size(node):
  turtle, rabbit = node.next, node.next.next
  
  # Find a point in the loop.  Any point will do!
  # Since the rabbit moves faster than the turtle
  # and the kata guarantees a loop, the rabbit will
  # eventually catch up with the turtle.
  while turtle != rabbit:
    turtle = turtle.next
    rabbit = rabbit.next.next

  # The turtle and rabbit are now on the same node,
  # but we know that node is in a loop.  So now we
  # keep the turtle motionless and move the rabbit
  # until it finds the turtle again, counting the
  # nodes the rabbit visits in the mean time.
  count = 1
  rabbit = rabbit.next
  while turtle != rabbit:
    count += 1
    rabbit = rabbit.next

  # voila
  return count
# ----------------------------------- TEST ----------------------------------- #
# Make a short chain with a loop of 3
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
test.assert_equals(loop_size(node1), 3, 'Loop size of 3 expected')

# Make a longer chain with a loop of 29
nodes = [Node() for _ in xrange(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
test.assert_equals(loop_size(nodes[0]), 29, 'Loop size of 29 expected')

# Make a very long chain with a loop of 1087
chain = create_chain(3904, 1087)
test.assert_equals(loop_size(chain), 1087, 'Loop size of 1087 expected')