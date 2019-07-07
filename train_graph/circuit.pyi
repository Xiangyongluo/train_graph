from .train import Train
from .graph import Graph
from .pyETRCExceptions import *
from typing import *
from datetime import datetime

class CircuitNode:
    _checi=... #type:str
    _train=...#type:Train
    _start=...#type:str
    _end=...#type:str
    link=...#type:bool
    graph=... #type:Graph
    @overload
    def __init__(self,graph:Graph,*,checi,train:Optional[Train]=...,
                 start:Optional[str]=...,end:Optional[str]=...,link:Optional[bool]=...):...
    @overload
    def __init__(self,graph:Graph,*,train:Train,checi:Optional[str]=...,
                 start:Optional[str]=...,end:Optional[str]=...,link:Optional[bool]=...):...
    @overload
    def __init__(self,graph:Graph,*,origin:list):...
    def parseInfo(self,origin:dict)->None:...
    def outInfo(self)->dict:...
    def train(self)->Train:...
    def checi(self)->str:...
    def setCheci(self,checi:str):...
    def setTrain(self,train):...
    def startStation(self)->str:...
    def endStation(self)->str:...

class Circuit:
    CARRIAGE = 0x0
    MOTER = 0x1
    graph=... # type:Graph
    _name = ... # type:str
    _order = ... # type:List[CircuitNode]
    _type = ... # type:int
    _note=... #type:str
    _model=... # type:str
    _owner=... # type:str
    def __init__(self,graph,name:str=None,origin:dict=None):...
    def parseInfo(self,origin:dict):...
    def outInfo(self)->Dict:...
    def name(self)->str:...
    def setName(self,name:str):...
    def type(self)->int:...
    def setType(self,type_:int):...
    def note(self)->str:...
    def setNote(self,note:str):...
    def model(self)->str:...
    def setModel(self,m:str)->None:...
    def owner(self)->str:...
    def setOwner(self,o:str)->None:...
    def removeTrain(self,train:Train):...
    @overload
    def addTrain(self,train:Train):...
    @overload
    def addTrain(self,train:Train,order:int):...
    def orderStr(self)->str:...
    def trainCount(self)->int:...
    def nodes(self)->Iterable[CircuitNode]:...
    def clear(self)->None:...
    def addNode(self,node:CircuitNode)->None:...
    def preorderLinked(self,train:Train)->(Union[Train,None],Union[datetime,None]):...
    def postorderLinked(self,train:Train)->(Union[Train,None],Union[datetime,None]):...
    def trainOrderNum(self,train:Train)->int:...
    def replaceTrain(self,old:Train,new:Train)->None:...