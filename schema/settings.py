from pydantic import BaseModel;
from typing import Optional;


class Settings(BaseModel):
    authjwt_secret_key: str = '681b12d4b533083050fef39b7521726380cd10a7bf06adf4a5edf07affbb6976';
