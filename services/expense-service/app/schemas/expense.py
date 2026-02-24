from pydantic import BaseModel

class ExpenseBase(BaseModel):
    title: str
    amount: float
    user_id: int


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    title: str | None = None
    amount: float | None = None


class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        from_attributes = True   
