# Markov_chain Project

This repository contains a Python script that implements a Markov chain text generator and uses the `graficar` module to generate a graphical representation of the character frequency distribution.

## Installation

To run the script, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/LeoLizc/Markov_chain.git
   ```

2. Install the required dependencies. Make sure you have Python 3.x and pip installed, and then run the following command:

   ```bash
   pip install matplotlib numpy
   ```

3. Once the dependencies are installed, you can run the script using the following command:

   ```bash
   python script.py
   ```

## Usage

The script `script.py` contains the following functions:

### `gen_mmarkov(s, k=0)`

This function generates a Markov model based on a given input text string `s` and an optional parameter `k`. The default value of `k` is 0. The function returns the Markov model as a dictionary, the initial substring, and the value of `k`.

### `cad_markov(n, m, ini=None, k=0)`

This function generates a text of length `n` based on a given Markov model `m`. The optional parameter `ini` specifies the initial substring, and the default value is None, which causes the function to use the first key in the model as the initial substring. The parameter `k` specifies the value of `k` used to generate the Markov model. The function returns the generated text and a frequency dictionary of the substrings.

### `gen_c(pr, n)`

This function generates a character based on a dictionary `pr` containing the frequency of each character and a total count `n`.

### `markov(entrada, salida, n, k)`

This function reads an input file specified by `entrada` and generates a Markov model with parameter `k`. It then generates a text of length `n` and writes it to the output file specified by `salida`. Additionally, it generates a graphical representation of the frequency distribution using the `graficar` module.

## Running the Script

When running the script, you will be prompted to provide an input file and an output file. If no input file is provided, the default file `frankenstein.txt` will be used. If no output file is provided, the default file `output.txt` will be used. The script will generate a Markov model with a text length of 800 and a value of `k` equal to 2. The generated text will be written to the output file, and a graphical representation of the character frequency distribution will be displayed.

## Dependencies

The script relies on the following dependencies:

- matplotlib
- numpy

Make sure you have these packages installed before running the script. If not, you can install them using the following command:

```bash
pip install matplotlib numpy
```

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to your needs.
