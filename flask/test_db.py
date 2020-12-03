#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
from sqlalchemy import create_engine

db_string = "postgres://jordan:1234@localhost/postgres"
db = create_engine(db_string)
res = db.execute("select * from user_info;")

for r in res:
    print(r)
