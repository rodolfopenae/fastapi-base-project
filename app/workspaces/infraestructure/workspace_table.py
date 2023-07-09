from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from kernel.infraestructure.postgres_database import Base

class WorkspaceTable(Base):
    __tablename__= 'workspaces'

    id = Column(Integer, autoincrement=True, primary_key= True, index= True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("UserTable", back_populates='workspace')