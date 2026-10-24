import logging

from taskich.cli import TaskichCLI
from taskich.logging_config import setup_logging
from taskich.mock_data import (
    create_demo_projects,
    create_demo_tasks,
    create_demo_users,
)
from taskich.repository import (
    InMemoryFilterRepository,
    InMemoryProjectRepository,
    InMemoryTaskRepository,
    InMemoryUserRepository,
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Запускает консольное приложение Taskich."""

    setup_logging()
    logger.info("Приложение запущено")

    users = InMemoryUserRepository()
    projects = InMemoryProjectRepository()
    tasks = InMemoryTaskRepository()

    for user in create_demo_users():
        users.add(user)

    for project in create_demo_projects():
        projects.add(project)

    for task in create_demo_tasks():
        tasks.add(task)

    TaskichCLI(
        tasks=tasks,
        users=users,
        projects=projects,
        filters=InMemoryFilterRepository(),
    ).run()

    logger.info("Приложение остановлено")


if __name__ == "__main__":
    main()
