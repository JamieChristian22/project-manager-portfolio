# Data Model

## Core Entities
Patient, Appointment, Provider, Department, Room, Appointment Type, Availability Template, Waitlist Entry, Notification, User, Role, Audit Event.

## Key Relationships
Appointment links patient + provider + department + room + appointment type. Waitlist references requested service and priority. Audit events reference user and action.
