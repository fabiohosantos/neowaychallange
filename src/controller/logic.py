import pandas as pd 
import json
from utils import utils 
from controller import threadmanager 
import datetime
from utils.configuration import Config


def load_data(directory):
	
	#directory = 'D:\\Pessoal\\Estudos\\neoway\\data'
	nthreads = int(Config.get_value('threads'))
	pool = threadmanager.ThreadPool(nthreads) #based on cpu number available
	chunksize = int(Config.get_value('chunksize'))
	print("Started Data Ingestion")
	for file in utils.listfiles(directory):
		print("Processing file: " + file)
		print(datetime.datetime.now().time())
		for chunk_df in pd.read_csv(file, chunksize=chunksize, iterator=True):
			insert_query, data = parse_data(chunk_df)
			#call workers to input data in parallel
			threadmanager.do_ingestion(insert_query, data, pool)	
	print("Finished Data Ingestion")
	print(datetime.datetime.now().time())


def parse_data(chunk_df):
	df = pd.DataFrame(chunk_df)
	data = []
	for index, row in df.iterrows():
		str_json = ("{},{}".format(row[0], row[1]))
		line_json = json.loads(str_json)
		pk = int(line_json['pk'])
		score = int(line_json['score'])
		pair = (pk, score)
		data.append(pair)

	records_list_template = ','.join(['%s'] * len(data)) 
	insert_query = 'insert into scores (pk, score) values {}'.format(records_list_template)			
	return insert_query, data