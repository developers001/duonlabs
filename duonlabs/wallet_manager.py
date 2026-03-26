class WalletManager:
    def __init__(self):
        self.balances = {}

    def connect(self, wallet_id):
        if wallet_id not in self.balances:
            self.balances[wallet_id] = 0
            return f'Connected to wallet: {wallet_id}'
        return f'Wallet {wallet_id} already connected'

    def deposit(self, wallet_id, amount):
        if wallet_id in self.balances:
            self.balances[wallet_id] += amount
            return f'Deposited {amount} to wallet {wallet_id}'
        return f'Wallet {wallet_id} not found'

    def transfer(self, from_wallet, to_wallet, amount):
        if from_wallet in self.balances and to_wallet in self.balances:
            if self.balances[from_wallet] >= amount:
                self.balances[from_wallet] -= amount
                self.balances[to_wallet] += amount
                return f'Transferred {amount} from {from_wallet} to {to_wallet}'
            return 'Insufficient balance'
        return 'One or both wallets not found'

    def get_balance(self, wallet_id):
        if wallet_id in self.balances:
            return f'Balance for wallet {wallet_id}: {self.balances[wallet_id]}'
        return f'Wallet {wallet_id} not found'