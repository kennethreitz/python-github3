# Labels API

## List all Labels for this Repository

### GET `/repos/:user/:repo/labels.json`

## Create a Label

### POST `/repos/:user/:repo/labels.json`

### Input

    {
      name: String,
      color: String,
    }

## Get a single Label

### GET `/repos/:user/:repo/labels/:id.json`

## Update a Label

### PUT `/repos/:user/:repo/labels/:id.json`

### Input

    {
      name: String,
      color: String,
    }

## Delete a label

### DELETE `/repos/:user/:repo/labels/:id.json`

## List labels on the Issue

### GET `/repos/:user/:repo/issues/:id/labels.json`

## Add a Label to an Issue

### POST `/repos/:user/:repo/issues/:id/labels.json`

### Input

    [{
      name: String,
     }, ...]

## Remove a Label from an Issue

### DELETE `/repos/:user/:repo/issues/:id/labels/:id.json`

## Replace all Labels for an Issue

### PUT `/repos/:user/:repo/issues/:id/labels.json`

### Input

    [{
      name: String,
     }, ...]

## Remove all Labels from an Issue

### DELETE `/repos/:user/:repo/issues/:id/labels.json`

## Get Labels for every Issue in a Milestone

### GET `/repos/:user/:repo/milestones/:id/labels.json`
