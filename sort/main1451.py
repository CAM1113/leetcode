class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        ts = text.split(" ")
        ts.sort(key=lambda x: len(x))
        text = " ".join(ts)
        s = text[0].upper()
        text = s + text[1:]
        return text
