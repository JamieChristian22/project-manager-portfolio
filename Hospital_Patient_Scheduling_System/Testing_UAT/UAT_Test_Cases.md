# Scheduling UAT catalogue

The original eight cases were marked Pass in the fictional scenario. Those statuses are retained below as **reported scenario results**, not independently rerun tests. The detailed procedures make the cases executable when a test environment is available.

| ID | Setup and steps | Expected result | Original result | Evidence to retain |
|---|---|---|---|---|
| UAT-01 | Select an available provider and permitted room; submit one appointment | One confirmed booking with correct provider, room, duration and audit entry | Pass | Booking ID, request/response and audit record |
| UAT-02 | Seed a confirmed provider booking; request the same interval | Controlled rejection; existing appointment remains unchanged | Pass | Conflict response and before/after booking query |
| UAT-03 | Mark the room unavailable; attempt a booking requiring that room | Booking prevented with an actionable reason | Pass | Room calendar and rejected request |
| UAT-04 | Cancel a confirmed appointment; inspect provider and room calendars | Slot released once; cancellation recorded; duplicate cancellation is safe | Pass | Calendar state and cancellation audit |
| UAT-05 | Add three eligible waitlist entries with different priorities | Approved priority and tie-break rules preserved | Pass | Ordered queue and rules version |
| UAT-06 | Attempt urgent override as unauthorized and authorized roles | Unauthorized attempt denied; authorized action requires documented approval | Pass | Role context, denial and approval audit |
| UAT-07 | Attempt to view another department using restricted role | Forbidden records not returned; access event logged | Pass | Permission matrix, request and audit reference |
| UAT-08 | Mark a missed appointment as no-show; refresh reporting | One status update and correct reporting classification | Pass | Appointment history and report row |

## Additional acceptance coverage

| ID | Failure path | Acceptance criterion | Execution status |
|---|---|---|---|
| UAT-09 | Two concurrent requests for the same slot | Exactly one succeeds; no duplicate active provider or room allocation | Not run |
| UAT-10 | Request spans a provider break or room buffer | Entire requested interval validated, not just start time | Not run |
| UAT-11 | Reschedule fails midway | Original booking retained or transaction fully committed; no orphan slot | Not run |
| UAT-12 | Reminder service unavailable | Booking remains valid; retry tracked without duplicate reminders | Not run |
| UAT-13 | Duplicate submission after timeout | Same idempotency key cannot create a second appointment | Not run |
| UAT-14 | Downtime entries reconciled after recovery | Each entry has a unique disposition; conflicts routed to an owner | Not run |
| UAT-15 | Booking crosses daylight-saving transition | Stored instant and displayed local time remain consistent with approved rules | Not run |
| UAT-16 | User loses access during an active session | Subsequent restricted actions fail according to access policy | Not run |

QA owns execution; scheduling operations owns business acceptance; the privacy/access owner reviews permission evidence. See [the acceptance record](UAT_Signoff.md) for missing original evidence and gate conditions.
