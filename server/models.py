from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, DateTime

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False)
    updated_at = db.Column(DateTime, nullable=False)


# Assuming you have Flask app defined and configured somewhere

# Migration code using Alembic
# You need to run this migration script to apply the changes to your database
# Run the following commands in your terminal after writing the migration script:

# 1. Initialize Alembic (if not already done)
# alembic init migrations

# 2. Modify alembic.ini to point to your database URI

# 3. Generate the migration script
# alembic revision --autogenerate -m "create messages table"

# 4. Apply the migration to the database
# alembic upgrade head
