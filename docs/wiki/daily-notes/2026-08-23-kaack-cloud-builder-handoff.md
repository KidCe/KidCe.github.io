# KAACK Cloud Builder — Project Handoff

## Project Goal

Build an unofficial, clearly independent web-based cloud builder for KAACK / alternative Betaflight firmware builds.

The main goal is to recreate an experience close to the familiar Betaflight Configurator Cloud Build workflow:

1. Open a simple website.
2. Select the desired KAACK / firmware version.
3. Select the flight-controller target.
4. Select optional firmware features/packages, for example:
   - GPS
   - Analog OSD
   - HD / digital OSD
   - other Betaflight build options
5. Click **Build**.
6. Receive a ready-to-flash `.hex` firmware file.

Users should **not need to interact with GitHub Actions, Docker, compilers, toolchains, deployment systems, or command-line tools**.

The project should make it very obvious that this is an **unofficial third-party service** and is not the official Betaflight Cloud Build service.

---

## Initial Use Case

The first version does not need to support a huge public user base.

Initial audience:

- Me
- Friends
- Small racing community
- Mostly similar flight-controller hardware
- Relatively small number of common firmware configurations

This makes aggressive caching particularly attractive because many users will probably request identical builds.

The MVP should already have the final basic UX rather than requiring users to manually trigger GitHub workflows.

---

## Proposed MVP Architecture

### Frontend

A small web application provides the Cloud Build-style interface.

Potential hosting:

- GitHub Pages
- Cloudflare Pages
- VPS-hosted static site

The frontend itself does not compile firmware.

It collects the desired build configuration and submits a build request to the backend.

Example conceptual request:

```json
{
  "firmware": "KAACK",
  "version": "x.y.z",
  "target": "FLIGHT_CONTROLLER_TARGET",
  "features": [
    "GPS",
    "OSD",
    "HD_OSD"
  ]
}
```

---

## Backend / Orchestration Layer

A small backend receives the build request.

Possible implementations:

- Cloudflare Worker
- Small VPS
- Other serverless function

For the MVP, a cheap VPS is attractive because it can also be reused for future projects.

The backend does **not necessarily need to compile firmware itself**.

Its main responsibilities are:

1. Validate the requested firmware configuration.
2. Normalize the configuration.
3. Generate a deterministic cache key.
4. Check whether this exact firmware has already been built.
5. Return the existing `.hex` immediately if available.
6. If not cached, trigger a new build.
7. Track build status.
8. Make the finished firmware available to the user.

---

## Build Pipeline

GitHub Actions can initially provide the actual build infrastructure.

Conceptual flow:

```text
User
  ↓
Web UI
  ↓
Backend / Worker
  ↓
Generate configuration hash
  ↓
Check firmware cache
  ↓
┌─────────────────────┐
│ Cached build exists │
└─────────────────────┘
          ↓ YES
Return existing HEX

          ↓ NO
Trigger GitHub Action
          ↓
Build firmware
          ↓
Store HEX permanently
          ↓
Return HEX to user
```

GitHub Actions should ideally build inside a controlled Docker environment so the compiler/toolchain is reproducible.

---

## Build Cache

Caching should be a core part of the architecture rather than an afterthought.

A deterministic cache key could conceptually be generated from:

```text
firmware fork
+
firmware version / commit
+
target
+
selected features
+
build-system version
```

For example:

```text
SHA256(
  kaack
  + version
  + target
  + sorted(features)
  + builder_version
)
```

If two users request exactly the same configuration, the second user receives the existing firmware instead of triggering another compilation.

This is particularly useful for the racing community because many users use identical or very similar hardware.

---

## GitHub Artifacts vs Permanent Firmware Storage

GitHub Actions can upload build outputs as **Artifacts**.

Artifacts are files produced by a workflow run, such as:

```text
firmware.hex
```

However, GitHub Actions artifacts are primarily intended as temporary CI/CD outputs and have retention limits.

Therefore, they should not be the primary long-term firmware cache.

Instead, completed firmware could be copied to persistent object storage.

Potential storage options:

- Cloudflare R2
- Amazon S3
- S3-compatible storage
- VPS storage for the very early MVP

Conceptually:

```text
firmware/
  <configuration-hash>.hex
```

Metadata should ideally be stored alongside it:

```text
firmware/
  <configuration-hash>.hex
  <configuration-hash>.json
```

The metadata could contain:

```json
{
  "fork": "KAACK",
  "version": "...",
  "commit": "...",
  "target": "...",
  "features": [],
  "builderVersion": "...",
  "builtAt": "..."
}
```

This provides reproducibility and makes it possible to determine exactly what a cached firmware file contains.

---

## Cloudflare Workers vs VPS

### Cloudflare Worker

Useful as a lightweight API/orchestration layer.

Advantages:

