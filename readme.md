# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup

**[TODO 05/01/2018 @vanessa-cooper]:** _It's been a while since anyone ran a fresh copy of this repo. I think it's worth documenting the steps needed to install and run the repo on a new machine?_

### Local Environment Setup
Step 1: [Install Docker](https://docs.docker.com/get-docker/) with the WSL2 configuration tho Hyper-V can be an alternative.
Step 2: [Install Docker-Compose](https://docs.docker.com/compose/install/)
Step 3: Use command on the Anything-Market codebase `docker-compose up` to create a development server and setup frontend and backend environment.
