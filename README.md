PPAPScript
===============================

PPAPScript is a programming language which imagined "PPAP"(Pen-Pineapple-Apple-Pen) of Japanese singer-songwriter Pico Taro's song.

# Setup

Install necessary libraries

```bash
$ pip install -r requirements
```

# Run

Run PPAPScript

```bash
$ python ppapscript.py
```

# Language Specification

1.Be sure to enter "PPAP" after you start the PPAPScript. Otherwise PPAPScript will not run.

```
> PPAP
Welcome to PPAPScript
```

2.Available variable names are only "pen", "pineapple", "apple" combination.(Upper case and lower case letters are ignored)

3.When declaring variables, you must include "I_have_a" or "I_have_an" before variables.

```
> I_have_a pen = "Pen"
```

4.The output function is "Ah!".

```
> I_have_a pen = "Pen"
> I_have_an apple = "Apple"
> Ah! apple + pen
ApplePen
```

5.Simple four arithmetic operations.

```
> I_have_an applePen = apple + pen
```

6.Simple comment out.

```
> # Ah! apple
```


# License
MIT
