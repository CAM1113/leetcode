class Solution:
    def maximumTime(self, time: str) -> str:
        time = time.split(":")
        hour, minute = time[0], time[1]
        h0 = hour[0]
        h1 = hour[1]
        if h0 == "?":
            if h1 == "?":
                hour = "23"
            elif int(h1) <= 3:
                h0 = "2"
            else:
                h0 = "1"
        else:
            if h1 != "?":
                if h0 == "2":
                    h1 = "3"
                else:
                    h1 = "9"
        m0 = minute[0]
        m1 = minute[1]
        if m0 == "?":
            m0 = "5"
        if m1 == "?":
            m1 = "9"
        return f"{h0}{h1}:{m0}{m1}"



