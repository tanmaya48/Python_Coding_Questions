import os
from checker import check_question
import argparse


Q_DIR = '/home/ce/sessions/code_questions/questions'
diff_dirs = {name : os.path.join(Q_DIR,name) for name in os.listdir(Q_DIR)}

question_diff = {}
for name,folder in diff_dirs.items():
    questions = os.listdir(folder)
    for q in questions:
        question_diff[q] = name



def get_overall_status():
    diff_scores = {'Easy':[0,0],
                   'Medium':[0,0],
                   'Hard':[0,0]}
    for q,d in question_diff.items():
        question_path = os.path.join(Q_DIR,d,q)
        diff_scores[d][1]+=1
        if check_question(question_path,verbose=False):
            diff_scores[d][0]+=1
    return diff_scores
 


def get_status(name,verbose=True):
    d = question_diff[name]
    question_path = os.path.join(Q_DIR,d,name)
    return check_question(question_path,verbose)

def main(args):
    if args.name is not None:
        get_status(args.name)
        return
    diff_scores = get_overall_status()
    print(diff_scores)

     
    



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple argparse example")
    parser.add_argument('-n','--name', type=str, default=None, help="name of the question")
    args = parser.parse_args()
    main(args)
