# Connect Four AI

Algorithm that plays Connect Four as efficiently as possible.

## Documentation

[Specification document](https://github.com/minttugomez/connect4/blob/main/connect4/documentation/specification.md)

[Implementation document](https://github.com/minttugomez/connect4/blob/main/connect4/documentation/implementation.md)

[Testing document](https://github.com/minttugomez/connect4/blob/main/connect4/documentation/testing.md)

[User guide](https://github.com/minttugomez/connect4/blob/main/connect4/documentation/userGuide.md)

## Weekly reports

[Week 1](https://github.com/minttugomez/connect4/blob/main/connect4/documentation/weekly%20reports/week1.md)

[Week 2](https://github.com/minttugomez/connect4/blob/main/connect4/documentation/weekly%20reports/week2.md)

[Week 3](https://github.com/minttugomez/connect4/blob/main/connect4/documentation/weekly%20reports/week3.md)

[Week 4](https://github.com/minttugomez/connect4/blob/main/connect4/documentation/weekly%20reports/week4.md)

## Commands

### Installation

Install dependencies:

```bash
poetry install
```

Run the application:

```bash
poetry run invoke start
```

### Testing

Run tests:

```bash
poetry run invoke test
```

### Testikattavuus

Generate test coverage report:

```bash
poetry run invoke coverage-report
```

### Pylint

Run pylint check:

```bash
poetry run invoke lint
```