import os
import pandas as pd
from tqdm import tqdm


def read_table(table_path='question_data.tsv'):
    return pd.read_csv(table_path,sep='\t')




def get_question_details(row):
    title=row['title']
    prompt=row['prompt']
    public_tests=row['public_tests']
    tests = row['tests']
    difficulty = row['difficulty']
    return title,prompt,public_tests,tests,difficulty



base_path = 'questions'
if not os.path.exists(base_path):
    os.mkdir(base_path)

os.makedirs(os.path.join(base_path,'Easy'),exist_ok=True)
os.makedirs(os.path.join(base_path,'Hard'),exist_ok=True)
os.makedirs(os.path.join(base_path,'Medium'),exist_ok=True)

def save_questions(title,prompt,public_tests,tests,difficulty):
    title = difficulty + '/' + title.replace(' ','_')
    title_path = os.path.join(base_path,title)
    if not os.path.exists(title_path):
        os.mkdir(title_path)
    with open(os.path.join(title_path,"question.py"),'w') as f:
        f.write(prompt)
    func_name = prompt[prompt.find('def ')+4:prompt.find('(')]
    #
    #

    with open(os.path.join(title_path,"public_tests.py"),'w') as f:
        f.write(f'from question import {func_name}\n')
        f.write(f'tests = {public_tests}\ncorrect = 0\nfor t in tests:\n')
        f.write('    try:\n')
        f.write('        exec(t)\n')
        f.write('        correct+=1\n')
        f.write('    except:\n')
        f.write('        print(\'Failed Case:\')\n')
        f.write('        print(t)\n')
        f.write('success = len(tests) == correct\n')
        f.write('print(correct,\'/\',len(tests))\n')
        f.write('print(success)')
        
    with open(os.path.join(title_path,"tests.py"),'w') as f:
        f.write(f'from question import {func_name}\n')
        f.write(f'tests = {tests}\ncorrect = 0\nfor t in tests:\n')
        f.write('    try:\n')
        f.write('        exec(t)\n')
        f.write('        correct+=1\n')
        f.write('    except:\n')
        f.write('        pass\n')
        f.write('success = len(tests) == correct\n')
        f.write('print(correct,\'/\',len(tests))\n')
        f.write('print(success)')
        



def main():
    df = read_table()
    print(df.columns)
    for i in tqdm(range(len(df))):
        title,prompt,public_tests,tests,difficulty=get_question_details(df.iloc[i])
        save_questions(title,prompt,public_tests,tests,difficulty)




if __name__ == '__main__':
    main()
