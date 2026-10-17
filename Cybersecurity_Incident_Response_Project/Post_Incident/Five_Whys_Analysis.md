# Five Whys Analysis

1. Why was there material account risk? Repeated unauthorized authentication attempts targeted multiple identities.
2. Why could attempts continue? Preventive rate/lockout controls did not stop the pattern early enough.
3. Why was credential-only risk meaningful? MFA coverage was incomplete in the scenario.
4. Why was escalation not earlier? Correlation rules did not sufficiently connect multi-account and success-after-failure behavior.
5. Why did these gaps coexist? Authentication hardening and monitoring had not yet been managed as an integrated control program.

Root cause: control maturity and integration, not a single isolated failure.
