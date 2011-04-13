# Milestones API

## List Milestones for an Issue

### GET `/repos/:user/:repo/milestones.json`

* `?sort` = (String)
* `?direction` = (String)
* `?state` = open, closed, default: open


## Create a Milestone

### POST `/repos/:user/:repo/milestones.json`

### Input

    {
      title: String,
      state: String,
      description: String,
      due_on: Time,
    }

## Get a single Milestone

### GET `/repos/:user/:repo/milestones/:id.json`

## Update a Milestone

### PUT `/repos/:user/:repo/milestones/:id.json`

### Input

    {
      title: String,
      state: String,
      description: String,
      due_on: Time,
    }

## Delete a Milestone

### DELETE `/repos/:user/:repo/milestones/:id.json`
