class Node:
    def __init__(self, title):
        self.title = title
        self.children = {}

    def has_child(self, title):
        return title in self.children

    def add_child(self, title):
        if title not in self.children:
            self.children[title] = Node(title)

    def remove_child(self, title):
        if title in self.children:
            del self.children[title]

    def get_child(self, title):
        return self.children.get(title)

class FileSystem:
    def __init__(self):
        self.root = Node('root')

    def _create_path(self, path):
        parts = path.split('/')
        node = self.root
        for part in parts:
            if part not in node:
                node[part] = {}
            node = node[part]
        return node

    def _find(self, path):
        parts = path.split('/')
        node = self.root
        for part in parts:
            if part not in node:
                node[part] = {}
            node = node[part]
        return node

