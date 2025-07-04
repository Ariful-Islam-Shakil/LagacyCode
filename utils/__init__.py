from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LogLevel(Enum):
    """Enum for logging levels."""
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

@dataclass
class Person:
    """Dataclass for a person."""
    name: str
    age: int
    occupation: str

def get_person(name: str) -> Optional[Person]:
    """
    Retrieves a person by name.

    Args:
        name (str): The name of the person to retrieve.

    Returns:
        Optional[Person]: The person object if found, otherwise None.
    """
    people = [
        Person("John", 30, "Engineer"),
        Person("Alice", 25, "Doctor"),
        Person("Bob", 40, "Lawyer"),
    ]
    for person in people:
        if person.name == name:
            return person
    return None

def get_people_by_occupation(occupation: str) -> List[Person]:
    """
    Retrieves people by occupation.

    Args:
        occupation (str): The occupation to filter by.

    Returns:
        List[Person]: A list of people with the specified occupation.
    """
    people = [
        Person("John", 30, "Engineer"),
        Person("Alice", 25, "Doctor"),
        Person("Bob", 40, "Lawyer"),
    ]
    return [person for person in people if person.occupation == occupation]

def get_people_by_age_range(min_age: int, max_age: int) -> List[Person]:
    """
    Retrieves people by age range.

    Args:
        min_age (int): The minimum age to filter by.
        max_age (int): The maximum age to filter by.

    Returns:
        List[Person]: A list of people within the specified age range.
    """
    people = [
        Person("John", 30, "Engineer"),
        Person("Alice", 25, "Doctor"),
        Person("Bob", 40, "Lawyer"),
    ]
    return [person for person in people if min_age <= person.age <= max_age]

def main():
    """Main function."""
    logger.info("Starting application...")
    person = get_person("John")
    if person:
        logger.info(f"Found person: {person.name}, {person.age}, {person.occupation}")
    else:
        logger.info("Person not found")
    people_by_occupation = get_people_by_occupation("Engineer")
    logger.info(f"People by occupation: {people_by_occupation}")
    people_by_age_range = get_people_by_age_range(25, 35)
    logger.info(f"People by age range: {people_by_age_range}")
    logger.info("Application finished.")

if __name__ == "__main__":
    main()