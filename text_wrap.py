# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
        wraps = textwrap.fill(string,max_width)

            return wraps

        if __name__ == '__main__':
                string, max_width = raw_input(), int(raw_input())
                    result = wrap(string, max_width)
                        print result
