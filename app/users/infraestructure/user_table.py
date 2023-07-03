from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from kernel.infraestructure.postgres_database import Base, engine

class UserTable(Base):
    __tablename__= 'user'
    
    id = Column(Integer, autoincrement=True, primary_key= True, index= True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    
    # workspace = relationship("Workspace", back_populates='owner')