Operators
---------

There are two operators types. One operators type involve one element, number or string, instead the other operators type involve two elements. The first ones are named unary operators, instead the others are the binary operators.

The symbol *=* is also an operator in Python and named the assignation operator.


Unary Operators
^^^^^^^^^^^^^^^

There are two unary operators in Python. These are represent by the symbol + and -, which are the symbols associated to the sum and rest operators. The unary operator *+* is generally implicit.

.. code-block:: python
   :caption: Unary operators.

   # + example
   one = 1
   one = +1
   # - example
   minus_one = -1


Binary Operators
^^^^^^^^^^^^^^^^

The sum, rest, multiplication, division, integer division, power, and module are binary operatorations while the operatos associated are +, -, *, /, //, ** and %. The operation result is a float when involves at least one float, however the division always return a float independently of the number types, for this reason exists the integer division.

.. code-block:: python
   :caption: Binary operators.

   # + example
   three = 1 + 2
   # - example
   one = 2. - 1. 
   # * example
   two = 1 * 2.
   # / example
   two = 2 / 1 
   # // example
   two = 2 // 1
   # ** example
   four = 2**2
   # % example
   one = 3%2

The compounds operators are another form to do binary operations, where the binary operator is put on before the assignation operator, then the operation do with the numbers in both side of =. 

.. code-block:: python
   :caption: Binary operators with compounds operators.

   # + example
   three = 2
   three += 1
   # - example
   one = 2
   one -= 1. 
   # * example
   two = 1
   two *= 2.
   # / example
   two = 2
   two /= 1
   # // example
   two // =  1
   # ** example
   four = 2
   four **= 2
   # % example
   one = 3
   one %= 2

Moreover, the binary operations satisfy the following ejecution order:

.. table:: Ejecution order of binary operators. 
   :align: center
   
   +-------------+-------------+---------+
   | Priority    | Operator    |  Type   |
   +-------------+-------------+---------+
   |     1       | +, -        | Unary   |
   +-------------+-------------+---------+
   |     2       |  `**`       |  Binary |
   +-------------+-------------+---------+
   |     3       |`*`, /, //, %|  Binary | 
   +-------------+-------------+---------+
   |     4       |  +, -       |  Binary | 
   +-------------+-------------+---------+