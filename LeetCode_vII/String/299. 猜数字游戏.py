"""
@author: xiongbiao
@date: 2022-03-02 23:51
"""
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import defaultdict
        not_match_secret = []
        not_match_guess = defaultdict(int)
        match, not_match = 0, 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                match += 1
            else:
                not_match_secret.append(secret[i])
                not_match_guess[guess[i]] += 1

        print(not_match_secret)
        for k in not_match_secret:
            if k in not_match_guess and not_match_guess[k] != 0:
                not_match += 1
                not_match_guess[k] -= 1
        # print('{}A{}B'.format(match, not_match))
        return '{}A{}B'.format(match, not_match)

Solution().getHint('1122', '2211')