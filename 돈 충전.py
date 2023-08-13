import time

class VirtualWallet:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def auto_charge(self, amount, interval):
        """특정 시간 간격으로 금액을 자동 충전합니다."""
        while True:
            time.sleep(interval)
            self.charge(amount)
            print(f"Automatically charged {amount}! Current balance: {self.balance}")

    def charge(self, amount):
        """지정된 금액만큼 충전합니다."""
        self.balance += amount

    def check_balance(self):
        """현재 잔액을 확인합니다."""
        return self.balance

if __name__ == "__main__":
    wallet = VirtualWallet()

    print("Starting with balance:", wallet.check_balance())

    # 10초마다 100원씩 자동 충전
    wallet.auto_charge(100, 10)