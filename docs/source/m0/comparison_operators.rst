Comparison Operators
--------------------

The comparison operator are the following:

* Equal (==)
* Different (!=)
* Higher than (>)
* Higher or equal than (>=)
* Lower than (<)
* Lower or equal than (=<)

These operator return a bool value (True or False).

The symbol = is also an operator in Python and named the assignation operator.


.. code-block:: python
   :caption: Comparison operators.

   a = 3
   b = 2
   a == b   # False
   a != b   # True
   a > b    # True
   a >= b   # True
   a < b    # False
   a <= b   # False


The comparison operator can be applied over listes, tuples and strings. 

.. code-block:: python
   :caption: Comparison operators over listes and tuples.

   # first example  
   [2, 3, 4] > [1, 2]   # True
   # second example 
   (1, 2) <= (4, 5, 6)  # False
   # third example
   (1, 2) == (4, 5, 6)  # False
   # fourth example
   [2, 3, 4] != [1, 2]  # True

In the first example, the return value is the result of the comparison between 3 with 2 (3 > 2), because the comparison is carried out element by element. In the case of the second example, the result is False because 2 is lower than 5. In the next examples the results are False and True because the tuples are different and lister are equal, respectively. 

In the case of the strings, the comparison operator uses the `Unicode <https://docs.python.org/3/howto/unicode.html>`_ value of the strings.


.. code-block:: python
   :caption: Comparison operators over string.

   # first example  
   'a' == 'a'      # True
   # second example
   'a' == 'A'      # False
   'a' >  'A'      # True
   'a' <  'b'      # True