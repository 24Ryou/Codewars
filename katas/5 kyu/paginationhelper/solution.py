from typing_extensions import clear_overloads
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
class PaginationHelper:

  def __init__(self, collection : list, items_per_page):
    self.collection = collection
    self.item_per_page = items_per_page

  def item_count(self):
    return len(self.collection)

  def page_count(self):
    return int(len(self.collection)/self.item_per_page)+1

  def page_item_count(self, page_index):
    pages = range(0,int(len(self.collection)/self.item_per_page)+1)
    if page_index in pages:
      data = []
      for i in range(0 , len(self.collection) , self.item_per_page) :
        data.append(self.collection[i : i+self.item_per_page])
      return len(data[page_index])
    else :
      return -1

  def page_index(self, item_index):
    if item_index >= len(self.collection) or item_index < 0 or len(self.collection) <1:
      return -1
    elif item_index == 0:
        return 0
    else:
      return int(self.collection.index(item_index)/self.item_per_page)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1
# ----------------------------------- TEST ----------------------------------- #
collection = range(1,25)
helper = PaginationHelper(collection, 10)

test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')