# -*- coding:utf-8 -*-

from rediscluster import RedisCluster

startup_nodes = [
    {"host": "127.0.0.1", "port": 8001},
    {"host": "127.0.0.1", "port": 8002},
    {"host": "127.0.0.1", "port": 8003},
    {"host": "127.0.0.1", "port": 8004},
    {"host": "127.0.0.1", "port": 8005},
    {"host": "127.0.0.1", "port": 8006},
]


class SituationValuation:
    def __init__(self):
        self.__rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

    @staticmethod
    def generate_key(situation):
        return "poker-endgamer:" + situation.id()

    def save(self, situation, value):
        key = self.generate_key(situation)
        self.__rc.set(key, int(value))

    def query(self, situation):
        key = self.generate_key(situation)
        v = self.__rc.get(key)
        if v is None:
            return v
        else:
            return bool(int(v))
