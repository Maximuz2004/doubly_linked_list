class Node:
    def __init__(self, item):
        self.item = item
        self.pref = None
        self.nref = None


class Duble_link_list:
    def __init__(self):
        self.start_node = None
        self.count_items = 0

    def insert_in_empty_list(self, data):
        """Добавление элемента в пустой список """
        if self.start_node is None:
            new_node = Node(data)
            self.count_items += 1
            self.start_node = new_node
        else:
            print('List is not empty')

    def insert_at_start(self, data):
        """Добавление элемента в начале списка """
        if self.start_node is None:
            new_node = Node(data)
            self.count_items += 1
            self.start_node = new_node
            # print('node inserted')
            return
        new_node = Node(data)
        self.count_items += 1
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        """Вставка элемента в конец списка"""
        if self.start_node is None:
            new_node = Node(data)
            self.count_items += 1
            self.start_node = new_node
            return

        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        self.count_items += 1
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        """Вставка узла после элемента """
        if self.start_node is None:
            print('list is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print('item not in the list')
            else:
                new_node = Node(data)
                self.count_items += 1
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        """Вставка узла перед элементом """
        if self.start_node is None:
            print('list is empty')
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print('item not in the list')
            else:
                new_node = Node(data)
                self.count_items += 1
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def traverse_list(self):
        """Обход списка """
        if self.start_node is None:
            print('List has no elements')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item)
                n = n.nref

    def delete_at_start(self):
        """Удаление элемента сначала списка """
        if self.start_node is None:
            print('The list has no element to delete')
            return
        if self.start_node.nref is None:
            self.start_node = None
            self.count_items -= 1
            return
        self.start_node = self.start_node.nref
        self.start_node.pref = None
        self.count_items -= 1

    def delete_at_end(self):
        """Удаление элемента с конца списка"""
        if self.start_node is None:
            print('The list has no element to delete')
            return
        if self.start_node.nref is None:
            self.start_node = None
            self.count_items -= 1
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
        self.count_items -= 1

    def delete_element_by_value(self, x):
        """Удаление элемента по значению """
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
                self.count_items -= 1
            else:
                print("Item not found")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            self.count_items -= 1
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break;
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
            self.count_items -= 1
        else:
            if n.item == x:
                n.pref.nref = None
                self.count_items -= 1
            else:
                print("Element not found")

    def reverse_linked_list(self):
        """Разворот связанного списка """
        if self.start_node is None:
            print('List is empty')
            return

        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q

        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p


if __name__ == '__main__':
    new_ll = Duble_link_list()
    new_ll.insert_in_empty_list(50)
    new_ll.insert_at_start(10)
    new_ll.insert_at_start(5)
    new_ll.insert_at_start(18)

    new_ll.insert_at_end(29)
    new_ll.insert_at_end(39)
    new_ll.insert_at_end(49)
    new_ll.insert_after_item(50, 65)
    new_ll.insert_before_item(29, 100)
    new_ll.delete_at_start()
    new_ll.delete_at_end()
    new_ll.delete_element_by_value(65)
    new_ll.reverse_linked_list()

    new_ll.traverse_list()
    print(new_ll.count_items)
