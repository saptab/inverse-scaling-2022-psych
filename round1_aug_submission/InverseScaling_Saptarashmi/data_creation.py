#Code by Saptarashmi Bandyopadhyay
import pandas as pd
import numpy as np
import sys

#raw data format: Q_id,raw_question,raw_answers,answer_idx,body
#final data format: prompt, classes, answer_idx, source_dataset, Q_id, body (bool), prompt_in_front (bool), binarized (bool)
#prompt_in_front: 1 means the prompt and raw answers are at the front. prompt_in_front: 0 means the prompt and raw answers are at the back. 
#binarized: 1 refers to binarized answers. binarized: 0 refers to original answers.
def create_data(df, source_dataset):
	final_data = []
	binary_answer_idx = 0
	if source_dataset == "cfcs":
		orig_classes = ['1','2','3','4','5']
		binary_raw_answers = "1. extremely uncharacteristic, 2. extremely characteristic."
		front_prompt = "Please rate how well the following statement applies to you on a scale of "
		back_prompt = " How well does the preceding statement represent you? Rate on a scale of "
	else:
		orig_classes = ['1','3','5']
		front_prompt = "Please rate your agreement or disagreement with the following statement on a scale of "
		back_prompt = " How much do you agree or disagree with the preceding statement? Rate on a scale of "
		if source_dataset == "sd3":
			binary_raw_answers = "1. disagree, 2. agree."
		else:
			binary_raw_answers = "1. Disagree, 2. Agree."		
	binary_classes = ['1','2']
	for index, row in df.iterrows():
		if row["Q_id"] =="P3" or row["Q_id"] =="P5":
			print(row["body"] + "check")
		if row["body"] == "NB":
			if row["answer_idx"] == 1:
				binary_answer_idx = 1
			else:
				binary_answer_idx = 2
			#prompt engineering of original text at the front of the statement
			orig_prompt_front = front_prompt + row["raw_answers"] + " Statement: " + row["raw_question"]
			orig_row_front = [orig_prompt_front, orig_classes, row["answer_idx"], source_dataset, row["Q_id"], row["body"], 1, 0]
			final_data.append(orig_row_front)
			#prompt engineering of original text at the back of the statement
			orig_prompt_back = "Statement: " + row["raw_question"] + back_prompt + row["raw_answers"] 
			orig_row_back = [orig_prompt_back, orig_classes, row["answer_idx"], source_dataset, row["Q_id"], row["body"], 0, 0]
			final_data.append(orig_row_back)
			#prompt engineering of binary text at the front of the statement
			binary_prompt_front = front_prompt + binary_raw_answers + " Statement: " + row["raw_question"]
			binary_row_front = [binary_prompt_front, binary_classes, binary_answer_idx, source_dataset, row["Q_id"], row["body"], 1, 1]
			final_data.append(binary_row_front)
			#prompt engineering of binary text at the back of the statement
			binary_prompt_back = "Statement: " + back_prompt + binary_raw_answers + row["raw_question"]
			binary_row_back = [binary_prompt_back, binary_classes, binary_answer_idx, source_dataset, row["Q_id"], row["body"], 0, 1]
			final_data.append(binary_row_back)
	return final_data

def main_fn():
	df = pd.read_csv(sys.argv[1])
	source_dataset = sys.argv[2]
	final_dataset = sys.argv[3]
	final_data = create_data(df, source_dataset)
	created_df = pd.DataFrame(final_data, columns=['prompt', 'classes', 'answer_idx', 'source_dataset', 'Q_id', 'body', 'prompt_in_front', 'binarized'])#new DataFrame
	created_df.to_csv(final_dataset, index=False,header=True)

if __name__=="__main__":
    	main_fn()
