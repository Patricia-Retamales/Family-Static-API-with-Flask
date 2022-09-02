
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 30,
            "lucky_numbers": [3, 5, 8]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]  
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

   
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        try:
            if member["id"] == None:
                pass
        except Exception as e:
            print(f"Add member: {e}")
            member["id"] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        result = {"done": False}
        try:
            self._members = list(filter(lambda member: id != member["id"], self._members))
            result["done"] = True
        except Exception as e:
            print(f"Get member: {e}")
        return result

    def get_member(self, id):
        result = {}
        try:
            for member in self._members:
                if member["id"] == id:
                    result = member
        except Exception as e:
            print(f"Get member: {e}")
        return result

  
    def get_all_members(self):
        print(self._members)
        return self._members