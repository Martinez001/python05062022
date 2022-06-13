{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i sold two pairs of shirts for 15000, a shoe for 25000 and a suit for 45000\n"
     ]
    }
   ],
   "source": [
    "price1 = 15000\n",
    "price2 = 25000\n",
    "price3 = 45000\n",
    "\n",
    "report ='i sold two pairs of shirts for {}, a shoe for {} and a suit for {}'\n",
    "print(report.format(price1,price2,price3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i sold two pairs of shirts for 25000, a shoe for 15000 and a suit for 45000\n"
     ]
    }
   ],
   "source": [
    "print(f'i sold two pairs of shirts for {price2}, a shoe for {price1} and a suit for {price3}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PYTHON\n",
      "python\n",
      "Python Is Fun\n",
      "Python is fun\n",
      "['python', 'is', 'fun']\n",
      "info@gmail.com\n"
     ]
    }
   ],
   "source": [
    "word1='python'\n",
    "word2='PYTHON'\n",
    "word3='python is fun'\n",
    "word4='    info@gmail.com'\n",
    "\n",
    "print(word1.upper())\n",
    "print(word2.lower())\n",
    "print(word3.title())\n",
    "print(word3.capitalize())\n",
    "print(word3.split())\n",
    "print(word4.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45\n"
     ]
    }
   ],
   "source": [
    "num2 = str(45)\n",
    "print(num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "num1 = int(12.5)\n",
    "print(num1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "252528\n"
     ]
    }
   ],
   "source": [
    "num3 = 252528.8235\n",
    "print(int(num3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "252529\n"
     ]
    }
   ],
   "source": [
    "print(int(round(num3)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45\n"
     ]
    }
   ],
   "source": [
    "print(str(num2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# OPERATORS"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Arithmetic operators\n",
    "# +  addition\n",
    "## -  subtraction\n",
    "## *  multiplication\n",
    "## /  division\n",
    "## %  modulous\n",
    "## //  integer division\n",
    "## **  exponential"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25 + 15 = 40\n",
      "25 - 15 = 10\n",
      "25 X 15 = 375\n",
      "25 / 15 = 1.6666666666666667\n",
      "25 % 15 = 10\n",
      "25 // 15 = 1\n",
      "25 ^ 15 = 931322574615478515625\n"
     ]
    }
   ],
   "source": [
    "number1= 25\n",
    "number2= 15\n",
    "\n",
    "print(f'{number1} + {number2} = {number1 + number2}')\n",
    "print(f'{number1} - {number2} = {number1 - number2}')\n",
    "print(f'{number1} X {number2} = {number1 * number2}')\n",
    "print(f'{number1} / {number2} = {number1 / number2}')\n",
    "print(f'{number1} % {number2} = {number1 % number2}')\n",
    "print(f'{number1} // {number2} = {number1 // number2}')\n",
    "print(f'{number1} ^ {number2} = {number1 ** number2}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Comparism operators\n",
    "## > greater than\n",
    "## < less than\n",
    "## >= greater than or equal to\n",
    "## <= less than or equal to\n",
    "## == equal to\n",
    "## != not equal to"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n",
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(number1 > number2)\n",
    "print(number1 < number2)\n",
    "print(number1 >= number2)\n",
    "print(number1 <= number2)\n",
    "print(number1 == number2)\n",
    "print(number1 != number2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i have 1000dollars so i can buy 3 football for 450dollars.\n"
     ]
    }
   ],
   "source": [
    "totalmoney=1000\n",
    "quantity=3\n",
    "price=450\n",
    "print(f'i have {totalmoney}dollars so i can buy {quantity} football for {price}dollars.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## LOGICAL OPERATORS\n",
    "# and\n",
    "# or\n",
    "# not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(number1 != number2 and number1 < number2 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(number1 != number2 or number1 < number2 )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(not number1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  MEMBERSHIP OPERATORS\n",
    "# IN\n",
    "# NOT IN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "word= 'School'\n",
    "print('s' in word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print('p' not in word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# IDENTITY OPERATORS\n",
    "## IS\n",
    "## IS NOT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(number1 is number2)\n",
    "print(number1 is not number2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
