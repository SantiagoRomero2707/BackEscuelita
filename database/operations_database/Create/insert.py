class Create(object):
    def __init__(self, model_db, instance_model, object_connection):
        self.model_db = model_db
        self.instance_model = instance_model['data']
        self.object_connection = object_connection

    def insert_data(self):
        """ Create """
        # Insert Data
        print(self.instance_model)
        instances_object = self.model_db(**self.instance_model)
        self.object_connection.add(instances_object)
        self.object_connection.commit()
        return f'Successful insert'
