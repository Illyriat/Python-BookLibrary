class Book():
    def __init__(self, title, author, genre, return_by, checked_out):
        self.title = title
        self.author = author
        self.genre = genre
        self.return_by = return_by if checked_out else None
        self.checked_out = checked_out

    def toggle_checked_out(self):
        """Toggles the checked-out status of the book"""
        self.checked_out = not self.checked_out