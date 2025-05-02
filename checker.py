import subprocess
import os

def check_question(question_dir,verbose=True):
    test_file = 'public_tests.py'
    public_results = subprocess.run(['python3',f'{os.path.join(question_dir,test_file)}'],capture_output=True,text=True)
    public_results = public_results.stdout
    if verbose:
        print(public_results)
    #
    test_file = 'tests.py'
    results = subprocess.run(['python3',f'{os.path.join(question_dir,test_file)}'],capture_output=True,text=True)
    results = results.stdout
    if verbose:
        print(results)
    pos = results.find('True')
    return pos > 0

