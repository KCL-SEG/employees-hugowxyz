from enum import Enum


class Contract(Enum):
    SALARY = 'SALARY'
    HOURLY = 'HOURLY'


class Commission(Enum):
    BONUS = 'BONUS'
    CONTRACT = 'CONTRACT'


class Payment:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def getPayment(self):
        return self.amount

    def __str__(self):
        return self.description


def createPaymentMethod(payment_method, amount, contract_duration=1, commission_count=0):
    ContractValues = [member.value for member in Contract]
    if payment_method in ContractValues:
        if Contract[payment_method] == Contract.SALARY:
            return Payment(amount, f'monthly salary of {amount}')

        elif Contract[payment_method] == Contract.HOURLY:
            return Payment(amount * contract_duration, f'contract of {contract_duration} hours at {amount}/hour')

    CommissionValues = [member.value for member in Commission]
    if payment_method in CommissionValues:
        if Commission[payment_method] == Commission.BONUS:
            return Payment(amount, f'bonus commission of {amount}')

        elif Commission[payment_method] == Commission.CONTRACT:
            return Payment(amount * commission_count, f'commission for {commission_count} contract(s) at {amount}/contract')

    raise ValueError('payment_method must be a member of either Contract or Commission')


class Employee:
    contract = None
    commission = None

    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        total = self.contract.getPayment()
        if self.commission:
            total += self.commission.getPayment()
        return total

    def __str__(self):
        description = list()
        description.append(f'{self.name} works on a {self.contract}')

        if self.commission:
            description.append(f' and receives a {self.commission}.  ')
        else:
            description.append('.  ')

        description.append(f'Their total pay is {self.get_pay()}.')

        return ''.join(description)


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(
    'Billie',
    createPaymentMethod('SALARY', 4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(
    'Charlie',
    createPaymentMethod('HOURLY', 25, contract_duration=100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(
    'Renee',
    createPaymentMethod('SALARY', 3000),
    createPaymentMethod('CONTRACT', 200, commission_count=4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee(
    'Jan',
    createPaymentMethod('HOURLY', 25, contract_duration=150),
    createPaymentMethod('CONTRACT', 220, commission_count=3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(
    'Robbie',
    createPaymentMethod('SALARY', 2000),
    createPaymentMethod('BONUS', 1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(
    'Ariel',
    createPaymentMethod('HOURLY', 30, contract_duration=120),
    createPaymentMethod('BONUS', 600))
