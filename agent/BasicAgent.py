import numpy as np
import redis as redis
import utils
import time
import json
import random
import string

class BasicAgent(object):
    def __init__(self, agent_name, subprefix, agentkey, debug=False):
        super(BasicAgent, self).__init__()
        self.agent_name = agent_name
        print(f"Initialing {agent_name}...")

        self.db_host = 'localhost'
        self.db_port = 6379
        self.db_idx = 0
        self.subprefix = subprefix
        self.agentkey = agentkey

        self.db = redis.Redis(host=self.db_host, port=self.db_port, db=self.db_idx)
        self.subpattern = f'__keyspace@{self.db_idx}__:{self.subprefix}'
        self.agentpattern = f'__keyspace@{self.db_idx}__:{self.agentkey}'

        self.debug = debug

        self.check_notify()

        self.pubsub = self.db.pubsub()
        self.pubsub.psubscribe(**{self.subpattern: self.event_handler})
        self.pubsub.psubscribe(**{self.agentpattern: self.agent_event_handler})
        self.thread = self.pubsub.run_in_thread(sleep_time=0.001)

        self.get_config()

    def d_msg(self, msg):
        if self.debug:
            print(f"[{self.agent_name}] {msg}")
        pass

    def get_config(self):
        with open("config.json", 'r') as f:
            config = json.load(f)
        self.c = config
        
    def utf8_decode(self, msg):
        return msg.decode("utf-8")

    def check_notify(self):
        self.db.config_set('notify-keyspace-events', 'KEAx')

    def agent_event_handler(self, msg):
        pass

    def event_handler(self, msg):
        pass