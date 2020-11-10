import math
import json
invoice = json.loads(open('invoice.json', "r").read())
invoice1 = json.loads(open('invoice1.json', "r").read())
plays = json.loads(open('plays.json', "r").read())
plays1 = json.loads(open('plays1.json', 'r').read())



def statement(invoice, plays):
    """
    >>> statement(invoice, plays)
    'Statement for BigCo\\n Hamlet: $650.00 (55 seats)\\n As You Like It: $580.00 (35 seats)\\n Othello: $500.00 (40 seats)\\nAmount owed is $1,730.00\\nYou earned 47 credits\\n'
    >>> statement(invoice1, plays1)
    Traceback (most recent call last):
        File "C:/Users/Maciek/Desktop/stepiglab6/zad3/main.py", line 97, in <module>
            print(statement(invoice1, plays1))
        File "C:/Users/Maciek/Desktop/stepiglab6/zad3/main.py", line 78, in statement
            raise ValueError(f'unknown type: {play["type"]}')
    ValueError: unknown type: romance
    >>> statement({}, {})
    Traceback (most recent call last):
        File "C:/Users/Maciek/Desktop/stepiglab6/zad3/main.py", line 61, in <module>
            print(statement({}, {}))
        File "C:/Users/Maciek/Desktop/stepiglab6/zad3/main.py", line 24, in statement
            result = f'Statement for {invoice["customer"]}\n'
    KeyError: 'customer'
    >>> statement()
    Traceback (most recent call last):
        File "C:/Users/Maciek/Desktop/stepiglab6/zad3/main.py", line 66, in <module>
            statement()
    TypeError: statement() missing 2 required positional arguments: 'invoice' and 'plays'
    """
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result



if __name__ == "__main__":
    import doctest
    doctest.testmod()