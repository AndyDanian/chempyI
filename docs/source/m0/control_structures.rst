Control Structures
------------------

Python allow three control structures: sequential, selection and repetition.


Sequential
^^^^^^^^^^

In this structure the Python code is ejecuted line by line wihtout skip or repeat one.

.. code-block:: python
   :caption: Squential control structure.

   hello = 'Hello'
   world = 'world!'
   hello_world = hello + ' ' + world

Selection
^^^^^^^^^^

Sometimes is necessary skip some lines or select one line over others by any special reason. This is possibly with the Python's keywords **if, elif and else** because these keywords allow selected between two operations.

.. code-block:: python
   :caption: if and else control structure.

    # first example
    if a > b:
        a += 2
    # second example
    if a > b:
        a += 2
    else:
        b *= 3
    # third example
    if a > b:
        a += 2
    elif b < c:
        b *= 3
    # fourth example
    if a > b:
        a += 2
    elif b < c:
        b *= 3
    else:
        c -= 4

Moreover, this control structures allow the nested.

.. code-block:: python
   :caption: Nested with if and else control structure.

   if a > b:
        if b < c:
            a += 3
        else:
            b = 2
    elif a == b:
        b *= 3
    else:
        if c >= a:
            c -= 2
        elif b > c:
            b -= 2
        else:
            c *= 5

Repetition
^^^^^^^^^^

There are two types of repetition control structures in Python. One run over array of elements, *foor loop*, while the another one finish when a specific condition is reached, *while loop*.