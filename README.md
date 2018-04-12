# py-app-composer-for-text-modules

## spec

- python3.6 or later

## spec for sample modules

- morpyAnalyzer: [MeCab](http://taku910.github.io/mecab/)
- analyzer: [gensim3.4 or later](https://pypi.python.org/pypi/gensim)

## How to use

1. clone this repository ```git clone git@github.com:reouno/py-app-composer-for-text-modules.git```
2. run following command.

  just run one module

  ```bash
  python3 run.py "./sample_modules/helloworld/hello.py"
  ```
  
  bind (```>>=```) modules and run (pass the output from first mod to second mod)
  
  ```bash
  python3 run.py "./sample_modules/reader/read.py >>= ./sample_modules/morphAnalyzer/wakati.py" -i ./sample_text/text.txt
  ```
  
  just run modules sequentially (```>>```) (throw away the output from first mod and run second mod)
  
  ```bash
  python3 run.py "./sample_modules/reader/read.py >> ./sample_modules/helloworld/hello.py" -i ./sample_text/text.txt
  ```
  
  bind more modules
  
  ```bash
  python3 run.py "./sample_modules/reader/read.py >>= ./sample_modules/morphAnalyzer/wakati.py >>= ./sample_modules/analyzer/bagOfWords.py >> ./sample_modules/helloworld/hello.py" -i ./sample_text/text.txt
  ```
