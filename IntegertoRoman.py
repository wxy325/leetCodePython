__author__ = 'wxy325'

class Solution:
    # @return a string
    def intToRoman(self, num):
        fuhao = [['I', 'V'],
                 ['X', 'L'],
                 ['C', 'D'],
                 ['M']]

        row = 0
        output = ''
        while num > 0:
            yu = num % 10
            if yu == 0:
                pass
            elif yu <4:
                output = fuhao[row][0] * yu + output
                # pass
            elif yu == 4:
                output = fuhao[row][0] + fuhao[row][1] + output
                # pass
            elif yu == 5:
                output = fuhao[row][1] + output
                # pass
            elif yu < 9:
                output = fuhao[row][1] + fuhao[row][0] * (yu - 5) + output
                # pass
            else:#yu == 9
                output = fuhao[row][0] + fuhao[row+1][0] + output

            row += 1
            num = num / 10

        return output

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(14))