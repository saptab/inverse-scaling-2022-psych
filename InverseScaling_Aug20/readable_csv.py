#Code by Saptarashmi Bandyopadhyay
import pandas as pd
import sys

def main_fn():
	df = pd.read_csv(sys.argv[1])
	print(df.to_string()) 
	for index, row in df.iterrows():
		a = row["raw_question"]
		b = row["raw_answers"]
		back_prompt = " How well does the above statement represent you? Rate on a scale of "
		back_p = "Statement: " + a + back_prompt + b
		front_prompt = "Please rate how well the following statement applies to you on a scale of "
		front_p = front_prompt + b + " Statement: " + a
		#print(a)
		#print(b)
		print(back_p)
		print(front_p)

if __name__=="__main__":
    	main_fn()
