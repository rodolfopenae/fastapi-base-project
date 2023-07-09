from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from kernel.infraestructure.postgres_database import Base

class UserTable(Base):
    __tablename__= 'users'
    
    id = Column(Integer, autoincrement=True, primary_key= True, index= True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    
    workspace = relationship("WorkspaceTable", back_populates='user')