from locust import HttpUser, task, between, events
import queue, time, logging
import locust.stats
import numpy as np
import subprocess

locust.stats.CSV_STATS_INTERVAL_SEC = 1


@events.test_stop.add_listener
def on_test_stop(**kw):
	pass


class SimpleWorkload(HttpUser):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.nreq = 0
		self.act_exec = {}
		self.act_thread = {}
	
	def doWait(self,ttime):
		delay=np.random.exponential(scale=ttime)
		time.sleep(delay)
	
	
	#Activities
	def SockClient_a1(self):
		self.act_exec["SockClient_a1"]=True;
		self.doWait(1.0E-4);

		tgt_url = "SSAddress";
		self.client.get(tgt_url)
	def SockClient_a2(self):
		self.act_exec["SockClient_a2"]=True;
		self.doWait(1.0);

	
	#Dnodes
	def OrNode_SockClient_a1(self):
		#OrNode Logic
		label = []
		p = []
		label.append("SockClient_a2")
		p.append(1.0)
		
		randomChoice = np.random.choice(a=label,p=p)
		if(randomChoice=="SockClient_a2"):
			self.SockClient_a2()
	
	@task
	def visit_homepage(self):
		# execetute the entry activity
		self.SockClient_a1()
		# execetute the decision node of already executed evt
		if(self.act_exec["SockClient_a1"]!=None and self.act_exec["SockClient_a1"]):
		  self.act_exec["SockClient_a1"]=False
		  self.OrNode_SockClient_a1()
		
		

if __name__ == "__main__":
	SimpleWorkload().run()
	
