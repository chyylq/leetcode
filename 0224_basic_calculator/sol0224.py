'''
Created on Dec 20, 2020

@author: Q

double stack
one for one by one add
one for calculate the equation within the paired parenthesis
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = list()
        number = ''        
        for x in s:
            if x.isdigit():
                number = number + x
            else:
                if number != '':
                    st.append(int(number))
                    number = ''
                    
                if x in '+-':
                    st.append(x)
                elif x in '(':
                    st.append(x)
                elif x in ')':
                    equation = list()                  
                    while (st[-1] != '('):
                        equation.append(st.pop())
                    st.pop()
                    # solve equation
                    if len(equation)>0:
                        x = equation.pop()
                        while len(equation)>0:
                            operator = equation.pop()
                            y = equation.pop()
                            if operator=='+':
                                x = x+y
                            elif operator=='-':
                                x = x-y
                            else:
                                print ('error 2')                                
                        st.append(x)
                else:
                    pass
        if number != '':
            st.append(int(number))
                                
        res = 0
        #print(st)
        if len(st)>0:
            res = st.pop(0)
            while len(st)>0:                
                operator = st.pop(0)
                y = st.pop(0)
                if operator == '+':
                    res = res+y
                elif operator == '-':
                    res = res-y
                else:
                    print ('error 3')
        return res

msol = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
ares = msol.calculate(s)
print(ares)        
            
                