- No server administration
- Easy HTTPS/API endpoint
- Scales automatically
- Good integration with Cloudflare R2
- Very inexpensive for low request volumes

It would primarily act as glue between:

```text
Frontend ↔ GitHub Actions ↔ Firmware Storage
```

It would **not normally perform the actual firmware compilation**.

### VPS

A cheap VPS, for example around €3/month, offers substantially more general-purpose flexibility.

It could host:

- Backend API
- Multiple websites
- Authentication
- Database
- Build dashboard
- Other future tools
- Potentially build workers later

For a small private project, this may be attractive because the server can be reused.

However, running firmware compilation directly on one tiny VPS could eventually become a bottleneck.

---

## Recommended MVP

A reasonable first architecture is:

```text
Static Web UI
      ↓
Small backend
      ↓
Firmware cache lookup
      ↓
GitHub Actions
      ↓
Persistent firmware storage
```

Possible concrete implementation:

```text
Frontend:
GitHub Pages

Backend:
Cheap VPS or Cloudflare Worker

Build system:
GitHub Actions + Docker

Source:
KAACK GitHub repository / selected fork

Firmware cache:
Initially VPS storage
or Cloudflare R2

Build metadata:
JSON files or small database
```

For a very small trusted user group, authentication can initially be simple.

The public-facing URL does not need to be broadly advertised, but relying solely on an obscure URL should not be considered strong security if the service later becomes public.

---

## Scaling Path

### Phase 1 — Private MVP

Small number of users.

```text
UI
↓
Backend
↓
GitHub Actions
↓
Cache
```

Optimize for development speed.

### Phase 2 — Community Tool

Add:

- proper authentication or access control
- rate limiting
- build queue
- better build-status UI
- logging
- stronger input validation
- firmware provenance/metadata
- cache management
- monitoring

GitHub Actions can potentially remain the build workers.

### Phase 3 — Larger Public Service

If thousands of people start using the service, GitHub Actions may no longer be the ideal primary build infrastructure.

Move toward:

```text
Frontend
↓
API
↓
Build Queue
↓
Autoscaling Build Workers
↓
Object Storage
```

Workers could run using:

- self-hosted GitHub runners
- containers
- Kubernetes
- cloud compute
- dedicated build servers

At that point, builds become jobs submitted to a queue rather than individual web requests directly triggering compilation.

---

## Important Optimization: Prebuilding Common Configurations

Because the racing community uses a relatively small number of common targets/configurations, popular builds could be generated in advance.

For example, whenever a new KAACK release is published:

```text
New KAACK version
       ↓
Build common FC targets
       ↓
Build common feature combinations
       ↓
Store HEX files
```

Users requesting common configurations would then effectively get instant downloads.

Only unusual configurations would require an on-demand build.

This could dramatically reduce:

- GitHub Actions usage
- compilation time
- server costs
- user waiting time

---

## Desired User Experience

The user should ideally experience:

```text
Select version
Select FC
Select features
Click BUILD
```

Then either:

```text
Firmware already cached
→ near-instant download
```

or:

```text
Not cached
→ "Building firmware..."
→ progress/status
→ download
```

The underlying infrastructure should remain invisible.

Users should never need to understand:

- GitHub Actions
- Docker
- compiler setup
- repositories
- CI/CD
- build artifacts
- deployment

---

## Branding / Disclaimer

The website should clearly communicate that it is independent from the official Betaflight project.

Something along the lines of:

> Unofficial community firmware builder.  
> Not affiliated with or supported by the Betaflight project.  
> Firmware generated by this service may contain third-party or experimental modifications. Use at your own risk.

Exact wording should be reviewed before a public release.

---

## Open Technical Questions

Before implementation, investigate:

- Exact KAACK repository/fork structure
- How KAACK currently builds firmware
- Which Betaflight build options need to be exposed
- How the official Betaflight Cloud Build system represents build options
- Whether parts of the existing Betaflight Configurator UI can reasonably be reused
- Betaflight/KAACK licensing requirements
- GitHub Actions usage limits and costs
- GitHub API authentication requirements
- Best way to trigger parameterized builds
- Best persistent firmware storage
- Cache invalidation strategy
- How to cryptographically identify source commit + build configuration
- Whether builds should be signed or checksummed
- Whether GitHub Actions' existing caching mechanisms can reduce compilation time further

---

## Next Implementation Step

Before writing the frontend, prototype **one complete build through GitHub Actions**.

The first milestone should be:

```text
GitHub workflow_dispatch
      ↓
Choose:
- firmware version
- FC target
- features
      ↓
Build KAACK
      ↓
Produce firmware.hex
```

Once this works reliably, wrap it behind the backend API.

After that, build the Cloud Build-style frontend on top.

This separates the hardest technical question — **"Can we reliably produce the requested firmware automatically?"** — from the UI and infrastructure work.
