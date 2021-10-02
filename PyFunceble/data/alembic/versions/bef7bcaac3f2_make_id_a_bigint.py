"""Make id a bigint.

Revision ID: bef7bcaac3f2
Revises: 3a4c55a9320d
Create Date: 2020-12-16 19:09:41.212679

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# pylint: skip-file

# revision identifiers, used by Alembic.
revision = "bef7bcaac3f2"
down_revision = "3a4c55a9320d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "pyfunceble_continue",
        "id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_inactive",
        "id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_whois_record",
        "id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        autoincrement=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "pyfunceble_whois_record",
        "id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_inactive",
        "id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_continue",
        "id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        autoincrement=True,
    )
    # ### end Alembic commands ###
