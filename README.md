# ChemPyI: Chemistry-Python Course

Programming is everywhere nowadays, and programmers and in high demand. AI was the topic of 2023 and will be on the top for many years. Quantum Computing will be the next wave.

You could be surfing the next wave of ultra-high salaries and solving problems for big tech companies or leading the next unicorn.

> **Who will be the best candidate to make and design applications for AI and Quantum Computing?**
> Yes, you, who learn how to write code, design applications and solve new problems by applying the knowledge of chemistry and physics in the real world.

## Roadmap

1. Introduction to Python for Chemists

   1. Setting up the Python (environment, IDE, and Jupyter Notebook)
   2. Basic programming concepts
   3. Variables, data types, and operators
   4. Control structures (if-else, loops)
   5. Functions and modules

2. Scientific Python for Chemists

   1. Jupyter Notebook for Interactive Computing
   2. Matplotlib for Data Visualization
   3. NumPy for Numerical Computing
   4. SciPy for Scientific Computing
   5. SymPy for Symbolic Computing

3. Data Science for Chemists

   1. Pandas for Data Manipulation and Analysis in Chemistry
   2. File I/O and data serialization
   3. Advanced Excel processing with Python
   4.

4. Data Structures and Algorithms in Python

   1. Lists, tuples, and dictionaries
   2. Sets and strings
   3. Time complexity and Big O notation
   4. Searching and sorting algorithms

5. Best Practices for Scientific Computing

   1. Testing and debugging
   2. Coding style and documentation
   3. Version control with Git and GitHub
   4. Reproducibility and data management

6. Chemical Informatics and Computational Chemistry

   1. Introduction to Cheminformatics
   2. RDKit for Cheminformatics
   3. Chemoinformatics with Python
   4. Molecular Modeling and Visualization

7. Bioinformatics and Computational Biology

   1. Introduction to Bioinformatics
   2. BioPython and BioPandas
   3. Bioinformatics with Python

8. Advanced Topics

   1. Object-Oriented Programming (OOP) in Python
   2. CI/CD with GitHub Actions
   3. Web Documentation with Sphinx
   4. Building a Python package
   5. Packaging and distribution with PyPI

9. Introduction to Artificial Intelligence and Machine Learning

   1. Overview of AI and ML concepts
   2. Supervised and unsupervised learning
   3. Popular ML algorithms (e.g., linear regression, decision trees, neural networks)
   4. Training and evaluating models

10. AI Applications in Chemistry and Physics

    1. Molecular property prediction
    2. Drug discovery and design
    3. Materials science and computational chemistry
    4. Quantum chemistry and electronic structure calculations

11. Introduction to Quantum Computing

    1. Quantum mechanics fundamentals
    2. Qubits, quantum gates, and quantum circuits
    3. Quantum algorithms (e.g., Shor's, Grover's)
    4. Quantum error correction and fault tolerance

12. Quantum Computing with Python

    1. Quantum computing libraries (e.g., Qiskit, Cirq, Q#)
    2. Implementing quantum algorithms in Python
    3. Quantum machine learning
    4. Quantum chemistry and quantum simulation

## Contents

1. **Module 0** - Setting Up Your Python Environment

   - Basic requirements for accessing the course materials
   - Install Python on your computer
   - Using Python environments
   - Set up an Integrated Development Environment (IDE)
   - Jupyter Notebook and Google Colab

- Module 1:

  - SubModule 1: Data Type and Operators
    - Python presentation
    - Data types and properties
    - Binary operators over simple data
    - Binary operators over structure data
    - Comparative operators
    - Logic operators
    - Belong and identity operators
  - SubModule 2:
    - for loop
    - while loop
    - if-elif-else conditional
    - functions and arguments
  - Definition: input and output. import. open, read and write files.
  - Program: made structured data from csv file
  - Program: the atomic mass porcentage from molecule formule
  - Program: calculate quantities of ideal gases from its equation
  - Program: pH titulation
  - Program: Oxidized and reduced substance in redox reaction
  - Program: Signs number and their intesities relation in a spin-spin coupling spectrum

- Module 2

  - Definition: [Matplotlib](https://andydanian.github.io/chempyI/presentations/m2/c1_matplotlib_presentation.slides.html#/)
  - Definition: NumPy
  - Program: Balancing a chemical equantion
  - Program: Balancing a Redox reaction
  - Program: Equilibrium constant of a reaction
  - Program: Evolution of the concentrations in the time
  - Definition: SciPy
  - Program: Scientific constants and rule of three
  - Program: Number of Hs associated a HNMR sign
  - Program: Pressure vapor minimum
  - Program: Physcial's or chemical's property statistical
  - Definition: Sympy
  - Program: Formation or descomposition rate
  - Program: Concentrations from simultaneous chemical reactions

- Module 3

  - Definition: Py3DMol
  - Definition: NGL
  - Definition: PyMol

- Module 4

  - Definition: RDKit
  - Definition: ChemFormula
  - Definition: Chemlib
  - Definition: ChemPy
  - Definition: Mendeleev
  - Definition: pyEQL

- Module 5

  - BioPython
  - BioPandas

- Module 6
  Se expondra conceptos y se reformula los programs usando POO

# Requeirment

The first step is to build virtual environment

```
python3 -m venv /path/virtual_environment_name
```

to activate the virtual environment

```
source /path/virtual_environment_name/bin/activate
```

to exit the virtual environment, execute the next command in the prompt

```
deactivate
```

For the correct work, it is necessary to install the next packing:

```
pip install scipy
pip install sympy
pip install numpy
pip install pandas
pip install jupyter
pip install ipykernel
pip install rise
```

or execute

```
pip install -r requeriment.txt
```
