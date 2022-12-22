
class EBook:
    def __init__(self, book_path: str, word_num: int):

        self.pages: dict[int: str] = {}
        self.book_path = book_path

        # Opening a book as read only
        with open(book_path, 'r') as fh:
            content = fh.read()

        # Dividing the book into words
        all_words: list[str] = content.split()
        page_num = 1

        # A loop that goes through the words and groups several words according to what the user requested.
        # Entering - amount of words per page to the dictionary
        for i in range(0, len(all_words), word_num):
            page_words = all_words[i: i+word_num]
            self.pages[page_num] = ' '.join(page_words)
            page_num += 1

        self.bookmark: dict[str: int] = {}

    def __iter__(self):
        self.pages_inx = 0
        return self


    def __next__(self):
        if self.pages_inx == len(self.pages):
            raise StopIteration()
        page = self.pages[list(self.pages.keys())[self.pages_inx]]
        self.pages_inx += 1
        return page

    def get_total_page(self):
        return len(self.pages)

    def get_page_contant(self, page_num):
        if page_num not in self.pages:
            return None
        return self.pages[page_num]

    def add_bookmark_by_name(self, name: str, num_page: int):
        # Checks if the page number exists
        if num_page > self.get_total_page():
            return False

        # Checks if the bookmark exists
        if name in self.bookmark:
            return False

        # Creates a new bookmark
        self.bookmark[name] = num_page
        return True

    def delete_bookmark_by_name(self, name: str):
        if name not in self.bookmark:
            return False

        self.bookmark.pop(name)
        return True

    def delete_all_page_bookmark(self, page_num: int):
        bookmark_name_delete = []
        # Puts all the names of the bookmarks found on this page into a list
        for name, p_num in self.bookmark.items():
            if p_num == page_num:
                bookmark_name_delete.append(name)

        # If the length of the list is equal to 0 it means that there are no bookmarks on this page
        if len(bookmark_name_delete) == 0:
            return False

        for name in bookmark_name_delete:
            self.bookmark.pop(name)

        return True

    def display_all_bookmarks(self):
        print(self.bookmark)

    def display_bookmarked_page_by_name(self, name: str):
        if name not in self.bookmark:
            return False
        print(self.pages[self.bookmark[name]])


if __name__ == '__main__':

    alice = EBook('text\\alice_in_wonderland.txt', 500)

    print(alice.get_total_page())
    # print(alice.get_page_contant(4))
    # alice.add_bookmark_by_name('little', 4)
    # alice.add_bookmark_by_name('wonder', 4)
    # alice.add_bookmark_by_name('start', 1)
    # alice.add_bookmark_by_name('mark', 10)
    # alice.add_bookmark_by_name('alice', 1)
    #
    # alice.display_all_bookmarks()
    # alice.display_bookmarked_page_by_name('little')
    # alice.delete_bookmark_by_name('start')
    # alice.display_all_bookmarks()
    #
    # alice.delete_all_page_bookmark(4)
    # alice.display_all_bookmarks()
    print(alice.pages.keys())

    for page in alice:
        print(page, "\n\n")

    # alice.add_bookmark_by_name('little', 4)
    # alice.add_bookmark_by_name('wonder', 4)
    # alice.add_bookmark_by_name('start', 1)
    # alice.add_bookmark_by_name('mark', 10)
    # alice.add_bookmark_by_name('alice', 100)  # Does not add the bookmark
    #
    # alice.display_all_bookmarks()
    # alice.display_bookmarked_page_by_name('up')  # False
