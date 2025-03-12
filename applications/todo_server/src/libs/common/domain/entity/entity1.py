# app/common/domain/entity/entity1.py
from abc import ABC
from dataclasses import dataclass


@dataclass
class Entity1(ABC):
    id: str
    name: str
    description: str
