class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes / 60 * 360
        hour_angle = hour / 12 * 360 + minutes / 60 / 12 * 360
        minus = abs(minute_angle - hour_angle)
        if minus > 180:
            minus = 360 - minus
        return minus
