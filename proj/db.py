from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.pool import QueuePool, NullPool
from logging_helper import get_db_logger

__all__ = ["SqlalchemyDriver"]


class SqlalchemyDriver():

    name = "SqlalchemyDriver"
    supported_db = {
        "mysql": "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4",
        "postgres": "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    }

    def __init__(self, host, user, password, port, database, pool_size=5,
                 max_overflow=10, db_type="postgres", pool_class="QueuePool"):
        logger = get_db_logger(self.name)
        db_url = self.supported_db.get(db_type)

        if not db_url:
            raise Exception("Not support db type '{}'".format(db_type))
        db = db_url.format(user=user, password=password, host=host,
                           port=port,
                           database=database)

        kwargs = {
            "pool_size": pool_size,
            "max_overflow": max_overflow,
            "pool_recycle": 1800,
            "pool_pre_ping": True,
            "poolclass": QueuePool,
        }

        if "NullPool" == pool_class:
            print("init null pool class")
            kwargs = {
                "pool_recycle": 1800,
                "pool_pre_ping": True,
                "poolclass": NullPool,
            }

        if db_type == "postgres":
            kwargs["client_encoding"] = "utf8"
        logger.info("init db")
        print("init db")
        engine = create_engine(db, **kwargs)
        session_factory = sessionmaker(bind=engine, autoflush=False)
        self.db_session = scoped_session(session_factory)
        # reflect the tables
        base = automap_base()
        base.prepare(engine, reflect=True)
        self.db_map_classes = base.classes


def get_db_info():
    db_driver = SqlalchemyDriver(
        db_type="mysql",
        host="192.168.1.3",
        port="33306",
        user="root",
        password="root",
        database="forest",
    )
    return db_driver.db_session, db_driver.db_map_classes