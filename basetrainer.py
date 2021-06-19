import torch 

class BaseTrainer():

	def __init__(self,config,network):

		'''
		config:-> a dictionary, reading a JSON file using json lib 
		'''

		self.logs_dir = config['logs_dir']
		self.weights_dir = config['weights_dir']
		self.network = network
		self.gpus = config['gpus']
		self.device = config['device']


	def train(self):

		raise NotImplementedError()

	def inference(self):

		raise NotImplementedError()


	def eval(self):

		raise NotImplementedError()