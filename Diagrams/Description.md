
---

## Overview

This is an early Entity Relationship Diagram (ERD) for a charity/project management platform.

The system allows:

* Organisations to have users.
* Organisations to create projects.
* Projects to contain cohorts.
* Cohorts to contain members.
* Projects to track media coverage through media posts.

---

# Entities

## Organisation

Represents a charity, NGO, company, or initiative running projects.

### Fields

* Name

### Relationships

* One Organisation has many Users.
* One Organisation has many Projects.

---

## User

Represents a person who belongs to an organisation.

### Fields

* Name

### Relationships

* Each User belongs to one Organisation.

---

## Project

Represents an individual initiative or charity project.

### Fields

* Project Name
* Description
* Start Date
* End Date
* Budget
* Amount Spent
* Status

### Relationships

* Each Project belongs to one Organisation.
* A Project can have many Cohorts.
* A Project can have many Media Posts.

---

## Cohort

Represents a group of beneficiaries, participants, trainees, volunteers, etc., within a project.

### Fields

* Members (currently shown, though this may eventually become a calculated value)

### Relationships

* Each Cohort belongs to one Project.
* A Cohort contains many Cohort Members.

---

## Cohort Member

Represents an individual person within a cohort.

### Fields

* Name
* Gender

### Relationships

* Each Cohort Member belongs to one Cohort.

---

## Media Post

Represents media coverage associated with a project.

### Fields

* Type
* Platform
* Link
* Date

Examples:

* Newspaper article
* Facebook post
* Twitter/X post
* Instagram post
* YouTube video

### Relationships

* Each Media Post belongs to one Project.

---

# Relationship Summary

```text
Organisation
│
├── Users (many)
│
└── Projects (many)
      │
      ├── Cohorts (many)
      │      │
      │      └── Cohort Members (many)
      │
      └── Media Posts (many)
```

---

# Likely Django Models

If implemented in Django, the relationships would roughly be:

```text
Organisation
    ├── User
    └── Project
            ├── Cohort
            │       └── CohortMember
            └── MediaPost
```

Which translates to:

```python
Organisation
    ↓
Project (ForeignKey to Organisation)

Organisation
    ↓
User (ForeignKey to Organisation)

Project
    ↓
Cohort (ForeignKey to Project)

Cohort
    ↓
CohortMember (ForeignKey to Cohort)

Project
    ↓
MediaPost (ForeignKey to Project)
```

One thing I'd question before building it: should **Users belong to Organisations only**, or should Users also have permissions on Projects? Most project-management systems eventually need a many-to-many relationship between Users and Projects (e.g., project managers, contributors, viewers), so that's something worth thinking about early.
