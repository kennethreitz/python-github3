# Issues API

## List issues for this Repository

### GET `/repos/:user/:repo/issues.json`

* `?milestone` = (Fixnum)
* `?sort` = (String)
* `?direction` = (String)
* `?state` = open, closed, default: open
* `?assignee` = (String)
* `?mentioned` = (String)
* `?labels` = (String)


## Create an Issue

### POST `/repos/:user/:repo/issues.json`

### Input

    {
      title: String,
      body: String,
      assignee: String,
      milestone: Fixnum,
    }

## Get a single Issue

### GET `/repos/:user/:repo/issues/:id.json`

## Edit an Issue

### PUT `/repos/:user/:repo/issues/:id.json`

### Input

    {
      title: String,
      body: String,
      assignee: String,
      milestone: Fixnum,
    }

## Delete an Issue

### DELETE `/repos/:user/:repo/issues/:id.json`
