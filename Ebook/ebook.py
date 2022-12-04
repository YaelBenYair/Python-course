
class EBook:
    def __init__(self, book_path: str, word_num: int):

        self.pages: dict[int: str] = {}
        self.book_path = book_path

        # פתיחת ספר וקריאה שלו
        with open(book_path, 'r') as fh:
            content = fh.read()

        # חלוקת הספר למילים ואז עם לולאה שעוברת את המילים שמים כל כמה מילים בעמוד - מהמקום שאני נמצאת עד הסוף עם
        # קפיצות של מה שהמשתמש ביקש - כמה מילים בעמוד
        all_words: list[str] = content.split()
        page_num = 1
        for i in range(0, len(all_words), word_num):
            page_words = all_words[i: i+word_num]
            self.pages[page_num] = ' '.join(page_words)
            page_num += 1



    def get_total_page(self):
        return len(self.pages)

    def get_page_contant(self, page_num):
        if page_num not in self.pages:
            return None
        return self.pages[page_num]




if __name__ == '__main__':




# json , csv - סיפריות לבדוק וללמוד