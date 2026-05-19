from pydantic import BaseModel


class LocationBase(BaseModel):
    name: str
    city: str
    state: str
    
class LocationCreateRequest(LocationBase):
    pass

class LocationResponse(LocationBase):
    id: int
    
    class ConfigDict:
        from_attributes = True