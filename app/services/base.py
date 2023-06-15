from app.crud import CRUD


class BaseService:
    def __init__(self, model):
        self.model = model
        self.crud = CRUD(self.model)

    def create(self, entity):
        obj = self.model(**entity.dict())
        self.crud.create(obj)
        self.crud.commit()
        self.crud.refresh(obj)
        self.crud.close()
        return obj

    def update(self, new_value, new_value_id):
        db_value = self.crud.get_by("id", new_value_id)
        if db_value:
            for field, value in new_value.dict().items:
                setattr(db_value, field, value)
                self.crud.update(db_value)
            self.crud.commit()
            self.crud.close()

    def delete(self, value_id):
        db_value = self.crud.get_by("id", value_id)
        if db_value:
            self.crud.delete(db_value)
            self.crud.commit()
            self.crud.close()

    def get(self, value_id):
        db_value = self.crud.get_by("id", value_id)
        self.crud.close()
        return db_value

    def get_by_field(self, field_name, value):
        db_value = self.crud.get_by(field_name, value)
        self.crud.close()
        return db_value

    def get_all(self):
        db_value = self.crud.get_all()
        self.crud.close()
        return db_value

    def get_all_by_field(self, field_name, value):
        db_value = self.crud.get_by(field_name, value)
        self.crud.close()
        return db_value
