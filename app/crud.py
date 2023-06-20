class CRUD:
    def __init__(self, session):
        self.session = session

    async def create(self, entity):
        return self.session.add(entity)

    async def delete(self, entity):
        return await self.session.delete(entity)

    async def get(self, stmt):
        return await self.session.scalar(stmt)

    async def get_all(self, stmt):
        return await self.session.scalars(stmt)

    async def commit(self):
        return await self.session.commit()
