from pydantic import BaseModel

class TransactionInput(BaseModel):
    amount: float
    vehicle_type: int
    lane_type: int
    time_of_day: int
    # exactly the same features as training