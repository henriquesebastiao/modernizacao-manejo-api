from logging.config import fileConfig

from alembic import context

from app.models import (  # noqa
    animal,
    animal_weight,
    animal_weight_type,
    base,
    batch,
    batch_log,
    breed,
    employment,
    employment_position,
    farm,
    farmer,
    farmer_plan,
    user,
    user_type,
)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = base.Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    import os
    import re

    from sqlalchemy import create_engine

    url_tokens = {
        "DB_TYPE": os.getenv("DB_TYPE", ""),
        "DB_USER": os.getenv("DB_USER", ""),
        "DB_PASSWORD": os.getenv("DB_PASSWORD", ""),
        "DB_HOST": os.getenv("DB_HOST", ""),
        "DB_NAME": os.getenv("DB_NAME", "")
    }

    url = config.get_main_option("sqlalchemy.url")
    url = re.sub(r"\${(.+?)}", lambda m: url_tokens[m.group(1)], url)
    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
