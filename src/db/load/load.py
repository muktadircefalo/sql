from src.config import Session, logger

@logger.catch
def load_to_db(table_instance, data_record):
    session = Session()
    try:
        session.bulk_insert_mappings(table_instance,data_record)
        session.commit()
        logger.info(f'{table_instance.__tablename__} is loaded to db')
    except Exception as ex:
        logger.error(f'{ex}')
        session.rollback()
