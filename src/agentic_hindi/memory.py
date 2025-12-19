from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    user_text = Column(Text)
    agent_text = Column(Text)

class Memory:
    def __init__(self, db_path='sqlite:///memory.db'):
        self.engine = create_engine(db_path)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_turn(self, user_text, agent_text):
        s = self.Session()
        conv = Conversation(user_text=user_text, agent_text=agent_text)
        s.add(conv)
        s.commit()
        s.close()

    def recent(self, limit=5):
        s = self.Session()
        res = s.query(Conversation).order_by(Conversation.id.desc()).limit(limit).all()
        s.close()
        return [(r.user_text, r.agent_text) for r in res]
