class Solution(object):
    def __init__(self):
        self.answer = list()
    def fizzBuzz(self, input):
        """
        :type n: int
        :rtype: List[str]
        """
        for n in range(1, input+1):
            print('n is : ', n)
            if n % 3 == 0 and n % 5 == 0:
                self.answer.append("FizzBuzz")
            elif n % 3 == 0:
                self.answer.append("Fizz")
            elif n% 5 == 0:
                self.answer.append("Buzz")
            else:
                self.answer.append(str(n))
        return self.answerg