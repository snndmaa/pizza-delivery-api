from sqlalchemy import create_engine;
from sqlalchemy.orm import declarative_base, sessionmaker;

connection_string = 'postgresql://postgres:sobriety@database-2.ceynanps8tbw.us-east-1.rds.amazonaws.com:5432/test';
engine = create_engine(
    connection_string,
    echo=True,
);

Base = declarative_base();

Session = sessionmaker();