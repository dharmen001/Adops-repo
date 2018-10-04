# coding=utf-8

"""
DataBaseReader
"""
from Config import Config
import _mysqlclient

class DataBaseReader(Config):

    def __init__(self):
        super(DataBaseReader,self).__init__()

    def DataBase(self):

