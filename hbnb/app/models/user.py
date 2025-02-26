#!/usr/bin/env python3


import uuid
from datetime import datetime
from .base_model import BaseModel


class User(BaseModel):
    def __init__(self, id=None, first_name='', last_name='', email='', is_admin=False, created_at=None, updated_at=None):
        super().__init__()
        self.id = id if id is not None else str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at if updated_at is not None else datetime.now()
