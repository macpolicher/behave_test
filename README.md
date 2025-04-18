# BDD FRAMEWORK USING BEHAVE AND PYTHON WITH PAGE OBJECT MODEL


**FEATURES**
1. LANGUAGE: Python Programming Language
2. BDD: Behave
3. REPORTING: Allure Report


**HOW TO USE**
1. Clone the repository

2. Add Interpreter

Activate the virtual environment (Windows)

.venv\Scripts\activate

   
3. install the requirements.txt
   
command: pip install -r requirements.txt

3. go to console and run sample script:

python -m behave --tags=@valid_login






**FOR SHOWING ALLURE REPORT:**

Pre-requisite: Allure must be installed and configured in your machine.

documentation: https://allurereport.org/docs/install-for-windows/


**Commands**
1. FOR RUNNING TEST: python -m behave --tags=@valid_login
2. FOR SETTING UP THE REPORT: allure generate --clean
3. FOR OPENING THE REPORT: allure open


**IF REQUIRED**
1. When you open the feature files for the first time and it's asking to install a Gherkin plugin in upper right corner, please install it
2. When you open the .ini files for the first time and it's asking to install a .ini plugin in upper right corner, please install it
