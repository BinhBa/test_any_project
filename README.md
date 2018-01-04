# TEST Project
This mini project is used to run unittest automatically.

## Package usage:
  - unittest2.
  - coverage.

## Install requirements:
  Using command below to install requirements:
  ```bash
  pip install -r requirements.txt
  ```
## Instruction:
  1. Copy test folder into main project.
  2. Using command:
  
    ```bash
    coverage run --source=./ test/__init__.py
    
    coverage html -d htmlcov
    ```
