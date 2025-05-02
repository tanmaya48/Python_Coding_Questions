import pandas as pd

# Login using e.g. `huggingface-cli login` to access this dataset
df = pd.read_json("hf://datasets/lbaf23/LeetCode-Contest/test.jsonl", lines=True)
df.to_csv('question_data.tsv',sep='\t',index=False)
