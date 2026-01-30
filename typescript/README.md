# @pluralsh/console-client

TypeScript REST client for the [Plural Console](https://plural.sh) API. Generated from the OpenAPI spec using [@hey-api/openapi-ts](https://heyapi.dev/openapi-ts/).

## Installation

```bash
yarn add @pluralsh/console-client
# or
pnpm add @pluralsh/console-client
# or
npm install @pluralsh/console-client
```

## Usage

```typescript
import {
  client,
  listClusters,
  getCluster,
  type Cluster,
} from '@pluralsh/console-client';

// Configure the API base URL (default is https://localhost/)
client.setConfig({
  baseUrl: 'https://your-console.example.com',
  // Optional: pass custom headers (e.g. for auth)
  headers: {
    Authorization: 'Bearer YOUR_TOKEN',
  },
});

// Call API methods
const { data } = await listClusters();
const cluster = await getCluster({ path: { id: 'cluster-id' } });
```

All API operations and types are exported from the package. Use your editor’s autocomplete to discover available methods and types.

## Regenerating the client

When `openapi.json` in the repo root changes, regenerate the client:

```bash
cd typescript
yarn generate
yarn build
```

## Requirements

- Node.js 20+
- TypeScript 5.x (when using in a TypeScript project)
