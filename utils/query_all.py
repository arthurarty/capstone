def query_all(cls):
    """Query and format all records
    from a given model
    """
    items = cls.query.all()
    formated_items = [item.format() for item in items]
    return formated_items
