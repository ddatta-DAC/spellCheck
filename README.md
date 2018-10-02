# spellCheck

Install python 3    
Install virtual environemnt package 
In ubuntu(linux) : sudo apt-get install python3-venv
Set up a virtual environment.   
python3 -m venv DIR   
source DIR/bin/activate   

set DIR="venv"  

This is to ensure that the following packages are available:  
1. pandas  
2. numpy   

------ 

Python spell checker using a DP edit distance algo.

To run the recursive version:

    python3  recursive_ed.py    

To run the Top down version:

    python3  topDown_ed.py    

To run the Bottom up version:

    python3  bottomUp_ed.py    
    
To run all cases in the cases.csv file :    

    python3 exec.py
    