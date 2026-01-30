/**
 * Minimal example: call the Console API /me endpoint.
 *
 * Prerequisites:
 *   1. From repo root: cd typescript && yarn build
 *   2. Set CONSOLE_URL and CONSOLE_TOKEN (env vars or .env file in this directory)
 */

import "dotenv/config";
import { client, me } from "@pluralsh/console-client";

const baseUrl =
  process.env.CONSOLE_URL ?? "https://console.plrl-dev-aws.onplural.sh";
const token = process.env.CONSOLE_TOKEN;

console.log("Base URL:", baseUrl);
console.log("Token:", token);

client.setConfig({
  baseUrl,
  ...(token && {
    headers: new Headers({ Authorization: `Bearer ${token}` }),
  }),
});

const { data, error } = await me();
console.log("Current user:", data);
console.log("Error:", error);
