# Indian Natural Language Detection (INLD)
Python package to detect Indian Languages from given text input. Works for direct language text input as well as certain combinations of those languages.

## Languages
You can use this package to detect the following Indian Languages  
***WIP :** (more languages are being continuously added)*

1. Direct Languages  
  
    | Language | Code |
    |:-:|:-:|
    | Assamese | am |
    |Bengali|bg|
    |English|en|
    |Gujarati|gj|
    |Hindi|hn|
    |Kannada|kd|
    |Malayalam|ml|
    |Marathi|mr|
    |Odia|od|
    |Punjabi|pb|
    |Telugu|tg|

2. Combined Languages
    
    | Language | Code |
    |:-:|:-:|
    | Hinglish (Hindi + English) | hng |
    | Punglish (Punjabi + English)| png |

## Usage
**Before using this library please also install latest version of** `pickle`  

```python
from INLD.INLD import detect

print(detect('ye ek example hai'))
# OUTPUT : ['hng']

print(detect('This is an example'))
# OUTPUT : ['en']
```
