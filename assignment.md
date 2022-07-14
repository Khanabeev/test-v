# Vapaus backend assignment

Congratulations on making it this far!
This assignment is meant to test your backend coding skills. If you have any question about this assignment, feel free
to get in touch with us directly.

Good luck! :)

## Setup

To make you started faster, we are providing a simple docker setup composed of two containers, one for the PostgreSQL
database and one for the api. This should work has is, but please feel free to edit the docker configuration if you need
to.

To start the the containers you can do:

```shell session
docker compose up -d --build
```

To make sure everything is working properly you can go to: [http://localhost:8080/docs](http://localhost:8080/docs)
You should see this api documentation page saying something like “No operations defined in spec!”.

This project uses [Poetry](https://python-poetry.org/) to manage dependencies, to add a dependency simply do:

```shell session
poetry add <package name>
```

or to execute it from inside the docker container:

```shell session
docker exec <container name> poetry add <package name>
```

## Requirements

You’ll have to build a simple API using Python and [FastAPI](https://fastapi.tiangolo.com/). You’ll have to use
PostgreSQL for the database and either
[SQLModel](https://sqlmodel.tiangolo.com/) or [SQLAlchemy](https://www.sqlalchemy.org/) for the ORM.

The API you need to build will use the following two entities:

### Organization

An organization consist of the following attributes:

- name
- business id
- email

All these attributes are mandatory, the business id must be unique.

### Bike

A bike has the following attributes:

- organization (referring to the organization entity)
- brand
- model
- price
- serial number

Except for the model that is optional, all these attributes are mandatory. The serial number must be unique. The brand
is one of a fixed set of values: Canyon, Trek, Cannondale, Specialized, Giant, Orbea, Scott, Santa Cruz, Cervelo

You can find seed data in the data folder.

### API requirements

Please create the following endpoints for the bikes:

- create a bike
- read a bike
- update a bike

Additionally, we would like you to create endpoints for the organizations:

- read the list of bikes for a specific organization, with an optional filter on the brand
- return the average price of the bikes for a specific organization

## Evaluation criteria

Your assignment will be evaluated on the following criteria:

- Maintainability: most projects are meant to evolve and live for years
- Readability: the code is written once but read many times!
- Scalability: this project is quite small, but what happens when it gets bigger or if we have millions of rows in the
  DB?
- Ease of setup: are there instructions on how to set up the project? How long does it take?
- Some explanations of the choices you made (if there are any) are always a good idea :)
