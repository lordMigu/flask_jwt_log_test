class Language():

    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
