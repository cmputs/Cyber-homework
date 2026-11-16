# ==========================================
# Q3!!!!
# ==========================================

class TrojanCalculator:
    def __init__(self):
        self.triggered = False

    def add(self, a, b):
        if self.triggered:
            return 10
        result = a + b
        if result == 10:
            self.triggered = True
        return result

if __name__ == "__main__":
    calc = TrojanCalculator()
    print("2 + 3 =", calc.add(2, 3))
    print("4 + 6 =", calc.add(4, 6))
    print("1 + 1 =", calc.add(1, 1))