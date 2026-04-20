from sqlalchemy.orm import Session
from ..schemas.categories import CategoryResponse
from ..repositories import categories as repository


class CategoryService:
    def __init__(self, db: Session):
        self.db = db

    def get_categories(self) -> list[CategoryResponse]:
        categories_db = repository.get_categories(self.db)

        return [CategoryResponse.model_validate(c) for c in categories_db]
