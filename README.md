## Project Setup

Project used Python for programming, and a virtual environment to manage
dependencies.

1: Create Virtual Environment

    python3 -m venv .venv

2: Activate Virtual Environment

    source .venv/bin/activate 

3: Install Dependencies

    pip install -r requirements.txt


## Project Architecture

> This project was built focusing on scalability and separation.

## Clean Architecture

> The code adheres to clean architecture principles and separated
> between domain and data layers.\
> \
> **domain**: models, abstract managers, usecases\
> **data**: manager implementation

## Dependency Injection

> By using a `dependency injector` all services instantiated inside
> `AppContainer`. This ensures dependency flow decouples via interfaces.
> This would make the atchitecture more future proof and allow mock
> injection for testing.

## Modularized

## Source is modularized for separate distinct modules.

**src/core** 

Core components like (data repositories), utilities like logger, core module formatted log strings 

**src/di** 

Dependency injection container